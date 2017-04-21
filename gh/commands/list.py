import gh
import os
import gh.utils
from . import Command


class List(Command):
    def init(self):
        """TODO: Docstring for init.

        :subparser: TODO
        :returns: TODO

        """

        self.subparser = self.parser.add_parser(
            "list",
            help="List repositories"
        )
        self.subparser.add_argument(
            "search",
            help="Search",
            nargs="?",
            default=".",
            action="store"
        )

    def main(self, config, args):
        """
        Main action if the command is triggered

        :config: User configuration
        :args: CLI user arguments
        :returns: TODO

        """
        print("todo...")
