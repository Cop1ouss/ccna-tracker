#!/usr/bin/env python3
"""
AnkiConnect sync — push flashcards/ccna-core-facts.csv straight into a
running Anki instance instead of manual CSV re-import on every change.

Requires the AnkiConnect add-on (https://ankiweb.net/shared/info/2055492159)
installed in Anki, and Anki running, before you run this script.

Usage:
    python3 sync_anki.py                  # sync the default CSV into "CCNA Core Facts"
    python3 sync_anki.py --dry-run         # show what would change, touch nothing
    python3 sync_anki.py --deck "My Deck"  # sync into a different deck name

No dependencies beyond the standard library.
"""

import argparse
import csv
import json
import pathlib
import sys
import urllib.error
import urllib.request

DEFAULT_URL = "http://127.0.0.1:8765"
DEFAULT_CSV = pathlib.Path(__file__).resolve().parent.parent / "flashcards" / "ccna-core-facts.csv"
DEFAULT_DECK = "CCNA Core Facts"
NOTE_TYPE = "Basic"


def invoke(url, action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise ConnectionError(
            f"Can't reach AnkiConnect at {url} — is Anki running with the AnkiConnect add-on installed?"
        ) from e
    if body.get("error"):
        raise RuntimeError(f"AnkiConnect error on '{action}': {body['error']}")
    return body["result"]


def escape_query_value(value):
    return value.replace('\\', '\\\\').replace('"', '\\"')


def read_cards(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [(row["Front"].strip(), row["Back"].strip()) for row in reader if row.get("Front")]


def main():
    parser = argparse.ArgumentParser(description="Sync ccna-core-facts.csv into Anki via AnkiConnect")
    parser.add_argument("--csv", type=pathlib.Path, default=DEFAULT_CSV)
    parser.add_argument("--deck", default=DEFAULT_DECK)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--dry-run", action="store_true", help="show planned changes without writing to Anki")
    args = parser.parse_args()

    if not args.csv.exists():
        sys.exit(f"CSV not found: {args.csv}")

    cards = read_cards(args.csv)
    if not cards:
        sys.exit(f"No cards found in {args.csv}")

    try:
        invoke(args.url, "version")
    except ConnectionError as e:
        sys.exit(str(e))

    if not args.dry_run:
        if args.deck not in invoke(args.url, "deckNames"):
            invoke(args.url, "createDeck", deck=args.deck)

    added = updated = unchanged = 0

    for front, back in cards:
        query = f'deck:"{escape_query_value(args.deck)}" Front:"{escape_query_value(front)}"'
        note_ids = invoke(args.url, "findNotes", query=query)

        if note_ids:
            existing = invoke(args.url, "notesInfo", notes=note_ids)[0]
            existing_back = existing["fields"]["Back"]["value"]
            if existing_back.strip() == back:
                unchanged += 1
                continue
            print(f"[update] {front}")
            if not args.dry_run:
                invoke(
                    args.url, "updateNoteFields",
                    note={"id": existing["noteId"], "fields": {"Front": front, "Back": back}},
                )
            updated += 1
        else:
            print(f"[add]    {front}")
            if not args.dry_run:
                invoke(
                    args.url, "addNote",
                    note={
                        "deckName": args.deck,
                        "modelName": NOTE_TYPE,
                        "fields": {"Front": front, "Back": back},
                        "tags": ["ccna-tracker"],
                    },
                )
            added += 1

    prefix = "[dry-run] " if args.dry_run else ""
    print(f"\n{prefix}Added {added}, updated {updated}, unchanged {unchanged} (of {len(cards)} cards).")


if __name__ == "__main__":
    main()
