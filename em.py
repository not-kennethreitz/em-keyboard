# -*- coding: utf-8 -*-

"""em: the technicolor cli emoji experience™

Usage:
  em <name>... [--no-copy]

Options:
  -h --help     Show this screen.
  --no-copy     Does not copy emoji to clipboard.

Examples:

  $ em sparkle cake sparkles
  $ em heart

Notes:
  - If all names provided map to emojis, the resulting emojis will be
    automatically added to your clipboard.
"""

from collections import defaultdict
import json
import fnmatch
import itertools
import sys

import xerox
from docopt import docopt


def parse_emojis(filename='emojis.json'):
    return json.load(open(filename))


def translate(lookup, code):
    output = []
    if code[0] == ':' and code[-1] == ':':
        code = code[1:-1]

    output.append(lookup.get(code, {'char': None})['char'])

    return output


def do_list(lookup, term):
    """Matches term glob against short-name."""

    space = lookup.keys()
    matches = fnmatch.filter(space, term)

    return [(m, translate(lookup, m)) for m in matches]


def do_find(lookup, term):
    """Matches term glob against short-name, keywords and categories."""

    space = defaultdict(list)

    for name in lookup.keys():
        space[name].append(name)

    for name, definition in lookup.iteritems():
        for keyword in definition['keywords']:
            space[keyword].append(name)
        space[definition['category']].append(name)

    matches = fnmatch.filter(space.keys(), term)

    results = set()
    for match in matches:
        results.update(space[match])

    return [(r, translate(lookup, r)) for r in results]


def cli():
    arguments = docopt(__doc__)

    names = arguments['<name>']
    no_copy = arguments['--no-copy']

    # Marker for if the given emoji isn't found.
    missing = False

    # Grab the lookup dictionary.
    lookup = parse_emojis()

    # Process the results.
    results = (translate(lookup, name) for name in names)
    results = list(itertools.chain.from_iterable(results))

    if None in results:
        no_copy = True
        missing = True
        results = (r for r in results if r)

    # Prepare the result strings.
    print_results = ' '.join(results)
    results = ''.join(results)

    # Copy the results (and say so!) to the clipboard.
    if not no_copy and not missing:
        xerox.copy(results)
        print u'Copied! {}'.format(print_results)

    # Script-kiddies.
    else:
        print(print_results)

    sys.exit(int(missing))

if __name__ == '__main__':
    cli()
