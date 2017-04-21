import webbrowser
import gh
import os
import gh.utils
from . import Command


class Browse(Command):
    def init(self):
        """TODO: Docstring for init.

        :subparser: TODO
        :returns: TODO

        """

        # open parser
        self.subparser = self.parser.add_parser(
            "browse",
            help="Browse the website of the repository"
        )
        self.subparser.add_argument(
            "search",
            help="Search",
            nargs="*",
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
        results = gh.utils.search_github(args.search)
        if results:
            info = self.pick(results, config)
            if not info:
                sys.exit(0)
            webbrowser.open(info["html_url"])
