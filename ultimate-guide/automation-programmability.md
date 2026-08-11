# Automation & Programmability (10%)

![Automation & Programmability](https://img.shields.io/badge/domain-Automation%20%26%20Programmability-fb923c) ![Weight](https://img.shields.io/badge/weight-10%25-fb923c)

Synthesized from **ENSA** (c5) — this domain had no source material at all until Course 05 shipped. Skeleton is the checklist in [`boss-battles/06-automation-programmability.md`](../boss-battles/06-automation-programmability.md). Four of six sub-topics are now covered; Terraform and AI/ML in network ops are the remaining from-scratch items.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ⚠️ Impact of automation on traditional network management

Still not taught head-on as its own objective (fewer manual CLI touches, config drift, intent-based networking aren't named explicitly anywhere), but **ENSA 5.8**'s traditional-vs-controller-based comparison and **5.9**'s automation modules both frame the *operational* cost difference — **ENSA-L8** has you write out, step by step, what a config change costs under per-device CLI vs. a hypothetical controller push. That's the practical substance of this objective even without the vocabulary ("config drift," "intent-based networking") attached to it. Know those two terms from outside material if the exam names them directly.

## ✅ Traditional (device-by-device) vs. controller-based/SDN architectures

**Closed by ENSA 5.8 (Network Architecture: Traditional vs. Controller-Based)** — a dedicated module now contrasts traditional device-by-device CLI management against controller-based/SDN, explains control/data-plane centralization, names northbound vs. southbound APIs (concept-level), and identifies Cisco's controller platforms (DNA Center / Catalyst Center, Meraki). **ENSA-L8** documents the operational tradeoff across a 10-device topology. This is the general SDN/controller-based-networking concept the blueprint means here — separate from the WLC-specific autonomous-vs-controller-based AP architecture already covered in `network-access.md`.

## ✅ REST-based APIs: CRUD operations, HTTP verbs (GET/POST/PUT/DELETE), common response codes

**Closed by ENSA 5.9 (Network Automation & Programmability)** — GET/POST/PUT/DELETE and common response codes (200/401/404/500) are now taught, and **ENSA-L9a** makes it hands-on: register for a free Cisco DevNet Sandbox account and send a real GET request (via Postman or curl) to an always-on IOS-XE device, then read the JSON response. This also now sources `practice-questions` Q7's HTTP 404 question from real course material instead of the bank alone.

## ⚠️ Configuration management tools: Ansible and Terraform

**Ansible closed by ENSA 5.9** — agentless (SSH-based), YAML playbooks, and why it's agentless are all taught, with **ENSA-L9b** running an actual two-task playbook (using the `cisco.ios` collection) against a DevNet Sandbox device to gather facts. This also sources `practice-questions` Q8's "Ansible is agentless" from real content now. **Terraform is still a full gap** — not mentioned anywhere in cisco-track, push-vs-pull and HCL syntax remain outside-study topics.

## ✅ JSON data encoding: reading and interpreting simple JSON objects

**Closed as taught content by ENSA 5.9** — beyond the tracker app's own `JSON.parse()`/`JSON.stringify()` plumbing, the module now has you read and interpret a real JSON API response from the DevNet Sandbox GET request in ENSA-L9a, which is exactly the key/value-reading skill the blueprint tests.

## ❌ AI/ML in network operations: generative and predictive use cases (new in v1.1 blueprint)

**Full gap, and the most surprising one.** `index.html`'s own `<meta>` description advertises the whole tracker as *"2026 content... aligned to CCNA 200-301 v1.1"* — and v1.1's headline addition over the previous blueprint version is exactly this AI/ML objective — but the objective itself was never actually written into any module. Nothing on generative AI use cases (e.g. Cisco AI Assistant, chatbot-driven troubleshooting) or predictive use cases (e.g. AI-driven capacity/failure prediction) appears anywhere.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Automation's impact on network management | ⚠️ (practical substance covered via ENSA-L8; terminology not named) |
| Traditional vs. controller-based/SDN | ✅ (closed by ENSA 5.8) |
| REST APIs (CRUD, verbs, response codes) | ✅ (closed by ENSA 5.9) |
| Ansible / Terraform | ⚠️ (Ansible ✅ closed by ENSA 5.9, Terraform ❌) |
| JSON encoding | ✅ (closed by ENSA 5.9 — real API response, not just app plumbing) |
| AI/ML in network ops | ❌ |

**Real gaps left before test day:** Terraform (push vs. pull, HCL) and AI/ML in network ops (v1.1's newest blueprint addition — still not written into any module, despite the tracker's own metadata claiming v1.1 alignment). Everything else in this domain — SDN/controller-based architecture, REST APIs, Ansible, and JSON — went from zero source material to real course content once Course 05 shipped. This is no longer the thinnest domain in the repo.
