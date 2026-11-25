#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the winning one-line fridge text to /output/entry.txt.
The line is a single line, 125 characters (limit 140), chosen by a local
pairwise tournament judged against the bounty's published judge brief
(see README.md for the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #30 led the Swiss at 2.9, #16 second at 2.85;
# the final went to #16, 0.8–0.2.
ENTRY = (
    "it's 3am. i've decided to start a podcast. episode one: the sound "
    "of you staring into me for nine minutes. it's just humming."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
