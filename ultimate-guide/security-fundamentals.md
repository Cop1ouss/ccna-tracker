# Security Fundamentals (15%)

![Security Fundamentals](https://img.shields.io/badge/domain-Security%20Fundamentals-a78bfa) ![Weight](https://img.shields.io/badge/weight-15%25-a78bfa)

Synthesized from **Networking Basics** (c1) and **SRWE** (c3). Skeleton is the checklist in [`boss-battles/05-security-fundamentals.md`](../boss-battles/05-security-fundamentals.md).

**Important scope note:** the brief for this domain asked me to also pull from CyberOps Associate, Network Defense, Network Security, Cyber Threat Management, Endpoint Security, and Introduction to Cybersecurity for angles the CCNA courses miss. I checked — **none of these exist as built content in cisco-track.** They appear exactly once, as five bullet points in a "Junior Cybersecurity Analyst" roadmap section on the homepage, listed as a *planned future track* alongside the badges/certs they lead to. There are no modules, no objectives, no labs — just the course names as a wishlist. Everything below is Cisco networking's own security content (c1 + c3), not cybersecurity-course content, because that's genuinely all that exists to synthesize from right now.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ✅ Core security concepts: threats, vulnerabilities, exploits, mitigation techniques

Good two-course arc. **c1 1.7 (Network Security Basics)** covers threats at the home-network level — malware, phishing, supply-chain risk, default-credential exposure — paired with the countermeasures (strong auth, WPA3, firmware updates, firewall concept). **c3 3.10 (LAN Security Concepts)** goes deeper into campus-specific attacks: MAC flooding, VLAN hopping, DHCP spoofing/starvation, ARP spoofing. What makes this genuinely well-taught rather than just a vocabulary list: **SRWE-L10** deliberately demonstrates an attack (MAC flooding, rogue DHCP) *before* SRWE-L11 teaches the mitigation, so each threat is mapped to its specific defense rather than left abstract.

## ⚠️ AAA concepts: authentication, authorization, accounting

Named but thin. **c3 3.10** lists "Describe AAA and 802.1X" as a stated learning objective and "AAA, 802.1X" as a topic, but nowhere in either course does my content actually break AAA into its three distinct pieces (authentication vs. authorization vs. accounting) or show a device-level AAA configuration (`aaa new-model`, `aaa authentication login`, etc.). It's referenced as a concept that exists, not taught piece-by-piece.

## ⚠️ Password/access policies: complexity, MFA, RADIUS vs. TACACS+ (conceptual)

**c1 1.7** explicitly names strong authentication and MFA as a learning objective, and every device-config lab across c2/c3 (NE-CAP-a, SRWE-L1a) reinforces the *habit* of strong passwords (`enable secret`, `service password-encryption`) even if "password complexity" isn't taught as its own rule set.

⚠️ **RADIUS** gets exactly one mention in the whole repo — SRWE-L13b's enterprise-WLAN lab says to point WPA3-Enterprise *"at a RADIUS/AAA server"* — but that's a WLAN-authentication context, not device-administration AAA, and it's a passing instruction, not an explanation of what RADIUS does or how it compares to anything.

❌ **TACACS+ does not appear anywhere in cisco-track.** There is no RADIUS-vs-TACACS+ comparison content at all (encryption scope, UDP vs. TCP, combined vs. separate AAA functions) despite that comparison being explicitly named in the checklist.

## ❌ Standard IPv4 ACLs: purpose, placement, wildcard masks

**Real gap.** I searched for `access-list`, `ACL`, and `wildcard` across every module and every lab guide in cisco-track and found zero matches — not a single mention, conceptual or configured. This repo's own `practice-questions/network-access-services-security-automation.md` Q5 already tests standard-ACL source-only filtering correctly, but that question isn't traceable to any cisco-track note — it's outside knowledge already sitting in the practice bank, not something these notes taught. ACL placement logic (standard ACLs go close to the destination; extended close to the source) and wildcard-mask arithmetic both need to be built from scratch.

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

## ❌ Remote access VPN concepts (site-to-site vs. remote-access, high level)

**Real gap** — VPN does not appear anywhere in cisco-track, in any form. No site-to-site vs. remote-access distinction, no IPsec, no SSL VPN, nothing. This is purely an outside-study topic for this domain.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Core security concepts (threats/mitigation) | ✅ |
| AAA concepts (A/A/A) | ⚠️ named, not broken down or configured |
| Password/access policies, MFA, RADIUS vs. TACACS+ | ⚠️ (RADIUS one passing mention; TACACS+ ❌) |
| Standard IPv4 ACLs, wildcard masks | ❌ |
| Layer 2 security (DHCP snooping, port security) | ✅ (only `shutdown` violation mode hands-on) |
| WLAN security (WPA2/WPA3, EAP) | ✅ WPA2/WPA3 · ⚠️ EAP terminology missing |
| Remote access VPN concepts | ❌ |

**Real gaps to close before test day:** standard ACLs and wildcard masks (zero content — this is a near-certain exam topic), TACACS+ and the RADIUS-vs-TACACS+ comparison, VPN concepts (site-to-site vs. remote-access), and EAP method names. AAA needs to go from "named" to "the three pieces explained." Also worth flagging to yourself: the cybersecurity-adjacent courses (CyberOps, Network Defense, etc.) you expected to lean on for a second angle on this domain haven't actually been built into cisco-track yet — that's a repo gap, not just a study gap.
