# Security policy

## Supported versions

Only the latest version on the default branch is supported. CCNA Tracker is deployed straight from it, so a fix lands for everyone as soon as it is merged.

## What this project handles

CCNA Tracker has no backend, no accounts and no analytics. It stores nothing; the Python scripts only read files in this repo, and `sync_anki.py` talks to a local AnkiConnect on `127.0.0.1`. Nothing you enter is sent to a server I run.

## Reporting a vulnerability

Please **don't open a public issue** for a security problem.

1. Go to the [Security tab](https://github.com/Cop1ouss/ccna-tracker/security) and click **Report a vulnerability**. That opens a private advisory only you and I can see.
2. Include what you found, how to reproduce it, and what an attacker could do with it.

I'll acknowledge the report within **3 days**, share a fix plan within **7 days**, and credit you in the release notes unless you'd rather stay anonymous.

## How this repo is protected

- **Dependabot** checks dependencies and GitHub Actions every week and opens update PRs.
- **CodeQL** scans the code on every pull request and once a week.
- **Secret scanning and push protection** block committed API keys and tokens.
- **CI** must pass before anything merges into the default branch.

---

<sub>© 2026 Dajoni Gomez · Uncook™ · part of the [journey log](https://cop1ouss.github.io/Cop1ouss/)</sub>
