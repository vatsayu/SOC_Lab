# Lab 12 – Use the ping Command

**Packet Tracer File:** `17_1_6_Packet_Tracer_Use_the_ping_Command.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Troubleshooting with ping, DNS vs IP connectivity

---

## Objective

Use the `ping` command to identify which PCs have connectivity problems and determine whether the issue is Layer 3 or DNS related.

---

## Step-by-Step Solution

### Part 1: Verify connectivity
1. On each PC → Desktop → Web Browser.
2. Enter `www.cisco.pka`.
3. Identify which PCs cannot load the website.

### Part 2: Ping the web server from PCs with issues
```bash
ping www.cisco.pka
```
Note whether a reply is received and what IP address (if any) is shown.

### Part 3: Ping from correctly configured PCs
Repeat the same ping on working PCs and compare results.

### Part 4: Ping the IP address directly
From the problem PCs, ping the actual IP address of the web server (instead of the name).

- If IP ping works but name ping fails → **DNS problem**.
- If IP ping also fails → deeper Layer 3 / gateway issue.

### Part 5: Compare DNS server information
1. On working PCs run:
   ```
   ipconfig /all
   ```
2. Note the DNS server address.
3. On problem PCs run the same command and compare.

### Part 6: Fix the configuration
1. Go to Desktop → **IP Configuration** on the problem PCs.
2. Correct the DNS server address so it matches the working PCs.
3. Test again with the web browser → `www.cisco.pka` should now load.

---

## What I Learned

- `ping` by name tests both DNS resolution and IP connectivity.
- `ping` by IP address tests only Layer 3 connectivity.
- When name fails but IP works → the problem is almost always DNS configuration.
- Always compare a working device with a non-working device.
