# OSPF Note-Taking Template

Companion to the OSPF gap flagged in [`../ip-connectivity.md`](../ip-connectivity.md) — cisco-track has zero taught OSPF content, so this is where that gets built from scratch while watching Jeremy's IT Lab's OSPF series. One section per sub-objective from [`../../boss-battles/03-ip-connectivity.md`](../../boss-battles/03-ip-connectivity.md)'s "Single-area OSPFv2" and "OSPF verification" checklist lines.

Fill in every blank. Once a section is solid, check the matching box in the boss-battle checklist and log any missed practice question against it with `scripts/log_session.py`.

---

## Neighbor Adjacency

**What are the 8 OSPF neighbor states, in order, from first contact to fully synchronized?**

> Down → ______ → ______ → 2-Way → ______ → ______ → ______ → Full

**What has to match between two routers' Hello packets before they'll even become neighbors (not yet adjacent — just neighbors)?**

>

**Two directly connected routers are stuck in `EXSTART`/`EXCHANGE` and never reach `FULL`. What's the single most common cause, and what command would you check first?**

>

**On a point-to-point link (no DR/BDR), do two OSPF routers still need to reach `FULL`, or is `2-Way` good enough there?**

>

---

## DR/BDR Election

**On what type of network does a DR/BDR election actually happen — and on what type does it never happen at all?**

>

**What OSPF priority value takes a router completely out of DR/BDR eligibility, no matter how long it's been on the segment?**

>

**When two routers have equal OSPF priority, what tie-breaks the election — and specifically, does *highest* or *lowest* value win?**

>

**A new router with a higher priority than the current DR joins the segment after the election has already happened. Does it become the new DR? Why or why not?**

>

**Command to set OSPF priority on an interface:**

```
interface ____________
 ip ospf priority ____
```

---

## Router ID

**If you never manually configure a router ID, how does the router pick one? Write the full decision order (loopbacks vs. physical interfaces, highest vs. lowest).**

>

**If you bring up a new, higher-IP loopback interface *after* the OSPF process is already running, does the router ID change automatically? What would force it to change?**

>

**Why do experienced engineers manually set a router ID (or use a dedicated loopback for it) instead of letting OSPF pick automatically?**

>

**Two ways to manually set the router ID — write both command forms:**

```
router ospf 1
 router-id ____________
```
```
interface loopback ____
 ip address ____________ ____________
```

---

## Passive Interfaces

**What does `passive-interface` actually suppress on an interface — and what does it *not* stop from happening to that interface's connected subnet?**

>

**Why would you make a LAN-facing access-layer interface passive instead of just leaving it out of the OSPF `network` statement entirely?**

>

**Command to make every OSPF interface passive by default, then re-enable OSPF hellos on just one uplink interface:**

```
router ospf 1
 passive-interface ____________
 no passive-interface ____________
```

---

## Verification Commands

Fill in what you'd actually expect to see in the output — not just the command syntax.

**`show ip ospf neighbor`** — what does each column tell you (Neighbor ID, Pri, State, Dead Time, Address, Interface)?

>

**`show ip route ospf`** — what letter code marks an OSPF-learned route in the routing table?

>

**`show ip protocols`** — name three specific things this command's OSPF section shows you:

> 1.
> 2.
> 3.
