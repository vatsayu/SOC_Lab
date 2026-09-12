# Lab 07 – Create a LAN

**Packet Tracer File:** `14_3_4_Packet_Tracer_Create_a_LAN.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Physical connections, DHCP vs Static IP, Connectivity testing, ipconfig, tracert

---

## Addressing Table

| Device       | Interface/Port | IPv4 Address       | Subnet Mask     |
|--------------|----------------|--------------------|-----------------|
| Admin PC     | NIC            | DHCP               | N/A             |
| Manager PC   | NIC            | DHCP               | N/A             |
| Printer      | NIC            | 192.168.1.100      | 255.255.255.0   |
| www.cisco.pt | NIC            | 209.165.200.225    | N/A             |

---

## Step-by-Step Solution

### Part 1: Connect Network Devices and Hosts

1. Power on the end devices and Office Router (Physical tab → power switch).
2. Use **Copper Straight-Through** cables according to the Connections Table:

| Device        | Interface     | Connected to   | Interface     |
|---------------|---------------|----------------|---------------|
| Office Router | G0/0          | ISP1           | G0/0          |
| Office Router | G0/1          | Switch         | G0/1          |
| Admin PC      | NIC           | Switch         | F0/1          |
| Manager PC    | NIC           | Switch         | F0/2          |
| Printer       | NIC           | Switch         | F0/24         |

3. All link lights should turn green.

### Part 2: Configure Devices with IPv4 Addressing

1. **Admin PC** and **Manager PC** → Desktop → IP Configuration → select **DHCP**.
2. **Printer** → Config tab → FastEthernet0:
   - IP Address: `192.168.1.100`
   - Subnet Mask: `255.255.255.0`
3. Questions:
   - Why different IPs but same mask & gateway?  
     → Because they are unique hosts on the **same subnet**.
   - Printer default gateway (if needed) = Office Router LAN IP (usually `192.168.1.1`).

### Part 3: Verify Connectivity

1. From Admin PC and Manager PC, ping the Printer IP → success.
2. Open Web Browser and go to the IP of the internet server and also the URL.
3. **Question:** If IP works but URL fails → **DNS problem**.

### Part 4: Use Networking Commands

1. `ipconfig` → shows basic addressing.
2. `ipconfig /all` → shows additional information (MAC, DHCP server, DNS servers, lease time, etc.).
3. `tracert www.cisco.pt` (or the server URL):
   - Shows how many routers are passed.
   - Second router is usually located at the ISP.

---

## Reflection

Biggest facilities challenge in a real office:  
**Physical cabling, cable management, power, and space planning.**

---

## What I Learned

- Difference between DHCP (dynamic) and static addressing.
- Servers and printers are often given static IPs.
- `ipconfig /all` and `tracert` are essential troubleshooting tools.
- Successful ping + web access confirms Layer 3 and Layer 7 connectivity.
