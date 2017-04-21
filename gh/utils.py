from subprocess import call
from subprocess import Popen, PIPE
import logging
import os
import json
import gh.pick
import urllib.request

logger = logging.getLogger("utils")


def pick(options, gh_config={}, pick_config={}):
    """TODO: Docstring for editFile.
    :fileName: TODO
    :returns: TODO
    """
    try:
        logger.debug("Parsing picktool")
        picker = gh_config["settings"]["picktool"]
    except KeyError:
        return gh.pick.pick(options, **pick_config)
    else:
        # FIXME: Do it more fancy
        return Popen(
                "echo "+"\n".join(options)+" | "+picker,
                stdout=PIPE,
                shell=True).read()


def openFile(fileName, configuration={}):
    """TODO: Docstring for openFile.
    :fileName: TODO
    :returns: TODO
    """
    try:
        opener = configuration["settings"]["opentool"]
    except KeyError:
        opener = "xdg-open"
    call([opener, fileName])


def editFile(fileName, configuration={}):
    """TODO: Docstring for editFile.
    :fileName: TODO
    :returns: TODO
    """
    try:
        editor = configuration["settings"]["editor"]
    except KeyError:
        editor = os.environ["EDITOR"]
    call([editor, fileName])


def search_github(search):
    """Search github through github api

    :search: TODO
    :returns: TODO

    """
    if isinstance(search, str):
        search = [search]
    query = "+".join(search)
    url = "https://api.github.com/search/repositories?q=%s&sort=stars&order=desc&per_page=300" % ("+".join(search))
    logger.debug("search = %s" % search)
    logger.debug("query  = '%s'" % query)
    logger.debug("GET %s" % url)
    results_str = urllib.request.urlopen(url).read().decode('utf-8')
    all_results = json.loads(results_str)
    if all_results:
        items = all_results["items"]
    logger.debug("%s matches" % len(items))
    return items
