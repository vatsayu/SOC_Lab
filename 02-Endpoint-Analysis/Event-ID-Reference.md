#  Day 10: Windows Event Log Auditing & Brute-Force Triage

## Core Security Event ID Technical Mapping
During live triage, an analyst must instantly decode specific Windows Security logs to establish user context and track malicious persistence mechanisms.

| Event ID | Log Definition | Analyst Investigation Logic |
| :--- | :--- | :--- |
| **4624** | Successful Account Logon | Checked to establish an active session, identify the Logon Type and map source workstations. |
| **4625** | Failed Account Logon | The primary indicator used to identify authentication failures, mistyped credentials, or automated brute-force attacks. |
| **4720** | User Account Created | Monitored strictly; unauthorized account creation is a standard backdoor method used by threat actors for persistence. |
| **4672** | Special Privileges Assigned | Triggers when an account logs on with administrative rights. Crucial for tracking privilege escalation. |

---

## 🎯 Case Study: Triaging an Authentication Incident via Logs

### 1. The Engineering Logic: Logon Types to Remember
When analyzing **Event ID 4624/4625** payloads, the `Logon Type` field reveals *how* the connection was made:
- **Logon Type 2 (Interactive):** A user physically typed credentials at the local keyboard or console.
- **Logon Type 3 (Network):** A connection was made from a remote machine (e.g., accessing a shared network folder or IIS website).
- **Logon Type 10 (RemoteInteractive):** The attacker used Remote Desktop Protocol (RDP) to gain a graphical user interface session.

---

## 🧪 Practical Hands-on Lab: LetsDefend Log Triage

### Incident Overview & Log Metrics
- **Alert Rule Name:** SOC176 - RDP Brute Force Detected
- **Target Hostname Audited:** `Server-1`
- **Target Account Targeted:** `Administrator`
- **Attacker Source Network Address:** `218.92.0.56`

### Timeline of Log Anomalies
1. **Phase 1 (The Flood):** Observed a high-velocity spike of **Event ID 4625 (Failed Logon)** entries within a very tight window. 
   - *Total Failures Count:* High-density volume of continuous failure entries.
   - *Failure Reason Code:* `0xC000006A` (User typed the wrong password or unknown user name/bad password combination).
   - *Logon Type:* Verified as `Logon Type 10`, confirming an active external RDP attack layer.
2. **Phase 2 (The Outcome / True Positive Verification):** Chronological log tracking across Log Management shows *no* trailing **Event ID 4624 (Successful Logon)** from source `218.92.0.56`. 
   - *Result:* Host password strength and security protocols successfully rejected the automated threat. The incident is classified as a **True Positive - Blocked Attempt**.

---

## 🛡️ Containment & Playbook Actions
Because an external IP address is dynamically running continuous malicious automation against our enterprise endpoint perimeter, the following defensive actions were taken to close the case:
1. **Perimeter Blocking:** Submitted the malicious external source IP address (`218.92.0.56`) to the network firewall gateway policy to completely block any future inbound traversal.
2. **Account Hardening:** Recommended enforcing standard domain Account Lockout thresholds (e.g., locking the profile for 15 minutes after 5 consecutive failed interactive attempts).
3. **Architecture Optimization:** Suggested hiding exposed public RDP instances behind an internal corporate VPN gateway or using a Zero-Trust Network Access platform.