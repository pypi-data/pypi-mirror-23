"""List the valid location identifiers."""

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import logging

from . import settings


def parser():
    """Return the command-line argument parser for ``epifx-locns``."""
    return settings.common_parser(locns=False)


def main(args=None):
    p = parser()
    if args is None:
        args = vars(p.parse_args())
    else:
        args = vars(p.parse_args(args))

    logging.basicConfig(level=args['loglevel'])

    for locn in sorted(settings.locations()):
        print(locn)
