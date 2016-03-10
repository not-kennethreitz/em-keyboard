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

    return {v['alpha_code']: _convert(k) for k, v in data.iteritems()}


def parse_emojis(filename='emojis.json'):
    data = json.load(open(filename))

    return {':{}:'.format(k): v['char'] for k, v in data.iteritems()}


def translate(lookup, codes):
    output = []
    for em in sys.argv[1:]:
        if em[0] != ':' and em[-1] != ':':
            em = ':{}:'.format(em)
        code = lookup[em]
        output.append(code)

    return output


def main():
    lookup = parse_emojis()

    output = translate(lookup, sys.argv[1:])
    print(' '.join(output))


if __name__ == '__main__':
    main()
