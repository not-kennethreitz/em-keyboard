from __future__ import absolute_import, print_function, unicode_literals

import sys
import json


def parse_eac(filename='eac.json'):
    data = json.load(open(filename))
    def _convert(code):
        try:
            return unichr(int(code, 16))
        except ValueError:
            return code

    return {v['alpha_code'][1:-1]: _convert(k) for k, v in data.iteritems()}


def parse_emojis(filename='emojis.json'):
    data = json.load(open(filename))

    return {k: v['char'] for k, v in data.iteritems()}


def parse_aliases(lookup, filename='aliases.json'):
    data = json.load(open(filename))

    return {k: [lookup[c] for c in v.split()] for k, v in data.iteritems()}


def translate(lookup, aliases, codes):
    output = []
    for code in sys.argv[1:]:
        if code[0] == ':' and code[-1] == ':':
            code = code[1:-1]

        if code in aliases:
            output.extend(aliases[code])
        else:
            output.append(lookup[code])

    return output


def main():
    lookup = parse_emojis()
    aliases = parse_aliases(lookup)

    output = translate(lookup, aliases, sys.argv[1:])
    print(' '.join(output))


if __name__ == '__main__':
    main()
