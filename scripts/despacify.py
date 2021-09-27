"""
Replace spaces in emoji keywords with underscores
"""
import json
import os

from em import EMOJI_PATH, parse_emojis

# The unprocessed source file
INPUT_EMOJILIB_PATH = os.path.join(os.path.dirname(EMOJI_PATH), "emoji-en-US.json")


def save_emojis(data, filename):
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=None, separators=(",", ":"))


def main():
    data = parse_emojis(INPUT_EMOJILIB_PATH)
    for emoji, keywords in data.items():
        keywords = [keyword.replace(" ", "_") for keyword in keywords]
        data[emoji] = keywords
    save_emojis(data, EMOJI_PATH)
    print(f"Emojis saved to {EMOJI_PATH}")


if __name__ == "__main__":
    main()
