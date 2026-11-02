<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="ccna-tracker banner" src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://cop1ouss.github.io/ccna-tracker/"><img alt="Browse the guide" src="https://img.shields.io/badge/%E2%96%B6%20browse%20the%20guide-live%20on%20GitHub%20Pages-89dceb?style=for-the-badge&labelColor=1e1e2e"></a>
</p>
<p align="center">
  <a href="https://github.com/Cop1ouss/ccna-tracker/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Cop1ouss/ccna-tracker/ci.yml?style=flat-square&label=CI&labelColor=1e1e2e&color=a6e3a1"></a>
  <a href="https://github.com/Cop1ouss/ccna-tracker/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://img.shields.io/github/actions/workflow/status/Cop1ouss/ccna-tracker/codeql.yml?style=flat-square&label=CodeQL&labelColor=1e1e2e&color=89b4fa"></a>
  <a href="SECURITY.md"><img alt="Security policy" src="https://img.shields.io/badge/security-policy-f38ba8?style=flat-square&labelColor=1e1e2e"></a>
  <img alt="exam: 200-301" src="https://img.shields.io/badge/exam-200--301-89dceb?style=flat-square&labelColor=1e1e2e">
  <img alt="domains: 6/6" src="https://img.shields.io/badge/domains-6%2F6-a6e3a1?style=flat-square&labelColor=1e1e2e">
  <img alt="status: in progress" src="https://img.shields.io/badge/status-in%20progress-f9e2af?style=flat-square&labelColor=1e1e2e">
  <img alt="labs: Packet Tracer · GNS3" src="https://img.shields.io/badge/labs-Packet%20Tracer%20%C2%B7%20GNS3-89dceb?style=flat-square&labelColor=1e1e2e">
</p>

<p align="center">
  <a href="https://cop1ouss.github.io/ccna-tracker/"><img alt="ccna-tracker on desktop" src="assets/screenshot-desktop.png" width="72%"></a>
  <a href="https://cop1ouss.github.io/ccna-tracker/"><img alt="ccna-tracker on a phone" src="assets/screenshot-phone.png" width="22%"></a>
</p>

Companion to [`cisco-track`](https://github.com/Cop1ouss/cisco-track) — that repo
holds the Jeremy's IT Lab notes and Cisco Networking Academy coursework. This one
is the hands-on, gamified, test-prep side: labs, drills, flashcards, and boss
battles, built around the official CCNA 200-301 v1.1 blueprint (six domains,
in effect through Feb 2, 2027).

> **Heads up:** CCNA 200-301 **v2.0** goes live Feb 3, 2027, replacing v1.1
> the day after it retires. Confirmed against Cisco's own exam-topics PDF —
> v2.0 restructures this into **five** domains (not six) with different
> names/weights and a much heavier troubleshoot/diagnose emphasis, plus new
> topics (SFTP/SCP, storm control, RA guard, DNS-record troubleshooting,
> OSPFv3, agentic AI) that this repo doesn't cover yet. Everything here still
> targets v1.1 — a v2.0 restructure is a separate future project, not
> something to start until you've settled your own exam timeline.

## Structure

| Path | What lives here |
|---|---|
| `boss-battles/` | One file per exam domain — objective checklist, XP/status tracking, missed-question log (styled after the `secplus-tracker` Agent Dajoni system) |
| `ultimate-guide/` | One synthesized study file per domain, built from cross-referencing `cisco-track`'s course notes against each boss battle's objective checklist — merged explanations, real IOS command examples, and honestly-flagged gaps where no note covers a blueprint objective |
| `practice-questions/` | Original practice questions with hidden-answer explanations, organized by domain and weighted toward higher-blueprint-weight domains |
| `mock-exams/` | Full-length mocks at the real domain weight distribution — questions and answer key kept in separate files so a mock can be taken cold |
| `flashcards/ccna-core-facts.csv` | Anki-importable deck — ADs, port numbers, HTTP codes, STP/HSRP facts |
| `scripts/subnet_drill.py` | Timed CLI subnetting quiz generator (stdlib only) |
| `scripts/coverage.py` | Readiness dashboard — reads Status/XP from the boss battles and prints per-domain and blueprint-weighted overall readiness |
| `scripts/sync_anki.py` | Pushes new/updated flashcards into a running Anki instance via AnkiConnect, instead of manual CSV re-import |
| `packet-tracer-labs/` | Self-imposed Packet Tracer challenge log |
| `gns3-topologies/` | Real(er) routing/switching topologies tied into the home lab |
| `tryhackme-log/` | Networking-focused CTF rooms completed |
| `STUDY-PLAN.md` | Suggested weekly rhythm, mapped to the Todoist recurring tasks |

## Quick start

```bash
# Run a subnetting drill
python3 scripts/subnet_drill.py -n 15

# Check overall exam readiness (per-domain + blueprint-weighted total)
python3 scripts/coverage.py

# Push new/updated flashcards into a running Anki instance (requires the
# AnkiConnect add-on: https://ankiweb.net/shared/info/2055492159)
python3 scripts/sync_anki.py --dry-run   # preview
python3 scripts/sync_anki.py             # apply

# Or import flashcards/ccna-core-facts.csv into Anki manually as a new deck
# File > Import in Anki, comma-separated, first line as header
```

## Exam blueprint (v1.1, live through Feb 2, 2027)

| Domain | Weight |
|---|---|
| Network Fundamentals | 20% |
| Network Access | 20% |
| IP Connectivity | 25% |
| IP Services | 10% |
| Security Fundamentals | 15% |
| Automation & Programmability | 10% |

IP Connectivity is the single biggest domain — weight your study time there.
v1.1 added generative/predictive AI & ML topics and swapped Puppet/Chef
references for Ansible/Terraform in the automation domain.

## Resources

**Video** — [Jeremy's IT Lab](https://www.youtube.com/@JeremysITLab) (primary), [NetworkChuck](https://www.youtube.com/@NetworkChuck) (fun supplement)
**Hands-on** — Cisco Packet Tracer, [GNS3](https://www.gns3.com/) / [EVE-NG](https://www.eve-ng.net/)
**Subnetting** — `scripts/subnet_drill.py`, [subnettingpractice.com](https://subnettingpractice.com/)
**CTF-style** — [TryHackMe](https://tryhackme.com/) networking rooms

## Related

Same "Networking & Certs" category as [`cisco-track`](https://github.com/Cop1ouss/cisco-track) and
[`secplus-tracker`](https://github.com/Cop1ouss/secplus-tracker).


## Project docs

| | |
| --- | --- |
| 📋 [PRD](docs/PRD.md) | The problem, the goal, scope and the finish line |
| 🛡️ [Security policy](SECURITY.md) | How to report a vulnerability privately |
| ⚖️ [License](LICENSE) | MIT |
| 🧪 [CI](.github/workflows/ci.yml) | What runs on every pull request |

---

<p align="center"><sub>Built by <a href="https://github.com/Cop1ouss">Dajoni Gomez</a> · part of the <a href="https://cop1ouss.github.io/Cop1ouss/">Uncook</a> journey log</sub></p>
