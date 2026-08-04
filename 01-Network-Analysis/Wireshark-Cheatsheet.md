# SOC Analyst Wireshark Display Filter Cheat Sheet 
**Date:** June 6, 2026  
**Focus:** Packet Dissection Syntax, Threat Isolation Filters, and Traffic Triage Logic

This reference guide maps out 15 critical Wireshark display filters used daily by Tier 1 SOC analysts to rapidly isolate anomalous behaviors, malicious data streams, and network threats.

---

## 1. Host Tracking & Network Reconnaissance

### 01. Filter by Specific Host IP
* **Filter:** `ip.addr == 10.0.0.5`
* **Analyst Logic:** Pulls all inbound and outbound traffic involving a suspected target or compromised host endpoint.

### 02. Isolate Traffic Flow Between Specific Targets
* **Filter:** `ip.src == 192.168.1.50 && ip.dst == 10.0.0.22`
* **Analyst Logic:** Restricts the view strictly to packets traveling from a specific origin machine to a target asset to trace lateral movement.

### 03. Track Active Port Scans (TCP SYN Floods)
* **Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0`
* **Analyst Logic:** Displays connection requests trying to open a port without finalizing the handshake. High volumes from a single source indicate an active adversarial scan.

---

## 2. Web Application & Payload Triage (HTTP/S)

### 04. Audit Inbound Web Data Submissions
* **Filter:** `http.request.method == "POST"`
* **Analyst Logic:** Isolates data entry transfers, such as unencrypted login attempts, form uploads, or web shell interaction traffic.

### 05. Hunt for Malicious User-Agent Submissions
* **Filter:** `http.user_agent contains "sqlmap" || http.user_agent contains "Nmap"`
* **Analyst Logic:** Directly surfaces automated exploitation scripts or vulnerability scanning tools attempting to probe corporate web application layers.

### 06. Monitor Outbound Executable File Transfers
* **Filter:** `http.content_type contains "application/x-msdownload" || http.request.uri contains ".exe"`
* **Analyst Logic:** Traces cleartext download streams of executable binary payloads entering the internal localized domain network.

---

## 3. Administrative Interface Auditing

### 07. Isolate Internal Remote Desktop Sessions
* **Filter:** `tcp.port == 3389`
* **Analyst Logic:** Surfaces remote desktop control loops. High numbers of connection resets on this port point directly to automated external brute forcing.

### 08. Expose Cleartext Administrative Sessions
* **Filter:** `tcp.port == 21 || tcp.port == 23`
* **Analyst Logic:** Instantly exposes insecure protocol use (FTP/Telnet) where usernames and passwords transit the local network entirely in plain cleartext.

### 09. Triage Domain Internal File Transfers
* **Filter:** `smb || smb2`
* **Analyst Logic:** Inspects internal file-sharing streams to track unauthorized connections to administrative hidden network directories (`C$`, `ADMIN$`).

---

## 4. Advanced Threat & Anomaly Filters

### 10. Detect Outbound DNS Tunneling Attempts
* **Filter:** `dns.qry.name.len > 30 && !dns.flags.response`
* **Analyst Logic:** Forces the viewer to look at uniquely long, high-character domain query names used to encode stolen data or exfiltrate strings without establishing direct connections.

### 11. Isolate Abnormally Large Packet Payloads
* **Filter:** `frame.len > 1400`
* **Analyst Logic:** Identifies massive individual data packets traveling across network wires, often matching continuous data staging or active data exfiltration phases.

### 12. Locate Broken TCP Handshakes (Connection Resets)
* **Filter:** `tcp.flags.reset == 1`
* **Analyst Logic:** Pinpoints broken network paths or immediate terminal shutdowns caused by automated tools hitting closed network endpoints.

### 13. Audit HTTP Redirection Actions
* **Filter:** `http.response.code >= 300 && http.response.code <= 399`
* **Analyst Logic:** Surfaces force-routing behaviors where a user visits a trusted link but is redirected to an unknown external resource.

### 14. Expose Cleartext Basic Authentication Transfers
* **Filter:** `http.authbasic`
* **Analyst Logic:** Surfacings plaintext web credentials transmitted without encryption protections.

### 15. Track Active Non-DNS UDP Data Blasts
* **Filter:** `udp && !dns`
* **Analyst Logic:** Strips out typical domain name resolution queries to reveal non-standard, high-velocity UDP traffic loops, indicating possible DoS actions or raw data tunnels.

---
## 5. Practical Verification & Triage Exercise

### ⚙️ Step-by-Step Packet Follow Methodology
When conducting network traffic forensics in a production triage timeline, follow this 3-step sequence:
1. **Apply Protocol Stream Isolation:** Use `http` or `tcp` display filters to isolate initial cleartext sessions. Look for unexpected domain lookups, abnormal `.zip` or `.exe` request downloads, or anomalous encoded strings.
2. **Follow Malicious Streams:** Right-click on a suspicious packet row in the top pane, navigate to **Follow** -> **TCP Stream**. Wireshark stitches the asymmetric transaction sequence together (`Red text` indicates client-to-server data; `Blue text` indicates server-to-client responses), allowing you to review raw scripts, file names, or terminal executions.
3. **Extract Dropped Artifacts:** To pull out a malicious payload or file for hash extraction, go to **File** -> **Export Objects** -> **HTTP**. This allows you to reconstruct and save the binary locally to evaluate its cryptographic hash signature against threat intelligence databases.