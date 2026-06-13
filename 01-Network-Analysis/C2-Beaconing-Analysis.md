# Advanced Threat Hunting: C2 Beaconing & User-Agent Anomalies
**Author:** Vatsayu  
**Date:** June 9, 2026  
**Focus:** Isolating Command and Control (C2) Traffic, Jitter Mechanics, and HTTP Header Analysis

This log details the methodology for hunting advanced persistent threats (APTs) that utilize encrypted HTTP/S channels to establish Command and Control (C2) beaconing, as well as the triage of malicious User-Agent strings.

---

## 1. Malicious User-Agent Triage

Threat actors often utilize automated scripts, Python libraries, or default command-line tools to execute web attacks or download secondary payloads. If the adversary fails to spoof a legitimate browser User-Agent, the traffic is highly visible.

### Analyst Hunting Strategy (Wireshark)
* **Filter:** `http.user_agent`
* **Execution:** Add the User-Agent field as a visual column in the Wireshark Packet List pane. Sort alphabetically to instantly bubble up anomalous tools.
* **Red Flag Indicators:** * `curl/7.X.X` or `Wget/1.X.X` (Command-line downloaders on standard workstations)
  * `python-requests/2.X` or `Go-http-client` (Automated scripting libraries)
  * `sqlmap/1.X` or `Nmap Scripting Engine` (Active vulnerability exploitation tools)
  * A completely missing/blank User-Agent header.

---

## 2. Command and Control (C2) Beaconing Mechanics

When an endpoint is compromised, the payload establishes a persistent outbound connection to an attacker-controlled server to request instructions. 

### The Rhythmic "Heartbeat"
Because the malware must constantly check in, it generates highly periodic network traffic. For example, a beacon set to a 60-second sleep interval will generate an outbound HTTP GET request to the exact same external IP address exactly every 60 seconds.

### The Adversary Defense: "Jitter"
To evade SOC analysts and automated anomaly-detection tools looking for perfect mathematical rhythms, adversaries apply **Jitter** (randomized variance).
* **Formula:** `Beacon Interval +/- Jitter Percentage`
* **Example:** A 60-second beacon with a 20% Jitter will randomize its check-ins between 48 seconds and 72 seconds.

### Analyst Hunting Strategy (Wireshark / SIEM)
1. **Filter out known noise:** Remove standard corporate telemetry (Microsoft updates, Google telemetry) from the capture.
2. **Endpoint Connection Sorting:** Aggregate outbound connections by Destination IP.
3. **Delta Time Analysis:** Calculate the time difference (Delta) between connections to the same IP. A tight, repeating cluster of Delta times (e.g., connections happening roughly every 45-55 seconds continuously over a 24-hour period) indicates an active C2 beacon.

---
## 3. Verification & Tracking
* **Training Matrix:** Advanced Network Forensics & PCAP Triage
* **Status:** Triage mechanics mapped and verified.
