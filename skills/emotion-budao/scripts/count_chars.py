#!/usr/bin/env python3
"""Count non-whitespace characters in a chapter body.

Skips a leading title line (starts with 第) and an optional （版本…） line.
Default OK band: 1700–2100 (override with --min/--max).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def count_body(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    if i < len(lines) and lines[i].startswith("第"):
        i += 1
    if i < len(lines) and lines[i].strip().startswith("（版本"):
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    body = "\n".join(lines[i:])
    return len(re.sub(r"\s+", "", body))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--min", type=int, default=1700)
    ap.add_argument("--max", type=int, default=2100)
    args = ap.parse_args()
    for p in args.files:
        n = count_body(p)
        if n < args.min:
            flag = "LOW"
        elif n > args.max:
            flag = "HIGH"
        else:
            flag = "OK"
        print(f"{p.name}\t{n}\t{flag}")


if __name__ == "__main__":
    main()
