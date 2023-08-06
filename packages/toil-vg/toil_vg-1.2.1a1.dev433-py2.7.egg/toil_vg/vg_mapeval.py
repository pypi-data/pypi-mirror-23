#!/usr/bin/env python2.7
"""
vg_mapeval.py: Compare alignment positions from gam or bam to a truth set
that was created with vg sim --gam

"""
from __future__ import print_function
import argparse, sys, os, os.path, errno, random, subprocess, shutil, itertools, glob, tarfile
import doctest, re, json, collections, time, timeit
import logging, logging.handlers, SocketServer, struct, socket, threading
import string, math
import urlparse
import getpass
import pdb
import gzip
import logging
import copy
from collections import Counter

from math import ceil
from subprocess import Popen, PIPE

try:
    import numpy as np
    from sklearn.metrics import roc_auc_score, average_precision_score, r2_score
    have_sklearn = True
except:
    have_sklearn = False

import tsv

from toil.common import Toil
from toil.job import Job
from toil.realtimeLogger import RealtimeLogger
from toil_vg.vg_common import *
from toil_vg.vg_map import *
from toil_vg.vg_index import *

logger = logging.getLogger(__name__)

def mapeval_subparser(parser):
    """
    Create a subparser for mapeval.  Should pass in results of subparsers.add_parser()
    """

    # Add the Toil options so the job store is the first argument
    Job.Runner.addToilOptions(parser)
    
    # General options
    parser.add_argument('out_store',
                        help='output store.  All output written here. Path specified using same syntax as toil jobStore')
    parser.add_argument('truth', default=None,
                        help='list of true positions of reads as output by toil-vg sim')        
    parser.add_argument('--gams', nargs='+', default=[],
                        help='aligned reads to compare to truth.  specify xg index locations with --index-bases')
    parser.add_argument("--index-bases", nargs='+', default=[],
                        help='use in place of gams to perform alignment.  will expect '
                        '<index-base>.gcsa, <index-base>.lcb and <index-base>.xg to exist')
    parser.add_argument('--vg-graphs', nargs='+', default=[],
                        help='vg graphs to use in place of gams or indexes.  indexes'
                        ' will be built as required')
    parser.add_argument('--gam-names', nargs='+', default=[],
                        help='a name for each gam passed in --gams/graphs/index-bases')
    parser.add_argument('--bams', nargs='+', default=[],
                        help='aligned reads to compare to truth in BAM format')
    parser.add_argument('--bam-names', nargs='+', default=[],
                        help='a name for each bam passed in with --bams')
    parser.add_argument('--pe-bams', nargs='+', default=[],
                        help='paired end aligned reads t compare to truth in BAM format')
    parser.add_argument('--pe-bam-names', nargs='+', default=[],
                        help='a name for each bam passed in with --pe-bams')
    parser.add_argument('--vg-paired', action='store_true',
                        help='if running vg map, do vg map -i as well')
    
    parser.add_argument('--mapeval-threshold', type=int, default=100,
                        help='distance between alignment and true position to be called correct')

    parser.add_argument('--bwa', action='store_true',
                        help='run bwa mem on the reads, and add to comparison')
    parser.add_argument('--bwa-paired', action='store_true',
                        help='run bwa mem paired end as well')
    parser.add_argument('--fasta', default=None,
                        help='fasta sequence file (required for bwa)')
    parser.add_argument('--gam-reads', default=None,
                        help='reads in GAM format (required for bwa)')

    parser.add_argument('--bwa-opts', type=str,
                        help='arguments for bwa mem (wrapped in \"\").')
    
    # We can compare all the scores against those from a particular GAM, if asked.
    parser.add_argument('--compare-gam-scores', default=None,
                        help='compare scores against those in the given named GAM')
    
    # Add mapping options
    map_parse_args(parser)

    # Add common options shared with everybody
    add_common_vg_parse_args(parser)

    # Add common docker options
    add_container_tool_parse_args(parser)
    
def parse_int(value):
    """
    Parse an int, interpreting an empty string as 0.
    """
    
    return int(value) if value.strip() != '' else 0

def run_bwa_index(job, options, gam_file_id, fasta_file_id, bwa_index_ids):
    """
    Make a bwa index for a fast sequence if not given in input. then run bwa mem
    """
    if not bwa_index_ids:
        bwa_index_ids = dict()
        work_dir = job.fileStore.getLocalTempDir()
        fasta_file = os.path.join(work_dir, os.path.basename(options.fasta))
        read_from_store(job, options, fasta_file_id, fasta_file)
        cmd = ['bwa', 'index', os.path.basename(fasta_file)]
        options.drunner.call(job, cmd, work_dir = work_dir)
        for idx_file in glob.glob('{}.*'.format(fasta_file)):
            bwa_index_ids[idx_file[len(fasta_file):]] = write_to_store(job, options, idx_file)

    bwa_stats_file_id = None
    bwa_pair_stats_file_id = None
                    
    if options.bwa:
        bwa_stats_file_id = job.addChildJobFn(run_bwa_mem, options, gam_file_id, bwa_index_ids, False,
                                            cores=options.alignment_cores, memory=options.alignment_mem,
                                            disk=options.alignment_disk).rv()
    if options.bwa_paired:
        bwa_pair_stats_file_id = job.addChildJobFn(run_bwa_mem, options, gam_file_id, bwa_index_ids, True,
                                                 cores=options.alignment_cores, memory=options.alignment_mem,
                                                 disk=options.alignment_disk).rv()

    return bwa_stats_file_id, bwa_pair_stats_file_id

    
def run_bwa_mem(job, options, gam_file_id, bwa_index_ids, paired_mode):
    """ run bwa-mem on reads in a gam.  optionally run in paired mode
    return id of bam file
    """

    work_dir = job.fileStore.getLocalTempDir()

    # read the gam file
    gam_file = os.path.join(work_dir, os.path.basename(options.gam_input_reads))
    read_from_store(job, options, gam_file_id, gam_file)

    # and the index files
    fasta_file = os.path.join(work_dir, os.path.basename(options.fasta))
    for suf, idx_id in bwa_index_ids.items():
        read_from_store(job, options, idx_id, '{}{}'.format(fasta_file, suf))

    # output positions file
    bam_file = os.path.join(work_dir, 'bwa-mem')
    if paired_mode:
        bam_file += '-pe'
    bam_file += '.bam'
    
    # if we're paired, must make some split files
    if paired_mode:

        # convert to json (todo: have docker image that can do vg and jq)
        json_file = gam_file + '.json'
        cmd = ['vg', 'view', '-a', os.path.basename(gam_file)]
        with open(json_file, 'w') as out_json:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_json)

        sim_fq_files = [None, os.path.join(work_dir, 'sim_1.fq.gz'),
                        os.path.join(work_dir, 'sim_2.fq.gz')]

        # make a fastq for each end of pair
        for i in [1, 2]:
            # extract paired end with jq
            cmd = ['jq', '-cr', 'select(.name | test("_{}$"))'.format(i),
                   os.path.basename(json_file)]
            end_file = json_file + '.{}'.format(i)
            with open(end_file, 'w') as end_out:
                options.drunner.call(job, cmd, work_dir = work_dir, outfile = end_out)

            cmd = [['vg', 'view', '-JaG', os.path.basename(end_file)]]
            cmd.append(['vg', 'view', '-X', '-'])
            cmd.append(['sed', 's/_{}$//'.format(i)])
            cmd.append(['gzip'])

            with open(sim_fq_files[i], 'w') as sim_out:
                options.drunner.call(job, cmd, work_dir = work_dir, outfile = sim_out)

            os.remove(end_file)

        # run bwa-mem on the paired end input
        cmd = ['bwa', 'mem', '-t', str(options.alignment_cores), os.path.basename(fasta_file),
                os.path.basename(sim_fq_files[1]), os.path.basename(sim_fq_files[2])] + options.bwa_opts        
        with open(bam_file + '.sam', 'w') as out_sam:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_sam)

        # separate samtools for docker (todo find image with both)
        # 2304 = get rid of 256 (secondary) + 2048 (supplementary)        
        cmd = ['samtools', 'view', '-1', '-F', '2304', os.path.basename(bam_file + '.sam')]
        with open(bam_file, 'w') as out_bam:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_bam)

    # single end
    else:

        # extract reads from gam.  as above, need to have single docker container (which shouldn't be
        # a big deal) to run all these chained command and avoid huge files on disk
        extracted_reads_file = os.path.join(work_dir, 'extracted_reads')
        cmd = ['vg', 'view', '-X', os.path.basename(gam_file)]
        with open(extracted_reads_file, 'w') as out_ext:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_ext)

        # run bwa-mem on single end input
        cmd = ['bwa', 'mem', '-t', str(options.alignment_cores), os.path.basename(fasta_file),
                os.path.basename(extracted_reads_file)] + options.bwa_opts

        with open(bam_file + '.sam', 'w') as out_sam:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_sam)

        # separate samtools for docker (todo find image with both)
        # 2304 = get rid of 256 (secondary) + 2048 (supplementary)
        cmd = ['samtools', 'view', '-1', '-F', '2304', os.path.basename(bam_file + '.sam')]
        with open(bam_file, 'w') as out_bam:
            options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_bam) 

    # return our id for the output bam file
    bam_file_id = write_to_store(job, options, bam_file)

    return bam_file_id

def extract_bam_read_stats(job, options, name, bam_file_id, paired):
    """
    extract positions, scores, and MAPQs from bam, return id of read stats file
    (lots of duplicated code with vg_sim, should merge?)
    
    Produces a read stats TSV of the format:
    read name, contig aligned to, alignment position, score, MAPQ
    
    TODO: Currently scores are not extracted and a score of 0 is always
    returned.

    """

    work_dir = job.fileStore.getLocalTempDir()

    # download input
    bam_file = os.path.join(work_dir, name)
    read_from_store(job, options, bam_file_id, bam_file)

    out_pos_file = bam_file + '.tsv'

    cmd = [['samtools', 'view', os.path.basename(bam_file)]]
    cmd.append(['grep', '-v', '^@'])
    if paired:
        # Now we use inline perl to parse the SAM flags and synthesize TSV
        # TODO: will need to switch to something more powerful to parse the score out of the AS tag. For now score everything as 0.
        # TODO: why _ and not / as the read name vs end number delimiter?
        cmd.append(['perl', '-ne', '@val = split("\t", $_); print @val[0] . "_" . (@val[1] & 64 ? "1" : @val[1] & 128 ? "2" : "?"), "\t" . @val[2] . "\t" . @val[3] . "\t0\t" . @val[4] . "\n";'])
    else:
        # No flags to parse since there's no end pairing and read names are correct.
        # Use inline perl again and insert a fake 0 score column
        cmd.append(['perl', '-ne', '@val = split("\t", $_); print @val[0] . "\t" . @val[2] . "\t" . @val[3] . "\t0\t" . @val[4] . "\n";'])
    cmd.append(['sort'])
    
    with open(out_pos_file, 'w') as out_pos:
        options.drunner.call(job, cmd, work_dir = work_dir, outfile = out_pos)

    stats_file_id = write_to_store(job, options, out_pos_file)
    return stats_file_id

    
def extract_gam_read_stats(job, options, xg_file_id, name, gam_file_id):
    """
    extract positions, scores, and MAPQs for reads from gam, return id of
    read stats file
    
    Produces a read stats TSV of the format:
    read name, contig aligned to, alignment position, score, MAPQ

    """

    work_dir = job.fileStore.getLocalTempDir()

    # download input
    xg_file = os.path.join(work_dir, '{}.xg'.format(name))
    read_from_store(job, options, xg_file_id, xg_file)
    gam_file = os.path.join(work_dir, name)
    read_from_store(job, options, gam_file_id, gam_file)

    out_pos_file = gam_file + '.tsv'
                           
    # go through intermediate json file until docker worked out
    gam_annot_json = gam_file + '.json'
    cmd = [['vg', 'annotate', '-p', '-a', os.path.basename(gam_file), '-x', os.path.basename(xg_file)]]
    cmd.append(['vg', 'view', '-aj', '-'])
    with open(gam_annot_json, 'w') as output_annot_json:
        options.drunner.call(job, cmd, work_dir = work_dir, outfile=output_annot_json)

    # turn the annotated gam json into truth positions, as separate command since
    # we're going to use a different docker container.  (Note, would be nice to
    # avoid writing the json to disk)        
    jq_cmd = [['jq', '-c', '-r', '[.name, .refpos[0].name, .refpos[0].offset, .score,'
               'if .mapping_quality == null then 0 else .mapping_quality end ] | @tsv',
               os.path.basename(gam_annot_json)]]
    jq_cmd.append(['sed', 's/null/0/g'])

    with open(out_pos_file + '.unsorted', 'w') as out_pos:
        options.drunner.call(job, jq_cmd, work_dir = work_dir, outfile=out_pos)

    # get rid of that big json asap
    os.remove(gam_annot_json)

    # sort the read stats file (not piping due to memory fears)
    sort_cmd = ['sort', os.path.basename(out_pos_file) + '.unsorted']
    with open(out_pos_file, 'w') as out_pos:
        options.drunner.call(job, sort_cmd, work_dir = work_dir, outfile = out_pos)

    # Make sure each line has all columns
    RealtimeLogger.info("Make sure all lines are full length")
    options.drunner.call(job, ['awk', '!length($5)',  os.path.basename(out_pos_file)], work_dir = work_dir)

    out_stats_file_id = write_to_store(job, options, out_pos_file)
    return out_stats_file_id
    
def compare_positions(job, options, truth_file_id, name, stats_file_id):
    """
    this is essentially pos_compare.py from vg/scripts
    return output file id.
    
    Compares positions from two TSV files. The truth has the format:
    read name, contig simulated from, true position
    
    And the file under test is a read stats TSV with the format:
    read name, contig aligned to, alignment position, alignment score, MAPQ
    
    Produces a CSV (NOT TSV) of the form:
    read name, correctness flag (0/1), MAPQ
    """
    work_dir = job.fileStore.getLocalTempDir()

    true_read_stats_file = os.path.join(work_dir, 'true.tsv')
    read_from_store(job, options, truth_file_id, true_read_stats_file)
    test_read_stats_file = os.path.join(work_dir, name + '.tsv')
    read_from_store(job, options, stats_file_id, test_read_stats_file)

    out_file = os.path.join(work_dir, name + '.compare.positions')

    with open(true_read_stats_file) as truth, open(test_read_stats_file) as test, \
         open(out_file, 'w') as out:
        line_no = 0
        for true_fields, test_fields in itertools.izip(tsv.TsvReader(truth), tsv.TsvReader(test)):
            # Zip everything up and assume that the reads correspond
            line_no += 1
            # every input has a true position
            true_read_name = true_fields[0]
            if len(true_fields) != 3 or len(test_fields) != 5:
                # With the new TSV reader, the files should always have the
                # correct field counts. Some fields just might be empty.
                raise RuntimeError('Incorrect field counts on line {} for {}: {} and {}'.format(
                    line_no, name, true_fields, test_fields))
            
            true_chr = true_fields[1]
            true_pos = parse_int(true_fields[2])
            aln_read_name = test_fields[0]
            if aln_read_name != true_read_name:
                raise RuntimeError('Mismatch on line {} of {} and {}.  Read names differ: {} != {}'.format(
                    line_no, true_read_stats_file, test_read_stats_file, true_read_name, aln_read_name))
            aln_chr = test_fields[1]
            aln_pos = parse_int(test_fields[2])
            # Skip over score field
            aln_mapq = parse_int(test_fields[4])
            aln_correct = 1 if aln_chr == true_chr and abs(true_pos - aln_pos) < options.mapeval_threshold else 0

            out.write('{}, {}, {}\n'.format(aln_read_name, aln_correct, aln_mapq))
        
        # make sure same length
        has_next = False
        try:
            iter(truth).next()
            has_next = True
        except:
            pass
        try:
            iter(test).next()
            has_next = True
        except:
            pass
        if has_next:
            raise RuntimeError('read stats files have different lengths')
        
    out_file_id = write_to_store(job, options, out_file)
    return out_file_id
    
def compare_scores(job, options, baseline_file_id, name, score_file_id):
    """
    Compares scores from TSV files. The baseline and file under test both have
    the format:
    read name, contig aligned to, alignment position, alignment score, MAPQ
    
    Produces a CSV (NOT TSV) of the form:
    read name, score difference
    
    Uses the given name as a file base name for the file under test.
    """
    work_dir = job.fileStore.getLocalTempDir()

    baseline_read_stats_file = os.path.join(work_dir, 'baseline.tsv')
    read_from_store(job, options, baseline_file_id, baseline_read_stats_file)
    test_read_stats_file = os.path.join(work_dir, name + '.tsv')
    read_from_store(job, options, score_file_id, test_read_stats_file)

    out_file = os.path.join(work_dir, name + '.compare.scores')

    with open(baseline_read_stats_file) as baseline, open(test_read_stats_file) as test, \
         open(out_file, 'w') as out:
        line_no = 0
        for baseline_fields, test_fields in itertools.izip(tsv.TsvReader(baseline), tsv.TsvReader(test)):
            # Zip everything up and assume that the reads correspond
            line_no += 1
            
            if len(baseline_fields) != 5 or len(test_fields) != 5:
                raise RuntimeError('Incorrect field counts on line {} for {}: {} and {}'.format(
                    line_no, name, baseline_fields, test_fields))
            
            if baseline_fields[0] != test_fields[0]:
                # Read names must correspond or something has gone wrong
                raise RuntimeError('Mismatch on line {} of {} and {}.  Read names differ: {} != {}'.format(
                    line_no, baseline_read_stats_file, test_read_stats_file, baseline_fields[0], test_fields[0]))
            
            # Order is: name, conting, pos, score, mapq
            aligned_score = test_fields[3]
            baseline_score = baseline_fields[3]
            # Compute the score difference. Scores are integers.
            score_diff = parse_int(aligned_score) - parse_int(baseline_score)
            
            # Report the score difference            
            out.write('{}, {}, {}, {}\n'.format(baseline_fields[0], score_diff, aligned_score, baseline_score))
        
        # make sure same length
        has_next = False
        try:
            iter(baseline).next()
            has_next = True
        except:
            pass
        try:
            iter(test).next()
            has_next = True
        except:
            pass
        if has_next:
            raise RuntimeError('read stats files have different lengths')
        
    out_file_id = write_to_store(job, options, out_file)
    return out_file_id

def get_gam_scores(job, options, xg_file_id, name, gam_file_id):
    """
    extract read stats from gam, return id of scores file
    
    Read stats file is a TSV of read name, contig name, contig offset, score, mapping quality

    """

    work_dir = job.fileStore.getLocalTempDir()

    # download input
    xg_file = os.path.join(work_dir, '{}.xg'.format(name))
    read_from_store(job, options, xg_file_id, xg_file)
    gam_file = os.path.join(work_dir, name)
    read_from_store(job, options, gam_file_id, gam_file)

    out_pos_file = gam_file + '.tsv'
                           
    # go through intermediate json file until docker worked out
    gam_annot_json = gam_file + '.json'
    cmd = [['vg', 'annotate', '-p', '-a', os.path.basename(gam_file), '-x', os.path.basename(xg_file)]]
    cmd.append(['vg', 'view', '-aj', '-'])
    with open(gam_annot_json, 'w') as output_annot_json:
        options.drunner.call(job, cmd, work_dir = work_dir, outfile=output_annot_json)

    # turn the annotated gam json into truth positions, as separate command since
    # we're going to use a different docker container.  (Note, would be nice to
    # avoid writing the json to disk)        
    jq_cmd = [['jq', '-c', '-r', '[.name, .refpos[0].name, .refpos[0].offset,'
               'if .mapping_quality == null then 0 else .mapping_quality end ] | @tsv',
               os.path.basename(gam_annot_json)]]
    jq_cmd.append(['sed', 's/null/0/g'])

    with open(out_pos_file + '.unsorted', 'w') as out_pos:
        options.drunner.call(job, jq_cmd, work_dir = work_dir, outfile=out_pos)

    # get rid of that big json asap
    os.remove(gam_annot_json)

    # sort the positions file (not piping due to memory fears)
    sort_cmd = ['sort', os.path.basename(out_pos_file) + '.unsorted']
    with open(out_pos_file, 'w') as out_pos:
        options.drunner.call(job, sort_cmd, work_dir = work_dir, outfile = out_pos)

    out_stats_file_id = write_to_store(job, options, out_pos_file)
    return out_stats_file_id


def run_map_eval_index(job, options, xg_file_ids, gcsa_file_ids, id_range_file_ids,
                       vg_file_ids, gam_file_ids,
                       bam_file_ids, pe_bam_file_ids, reads_gam_file_id,
                       fasta_file_id, bwa_index_ids, true_read_stats_file_id):
    """ create indexes for the input vg graphs.  if none specified, then we just pass through 
    the input indexes """

    # index_ids are of the form (xg, (gcsa, lcp), id_ranges ) as returned by run_indexing
    index_ids = []
    if vg_file_ids:
        for vg_file_id in vg_file_ids:
            # vg index uses .graphs and .chroms for naming
            # todo: clean up 
            options.graphs = ['./default.vg']
            options.chroms = ['default']
            index_ids.append(job.addChildJobFn(run_indexing, options, [vg_file_id], cores=options.misc_cores,
                                               memory=options.misc_mem, disk=options.misc_disk).rv())
    else:
        for i, xg_id in enumerate(xg_file_ids):
            index_ids.append((xg_id, gcsa_file_ids[i] if gcsa_file_ids else None,
                              id_range_file_ids[i] if id_range_file_ids else None))

    
    return job.addFollowOnJobFn(run_map_eval_align, options, index_ids, gam_file_ids,
                                bam_file_ids, pe_bam_file_ids, reads_gam_file_id,
                                fasta_file_id, bwa_index_ids, true_read_stats_file_id).rv()
            


def run_map_eval_align(job, options, index_ids, gam_file_ids, bam_file_ids, pe_bam_file_ids, reads_gam_file_id,
                       fasta_file_id, bwa_index_ids, true_read_stats_file_id):
    """ run some alignments for the comparison if required"""

    do_vg_mapping = not gam_file_ids
    if do_vg_mapping:
        gam_file_ids = []
        # run vg map if requested
        for i, index_id in enumerate(index_ids):
            # todo: clean up
            map_opts = copy.deepcopy(options)
            map_opts.sample_name = 'sample-{}'.format(i)
            map_opts.interleaved = False
            gam_file_ids.append(job.addChildJobFn(run_mapping, map_opts, index_id[0], index_id[1],
                                                  None, [reads_gam_file_id],
                                                  cores=options.misc_cores,
                                                  memory=options.misc_mem, disk=options.misc_disk).rv())

    if do_vg_mapping and options.vg_paired:
        # run paired end version of all vg inputs if --pe-gams specified
        for i, index_id in enumerate(index_ids):
            # todo: clean up
            map_opts_pe = copy.deepcopy(options)
            map_opts_pe.sample_name = 'sample-pe-{}'.format(i)
            map_opts_pe.interleaved = True
            gam_file_ids.append(job.addChildJobFn(run_mapping, map_opts_pe, index_id[0], index_id[1],
                                                  None, [reads_gam_file_id],
                                                  cores=options.misc_cores,
                                                  memory=options.misc_mem, disk=options.misc_disk).rv())
            
        # make sure associated lists are extended to fit new mappings
        for i in range(len(index_ids)):
            index_ids.append(index_ids[i])
            options.gam_names.append(options.gam_names[i] + '-pe')
        
    # run bwa if requested
    bwa_bam_file_ids = [None, None]
    if options.bwa or options.bwa_paired:
        bwa_bam_file_ids = job.addChildJobFn(run_bwa_index, options, reads_gam_file_id,
                                             fasta_file_id, bwa_index_ids,
                                             cores=options.alignment_cores, memory=options.alignment_mem,
                                             disk=options.alignment_disk).rv()
        
    # scrape out the xg ids, don't need others any more
    xg_ids = [index_id[0] for index_id in index_ids]

    return job.addFollowOnJobFn(run_map_eval, options, xg_ids, gam_file_ids, bam_file_ids,
                                pe_bam_file_ids, bwa_bam_file_ids,
                                true_read_stats_file_id, cores=options.misc_cores,
                                memory=options.misc_mem, disk=options.misc_disk).rv()

def run_map_eval(job, options, xg_file_ids, gam_file_ids, bam_file_ids, pe_bam_file_ids, bwa_bam_file_ids, true_read_stats_file_id):
    """ run the mapping comparison.  Dump some tables into the outstore """

    # munge out the returned pair from run_bwa_index()
    if bwa_bam_file_ids[0] is not None:
        bam_file_ids.append(bwa_bam_file_ids[0])
        options.bam_names.append('bwa-mem')
    if bwa_bam_file_ids[1] is not None:
        pe_bam_file_ids.append(bwa_bam_file_ids[1])
        options.pe_bam_names.append('bwa-mem-pe')

    # get the bwa read alignment statistics, one id for each bam_name
    bam_stats_file_ids = []
    for bam_i, bam_id in enumerate(bam_file_ids):
        name = '{}-{}.bam'.format(options.bam_names[bam_i], bam_i)
        bam_stats_file_ids.append(job.addChildJobFn(extract_bam_read_stats, options, name, bam_id, False,
                                                    cores=options.misc_cores, memory=options.misc_mem,
                                                    disk=options.misc_disk).rv())
    # separate flow for paired end bams because different logic used
    pe_bam_stats_file_ids = []
    for bam_i, bam_id in enumerate(pe_bam_file_ids):
        name = '{}-{}.bam'.format(options.pe_bam_names[bam_i], bam_i)
        pe_bam_stats_file_ids.append(job.addChildJobFn(extract_bam_read_stats, options, name, bam_id, True,
                                                       cores=options.misc_cores, memory=options.misc_mem,
                                                       disk=options.misc_disk).rv())

    # get the gam read alignment statistics, one for each gam_name (todo: run vg map like we do bwa?)
    gam_stats_file_ids = []
    for gam_i, gam_id in enumerate(gam_file_ids):
        name = '{}-{}.gam'.format(options.gam_names[gam_i], gam_i)
        # run_mapping will return a list of gam_ids.  since we don't
        # specify id ranges, this will always have one entry
        gam = gam_id
        if type(gam_id) is list:
            assert len(gam_id) == 1
            gam = gam_id[0]
        gam_stats_file_ids.append(job.addChildJobFn(extract_gam_read_stats, options, xg_file_ids[gam_i], name, gam,
                                                    cores=options.misc_cores, memory=options.misc_mem,
                                                    disk=options.misc_disk).rv())

    # compare all our positions
    position_comparison_results = job.addFollowOnJobFn(run_map_eval_compare_positions, options, true_read_stats_file_id,
                                                       gam_stats_file_ids, bam_stats_file_ids, pe_bam_stats_file_ids,
                                                       cores=options.misc_cores, memory=options.misc_mem,
                                                       disk=options.misc_disk).rv()
    
    if options.compare_gam_scores is not None:
        # We want to compare the scores from all the GAMs against a baseline
        
        # Make a dict mapping from assigned GAM name in options.gam_names to the stats file for that GAM's alignment
        name_to_stats_id = dict(itertools.izip(options.gam_names, gam_stats_file_ids))
        
        # Find the baseline scores
        baseline_stats_id = name_to_stats_id[options.compare_gam_scores]
        
        # compare all our scores against the baseline
        # Nothing is returned, all results are dumped to the out store
        job.addFollowOnJobFn(run_map_eval_compare_scores, options, baseline_stats_id,
                             gam_stats_file_ids, bam_stats_file_ids, pe_bam_stats_file_ids,
                             cores=options.misc_cores, memory=options.misc_mem,
                             disk=options.misc_disk).rv()
        
    return position_comparison_results

def run_map_eval_compare_positions(job, options, true_read_stats_file_id, gam_stats_file_ids,
                         bam_stats_file_ids, pe_bam_stats_file_ids):
    """
    run compare on the positions
    """

    # merge up all the output data into one list
    names = options.gam_names + options.bam_names + options.pe_bam_names
    stats_file_ids = gam_stats_file_ids + bam_stats_file_ids + pe_bam_stats_file_ids

    compare_ids = []
    for name, stats_file_id in zip(names, stats_file_ids):
        compare_ids.append(job.addChildJobFn(compare_positions, options, true_read_stats_file_id, name, stats_file_id,
                                             cores=options.misc_cores, memory=options.misc_mem,
                                             disk=options.misc_disk).rv())

    return job.addFollowOnJobFn(run_process_position_comparisons, options, names, compare_ids,
                                cores=options.misc_cores, memory=options.misc_mem,
                                disk=options.misc_disk).rv()

def run_process_position_comparisons(job, options, names, compare_ids):
    """
    Write some raw tables of position comparisons to the output.  Compute some stats for each graph
    """

    work_dir = job.fileStore.getLocalTempDir()

    map_stats = []

    # make the position.results.tsv and position.stats.tsv
    results_file = os.path.join(work_dir, 'position.results.tsv')
    with open(results_file, 'w') as out_results:
        out_results.write('correct\tmq\taligner\n')

        def write_tsv(comp_file, a):
            """
            Read the given comparison CSV for the given condition name, and dump
            it to the combined results file.
            """
            with open(comp_file) as comp_in:
                for line in comp_in:
                    toks = line.rstrip().split(', ')
                    # TODO: why are we quoting the aligner name here? What parses TSV and respects quotes?
                    out_results.write('{}\t{}\t"{}"\n'.format(toks[1], toks[2], a))

        for i, nci in enumerate(zip(names, compare_ids)):
            name, compare_id = nci[0], nci[1]
            compare_file = os.path.join(work_dir, '{}-{}.compare.positions'.format(name, i))
            read_from_store(job, options, compare_id, compare_file)
            write_to_store(job, options, compare_file, use_out_store = True)
            write_tsv(compare_file, name)

            map_stats.append([job.addChildJobFn(run_acc, options, name, compare_id, cores=options.misc_cores,
                                                memory=options.misc_mem, disk=options.misc_disk).rv(),
                              job.addChildJobFn(run_auc, options, name, compare_id, cores=options.misc_cores,
                                                memory=options.misc_mem, disk=options.misc_disk).rv(),
                              job.addChildJobFn(run_qq, options, name, compare_id, cores=options.misc_cores,
                                                memory=options.misc_mem, disk=options.misc_disk).rv()])
            
    write_to_store(job, options, results_file, use_out_store = True)

    return job.addFollowOnJobFn(run_write_position_stats, options, names, map_stats).rv()

def run_write_position_stats(job, options, names, map_stats):
    """
    write the position comparison statistics as tsv
    
    This is different than the stats TSV format used internally, for read stats.
    """

    work_dir = job.fileStore.getLocalTempDir()
    stats_file = os.path.join(work_dir, 'stats.tsv')
    with open(stats_file, 'w') as stats_out:
        stats_out.write('aligner\tcount\tacc\tauc\tqq-r\n')
        for name, stats in zip(names, map_stats):
            stats_out.write('{}\t{}\t{}\t{}\t{}\n'.format(name, stats[0][0], stats[0][1],
                                                          stats[1][0], stats[2]))

    write_to_store(job, options, stats_file, use_out_store = True)
    
def run_acc(job, options, name, compare_id):
    """
    Percentage of correctly aligned reads (ignore quality)
    """
    
    work_dir = job.fileStore.getLocalTempDir()

    compare_file = os.path.join(work_dir, '{}.compare.positions'.format(name))
    read_from_store(job, options, compare_id, compare_file)
    
    total = 0
    correct = 0
    with open(compare_file) as compare_f:
        for line in compare_f:
            toks = line.split(', ')
            total += 1
            if toks[1] == '1':
                correct += 1
                
    acc = float(correct) / float(total) if total > 0 else 0
    return total, acc
    
def run_auc(job, options, name, compare_id):
    """
    AUC of roc plot
    """
    if not have_sklearn:
        return ["sklearn_not_installed"] * 2 
    
    work_dir = job.fileStore.getLocalTempDir()

    compare_file = os.path.join(work_dir, '{}.compare.positions'.format(name))
    read_from_store(job, options, compare_id, compare_file)

    try:
        data = np.loadtxt(compare_file, dtype=np.int, delimiter =', ', usecols=(1,2)).T
        auc = roc_auc_score(data[0], data[1])
        aupr = average_precision_score(data[0], data[1])
    except:
        # will happen if file is empty
        auc, aupr = 0, 0

    return auc, aupr    

def run_qq(job, options, name, compare_id):
    """
    some measure of qq consistency 
    """
    if not have_sklearn:
        return "sklearn_not_installed"

    work_dir = job.fileStore.getLocalTempDir()

    compare_file = os.path.join(work_dir, '{}.compare.positions'.format(name))
    read_from_store(job, options, compare_id, compare_file)

    try:
        data = np.loadtxt(compare_file, dtype=np.int, delimiter =', ', usecols=(1,2))

        # this can surley be sped up if necessary
        correct = Counter()
        total = Counter()
        for row in data:
            correct[row[1]] += row[0]
            total[row[1]] += 1

        qual_scores = []
        qual_observed = []            
        for qual, cor in correct.items():
            qual_scores.append(qual)
            p_err = max(1. - float(cor) / float(total[qual]), sys.float_info.epsilon)
            observed_score =-10. * math.log10(p_err)
            qual_observed.append(observed_score)

        # should do non-linear regression as well? 
        r2 = r2_score(qual_observed, qual_scores)
    except:
        # will happen if file is empty
        r2 = 'fail'

    return r2
    
def run_map_eval_compare_scores(job, options, baseline_stats_file_id, gam_stats_file_ids,
                                bam_stats_file_ids, pe_bam_stats_file_ids):
    """
    Compare scores in the given stats files in the lists to those in the given
    baseline stats file.
    
    Stats file format is a TSV of:
    read name, contig name, contig offset, score, mapping quality
    
    Will save the output to the outstore, as a CSV of read name and score
    difference, named <GAM/BAM name>.compare.scores.
    
    Will also save a concatenated TSV file, with score difference and quoted
    aligner/condition name, as score.results.tsv
    
    For now, just ignores BAMs because we don't pull in pysam to parse out their
    scores.
    
    """
    
    # merge up all the condition names and file IDs into synchronized lists
    # TODO: until we can extract the scores from BAMs, just process the GAMs
    names = options.gam_names
    stats_file_ids = gam_stats_file_ids
    
    RealtimeLogger.info(names)
    RealtimeLogger.info(stats_file_ids)

    compare_ids = []
    for name, stats_file_id in zip(names, stats_file_ids):
        compare_ids.append(job.addChildJobFn(compare_scores, options, baseline_stats_file_id, name, stats_file_id,
                                             cores=options.misc_cores, memory=options.misc_mem,
                                             disk=options.misc_disk).rv())

    job.addFollowOnJobFn(run_process_score_comparisons, options, names, compare_ids,
                         cores=options.misc_cores, memory=options.misc_mem,
                         disk=options.misc_disk)

def run_process_score_comparisons(job, options, names, compare_ids):
    """
    Write some raw tables of score comparisons to the output.  Compute some stats for each graph
    """

    work_dir = job.fileStore.getLocalTempDir()

    # Holds a list (by aligner) of lists (by type of statistic) of stats info
    # (that might be tuples, depending on the stat)
    # TODO: Change this to dicts by stat type.
    map_stats = []

    # make the score.results.tsv, which holds score differences and aligner/condition names.
    results_file = os.path.join(work_dir, 'score.results.tsv')
    with open(results_file, 'w') as out_results_file:
        out_results = tsv.TsvWriter(out_results_file)
        out_results.comment('diff\taligner')

        def write_tsv(comp_file, a):
            """
            Read the given comparison CSV for the given condition name, and dump
            it to the combined results file.
            """
            with open(comp_file) as comp_in:
                for line in comp_in:
                    toks = line.rstrip().split(', ')
                    out_results.line(toks[1], a)

        for i, nci in enumerate(zip(names, compare_ids)):
            name, compare_id = nci[0], nci[1]
            compare_file = os.path.join(work_dir, '{}-{}.compare.scores'.format(name, i))
            read_from_store(job, options, compare_id, compare_file)
            write_to_store(job, options, compare_file, use_out_store = True)
            write_tsv(compare_file, name)

            # Tabulate overall statistics
            map_stats.append([job.addChildJobFn(run_portion_worse, options, name, compare_id, cores=options.misc_cores,
                                                memory=options.misc_mem, disk=options.misc_disk).rv()])
            
    write_to_store(job, options, results_file, use_out_store = True)
    
    return job.addFollowOnJobFn(run_write_score_stats, options, names, map_stats).rv()
    
def run_write_score_stats(job, options, names, map_stats):
    """
    write the score comparison statistics as tsv
    
    This is different than the stats TSV format used internally, for read stats.
    """

    work_dir = job.fileStore.getLocalTempDir()
    stats_file = os.path.join(work_dir, 'score.stats.tsv')
    with open(stats_file, 'w') as stats_out_file:
        # Put each stat as a different column.
        stats_out = tsv.TsvWriter(stats_out_file)
        stats_out.comment('aligner\tcount\tworse')
        for name, stats in zip(names, map_stats):
            stats_out.line(name, stats[0][0], stats[0][1])

    write_to_store(job, options, stats_file, use_out_store = True)
    
def run_portion_worse(job, options, name, compare_id):
    """
    Compute percentage of reads that get worse from the baseline graph.
    Return total reads and portion that got worse.
    """
    
    work_dir = job.fileStore.getLocalTempDir()

    compare_file = os.path.join(work_dir, '{}.compare.scores'.format(name))
    read_from_store(job, options, compare_id, compare_file)
    
    total = 0
    worse = 0
    with open(compare_file) as compare_f:
        for line in compare_f:
            toks = line.split(', ')
            total += 1
            if int(toks[1]) < 0:
                worse += 1
                
    portion = float(worse) / float(total) if total > 0 else 0
    return total, portion

def mapeval_main(options):
    """
    Wrapper for vg map. 
    """

    # make the docker runner
    options.drunner = ContainerRunner(
        container_tool_map = get_container_tool_map(options))

    # check bwa / bam input parameters.  
    if options.bwa or options.bwa_paired:
        require(options.gam_input_reads, '--gam_input_reads required for bwa')
        require(options.fasta, '--fasta required for bwa')
    if options.bams:
        requrire(options.bam_names and len(options.bams) == len(options.bam_names),
                 '--bams and --bam-names must have same number of inputs')
    if options.pe_bams:
        requrire(options.pe_bam_names and len(options.pe_bams) == len(options.pe_bam_names),
                 '--pe-bams and --pe-bam-names must have same number of inputs')

    # some options from toil-vg map are disabled on the command line
    # this can be eventually cleaned up a bit better 
    require(not (options.interleaved or options.fastq),
            '--interleaved and --fastq disabled in toil-vg mapeval')

    # accept graphs or indexes in place of gams
    require(options.gams or options.index_bases or options.vg_graphs,
            'one of --vg-graphs, --index-bases or --gams must be used to specifiy vg input')

    if options.gams:
        require(len(options.index_bases) == len(options.gams),
                '--index-bases must be used along with --gams to specify xg locations')
    if options.vg_graphs:
        require(not options.gams and not options.index_bases,
                'if --vg-graphs specified, --gams and --index-bases must not be used')

    # must have a name for each graph/index/gam
    if options.gams:
        require(options.gam_names and len(options.gams) == len(options.gam_names),
                 '--gams and --gam_names must have same number of inputs')
    if options.vg_graphs:
        require(options.gam_names and len(options.vg_graphs) == len(options.gam_names),
                 '--vg-graphs and --gam_names must have same number of inputs')
    if options.index_bases:
        require(options.gam_names and len(options.index_bases) == len(options.gam_names),
                 '--index-bases and --gam_names must have same number of inputs')
        
    
    # Some file io is dependent on knowing if we're in the pipeline
    # or standalone. Hack this in here for now
    options.tool = 'mapeval'

    # Throw error if something wrong with IOStore string
    IOStore.get(options.out_store)
    
    # How long did it take to run the entire pipeline, in seconds?
    run_time_pipeline = None
        
    # Mark when we start the pipeline
    start_time_pipeline = timeit.default_timer()
    
    with Toil(options) as toil:
        if not toil.options.restart:

            start_time = timeit.default_timer()
            
            # Upload local files to the remote IO Store
            if options.gam_input_reads:
                inputReadsGAMFileID = import_to_store(toil, options, options.gam_input_reads)
            else:
                inputReadsGAMFileID = None

            # Input vg data.  can be either .vg or .gam/.xg or .xg/.gcsa/.gcsa.lcp
            inputGAMFileIDs = []
            if options.gams:
                for gam in options.gams:
                    inputGAMFileIDs.append(import_to_store(toil, options, gam))

            inputVGFileIDs = []
            if options.vg_graphs:
                for graph in options.vg_graphs:
                    inputVGFileIDs.append(import_to_store(toil, options, graph))

            inputXGFileIDs = []
            inputGCSAFileIDs = [] # list of gcsa/lcp pairs
            inputIDRangeFileIDs = []
            if options.index_bases:
                for ib in options.index_bases:
                    inputXGFileIDs.append(import_to_store(toil, options, ib + '.xg'))
                    if not options.gams:
                        inputGCSAFileIDs.append(
                            (import_to_store(toil, options, ib + '.gcsa'),
                            import_to_store(toil, options, ib + '.gcsa.lcp')))
                        # multiple gam outputs not currently supported by evaluation pipeline
                        #if os.path.isfile(os.path.join(ib, '_id_ranges.tsv')):
                        #    inputIDRAngeFileIDs.append(
                        #        import_to_store(toil, options, ib + '_id_ranges.tsv'))
                                                                       
                                        
            # Input bwa data        
            inputBAMFileIDs = []
            if options.bams:
                for bam in options.bams:
                    inputBAMFileIDs.append(import_to_store(toil, options. bam))
            inputPEBAMFileIDs = []
            if options.pe_bams:
                for bam in options.pe_bams:
                    inputPEBAMFileIDs.append(import_to_store(toil, options. bam))

            if options.fasta:
                inputBwaIndexIDs = dict()
                for suf in ['.amb', '.ann', '.bwt', '.pac', '.sa']:
                    fidx = '{}{}'.format(options.fasta, suf)
                    if os.path.exists(fidx):
                        inputBwaIndexIDs[suf] = import_to_store(toil, options, fidx)
                    else:
                        inputBwaIndexIDs = None
                        break
                if not inputBwaIndexIDs:
                    inputFastaID = import_to_store(toil, options, options.fasta)
            else:
                inputFastaID = None
                inputBwaIndexIDs = None
            inputTruePosFileID = import_to_store(toil, options, options.truth)

            end_time = timeit.default_timer()
            logger.info('Imported input files into Toil in {} seconds'.format(end_time - start_time))

            # Make a root job
            root_job = Job.wrapJobFn(run_map_eval_index, options, inputXGFileIDs,
                                     inputGCSAFileIDs,
                                     inputIDRangeFileIDs,
                                     inputVGFileIDs,
                                     inputGAMFileIDs,
                                     inputBAMFileIDs,
                                     inputPEBAMFileIDs,
                                     inputReadsGAMFileID,
                                     inputFastaID,
                                     inputBwaIndexIDs,
                                     inputTruePosFileID,
                                     cores=options.misc_cores,
                                     memory=options.misc_mem,
                                     disk=options.misc_disk)
            
            # Run the job and store the returned list of output files to download
            toil.start(root_job)
        else:
            toil.restart()
            
    end_time_pipeline = timeit.default_timer()
    run_time_pipeline = end_time_pipeline - start_time_pipeline
 
    print("All jobs completed successfully. Pipeline took {} seconds.".format(run_time_pipeline))
    
