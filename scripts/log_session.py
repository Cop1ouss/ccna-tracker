#!/usr/bin/env python3
"""
Interactive study-session logger — updates a boss-battle file's Status and
XP in place, optionally appends a dated missed-question log entry, then
runs coverage.py so you see updated readiness immediately.

No new storage format: this only edits the existing boss-battles/*.md
files by hand, the same fields coverage.py already reads.

Usage:
    python3 log_session.py

No dependencies beyond the standard library.
"""

import datetime
import pathlib
import re
import subprocess
import sys

HEADER_RE = re.compile(r"^#\s*Boss:\s*(.+?)\s*\((\d+)%\)", re.MULTILINE)
STATUS_RE = re.compile(r"(\*\*Status:\*\*\s*)(.+)")
XP_RE = re.compile(r"(\*\*XP:\*\*\s*)(\d+)(\s*/\s*)(\d+)")
TABLE_SEP_RE = re.compile(r"^\|[-\s|]+\|$")

BOSS_DIR = pathlib.Path(__file__).resolve().parent.parent / "boss-battles"
COVERAGE_SCRIPT = pathlib.Path(__file__).resolve().parent / "coverage.py"
STATUS_OPTIONS = ["Not started", "In progress", "Complete"]
TAG_OPTIONS = ["repeat", "regression", "new"]


def load_domain(path):
    text = path.read_text(encoding="utf-8")
    header = HEADER_RE.search(text)
    status_m = STATUS_RE.search(text)
    xp_m = XP_RE.search(text)
    if not (header and status_m and xp_m):
        raise ValueError(f"{path.name}: couldn't parse header/Status/XP")
    return {
        "path": path,
        "text": text,
        "name": header.group(1),
        "weight": int(header.group(2)),
        "status": status_m.group(2).strip(),
        "xp_current": int(xp_m.group(2)),
        "xp_max": int(xp_m.group(4)),
    }


def prompt_index(prompt, count, default=None):
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        if raw.isdigit() and 1 <= int(raw) <= count:
            return int(raw) - 1
        hint = " (or Enter to keep current)" if default is not None else ""
        print(f"  Enter a number 1-{count}{hint}.")


def prompt_xp(current, maximum):
    while True:
        raw = input(f"New XP (absolute number, or +N/-N to adjust) [Enter to keep {current}]: ").strip()
        if not raw:
            return current
        m = re.match(r"^([+-])(\d+)$", raw)
        if m:
            sign, amount = m.groups()
            new_val = current + (int(amount) if sign == "+" else -int(amount))
        elif raw.isdigit():
            new_val = int(raw)
        else:
            print("  Enter a plain number, or +N/-N.")
            continue
        return max(0, min(maximum, new_val))


def prompt_missed_question():
    if input("\nLog a missed question? [y/N]: ").strip().lower() != "y":
        return None
    question = input("  Question: ").strip()
    why = input("  Why I picked wrong answer: ").strip()
    tag_idx = prompt_index(
        "  Tag [1=repeat, 2=regression, 3=new] (Enter=new): ", len(TAG_OPTIONS), default=2
    )
    return question, why, TAG_OPTIONS[tag_idx]


def update_status(text, new_status):
    return STATUS_RE.sub(lambda m: m.group(1) + new_status, text, count=1)


def update_xp(text, new_current):
    return XP_RE.sub(
        lambda m: f"{m.group(1)}{new_current}{m.group(3)}{m.group(4)}", text, count=1
    )


def append_missed_question(text, question, why, tag):
    date = datetime.date.today().isoformat()
    row = f"| {date} | {question} | {why} | {tag} |"

    lines = text.splitlines()
    sep_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Missed-question log"):
            for j in range(i + 1, min(i + 5, len(lines))):
                if TABLE_SEP_RE.match(lines[j].strip()):
                    sep_idx = j
                    break
            break
    if sep_idx is None:
        raise ValueError("Couldn't find the missed-question log table")

    row_start = sep_idx + 1
    row_end = row_start
    while row_end < len(lines) and lines[row_end].strip().startswith("|"):
        row_end += 1
    existing_rows = lines[row_start:row_end]

    is_blank_placeholder = len(existing_rows) == 1 and all(
        cell.strip() == "" for cell in existing_rows[0].strip().strip("|").split("|")
    )

    if is_blank_placeholder:
        lines[row_start] = row
    else:
        lines.insert(row_end, row)

    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def main():
    paths = sorted(BOSS_DIR.glob("*.md"))
    if not paths:
        sys.exit(f"No boss-battle files found in {BOSS_DIR}")
    domains = [load_domain(p) for p in paths]

    print("Boss battles:")
    for i, d in enumerate(domains, 1):
        print(f"  {i}. {d['name']} ({d['weight']}%) — {d['status']}, XP {d['xp_current']}/{d['xp_max']}")

    idx = prompt_index(f"\nPick a domain [1-{len(domains)}]: ", len(domains))
    domain = domains[idx]
    print(f"\nSelected: {domain['name']}")

    print(f"Current status: {domain['status']}")
    default_status_idx = STATUS_OPTIONS.index(domain["status"]) if domain["status"] in STATUS_OPTIONS else None
    status_prompt = "New status [" + "/".join(f"{i+1}={s}" for i, s in enumerate(STATUS_OPTIONS)) + "]"
    status_prompt += " [Enter to keep current]: " if default_status_idx is not None else ": "
    new_status = STATUS_OPTIONS[prompt_index(status_prompt, len(STATUS_OPTIONS), default=default_status_idx)]

    print(f"Current XP: {domain['xp_current']}/{domain['xp_max']}")
    new_xp = prompt_xp(domain["xp_current"], domain["xp_max"])

    missed = prompt_missed_question()

    text = update_status(domain["text"], new_status)
    text = update_xp(text, new_xp)
    if missed:
        text = append_missed_question(text, *missed)

    domain["path"].write_text(text, encoding="utf-8")
    rel = domain["path"].relative_to(BOSS_DIR.parent)
    print(f"\nUpdated {rel}.")

    print("\nRunning coverage.py...\n")
    subprocess.run([sys.executable, str(COVERAGE_SCRIPT)], check=False)


if __name__ == "__main__":
    main()
