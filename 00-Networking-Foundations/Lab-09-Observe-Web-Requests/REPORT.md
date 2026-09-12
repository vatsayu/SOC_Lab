# Lab 09 – Observe Web Requests

**Packet Tracer File:** `16_4_3_Packet_Tracer_Observe_Web_Requests.pka`  
**Status:** Completed  
**Difficulty:** Beginner  
**Topics:** HTTP, TCP overhead, DNS, Simulation Mode, Complex PDU

---

## Objective

View the client/server traffic when a PC requests web services and understand the amount of overhead created by HTTP over TCP.

---

## Step-by-Step Solution

### Part 1: Verify connectivity
1. Click **External Client** → Desktop → Command Prompt.
2. Ping the URL:
   ```
   ping ciscolearn.web.com
   ```
3. Notice the IP address returned by DNS.

### Part 2: Connect to the web server
1. Open **Web Browser** on External Client.
2. Type `ciscolearn.web.com` and press Go.
3. Read the web page that appears.

### Part 3: View the HTML code
1. Click the `ciscolearn.web.com` server.
2. Services tab → HTTP → click **(edit)** next to index.html.
3. Compare the HTML code with what the browser displays.

### Part 4: Observe traffic in Simulation Mode
1. Enter **Simulation** mode.
2. Edit Filters → Misc tab → only **TCP** and **HTTP** checked.
3. Create a **Complex PDU**:
   - Source = External Client
   - Application = HTTP
   - Destination = ciscolearn.web.com server
   - Starting Source Port = 1000
   - Periodic Interval = 120 seconds
4. Click **Create PDU** then **Play**.
5. Observe the large number of packets (TCP handshake, data segments, ACKs, teardown).

**Key Observation:**  
HTTP is a TCP protocol → connection establishment + acknowledgements create significant traffic overhead compared to a simple ping.

---

## What I Learned

- DNS resolves the domain name to an IP address before the HTTP request.
- HTTP generates many packets because of TCP reliability mechanisms.
- Simulation mode + Complex PDU is the best way to study application traffic.
