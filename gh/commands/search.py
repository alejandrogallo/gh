import gh
import os
import sys
import gh.utils
import gh.pick
from subprocess import call
from . import Command


class Search(Command):
    def init(self):
        self.subparser = self.parser.add_parser(
            "search",
            help="Search repository and output json information"
        )
        self.subparser.add_argument(
            "search",
            help="Search string",
            nargs="*",
            default="",
            action="store"
        )

    def main(self, config, args):
        results = gh.utils.search_github(args.search)
        info = self.pick(results, config)
        print(info)
