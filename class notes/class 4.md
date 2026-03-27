# Networking 
**Networking** is the practice of connecting computers and other hardware devices to share resources, transport data, and communicate.
## Types of Network
   - PAN 
   A PAN is the smallest and most basic type of network. It is designed for a single person, typically within a range of **10 meters** (about 33 feet).
- **Purpose:** Syncing personal devices.
- **Examples:** Connecting your Bluetooth headphones to your smartphone, or a smartwatch to a tablet.
-  **Technology:** Bluetooth, Zigbee, Infrared.
   - LAN
A LAN connects devices within a limited area, such as a single room, a home, or an office building. It is private, high-speed, and very secure.
- **Purpose:** Sharing resources like printers, files, or an internet connection among multiple users in one location.
- **Examples:** Your home Wi-Fi network or a small business Ethernet setup.
- **Technology:** Ethernet (cables), Wi-Fi (WLAN).
   - MAN
A MAN spans an entire city or a large campus. It is essentially a collection of several LANs connected together to cover a larger area than a single building but smaller than a wide geographic region.
- **Purpose:** Connecting multiple branches of a business or government offices across a city.
- **Examples:** A city-wide public Wi-Fi network or a university campus network.
- **Technology:** Fiber optic cables, microwave transmission.
   - WAN
A WAN covers a vast distance, such as a country, a continent, or even the entire globe. It connects smaller networks (LANs and MANs) so that computers in one location can communicate with computers in another remote location.
- **Purpose:** Global communication and data exchange.
- **Examples:** **The Internet** is the largest and most well-known WAN.
- **Technology:** Leased lines, satellites, fiber optic transoceanic cables.
## IP And Mac Address
### IP
- An **IP (Internet Protocol) Address** is a unique numerical label assigned to every device connected to a computer network.
#### Types of IP
##### IPv4
IPv4 is the most widely used version, though its addresses are technically "exhausted" (we've run out of new ones).
- **Format:** 32-bit address displayed as four decimal numbers separated by dots (e.g., `192.168.1.1`).
- **Capacity:** Supports approximately **4.3 billion** unique addresses.
- **Structure:** Each number (octet) ranges from 0 to 255.
##### IPv6
IPv6 was created to replace IPv4 and provide an almost infinite number of addresses.
- **Format:** 128-bit address displayed as eight groups of four hexadecimal digits separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
- **Capacity:** Supports $3.4 \times 10^{38}$ addresses (340 undecillion).
- **Features:** More secure (built-in IPsec) and more efficient routing than IPv4.
## Class of Networking

![[Pasted image 20260322074148.png]]


# OSI Model 
- The OSI (Open Systems Interconnection) Model is a conceptual framework used to understand how data moves across a network. It breaks down the complex process of network communication into seven distinct layers, each with a specific job and set of protocols.
- There Are Seven Layers
1. Layer 7 : Application 
 - This is the layer where users interact with network services. When we use a web browser or an email client, you are at the Application layer.
 - Protocols use **HTTP, FTP, SMTP, DNS  **
2. Layer 6: Presentation
- This layer acts as a translator. It ensures that data is in a usable format and handles tasks like **encryption**, **decryption**, and **compression**.
- Protocols use  **TLS, SSL **
3. Layer 5: Session
- This layer manages the "conversation" between two devices. It opens, maintains, and closes the connection (session) to ensure data is synchronized and handled correctly.
- **Key Task:** Authentication and session restoration.
4. Layer 4: Transport
- The Transport layer is responsible for end-to-end communication. it determines how much data to send, at what speed, and where it goes.
- Protocols use **TCP, UDP**
5. Layer 3: Network
- This is where **routing** happens. It determines the best physical path for the data to take to reach its destination based on IP addresses.
- Protocols use  IP **(IPv4/IPv6), ICMP.**
6. Layer 2: Data Link 
- This layer handles node-to-node data transfer. It packages data into **frames** and handles error correction from the physical layer. It uses **MAC addresses** to identify specific hardware.
- **Key components:** Switches and Bridge.
7. Layer 1: Physical 
- 1. The "lowest" layer consists of the actual hardware and physical medium (cables, radio waves, fiber optics) used to transmit raw bit streams.
   - **Key components:** Hubs, Repeaters, Ethernet cables.
