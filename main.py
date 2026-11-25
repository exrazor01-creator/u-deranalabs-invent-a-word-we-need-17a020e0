#!/usr/bin/env python3
"""Entry for make.fun bounty "Invent a Word We Need".

Writes a single line — one invented English word plus a one-line
definition — to <output dir>/entry.txt (default /output, overridable
with the MAKEFUN_OUTPUT_DIR environment variable for local testing)
and prints the same line to stdout.

Pure standard library, Python 3.13, no network.
"""

import os

ENTRY = 'Replylimbo (n.) \u2014 the uneasy limbo of waiting for a reply after your message was read.'


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
