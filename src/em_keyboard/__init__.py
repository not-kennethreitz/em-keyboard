"""em: the technicolor cli emoji keyboard

Examples:

  $ em sparkle shortcake sparkles
  $ em red_heart

  $ em -s food

Notes:
  - If all names provided map to emojis, the resulting emojis will be
    automatically added to your clipboard.
  - ✨ 🍰 ✨  (sparkles shortcake sparkles)
"""

from __future__ import annotations

import os
from importlib.resources import as_file, files

from em_keyboard import _version

__version__ = _version.__version__

with as_file(files("em_keyboard").joinpath("emojis.json")) as em_json:
    EMOJI_PATH = em_json

CUSTOM_EMOJI_PATH = os.path.join(os.path.expanduser("~/.emojis.json"))

EmojiDict = dict[str, list[str]]


def try_copy_to_clipboard(text: str) -> bool:
    try:
        import pyperclip  # type: ignore[import]
    except ModuleNotFoundError:
        pyperclip = None
        try:
            import xerox  # type: ignore[import]
        except ModuleNotFoundError:
            return False
    copier = pyperclip if pyperclip else xerox
    copier_error = pyperclip.PyperclipException if pyperclip else xerox.ToolNotFound
    try:
        copier.copy(text)
    except copier_error:
        return False
    return True


def parse_emojis(filename: str | os.PathLike[str] = EMOJI_PATH) -> EmojiDict:
    import json

    return json.load(open(filename, encoding="utf-8"))


def translate(lookup: EmojiDict, code: str) -> str | None:
    if code[0] == ":" and code[-1] == ":":
        code = code[1:-1]

    for emoji, keywords in lookup.items():
        if code == keywords[0]:
            return emoji
    return None


def do_find(lookup: EmojiDict, terms: tuple[str, ...]) -> list[tuple[str, str]]:
    """Match terms against keywords."""
    assert terms, "at least one search term required"
    return [
        (keywords[0], emoji)
        for emoji, keywords in lookup.items()
        if all(any(term in kw for kw in keywords) for term in terms)
    ]


def clean_name(name: str) -> str:
    """Clean emoji name replacing specials chars by underscore"""
    return name.replace("-", "_").replace(" ", "_").lower()
