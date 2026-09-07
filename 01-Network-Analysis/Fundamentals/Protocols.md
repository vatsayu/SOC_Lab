# Corporate Network Protocols & Adversary Attack Vectors  
**Date:** June 5, 2026  
**Focus:** Foundational Port Security, Traffic Characteristics, and SOC Triage Indicators

## 1. Enterprise Protocol Security Matrix

| Protocol Name | Target Port | Transport Layer | Core Functional Purpose | Primary Adversary Attack Vector |
| :--- | :--- | :--- | :--- | :--- |
| **DNS** | 53 | UDP / TCP | Translates domain names to IP strings | DNS Tunneling (Data Exfiltration), Cache Poisoning |
| **HTTP** | 80 | TCP | Cleartext web communication layer | Credential Sniffing, Web Application Payloads |
| **HTTPS** | 443 | TCP | Encrypted web session data via TLS | Command & Control (C2) traffic concealment |
| **SMB** | 445 | TCP | Local Windows resource/file sharing | Remote Code Execution (EternalBlue), Lateral Movement |
| **RDP** | 3389 | TCP | Graphical console remote administration | External Brute-Forcing, Credential Stuffing |

---

## 2. Technical Triage & Detection Methodologies

### A. Outbound DNS Tunneling Analysis
* **Adversary Mechanism:** Threat actors chunk private data or C2 assembly instructions into small character strings, appending them as unique subdomains to an external domain infrastructure they control (e.g., `encoded_password_payload.attackerdomain.com`).
* **SOC Analyst Ingestion Focus:** Look for high-volume spikes of highly randomized, uniquely long subdomain lookup requests directed toward an unknown, newly registered external domain zone. Look for high Shannon entropy values in domain queries.

### B. Enterprise SMB Lateral Movement Analysis
* **Adversary Mechanism:** After compromising an initial endpoint, attackers scan port 445 internally, executing network exploits (e.g., EternalBlue) or leveraging stolen administrative tokens to compromise neighboring hosts.
* **SOC Analyst Ingestion Focus:** Monitor host monitoring agents (or SIEM alerts) for abnormal administrative hidden share connections (such as `C$` or `ADMIN$`) originating from unauthorized, standard user workstations.

### C. RDP Authentication Abuse Analysis
* **Adversary Mechanism:** Threat actors leverage credential dumps or automated brute-force scripts against open Port 3389 instances to establish an interactive GUI backdoor into infrastructure servers.
* **SOC Analyst Ingestion Focus:** Audit host event logs for high-frequency bursts of Event ID 4625 (Failed Logon) immediately preceding an Event ID 4624 (Successful Logon) utilizing Logon Type 10 (Remote Desktop).

---
## 3. Training Resources & Progress Verification
* **Source Material:** Professor Messer CompTIA Security+ / CySA+ Network Security Architecture Paths