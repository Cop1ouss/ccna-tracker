# Mock Exam 1 — Answer Key

Score yourself, then log every miss in the matching `boss-battles/*.md`
missed-question table with a tag (repeat/regression/new) — that log is what
`scripts/coverage.py` and your own review will lean on later, not this file.

**Passing bar:** Cisco's unofficial cut is ~82–85%. That's roughly 55/65.

---

## Network Fundamentals

1. **B** — a switch forwards based on MAC address (Layer 2); a router forwards based on IP (Layer 3).
2. **C** — access connects end devices, distribution enforces policy/aggregates, core is pure high-speed transport.
3. **A** — 10GBASE-T over Cat 6A is rated to 55m; 100m applies to Cat 6A at 1 Gbps or Cat 5e/6 generally.
4. **B** — one side hard-set breaks auto-negotiation on the other side, producing a duplex mismatch (works but slow, with errors).
5. **C** — /29 gives 6 usable hosts, covering 5 now with 1 spare; /30 (2 usable) is too small, /28 (14 usable) wastes more than needed for "room to grow to 8."
6. **C** — global unicast addresses are globally routable, the IPv6 analog of public IPv4.
7. **B** — EUI-64 splits the 48-bit MAC, inserts FFFE in the middle, and flips the 7th bit to form a 64-bit interface ID.
8. **B** — unknown-unicast frames are flooded out every port except the source port until the switch learns where that MAC lives.
9. **C** — 6 GHz (Wi-Fi 6E/7) has the most non-overlapping channels and no legacy-device congestion, since only newer clients use it.
10. **B** — the hypervisor abstracts physical hardware so multiple VMs can run isolated on the same box.
11. **C** — Layer 3 (Network layer) is where IP-based forwarding decisions happen.
12. **A** — /25 on 192.168.5.0 splits into .0–.127 and .128–.255; a host at .10 is in the first block, broadcast .127.
13. **B** — SFP/SFP+ is a modular transceiver slot letting one physical port take different fiber or copper media types.

## Network Access

14. **B** — VLAN 1 is the default native VLAN unless explicitly changed.
15. **B** — `dynamic desirable` actively sends DTP frames asking the other side to trunk; `auto` only responds, never initiates.
16. **B** — CDP is Cisco-proprietary, Cisco devices only.
17. **B** — LLDP (IEEE 802.1AB) is the vendor-neutral discovery protocol.
18. **B** — `mode active` is LACP's actively-negotiating mode; PAgP uses `desirable`/`auto` instead.
19. **B** — the root bridge is designated on every one of its own ports by definition — it doesn't have a "root port" (it has none, since it IS the root).
20. **C** — Listening comes after Blocking and before Learning; it listens for BPDUs but doesn't forward or learn yet.
21. **C** — BPDU Guard err-disables the port on receipt of any BPDU, full stop.
22. **B** — Root Guard is more surgical: it blocks that one port from becoming root port (keeping it in a root-inconsistent state) rather than disabling the whole port.
23. **B** — a lightweight AP has no standalone config; it joins/registers to a WLC and receives config from there.
24. **B** — cloud-based WLC deployment runs the controller function off-site in the cloud, vs. centralized (on-prem hardware controller) or embedded (controller function built into a switch).
25. **B** — WPA3-Personal uses a pre-shared key (passphrase); WPA3-Enterprise is the 802.1X/certificate option.
26. **B** — overlapping 2.4 GHz channels cause co-channel/adjacent-channel interference that directly degrades throughput for nearby APs.

## IP Connectivity

27. **B** — longest-prefix match is always evaluated before administrative distance; the /24 is more specific than the /16 regardless of which protocol sourced it.
28. **A** — directly connected routes have AD 0, the most trusted of all.
29. **B** — a static route only installs in the table if its next hop is currently reachable.
30. **B** — a floating static (higher AD than the primary) only gets installed once the lower-AD primary route is withdrawn from the table.
31. **B** — on broadcast multi-access segments, only DR and BDR form FULL with everyone; DROTHER-to-DROTHER stays at 2-WAY by design.
32. **B** — router ID defaults to the highest active loopback IP, or if none exists, the highest active physical interface IP, at process startup.
33. **B** — MTU mismatch is the classic cause of routers stalling in EXSTART/EXCHANGE — hellos succeed but database description packets don't.
34. **B** — `passive-interface` stops hellos (no adjacency forms) while the interface's subnet is still advertised.
35. **B** — `show ip ospf neighbor` is specifically the neighbor-state/DR-BDR-role table.
36. **B** — without preempt, a returning higher-priority router does not reclaim Active; the current Active keeps the role.
37. **B** — HSRP's virtual MAC is 0000.0C07.ACxx, constant regardless of which physical router is currently Active.
38. **B** — VRRP is the IETF open-standard FHRP, functionally similar to HSRP (which is Cisco-proprietary).
39. **B** — no route matches 8.8.8.8 more specifically than 0.0.0.0/0, so the default route is used.
40. **B** — IPv6 static/default routes use the `ipv6 route` command family, separate from `ip route` for IPv4.
41. **B** — the /25 is the longer, more specific match and wins regardless of configuration order or AD.
42. **B** — equal-AD routes to the same destination install and load-balance together, which breaks a "primary vs. backup only" intent — that's what floating statics (different AD) are for instead.

## IP Services

43. **C** — many-to-one translation distinguished by port is PAT / NAT overload, the default on most home and small-office routers.
44. **B** — `ip helper-address` relays broadcast UDP services (DHCP chief among them) to a unicast server across a router boundary.
45. **C** — lower severity numbers are more urgent; 0 (Emergency) is worst, 7 (Debugging) is least urgent, so 2 (Critical) is near the top.
46. **B** — SSH v2 needs an RSA keypair to set up its encrypted channel; without `crypto key generate rsa`, SSH can't actually start.
47. **B** — TFTP is UDP/simple/unauthenticated; FTP is TCP/connection-oriented and supports authentication.
48. **B** — NTP (Network Time Protocol) exists specifically to synchronize clocks across many devices.

## Security Fundamentals

49. **B** — a vulnerability is the weakness itself; an exploit is the specific technique/code that takes advantage of it.
50. **B** — authorization governs what an authenticated identity is permitted to do.
51. **B** — TACACS+ encrypts the whole packet and splits AAA into distinct exchanges; RADIUS only encrypts the password and bundles authentication+authorization together.
52. **B** — standard ACLs (1–99, 1300–1999) match source IP address only — nothing else.
53. **B** — `0.0.0.255` is the wildcard that matches any host within a /24 (inverse of the 255.255.255.0 subnet mask).
54. **B** — since a standard ACL can't distinguish destinations, placing it near the source would block that host from reaching everything, not just one destination — so it belongs near the destination instead.
55. **B** — `restrict` mode drops the violating traffic and logs it, but leaves the port up (unlike `shutdown`, which err-disables it).
56. **B** — DHCP snooping's core job is blocking rogue/unauthorized DHCP servers from answering on untrusted ports.
57. **A** — site-to-site is a permanent gateway-to-gateway tunnel between networks; remote-access is a per-user, on-demand client tunnel.
58. **B** — the defining difference is authentication method: WPA3-Enterprise uses 802.1X/EAP against a backend (e.g. RADIUS) server instead of a shared passphrase.

## Automation & Programmability

59. **B** — `GET` retrieves a resource without changing it; that's the whole point of the verb.
60. **C** — 401 Unauthorized means authentication is missing or failed (compare: 404 Not Found, 500 Server Error, 200 OK).
61. **B** — Ansible is agentless, reaching managed nodes over SSH (or APIs for network devices) rather than requiring installed software.
62. **B** — Terraform is infrastructure-as-code, primarily for declaring/provisioning infrastructure state, distinct from Ansible's configuration-management focus.
63. **B** — `20` is a bare number in JSON, not wrapped in quotes, so it's the Number type (contrast with `"status": "active"`, a String).
64. **B** — SDN/controller-based management centralizes config push through one controller instead of touching every device's CLI individually.
65. **B** — forecasting capacity exhaustion from historical trends is predictive; generating text/config/summaries from a prompt (A, C, D) is generative.
