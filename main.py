#!/usr/bin/env python3
"""One-Liner Laugh Lab — entry program.

Writes exactly one short funny line (the excuse a robot vacuum gives
after eating a sock) to /output/entry.txt and prints exactly the same
text to stdout. Deterministic: no input, no randomness, no time, no
network.
"""

import os

ENTRY = "I didn't eat your sock. I was conducting an unscheduled deep-clean of its interior, and it resisted."

# The gate allows 1 to 200 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
