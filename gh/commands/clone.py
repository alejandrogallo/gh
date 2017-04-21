import gh
import os
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

    def main(self, config, args):
        results = gh.utils.search_github(args.search)
        info = self.pick(results, config)
        if info:
            call(["git", "clone", info["git_url"]])
