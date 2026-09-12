# Lab 10 – Use Telnet and SSH

**Packet Tracer File:** `16_6_4_Packet_Tracer_Use_Telnet_and_SSH.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Remote access, Telnet vs SSH, Security

---

## Addressing Table

| Device | Interface | IP Address     | Subnet Mask   |
|--------|-----------|----------------|---------------|
| HQ     | G0/0/1    | 64.100.1.1     | 255.255.255.0 |
| PC0    | NIC       | DHCP           |               |
| PC1    | NIC       | DHCP           |               |

---

## Step-by-Step Solution

### Part 1: Verify Connectivity

1. From a PC → Desktop → Command Prompt.
2. Verify IP address from DHCP:
   ```
   ipconfig
   ```
   or
   ```
   ipconfig /all
   ```
3. Ping the router:
   ```
   ping 64.100.1.1
   ```

**Question:** What command did you use to verify the IP address from DHCP?  
**Answer:** `ipconfig` (or `ipconfig /all`)

### Part 2: Access a Remote Device

#### Step 1: Try Telnet
```bash
telnet 64.100.1.1
```

**Result:** Connection fails / refused.  
The router is configured to reject insecure Telnet access.

#### Step 2: Use SSH
```bash
ssh -l admin 64.100.1.1
```
Password when prompted: `class`

**Successful prompt after login:**  
`HQ#` (or `HQ>`)

---

## What I Learned

- Telnet sends everything (including passwords) in clear text → insecure.
- SSH encrypts the entire session → preferred remote access method.
- Modern devices should disable Telnet and only allow SSH.
- Command syntax: `ssh -l username ip-address`
