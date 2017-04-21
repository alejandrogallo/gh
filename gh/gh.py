#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#  Import modules {{{1  #
#########################

import sys
import logging
import argparse
import argcomplete

from .config import Configuration
import gh.commands

logger = logging.getLogger("gh")

if sys.version_info < (3, 0):
    raise Exception("This script must use python 3.0 or greater")
    sys.exit(1)


#  Utility functions {{{1  #
############################


def main():
    config = Configuration()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Simple github searcher program"
    )

    SUBPARSER_HELP = "For further information for every "\
                     "command, type in 'gh <command> -h'"
    subparsers = parser.add_subparsers(
        help=SUBPARSER_HELP,
        metavar="command",
        dest="command"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Make the output verbose (equivalent to --log DEBUG)",
        default=False,
        action="store_true"
    )
    parser.add_argument(
        "--log",
        help="Logging level",
        choices=[
            "INFO",
            "DEBUG",
            "WARNING",
            "ERROR",
            "CRITICAL"
            ],
        action="store",
        default="INFO"
    )

    subcommands = gh.commands.init(subparsers)

    # autocompletion
    argcomplete.autocomplete(parser)
    # Parse arguments
    args = parser.parse_args()

    if args.verbose:
        args.log = "DEBUG"
    logging.basicConfig(level=getattr(logging, args.log))

    if args.command:
        if args.command in subcommands.keys():
            subcommands[args.command].main(config, args)
# vim:set et sw=4 ts=4 ft=python:
