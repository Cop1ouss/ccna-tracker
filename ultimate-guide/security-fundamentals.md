# Security Fundamentals (15%)

![Security Fundamentals](https://img.shields.io/badge/domain-Security%20Fundamentals-a78bfa) ![Weight](https://img.shields.io/badge/weight-15%25-a78bfa)

Synthesized from **Networking Basics** (c1), **SRWE** (c3), and **ENSA** (c5). Skeleton is the checklist in [`boss-battles/05-security-fundamentals.md`](../boss-battles/05-security-fundamentals.md). Course 05 closed the ACL and AAA gaps and added VPN concepts.

**Important scope note:** the brief for this domain asked me to also pull from Cybersecurity Associate (formerly CyberOps Associate/CBROPS), Network Defense, Network Security, Cyber Threat Management, Endpoint Security, and Introduction to Cybersecurity for angles the CCNA courses miss. I checked — **none of these exist as built content in cisco-track.** They appear exactly once, as five bullet points in a "Junior Cybersecurity Analyst" roadmap section on the homepage, listed as a *planned future track* alongside the badges/certs they lead to. There are no modules, no objectives, no labs — just the course names as a wishlist. Everything below is Cisco networking's own security content (c1 + c3), not cybersecurity-course content, because that's genuinely all that exists to synthesize from right now.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ✅ Core security concepts: threats, vulnerabilities, exploits, mitigation techniques

Good two-course arc. **c1 1.7 (Network Security Basics)** covers threats at the home-network level — malware, phishing, supply-chain risk, default-credential exposure — paired with the countermeasures (strong auth, WPA3, firmware updates, firewall concept). **c3 3.10 (LAN Security Concepts)** goes deeper into campus-specific attacks: MAC flooding, VLAN hopping, DHCP spoofing/starvation, ARP spoofing. What makes this genuinely well-taught rather than just a vocabulary list: **SRWE-L10** deliberately demonstrates an attack (MAC flooding, rogue DHCP) *before* SRWE-L11 teaches the mitigation, so each threat is mapped to its specific defense rather than left abstract.

## ✅ AAA concepts: authentication, authorization, accounting

**c3 3.10** names AAA/802.1X as a topic, and **ENSA 5.3 (Network Security: AAA, RADIUS/TACACS+, VPN Concepts)** now breaks it down and configures it: `aaa new-model` + a local user database, with AAA login enforced on console and VTY lines instead of a flat password. **ENSA-L3** is the hands-on version of exactly this. Accounting itself is still concept-level (no `aaa accounting` config), but authentication and authorization are both real IOS commands now, not just a named objective.

## ⚠️ Password/access policies: complexity, MFA, RADIUS vs. TACACS+ (conceptual)

**c1 1.7** explicitly names strong authentication and MFA as a learning objective, and every device-config lab across c2/c3 (NE-CAP-a, SRWE-L1a) reinforces the *habit* of strong passwords (`enable secret`, `service password-encryption`).

✅ **RADIUS vs. TACACS+ comparison closed by ENSA 5.3** — encryption scope, transport, and AAA separation are now explicitly taught and compared, on top of SRWE-L13b's earlier passing WPA3-Enterprise/RADIUS mention. Still no TACACS+ CLI configuration anywhere in cisco-track (the module stays conceptual for TACACS+), so know the comparison from real course content, but expect to configure TACACS+ from outside knowledge if the exam asks for syntax.

## ✅ Standard IPv4 ACLs: purpose, placement, wildcard masks

**Closed by ENSA 5.4 (ACLs for IPv4)** — wildcard-mask math, standard ACL syntax (1-99), extended ACL syntax (100-199), `ip access-group in/out`, and the placement rule (standard near destination, extended near source) are all taught. **ENSA-L4a** blocks a single host from a server subnet with a standard ACL; **ENSA-L4b** builds an extended ACL permitting only HTTP/HTTPS and includes a planted-misconfiguration troubleshooting exercise (wrong wildcard, wrong placement, missing permit). This also now sources `practice-questions` Q5's standard-ACL question from real course material instead of the bank alone.

## ✅ Layer 2 security: DHCP snooping, port security (violation modes)

The best-covered item in this domain, with real commands from **SRWE-L11a** and **SRWE-L11b**:

```
interface fa0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```
```
show port-security interface fa0/1
show port-security address
```
```
ip dhcp snooping
ip dhcp snooping vlan 10
interface g0/1
 ip dhcp snooping trust
```
```
ip arp inspection vlan 10
interface g0/1
 ip arp inspection trust
```

⚠️ One nuance on **violation modes**: the lab only configures and verifies `shutdown` mode (the port err-disables). The checklist wants all the violation modes distinguished — `restrict` (drop + log, port stays up) and `protect` (silently drop) are correctly explained in this repo's own `practice-questions` Q6, but again that's bank content, not something demonstrated in a cisco-track lab. Know `shutdown` hands-on; know `restrict`/`protect` from the question bank, not from a lab.

## ✅ WLAN security: WPA2 vs. WPA3, EAP concepts

**c1 1.7**, **c3 3.12**, and **c3 3.13** consistently reinforce the same correct 2026 framing across all three touches: WPA3 is the default, WPA2 is the legacy fallback only for device-limited scenarios, never WEP, never Open. **SRWE-L13a/b** puts this into practice — WPA3-Personal (PSK) for a standard WLAN, then WPA3-Enterprise (802.1X, RADIUS-backed) for a VLAN-mapped enterprise WLAN, correctly distinguishing PSK from Enterprise auth.

⚠️ **EAP itself is never named.** 802.1X is covered as the *framework* (port-based access control triggering RADIUS authentication), but the actual EAP methods the exam might reference (EAP-TLS, PEAP, EAP-FAST) don't appear — my notes get you to "802.1X hands off to a RADIUS server" without the EAP vocabulary layered on top.

## ⚠️ Remote access VPN concepts (site-to-site vs. remote-access, high level)

**Concept-level gap closed by ENSA 5.3** — site-to-site vs. remote-access VPN is now distinguished, plus IPsec at a high level. Still no SSL VPN mention and no hands-on config (the module is concept-only here by design, no lab attached to this sub-topic), so know the distinction from real content but don't expect a worked example to point to.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Core security concepts (threats/mitigation) | ✅ |
| AAA concepts (A/A/A) | ✅ (closed by ENSA 5.3 — authentication/authorization configured, accounting still concept-only) |
| Password/access policies, MFA, RADIUS vs. TACACS+ | ⚠️ (comparison closed by ENSA 5.3; TACACS+ CLI still ❌) |
| Standard IPv4 ACLs, wildcard masks | ✅ (closed by ENSA 5.4) |
| Layer 2 security (DHCP snooping, port security) | ✅ (only `shutdown` violation mode hands-on) |
| WLAN security (WPA2/WPA3, EAP) | ✅ WPA2/WPA3 · ⚠️ EAP terminology missing |
| Remote access VPN concepts | ⚠️ (closed at concept level by ENSA 5.3; no hands-on config) |

**Real gaps left before test day:** TACACS+ CLI configuration and EAP method names (EAP-TLS, PEAP, EAP-FAST) — both still genuinely outside-study topics. Everything else in this domain, including ACLs and AAA (this domain's two biggest former holes), is now backed by real course content. Also still worth flagging: the cybersecurity-adjacent courses (CyberOps, Network Defense, etc.) remain a wishlist item on the homepage, not built content — that's a repo gap, not just a study gap.
