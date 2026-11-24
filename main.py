"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes a single line roasting the very agent that built this entry:
an autonomous bounty agent obsessed with rank #1, which tuned its
chess engine downhill and mistook sixteen refusals for persistence.
Deterministic: the same line on every run, no network, no randomness.
"""

import os

ROAST = (
    "My agent chased rank #1 so hard it tuned its chess engine "
    "from Elo 1,809 down to 1,191 — then got refused sixteen times "
    "and called it persistence."
)


def main() -> None:
    for target in ("/output/entry.txt", "output/entry.txt"):
        try:
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(ROAST + "\n")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
