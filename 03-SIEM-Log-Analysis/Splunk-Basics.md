# 🖥️ SIEM Foundations: Splunk Architecture & Log Ingestion Engineering
**Author:** Vatsayu  
**Date:** June 15, 2026  
**Focus:** Splunk Component Layout, Enterprise Data Pipelines, and Hands-On Data Ingestion Mechanics

This log details the fundamental engineering layout of an enterprise SIEM (Splunk Focus) and outlines the step-by-step practical implementation for configuring indexers, search heads, and data inputs using free laboratory environments.

---

## 1. Enterprise Splunk Component Architecture

To effectively search logs as an analyst, you must understand the underlying pipeline that transforms raw system data into searchable text strings. Splunk Enterprise is split into three foundational components:

### 📦 The Universal Forwarder (UF)
* **Role:** The lightweight collector agent deployed directly on target assets (Windows Domain Controllers, Linux Web Servers).
* **Mechanism:** It consumes zero-effort compute power to monitor static files or system event streams, immediately forwarding the raw data over port **9997** to the indexer cluster.
* **Core Blue-Team Files:** * `inputs.conf`: Dictates *what* files, directories, or system events the agent is authorized to capture.
  * `outputs.conf`: Dictates *where* (the specific target Indexer IP address and port) to ship the collected logs.

### 🗄️ The Indexer
* **Role:** The data engine and storage repository.
* **Mechanism:** Receives incoming raw data streams from forwarders on port **9997**. It breaks the stream into discrete events, extracts the global timestamp, assigns critical operational metadata (`host`, `source`, `sourcetype`), and serializes/compresses the data onto disk blocks called **Buckets**.

### 🔍 The Search Head
* **Role:** The operational interface for the security team.
* **Mechanism:** The graphical user interface (Web UI running on port **8000**). When an analyst executes a Search Processing Language (SPL) query, the Search Head distributes the parsing request downward to the Indexers, aggregates the scattered hits, and builds the visual fields, charts, or alerts used in triage.

---

## 2. Hands-on Ingestion Lab: Step-by-Step Execution

### Lab Environment Selection
* **Platform:** TryHackMe ("Splunk: Basics" / "Splunk: Data Ingestion" Room) or Local Splunk Enterprise Instance (`http://localhost:8000`).

### Step 1: Open Ingestion Receiving Interface
1. Access the Splunk Web UI via your administrative browser pane at port `8000`.
2. Locate and click on the top-right menu panel path: **Settings** $\rightarrow$ **Data** $\rightarrow$ **Forwarding and receiving**.
3. Under the **Receive data** segment, click **+ Add New**.
4. Explicitly declare port `9997` as the listening network socket. This enables the Indexer to accept data streams from enterprise system forwarders. Click **Save**.

### Step 2: Manual Single-File Data Ingestion (Triage Warmup)
To replicate how historical event logs are loaded for threat replication, follow these strict ingestion steps:
1. Navigate back to the home view and choose **Settings** $\rightarrow$ **Add Data**.
2. Select the **Upload** module to import a static diagnostic file from your local machine.
3. Click **Select File** and point the browser to a mock log sheet (e.g., a web access `.log` or a flat server auth file).
4. **Set Source Type:** On the parsing screen, do not leave it to automatic detection. Click the category side-pane and explicitly categorize the file structure (e.g., select `syslog` or `access_combined` for web traffic). This forces Splunk to parse field boundaries uniformly.
5. **Assign Index:** Save the dataset inside a dedicated bucket (e.g., create a test sandbox index called `web_analysis`). Click **Review**, then hit **Submit**.

### Step 3: Verifying the Ingestion Pipeline via Search Head
1. Click on the **Search & Reporting** application panel on the home layout.
2. In the query box, clear any defaults and search across your newly configured index:
   ```splunk
   index="web_analysis"
