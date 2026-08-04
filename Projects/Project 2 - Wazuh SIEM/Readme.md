# Project 2: Wazuh SIEM Security Lab

## What Is This Project?
Wazuh is a free, open-source Security Information and Event Management (SIEM) tool. In this project, I set up a security monitoring lab to practice real-world log analysis and file integrity monitoring. The lab consists of a Wazuh Manager (Ubuntu) and a Wazuh Agent (Windows).

## Concepts Learned
* **SIEM Fundamentals:** Understanding why organizations use SIEM tools to monitor security events.
* **Agent-Manager Communication:** Connecting endpoints to a central management server.
* **File Integrity Monitoring (FIM):** Detecting unauthorized file and directory changes, which is critical for identifying potential system compromises.
* **Log Analysis:** Learning to interpret security event logs to identify threats.

## Tools Required
* **VirtualBox:** To run the virtual machines.
* **Ubuntu 22.04:** Used as the Wazuh Manager.
* **Windows 10/11:** Used as the Wazuh Agent.
* **Wazuh OVA:** Pre-built virtual appliance for the manager.

## Step-by-Step Implementation

### Phase 1: Set Up the Wazuh Manager
1. Import the Wazuh OVA into VirtualBox via `File > Import Appliance`.
2. Start the VM and log in with default credentials.
3. Run `ip a` in the terminal to find the VM's IP address.
4. Access the dashboard on your host machine at `https://[UBUNTU-IP]`.

### Phase 2: Set Up the Windows Agent
1. Create a Windows VM on the same Host-Only network as the manager.
2. Download the Wazuh Agent MSI from `wazuh.com/install` and run the installer.
3. Enter the Ubuntu Manager's IP address when prompted.
4. Verify the agent is 'Running' in Windows Services and 'Active' in the dashboard.

### Phase 3: Configure File Integrity Monitoring (FIM)
1. On the Windows VM, edit `C:\Program Files (x86)\ossec-agent\ossec.conf`.
2. Add the directory to monitor within the `<syscheck>` section: `<directories check_all="yes">C:\Users\YourUsername\Documents</directories>`.
3. Restart the Wazuh service: `net stop wazuh && net start wazuh`.
4. Create a test file in the monitored folder and verify the alert in the dashboard.
