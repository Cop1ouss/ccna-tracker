# Network Access (20%)

![Network Access](https://img.shields.io/badge/domain-Network%20Access-34d399) ![Weight](https://img.shields.io/badge/weight-20%25-34d399)

Synthesized almost entirely from **SRWE** (c3) — this is the domain SRWE was built for. Skeleton is the checklist in [`boss-battles/02-network-access.md`](../boss-battles/02-network-access.md). Port security / DHCP snooping / DAI live in `security-fundamentals.md` instead, since that's where the boss-battle checklist puts Layer 2 security. Checked **ENSA** (c5) against this domain too — the only overlap is general QoS concepts (see the WLAN QoS-profile item below); CDP/LLDP, EtherChannel, STP protection features, and WLC deployment models remain untouched by Course 05.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ⚠️ VLANs: access vs. trunk ports, native VLAN, voice VLAN, default VLAN

**c3 3.3 (VLANs)** is the source, backed by two labs. Access vs. trunk and native VLAN are hands-on with real config:

```
vlan 10
 name Staff
vlan 20
 name Students
vlan 30
 name Servers
```
```
interface fa0/1
 switchport mode access
 switchport access vlan 10
```
```
interface g0/1
 switchport mode trunk
 switchport nonegotiate
 switchport trunk native vlan 99
```
```
show vlan brief
show interfaces trunk
```

**SRWE-L3b** deliberately plants a native-VLAN mismatch, a missing trunk mode, and a too-restrictive allowed-VLAN list to troubleshoot — good exam-style diagnostic practice.

⚠️ **Voice VLAN** is named as a topic in 3.3's outline but never gets its own config step in either lab — no `switchport voice vlan <id>` example exists in my notes, so the concept is known but the syntax is untested. **Default VLAN** (VLAN 1's special status) isn't explained as its own concept either — it comes up implicitly through the native-VLAN-99 examples (which exist specifically to move off VLAN 1) but nothing states outright *why* VLAN 1 is risky to leave as native/default.

## ✅ Interswitch connectivity: 802.1Q trunking, DTP behavior

Same SRWE-L3a/b labs cover this well. The `switchport nonegotiate` command above **is** the DTP story in practice — my own notes' framing (3.3 topics: *"DTP (disable in prod)"*) matches current best practice: DTP auto-negotiation is a VLAN-hopping attack surface, so production trunks should be hard-set on both ends rather than negotiated.

## ❌ Layer 2 discovery protocols: CDP and LLDP

**Real gap.** The only appearance of "CDP" anywhere in my notes is a passing mention in SRWE-L3b's troubleshooting step — *"read the CDP/native-VLAN mismatch warnings"* — referring to a console log message IOS emits, not actual CDP configuration or verification. There's no `show cdp neighbors` (or `show cdp neighbors detail`) example, and **LLDP doesn't appear anywhere in the repo at all** — not as a topic, not as a command, not even a mention. Since CDP is Cisco-proprietary and LLDP is the vendor-neutral IEEE standard, and the exam blueprint explicitly wants both, this needs outside study.

## ⚠️ EtherChannel: LACP, static vs. dynamic bundling, load balancing basics

**c3 3.6** plus **SRWE-L6** give solid LACP hands-on:

```
interface range g0/1 - 2
 channel-group 1 mode active
 no shutdown
```
```
interface port-channel 1
 switchport mode trunk
```
```
show etherchannel summary
```

This confirms LACP *active* mode and reading `show etherchannel summary` for bundle status (P = bundled ports, protocol = LACP). The objectives list also says *"Compare LACP and PAgP modes,"* but only the `active` LACP mode is actually configured in the lab — there's no example of `passive` mode, no PAgP (`desirable`/`auto`) commands, and no worked example of a channel-group **mode mismatch** (e.g. active↔active required, active↔passive works, passive↔passive fails) even though "diagnose channel mismatches" is a stated objective. Load balancing is named as a topic but never configured or explained (no `port-channel load-balance` example).

## ✅ Spanning Tree Protocol: root bridge election, port roles/states, PortFast, BPDU guard

Well covered by **c3 3.5** and **SRWE-L5**, and explicitly framed around the 2026-current default:

```
spanning-tree mode rapid-pvst
show spanning-tree
spanning-tree vlan 1 root primary
show spanning-tree vlan 1
```
```
interface range fa0/1 - 24
 spanning-tree portfast
 spanning-tree bpduguard enable
```

My notes are correctly emphatic that **Rapid PVST+** is the modern Cisco default (sub-second convergence) versus legacy 802.1D STP's 30+ second reconvergence — v1.1 blueprint alignment confirmed. Root bridge election, port roles/states, PortFast, and BPDU Guard are all backed by a real command, not just a topic bullet.

## ⚠️ STP protection features: root guard, loop guard, BPDU filter, BPDU guard

BPDU Guard is fully covered (see command block above). **Root Guard** is *named* in the 3.5 topic list (*"PortFast, BPDU/Root Guard"*) but never actually configured in the lab — no `spanning-tree guard root` example exists.

❌ **Loop Guard and BPDU Filter are full gaps** — neither is mentioned anywhere in the repo, not even as a topic name. Of the four STP protection features on the blueprint, only one (BPDU Guard) has both concept and command; two (Root Guard) has concept only; two (Loop Guard, BPDU Filter) have nothing.

## ⚠️ Wireless architectures: autonomous vs. lightweight AP, WLC deployment models

**c3 3.12 (WLAN Concepts)** explicitly states the autonomous-vs-lightweight distinction as a learning objective, alongside 802.11 standards/bands (including Wi-Fi 6E/7) and non-overlapping channel planning — reinforced by lab **SRWE-L12**'s site-planning exercise (channel assignment, 2.4/5/6 GHz justification).

❌ **Gap:** the blueprint specifically wants the three **WLC deployment models** — centralized, cloud-based, and embedded/converged. My notes only ever say "APs + WLC" as a topic, without naming or distinguishing the three deployment models Cisco tests on.

## ⚠️ WLAN configuration (GUI-based): SSID creation, WPA2/WPA3, QoS profile basics

**c3 3.13 + labs SRWE-L13a/b** match the "GUI-based" framing in the checklist exactly — these are WLC GUI walkthroughs (register an AP, create a WPA3-Personal WLAN, map a second WLAN to a VLAN with WPA3-Enterprise/802.1X), not CLI. SSID creation and the WPA2→WPA3 shift are solid, with the correct 2026 framing (WPA3 default, WPA2 legacy fallback, WPA3-Enterprise using 802.1X rather than PSK).

⚠️ **Gap:** **QoS profile basics** — nothing in either WLAN module, and ENSA doesn't cover WLAN-specific QoS profiles either. The general concept is no longer a full gap, though — **ENSA 5.7 (QoS Concepts)** now covers marking (DSCP/CoS), queuing, and congestion management at the concept level (see `ip-services.md`), so the vocabulary is real content now, but a WLAN QoS profile specifically still has no source material.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| VLANs (access/trunk/native/voice/default) | ⚠️ (voice VLAN command, default-VLAN rationale missing) |
| Interswitch connectivity (802.1Q, DTP) | ✅ |
| L2 discovery protocols (CDP, LLDP) | ❌ |
| EtherChannel (LACP/PAgP, load balancing) | ⚠️ (only LACP active mode; no PAgP, no load-balancing config) |
| STP core (root election, port roles, PortFast, BPDU guard) | ✅ |
| STP protection (root/loop guard, BPDU filter/guard) | ⚠️ (only BPDU guard has a command; root guard concept-only; loop guard + BPDU filter ❌) |
| Wireless architectures (autonomous/lightweight, WLC models) | ⚠️ (WLC deployment models not named) |
| WLAN config GUI (SSID, WPA2/3, QoS) | ⚠️ (general QoS ✅ via ENSA 5.7, WLAN-specific QoS profile ❌) |

**Real gaps to close before test day:** CDP/LLDP verification commands, LACP passive mode + PAgP + channel mismatch scenarios, EtherChannel load balancing, root guard/loop guard/BPDU filter commands, the three WLC deployment models, and WLAN-specific QoS profile configuration (general QoS concepts are now covered via ENSA, this domain's gap is just the WLAN-profile application of it).
