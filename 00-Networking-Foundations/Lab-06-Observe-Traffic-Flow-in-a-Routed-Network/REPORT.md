# Lab 06 – Observe Traffic Flow in a Routed Network

**Packet Tracer File:** `14_3_3_Packet_Tracer_Observe_Traffic_Flow_in_a_Routed_Network.pka`  
**Status:** Completed  
**Difficulty:** Intermediate  
**Topics:** Broadcast domains, ARP, Routing, Network efficiency, Subnetting benefits

---

## Objective

- Observe traffic flow in a flat (unrouted) LAN
- Reconfigure the network so each department is on its own network
- Compare ARP behavior before and after routing
- Understand why multiple networks improve efficiency

---

## Step-by-Step Solution

### Part 1: Observe Traffic Flow in an Unrouted LAN

1. Hover over **Sales 1** and note its IP address.
2. Click Sales 1 → Desktop → Command Prompt.
3. Clear ARP cache:
   ```
   arp -a
   arp -d
   ```
4. Switch to **Simulation** mode.
5. From **Sales 2** Command Prompt:
   ```
   ping <IP of Sales 1>
   ```
6. Use **Capture / Forward** and examine the PDUs.

**Observations:**
- Source and Destination MAC + IP of the first frame.
- Destination MAC is the **broadcast address** (FF-FF-FF-FF-FF-FF) because ARP is needed.
- Every host and switch on the LAN must process the ARP request.
- This creates unnecessary traffic on a large network.

### Part 2: Reconfigure the Network to Route Between LANs

1. The three switches are currently connected to each other.
2. Move the cable ends:
   - Accounting switch link → Edge Router **GigabitEthernet 1/0**
   - Finance–Sales link → Edge Router available GigabitEthernet port
3. On each host in Finance and Sales networks, open Command Prompt and run:
   ```
   ipconfig /renew
   ```
4. Record the new networks:
   - Finance network → usually `192.168.2.0/24`
   - Sales network → usually `192.168.3.0/24`
   - Accounting stays on `192.168.1.0/24`

### Part 3: Observe Traffic Flow in the Routed Network

1. Clear ARP cache on Sales 2 again.
2. Switch to Simulation mode.
3. Ping Sales 1 from Sales 2.
4. Observe ARP request behavior.

**Question:** Which devices receive the ARP broadcasts this time?  
**Answer:** Only devices on the **same network** (Sales network). The ARP request does not cross the router.

**Benefit of multiple IPv4 networks / subnets:**  
Broadcast domains become smaller → less unnecessary traffic → better performance and security.

---

## What I Learned

- In a flat network, ARP broadcasts reach every device → inefficient.
- Routers stop broadcasts and create separate broadcast domains.
- Using different subnets for different departments improves network efficiency.
- `ipconfig /renew` forces a client to request a new IP from DHCP.
