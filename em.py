"""em: the technicolor cli emoji experience™

Usage:
  em <name>... [--no-copy]
  em set <name> <charecter>...
  naval_fate.py --version

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

from docopt import docopt



def cli():
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    cli()