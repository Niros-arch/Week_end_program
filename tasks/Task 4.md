# Port 
- A **port** is **NOT** a physical connection it is a ***Logical connection*** that's used by programs and service to exchange information 
- it specifically determines w/c **Program** or **Service** on a computer or server that is going to be used 
- Ports will have a unique number that identifies them 
- the number ranges is **0-65535** like 80,443- web pages (HTTP,HTTPS) 
- A port is always associated with an Ip address
- They are assigned by **IANA** 
- Port numbers are broken down into 3 categories 
- Port numbers 0-1023 are called System or Well-known ports.
- Port numbers 1024-49151 are called User or Registered ports. These are ports that can be registered by companies and developers for a particular service. like adobe server (1102) and oracle (1527)
- Port numbers 49152-65535 are called Dynamic or Private ports. These are client-side ports that are free to use 
## Top 30 common ports and what kind of attacks can they face?
### **KIBANA**
- `Default Port: 5601`
- **Kibana** is an open-source data visualization and exploration tool used for log and time-series analytics. It provides powerful and beautiful dashboards for real-time visualization of data in Elasticsearch.
- **Unauthorized takeover** is possible through several attack vectors if the instance is unsecured:
  - **Attack Vectors**
  I. Defalt Credentials 
  II. ### Kibana File Read Vulnerability (CVE-2019-7609)
  III. ### Remote Code Execution via Kibana Timelion (CVE-2018-17246)
### WinRM (Windows Remote Management)
- **`Default Ports: 5985 (HTTP), 5986 (HTTPS)`**
- **Windows Remote Management (WinRM)** is Microsoft's implementation of the WS-Management protocol, allowing remote management of Windows machines. It's built into Windows and commonly used for remote administration, PowerShell remoting, and system automation. WinRM is the native remote management protocol for Windows and is often preferred over RDP in enterprise environments.
-  the attack that can be happen on Win RM 
1. **brute-force attacks**
2.  **password spraying**
3.  **pass-the-hash**
4. **Lateral Movement**\
5. **In-Memory Execution**
- these three attacks can do  on the Win Rm
- tools that can use on this 
1. evil-winrm
2. NetExec
3. PowerShell Cradles 
4. .NET Module Loaders
#### Using evil-winrm 
```
# Basic connection
evil-winrm -i target.com -u administrator -p 'password'

# With domain
evil-winrm -i target.com -u 'DOMAIN\username' -p 'password'

# Using hash (Pass-the-Hash)
evil-winrm -i target.com -u administrator -H 'NTHASH'

# Using SSL (port 5986)
evil-winrm -i target.com -u administrator -p 'password' -S

# With custom port
evil-winrm -i target.com -u administrator -p 'password' -P 5985
```
#### Using  Power-Shell 
```
# Create credentials
$password = ConvertTo-SecureString "password" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("administrator", $password)

# Connect interactively
Enter-PSSession -ComputerName target.com -Credential $cred

# Run command remotely
Invoke-Command -ComputerName target.com -Credential $cred -ScriptBlock { whoami }

# Connect to multiple machines
$computers = "server1", "server2", "server3"
Invoke-Command -ComputerName $computers -Credential $cred -ScriptBlock { hostname }
```
#### Using NetExec
```
netexec winrm target.com -u administrator -p 'password'          # Basic connection

netexec winrm target.com -u username -p 'password' -d DOMAIN     # With domain

netexec winrm target.com -u administrator -H 'NTHASH'            # Pass-the-Hash

netexec winrm target.com -u administrator -p 'password' --port 5986  # Using SSL (5986)

netexec winrm target.com -u administrator -p 'password' --port 5985  # Custom port

netexec winrm target.com -u users.txt -p 'Password123!'          # Password spray

netexec winrm target.com -u users.txt -p passwords.txt           # Brute force

netexec winrm target.com -u administrator -p 'password' -x "whoami"  # Execute command

netexec winrm target.com -u administrator -p 'password' -X "whoami"  # Execute PowerShell

netexec winrm target.com -u administrator -p 'password' --local-auth # Local authentication

netexec winrm targets.txt -u administrator -p 'password'          # Multiple targets
```
### Telnet
- **`Default Port: 23`**
-  **Telnet** is an old network protocol that provides insecure access to computers over a network. It is used to connect to remote systems over TCP/IP networks. However, due to security vulnerabilities, its usage is not recommended, and more secure alternatives like SSH are preferred.
-  the attack that can be happen on Telnet 
1. **Brute force attacks** :- are common, where attackers use automated tools to guess passwords on Telnet lines, especially when weak or default credentials are used.
2. **Remote Code Execution (RCE)** :-vulnerabilities, including CVE-2026-32746 and CVE-2023-40478, enable attackers to execute arbitrary code or cause stack-based buffer overflows during protocol negotiation or command processing.
3. **Man-in-the-Middle** :--  attacks exploit the unsecured connection to modify traffic or inject malicious commands between the client and server. 
###  TFTP (Trivial File Transfer Protocol)
- **`Default Port: 69 (UDP)`**
- **Trivial File Transfer Protocol (TFTP)** is a simple, lockstep file transfer protocol that uses UDP port 69. It's designed to be simple and easy to implement, lacking the authentication and features of FTP. TFTP is commonly used for booting diskless workstations, uploading configurations to network devices, and firmware updates. Due to its lack of authentication, it can be a significant security risk when misconfigured.
-  the attack that can be happen on TFTP 
1. **Reflection/Amplification DDoS** :-  Attackers send small, crafted Read Request (RRQ) or Write Request (WRQ) packets with a spoofed victim IP to public TFTP servers (approx. 599,600 open servers exist), causing the servers to reply with large data packets to the victim, as seen in attacks peaking at **1.2 Gbps**.
2. **Data Interception and Exfiltration** :- Since TFTP transmits all data in **clear text**, attackers can perform packet sniffing to intercept sensitive information such as **firmware, configuration files, and passwords** embedded in device settings.
3. **Malware Delivery and Persistence** :- The protocol's simplicity allows attackers to upload modified firmware or malware to devices like Cisco routers (e.g., the **SYNful Knock** malware) to maintain persistent control over network infrastructure.
###  Apache Tomcat
- **`Default Ports: 8080 (HTTP), 8443 (HTTPS), 8009 (AJP)`**
- **Apache Tomcat** is an open-source Java Servlet Container and web server developed by the Apache Software Foundation. It implements Java Servlet, JavaServer Pages (JSP), and WebSocket specifications. Tomcat is widely used for hosting Java web applications and is a common target in enterprise environments.
- Apache Tomcat servers face several critical attack vectors, primarily targeting **Remote Code Execution (RCE)**, **Denial of Service (DoS)**, and **Unauthorized Access** via misconfigured management interfaces.
### SSH (Secure Shell)
- **`Default Port: 22 
- **Secure Shell (SSH)** is a protocol used to securely connect to another computer over a network. It allows you to log into another computer, execute commands, and transfer files, all in a secure manner. This is because SSH encrypts your connection, making it difficult for hackers to intercept and understand the data being exchanged.
- It's commonly used by network administrators to control web servers, by developers to access programming environments, and by anyone needing secure access to a computer over the internet.
 1. - **Brute-force and Dictionary Attacks**: Automated guessing of credentials to gain unauthorized access. 
2. **Man-in-the-Middle (MITM)**: Interception of traffic to capture passwords or alter data if host keys are not verified. 
3.  **Session Hijacking**: Taking over an active TCP connection to inject commands or steal data. 
4.  **Key Management Issues**: Risks from unmanaged keys (key sprawl), stolen private keys, or weak passphrases. 
5.  **DoS Attacks**: Flooding the server with connection requests to exhaust computational resources.
6. **Software Vulnerabilities**: Exploiting known flaws in outdated SSH versions (e.g., CVE-2021-28041) or misconfigured settings.
#### Connect with Terminal
If you have knowledge of a target credential, you can establish a remote server connection via SSH using that credential.

```
ssh username@X.X.X.X
```

If you have the private key, you can log in to a remote server using SSH.

```
ssh -i path/to/private_key user@target-ip
```
###  SMB (Server Message Block)
 - **`Default Port: 139, 445`**
 - **SMB (Server Message Block)**, also known as CIFS (Common Internet File System), is a network protocol that allows for file sharing, network browsing, printing services, and inter-process communication over a network. The SMB protocol provides you with the ability to access resources from a server.
 1. **SMB Relay Attacks**: Attackers position themselves as a man-in-the-middle to intercept authentication requests and relay credentials to other targets, often exploiting disabled SMB signing. 
2. **Protocol Exploits**: Vulnerabilities in older versions like **SMBv1** (e.g., **EternalBlue**, **SMBGhost**) allow for remote code execution, enabling malware like **WannaCry** and **NotPetya** to self-propagate across networks. 
3. **Man-in-the-Middle (MitM)**: Threat actors inject malicious code or use ARP spoofing to intercept data, steal credentials, or alter communications between clients and servers. 
4. **Brute Force and Pass-the-Hash**: Automated tools guess credentials, while attackers reuse stolen hashes to move laterally within a network.
 #### Connect 
In order to initiate the process, it's imperative to establish a connection to the Server Message Block (SMB) server.

```
smbclient -L //target-ip
```
### RDP (Remote Desktop Protocol)
- **`Default Port: 3389`**
- **Remote Desktop Protocol (RDP)** is a proprietary protocol developed by Microsoft that provides a graphical interface for users to connect to another computer over a network connection. RDP is widely used for remote administration, technical support, and accessing work computers from home. It transmits keyboard, mouse, and display data between client and server, making it a critical service in Windows environments.
1.  **Brute Force and Credential Stuffing**: Attackers use scripts to systematically try username-password combinations or reuse leaked credentials from other breaches to gain unauthorized access. 
2. **Vulnerability Exploitation**: Outdated systems are targeted by worms and exploits like BlueKeep that allow attackers to execute code remotely or spread across networks without user interaction. 
3. **Rogue RDP and Proxy Attacks**: Threat actors deploy malicious RDP configurations to redirect traffic to rogue servers, enabling **data exfiltration**, **clipboard capture**, and the installation of malware via resource redirection. 
4. **Denial of Service (DoS)**: Servers can be overwhelmed with connection requests to disrupt legitimate access and cause downtime. 
5. **Lateral Movement**: Once inside, attackers often use RDP as a foothold to move laterally across the network, escalate privileges, and deploy ransomware.
#### Using xfreerdp (Linux)
```
# Basic connection
xfreerdp /v:target.com

# With credentials
xfreerdp /u:administrator /p:password /v:target.com

# With domain
xfreerdp /u:DOMAIN\\username /p:password /v:target.com

# Full options
xfreerdp /u:administrator /p:password /v:target.com:3389 \
  /cert:ignore /size:1920x1080 +clipboard +drives

# Pass-the-Hash
xfreerdp /u:administrator /pth:NTHASH /v:target.com

# Dynamic resolution
xfreerdp /u:username /p:password /v:target.com /dynamic-resolution
```
#### Using mstsc (Windows)
```
# Basic connection
mstsc /v:target.com

# With specific port
mstsc /v:target.com:3389

# Full screen mode
mstsc /v:target.com /f

# Admin mode
mstsc /v:target.com /admin

# Save connection settings
mstsc /v:target.com /save:connection.rdp
```

###  Oracle Database
- **`Default Ports: 1521 (Listener), 1630 (iSQL*Net)`** 
- **Oracle Database** is a multi-model database management system produced and marketed by Oracle Corporation. It's one of the most widely used enterprise relational database management systems, particularly in large corporations and government organizations. Oracle Database offers advanced features including stored procedures, triggers, and the ability to execute Java code within the database. Due to its complexity and enterprise deployment, Oracle databases often contain highly sensitive data and can be challenging to secure properly. 
- Oracle databases face several critical attack vectors, including **SQL injection**, which allows attackers to insert malicious commands into queries to retrieve or corrupt data, and **Padding Oracle Attacks**, which exploit encryption feedback to decrypt ciphertext or craft valid encrypted messages.  Other significant threats include **Timing Oracle Attacks**, where response times reveal sensitive information, and **Blind Oracle Attacks**, which infer data through indirect behavioral changes rather than direct error messages.
### NTP (Network Time Protocol)
- **`Default Port: 123 (UDP)`**
- **Network Time Protocol (NTP)** is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. NTP is one of the oldest internet protocols still in use and is critical for maintaining accurate time across networks. Precise time synchronization is essential for security protocols like Kerberos, logging systems, and distributed applications. NTP servers can leak system information and, in some cases, be exploited for amplification attacks.
- Network Time Protocol (NTP) is vulnerable to several distinct attack vectors, primarily **amplification attacks**, **time manipulation**, and **denial of service (DoS)** exploits.
### LDAP (Lightweight Directory Access Protocol) 
- **`Default Ports: 389 (LDAP), 636 (LDAPS), 3268 (Global Catalog)`** 
- **Lightweight Directory Access Protocol (LDAP)** is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an IP network. LDAP is commonly used for user authentication, authorization, and storing organizational information. Microsoft's Active Directory is built on LDAP. LDAP directories store information hierarchically in a tree structure.
1. **LDAP Injection**: Attackers inject malicious characters into user input fields to manipulate LDAP queries, enabling **authentication bypass**, **privilege escalation**, or **data exfiltration**.  For example, inserting `*)(uid=*))(|(uid=*` can bypass password checks or retrieve all user objects.
2. **Pass-Back Attacks**: Malicious LDAP servers intercept authentication requests and redirect them to attacker-controlled systems to **capture user credentials** or session tokens. 
3. **Anonymous and Null Bind Exploits**: Attackers leverage unauthenticated or empty-credential binds to **enumerate directory contents** without valid credentials, exposing sensitive organizational data. 
4. **Brute Force Attacks**: Automated tools like Hydra or Nmap scripts attempt to **guess valid credentials** by testing large lists of usernames and passwords against LDAP services. 
5. **Blind LDAP Injection**: When direct output is not visible, attackers infer directory structure or user attributes by observing **true/false responses** over time. 
6. **Denial of Service (DoS)**: Crafted queries can consume excessive server resources, **crashing applications** or making the directory unavailable to legitimate users.
### Kerberos
- **`Default Port: 88`**
- **Kerberos** is a network authentication protocol designed to provide strong authentication for client/server applications using secret-key cryptography. Developed by MIT, it's the default authentication protocol in Windows Active Directory environments. Kerberos uses tickets to allow nodes to prove their identity over non-secure networks without transmitting passwords. The protocol involves a Key Distribution Center (KDC) that includes an Authentication Server (AS) and a Ticket Granting Server (TGS).
1.  Roasting and Delegation Attacks :- **Kerberoasting** is a sophisticated post-exploitation technique where an authenticated user requests service tickets (TGS) for accounts with Service Principal Names (SPNs).  The attacker then cracks the encrypted password hash offline to recover plaintext credentials, a method frequently used by groups like **FIN7** and the **Akira Ransomware Group** to gain elevated access.  **AS-REQ Roasting** (or ASREPRoast) occurs when **Kerberos pre-authentication** is disabled for a user account, allowing attackers to request an authentication response without a password and brute-force the resulting hash.
2.  Ticket Forgery and Abuse :- **Golden Ticket** attacks involve forging a Ticket Granting Ticket (TGT) using the `krbtgt` account's password hash, granting the attacker unrestricted access to the entire domain and the ability to impersonate any user, including administrators.  **Silver Ticket** attacks are less powerful but stealthier, as they forge a Ticket Granting Service (TGS) for a specific service, allowing access to that resource without contacting the Domain Controller.  **Pass-the-Ticket** attacks focus on stealing existing TGTs or TGS tickets to perform lateral movement across the network.  Additionally, **Delegation attacks** such as **Unconstrained Delegation**, **Constrained Delegation**, and **Resource-Based Constrained Delegation** allow attackers to impersonate users to access other services by exploiting misconfigured trust relationships.
3.  Impact and Mitigation : -These attacks pose a **high impact** risk to industries like healthcare, finance, and retail, leading to data breaches, regulatory fines, and infrastructure compromise.  Defense strategies rely on **strong passwords**, **AES encryption**, **Group Managed Service Accounts (gMSAs)**, and **Multi-Factor Authentication (MFA)**, alongside rigorous auditing of **Ticket Granting Ticket (TGT)** and **Ticket Granting Service (TGS)** operations to detect anomalies
#### Connect
-  Using kinit (Get TGT)
Use the standard
Kerberos client to obtain Ticket Granting Tickets.

```
# Request Ticket Granting Ticketkinit username@DOMAIN.COM# With passwordecho 'password' | kinit username@DOMAIN.COM# Check ticketsklist# Destroy ticketskdestroy
```
#### Using Impacket Tools
Use Impacket tools for advanced Kerberos operations and ticket management.
```
# Get TGTgetTGT.py DOMAIN/username:password# Use ticketexport KRB5CCNAME=username.ccache# Request service ticketgetST.py -spn service/hostname DOMAIN/username -k -no-pass
```

###  FTP (File Transfer Protocol)
- **`Default Port: 21`**
- **FTP (File Transfer Protocol)** is a standard network protocol used for transferring files from one host to another over a TCP-based network, such as the Internet. It enables users to upload or download files, manage file directories on a remote server, and navigate the server's file system. FTP operates on a `client-server` model, where the client initiates a connection to the server to request files or submit files for storage. The protocol supports anonymous access, where users can log in with a common username like 'anonymous' or 'ftp', and authenticated access, where a username and password are required.
- Common FTP attacks include **brute force** and **dictionary attacks**, where automated tools systematically guess weak passwords or use lists of common credentials to gain unauthorized access.  **Man-in-the-Middle (MitM)** attacks allow hackers to intercept unencrypted communications, stealing login credentials and sensitive data transmitted in plaintext. 
###  IMAP (Internet Message Access Protocol)
- **`Default Ports: 143 (IMAP), 993 (IMAPS)`**
- **Internet Message Access Protocol (IMAP)** is a standard email protocol that stores email messages on a mail server and allows the end user to view and manipulate them as though they were stored locally on their device. Unlike POP3, IMAP synchronizes email across multiple devices and allows management of email directly on the server.
1. **Injection and Credential Attacks**: IMAP is susceptible to **IMAP/SMTP injection** when input is not properly sanitized, allowing attackers to execute arbitrary commands on the mail server.  Additionally, because legacy IMAP often relies on **basic authentication**, it faces risks from **brute force** and **credential stuffing** attacks, which can be used to bypass MFA protections enforced by cloud providers. 
2. **Data Interception and Theft**: Without mandatory TLS encryption, **unencrypted communication** allows attackers to intercept sensitive data, including email content and login credentials.  Attackers can also misuse the protocol for **data encoding and theft**, disguising stolen information within email traffic to bypass security mechanisms. 
3. **Malware and Service Disruption**: The protocol serves as a vector for **malware delivery** via malicious attachments or phishing links, leading to ransomware or data breaches.  Furthermore, IMAP servers can be targeted by **Denial of Service (DoS)** attacks, which flood the server with excessive requests to cause service disruption or downtime.
###  SMTP (Simple Mail Transfer Protocol)
- **`Default Ports: 25 (SMTP), 465 (SMTPS), 587 (Submission)`**
- **Simple Mail Transfer Protocol (SMTP)** is an internet standard communication protocol for electronic mail transmission. SMTP is a text-based protocol where one or more recipients of a message are specified, and then the message text is transferred. It operates on a push model, where the sending mail server pushes messages to receiving mail servers. SMTP is crucial for email communication infrastructure and can be exploited for phishing, spam, and information disclosure.
- SMTP servers face a wide range of attacks, primarily **Open Relay Exploits**, **Email Spoofing**, **Brute Force Attacks**, and **Denial of Service (DoS)**.  **Open relay misconfiguration** allows unauthorized third parties to send emails through the server, which spammers abuse to distribute bulk spam or malware, often resulting in the server being blacklisted.  **Email spoofing** exploits the lack of inherent sender verification to forge "From" addresses, enabling phishing campaigns and brand impersonation. 
### Domain Name System (DNS)
- **`Default Port: 53`**
- **DNS (Domain Name System)** functions as the internet's phonebook, converting user-friendly domain names like hackviser.com into numerical IP addresses, enabling swift access to online resources. DNS is a hierarchical and decentralized naming system for computers, services, or any resource connected to the Internet or a private network. It translates human-readable domain names to numerical IP addresses, essential for locating and identifying computer services and devices within network protocols.
1. - **DNS amplification and flood attacks** overwhelm servers with massive traffic volumes, often using spoofed IP addresses to launch Distributed Denial of Service (DDoS) attacks. 
2. **DNS tunneling** allows attackers to bypass firewalls by hiding data within DNS queries to exfiltrate information or establish command-and-control channels. 
3. **Zero-day attacks** exploit previously unknown software vulnerabilities in DNS servers or protocols before patches are available. 
4. **Fast-flux DNS** rapidly swaps IP addresses associated with a domain to evade detection and blacklisting. 
5. **NXDOMAIN attacks** flood servers with requests for non-existent domains to exhaust resources and disrupt legitimate lookups.
### HTTP/HTTPS (Web Server)
- **`Default Ports: 80 (HTTP), 443 (HTTPS), 8080, 8443`**
- **HTTP (Hypertext Transfer Protocol)** and **HTTPS (HTTP Secure)** are the foundation protocols of the World Wide Web. They enable communication between web clients and servers. HTTP operates on port 80 by default, while HTTPS uses SSL/TLS encryption and operates on port 443. Alternative ports like 8080, 8443, and others are commonly used for development, proxies, or secondary web services.
1. **HTTP Flood DDoS**: Overloading servers with high volumes of GET/POST requests using botnets. 
2. **MITM Attacks**: Intercepting or altering traffic, especially on sites not enforcing HTTPS Strict Transport Security (HSTS). 
3. **Injection Flaws**: Including SQLi, XSS, and SSRF via poorly validated inputs. 
4. **Header Manipulation**: Exploiting Host, Origin, or Cookie headers for cache poisoning or session hijacking. 
5. **Protocol Downgrade**: Forcing connections to HTTP instead of HTTPS to enable interception.

### IRC 
- **`Default Port: 6667`**
- **IRC (Internet Relay Chat)**, is a protocol and communication system that allows users to engage in real-time text-based conversations. In this article, we will examine the pentesting techniques for IRC.
1. **Flood Attacks**: These include **Connect floods** (rapid join/quit spam), **Nick floods** (rapid nickname changes), and **Post floods** (repetitive text) designed to overwhelm channels or disconnect users. 
2. **Protocol Exploits**: Attacks like **CTCP floods** exploit client responses to requests, while **DCC floods** initiate numerous file transfer sessions to crash clients or exhaust bandwidth. 
3. **Malware Distribution**: **Trojan horses** disguised as legitimate files can infect users, turning their computers into **botnets** that execute commands from a central server to attack others. 
4. **Network Attacks**: **Nukes** (operating system exploits) and **ICMP floods** target specific OS vulnerabilities or raw internet connections to crash machines or sever IRC connections, often independent of the IRC server itself. 
5. 
6. **Social Engineering**: **User impersonation** allows attackers to pose as trusted users or operators to trick others into downloading malicious files or revealing sensitive information.
### NFS (Network File System)
- **`Default Ports: 2049 (NFS), 111 (RPC)`**
- **Network File System (NFS)** is a distributed file system protocol that allows users to access files over a network in a manner similar to how local storage is accessed. Developed by Sun Microsystems, NFS enables file sharing between Unix/Linux systems. Modern implementations (NFSv4) have improved security, but older versions and misconfigurations can lead to unauthorized access and data exposure.
1. - **Misconfiguration Attacks**: Using wildcards in `/etc/exports` or disabling `root_squash` to allow unauthorized access. 
2. **Authentication Bypass**: Exploiting the lack of strong authentication in older versions to access sensitive files like SSH keys or configuration credentials. 
3. **Data Interception**: Utilizing the absence of encryption in NFSv2/v3 to capture plaintext data via network sniffing. 
4. **Privilege Escalation**: Placing malicious SUID binaries on shares or spoofing UIDs to gain root-level control. 
5. **File System Exploitation**: Bypassing `subtree_check` to access files outside the intended export directory. 
###  NTP (Network Time Protocol)
- **`Default Port: 123 (UDP)`**
- **Network Time Protocol (NTP)** is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. NTP is one of the oldest internet protocols still in use and is critical for maintaining accurate time across networks. Precise time synchronization is essential for security protocols like Kerberos, logging systems, and distributed applications. NTP servers can leak system information and, in some cases, be exploited for amplification attacks.
1.   **Spoofed Kiss-o'-Death (KoD) Attacks**: An attacker can send a single spoofed KoD packet to a vulnerable client, causing it to stop querying time servers for days or years (CVE-2015-7704). 
2. **Priming the Pump**: Attackers can force NTP servers to rate-limit a victim by sending high volumes of spoofed queries, resulting in the server sending valid KoD packets to the victim (CVE-2015-7705). 
3.  **Fragmentation and Reboot Attacks**: Off-path attackers can exploit IPv4 fragmentation or client reboot behaviors to stealthily shift system clocks (CVE-2015-5300), potentially disrupting cryptographic protocols like TLS, Kerberos, and DNSSEC.
### **RSH (Remote Shell)**
-  **`Default Port: 514`**
- **RSH (Remote Shell)**, is a protocol that allows users to execute shell commands on a remote machine. In this article, we will examine the pentesting techniques for RSH under the following categories: Connect, Recon, Enumeration, Attack Vectors, and Post-Exploitation.
1. **IP Spoofing and Sequence Number Guessing**: Since RSH uses source-based authentication, attackers can forge their IP address to bypass login requirements if the target system is vulnerable to TCP sequence number prediction.
2. **Eavesdropping (Man-in-the-Middle)**: All data, including passwords and commands, is transmitted in plain text, allowing network sniffers to intercept sensitive information. 
3.  **Brute Force Attacks**: Tools like **Hydra** can be used to guess weak passwords against RSH services, particularly when strong authentication is not enforced. 
4. **Privilege Escalation**: Once access is gained, attackers often search for **SUID binaries** or exploit misconfigured trust files to escalate privileges to root. 
5. **Reverse Shell Exploits**: Malicious actors can leverage RSH vulnerabilities to establish **reverse shells**, allowing them to execute commands on the target machine and bypass firewalls that filter incoming connections. 
###  VNC (Virtual Network Computing)
- **`Default Ports: 5900-5906`**
- **Virtual Network Computing (VNC)** is a graphical desktop-sharing system that uses the Remote Frame Buffer (RFB) protocol to remotely control another computer. VNC transmits keyboard and mouse events from one computer to another, relaying graphical screen updates back. It's platform-independent and widely used for remote technical support, access to work computers, and server administration.
1. **Brute force and password guessing** on weak or default credentials. 
2.  **Authentication bypass** via known vulnerabilities (e.g., CVE-2006-2369 in RealVNC). 
3. **Man-in-the-middle (MitM)** attacks due to lack of default session encryption. 
4. **Remote code execution** through buffer overflows or uninitialized variable flaws. 
5. **Denial-of-service (DoS)** via crafted inputs causing crashes or resource exhaustion.
### POP3 (Post Office Protocol)
- **`Default Ports: 110 (POP3), 995 (POP3S)`**
- **Post Office Protocol version 3 (POP3)** is an email protocol used to retrieve emails from a remote server to a local client. Unlike IMAP, POP3 typically downloads emails to the client and deletes them from the server (though this can be configured). POP3 is simpler than IMAP but less feature-rich, primarily designed for offline email access.
1. **Unencrypted Data Interception:** By default, POP3 transmits usernames, passwords, and email content in plaintext, allowing attackers on the same network to intercept sensitive data using packet sniffers. 
2. **Brute-Force and Dictionary Attacks:** Many POP3 servers do not implement account lockout policies or log failed attempts, making them easy targets for automated tools like Hydra or Medusa to guess weak passwords.
3. **Process Manipulation and Buffer Overflows:** Vulnerable POP3 server implementations (such as older versions of Qualcomm QPOP) may contain buffer overflow flaws in commands like `LIST`, `RETR`, or `DELE`, allowing authenticated or unauthenticated users to execute arbitrary code. 
4. **Credential Harvesting via Phishing:** Attackers often use spear-phishing to steal user credentials, which are then leveraged to access POP3 servers and retrieve emails or internal data. 
5. **Denial of Service (DoS):** Specific vulnerabilities, such as buffer overflows triggered by long username or password strings, can cause POP3 services to crash or become unavailable.
### **Remote Procedure Call (RPC)**
- **`Default Port: 111 
- **Remote Procedure Call (RPC)** is a request-response protocol that allows a program to cause a procedure to execute on a remote system, commonly used for network-based services like SMB, DCOM, and Active Directory replication.  By default, the **RPC Endpoint Mapper** listens on **TCP and UDP port 135**, which clients contact first to determine the specific dynamic port assigned to a service.
1. - **Buffer Overflow Attacks**: Attackers exploit vulnerabilities in RPC servers to overwrite memory buffers, allowing them to execute arbitrary code. 
2. **Man-in-the-Middle (MitM) Attacks**: Malicious actors intercept and modify RPC messages during transmission to steal data or inject malicious commands. 
3. **Reflection Attacks**: Attackers send malicious RPC requests to a server, causing the server to send responses to a victim, often bypassing security checks. 
4. **Null Session Attacks**: Vulnerable servers allow unauthenticated connections, enabling attackers to retrieve sensitive information like user lists or network shares. 
5. **Denial of Service (DoS)**: Overloading the RPC server with a high volume of requests to crash the service or disrupt availability. 
6. **Authentication Bypass**: Exploiting flaws to bypass authentication mechanisms and gain unauthorized access to RPC services.
7. **Code Injection**: Injecting malicious code into RPC requests to execute commands on the server. 
8. **Directory Traversal**: Crafting requests to access files outside the intended directory, exposing sensitive system files.
### MSSQL (Microsoft SQL Server)
- **`Default Port: 1433`**
- **Microsoft SQL Server (MSSQL)** is a relational database management system developed by Microsoft. It's widely used in enterprise environments and integrates tightly with Windows infrastructure. MSSQL offers powerful features including stored procedures, xp_cmdshell for command execution, and extensive Windows authentication integration.
1.  **SQL Injection**: Includes in-band, blind (inferential), and out-of-band methods to execute arbitrary code or extract data.  
2. **Privilege Escalation**: Techniques involve exploiting `db_ddladmin` roles, modifying stored procedures, or using `EXECUTE AS` to impersonate `sysadmin`. 
3. **Persistence**: Achieved through startup procedures, scheduled SQL Agent jobs, or unauthorized DLL loads. 
4. **Lateral Movement**: Utilizing linked servers or UNC paths to capture NTLM hashes and move across network tiers. 
5. **Ransomware**: Direct attacks on exposed servers to encrypt data, often preceded by data theft.
### Docker API
- **`Default Ports: 2375 (HTTP), 2376 (HTTPS)`**
- **Docker** is a containerization platform that allows developers to package applications and their dependencies into isolated containers. The Docker API provides remote management capabilities, enabling administration of Docker hosts over the network. When exposed without proper authentication, it can lead to complete host compromise.
1. - **Container Escape**: Attackers exploit vulnerabilities (e.g., CVE-2019-5736, CVE-2020-14386) to break out of containers and gain **root access on the host**, potentially compromising all other containers. 
2. **Lateral Movement**: Poor network isolation allows attackers to move between containers via **ARP spoofing**, **sniffing**, or **DDoS**, especially when inter-container communication is unrestricted.
3. **Privilege Escalation**: Running containers with excessive privileges (e.g., `--privileged` flag or root user) enables attackers to escalate privileges and access sensitive host resources. 
4. **Supply Chain Attacks**: Malicious or tampered images (e.g., typosquatting, poisoned base images) can introduce backdoors, crypto miners, or other malware into the environment. 
5. **Resource Starvation**: Attackers can exhaust CPU, memory, or disk I/O by running resource-intensive processes, leading to **Denial-of-Service (DoS)** conditions.
6. **Docker API Exploits**: Exposed or misconfigured Docker APIs (e.g., CVE-2024-41110) allow unauthorized command execution and container manipulation. 
7. **Man-in-the-Middle (MITM)**: Unencrypted communication between containers can be intercepted or modified, enabling data theft or tampering.
8. **Orchestration Attacks**: Compromised orchestration tools (e.g., Kubernetes, Docker Swarm) can lead to cluster-wide breaches via default configurations or weak RBAC policies.
### MySQL
- **`Default Port: 3306`**
- **MySQL** is an open source relational database management system (RDBMS) widely used worldwide. Databases are used to store and manage interrelated data. MySQL is a preferred solution in many areas such as web-based applications, data storage, e-commerce, and log records. SQL (Structured Query Language) is the language MySQL uses to communicate with the database.
- **Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attacks** can overwhelm the server with fake queries or crafted SELECT statements (e.g., using `UpdateXML()`), causing the database to crash or become unavailable.  Additionally, **Race Condition (TOCTTOU) vulnerabilities** exist in older versions, enabling attackers to escalate privileges or execute arbitrary code through improper synchronization of concurrent operations.
### 
