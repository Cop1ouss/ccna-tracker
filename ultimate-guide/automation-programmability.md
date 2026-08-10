# Automation & Programmability (10%)

Skeleton is the checklist in [`boss-battles/06-automation-programmability.md`](../boss-battles/06-automation-programmability.md). This is the thinnest domain in the entire repo by a wide margin — five of six sub-topics have no source material in cisco-track at all. Read this one in full; there isn't a "well-covered" section to skim past.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ❌ Impact of automation on traditional network management

**Real gap.** No module in any course discusses how automation changes day-to-day network operations (fewer manual CLI touches, config drift, intent-based networking, etc.). Nothing to cross-reference.

## ⚠️ Traditional (device-by-device) vs. controller-based/SDN architectures

The one item in this domain with *something* behind it. **c2 2.12 (Network Design, Cloud & Virtualization)** lists *"Explain virtualization and SDN at a high level"* as a stated learning objective, and its topic list names cloud-managed networking platforms — Meraki and Catalyst Center — as the v1.1-blueprint-aligned example of controller-based management.

❌ But there's a real gap underneath that objective: the topic list itself never actually names "SDN," never contrasts it against traditional device-by-device CLI management, and never explains what a network controller *does* differently (centralized policy push, southbound/northbound APIs, abstraction from per-device config). Autonomous-vs-controller-based **AP** architecture is well covered (see `network-access.md`), but that's WLC-specific, not the general SDN/controller-based-networking concept the blueprint means here — don't let familiarity with WLC deployment models substitute for this.

## ❌ REST-based APIs: CRUD operations, HTTP verbs (GET/POST/PUT/DELETE), common response codes

**Full gap** in cisco-track — no module, topic, or lab touches REST, HTTP verbs, or status codes. Worth flagging: this repo's own `practice-questions/network-access-services-security-automation.md` Q7 already tests HTTP 404 correctly, but that question is pre-existing content in the practice bank, not something traceable to a cisco-track note. It's a good self-check once you've actually studied this from an outside source — not evidence the topic is covered.

## ❌ Configuration management tools: Ansible and Terraform

**Full gap.** Neither tool is mentioned anywhere in cisco-track — not agentless-vs-agent-based, not push-vs-pull, not YAML/HCL syntax. Same caveat as above: `practice-questions` Q8 already correctly tests "Ansible is agentless," but that's bank content, not cisco-track content.

## ❌ JSON data encoding: reading and interpreting simple JSON objects

**Full gap as *taught* content.** JSON does technically appear in cisco-track — but only inside the tracker app's own `index.html` JavaScript, where it calls `JSON.parse()`/`JSON.stringify()` to save your lab-completion progress to `localStorage`. That's the tracker's plumbing, not a networking lesson — no module ever presents a sample JSON API response and asks you to read a key/value pair out of it, which is what the blueprint actually tests.

## ❌ AI/ML in network operations: generative and predictive use cases (new in v1.1 blueprint)

**Full gap, and the most surprising one.** `index.html`'s own `<meta>` description advertises the whole tracker as *"2026 content... aligned to CCNA 200-301 v1.1"* — and v1.1's headline addition over the previous blueprint version is exactly this AI/ML objective — but the objective itself was never actually written into any module. Nothing on generative AI use cases (e.g. Cisco AI Assistant, chatbot-driven troubleshooting) or predictive use cases (e.g. AI-driven capacity/failure prediction) appears anywhere.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Automation's impact on network management | ❌ |
| Traditional vs. controller-based/SDN | ⚠️ objective named, no real depth |
| REST APIs (CRUD, verbs, response codes) | ❌ |
| Ansible / Terraform | ❌ |
| JSON encoding | ❌ (only exists as app plumbing, not a lesson) |
| AI/ML in network ops | ❌ |

**Real gaps to close before test day:** essentially this entire domain. Of the six sub-topics, one has a bare objective mention and the other five have nothing. Given this is 10% of the exam — the same weight as IP Services, which at least had DHCP/DNS/SSH solid — this domain should be treated as a from-scratch study block, not a review pass. It's also the strongest case in the whole repo for building an actual course module: right now "Automation & Programmability" exists as an exam-blueprint line item and nothing else in cisco-track.
