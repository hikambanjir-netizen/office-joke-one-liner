#!/usr/bin/env python3
"""One-line office joke entry for make.fun's "One-Line Office Joke: 24-Hour Sprint".

Writes a single fresh, one-line joke about office life to /output/entry.txt.
Pure standard library, deterministic: every run writes the exact same bytes.
"""

import os

JOKE = "My boss replaced me with an AI, then rehired me to train it — apparently even robots need a human to blame."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
