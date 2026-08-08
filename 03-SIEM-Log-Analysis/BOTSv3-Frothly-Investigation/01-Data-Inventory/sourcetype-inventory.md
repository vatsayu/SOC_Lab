# Day 1 – Sourcetype Inventory (BOTSv3)

**Date:** 2026-08-06  
**Search used:**

index=botsv3 earliest=0
| stats count by sourcetype
| sort -count

**Note:** Search was run with **Sampling 1:100** for speed. Counts below are sampled (real volume is ~100× higher).

---

## Summary

| Item                        | Value                  |
|----------------------------|------------------------|
| Approximate total events   | ~2,000,000+ (full set) |
| Distinct sourcetypes       | 78+                    |
| Distinct hosts             | 28                     |
| Main attack window         | 20 August 2018         |
| Environment type           | Hybrid (On-prem + AWS) |

---

## Top 15 Sourcetypes (Sampled)

| Rank | Sourcetype                      | Sampled Count | Why it matters for SOC Analyst                  |
|------|---------------------------------|---------------|-------------------------------------------------|
| 1    | syslog                          | 2,787         | General system & application logs               |
| 2    | stream:ip                       | 2,292         | Network layer visibility                        |
| 3    | stream:dns                      | 2,149         | DNS queries – excellent for C2 & beaconing      |
| 4    | osquery:results                 | 2,126         | Endpoint inventory & process data               |
| 5    | stream:udp                      | 1,541         | UDP traffic                                     |
| 6    | WinHostMon                      | 1,298         | Windows host performance & status               |
| 7    | aws:cloudwatchlogs              | 1,126         | AWS CloudWatch logs                             |
| 8    | PerfmonMk:Process               | 1,115         | Windows process monitoring                      |
| 9    | aws:cloudwatchlogs:vpcflow      | 959           | AWS VPC Flow Logs                               |
| 10   | stream:tcp                      | 875           | TCP connections                                 |
| 11   | stream:http                     | 249           | Web traffic (very useful for investigations)    |
| 12   | stream:mysql                    | 446           | Database traffic                                |
| 13   | symantec:ep:packet:file         | 135           | Symantec Endpoint Protection                    |
| 14   | symantec:ep:traffic:file        | 65            | Symantec traffic logs                           |
| 15   | stream:smtp                     | 10            | Email traffic                                   |

---

## Top Hosts Observed

| Host                          | Sampled Count | Likely Role                     |
|-------------------------------|---------------|---------------------------------|
| hoth                          | 3,833         | Linux server (important)        |
| serverless                    | 2,441         | Cloud / serverless component    |
| BSTOLL-L                      | 2,173         | Windows workstation (key host)  |
| gacrux.i-0920036c8ca91e501    | 1,725         | AWS instance                    |
| mars.i-08e52f8b5a034012d      | 1,541         | AWS instance                    |
| matar                         | 850           | Linux host                      |
| ip-172-16-0-109.ec2.internal  | 797           | AWS internal host               |
| FROTHLY-FW1                   | 764           | Firewall (Cisco ASA)            |
| splunkhwf.froth.ly            | 757           | Splunk / internal host          |
| BTUN-L                        | 741           | Windows workstation             |

---

## Key Observations

- Strong mix of **network (stream:*)**, **endpoint (osquery + Windows)**, and **cloud (AWS)** data.
- `hoth` and `BSTOLL-L` appear frequently → these will be important during investigation.
- Firewall (`FROTHLY-FW1` + `cisco:asa`) and DNS (`stream:dns`) give good visibility for lateral movement and C2.
- Data is heavily concentrated around **20 August 2018**.

---

## Screenshots
- [Sourcetype Stats](../screenshots/Day1/01-sourcetype-stats.png)
- [Host Values](../screenshots/Day1/02-host-values.png)
- [Destination IP Values](../screenshots/Day1/03-dest_ip-values.png)

## Next Steps (Day 2)

- Map the most important hosts in detail
- Start first investigation questions (IAM users, CloudTrail, etc.)
- Practice basic SPL filters and field extraction