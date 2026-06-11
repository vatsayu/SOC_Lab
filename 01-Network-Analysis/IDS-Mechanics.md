# Intrusion Detection Systems (IDS) & Alert Verification Mechanics
**Author:** Vatsayu  
**Date:** June 8, 2026  
**Focus:** Signature vs. Anomaly Detection, Snort Rule Anatomy, and PCAP Verification

This log details the operational mechanics of enterprise network security sensors (IDS/IPS) and maps automated detection logic directly to manual Wireshark packet analysis workflows.

---

## 1. Detection Engine Methodologies

To secure enterprise perimeters, sensors utilize two primary detection engines:

### Signature-Based Detection
* **Mechanism:** Compares network packet payloads and headers against a database of known threat indicators (hashes, specific byte sequences, or malicious domains).
* **Advantage:** Extremely fast with very low false-positive rates.
* **Blind Spot:** Completely blind to Zero-Day attacks or newly compiled, unindexed malware.

### Anomaly-Based (Heuristic) Detection
* **Mechanism:** Utilizes machine learning to establish a baseline of standard network behavior. Alerts trigger when traffic deviates from this baseline (e.g., unusual port usage or massive data exfiltration spikes).
* **Advantage:** Capable of catching Zero-Days and insider threats.
* **Blind Spot:** Prone to high false-positive rates during standard business network changes or updates.

---

## 2. Snort Rule Anatomy vs. Wireshark Verification

When an IDS like Snort or Suricata generates an alert, a Tier 1 Analyst must pull the associated PCAP and verify it manually in Wireshark to declare it a True Positive or False Positive. 

### Scenario: SQL Injection Attempt
A Snort sensor triggers an alert for an attempted SQL Injection against a corporate web server. 

**The Raw Snort IDS Rule:**
`alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS 80 (msg:"SQL Injection Attempt Detected"; content:"UNION SELECT"; sid:100055; rev:1;)`

**Rule Breakdown:**
* `alert tcp`: The sensor is watching TCP traffic.
* `$EXTERNAL_NET any`: Traffic originating from any external IP and port.
* `-> $HTTP_SERVERS 80`: Traffic directed toward internal web servers on port 80.
* `content:"UNION SELECT"`: The exact malicious signature payload the engine is looking for.

### Analyst Verification Workflow
To verify this alert, the analyst downloads the PCAP surrounding the timestamp of the alert and applies the following manual display filter in Wireshark:

**Wireshark Translation Filter:**
`tcp.port == 80 && http contains "UNION SELECT"`

If the resulting packet stream shows a successful HTTP `200 OK` response with sensitive database information attached, the analyst escalates the alert as a **Critical True Positive**. If the server responded with an HTTP `403 Forbidden` or `404 Not Found`, the attack failed, and the analyst logs it as a blocked perimeter attempt.

---
## 3. Verification & Tracking
* **Source Material:** Professor Messer Network Appliances & Intrusion Prevention
* **Status:** Mechanics mapped and verified.
