# IP Connectivity (25%) — biggest domain

![IP Connectivity](https://img.shields.io/badge/domain-IP%20Connectivity-fbbf24) ![Weight](https://img.shields.io/badge/weight-25%25-fbbf24)

Synthesized from **Networking Essentials** (c2), **SRWE** (c3), and **ENSA** (c5). Skeleton is the checklist in [`boss-battles/03-ip-connectivity.md`](../boss-battles/03-ip-connectivity.md). This is the highest-weighted domain in the exam, and now the strongest — OSPF, its former single biggest gap, was closed when Course 05 (ENSA) shipped.

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

## ✅ Single-area OSPFv2: neighbor adjacency, DR/BDR election, router ID, passive interfaces

**Closed by ENSA 5.1–5.2.** Previously the largest single gap in the repo — c2/c3 only ever mentioned OSPF as an optional stretch-goal on NE-L9 and SRWE-CAP, never as guided instruction. Course 05's **5.1 (Single-Area OSPFv2 Concepts)** now teaches the neighbor state machine (Down → Init → 2-Way → ExStart → Exchange → Loading → Full), why DR/BDR election happens on multi-access segments, router-ID selection order, and when a passive interface is the right call — with **ENSA-L1** stepping through adjacency formation packet-by-packet in Simulation mode. **5.2 (Configuration & Verification)** takes it hands-on: `router ospf` + `network` + wildcard mask, manual router-id/priority tuning, `passive-interface`/`passive-interface default` — drilled across **ENSA-L2a** (basic three-router single-area OSPF) and **ENSA-L2b** (passive interfaces + router-ID control via loopbacks + forced DR/BDR election). The old NE-L9/SRWE-CAP "swap static for OSPF" stretch goals are now backed by real guided content instead of being pure outside-study prompts.

## ✅ OSPF verification: `show ip ospf neighbor`, `show ip route ospf`, `show ip protocols`

Also closed by ENSA 5.2 — all three commands are named explicitly in the module's objectives and topics list, and verified end-to-end in ENSA-L2a/L2b (full adjacency + complete routing table) plus the ENSA capstone (5.10), which layers OSPF across 3+ routers alongside ACLs and NAT on one topology.

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
| Single-area OSPFv2 | ✅ (closed by ENSA 5.1–5.2) |
| OSPF verification commands | ✅ (closed by ENSA 5.2) |
| HSRP (FHRP) | ✅ |
| Routing table reading under pressure | ✅ (untimed) |

**No real gaps left in this domain.** Static routing, HSRP, routing-table literacy, and now OSPFv2 (concepts, config, and verification) are all backed by real course content. The one thing still worth doing yourself: timed practice — routing-table reading under pressure is covered but untimed.
