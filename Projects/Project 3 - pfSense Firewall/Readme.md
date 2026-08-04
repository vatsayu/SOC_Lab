# Project 3: pfSense Network Firewall

## What Is This Project?
[cite_start]In this project, I built a simulated network environment using pfSense, an open-source firewall[cite: 187]. [cite_start]The architecture includes a pfSense firewall, an internal Ubuntu machine (LAN), and an external Kali Linux machine (WAN)[cite: 187].

## Concepts Learned 
* [cite_start]**Stateful vs. Stateless Firewalls:** pfSense is stateful, meaning it keeps track of ongoing connections[cite: 190, 191].
* [cite_start]**Firewall Rules:** Learning to create specific rules to allow or block traffic[cite: 189].
* [cite_start]**Traffic Shaping:** Implementing rate limiting to prevent bandwidth abuse[cite: 190].
* [cite_start]**Log Analysis:** Interpreting firewall logs to identify attack patterns[cite: 190].

## Tools Required
* [cite_start]**VirtualBox:** For running the virtual machines[cite: 192].
* [cite_start]**pfSense ISO:** The firewall operating system[cite: 192].
* [cite_start]**Ubuntu 22.04:** Used as the protected internal machine[cite: 192].
* [cite_start]**Kali Linux:** Used as the attacker machine[cite: 192].

## Step-by-Step Implementation

### Phase 1: Network Architecture
1. [cite_start]In VirtualBox, create two Host-Only networks: one for LAN (e.g., 192.168.100.0/24) and one for WAN (e.g., 192.168.200.0/24)[cite: 194, 195, 196].
2. [cite_start]Configure the pfSense VM with two network adapters, assigning them to the LAN and WAN networks[cite: 200, 201].

### Phase 2: Configuration
1. [cite_start]Install the pfSense ISO and assign `em0` to WAN and `em1` to LAN[cite: 202, 203].
2. [cite_start]From the Ubuntu VM on the LAN, navigate to the pfSense LAN IP (e.g., `https://192.168.1.1`) to complete the setup[cite: 204, 205].

### Phase 3: Firewall Rules
1. [cite_start]Navigate to **Firewall > Rules**[cite: 210].
2. [cite_start]Create a Block rule on the WAN interface to restrict traffic to the Ubuntu machine[cite: 211, 212].
3. [cite_start]Create an Allow rule for specific traffic (e.g., Port 80 for HTTP)[cite: 214].
4. [cite_start]Remember: Rules are processed top-to-bottom; order matters[cite: 218].

### Phase 4: Rate Limiting & Logs
1. [cite_start]Navigate to **Firewall > Traffic Shaper** to set up a 'Limiter'[cite: 219, 220].
2. [cite_start]Apply the limiter to your WAN pass rule[cite: 221].
3. [cite_start]View firewall logs under **Status > System Logs > Firewall** to identify blocked versus allowed traffic[cite: 224, 225].