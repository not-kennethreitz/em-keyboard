from __future__ import absolute_import, print_function, unicode_literals

import sys
import json


def parse_dictionary(filelike):
    data = json.loads(filelike.read())

    def _convert(code):
        try:
            return int(code, 16)
        except ValueError:
            return code

    return {v['alpha_code']: _convert(k) for k, v in data.iteritems()}


def translate(codes):
    with open('eac.json') as f:
        lookup = parse_dictionary(f)

    output = []
    for em in sys.argv[1:]:
        if em[0] != ':' and em[-1] != ':':
            em = ':{}:'.format(em)
        code = lookup[em]
        output.append(unichr(code))

    return output


def main():
    output = translate(sys.argv[1:])
    print(' '.join(output))


if __name__ == '__main__':
    main()
