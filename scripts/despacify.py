"""
Replace spaces in emoji keywords with underscores
"""
from __future__ import annotations

import json

from em_keyboard import parse_emojis

INPUT_EMOJILIB_PATH = "src/em_keyboard/emoji-en-US.json"
OUTPUT_EMOJI_PATH = "src/em_keyboard/emojis.json"


def save_emojis(data: dict[str, list[str]], filename: str) -> None:
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=None, separators=(",", ":"))
        outfile.write("\n")


def main() -> None:
    data = parse_emojis(INPUT_EMOJILIB_PATH)
    for emoji, keywords in data.items():
        keywords = [keyword.replace(" ", "_") for keyword in keywords]
        data[emoji] = keywords
    save_emojis(data, OUTPUT_EMOJI_PATH)
    print(f"Emojis saved to {OUTPUT_EMOJI_PATH}")


if __name__ == "__main__":
    main()
