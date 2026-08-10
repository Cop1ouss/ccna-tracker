# Mock Exam 1 — CCNA 200-301 v1.1

65 questions, weighted at the real exam's domain distribution: Network
Fundamentals 13, Network Access 13, IP Connectivity 16, IP Services 6,
Security Fundamentals 10, Automation & Programmability 7.

**Take this cold.** Answers and explanations are in
[`mock-exam-1-answers.md`](mock-exam-1-answers.md) — don't open it until
you've answered everything (or given up on a question and moved on, same
as the real exam). Budget ~90 minutes. Cisco's unofficial passing cut is
roughly 82–85%, so treat 85%+ here as your real target, not 60%.

Log anything you miss in the matching `boss-battles/*.md` file's
missed-question table, not here.

---

## Network Fundamentals (Q1–13)

**Q1.** Which device operates primarily at Layer 2, forwarding frames based on MAC address?
A) Router B) Switch C) Firewall D) Wireless LAN Controller

**Q2.** A campus network uses an access/distribution/core hierarchy. Which layer is responsible for high-speed backbone transport, not policy enforcement?
A) Access B) Distribution C) Core D) Edge

**Q3.** What is the maximum reliable distance for Cat 6A UTP running 10GBASE-T?
A) 55 meters B) 100 meters C) 185 meters D) 300 meters

**Q4.** Two switch ports are hard-set to full duplex on one end and left at auto on the other. What's the likely symptom?
A) Link stays down B) Duplex mismatch causing collisions/errors C) No effect, auto detects the hard-set side D) Speed drops to 10 Mbps

**Q5.** A network has 5 hosts on a segment and needs the smallest subnet that fits them with room to grow to 8. What prefix length?
A) /27 B) /28 C) /29 D) /30

**Q6.** Which IPv6 address type is roughly equivalent in purpose to public IPv4 addressing?
A) Link-local B) Unique local C) Global unicast D) Multicast

**Q7.** What does EUI-64 use to generate the interface ID portion of an IPv6 address?
A) A random 64-bit value B) The device's MAC address, split and padded with FFFE C) The subnet prefix reversed D) A DHCPv6-assigned value

**Q8.** A switch receives a frame destined for a MAC address not in its MAC address table. What does it do?
A) Drops the frame B) Floods it out all ports except the one it arrived on C) Sends an ARP request D) Forwards it to the default gateway

**Q9.** Which wireless band offers the most non-overlapping channels and least legacy-device interference?
A) 2.4 GHz B) 5 GHz C) 6 GHz D) They're identical

**Q10.** What best describes the relationship between a hypervisor and a virtual machine?
A) The VM runs the hypervisor as an application B) The hypervisor abstracts physical hardware so multiple VMs can share it C) They are the same thing D) A hypervisor is a type of VM

**Q11.** In the OSI model, at which layer does a router primarily make forwarding decisions?
A) Layer 1 B) Layer 2 C) Layer 3 D) Layer 4

**Q12.** A host is configured with IP 192.168.5.10/25. What is the broadcast address for its subnet?
A) 192.168.5.127 B) 192.168.5.255 C) 192.168.5.128 D) 192.168.5.63

**Q13.** What's the primary purpose of an SFP+ transceiver on a switch?
A) Power delivery to end devices B) Modular fiber/copper media flexibility on a single port C) Wireless signal amplification D) VLAN tagging

---

## Network Access (Q14–26)

**Q14.** A trunk port carries VLANs 10, 20, and untagged native VLAN traffic. What VLAN is the native VLAN if never explicitly configured?
A) VLAN 0 B) VLAN 1 C) The lowest numbered VLAN on the trunk D) There is no default

**Q15.** What does `switchport mode dynamic desirable` do?
A) Hard-sets the port as a trunk B) Actively negotiates trunking via DTP with the far end C) Disables the port D) Forces access mode

**Q16.** CDP is a discovery protocol that works between which types of devices?
A) Any vendor's devices B) Cisco devices only C) Only routers, not switches D) Only wireless devices

**Q17.** Which protocol is the vendor-neutral equivalent to CDP?
A) STP B) LLDP C) DTP D) VTP

**Q18.** An EtherChannel is configured with `channel-group 1 mode active` on both switches. What protocol negotiates this bundle?
A) PAgP B) LACP C) DTP D) HSRP

**Q19.** In Rapid PVST+, which port role is elected for the switch with the lowest bridge ID?
A) Root port B) Designated port on all its ports (it's the root bridge) C) Blocking D) Alternate

**Q20.** What's the STP port state that forwards no traffic and doesn't yet learn MAC addresses, but does listen for BPDUs?
A) Forwarding B) Learning C) Listening D) Blocking

**Q21.** BPDU Guard is applied to an access port and a BPDU arrives. What happens?
A) The port ignores it B) The port becomes root port C) The port is err-disabled D) The switch reboots

**Q22.** Root Guard differs from BPDU Guard how?
A) They're identical B) Root Guard prevents a port from becoming root port if it hears a superior BPDU, rather than shutting the port down entirely C) Root Guard only works on trunk ports D) Root Guard is deprecated

**Q23.** A lightweight AP is powered on with no prior configuration. Where does it get its operating configuration?
A) A local config file on the AP B) A WLC it registers to C) Manual CLI entry only D) It broadcasts its own SSID by default with no config needed

**Q24.** Which WLC deployment model runs the controller function in the cloud rather than on local hardware?
A) Centralized B) Cloud-based C) Embedded D) Autonomous

**Q25.** A WLAN is configured for WPA3-Personal. What does the client use to authenticate?
A) A certificate B) A shared passphrase (PSK) C) 802.1X with RADIUS D) MAC address whitelisting

**Q26.** What's the primary reason non-overlapping channels matter in 2.4 GHz Wi-Fi design?
A) Regulatory requirement only B) Adjacent-channel interference degrades throughput when overlapping channels are used nearby C) It affects encryption strength D) It changes the SSID broadcast range

---

## IP Connectivity (Q27–42)

**Q27.** A routing table has a static route to 10.1.0.0/16 (AD 1) and an OSPF route to 10.1.1.0/24 (AD 110). A packet is destined for 10.1.1.5. Which route is used?
A) The static /16 route, because AD 1 beats AD 110 B) The OSPF /24 route, because longest-prefix match is evaluated first C) Both, load-balanced D) Neither; the packet is dropped

**Q28.** What administrative distance does a directly connected route have?
A) 0 B) 1 C) 90 D) 110

**Q29.** A static route is configured with an unreachable next hop. What happens to it in the routing table?
A) It stays installed regardless B) It is not installed until the next hop becomes reachable C) It's installed with AD 255 D) It replaces the default route

**Q30.** What's the purpose of a floating static route configured with AD 5 when the primary route to the same destination has AD 1?
A) It load-balances with the primary route B) It only activates as a backup if the AD-1 route disappears from the table C) It takes priority over the AD-1 route D) It has no effect since AD 1 always wins

**Q31.** On a broadcast multi-access OSPF segment with three routers, how many of them will show FULL adjacency with each other in a typical steady state?
A) All three form FULL with each other B) Only the DR and BDR form FULL with everyone; DROTHERs stay 2-WAY with each other C) None form FULL D) Only the router with the lowest router ID forms FULL

**Q32.** What determines an OSPF router's router ID if not explicitly configured?
A) Lowest MAC address B) Highest IP address on any active loopback, or highest IP on any active physical interface if no loopback exists C) A random value D) The hostname, hashed

**Q33.** Two OSPF neighbors are stuck in EXSTART and never reach FULL. What's a common cause?
A) A VLAN mismatch B) An MTU mismatch between the two interfaces C) A missing default route D) DHCP is not configured

**Q34.** What command suppresses OSPF hello packets on an interface while still advertising its connected subnet?
A) `no ip ospf enable` B) `passive-interface` C) `shutdown` D) `ip ospf priority 0`

**Q35.** Which `show` command displays OSPF neighbor states and roles (DR/BDR/DROTHER)?
A) `show ip route ospf` B) `show ip ospf neighbor` C) `show ip protocols` D) `show ip ospf database`

**Q36.** In HSRP, what happens if the Active router reboots and comes back online, with preempt disabled?
A) It automatically reclaims the Active role B) It stays Standby; the current Active keeps the role C) Both routers become Active D) HSRP resets the group entirely

**Q37.** What virtual MAC address format does HSRP use for its virtual gateway?
A) A random MAC generated at boot B) 0000.0C07.ACxx, where xx encodes the group number C) The Active router's real MAC D) FF:FF:FF:FF:FF:FF

**Q38.** VRRP is best described as:
A) A Cisco-proprietary alternative to HSRP B) The open-standard (IETF) equivalent to HSRP/GLBP for first-hop redundancy C) A routing protocol, not a redundancy protocol D) A Layer 2 protocol only

**Q39.** A routing table shows `S 0.0.0.0/0 [1/0] via 203.0.113.1` and a connected route to 192.168.1.0/24. A packet destined for 8.8.8.8 arrives. Which route is used?
A) The connected route B) The default route (0.0.0.0/0) C) Neither; dropped D) Both, split evenly

**Q40.** What's the correct IOS syntax to configure a default IPv6 route pointing to next-hop 2001:db8::1?
A) `ip route 0.0.0.0 0.0.0.0 2001:db8::1` B) `ipv6 route ::/0 2001:db8::1` C) `ipv6 default-route 2001:db8::1` D) `route ipv6 any 2001:db8::1`

**Q41.** Given routes `172.16.1.0/24` and `172.16.1.128/25` to the same next-hop family, which is preferred for a packet destined to 172.16.1.200?
A) The /24, because it was configured first B) The /25, because it's the longer (more specific) match C) Whichever has the lower AD D) They're evaluated as a tie and load-balanced

**Q42.** What's the main risk of configuring two static routes to the same destination with identical administrative distance via two different next hops?
A) IOS rejects the second one automatically B) Traffic load-balances across both, which may be undesired if one path is meant purely as backup C) It causes a routing loop D) The routes fail silently

---

## IP Services (Q43–48)

**Q43.** A firewall shows all outbound internet traffic from an internal /24 network using a single public IP address, differentiated by source port. What NAT type is this?
A) Static NAT B) Dynamic NAT C) PAT (NAT overload) D) NAT64

**Q44.** What's the primary purpose of `ip helper-address` on a router interface?
A) Encrypts DHCP traffic B) Relays broadcast services like DHCP to a unicast server on another subnet C) Assigns static IPs D) Configures NTP

**Q45.** A syslog message arrives at severity level 2. How urgent is it relative to the full 0–7 scale?
A) Least urgent (informational) B) Moderately urgent C) Very urgent — 2 (Critical) is near the top of the severity scale D) Irrelevant; severity doesn't indicate urgency

**Q46.** Why does IOS's `crypto key generate rsa` step matter before enabling SSH?
A) It's optional cosmetic step B) SSH requires an RSA key pair to establish its encrypted session; without one, `ip ssh version 2` has nothing to use C) It generates the enable password D) It's required only for Telnet, not SSH

**Q47.** What's the functional difference between TFTP and FTP for IOS image/config transfers?
A) No difference B) TFTP is UDP-based and unauthenticated; FTP is TCP-based and supports authentication C) FTP is faster but insecure D) TFTP requires a username/password, FTP does not

**Q48.** An engineer needs to synchronize the clock on 40 routers so syslog timestamps and certificate validation are consistent. What service is designed for this?
A) SNMP B) NTP C) TFTP D) SSH

---

## Security Fundamentals (Q49–58)

**Q49.** What's the difference between a vulnerability and an exploit?
A) They're synonyms B) A vulnerability is a weakness; an exploit is the specific method/code used to take advantage of that weakness C) An exploit is always a piece of malware D) A vulnerability only applies to software, never hardware

**Q50.** In the AAA model, which piece answers "what is this authenticated user allowed to do"?
A) Authentication B) Authorization C) Accounting D) Auditing

**Q51.** TACACS+ differs from RADIUS in which concrete way?
A) TACACS+ uses UDP; RADIUS uses TCP B) TACACS+ encrypts the full packet body and separates AAA functions; RADIUS encrypts only the password and combines authentication/authorization C) They are functionally identical D) RADIUS is Cisco-proprietary; TACACS+ is the open standard

**Q52.** A standard IPv4 ACL can filter traffic based on:
A) Source and destination IP, protocol, and port B) Source IP address only C) Destination IP address only D) MAC address only

**Q53.** What wildcard mask matches an entire /24 network in an ACL statement?
A) 255.255.255.0 B) 0.0.0.255 C) 0.0.0.0 D) 255.255.255.255

**Q54.** Why are standard ACLs conventionally placed close to the destination rather than the source?
A) Performance only B) Because they can only match source address, placing them near the source would block that host from reaching everything, not just the intended destination C) IOS enforces this placement D) There's no reason; placement doesn't matter

**Q55.** Port security is configured with `switchport port-security violation restrict`. A second, unauthorized MAC address is seen on the port. What happens?
A) The port is err-disabled B) Traffic from the new MAC is dropped, a violation is logged, but the port stays up C) All traffic on the port is dropped, port stays up D) Nothing; restrict mode takes no action

**Q56.** DHCP snooping is enabled on a switch with `ip dhcp snooping vlan 10`, and all uplinks are marked as trusted. What does this protect against?
A) MAC flooding B) Rogue DHCP servers handing out bogus configuration on untrusted (access/host-facing) ports C) VLAN hopping D) ARP spoofing directly (that's DAI's job)

**Q57.** What's the structural difference between a site-to-site VPN and a remote-access VPN?
A) Site-to-site connects two networks via gateway devices permanently; remote-access connects an individual client on demand B) They are the same thing with different names C) Remote-access VPNs never use encryption D) Site-to-site VPNs only work over MPLS

**Q58.** WPA3-Enterprise differs from WPA3-Personal primarily by:
A) Using a stronger encryption cipher only B) Requiring 802.1X/EAP authentication against a backend server instead of a shared passphrase C) Not supporting 6 GHz D) Being deprecated in favor of WPA2

---

## Automation & Programmability (Q59–65)

**Q59.** Which HTTP verb is used to retrieve a resource via a REST API without modifying it?
A) POST B) GET C) PUT D) DELETE

**Q60.** An API call returns HTTP status 401. What does this indicate?
A) Resource not found B) Server error C) Unauthorized — authentication failed or is missing D) Success

**Q61.** Is Ansible agent-based or agentless, and what does it typically use to reach managed devices?
A) Agent-based, requiring software installed on every device B) Agentless, typically using SSH or APIs C) Agent-based, requiring a dedicated hardware appliance D) Agentless, but only works over SNMP

**Q62.** Terraform is primarily categorized as what kind of tool?
A) A configuration-management tool identical to Ansible B) An infrastructure-as-code / provisioning tool, often used to declare and stand up infrastructure state C) A network monitoring tool D) A routing protocol

**Q63.** Given the JSON `{"vlan": 20, "status": "active"}`, what data type is the value associated with `"vlan"`?
A) String B) Number C) Boolean D) Array

**Q64.** What's a key architectural difference between traditional network management and controller-based (SDN) management?
A) Traditional management is always faster B) Controller-based management centralizes configuration push through one control point instead of touching each device's CLI individually C) SDN eliminates the need for switches D) Traditional management requires no CLI knowledge

**Q65.** Which of these is a predictive (rather than generative) AI/ML use case in network operations?
A) A chatbot that answers "how do I configure VLAN 10" B) Forecasting link capacity exhaustion before it happens based on historical trend data C) Auto-generating a sample config snippet from a prompt D) Summarizing a long log file into a paragraph
