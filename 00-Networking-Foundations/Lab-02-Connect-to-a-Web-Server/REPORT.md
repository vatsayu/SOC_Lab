# Lab 02 – Connect to a Web Server

**Packet Tracer File:** `8_1_3_Packet_Tracer_Connect_to_a_Web_Server.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics Covered:** Ping (ICMP), Web Browser access, IP connectivity, Client-Server communication

---

## Objective

- Verify network connectivity from a PC to a web server using the `ping` command
- Access a web server using its IP address through a web browser
- Observe basic client-server communication

---

## Topology Overview

Simple network:
- **PC0** (client)
- Web Server with IP address `172.33.100.50`
- Devices are already connected and configured

---

## Step-by-Step Solution (How I Completed It)

### Part 1: Verify Connectivity to the Web Server

1. Click on **PC0**.
2. Go to the **Desktop** tab.
3. Click **Command Prompt**.
4. Type the following command and press Enter:
   ```
   ping 172.33.100.50
   ```
5. Result:
   - Received replies from `172.33.100.50`
   - Example output:
     ```
     Reply from 172.33.100.50: bytes=32 time=0ms TTL=127
     ```
   - This confirms Layer 3 (IP) connectivity is working.

**Note:** The first ping may sometimes time out while ARP resolves the MAC address. This is normal.

6. Close only the Command Prompt window (leave the PC0 window open).

---

### Part 2: Connect to the Web Server via Web Browser

1. Still on **PC0** → Desktop tab.
2. Click **Web Browser**.
3. In the URL box, type:
   ```
   172.33.100.50
   ```
4. Click **Go**.
5. The web page from the server loaded successfully.

---

### Question Answer

**What messages did you see after the web page has finished loading?**

The web page content itself appeared (a simple webpage hosted on the server).  
No error messages were shown. This confirms that both the network path and the HTTP service on the server are working correctly.

---

## Key Commands / Actions Used

| Action              | Location                  | Purpose                              |
|---------------------|---------------------------|--------------------------------------|
| `ping`              | Command Prompt            | Test Layer 3 connectivity            |
| Web Browser         | PC Desktop                | Access web server using IP address   |
| Fast Forward Time   | Bottom toolbar (if needed)| Speed up any delayed responses       |

---

## What I Learned

- `ping` uses ICMP and is the fastest way to check if a device is reachable at Layer 3.
- Successful ping replies mean the IP path (including any routers/switches) is working.
- A web browser uses HTTP (Layer 7) on top of the working IP connection.
- You can access a server either by IP address or by domain name (in later labs we will see DNS).
- Even a simple network still follows the client-server model: PC requests → Server responds.

---

## Common Issues & How I Fixed Them

| Problem                          | Solution                                      |
|----------------------------------|-----------------------------------------------|
| Ping shows "Request timed out"   | Wait a few seconds or click Fast Forward Time |
| Web page does not load           | Confirm ping works first, then try browser again |
| Wrong IP typed                   | Double-check the IP: `172.33.100.50`          |

---

## Final Result

- Ping to `172.33.100.50` successful
- Web page loaded successfully using the IP address
- Lab completed with full connectivity

---

## Next Lab

→ Lab 03 – Configure DHCP on a Wireless Router (`11_2_3_Packet_Tracer_Configure_DHCP_on_a_Wireless_Router.pka`)
