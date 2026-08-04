# Day 13: Linux Forensics — CLI Log Parsing vs. Splunk Auditing

## 📖 Mission Scenario
**Incident Context:** At 18:00 UTC, the network security team flagged an unusual outbound volume spike from a production Ubuntu web server (`web-prod-01`). An unknown external IP address (`198.51.100.42`) was seen establishing persistent SSH connections. 

**Your Objective:** You are the SOC Analyst on duty. You must triage the authentication logs on `web-prod-01` to determine if an adversary successfully brute-forced local accounts, identify which identities were compromised, and audit any subsequent administrative privilege escalation (`sudo`) commands executed by the attacker.

---

## 📁 Core Linux Log Architecture Reference

When investigating a live Linux environment, security-relevant actions are written to flat text streams. In a SIEM environment like Splunk, these raw lines are indexed into searchable key-value fields.

| Linux Distribution Family | Default Path | Splunk Target Sourcetype | Primary Event Coverage |
| :--- | :--- | :--- | :--- |
| **Debian / Ubuntu** | `/var/log/auth.log` | `linux_secure` or `syslog` | SSH logins, `sudo` usage, user additions, PAM sessions. |
| **RHEL / CentOS / Rocky** | `/var/log/secure` | `linux_secure` | SSH logins, `sudo` usage, user additions, PAM sessions. |
| **Generic System Daemon** | `/var/log/syslog` | `syslog` | Global system events, cron jobs, service crashes. |

---

## 🔍 Investigation Runbooks: CLI vs. Splunk SPL

### Phase 1: Identifying the Brute-Force Vector
* **Goal:** Verify if a brute-force attack occurred, isolate the top attacking source IP addresses, and find out if any attempts succeeded.

#### Tactical Command-Line Execution (On the Endpoint)
```bash
# Extract top 10 unique external IP addresses attempting to guess passwords
grep "Failed password for" /var/log/auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr | head -n 10

# Check for successful logins following brute-force activity to confirm compromise
grep "Accepted password for" /var/log/auth.log
```
# Enterprise SIEM Execution (Inside Splunk)
index=linux sourcetype=linux_secure "Failed password"
| stats count by src_ip, user
| sort - count

index=linux sourcetype=linux_secure "Accepted password"
| table _time, host, user, src_ip, port
| sort - _time

# Phase 2: Post-Exploitation & Privilege Escalation Audit

Goal: Once an account is breached, attackers frequently attempt to pivot to root using sudo. We need to track every command they ran with elevated privileges.

Tactical Command-Line Execution (On the Endpoint)

# Audit all successful sudo commands executed by users
grep "COMMAND=" /var/log/auth.log | awk -F'USER=' '{print $2}' | awk -F'COMMAND=' '{print "User Context: " $1 "-> Executed: " $2}'

# Detect failed attempts to switch to root or use sudo by unauthorized accounts
grep -E "authentication failure|not in sudoers" /var/log/auth.log