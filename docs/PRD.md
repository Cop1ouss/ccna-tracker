# PRD: CCNA Tracker

| | |
| --- | --- |
| **Owner** | Dajoni Gomez |
| **Status** | Build → Ship |
| **Phase color** | Onyx (building) |
| **Live** | https://cop1ouss.github.io/ccna-tracker/ |

## Problem

Watching videos and reading notes feels like progress, but the CCNA is won in the CLI and in timed subnetting. I need the **hands-on, test-prep side** of studying to be just as structured as the curriculum in [`cisco-track`](https://github.com/Cop1ouss/cisco-track), and measurable.

## Goal

Pass **CCNA 200-301 v1.1** before it retires on Feb 2, 2027, with a readiness number based on blueprint weights instead of a gut feeling.

## Users

- **Me.**
- Other CCNA candidates who want labs, drills and an honest readiness score.

## Scope

**In:**
- Boss battles for the 6 domains.
- Ultimate guide per domain.
- Original practice questions and full mock exams.
- An Anki deck.
- Packet Tracer and GNS3 labs.
- Python scripts: a subnetting drill, a coverage/readiness report and an Anki sync.

**Out:**
- Copying exam dumps or copyrighted question banks.
- v2.0 content until my exam date is settled.

## Requirements

1. `scripts/coverage.py` prints per-domain and blueprint-weighted readiness from the boss-battle files.
2. `scripts/subnet_drill.py` generates timed questions with standard library only.
3. `scripts/sync_anki.py` pushes the deck through AnkiConnect, with a `--dry-run` mode.
4. Mock exams keep questions and answer keys in separate files.
5. Every lab maps back to a blueprint objective.

## Finish line

- Weighted readiness **≥ 85%**.
- Two mock exams passed cold.
- Subnetting drill: 15 questions at ≥ 90% under the time limit.
- Then book the exam.

## Risks

- **Blueprint change on Feb 3, 2027.** Mitigation: the README warning, and booking the v1.1 exam first.
- **Overlap with cisco-track.** Mitigation: possibly merge both into one CCNA repo later. This repo stays the hands-on half.

---

<sub>© 2026 Dajoni Gomez · Uncook™ · part of the [journey log](https://cop1ouss.github.io/Cop1ouss/)</sub>
