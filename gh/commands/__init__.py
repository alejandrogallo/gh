import logging
import gh.utils

COMMANDS = [
    "clone",
    "config",
    "search",
    "browse"
]

logger = logging.getLogger("commands")


def init(parser):
    global COMMANDS
    global logger
    commands = dict()
    cmd = None
    logger.debug("Initializing commands")
    for command in COMMANDS:
        logger.debug(command)
        exec("from .%s import %s" % (command, command.capitalize()))
        cmd = eval(command.capitalize())(parser)
        cmd.setParser(parser)
        cmd.init()
        commands[command] = cmd
    return commands


class Command(object):

    args = None
    subparser = None

    def __init__(self, parser=None):
        self.parser = parser
        self.logger = logging.getLogger(self.__class__.__name__)

    def init(self):
        pass

    def setParser(self, parser):
        """TODO: Docstring for setParser.

        :parser: TODO
        :returns: TODO

        """
        self.parser = parser

    def getParser(self):
        """TODO: Docstring for getParser.
        :returns: TODO

        """
        return self.parser

    def default_header_filter(self, x):
        return "{:<70.70} ({}|{}|{:<4.4}) | {}".format(
            x["description"] or "-No description-",
            str(x["stargazers_count"]),
            str(x["forks"]),
            x["language"] or "???",
            x["full_name"] or "???/???"
        )

    def default_match_filter(self, x):
        return self.default_header_filter(x)

    def pick(self, options, gh_config, pick_config={}):
        """TODO: Docstring for pick.

        :options: TODO
        :returns: TODO

        """
        if not pick_config:
            pick_config=dict(
                header_filter=self.default_header_filter,
                match_filter=self.default_match_filter
            )
        return gh.utils.pick(
            options,
            gh_config,
            pick_config
        )

    def main(self, config=None, args=None):
        if not args:
            self.args = args
