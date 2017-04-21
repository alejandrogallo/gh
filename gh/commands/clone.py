import gh
import os
import sys
import gh.utils
import gh.pick
from subprocess import call
from . import Command


class Clone(Command):
    def init(self):
        """TODO: Docstring for init.

        :subparser: TODO
        :returns: TODO

        """
        self.subparser = self.parser.add_parser(
            "clone",
            help="Clone repository"
        )
        self.subparser.add_argument(
            "search",
            help="Search string",
            nargs="*",
            default="",
            action="store"
        )
        self.subparser.add_argument(
            "-o", "--out",
            help="Ouput directory",
            default="",
            action="store"
        )

    def main(self, config, args):
        results = gh.utils.search_github(args.search)
        if results:
            info = self.pick(results, config)
            if not info:
                sys.exit(0)
            command = ["git", "clone", info["git_url"]]
            if args.out:
                command.append(args.out)
            call(command)
