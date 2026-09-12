# Lab 08 – The Client Interaction

**Packet Tracer File:** `16_1_5_Packet_Tracer_The_Client_Interaction.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** Client-Server model, DNS, HTTP, Simulation Mode, PDU inspection

---

## Objective

Observe the complete client-server interaction when a PC requests a web page (DNS resolution + HTTP).

---

## Step-by-Step Solution

### Part 1: Enter Simulation Mode
Click the **Simulation Mode** button (bottom right).

### Part 2: Set Event List Filters
1. Click **Show All/None** to clear all filters.
2. Click **Edit Filters**.
3. Under **IPv4** tab → select **DNS**.
4. Under **Misc** tab → select **HTTP**.
5. Close the window.

### Part 3: Request a web page
1. Click the PC → Desktop → **Web Browser**.
2. Type `www.example.com` and click **Go**.
3. Minimize the PC window.

### Part 4: Run the simulation
1. Click **Play** in the Simulation Panel.
2. Observe the events:
   - DNS query
   - DNS reply (IP address of the server)
   - TCP 3-way handshake
   - HTTP GET request
   - HTTP response (web page data, often in multiple segments)
   - TCP acknowledgements
3. When buffer is full → click **View Previous Event**.

### Part 5 & 6: Examine PDU Information
1. Click the colored box of the first event in the Event List.
2. Use **Next Layer >>** to walk through each OSI layer and read the description.

---

## What I Learned

- A simple web request actually involves multiple protocols:
  1. DNS (to resolve name → IP)
  2. TCP (connection establishment)
  3. HTTP (the actual web page request)
- Simulation mode makes the entire conversation visible.
- HTTP runs on top of TCP.
