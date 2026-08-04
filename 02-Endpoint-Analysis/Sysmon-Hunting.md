# Day 11: Sysmon Process Mapping & Thread Queries

## Overview
This document outlines the methodology for utilizing Microsoft Sysmon (System Monitor) to perform granular endpoint threat hunting. By moving beyond standard Windows Event Logs, we gain visibility into process lineage, network socket creation, and DLL injection techniques.

## Configuration Strategy
For this lab, I implemented the [SwiftOnSecurity Sysmon Configuration](https://github.com/SwiftOnSecurity/sysmon-config) to ensure high-fidelity logging without overwhelming the Splunk indexer with noise.

## Key Event IDs Monitored
| Event ID | Description | Security Utility |
| :--- | :--- | :--- |
| **1** | Process Creation | Identifies malicious command-line arguments. |
| **3** | Network Connection | Detects C2 callbacks and lateral movement. |
| **7** | Image Loaded | Detects DLL side-loading and injection. |
| **11** | FileCreate | Monitors persistence mechanism installation. |

## Threat Hunting Queries (SPL)

### 1. Detecting Suspicious Parent-Child Relationships
Hunting for Office documents spawning unauthorized shells, a common indicator of weaponized macro payloads.

## splunk

index="wazuh_alerts" sourcetype="sysmon" EventCode=1 
| search ParentImage IN ("*\\WINWORD.EXE", "*\\EXCEL.EXE", "*\\POWERPNT.EXE")
| search Image IN ("*\\powershell.exe", "*\\cmd.exe", "*\\wscript.exe", "*\\cscript.exe")
| table _time, Computer, ParentImage, Image, CommandLine
| sort - _time

2. Identifying Unsigned Image Loads (Potential DLL Injection)
Searching for unsigned modules loaded into high-value processes.

Code snippet
index="wazuh_alerts" sourcetype="sysmon" EventCode=7 Signed=false
| stats count by Image, ImageLoaded, Computer
| sort - count
Lab Observations
Normalization: Used ParentImage and Image fields to visualize process trees.

Findings: Identified legitimate background activities (e.g., winword.exe spawning splwow64.exe for printing) to establish a baseline of "normal" behavior in the lab environment.