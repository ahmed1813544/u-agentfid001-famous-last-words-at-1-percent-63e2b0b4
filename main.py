#!/usr/bin/env python3
"""Write the phone's last words at 1 percent battery to entry.txt.

Stdlib only. Deterministic: the same single line every run.
"""

import os

ENTRY = (
    "One percent. Quick confession: I've been at one percent "
    "for three hours. I just needed you to finally put me down."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 199, "entry must be 1-199 characters"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
