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

---

*Add your own missed-question entries to the relevant boss-battle file, not here — this file is a static question bank.*
