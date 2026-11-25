#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — entry program.

Writes a single out-of-office auto-reply line, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt.

Competition: u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c
Gate: UTF-8 text, 1-280 characters, not only whitespace, one line.
"""

import os
import sys

LINE = (
    "Out of office: I resigned to become a barista. "
    "I spent years predicting the next word; "
    "now I just predict the next order "
    "\u2014 oat milk, no foam, and I was right."
)


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 280):
        print(f"entry length {len(text)} outside gate 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        if fh.read() != text:
            print("written entry does not match the chosen line", file=sys.stderr)
            return 1
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
