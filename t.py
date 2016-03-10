from __future__ import absolute_import, print_function, unicode_literals

import sys


from em import *  # noqa


def main():
    lookup = parse_emojis()
    aliases = parse_aliases(lookup)

    output = do_find(lookup, aliases, sys.argv[1])
    for name, emoji in output:
        print('{} : {}'.format(' '.join(emoji), name))


if __name__ == '__main__':
    main()
