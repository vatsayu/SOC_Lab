# Day 12: Windows Security Triage via Sysmon

## Objective
To perform a hands-on security triage of Windows Event Logs (specifically Sysmon) to identify potentially malicious process activity, credential dumping, and network beaconing.

## Lab Workflow
1. **Data Ingestion:** Ensure Sysmon logs are ingested into Splunk and assigned the correct `sourcetype` (`XmlWinEventLog:Microsoft-Windows-Sysmon/Operational`).
2. **Analysis Tasks:**
   - **Parent/Child Relationship Check:** Investigating suspicious process spawning.
   - **Credential Dumping Detection:** Searching for unauthorized access to `lsass.exe`.
   - **Network Beaconing Analysis:** Identifying non-standard processes initiating network connections.

## Investigation Queries

### 1. Identifying Parent/Child Anomalies
* **Purpose:** Detect office applications (e.g., Word) spawning shells (PowerShell/CMD).
* **SPL Query:**
    ```splunk
    index=main sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 
    | stats count by ParentImage, Image, CommandLine
    ```

### 2. Detecting Credential Dumping
* **Purpose:** Search for processes accessing `lsass.exe`, a common indicator of credential theft.
* **SPL Query:**
    ```splunk
    index=main sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=10 
    TargetImage="C:\\windows\\system32\\lsass.exe"
    ```

### 3. Detecting Non-Browser Network Beaconing
* **Purpose:** Identify processes other than web browsers that are initiating network connections.
* **SPL Query:**
    ```splunk
    index=main sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=3 
    | search NOT (Image="*chrome.exe" OR Image="*firefox.exe") 
    | stats count by Image, DestinationIp, DestinationPort
    ```


## Next Steps
* Proceed to Day 13: Linux Forensics.
