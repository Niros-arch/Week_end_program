Here’s a **clear and simple explanation of TCP vs UDP** 
# TCP vs UDP (Well Explained)
## What is TCP?
**Transmission Control Protocol** is a **reliable, connection-oriented** protocol.
This means:
- ✔ Ensures data arrives
- ✔ Sends data in order
- ✔ Resends lost packets
- ✔ Slower but reliable
### How TCP Works
TCP uses **3-Way Handshake**:
1. Client → SYN
2. Server → SYN-ACK
3. Client → ACK
Connection established ✅
### TCP Characteristics
- Reliable
- Slower
- Ordered delivery
- Error checking
- Connection-based
### TCP Common Ports
![[Pasted image 20260327151601.png]]
## What is UDP?

**User Datagram Protocol** is a **fast, connectionless** protocol.
This means:
- ❌ No delivery guarantee
- ❌ No order guarantee
- ✔ Faster
- ✔ Lightweight
### How UDP Works
UDP just **sends data immediately** — no handshake.
Like sending a letter **without tracking** 
### UDP Characteristics
- Fast
- No connection
- No error correction
- No retransmission
- Lightweight
### UDP Common Ports

|Port|Service|
|---|---|
|53|DNS|
|67/68|DHCP|
|69|TFTP|
|123|NTP|
|161|SNMP|
|500|VPN|
|514|Syslog|
![[Pasted image 20260327151655.png]]
