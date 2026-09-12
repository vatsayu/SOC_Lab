# Lab 03 – Configure DHCP on a Wireless Router

**Packet Tracer File:** `11_2_3_Packet_Tracer_Configure_DHCP_on_a_Wireless_Router.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Wireless Router, DHCP Server, IP addressing, Client configuration

---

## Objective

- Connect 3 PCs to a wireless router
- Change the default DHCP settings to a specific network range
- Configure clients to obtain IP addresses automatically via DHCP
- Verify connectivity between devices

---

## Step-by-Step Solution

### Part 1: Set up the network topology

1. Add three generic PCs (PC0, PC1, PC2).
2. Connect each PC to an Ethernet port on the wireless router using **Copper Straight-Through** cables.
3. Wait until all link lights turn green (or click Fast Forward Time).

### Part 2: Observe the default DHCP settings

1. Click **PC0** → Desktop → **IP Configuration** → select **DHCP**.
2. Record the Default Gateway address (usually `192.168.0.1`).
3. Open Web Browser on PC0 and enter the Default Gateway IP.
4. Login with:
   - Username: `admin`
   - Password: `admin`
5. Scroll through the Basic Setup page and note:
   - Router IP address
   - DHCP is enabled
   - Starting IP address of the DHCP pool
   - Maximum number of users

### Part 3: Change the default IP address of the wireless router

1. In the Router IP Settings section, change the IP address to:
   ```
   192.168.5.1
   ```
2. Scroll down and click **Save Settings**.
3. The browser will show an error (expected) because the PC still has the old IP.
4. Close the browser.
5. On PC0 → IP Configuration → click **Static** then immediately click **DHCP** again to renew the address.
6. Open the browser and go to `192.168.5.1`.
7. Login again with `admin` / `admin`.

### Part 4: Change the default DHCP range of addresses

1. Notice the DHCP Server Start IP Address is now on the same network (`192.168.5.x`).
2. Change the following:
   - Starting IP Address → `192.168.5.126`
   - Maximum Number of Users → `75`
3. Click **Save Settings**.
4. Close the browser.
5. On PC0 → IP Configuration → Static → DHCP (to renew).
6. Open **Command Prompt** on PC0 and type:
   ```
   ipconfig
   ```
7. Record the IP address of PC0 (it should be `192.168.5.126`).

### Part 5: Enable DHCP on the other PCs

1. On **PC1** → Desktop → IP Configuration → select **DHCP**.
2. Record the IP address of PC1 (usually `192.168.5.127`).
3. Repeat the same steps on **PC2**.

### Part 6: Verify connectivity

From **PC2** Command Prompt:

```bash
ipconfig
ping 192.168.5.1          # Wireless Router
ping 192.168.5.126        # PC0
ping 192.168.5.127        # PC1
```

All pings should be successful.

---

## Expected Results

| Device | Expected IP Address     |
|--------|-------------------------|
| Router | 192.168.5.1            |
| PC0    | 192.168.5.126          |
| PC1    | 192.168.5.127          |
| PC2    | 192.168.5.128          |

---

## What I Learned

- How to change the LAN IP address of a home wireless router
- How DHCP pool start address and maximum users work
- Importance of renewing the IP address on clients after changing router settings
- How to verify Layer 3 connectivity with `ping` and `ipconfig`

---

## Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| Browser cannot reach new router IP | Renew DHCP on the PC (Static → DHCP) |
| IP address not updating | Click Fast Forward Time several times |
| Ping fails | Confirm all PCs are set to DHCP and have 192.168.5.x addresses |
