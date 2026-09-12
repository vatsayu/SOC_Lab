# Lab 04 – Examine NAT on a Wireless Router

**Packet Tracer File:** `12_2_2_Packet_Tracer_Examine_NAT_on_a_Wireless_Router.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** NAT, Private vs Public IP, DHCP, Simulation Mode, Packet analysis

---

## Objective

- Examine NAT configuration on a wireless router
- Connect multiple PCs using DHCP
- Observe traffic that crosses the network using NAT
- Understand the difference between private and public addresses

---

## Step-by-Step Solution

### Part 1: Examine the configuration for accessing external network

1. Add 1 PC and connect it to the wireless router with a straight-through cable.
2. Wait for link lights to turn green (or Fast Forward).
3. On the PC → Desktop → IP Configuration → select **DHCP**.
4. Note the Default Gateway address.
5. Open Web Browser → enter the Default Gateway IP.
6. Login: `admin` / `admin`.
7. Click **Status** (upper right) → Router sub-menu.
8. Scroll to **Internet Connection**.
   - The IP address shown here is assigned by the ISP.
   - If it shows `0.0.0.0`, wait a few seconds and refresh.

**Question:** Is this a private or public address?  
**Answer:** **Public address** (assigned by the ISP).

### Part 2: Examine the configurations for accessing the internal network

1. Click **Local Network** within the Status menu.
2. Examine the Local Network information (this is the internal LAN address).
3. Scroll further to see the DHCP server range.

**Question:** Are these private or public addresses?  
**Answer:** **Private addresses**.

### Part 3: Connect 3 more PCs

1. Add 3 more PCs and connect them to the wireless router with straight-through cables.
2. On each PC → Desktop → IP Configuration → select **DHCP**.
3. Verify with Command Prompt:
   ```
   ipconfig /all
   ```
   All devices receive private addresses.

### Part 4: View NAT translation (Simulation Mode)

1. Switch to **Simulation** mode (bottom right).
2. In Simulation Panel → **Show All/None** → then **Edit Filters**.
3. Under Misc tab → check only **TCP** and **HTTP**.
4. Create a Complex PDU:
   - Click the open envelope icon.
   - Click one of the PCs as source.
   - Application: **HTTP**
   - Destination: click the `ciscolearn.nat.com` server
   - Source Port: `1000`
   - Simulation Settings → Periodic → Interval `120` seconds
   - Click **Create PDU**
5. Click **Play** and observe the traffic.
6. When buffer is full, click **View Previous Events**.

### Part 5: View header information

1. In the Event List, double-click the 3rd line.
2. Click the envelope in the work area.
3. Examine:
   - **Inbound PDU Details** → Source and Destination IP
   - **Outbound PDU Details** → Source and Destination IP

**Key Observation:**  
The **Source IP changes** after the packet leaves the router (private → public). This is NAT/PAT in action.

---

## What I Learned

- Private addresses (192.168.x.x, 10.x.x.x, 172.16-31.x.x) cannot travel on the public Internet.
- The wireless router performs Network Address Translation (NAT / PAT).
- Inside the LAN → private IP is used.
- When traffic goes to the Internet → source IP is translated to the public IP of the router’s Internet interface.
- Simulation mode is the best way to visually confirm NAT.

---

## Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| Internet IP shows 0.0.0.0 | Wait a few seconds or click Fast Forward Time |
| No traffic appears in Simulation | Make sure only TCP and HTTP filters are enabled |
| Cannot see source IP change | Look carefully at Inbound vs Outbound PDU Details |
