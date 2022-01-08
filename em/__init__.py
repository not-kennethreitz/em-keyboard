"""em: the technicolor cli emoji keyboard™

Examples:

  $ em sparkle shortcake sparkles
  $ em red_heart

  $ em -s food

Notes:
  - If all names provided map to emojis, the resulting emojis will be
    automatically added to your clipboard.
  - ✨ 🍰 ✨  (sparkles shortcake sparkles)
"""


import argparse
import itertools
import json
import os
import re
import sys

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python 3.7 and lower
    import importlib_metadata

try:
    import pyperclip as copier
except ImportError:
    try:
        import xerox as copier
    except ImportError:
        copier = None

__version__: str = importlib_metadata.version("em_keyboard")

EMOJI_PATH = os.path.join(os.path.dirname(__file__), "emojis.json")
CUSTOM_EMOJI_PATH = os.path.join(os.path.expanduser("~/.emojis.json"))


def parse_emojis(filename=EMOJI_PATH):
    return json.load(open(filename, encoding="utf-8"))


def translate(lookup: dict, code: str) -> list:
    output = []
    if code[0] == ":" and code[-1] == ":":
        code = code[1:-1]

    for emoji, keywords in lookup.items():
        if code == keywords[0]:
            output.append(emoji)
            break
    else:
        output.append(None)

    return output


def do_find(lookup: dict, term: str) -> list:
    """Match term against keywords."""
    output = []
    seen = set()

    for emoji, keywords in lookup.items():
        for keyword in keywords:
            if term in keyword and emoji not in seen:
                output.append((keywords[0], emoji))
                seen.add(emoji)

    return output


def clean_name(name):
    """Clean emoji name replacing specials chars by underscore"""
    special_chars = "[-. ]"  # square brackets are part of the regex
    return re.sub(special_chars, "_", name).lower()


def cli():
    # CLI argument parsing.
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("name", nargs="+", help="Text to convert to emoji")
    parser.add_argument("-s", "--search", action="store_true", help="Search for emoji")
    parser.add_argument(
        "--no-copy", action="store_true", help="Does not copy emoji to clipboard"
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()
    names = tuple(map(clean_name, args.name))
    no_copy = args.no_copy

    # Marker for if the given emoji isn't found.
    missing = False

    # Grab the lookup dictionary.
    lookup = parse_emojis()

    if os.path.isfile(CUSTOM_EMOJI_PATH):
        lookup.update(parse_emojis(CUSTOM_EMOJI_PATH))

    # Search mode.
    if args.search:

        # Lookup the search term.
        found = do_find(lookup, names[0])

        # print them to the screen.
        for (name, emoji) in found:
            # Some registered emoji have no value.
            try:
                print(f"{emoji}  {name}")
            # Sometimes, an emoji will have no value.
            except TypeError:
                pass

        if len(found):
            sys.exit(0)
        else:
            sys.exit(1)

    # Process the results.
    results = (translate(lookup, name) for name in names)
    results = list(itertools.chain.from_iterable(results))

    if None in results:
        no_copy = True
        missing = True
        results = (r for r in results if r)

    # Prepare the result strings.
    print_results = " ".join(results)
    results = "".join(results)

    # Copy the results (and say so!) to the clipboard.
    if copier and not no_copy and not missing:
        copier.copy(results)
        print(f"Copied! {print_results}")

    # Script-kiddies.
    else:
        print(print_results)

    sys.exit(int(missing))


if __name__ == "__main__":
    cli()
