# -*- coding: utf-8 -*-

"""em: the technicolor cli emoji experience™

Usage:
  em <name>... [--no-copy]
  em add <name> <character>...

Options:
  -h --help     Show this screen.
  --no-copy     Does not copy emoji to clipboard.

Examples:

  $ em sparkle cake sparkles
  $ em heart

Notes:
  - If all names provided map to emojis, the resulting emojis will be
    automatically added to your clipboard.
  - Custom aliases for emoji sets are supported.
"""

from __future__ import absolute_import, print_function, unicode_literals

from collections import defaultdict
import json
import fnmatch
import itertools
import sys

import xerox
from docopt import docopt


def parse_emojis(filename='emojis.json'):
    return json.load(open(filename))


def parse_aliases(lookup, filename='aliases.json'):
    data = json.load(open(filename))

    return {k: [lookup[c] for c in v.split()] for k, v in data.iteritems()}


def translate(lookup, aliases, code):
    output = []
    if code[0] == ':' and code[-1] == ':':
        code = code[1:-1]

    if code in aliases:
        output.extend(aliases[code])
    else:
        output.append(lookup.get(code, {'char': None})['char'])

    return output


def do_list(lookup, aliases, term):
    """
        matches term glob against short-name,
    """
    space = lookup.keys() + aliases.keys()

    matches = fnmatch.filter(space, term)

    return [(m, translate(lookup, aliases, m)) for m in matches]


def do_find(lookup, aliases, term):
    """
        matches term glob against short-name, keywords and categories
    """
    space = defaultdict(list)

    for name in lookup.keys():
        space[name].append(name)

    for name, definition in lookup.iteritems():
        for keyword in definition['keywords']:
            space[keyword].append(name)
        space[definition['category']].append(name)

    for name in aliases.keys():
        space[name].append(name)

    matches = fnmatch.filter(space.keys(), term)

    results = set()
    for match in matches:
        results.update(space[match])

    return [(r, translate(lookup, aliases, r)) for r in results]


def cli():
    arguments = docopt(__doc__)

    names = arguments['<name>']
    no_copy = arguments['--no-copy']

    if arguments['add']:
        arguments['<charecter>']
        arguments['<name>']


    missing = False

    lookup = parse_emojis()
    aliases = parse_aliases(lookup)

    results = (translate(lookup, aliases, name) for name in names)
    results = list(itertools.chain.from_iterable(results))
    if None in results:
        no_copy = True
        missing = True
        results = (r for r in results if r)

    print_results = ' '.join(results)
    results = ''.join(results)

    print(print_results)

    if not no_copy and not missing:
        xerox.copy(results)

    sys.exit(int(missing))

if __name__ == '__main__':
    cli()
