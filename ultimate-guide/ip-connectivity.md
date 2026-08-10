# IP Connectivity (25%) — biggest domain

![IP Connectivity](https://img.shields.io/badge/domain-IP%20Connectivity-fbbf24) ![Weight](https://img.shields.io/badge/weight-25%25-fbbf24)

Synthesized from **Networking Essentials** (c2) and **SRWE** (c3). Skeleton is the checklist in [`boss-battles/03-ip-connectivity.md`](../boss-battles/03-ip-connectivity.md). This domain carries the most exam weight — and it's also where my notes have their single biggest hole. Read the OSPF section below before anything else.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ✅ Routing table components: routing decisions, administrative distance, longest-match lookup

Two courses reinforce each other well here. **c2 2.9 (Routing Between Networks)** introduces the routing table, connected/static/dynamic route types, administrative distance, and the default route. **c3 3.14 (Routing Concepts)** revisits it at CCNA depth — path determination, routing table codes, and explicitly states the evaluation order as an objective: *"Apply longest-prefix match"* and *"Compare route sources / AD."* My own practice-question bank already tests the correct precedence directly:

> Longest-prefix match is evaluated **before** administrative distance — AD only breaks ties when multiple routes have the **same** prefix length.

(See `practice-questions/network-fundamentals-and-ip-connectivity.md` Q4.) Both courses agree; no conflict to reconcile.

## ✅ Static routing: IPv4 and IPv6, default routes, floating static routes

Strong coverage with real, varied lab commands across **c2 2.9**, **c3 3.15**, and three separate labs (NE-L9, SRWE-L15a, SRWE-L15b):

```
ip route 10.0.30.0 255.255.255.0 10.0.12.2
ip route 10.0.3.0 255.255.255.0 10.0.12.2
```
```
ip route 0.0.0.0 0.0.0.0 <next-hop>
```
IPv4 + IPv6 together, three-router mesh (SRWE-L15a):
```
ipv6 unicast-routing
ip route 10.0.3.0 255.255.255.0 10.0.12.2
ipv6 route 2001:db8:3::/64 2001:db8:12::2
```
```
ip route 0.0.0.0 0.0.0.0 <next-hop>
ipv6 route ::/0 <next-hop-v6>
```
**Floating static** (SRWE-L15b) — the exact AD-based failover behavior, with a worked administrative-distance value:
```
ip route 10.0.2.0 255.255.255.0 10.0.12.2
ip route 10.0.2.0 255.255.255.0 10.0.99.2 5
```
Verification pattern is consistent throughout: `show ip route` / `show ipv6 route`, confirm only the AD-1 (or lower) route is installed while the primary path is up, confirm the backup installs automatically on failure.

## ❌ Single-area OSPFv2: neighbor adjacency, DR/BDR election, router ID, passive interfaces

**This is the largest single gap in the entire repo relative to how much the exam weights it.** I checked every course module and every lab guide: **"OSPF" appears exactly zero times as taught content anywhere in cisco-track.** The only two mentions of OSPF in the whole tracker are both *stretch-goal "challenge" suggestions* tacked onto the end of two labs —

- NE-L9 (Static Routing Across Three Routers): *"Replace all static routes with OSPF single-area and compare the routing tables."*
- SRWE-CAP (the SRWE capstone): *"Swap static routing for OSPF and add a second WAN link as a backup path."*

Both are framed as *optional extensions for after the lab*, not guided instruction — there's no walkthrough of `router ospf`, `network` statements with wildcard masks, neighbor states (Down→Init→2-Way→ExStart→Exchange→Loading→Full), DR/BDR election on multi-access segments, router-id selection, or passive-interface configuration anywhere. My own practice question bank has one OSPF question (2-WAY/DROTHER behavior), but it's testing a concept I clearly know from outside study, not from these notes.

**Bottom line:** neighbor adjacency, DR/BDR election, router ID, and passive interfaces all need to be learned from an outside source (Jeremy's IT Lab's OSPF series is the obvious fit given it's already your primary video resource) — nothing here to cross-reference.

## ❌ OSPF verification: `show ip ospf neighbor`, `show ip route ospf`, `show ip protocols`

Direct consequence of the gap above — none of these three commands appear anywhere in my notes. No `show` output to compare against, no sample neighbor table, no `show ip protocols` field walkthrough. Full gap, needs to be built from scratch alongside the OSPF concept study above.

## ✅ First-hop redundancy: HSRP concepts (active/standby, priority, preemption)

Solidly covered by **c3 3.9 (FHRP Concepts)** and lab **SRWE-L9**, with real config and the preemption gotcha correctly captured:

```
interface g0/0
 standby 1 ip 192.168.1.1
 standby 1 priority 110
 standby 1 preempt
```
```
show standby brief
```

The lab's verification steps explicitly confirm the two behaviors the exam likes to test — the higher-priority router becomes Active, and it only *reclaims* Active after a reboot if `preempt` is configured (matching practice-question Q6, which tests exactly this without-preempt trap). VRRP and GLBP are named in the topic list as comparison points but not configured — HSRP itself, the one actually on the checklist, is solid.

## ✅ Reading and interpreting a routing table under exam time pressure

**c3 3.14 + lab SRWE-L14** is built for exactly this: predict the path a packet takes through a routing table *before* verifying with `tracert`, explicitly training longest-prefix-match reasoning under the same conditions the exam demands. Combined with the repeated `show ip route` exposure across NE-L9, SRWE-L15a/b, and SRWE-L14, routing-table literacy has more hands-on repetition than almost any other item in this domain — it's just never been timed. Pair this with the mock exam's OSPF and static-routing questions for timed practice.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Routing table / AD / longest-match | ✅ |
| Static routing (IPv4/IPv6, default, floating) | ✅ |
| Single-area OSPFv2 | ❌ **zero content — largest gap in the repo** |
| OSPF verification commands | ❌ |
| HSRP (FHRP) | ✅ |
| Routing table reading under pressure | ✅ (untimed) |

**Real gaps to close before test day:** all of OSPFv2 — this alone is worth studying as if it were its own domain, given IP Connectivity is 25% of the exam and OSPF is roughly half of what this domain normally tests. Everything else in this domain (static routing, HSRP, routing-table literacy) is genuinely strong.
