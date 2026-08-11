# Automation & Programmability (10%)

![Automation & Programmability](https://img.shields.io/badge/domain-Automation%20%26%20Programmability-fb923c) ![Weight](https://img.shields.io/badge/weight-10%25-fb923c)

Synthesized from **ENSA** (c5) — this domain had no source material at all until Course 05 shipped. Skeleton is the checklist in [`boss-battles/06-automation-programmability.md`](../boss-battles/06-automation-programmability.md). Four of six sub-topics come from ENSA; Terraform and AI/ML in network ops are outside-study additions written in directly (marked as such below — no cisco-track lab backs them).

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ⚠️ Impact of automation on traditional network management

Still not taught head-on as its own objective (fewer manual CLI touches, config drift, intent-based networking aren't named explicitly anywhere), but **ENSA 5.8**'s traditional-vs-controller-based comparison and **5.9**'s automation modules both frame the *operational* cost difference — **ENSA-L8** has you write out, step by step, what a config change costs under per-device CLI vs. a hypothetical controller push. That's the practical substance of this objective even without the vocabulary ("config drift," "intent-based networking") attached to it. Know those two terms from outside material if the exam names them directly.

## ✅ Traditional (device-by-device) vs. controller-based/SDN architectures

**Closed by ENSA 5.8 (Network Architecture: Traditional vs. Controller-Based)** — a dedicated module now contrasts traditional device-by-device CLI management against controller-based/SDN, explains control/data-plane centralization, names northbound vs. southbound APIs (concept-level), and identifies Cisco's controller platforms (DNA Center / Catalyst Center, Meraki). **ENSA-L8** documents the operational tradeoff across a 10-device topology. This is the general SDN/controller-based-networking concept the blueprint means here — separate from the WLC-specific autonomous-vs-controller-based AP architecture already covered in `network-access.md`.

## ✅ REST-based APIs: CRUD operations, HTTP verbs (GET/POST/PUT/DELETE), common response codes

**Closed by ENSA 5.9 (Network Automation & Programmability)** — GET/POST/PUT/DELETE and common response codes (200/401/404/500) are now taught, and **ENSA-L9a** makes it hands-on: register for a free Cisco DevNet Sandbox account and send a real GET request (via Postman or curl) to an always-on IOS-XE device, then read the JSON response. This also now sources `practice-questions` Q7's HTTP 404 question from real course material instead of the bank alone.

## ✅ Configuration management tools: Ansible and Terraform

**Ansible closed by ENSA 5.9** — agentless (SSH-based), YAML playbooks, and why it's agentless are all taught, with **ENSA-L9b** running an actual two-task playbook (using the `cisco.ios` collection) against a DevNet Sandbox device to gather facts. This also sources `practice-questions` Q8's "Ansible is agentless" from real content now.

**Terraform — outside-study addition** (no cisco-track lab backs this, added directly). The exam-testable distinction is *what each tool is for*, not just syntax: **Ansible configures things that already exist** (push config to a running router/switch); **Terraform provisions the things themselves** (spins up the VM, the VPC, the cloud network interface in the first place) — infrastructure-as-code, not configuration management. Terraform is written in **HCL** (HashiCorp Configuration Language), is fully declarative (you describe the end state, not the steps), and tracks everything it created in a **state file** so it knows what to change/destroy on the next run — Ansible has no equivalent state tracking, it just runs the playbook's tasks top to bottom every time.

```hcl
resource "aws_instance" "lab_router" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.micro"
}
```
Workflow: `terraform init` (download providers) → `terraform plan` (preview the diff against current state) → `terraform apply` (make it real) → `terraform destroy` (tear it down). If a question is about **provisioning cloud/virtual infrastructure that doesn't exist yet**, that's Terraform; if it's about **pushing config to devices that already exist**, that's Ansible.

## ✅ JSON data encoding: reading and interpreting simple JSON objects

**Closed as taught content by ENSA 5.9** — beyond the tracker app's own `JSON.parse()`/`JSON.stringify()` plumbing, the module now has you read and interpret a real JSON API response from the DevNet Sandbox GET request in ENSA-L9a, which is exactly the key/value-reading skill the blueprint tests.

## ✅ AI/ML in network operations: generative and predictive use cases (new in v1.1 blueprint)

**Outside-study addition** (no cisco-track lab backs this, added directly — `index.html` advertises v1.1 alignment but never actually wrote this objective into a module, and it's v1.1's headline addition over the prior blueprint version, so it's worth having cold). The blueprint splits this into two distinct use-case categories:

**Generative AI use cases** — the AI produces new content/output on request. In network ops this means natural-language-to-config tools (describe what you want in plain English, the assistant drafts the CLI), chatbot-driven troubleshooting assistants that can query device state and suggest a fix, and documentation/summarization (turning a pile of `show tech-support` output into a plain-English incident summary). Cisco's own example is the **AI Assistant** built into Catalyst Center/DNA Center.

**Predictive/ML use cases** — the model forecasts something from historical data rather than generating new content. In network ops this means **anomaly detection** (learning a traffic baseline so it can flag a deviation before a human would notice), **predictive capacity planning** (forecasting when a link or CPU will saturate before it happens), and **predictive failure/maintenance** (flagging hardware likely to fail from early signal patterns — fan wear, rising error counters — before it actually goes down).

Exam framing: if the scenario describes the AI **creating** something (a config, a summary, an answer to a question) — that's generative. If it describes the AI **forecasting or flagging a pattern** from existing data — that's predictive/ML. Both fall under the same "AIOps" umbrella: using AI to reduce how much of network operations requires a human staring at dashboards.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Automation's impact on network management | ⚠️ (practical substance covered via ENSA-L8; terminology not named) |
| Traditional vs. controller-based/SDN | ✅ (closed by ENSA 5.8) |
| REST APIs (CRUD, verbs, response codes) | ✅ (closed by ENSA 5.9) |
| Ansible / Terraform | ✅ (Ansible via ENSA 5.9, Terraform added directly below) |
| JSON encoding | ✅ (closed by ENSA 5.9 — real API response, not just app plumbing) |
| AI/ML in network ops | ✅ (added directly below) |

**No real gaps left in this domain.** The only soft spot is the first item — automation's operational impact has real practical substance via ENSA-L8, but the specific terms ("config drift," "intent-based networking") aren't named anywhere in cisco-track, so know those two words from outside material if a question uses them directly. Everything else — SDN/controller-based architecture, REST APIs, Ansible, Terraform, JSON, and AI/ML — now has real content, either from Course 05 or written in above. This went from the thinnest domain in the repo to a fully covered one.
