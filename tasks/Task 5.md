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
<img width="814" height="377" alt="image" src="https://github.com/user-attachments/assets/ae01385b-dff6-439e-bccb-5ab7e73c7e49" />

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
<img width="814" height="377" alt="image" src="https://github.com/user-attachments/assets/b29047b2-967f-428a-920a-7d60641516d0" />

