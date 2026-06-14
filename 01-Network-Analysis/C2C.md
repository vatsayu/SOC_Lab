# 🛡️ Hands-On Lab: Malicious User-Agent Triage & Stealth C2 Beaconing Analysis

A practical exploration of network threat hunting, signature verification, and behavioral analysis using Wireshark and PowerShell. This project simulates real-world adversarial tactics to demonstrate how Security Operations Center (SOC) analysts identify compromise through traffic patterns.

---

## 📌 Project Overview
Modern threat actors try to blend in with normal web activity to bypass firewalls and intrusion detection systems. This lab walks through two primary methodologies for hunting network-based threats:
1. **Signature-Based Triage:** Spotting automated scripts and known exploitation frameworks via non-standard `User-Agent` strings.
2. **Behavioral-Based Analysis:** Spotting advanced Command and Control (C2) implants that try to hide their identity but reveal themselves through automated timing loops (**Jittered Beacons**).

---

## 🛠️ Phase 1: Environment Setup & Tool Verification

### Step 1: Initialize Traffic Monitoring
1. Launch **Wireshark** with administrator privileges.
2. Identify your active network interface (look for the live, spiking line graph next to your active **Wi-Fi** or **Ethernet** adapter).
3. Double-click the active adapter to initiate a live packet capture.

### Step 2: Configure Global Time Constraints
To track localized timing intervals precisely instead of standard calendar clock time:
1. Navigate to the top menu and select **View** ➡️ **Time Display Format**.
2. Select **Seconds Since Previously Displayed Packet**. 

> 💡 **Why?** This shifts Wireshark's focus to calculate the exact *Delta Time* (time elapsed) between consecutive requests, which is critical for behavioral analysis.

---

## 🚀 Phase 2: Generating Exploitation & Automation Signatures

### Step 3: Execute Anomalous User-Agent Simulation
Attackers frequently utilize default command-line utilities or automated scripts that leave loud, distinctive signatures in HTTP headers. 

Open a native **PowerShell** window and execute the following block to generate suspicious telemetry:

# 1. Simulating a basic Python web scraper / automated downloader
Invoke-WebRequest -Uri "[http://httpbin.org/get?source=python-script](http://httpbin.org/get?source=python-script)" -UserAgent "python-requests/2.31.0" -UseBasicParsing

# 2. Simulating a default command-line utility pulling down files
Invoke-WebRequest -Uri "[http://httpbin.org/get?source=curl-tool](http://httpbin.org/get?source=curl-tool)" -UserAgent "curl/7.88.1" -UseBasicParsing

# 3. Simulating an active vulnerability exploitation scan
Invoke-WebRequest -Uri "[http://httpbin.org/get?source=vulnerability-scan](http://httpbin.org/get?source=vulnerability-scan)" -UserAgent "sqlmap/1.7.5#stable" -UseBasicParsing


## 🕵️ Phase 3: Simulating a Stealth Command & Control (C2) Beacon

Step 4: Launch the Jittered C2 Implant
To bypass basic signature detection, advanced malware masquerades as a legitimate browser string (Mozilla/5.0) and introduces randomized variance (Jitter) to its check-in frequency.

Copy and paste this loop into your PowerShell terminal and let it execute for 1 to 2 minutes:

$BaseInterval = 10
$JitterPercent = 0.20

while($true) {
    # Calculate Jitter bounds (adds/subtracts random variance between 8 and 12 seconds)
    $MaxVariance = $BaseInterval * $JitterPercent
    $RandomVariance = Get-Random -Minimum (-$MaxVariance) -Maximum ($MaxVariance + 1)
    $ActualSleep = $BaseInterval + $RandomVariance
    
    Write-Host "Sending Jittered Beacon. Sleeping for $ActualSleep seconds..."
    Invoke-WebRequest -Uri "[http://httpbin.org/get?type=beacon](http://httpbin.org/get?type=beacon)" -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -UseBasicParsing
    
    Start-Sleep -Seconds $ActualSleep
}
Press Ctrl + C inside the PowerShell terminal after a couple of minutes to safely terminate the loop.

## 🔍 Phase 4: SOC Analyst Triage & Behavioral Analysis

Step 5: Stop and Isolate the Capture
Return to Wireshark and click the Red Square (Stop Capture) button in the top left.

In the display filter bar, type http and hit Enter to remove unrelated background network noise.

Step 6: Customize the Wireshark Interface for Signature Hunting
Expand any captured HTTP packet in the Packet Details (middle) pane.

Expand the Hypertext Transfer Protocol dropdown and locate the line item: User-Agent: ....

Right-click on the User-Agent line and select Apply as Column.

Left-click your new User-Agent column header to sort everything alphabetically. This instantly bubbles up the curl, python-requests, and sqlmap signatures out of the background noise.

Step 7: Perform Delta-Time Behavioral Analysis (Catching the Beacon)
Because the second script used a normal browser string, signature sorting won't uncover it. Instead, we hunt by behavioral trends over time:

Clear your previous filter and apply: Plaintext
http.request.uri contains "type=beacon"
Examine your Time column on the far left.

Observe the Delta variations: notice how despite the randomized jitter, the requests are clustered strictly between ~8.0 and ~13.0 seconds.

⚠️ Analyst Conclusion: No human browses a website with a pattern this tight and continuous. This periodic clustering flags an automated script signature—confirming an active C2 beacon.

## 🔒 Phase 5: Sanitization & Export

Step 8: Safely Export the PCAP for Documentation
To share this lab in a public portfolio without exposing internal home network infrastructure or personal tokens leaked in background traffic:

Keep your target filter applied: http.request.uri contains "type=beacon"

Navigate to File ➡️ Export Specified Packets...

Ensure the packet range radio button is set to Filtered or Selected packets only.

Save the file as c2_simulation_filtered.pcapng to complete your repository deployment kit.
