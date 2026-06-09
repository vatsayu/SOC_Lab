# Network Fundamentals Defense Log
**Platform ID:** [Xer0rooT]  
**Date:** June 7, 2026  
**Focus:** Network Topologies, Device Boundaries, OSI Sub-System Dissection, and NAT Mechanics

This log documents the completion of the foundational Network Fundamentals training tier on LetsDefend, translating foundational structural networking concepts into active SOC defense logic.

---

## 1. Boundary Controls & Device Triage Architecture

During live incident triage, internal communication pipelines rely on precise boundaries established by three primary infrastructure layers:

1. **Layer 2 Switches (Data Link):** Processes incoming frames via localized MAC addresses. In an incident scenario, switches define the broadcast domain boundary; an attacker leveraging ARP Poisoning manipulate this layer to redirect traffic.
2. **Layer 3 Routers (Network):** Handles logical packet routing via IPv4/IPv6 schemas. Routers dictate cross-subnet traffic rules and act as the first line of path segmentation.
3. **Firewalls (Stateful Inspection):** Enforces strict Access Control Lists (ACLs). It dynamically analyzes the state of network interactions to drop unauthorized connection requests before internal nodes process them.

---

## 2. The Defensive OSI Layer Reference Matrix

As a SOC Analyst, every incoming security alert maps directly to a layer within the OSI model. Isolating the active layer allows for rapid defensive scoping:

| OSI Layer | Name | Monitored Data Units | Active Attacks | Detection Strategy / Tooling |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 7** | Application | Data (HTTP, DNS, FTP) | SQLi, XSS, Phishing | WAF Logs, HTTP Status Audits |
| **Layer 4** | Transport | Segments (TCP) / Datagrams (UDP) | Port Scanning, SYN Flood | Wireshark Handshake Flags |
| **Layer 3** | Network | Packets (IP Addresses) | IP Spoofing, ICMP Tunnels | Router ACLs, SIEM IP Geolocation |
| **Layer 2** | Data Link | Frames (MAC Addresses) | ARP Spoofing, MAC Flooding | Static ARP Tables, Switch Port Security |

---

## 3. Network Address Translation (NAT) Threat Hunting Mechanics

### The Core Challenge for Analysts
Internal enterprise networks utilize private RFC 1918 address fields (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) that cannot route across the public internet. To communicate externally, a router modifies packet headers via **NAT**, replacing the private source IP with the organization's public-facing egress IP.

### The Defensive Hunting Strategy
When monitoring external threat intelligence feeds, an alert might flag your company’s public IP address executing a malicious connection to a known malicious command-and-control (C2) server. 
* To locate the compromised machine, a SOC analyst cannot rely on public IP logs alone. 
* The analyst must cross-reference the exact timestamp and source port from the external firewall logs with internal **NAT Translation Tables** or **DHCP lease history** to reverse-map the connection back to the exact internal private IP address of the infected endpoint.

---
## 4. Verification & Certification Progress Tracking
* **Course Completed:** LetsDefend - Network Fundamentals Course
* **Status:** Operational Baseline Verified
* **Next Milestone:** Day 4 — SOC Fundamentals & SIEM Engineering Architecture Overview
