# Lab 05 – Identify MAC and IP Addresses

**Packet Tracer File:** `13_1_3_Packet_Tracer_Identify_MAC_and_IP_Addresses.pka`  
**Status:** Completed  
**Difficulty:** Intermediate  
**Topics:** MAC vs IP, ARP, Local vs Remote communication, PDU analysis, OSI layers

---

## Objective

- Inspect Ethernet frames and IP packets at different points in the network
- Understand how MAC addresses change while IP addresses stay the same
- Compare local (same network) vs remote (different network) communication

---

## Step-by-Step Solution

### Part 1: Gather PDU Information for Local Network Communication

1. Click host `172.16.31.3` → Command Prompt.
2. Enter:
   ```
   ping 172.16.31.2
   ```
3. Switch to **Simulation** mode and repeat the ping.
4. Click the PDU and examine:
   - OSI Model tab
   - Outbound PDU Details tab
5. Record for each hop:
   - At Device
   - Source MAC
   - Destination MAC
   - Source IPv4
   - Destination IPv4
6. Use **Capture / Forward** to move the PDU step by step until it reaches the destination.

**Key Observation (Local communication):**  
Destination MAC = actual MAC of the target host (because they are on the same network). No default gateway is needed.

### Part 2: Gather PDU Information for Remote Network Communication

1. Return to Command Prompt of `172.16.31.3`.
2. Enter:
   ```
   ping 10.10.10.2
   ```
3. Switch to Simulation mode and repeat the ping.
4. Examine the first PDU:
   - Source MAC = MAC of 172.16.31.3
   - Destination MAC = MAC of the Router interface (default gateway)
   - Source IP = 172.16.31.3
   - Destination IP = 10.10.10.2
5. Continue capturing through the router until the PDU reaches 10.10.10.2.
6. Also capture the echo-reply (pong) path.

**Key Observation (Remote communication):**  
- Destination MAC on the first hop is the **router’s MAC** (default gateway).
- At the router the MAC addresses are rewritten.
- IP addresses remain the same end-to-end.

---

## Reflection Questions – Answers

1. **What different types of cables/media were used?**  
   Copper straight-through (Ethernet) and wireless.

2. **Did the cables change the handling of the PDU?**  
   No. Cables only transport the frames.

3. **Did the wireless Access Point do anything to the PDUs?**  
   It only forwards frames at Layer 2. It does not change IP or MAC addresses.

4. **Was PDU addressing changed by the access point?**  
   No.

5. **Highest OSI layer the Access Point used?**  
   Layer 2 (Data Link).

6. **At what Layer do cables and access points operate?**  
   Layer 1 (Physical) and Layer 2 (Data Link).

7. **Which MAC address appeared first in PDU Details?**  
   Destination MAC appears first, then Source MAC.

8. **Meaning of red Xs and green check marks?**  
   Green check = successful / accepted. Red X = dropped or filtered.

9. **Where did MAC addresses suddenly change?**  
   At the **Router** (Layer 3 device).

10. **Which device uses MAC addresses starting with 00D0:BA?**  
    The Router.

11. **What devices did the other MAC addresses belong to?**  
    Hosts and the wireless Access Point / switch.

12. **Did the sending and receiving IPv4 addresses change?**  
    No. IP addresses stay the same end-to-end.

13. **What happens to source and destination addresses on the reply (pong)?**  
    They are swapped.

14. **Why are router interfaces in two different IP networks?**  
    So the router can route traffic between different networks.

15. **Which IP networks are connected by the router?**  
    172.16.31.0 network and 10.10.10.0 network.

---

## What I Learned

- MAC addresses are local (hop-by-hop).
- IP addresses are end-to-end.
- ARP is only used on the local network.
- Default gateway is required only when communicating with remote networks.
- Routers rewrite MAC addresses; switches and APs do not change IP addresses.
