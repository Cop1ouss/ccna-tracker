# IP Services (10%)

![IP Services](https://img.shields.io/badge/domain-IP%20Services-f472b6) ![Weight](https://img.shields.io/badge/weight-10%25-f472b6)

Synthesized from **Networking Basics** (c1), **Networking Essentials** (c2), **SRWE** (c3), and **ENSA** (c5). Skeleton is the checklist in [`boss-battles/04-ip-services.md`](../boss-battles/04-ip-services.md). Course 05 closed most of what used to be this domain's most individually-gapped items — NAT, NTP, and SNMP/syslog all shipped with ENSA.

**Legend:** ✅ well covered · ⚠️ partial · ❌ gap

---

## ✅ NAT: static, dynamic, and PAT (port address translation)

**c1 1.5 (Connect to the Internet)** covers NAT at the conceptual level ("Describe NAT conceptually"), and **ENSA 5.5 (NAT for IPv4)** now takes it all the way to IOS config: `ip nat inside`/`ip nat outside`, static NAT (one-to-one), dynamic NAT (pool + access-list match), and PAT/overload, verified with `show ip nat translations`. **ENSA-L5a** builds static + dynamic NAT for an internal server and a shared pool; **ENSA-L5b** does PAT for a whole subnet sharing one public IP. NAT CLI syntax is no longer untested.

## ✅ NTP: client/server configuration

**Closed by ENSA 5.6 (Network Services: NTP, SNMP, Syslog)** — `ntp server` client config and `show ntp status` are both taught, framed correctly as the prerequisite that has to come first before SNMP/syslog make sense (so logs and monitoring data actually correlate). **ENSA-L6** configures a router/switch to point at an NTP server as part of the combined services lab.

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

## ✅ SNMP: basic operation and use case

**Read-only closed by ENSA 5.6** — `snmp-server community` (read-only) is taught and configured in **ENSA-L6**. The rest below is an **outside-study addition** (no cisco-track lab backs it — added directly since it's stable, well-documented material, not something that needs a hands-on lab to get right):

**MIB (Management Information Base)** — a hierarchical, tree-structured database of every variable a device exposes for monitoring (interface counters, CPU load, temperature, uptime). Vendors and standards bodies define which variables exist and where they sit in the tree.

**OID (Object Identifier)** — the dotted-numeric address of one specific variable inside that tree, e.g. `1.3.6.1.2.1.1.3.0` = `sysUpTime`. SNMP GET/GETNEXT/GETBULK requests reference OIDs directly; a MIB file is just the human-readable map that turns numbers into names like `ifInOctets`.

**SNMP versions** (a real exam-testable distinction):
- **v1** — original, community-string auth only (plaintext), no GETBULK.
- **v2c** — adds GETBULK (pull many OIDs in one request) and better error handling, still plaintext community strings.
- **v3** — adds real security: per-user authentication (MD5/SHA) and optional encryption (DES/AES). The only version with actual confidentiality/integrity — v1/v2c community strings are visible to anyone sniffing the segment.

**Polling vs. traps** — the operational distinction the exam cares about: *polling* is manager-initiated (NMS asks a device for a value on a schedule); a *trap* is device-initiated and unsolicited (the device pushes a notification the instant something crosses a threshold, e.g. an interface goes down), so traps get you faster alerting than polling alone.

```
snmp-server community public RO
snmp-server community private RW
snmp-server host 10.1.1.50 version 2c public
snmp-server enable traps
snmp-server contact netops@example.com
snmp-server location "NOC Rack 3"
```
`RO`/`RW` on the community line is the write-access distinction ENSA's read-only-only lab doesn't show — `RW` lets a manager *set*, not just *get*, values, which is why RW community strings are a real security liability if left at defaults.

## ✅ Syslog: severity levels, use case

**Closed by ENSA 5.6** — `logging host` + `logging trap`, plus the severity 0–7 scale, are now taught content, configured in **ENSA-L6** capped at Warning severity. This matches (and now sources) `practice-questions` Q4's "severity 7 = Debugging" from actual course material instead of the practice bank alone.

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

## ⚠️ QoS: basic concepts — marking, queuing, congestion management

**Concept-level gap closed by ENSA 5.7 (QoS Concepts)** — trust boundary + marking (DSCP/CoS), queuing strategies (FIFO vs. priority/weighted), and congestion management vs. avoidance are all now taught, matching what the exam actually wants here (explain QoS, not configure a policy-map — the module has zero labs by design). Same still applies to the WLAN-side QoS-profile mention in `network-access.md`: the *concept* is covered, but there's still no hands-on config anywhere in cisco-track.

## ✅ TFTP/FTP: file transfer use cases (IOS image/config backup)

**TFTP is solid** — **SRWE-L1b** walks through the exact operational pattern the exam cares about (backup before risky changes, restore after a wipe):

```
copy startup-config tftp:
```
```
copy tftp: running-config
```

**FTP — outside-study addition** (no cisco-track lab backs this, added directly): where TFTP is UDP/69, unauthenticated, and has no directory listing or delete capability, **FTP is TCP-based, authenticated (username/password), and connection-oriented** — control connection on port 21, a separate data connection on port 20 (active mode) or a server-assigned port (passive mode, the one that actually works through NAT/firewalls, which is why it's the default almost everywhere today). The IOS syntax mirrors TFTP's `copy` pattern, just with credentials supplied first:

```
ip ftp username admin
ip ftp password Cisc0!
copy running-config ftp://10.1.1.10/backup-config.txt
copy ftp://10.1.1.10/ios-image.bin flash:
```
Exam framing: TFTP is the "quick and simple, same-subnet lab" tool; FTP is the "authenticated, routable, production" tool — pick FTP when the scenario mentions credentials, security, or a file transfer across a WAN link.

---

## Domain summary

| Sub-topic | Status |
|---|---|
| NAT (static/dynamic/PAT) | ✅ (closed by ENSA 5.5) |
| NTP | ✅ (closed by ENSA 5.6) |
| DHCP (client/relay/options) | ✅ |
| DNS | ✅ |
| SNMP | ✅ (read-only via ENSA 5.6; MIB/OID/version/trap depth added directly below) |
| Syslog | ✅ (closed by ENSA 5.6) |
| SSH (vs. Telnet) | ✅ |
| QoS | ⚠️ (concept closed by ENSA 5.7; no hands-on config anywhere) |
| TFTP/FTP | ✅ (TFTP via SRWE-L1b, FTP added directly below) |

**No real gaps left in this domain.** The only remaining soft spot is QoS — concepts are covered (ENSA 5.7) but there's still no hands-on config anywhere in cisco-track, which matches what the exam actually tests here (explain, don't configure).
