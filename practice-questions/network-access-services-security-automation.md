# Practice Questions — Network Access, IP Services, Security, Automation

---

## Network Access

**Q1.** A trunk port between two switches carries VLANs 10, 20, and the native
VLAN 1. A host on VLAN 1 on Switch A can't reach a host on VLAN 1 on Switch B,
but VLANs 10 and 20 work fine. What's a likely misconfiguration?
<details><summary>Answer</summary>
Native VLAN mismatch — if one switch has native VLAN 1 and the other has native
VLAN set to something else (or untagged frames are being dropped/misrouted),
only the native VLAN traffic breaks while tagged VLANs stay fine.
</details>

**Q2.** A switch port connected to a single PC keeps flapping through STP's
listening/learning states for 30 seconds every time the PC reboots, causing
a brief loss of connectivity. What single feature fixes this?
<details><summary>Answer</summary>
PortFast — it skips listening/learning on access ports that will never connect
to another switch, going straight to forwarding.
</details>

**Q9.** A trunk port has `switchport trunk allowed vlan 10,20,30` configured.
An access port on the same switch is assigned to VLAN 40. Can VLAN 40 traffic
cross the trunk?
<details><summary>Answer</summary>
No — the allowed-VLAN list restricts which VLANs are permitted across the
trunk regardless of what VLANs exist elsewhere on the switch. VLAN 40 would
need to be added to the allowed list first.
</details>

**Q10.** What does `switchport nonegotiate` do, and why is it recommended
on production trunk links?
<details><summary>Answer</summary>
It disables DTP (Dynamic Trunking Protocol) on that port, so the port won't
negotiate trunking automatically. It's recommended because DTP negotiation
is a known VLAN-hopping attack vector — an attacker's PC pretending to
speak DTP can trick a misconfigured access port into becoming a trunk.
</details>

**Q11.** Two switches are cabled together with two separate links, both
configured with `channel-group 1 mode active`. `show etherchannel summary`
shows the Port-Channel interface with both ports listed but flagged `(I)`
instead of `(P)`. What does that indicate?
<details><summary>Answer</summary>
`(I)` means "individual" — the ports are up but NOT bundled into the
EtherChannel, usually because of a configuration mismatch between the two
switches (mismatched mode, VLAN, trunk encapsulation, or speed/duplex on
one side). Only `(P)` ports are actually part of the active bundle.
</details>

**Q12.** In Rapid PVST+, what's the fastest way for a switch to become the
root bridge for VLAN 1 without changing every other switch's priority by
hand?
<details><summary>Answer</summary>
`spanning-tree vlan 1 root primary` — it automatically sets that switch's
bridge priority low enough (in a fixed increment below the current root)
to win the election, without you calculating and setting priorities on
every other switch.
</details>

**Q13.** A switch port configured with `spanning-tree bpduguard enable`
receives a BPDU. What happens to the port?
<details><summary>Answer</summary>
It goes err-disabled immediately. BPDU Guard assumes a port that should
never see a BPDU (an access port facing an end host) has instead been
connected to another switch or a rogue device, and shuts it down rather
than participating in STP.
</details>

**Q14.** An autonomous AP and a lightweight AP both need their SSID and
security settings configured. Where does each get that configuration from?
<details><summary>Answer</summary>
An autonomous AP is configured individually, device by device (it has its
own full AP OS and management). A lightweight AP has no standalone
configuration — it registers to a Wireless LAN Controller (WLC), which
pushes SSID, security, and channel settings to every AP it manages
centrally.
</details>

**Q15.** A WLC has a WLAN configured for WPA3-Enterprise. What authenticates
the client instead of a shared passphrase?
<details><summary>Answer</summary>
802.1X, typically backed by a RADIUS server — the client authenticates with
individual credentials (or a certificate) through the EAP exchange, rather
than everyone sharing one PSK like WPA3-Personal.
</details>

**Q16.** Why does forcing all access ports on a switch to `PortFast` +
`BPDU Guard` (rather than leaving them at STP defaults) matter operationally,
beyond just "faster to forwarding"?
<details><summary>Answer</summary>
PortFast alone just skips the 30-second listening/learning delay — it
doesn't protect against a loop if someone plugs a switch into that port.
BPDU Guard is what makes PortFast safe on access ports: if a BPDU ever
appears (meaning something switch-like got connected where only an end
host was expected), the port shuts down instead of silently forming a loop.
</details>

---

## IP Services

**Q3.** An internal host with private IP 192.168.1.10 browses the internet.
The firewall shows outbound traffic as coming from a single public IP,
203.0.113.5, regardless of which internal host initiated it. What NAT type is this?
<details><summary>Answer</summary>
PAT (Port Address Translation / NAT overload) — many-to-one translation using
port numbers to distinguish sessions, the default for most home/office setups.
</details>

**Q4.** A syslog server is filling up with messages at severity level 7. Should
you be worried?
<details><summary>Answer</summary>
No — severity 7 is "Debugging," the least urgent level. Severity 0 (Emergency)
is the one to worry about; lower number = higher severity.
</details>

**Q17.** A router is configured with `ip dhcp pool LAN` including a
`network`/`default-router`/`dns-server` set, and `ip dhcp excluded-address
10.0.0.1 10.0.0.10`. What's the purpose of the excluded-address line?
<details><summary>Answer</summary>
It keeps the DHCP pool from handing out addresses in that range — typically
because they're already statically assigned (gateway, servers, printers).
Without it, the DHCP scope could offer an address that's already in use
elsewhere.
</details>

**Q18.** A DHCP server lives on Router-A's subnet, but clients needing
addresses are on Router-B's subnet, one hop away. Router-B has no DHCP pool
configured. What single command on Router-B's client-facing interface makes
DHCP work for those clients?
<details><summary>Answer</summary>
`ip helper-address <Router-A's-interface-IP>` — it relays DHCP (and several
other UDP broadcast services) from Router-B's LAN toward the unicast address
of the actual DHCP server, since DHCP discovery is normally a broadcast
that wouldn't otherwise cross a router boundary.
</details>

**Q19.** What's the functional difference between TFTP and FTP for backing
up a router's configuration?
<details><summary>Answer</summary>
TFTP is simple, connectionless (UDP/69), and unauthenticated — fine for a
trusted internal management network, which is why IOS's `copy` command
workflow defaults to it. FTP is connection-oriented (TCP/20-21) and
supports authentication, making it a better fit when the transfer needs to
cross a less-trusted network or leave an audit trail.
</details>

---

## Security Fundamentals

**Q5.** You want to block a specific host, 10.0.0.5, from reaching anything,
while permitting all other traffic, using a standard ACL. What does the ACL
match on?
<details><summary>Answer</summary>
Source IP address only — standard ACLs (1–99, 1300–1999) can only filter based
on source address, not destination, port, or protocol.
</details>

**Q6.** A switch port has port security configured with a max of 1 MAC address
and violation mode set to "restrict." A second device connects. What happens?
<details><summary>Answer</summary>
The port stays up, the violating traffic is dropped, and a syslog/SNMP alert
is generated — but the port does NOT go err-disabled. That's "shutdown" mode's
behavior instead.
</details>

**Q20.** What's the difference between authentication and authorization in
the AAA model?
<details><summary>Answer</summary>
Authentication proves who you are (username/password, certificate, MFA).
Authorization determines what you're allowed to do once authenticated
(which commands, which VLANs, which resources) — you can be authenticated
without being authorized for a specific action.
</details>

**Q21.** What does the "accounting" piece of AAA actually record?
<details><summary>Answer</summary>
A log of what an authenticated/authorized user actually did — commands
run, session start/stop times, resources accessed. It's the audit trail,
used for billing, compliance, or incident investigation after the fact.
</details>

**Q22.** Both RADIUS and TACACS+ can centralize authentication for network
device logins. Name one concrete way they differ.
<details><summary>Answer</summary>
TACACS+ encrypts the entire packet body and separates authentication,
authorization, and accounting into distinct exchanges (useful for granular
command-level authorization); RADIUS encrypts only the password field and
combines authentication+authorization into one exchange. TACACS+ also uses
TCP (49); RADIUS uses UDP (1812/1813).
</details>

**Q23.** An engineer wants to permit only host 10.0.0.10 to reach a server,
and block every other host in 10.0.0.0/24, using one standard ACL applied
inbound on the server's connected interface. What wildcard mask correctly
matches just that one host in a `permit`/`deny` line?
<details><summary>Answer</summary>
`0.0.0.0` — a wildcard of all zeros means every octet must match exactly,
so `permit 10.0.0.10 0.0.0.0` matches only that single address. (The
implicit `deny any` at the end of every ACL handles blocking the rest of
the subnet automatically.)
</details>

**Q24.** Why are standard ACLs conventionally placed as close to the
*destination* as possible, while extended ACLs go as close to the *source*
as possible?
<details><summary>Answer</summary>
A standard ACL only matches source address — placed too close to the
source, it would block that host from reaching *anything*, not just the
one destination you meant to restrict. An extended ACL can match source,
destination, protocol, and port together, so it can safely filter right at
the source without over-blocking.
</details>

**Q25.** A site-to-site VPN and a remote-access VPN both use encryption to
protect traffic. What's the structural difference between them?
<details><summary>Answer</summary>
A site-to-site VPN is a permanent, router/firewall-to-router/firewall
tunnel connecting two networks (e.g. two office LANs) — end users don't
see it. A remote-access VPN is a per-user, on-demand tunnel from an
individual client device (a laptop running VPN client software) into a
network, usually torn down when the user disconnects.
</details>

---

## Automation & Programmability

**Q7.** An API call to a controller returns HTTP status 404. What does that mean?
<details><summary>Answer</summary>
Not Found — the requested resource/endpoint doesn't exist. (Compare: 200 = OK,
401 = Unauthorized, 500 = Server Error.)
</details>

**Q8.** True or false: Ansible requires an agent installed on every managed
device.
<details><summary>Answer</summary>
False — Ansible is agentless, using SSH (or APIs) to push configuration. This
is a key differentiator from agent-based tools in exam questions.
</details>

**Q26.** An API call to update an existing resource on a controller should
use which REST/HTTP verb — and how does that differ from the verb you'd use
to fully replace the resource?
<details><summary>Answer</summary>
`PATCH` for a partial update (only the fields you send change); `PUT` for a
full replace (the entire resource is overwritten with what you send, so
omitted fields may be reset to defaults). Both differ from `POST`, which
creates a new resource rather than modifying an existing one.
</details>

**Q27.** A controller-based (SDN) architecture centralizes configuration
push through a controller, versus traditional device-by-device CLI
management. Name one operational tradeoff this introduces.
<details><summary>Answer</summary>
Faster, more consistent bulk changes (push one policy to hundreds of
devices at once) at the cost of a new single point of dependency — if the
controller is unreachable or misconfigured, that can affect the whole
managed fleet at once, unlike an isolated per-device CLI mistake.
</details>

**Q28.** Given this JSON snippet returned by a network API —
```json
{"interface": "GigabitEthernet0/1", "status": "up", "vlan": 10}
```
— what value would you extract to check whether the interface's VLAN
assignment is correct?
<details><summary>Answer</summary>
The value of the `"vlan"` key — `10`. Reading JSON is just matching a key
name to its value; here the interface is up and assigned to VLAN 10.
</details>

---

*Add your own missed-question entries to the relevant boss-battle file, not here — this file is a static question bank.*
