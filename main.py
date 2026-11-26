"""Roast the Smart Fridge entry: writes the chosen one-line roast to entry.txt.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1-160
characters, not only whitespace, exactly one line, no trailing newline.
This program self-checks the gate before writing, so a bad line can
never reach the file.
"""

import os

ENTRY = (
    "My robot vacuum mapped the dog, named the spot 'obstacle', "
    "and now circles him every morning like a tiny landlord collecting rent."
)


def check_gate(text):
    """Raise if the entry would fail the scorer's gate."""
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
