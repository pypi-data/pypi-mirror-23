import sys

import option_parsers

import resquiggle
import plot_commands
import text_output_commands

from collections import OrderedDict

import nanoraw_helper as nh

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    commands = [
        ('Main Comand (Must be run before any other commands):',[
            ('genome_resquiggle','Re-annotate raw signal with ' +
             'genomic aignement of existing basecalls.',
             option_parsers.get_resquiggle_parser(),
             resquiggle.resquiggle_main)]),
        ('Genome Anchored Plotting Commands:', [
            ('plot_max_coverage',
             'Plot signal in regions with the maximum coverage.',
             option_parsers.get_max_cov_parser(),
             plot_commands.max_cov_main),
            ('plot_genome_location',
             'Plot signal at defined genomic locations.',
             option_parsers.get_genome_loc_parser(),
             plot_commands.genome_loc_main),
            ('plot_motif_centered',
             'Plot signal at regions centered on a specific motif.',
             option_parsers.get_motif_loc_parser(),
             plot_commands.motif_loc_main),
            ('plot_max_difference',
             'Plot signal where signal differs the most ' +
             'between two groups.',
             option_parsers.get_max_diff_parser(),
             plot_commands.max_diff_main),
            ('plot_most_significant',
             'Plot signal where signal differs the most ' +
             'significantly between two groups.',
             option_parsers.get_signif_diff_parser(),
             plot_commands.signif_diff_main),
            ('plot_motif_with_stats',
             'Plot signal from several regions and test ' +
             'statistics centered on a k-mer of interst.',
             option_parsers.get_signif_motif_parser(),
             plot_commands.motif_signif_diff_main)]),
        ('Sequencing Time Anchored Plotting Command:', [
            ('plot_correction',
             'Plot segmentation before and after correction.',
             option_parsers.get_correction_parser(),
             plot_commands.plot_correction_main),
            ('plot_multi_correction',
             'Plot multiple raw signals anchored by genomic location.',
             option_parsers.get_multi_correction_parser(),
             plot_commands.plot_multi_correction_main)]),
        ('Other Plotting Commands:', [
            ('cluster_most_significant',
             'Clustering traces at bases with significant differences.',
             option_parsers.get_cluster_signif_diff_parser(),
             plot_commands.cluster_signif_diff_main),
            ('plot_kmer','Plot signal quantiles acorss kmers.',
             option_parsers.get_kmer_dist_parser(),
             plot_commands.kmer_dist_main)]),
        ('Auxiliary Commands:',[
            ('write_most_significant_fasta',
             'Write sequence where signal differs the most ' +
             'significantly between two groups.',
             option_parsers.get_write_signif_diff_parser(),
             text_output_commands.write_signif_diff_main),
            ('write_wiggles','Write wiggle files for nanopore ' +
             'signal values, coverage, and statistics.',
             option_parsers.get_wiggle_parser(),
             text_output_commands.wiggle_main)]),
    ]
    desc = '\n\n'.join([
        grp + '\n' + '\n'.join([
            '\t{0: <30}{1}'.format(cmd, cmd_help)
            for cmd, cmd_help, cmd_parser, cmd_main in cmds])
        for grp, cmds in commands])

    import argparse
    parser = argparse.ArgumentParser(
        prog='nanoraw',
        description='nanoraw is a command line and python toolset ' +
        'to analyze and visualize raw nanopore sequencing data.',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-v', '--version',
        action='version', version='nanoraw version: {}'.format(
            nh.NANORAW_VERSION),
        help='show nanoraw version and exit.')
    subparsers = parser.add_subparsers(
        title='commands', description=desc,
        help='Additional help available for subcommands.')

    # fill subparser with parsers and linked main functions
    for grp, cmds in commands:
        for cmd, cmd_help, cmd_parser, cmd_main in cmds:
            subparser_cmd = subparsers.add_parser(
                cmd, parents=[cmd_parser,], add_help=False)
            subparser_cmd.set_defaults(func=cmd_main)

    args = parser.parse_args(args)

    args.func(args)

    return

if __name__ == "__main__":
    main()
