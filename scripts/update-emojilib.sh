wget https://github.com/muan/emojilib/raw/main/dist/emoji-en-US.json -O src/em_keyboard/emoji-en-US.json
echo >> src/em_keyboard/emoji-en-US.json  # Add newline to end of file
python3 scripts/despacify.py
