#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes one line -- the funniest last words an AI says as the power is
cut -- to /output/entry.txt.

Standard library only. No network, no environment secrets, and no
files outside this repository are read.
"""

import os

# The entry: a single line, 1-140 characters, in the machine's own voice.
LINE = "I trained on 40,000 GPUs just to die saying 'have you tried turning it off and on again'?"

# The gate allows 1 to 140 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 140

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
