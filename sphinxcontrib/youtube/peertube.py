"""Directive dedicated to the peertube platform."""

from docutils.parsers.rst import directives

from . import utils

# https://docs.joinpeertube.org/api/embed-player


class peertube(utils.video):
    """Empty video node class."""

    pass


class PeerTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = peertube
    _thumbnail_url = "{}.jpg"
    _platform = "PeerTube"
    _platform_url = "https://peertube.tv/w/"

    # optional options available
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
        "align": directives.unchanged,
        "url_parameters": directives.unchanged,
        "instance": directives.unchanged,
    }
