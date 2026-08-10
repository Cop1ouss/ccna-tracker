# Practice Questions — Network Fundamentals & IP Connectivity

Original questions, not pulled from a paid test bank. Answers and explanations
below each question — cover them while you attempt it.

---

## Network Fundamentals

**Q1.** You need to connect two switches 150 meters apart in a campus building,
with no plans to upgrade beyond 1 Gbps. Copper UTP is out of range. What's the
most cost-effective media choice?
<details><summary>Answer</summary>
Multi-mode fiber. Single-mode is overkill (and pricier) for short campus runs;
UTP maxes out around 100m for reliable Gigabit Ethernet.
</details>

**Q2.** A host has the IPv6 address `2001:db8:acad::1`. What type of address is this?
<details><summary>Answer</summary>
Global unicast address — the `2001:db8::/32` range is reserved for documentation,
but structurally it's formatted as a GUA (routable, globally unique prefix).
</details>

**Q3.** Two switch ports are set to auto/auto for speed and duplex but the link
shows as half-duplex on one side. What's the likely cause?
<details><summary>Answer</summary>
A duplex mismatch — usually because one side isn't actually set to auto (hard-set
to full or half on one end). Auto-negotiation failure like this is a classic
"works but slow with lots of errors" symptom.
</details>

---

## IP Connectivity

**Q4.** A router has these routes to reach 10.1.1.0/24:
- Static route: 10.1.1.0/24, AD 1
- OSPF route: 10.1.1.0/25, AD 110
- OSPF route: 10.1.1.0/24, AD 110

A packet destined for 10.1.1.5 arrives. Which route wins?
<details><summary>Answer</summary>
The OSPF /25 route. Longest-prefix match is evaluated *before* administrative
distance — AD only breaks ties when multiple routes have the **same** prefix length.
</details>

**Q5.** Two routers are running single-area OSPFv2 but never form a full
adjacency — they stay stuck in 2-WAY. What's the most likely cause on a
multi-access (Ethernet) segment?
<details><summary>Answer</summary>
Expected behavior if they're both DROTHER (neither is DR/BDR) — DROTHERs stay in
2-WAY with each other by design on broadcast multi-access networks. Only DR/BDR
form FULL with everyone.
</details>

**Q6.** HSRP is configured with Router A at priority 110 and Router B at
priority 100 (default preempt off). Router A reboots. What happens when it
comes back online?
<details><summary>Answer</summary>
Router B stays active. Without preemption enabled, a higher-priority router
that returns after an election does NOT automatically reclaim the active role.
</details>

---

*Add your own missed-question entries to the relevant boss-battle file, not here — this file is a static question bank.*
