# Lab 11 – Use the ipconfig Command

**Packet Tracer File:** `17_1_3_Packet_Tracer_Use_the_ipconfig_Command.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Troubleshooting, Static IP configuration, ipconfig /all

---

## Objective

Use the `ipconfig /all` command to identify which PC has an incorrect IP configuration and fix it.

---

## Step-by-Step Solution

### Part 1: Verify Configurations

1. Access **Command Prompt** on each of the four PCs.
2. Run:
   ```
   ipconfig /all
   ```
3. Examine and record for every PC:
   - IP Address
   - Subnet Mask
   - Default Gateway
   - DNS Server (if shown)

All PCs should be on the `192.168.1.0/24` network with the correct default gateway.

### Part 2: Correct Any Misconfigurations

1. Identify the PC whose IP address, subnet mask, or default gateway does **not** match the correct network.
2. On that PC → Desktop → **IP Configuration**.
3. Correct the values so they match the working PCs (same network, same gateway).
4. Verify connectivity by opening the web browser and going to `www.cisco.pka`.

---

## What I Learned

- `ipconfig /all` is one of the most important troubleshooting commands on Windows/Packet Tracer PCs.
- A single wrong default gateway or IP address can prevent internet access.
- Always compare a working PC with a non-working PC when troubleshooting.
