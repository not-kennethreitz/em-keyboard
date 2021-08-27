# em: the cli emoji keyboard™

[![PyPI version](https://img.shields.io/pypi/v/em-keyboard.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/em-keyboard/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/em-keyboard.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/em-keyboard/)
[![PyPI downloads](https://img.shields.io/pypi/dm/em-keyboard.svg)](https://pypistats.org/packages/em-keyboard)
[![GitHub Actions status](https://github.com/hugovk/em-keyboard/workflows/Test/badge.svg)](https://github.com/hugovk/em-keyboard/actions)
[![codecov](https://codecov.io/gh/hugovk/em-keyboard/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/em-keyboard)
[![GitHub](https://img.shields.io/github/license/hugovk/em-keyboard.svg)](LICENSE)

**Emoji your friends and colleagues from the comfort of your own
terminal.**

**em** is a nifty command-line utility for referencing emoji characters
by name. Provide the names of a few emoji, and those lucky chosen emojis
will be displayed in your terminal, then copied to your clipboard.
Automagically.

Emoji can be also searched by both categories and aspects.

## Example Usage

Let's serve some delicious cake:

```console
$ em sparkles shortcake sparkles
Copied! ✨🍰✨
```

Let's skip the copying (for scripts):

```console
$ em 'chocolate bar' --no-copy
🍫
```

Let's find some emoji, by color:

```console
$ em -s yellow
💛  yellow_heart
🌼  blossom
🌕  full_moon
⭐  star
🚸  children_crossing
🟡  yellow_circle
🟨  yellow_square
```

## Installation

At this time, **em** requires Python and pip:

```sh
python3 -m pip install em-keyboard
```

That's it!

## Tests

If you wanna develop, you might want to write and run tests:

```sh
python3 -m pip install tox
tox
```

## Have fun!

✨🍰✨
