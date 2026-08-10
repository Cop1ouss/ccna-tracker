# Network Fundamentals (20%)

Synthesized from `cisco-track`'s **Networking Basics** (c1), **Networking Essentials** (c2), and — where it adds something the other two miss — **SRWE** (c3). Skeleton is the checklist in [`boss-battles/01-network-fundamentals.md`](../boss-battles/01-network-fundamentals.md).

**Legend:** ✅ well covered · ⚠️ partial (concept present, missing depth/commands) · ❌ gap (nothing in my notes — not invented here)

---

## ✅ Network components: routers, switches, APs, WLC, firewalls, servers, endpoints

**c1 (1.2 – Network Components, Types & Connections)** introduces the cast at the beginner level: end devices vs. intermediary devices (switches, routers, APs), and client/server vs. peer-to-peer roles. **c2** doesn't re-teach this directly — it assumes it and moves straight to protocols — so c1 is the sole source here. Firewalls and WLCs specifically only show up later as *configuration* topics (c1 1.7 "firewall concepts" at a home-router level; the WLC gets real treatment in Network Access domain via c3 3.13), not as a "components" overview — the two courses split "what a device is" (c1) from "how you configure it" (c2/c3) rather than repeating each other.

## ✅ Network topology architectures: two-tier, three-tier, on-prem vs. cloud, SOHO, WAN

**c2 2.12 (Network Design, Cloud & Virtualization)** covers the **3-tier hierarchical model** (access/distribution/core) and redundancy design, plus cloud service models (IaaS/PaaS/SaaS) and cloud-managed networking (Meraki, Catalyst Center) — the v1.1-blueprint angle. **c1** supplies the SOHO end of the spectrum implicitly through its entire home-network build sequence (1.4–1.8), though it never uses the acronym "SOHO." WAN is touched at the conceptual level in c1 1.5 (ISP connection types) and c2 1.2's LAN/WAN/internet/intranet distinction.

⚠️ **Gap within this item:** **two-tier** collapsed-core designs and **spine-leaf** are not named anywhere in either course — c2 2.12 goes straight from "hierarchical design" to redundancy without walking through the two-tier vs. three-tier tradeoff, and spine-leaf (a data-center-oriented topology) isn't mentioned at all. If this comes up on the exam, that's outside content, not review.

## ⚠️ Physical interfaces & cabling: copper (UTP/STP) vs. fiber, SFP/SFP+ transceivers

**c2 2.2 (Network Media)** is the real source: UTP categories (through Cat 6A/8), straight-through vs. crossover in the "auto-MDIX era," single- vs. multi-mode fiber, connectors, and media tradeoffs (attenuation, EMI, distance). **c1 1.2** briefly names copper/fiber/wireless as media options at a much shallower level.

❌ **Gap:** neither course's notes mention **SFP/SFP+ transceivers** by name. Fiber connector types are covered generically ("Connectors" topic) but the specific SFP/SFP+ modular-transceiver concept the blueprint calls out isn't there.

## ⚠️ Interface/port config: speed, duplex, auto-MDIX

Conceptually present — c2 2.2 names "auto-MDIX era" as the reason straight-through/crossover no longer matters much, and c3 3.2 (Switching Concepts) lists "Duplex and speed" as a topic alongside store-and-forward vs. cut-through switching. Neither course's lab guides contain an actual `speed`/`duplex` interface-config command (e.g. `interface gi0/1` → `speed 100` / `duplex full`) — every CLI lab I have (NE-CAP-a, SRWE-L1a) configures `hostname`, SSH, and `ip address`, but never touches speed/duplex explicitly. Treat the concept as known, the CLI syntax as untested.

## ✅ Switching concepts: MAC learning/aging, frame switching, frame flooding, MAC address table

Best-covered item in the domain. **c2 2.3 (The Access Layer & Ethernet Switching)** is the primary source — Ethernet II frame fields, MAC structure (OUI + device), switch learning/forwarding, MAC aging, collision vs. broadcast domains — reinforced hands-on by lab **NE-L3** ("Watch a Switch Learn," Simulation-mode observation of flood → learn → forward). **c3 3.2** revisits the same ground at CCNA depth with store-and-forward vs. cut-through forwarding and buffering added. Verification command from my own notes:

```
show mac address-table
```

## ✅ IPv4 addressing and subnetting: CIDR, VLSM, subnet math

Strongest module in either course. **c2 2.5 (IPv4 Addressing & Network Segmentation)** — explicitly flagged in my own notes as *"the highest-value skill in networking... subnetting is on every CCNA exam"* — covers CIDR, the 2ⁿ/2ⁿ-2 subnet math, fixed-length subnetting, VLSM, and /30–/31 point-to-point links, backed by two labs (NE-L5a speed drill, NE-L5b VLSM department plan). **c1 1.6** lays the binary-conversion groundwork (binary↔decimal, network/host portions, subnet mask role) that c2 assumes. The `scripts/subnet_drill.py` tool in this repo drills exactly this.

## ✅ IPv6 addressing: global unicast, link-local, unique-local, multicast, anycast, EUI-64

**c2 2.6 (IPv6 Addressing Formats & Rules)** is the source: 128-bit format + compression, link-local (`FE80::/10`), EUI-64 interface-ID generation, and SLAAC/RA. Its stated objectives explicitly name GUA, LLA, ULA, and multicast. Lab **NE-L6** has real config:

```
ipv6 unicast-routing
interface g0/0
 ipv6 address 2001:db8:a::1/64
interface g0/1
 ipv6 address 2001:db8:b::1/64
```
```
show ipv6 interface brief
show ipv6 route
```

❌ **Gap:** **anycast** addressing is not mentioned anywhere in either course's notes — the objective list stops at multicast. Everything else in this bullet is solid; anycast specifically needs outside review.

## ✅ Wireless principles: nonoverlapping channels, SSID, RF, encryption basics

Split cleanly across three courses with no real overlap to reconcile: **c1 1.3** introduces Wi-Fi fundamentals (802.11 a/b/g/n/ac/ax/be, 2.4/5/6 GHz bands, SSID/association) and cellular/Bluetooth/NFC context; **c1 1.7** covers WPA3-first / WPA2-legacy encryption at the home-router level; **c3 3.12 (WLAN Concepts)** goes deeper on nonoverlapping channel planning and autonomous vs. lightweight/controller-based AP architectures, explicitly calling out WPA3 as the 2026 default over WPA2. No disagreement between courses — c3 is just c1's material at CCNA depth.

## ⚠️ Virtualization fundamentals: VMs vs. containers, virtual switching concepts

**c2 2.12** covers hypervisors and VMs as part of its cloud/virtualization topic list, alongside SDN at a high level.

❌ **Gap:** **containers** are not covered as a network-fundamentals concept anywhere — the only "container" hit in the whole repo's source is Active Directory's OU-vs-container distinction (c4 4.5), which is a completely different meaning of the word and not a substitute. **Virtual switching** (vSwitch/vNIC concepts) also isn't named explicitly; c2 2.12 stays at the "what is a hypervisor" level.

## ✅ Switch verification commands: `show mac address-table`, `show interfaces`

Covered via **NE-L3**'s `show mac address-table` (see above). `show interfaces` itself isn't run in any lab guide I have, though `show ip route` / `show ipv6 interface brief` (NE-L6, NE-L9) establish the same `show`-command verification habit. Treat `show interfaces` output interpretation specifically as light on hands-on practice.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| Network components | ✅ |
| Topology architectures | ✅ (two-tier/spine-leaf ❌) |
| Physical interfaces & cabling | ⚠️ (SFP/SFP+ ❌) |
| Interface/port config (speed/duplex/auto-MDIX) | ⚠️ (no CLI example) |
| Switching concepts | ✅ |
| IPv4 addressing & subnetting | ✅ |
| IPv6 addressing | ✅ (anycast ❌) |
| Wireless principles | ✅ |
| Virtualization fundamentals | ⚠️ (containers ❌) |
| Switch verification commands | ✅ (`show interfaces` untested) |

**Real gaps to close before test day:** two-tier/spine-leaf topology naming, SFP/SFP+ transceivers, IPv6 anycast, VM-vs-container distinction, `speed`/`duplex` CLI syntax, `show interfaces` hands-on.
