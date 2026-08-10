#!/usr/bin/env python3
"""
Readiness dashboard — reads Status/XP out of every boss-battles/*.md file
and prints per-domain and overall (blueprint-weighted) readiness.

Usage:
    python3 coverage.py

No dependencies beyond the standard library.
"""

import argparse
import pathlib
import re
import sys

HEADER_RE = re.compile(r"^#\s*Boss:\s*(.+?)\s*\((\d+)%\)", re.MULTILINE)
STATUS_RE = re.compile(r"\*\*Status:\*\*\s*(.+)")
XP_RE = re.compile(r"\*\*XP:\*\*\s*(\d+)\s*/\s*(\d+)")

DEFAULT_DIR = pathlib.Path(__file__).resolve().parent.parent / "boss-battles"
BAR_WIDTH = 24


def parse_boss_battle(path):
    text = path.read_text(encoding="utf-8")

    header = HEADER_RE.search(text)
    if not header:
        raise ValueError(f"{path.name}: couldn't find '# Boss: <Name> (NN%)' header")
    name, weight = header.group(1), int(header.group(2))

    status_match = STATUS_RE.search(text)
    status = status_match.group(1).strip() if status_match else "Unknown"

    xp_match = XP_RE.search(text)
    if not xp_match:
        raise ValueError(f"{path.name}: couldn't find '**XP:** N / M' line")
    xp_current, xp_max = int(xp_match.group(1)), int(xp_match.group(2))
    pct = (xp_current / xp_max * 100) if xp_max else 0.0

    return {
        "file": path.name,
        "name": name,
        "weight": weight,
        "status": status,
        "xp_current": xp_current,
        "xp_max": xp_max,
        "pct": pct,
    }


def bar(pct, width=BAR_WIDTH):
    filled = round(width * pct / 100)
    return "#" * filled + "-" * (width - filled)


def main():
    parser = argparse.ArgumentParser(description="CCNA boss-battle readiness dashboard")
    parser.add_argument("--dir", type=pathlib.Path, default=DEFAULT_DIR,
                         help="directory containing boss-battles/*.md (default: ../boss-battles)")
    args = parser.parse_args()

    files = sorted(args.dir.glob("*.md"))
    if not files:
        sys.exit(f"No boss-battle files found in {args.dir}")

    domains = []
    for path in files:
        try:
            domains.append(parse_boss_battle(path))
        except ValueError as e:
            sys.exit(str(e))

    weight_sum = sum(d["weight"] for d in domains)
    if weight_sum != 100:
        print(f"Warning: domain weights sum to {weight_sum}%, not 100% — overall % below will be skewed.\n")

    print(f"{'Domain':<32} {'Weight':>7} {'XP':>10} {'Status':<14} {'Progress'}")
    print("-" * 100)
    for d in domains:
        xp_str = f"{d['xp_current']}/{d['xp_max']}"
        print(f"{d['name']:<32} {d['weight']:>6}% {xp_str:>10} {d['status']:<14} [{bar(d['pct'])}] {d['pct']:5.1f}%")

    overall = sum(d["pct"] * d["weight"] / 100 for d in domains)
    print("-" * 100)
    print(f"{'OVERALL (blueprint-weighted)':<32} {'100%':>7} {'':>10} {'':<14} [{bar(overall)}] {overall:5.1f}%")


if __name__ == "__main__":
    main()
