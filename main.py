#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
Deterministic: the same line every run, no trailing newline.
"""

import os

ROAST = (
    "My robot vacuum has mapped every inch of my apartment, "
    "yet still finds the one cable I need and eats it."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
