# Open-Source SOC Analyst Portfolio
Welcome! This repository tracks my intensive, 30-day technical validation across Network Analysis, Endpoint Forensics, SIEM Log Auditing, and Incident Response. 

My training relies entirely on enterprise-grade free resources including **Professor Messer (Security+/CySA+)**, **LetsDefend**, and **Blue Team Labs Online (BTLO)**.

## 🛠️ Specialized Technical Focus
* **Network & Traffic Forensics:** Packet dissection and anomaly tracking using **Wireshark**.
* **Security Information & Event Management (SIEM):** Mass log queries using **Splunk (SPL)**.
* **Operating System Security:** Windows Event/Sysmon logging and Linux core system monitoring.

---

## 🏗️ Core Laboratory Architecture (4 Production Projects)
To demonstrate structural hands-on competency to hiring managers, my local virtual environment mirrors enterprise perimeter security architectures. Each project is documented with explicit deployment phases, alert thresholds, and triage logs.

### 🛡️ Project 1: SafeLine Web Application Firewall (WAF) Lab
* **Objective:** Deploy a Web Application Firewall to actively shield web traffic interfaces and mitigate application-layer exploits.
* **Environment Components:** Ubuntu 22.04 LTS VM, Docker, Docker-Compose, DVWA (Damn Vulnerable Web Application), SafeLine WAF.
* **Practical Tasks:** - Simulated a malicious attacker executing an unauthenticated SQL Injection (`1' OR '1'='1`) attack payload against standard application input fields.
  - Deployed SafeLine WAF reverse-proxy configurations over Port 80 to catch malicious patterns and return explicit red-flag access violations.
  - Engineered Anti-Bot Rate Limiting infrastructure restricting client traffic down to 20 requests per second to counter automated Denial of Service (DoS) floods.
* **Documentation Links:** [Setup Log & Logs Analysis](./01-Network-Analysis/Project-1-WAF-SafeLine.md)

### 📊 Project 2: Wazuh SIEM Security Intelligence Lab
* **Objective:** Centralize telemetry and monitor active file-integrity states via an enterprise-grade SIEM platform.
* **Environment Components:** Ubuntu 22.04 (Wazuh Manager node Appliance), Windows 10/11 Endpoint (Wazuh Agent), Oracle VirtualBox Host-Only networking.
* **Practical Tasks:**
  - Automated deployment of the centralized security monitoring console via the pre-built Wazuh Appliance OVA framework.
  - Installed and authenticated local monitoring agents on guest endpoints to feed critical operating system event streams into the SIEM dashboard.
  - Configured custom File Integrity Monitoring (`<syscheck>`) criteria inside the agent `ossec.conf` file to dynamically trigger alerts on unauthorized file alterations across sensitive file paths.
* **Documentation Links:** [SIEM Dashboard Configurations](./03-SIEM-Log-Analysis/Project-2-Wazuh-SIEM.md)

### 🧱 Project 3: pfSense Network Firewall & Traffic Rules Engine
* **Objective:** Configure a stateful firewall router to isolate internal localized boundaries from unauthenticated networks.
* **Environment Components:** pfSense Firewall OS, Ubuntu Client Node (Protected Local Area Network Side), Kali Linux Endpoint (Simulated WAN External Space).
* **Practical Tasks:**
  - Architected dual virtual switch network interfaces inside VirtualBox isolating the protected LAN subnet from the exposed WAN subnet zone.
  - Provisioned strict Top-to-Bottom processing rules allowing inbound Layer 7 HTTP connections (Port 80 TCP) while matching and blocking raw ICMP Echo requests (Pings).
  - Implemented advanced rate-limiting control options inside stateful firewall structures to flag and restrict high-velocity brute-force floods.
* **Documentation Links:** [Firewall Rule Blueprints](./01-Network-Analysis/Project-3-pfSense-Firewall.md)

### 🤖 Project 4: AI-Powered Autonomous SOC Analyst Agent
* **Objective:** Develop an automated initial pipeline using Large Language Models to evaluate log data against active playbooks.
* **Environment Components:** Ubuntu Server, Airia AI API Framework, Python 3 Development Tools, Kali Linux Network Ingestion.
* **Practical Tasks:**
  - Coded a custom Python automation script natively connecting endpoint log data streams to remote text-generation engines using standard API calls.
  - Injected an operational SOC Playbook into the system prompt framework to train the AI to parse raw text streams into discrete structural variables.
  - Tested classification accuracy against authentication logs to successfully isolate SSH Brute-Force sequences, quantify severity levels, and map tactical response plans.
* **Documentation Links:** [Python Scripts & AI Output Logs](./02-Endpoint-Analysis/Project-4-AI-SOC-Agent.md)

---

## 📅 30-Day Practical Project Roadmap

### 🌐 Phase 1: Network Traffic Analysis (Wireshark Focus)
- [ ] **Day 1:** [Network Security Protocols & Vulnerabilities](./01-Network-Analysis/Network-Protocols.md)
- [ ] **Day 2:** [SOC Analyst Wireshark Filter Cheat Sheet](./01-Network-Analysis/Wireshark-Cheatsheet.md)
- [ ] **Day 3:** [Network Ingestion & Data Flow Fundamentals](./01-Network-Analysis/Network-Fundamentals.md)
- [ ] **Day 4:** [PCAP Investigation: Cleartext Credential Triage](./01-Network-Analysis/PCAP-Challenge-1.md)
- [ ] **Day 5:** [IDS/IPS Architecture & Alert Verification](./01-Network-Analysis/IDS-Mechanics.md)
- [ ] **Day 6:** [Advanced Traffic Analysis: C2 Beaconing Triage](./01-Network-Analysis/C2-Beaconing-Analysis.md)
- [ ] **Day 7:** Phase 1 Quality Audit & Repository Synchronization

### 🖥️ Phase 2: SIEM Foundations & Log Ingestion (Splunk Focus)
- [ ] **Day 8:** [SIEM Architecture & Splunk Component Layout](./03-SIEM-Log-Analysis/Splunk-Basics.md)
- [ ] **Day 9:** [Live SPL Syntax Production Cheat Sheet](./03-SIEM-Log-Analysis/SPL-Syntax-Guide.md)
- [ ] **Day 10:** [Windows Event Log Auditing & Reference](./02-Endpoint-Analysis/Event-ID-Reference.md)
- [ ] **Day 11:** [Sysmon Process Mapping & Thread Queries](./02-Endpoint-Analysis/Sysmon-Hunting.md)
- [ ] **Day 12:** [Hands-on Lab: Windows Security Triage via Sysmon](./02-Endpoint-Analysis/Sysmon-Lab.md)
- [ ] **Day 13:** [Linux Forensics: CLI Log Parsing vs. Splunk Auditing](./02-Endpoint-Analysis/Linux-Forensics.md)
- [ ] **Day 14:** Phase 2 Quality Audit & Repository Synchronization

### 📧 Phase 3: Phishing & Web Application Attack Triage
- [ ] **Day 15:** [Email Security Infrastructure: Header Dissection](./04-Incident-Reports/Email-Header-Analysis.md)
- [ ] **Day 16:** [Operational Sandbox Ingestion Workflow Guide](./04-Incident-Reports/Phishing-Triage-Workflow.md)
- [ ] **Day 17:** [Phishing Incident Report: Raw .eml Analysis](./04-Incident-Reports/Phishing-Case-01.md)
- [ ] **Day 18:** [Web Server Access Logs Architecture Breakdown](./04-Incident-Reports/Web-Log-Anatomy.md)
- [ ] **Day 19:** [Advanced SPL Injection Detection Engineering](./03-SIEM-Log-Analysis/Web-Attack-Hunting.md)
- [ ] **Day 20:** [Web Application Attack Incident Report](./04-Incident-Reports/Web-Attack-Case-01.md)
- [ ] **Day 21:** Phase 3 Quality Audit & Repository Synchronization

### 🚨 Phase 4: Production Workflows & Live Incident Simulations
- [ ] **Day 22:** [Mapping Incidents to Cyber Kill Chain & MITRE ATT&CK Frameworks](./04-Incident-Reports/Threat-Framework-Mapping.md)
- [ ] **Day 23:** [Threat Hunting Guide: 5 Production-Ready SPL Persistence Queries](./03-SIEM-Log-Analysis/Threat-Hunting-SPL.md)
- [ ] **Day 24-27:** Live SOC Simulator Alerts (LetsDefend Tier 1 Analyst Cases)
  - [ ] [Incident 01 Blue Team Case Wrap-up](./04-Incident-Reports/Simulator-Alert-01.md)
  - [ ] [Incident 02 Blue Team Case Wrap-up](./04-Incident-Reports/Simulator-Alert-02.md)
  - [ ] [Incident 03 Blue Team Case Wrap-up](./04-Incident-Reports/Simulator-Alert-03.md)
  - [ ] [Incident 04 Blue Team Case Wrap-up](./04-Incident-Reports/Simulator-Alert-04.md)
- [ ] **Day 28-29:** Complete Repository Clean-up & Navigation Finalization
- [ ] **Day 30:** Resume Translation & Portfolio Launch Metrics
