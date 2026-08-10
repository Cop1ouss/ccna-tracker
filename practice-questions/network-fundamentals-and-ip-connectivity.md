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

**Q7.** You need 6 usable host addresses per subnet with the least address
waste. What prefix length do you assign each subnet?
<details><summary>Answer</summary>
/29. 2^(32-29) - 2 = 6 usable hosts exactly. A /28 wastes addresses (14 usable
for a need of 6); a /30 (2 usable) is too small.
</details>

**Q8.** A network engineer has 192.168.10.0/24 and needs 4 subnets of unequal
size: one for 50 hosts, one for 25 hosts, and two for 10 hosts each. What
technique fits, and what's the first subnet mask you'd assign (for the
50-host subnet)?
<details><summary>Answer</summary>
VLSM. The 50-host subnet needs a /26 (62 usable) — the smallest block that
fits, sized before any of the smaller subnets so larger blocks aren't
fragmented around them.
</details>

**Q9.** A switch port with no cable plugged in is left in its factory-default
state. Six months later a laptop is plugged into it and gets an IP immediately
with no delay before forwarding. What single feature is most likely already
enabled, and why does that matter for interface hygiene generally?
<details><summary>Answer</summary>
PortFast — it skips STP's listening/learning states on access ports. It
matters because leaving unused ports in a default (non-access, non-PortFast)
state is itself a hygiene issue; this question is really testing whether you
recognize PortFast's effect versus assuming "it's just fast because it's a
new switch."
</details>

**Q10.** What's the compressed form of
`2001:0db8:0000:0000:0000:ff00:0042:8329`?
<details><summary>Answer</summary>
`2001:db8::ff00:42:8329` — leading zeros in each hextet are dropped, and
exactly one run of consecutive all-zero hextets is collapsed to `::`
(only one `::` is allowed per address).
</details>

**Q11.** A host's IPv6 address is `fe80::1a2b:3cff:fe4d:5e6f/64`. What type of
address is this, and can it be used to reach a host on a different subnet?
<details><summary>Answer</summary>
Link-local (FE80::/10) — auto-generated on every IPv6 interface, valid only
on the local link. It cannot route off-subnet; it's used for local
neighbor discovery and as the next-hop for on-link default routes, not
end-to-end communication.
</details>

**Q12.** Two switches are connected by a single Cat 6 cable. Auto-MDIX is
enabled on both ends. Does it matter whether you use a straight-through or
crossover cable?
<details><summary>Answer</summary>
No — auto-MDIX detects the connection type and automatically swaps
transmit/receive pairs internally as needed. This is why modern switch-to-
switch links no longer require crossover cables the way pre-auto-MDIX gear
did.
</details>

**Q13.** A small office wants to virtualize three servers (file, print, and a
line-of-business app) onto one physical box to save space and power. What's
the component that lets multiple VMs share that one physical machine's
hardware?
<details><summary>Answer</summary>
A hypervisor — it abstracts the physical CPU/RAM/storage/NICs and presents
each VM with its own virtual hardware, scheduling access to the real
hardware underneath.
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

**Q14.** A router has a static route to 0.0.0.0/0 pointing at its ISP uplink,
and a directly connected route to 192.168.1.0/24 on its LAN interface. A
packet arrives destined for 192.168.1.50. Which route is used and why?
<details><summary>Answer</summary>
The connected route — it's a more specific match (/24 vs. /0). Longest-prefix
match always wins regardless of administrative distance; the default route
is only used when nothing more specific matches.
</details>

**Q15.** You configure `ip route 10.0.0.0 255.255.255.0 192.168.1.2` on a
router, but `192.168.1.2` isn't currently reachable (the link is down).
Does the route appear in `show ip route`?
<details><summary>Answer</summary>
No — a static route only gets installed in the routing table if its next
hop (or exit interface) is currently reachable. It stays configured but
inactive until reachability is restored.
</details>

**Q16.** What administrative distance does a static route configured with
an exit interface (instead of a next-hop IP) have, and how does that compare
to one configured with a next-hop IP?
<details><summary>Answer</summary>
Both default to AD 1 — the configuration style (next-hop vs. exit-interface)
doesn't change the AD. Exit-interface static routes have a different
behavioral quirk on multi-access networks (they can cause proxy-ARP
side effects), but AD itself is unaffected.
</details>

**Q17.** Two routers, R1 and R2, are directly connected and both configured
for single-area OSPFv2 on that link. Twenty seconds after enabling OSPF,
`show ip ospf neighbor` on R1 shows R2 stuck in EXSTART. What's a likely
cause?
<details><summary>Answer</summary>
An MTU mismatch on the link. OSPF gets through the early neighbor states
fine but stalls in EXSTART/EXCHANGE when the two sides disagree on MTU
during database description packet exchange — a classic OSPF adjacency
gotcha.
</details>

**Q18.** On a point-to-point serial link running single-area OSPFv2, is a
DR/BDR election required?
<details><summary>Answer</summary>
No — DR/BDR election only happens on multi-access networks (broadcast or
NBMA), where it exists to reduce the number of adjacencies. Point-to-point
links have exactly two routers, so there's nothing to elect.
</details>

**Q19.** A router is configured with `router ospf 1` and multiple `network`
statements, but you don't want OSPF to send hellos out the interface facing
the internet edge (no OSPF neighbors should ever form there) while still
advertising that interface's subnet. What command accomplishes this?
<details><summary>Answer</summary>
`passive-interface <interface>` under the OSPF process — it suppresses
hello packets on that interface (so no adjacency can form) while the
interface's connected subnet is still advertised into OSPF.
</details>

**Q20.** Two HSRP routers share virtual IP 10.1.1.1. R1 has priority 150,
R2 has default priority (100), and both have preempt enabled. R1's uplink
fails and its HSRP priority drops via interface tracking to 90. What happens?
<details><summary>Answer</summary>
R2 becomes Active — its priority (100) now exceeds R1's tracked-down
priority (90). When R1's uplink recovers and its priority returns to 150,
preempt lets it reclaim Active automatically.
</details>

**Q21.** In HSRP, what MAC address does the virtual router use, and why does
that matter during a failover?
<details><summary>Answer</summary>
A well-known HSRP virtual MAC (0000.0C07.ACxx, where xx is the group
number) — because it's the same MAC regardless of which physical router is
Active, hosts never need to re-ARP for the gateway during a failover. Only
the active router internally changes; the client-facing MAC/IP pair stays
constant.
</details>

**Q22.** A routing table shows these entries for 172.16.0.0:
`O 172.16.0.0/16 [110/20]` and `S 172.16.1.0/24 [1/0]`. A packet is destined
for 172.16.1.5. Which route wins?
<details><summary>Answer</summary>
The static /24 — more specific prefix beats the OSPF /16 regardless of AD
(1 vs. 110). This is the same longest-prefix-match-first rule tested in
Q4/Q14, just with the roles of static and dynamic reversed.
</details>

**Q23.** What's the primary operational reason to configure a floating
static route with a higher administrative distance than your primary route,
rather than just configuring two equal-AD static routes to the same
destination?
<details><summary>Answer</summary>
Equal-AD routes would both install and load-balance simultaneously — not
what you want for a backup path. A floating static (higher AD) only gets
installed when the primary route disappears from the table, giving clean
primary/backup failover instead of both paths being active at once.
</details>

---

*Add your own missed-question entries to the relevant boss-battle file, not here — this file is a static question bank.*
