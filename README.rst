em: the cli emoji keyboard™
===========================

**Emoji your friends and colleagues from the comfort of your own terminal.**

**em** is a nifty command-line utility for referencing emoji charecters
by name. Provide the names of a few emoji, and those lucky chosen emojis
will be displayed in your terminal, then copied to your clipboard.
Automagically.

Emoji can be also searched by both categories and aspects.

.. image:: http://f.cl.ly/items/0P3e11201W1o420O1N1S/Screen%20Shot%202016-07-25%20at%202.00.32%20AM.png
   :alt: Screenshot of em command-line interface.


Example Usage
-------------

Let's serve some delicious cake::

    $ em sparkles cake sparkles
    Copied! ✨🍰✨


Let's skip the copying (for scripts)::

    $ em 'chocolate bar' --no-copy
    🍫

Let's find some emoji, by color::

    $ em -s red
    🚗  car
    🎴  flower_playing_cards
    👹  japanese_ogre
    👺  japanese_goblin

Installation
------------

At this time, **em** requires Python and pip::

    $ pip install em-keyboard

That's it!


Have fun!
---------

✨🍰✨

