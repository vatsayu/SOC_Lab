# SIEM Log Parsing & Basic SPL Command Syntactics
**Focus:** Search Processing Language (SPL) Pipeline Operations, Field Filtering, and Noise Reduction.

## 1. Core SPL Structural Pipeline Commands
* **`index` / `sourcetype`:** The primary filtering layer. Restricting queries here prevents Splunk from scanning unnecessary data buckets.
* **`fields`:** Controls what data columns are preserved across the pipeline. Using it early saves search memory.
* **`dedup`:** Strips away repeating duplicate events based on a specified field, isolating unique attributes.
* **`table`:** A formatting command that transforms raw logs into a clean, spreadsheet-style table.

## 2. Practical Verification Query (Splunk Telemetry Analysis)
```splunk
index="_internal" sourcetype="splunkd" 
| fields component, log_level, message 
| dedup component 
| table component, log_level, message
