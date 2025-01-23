"""
CLI for em_keyboard
"""

from __future__ import annotations

import argparse
import os
import sys

from em_keyboard import (
    CUSTOM_EMOJI_PATH,
    __version__,
    clean_name,
    do_find,
    parse_emojis,
    translate,
    try_copy_to_clipboard,
)


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("name", nargs="*", help="Text to convert to emoji")
    parser.add_argument("-s", "--search", action="store_true", help="Search for emoji")
    parser.add_argument("-r", "--random", action="store_true", help="Get random emoji")
    parser.add_argument(
        "--no-copy", action="store_true", help="Does not copy emoji to clipboard"
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args(arg_list)
    return args


def main(arg_list: list[str] | None = None) -> None:
    args = parse_args(arg_list)
    no_copy = args.no_copy

    if not args.name and not args.random:
        sys.exit("Error: the 'name' argument is required")

    # Grab the lookup dictionary.
    lookup = parse_emojis()

    if os.path.isfile(CUSTOM_EMOJI_PATH):
        lookup.update(parse_emojis(CUSTOM_EMOJI_PATH))

    if args.random:
        import random

        emoji, keywords = random.choice(list(lookup.items()))
        name = keywords[0]
        if not no_copy:
            copied = try_copy_to_clipboard(emoji)
        else:
            copied = False
        print(f"Copied! {emoji}  {name}" if copied else f"{emoji}  {name}")
        sys.exit(0)

    names = tuple(map(clean_name, args.name))

    # Marker for if the given emoji isn't found.
    missing = False

    # Search mode.
    if args.search:
        # Lookup the search term.
        found = do_find(lookup, names)

        # print them to the screen.
        for name, emoji in found:
            # Some registered emoji have no value.
            try:
                # Copy the results (and say so!) to the clipboard.
                if not no_copy and len(found) == 1:
                    copied = try_copy_to_clipboard(emoji)
                else:
                    copied = False
                print(f"Copied! {emoji}  {name}" if copied else f"{emoji}  {name}")

            # Sometimes, an emoji will have no value.
            except TypeError:
                pass

        if len(found):
            sys.exit(0)
        else:
            sys.exit(1)

    # Process the results.
    results = tuple(translate(lookup, name) for name in names)

    if None in results:
        no_copy = True
        missing = True
        results = tuple(r for r in results if r)

    # Prepare the result strings.
    print_results = " ".join(results)
    results = "".join(results)

    # Copy the results (and say so!) to the clipboard.
    if not no_copy and not missing:
        copied = try_copy_to_clipboard(results)
    else:
        copied = False

    if print_results:
        print(f"Copied! {print_results}" if copied else print_results)

    sys.exit(int(missing))


if __name__ == "__main__":
    main()
