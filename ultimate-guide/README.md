![CCNA Tracker banner](../assets/banner.svg)

# Ultimate Guide

One synthesized study file per exam domain, built by cross-referencing every relevant note across [`cisco-track`](https://github.com/Cop1ouss/cisco-track)'s courses against the objective checklist in the matching `boss-battles/*.md` file. Overlapping content is merged into one explanation per objective; real IOS command examples are kept from source notes rather than rewritten generically; anything the blueprint expects that no note actually covers is flagged as a gap, not invented.

| File | Weight | Status |
|---|---|---|
| [`network-fundamentals.md`](network-fundamentals.md) | 20% | ✅ mostly solid — a few named-but-uncommanded items (SFP/SFP+, anycast, two-tier/spine-leaf) |
| [`network-access.md`](network-access.md) | 20% | ⚠️ VLAN/STP/EtherChannel core solid — CDP/LLDP, loop guard, BPDU filter, WLC deployment models are gaps |
| [`ip-connectivity.md`](ip-connectivity.md) | 25% | ❌ static routing + HSRP solid, but **single-area OSPFv2 has zero source content** — the single biggest gap in the repo |
| [`ip-services.md`](ip-services.md) | 10% | ❌ DHCP/DNS/SSH solid — NTP, SNMP, syslog, QoS, FTP have zero source content |
| [`security-fundamentals.md`](security-fundamentals.md) | 15% | ⚠️ L2 security + threat concepts solid — ACLs, TACACS+, VPN concepts, EAP terminology are gaps |
| [`automation-programmability.md`](automation-programmability.md) | 10% | ❌ thinnest domain in the repo — 5 of 6 sub-topics have zero source content |

**Reading this before a study session:** each file opens with a legend (✅ well covered · ⚠️ partial · ❌ gap) and closes with a domain summary table plus a one-line list of what specifically needs outside study. Treat ❌ items as "build from scratch," not "review" — nothing was invented to paper over a gap, per the brief this guide was built against.

Run `python3 ../scripts/coverage.py` for the numeric readiness dashboard once you've started actually working the boss-battle checklists — this guide tells you *what's missing from your notes*, `coverage.py` tells you *what you've mastered so far*.
