# IP Services (10%)

![IP Services](https://img.shields.io/badge/domain-IP%20Services-f472b6) ![Weight](https://img.shields.io/badge/weight-10%25-f472b6)

Synthesized from **Networking Basics** (c1), **Networking Essentials** (c2), and **SRWE** (c3). Skeleton is the checklist in [`boss-battles/04-ip-services.md`](../boss-battles/04-ip-services.md). This is the domain with the most individually-gapped items — several services just never come up in either course.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ⚠️ NAT: static, dynamic, and PAT (port address translation)

**c1 1.5 (Connect to the Internet)** covers NAT at the conceptual level only — it's a named topic ("NAT overview") and a stated objective ("Describe NAT conceptually"), framed as *why* a home router hides private addresses behind one public IP.

❌ **Gap:** no course ever configures NAT on IOS. I searched every lab guide for `ip nat inside`/`ip nat outside`/`ip nat inside source` and found nothing — the concept is understood at the "what and why" level but there's no worked static NAT, dynamic NAT (with an access-list + pool), or PAT/overload configuration anywhere in cisco-track. This repo's own `practice-questions/network-access-services-security-automation.md` Q3 tests PAT recognition conceptually, but that question isn't sourced from cisco-track notes — it's outside knowledge already in the practice bank. Treat NAT CLI syntax as untested.

## ❌ NTP: client/server configuration

**Real gap** — NTP does not appear anywhere in cisco-track, not as a topic, not as a lab, not as a passing mention. No `ntp server`, no `show clock`, no `show ntp status`. Needs to be learned from scratch.

## ✅ DHCP: client and relay concepts, DHCP options basics

The strongest item in this domain — three courses reinforce each other with real, escalating depth. **c2 2.7** teaches the DORA exchange, scope/lease lifecycle, and reservations vs. exclusions conceptually (**NE-L7** stands up a basic scope). **c3 3.7** goes to full IOS config with relay:

```
ip dhcp excluded-address 10.0.2.1 10.0.2.10
ip dhcp pool LAN_B
 network 10.0.2.0 255.255.255.0
 default-router 10.0.2.1
 dns-server 8.8.8.8
```
```
interface g0/0
 ip helper-address <R-A-interface-ip>
```
```
show ip dhcp binding
```

The pool's `default-router`/`dns-server` lines *are* DHCP options in practice (option 3 and option 6), even though my notes never use the word "option" to name them generically — know the syntax, just connect it to the "options" terminology if the exam phrases a question that way. **c3 3.8** extends the same pattern to DHCPv6 (stateful, via `ipv6 dhcp pool` + `ipv6 nd managed-config-flag`) and SLAAC — both dynamic-addressing paths for IPv6 are covered, not just DHCPv4.

## ✅ DNS: lookup process, role in network operations

**c2 2.11 (Application Layer Services & Network Testing)** covers DNS resolution and record types (A, AAAA, MX, CNAME) alongside HTTPS/TLS 1.3 and email protocols, and **NE-L11a** builds a working DHCP+DNS+HTTP service stack — a client gets an address, resolves a name, and loads a page, which is DNS's actual operational role rather than just definitions. Good conceptual-to-practical bridge.

## ❌ SNMP: basic operation and use case

**Real gap** — zero mentions anywhere in cisco-track. No community strings, no `snmp-server` commands, no MIB/OID/trap vocabulary. Needs outside study.

## ❌ Syslog: severity levels, use case

**Real gap** in cisco-track specifically — no `logging` commands, no severity-level table, nothing. Worth noting: this repo's own `practice-questions/network-access-services-security-automation.md` Q4 already tests syslog severity 7 = Debugging correctly, but that question predates this synthesis and isn't traceable to cisco-track notes — it's accurate, just not something these notes taught. Learn syslog severity 0–7 from outside material; the practice question is a good self-check once you have.

## ✅ SSH: configuration and why it replaces Telnet

Very well covered, and the "why" is baked into the framing rather than left implicit — every device-configuration lab in c3 explicitly enforces SSH-only, Telnet-disabled as the baseline standard (not an optional hardening step). From **SRWE-L1a** / **NE-CAP-a**:

```
ip domain-name lab.local
crypto key generate rsa modulus 2048
ip ssh version 2
username admin secret Adm1n!
line vty 0 4
 login local
 transport input ssh
```

The repeated emphasis across both courses — SSH v2 only, local user auth, Telnet never enabled — means this isn't just "known," it's drilled as the default posture for every device built in these labs.

## ❌ QoS: basic concepts — marking, queuing, congestion management

**Confirmed full gap**, and the same one already flagged in `network-access.md`'s WLAN section — QoS does not appear anywhere in cisco-track at all, conceptual or configured. No marking (DSCP/CoS), no queuing models, no congestion-management vocabulary. This is a from-scratch topic for the exam.

## ⚠️ TFTP/FTP: file transfer use cases (IOS image/config backup)

**TFTP is solid** — **SRWE-L1b** walks through the exact operational pattern the exam cares about (backup before risky changes, restore after a wipe):

```
copy startup-config tftp:
```
```
copy tftp: running-config
```

❌ **FTP itself is a gap** — the boss-battle checklist pairs TFTP with FTP, but FTP never appears anywhere in cisco-track. Know that FTP is the connection-oriented, authenticated alternative to TFTP's simple/unauthenticated UDP transfer, but there's no worked example to point to.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| NAT (static/dynamic/PAT) | ⚠️ concept only, no CLI |
| NTP | ❌ |
| DHCP (client/relay/options) | ✅ |
| DNS | ✅ |
| SNMP | ❌ |
| Syslog | ❌ (self-check question exists but isn't sourced from notes) |
| SSH (vs. Telnet) | ✅ |
| QoS | ❌ |
| TFTP/FTP | ⚠️ (TFTP ✅, FTP ❌) |

**Real gaps to close before test day:** NAT CLI configuration (static/dynamic/PAT), NTP, SNMP, syslog, QoS, and FTP. That's five of nine sub-topics with no source material at all — despite being only 10% of the exam, this domain needs the most outside-source work per point of weight of any domain in the blueprint.
