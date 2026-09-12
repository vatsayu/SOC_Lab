# Lab 01 – Configure a Wireless Router and Clients

**Packet Tracer File:** `4_4_4_Packet_Tracer_Configure_a_Wireless_Router_and_Client.pka`  
**Status:** Completed 100%  
**Difficulty:** Beginner  
**Topics Covered:** Physical cabling, DHCP, Home Wireless Router GUI, SSID, WPA2 security, wired + wireless client connectivity

---

## Objective

Build a complete home network by:
- Connecting coaxial and Ethernet cables correctly
- Configuring a home wireless router (DHCP limit, admin password, SSID, WPA2)
- Connecting both wired PCs and a wireless laptop
- Verifying internet access from all devices

---

## Topology Overview

- Cable company delivers internet + TV via coaxial
- Cable Splitter separates the signal
- Cable Modem provides internet to the Home Wireless Router
- Home Wireless Router acts as the center of the network (DHCP + Wireless AP + switch)
- Office PC and Bedroom PC → wired connections
- Laptop → wireless connection

---

## Step-by-Step Solution (How I Completed It)

### Part 1: Connect the Devices

#### 1.1 Coaxial Connections
1. Click **Connections** (lightning bolt icon).
2. Select **Coaxial** cable (blue zigzag).
3. Connect:
   - Cable Splitter `Coaxial1` → Cable Modem `Port 0`
   - Cable Splitter `Coaxial2` → TV `Port 0`
4. Click the TV → turn power **ON**.
   - Result: TV shows a program (confirms coaxial path is correct).

#### 1.2 Ethernet Connections
1. Select **Copper Straight-Through** cable.
2. Connect:
   - Cable Modem `Port 1` → Home Wireless Router `Internet` port
   - Office PC `FastEthernet0` → Home Wireless Router `GigabitEthernet 1`
   - Bedroom PC `FastEthernet0` → Home Wireless Router `GigabitEthernet 2`
3. All link lights turned green.

**Why this matters:**  
The modem must connect to the router’s **Internet** port so the router can get a public IP and share internet with the home network.

---

### Part 2: Configure the Wireless Router

#### 2.1 Access the Router GUI
1. Click **Office PC** → Desktop → **IP Configuration** → select **DHCP**.
2. Office PC received IP in the `192.168.0.0/24` range.
3. Default Gateway was `192.168.0.1`.
4. Open **Web Browser** → enter `192.168.0.1`.
5. Login with default credentials:
   - Username: `admin`
   - Password: `admin`

#### 2.2 Basic Settings
1. Under **Setup** tab → Network Setup:
   - Maximum Number of Users → changed to **10**
   - Clicked **Save Settings**
2. Under **Administration** tab:
   - New Router Password → `MyPassword1!`
   - Confirmed password and saved.
   - Re-logged in with the new password.

**Note:** After changing settings you may lose connection.  
Solution used: Toggle IP Configuration between Static ↔ DHCP to renew the address, then open the browser again.

#### 2.3 Configure Wireless LAN
1. Click **Wireless** tab.
2. For 2.4 GHz network:
   - Enabled the radio
   - Changed Network Name (SSID) to **MyHome**
   - Saved settings
3. Clicked **Wireless Security** sub-tab:
   - Security Mode → **WPA2 Personal**
   - Passphrase → `MyPassPhrase1!`
   - Saved settings

**Why WPA2 Personal?**  
It is the strongest security option available on this router for home use. The passphrase prevents unauthorized users from joining the network.

---

### Part 3: Configure Clients and Test Connectivity

#### 3.1 Connect the Laptop (Wireless)
1. Click **Laptop** → Desktop → **PC Wireless**.
2. Connect tab → selected network **MyHome**.
3. Entered Pre-shared Key: `MyPassPhrase1!`
4. Clicked Connect.
5. Link Information tab showed: “You have successfully connected to the access point”.
6. IP address started with `192.168.0.`.

#### 3.2 Test Internet Access
Opened Web Browser on all three devices and navigated to:
```
skillsforall.srv
```

- Office PC → Success
- Bedroom PC → Success (after setting it to DHCP)
- Laptop → Success

All devices could reach the internet.

---

## Key Commands / Actions Used

| Action                        | Location                          | Purpose                              |
|-------------------------------|-----------------------------------|--------------------------------------|
| DHCP                          | PC → IP Configuration             | Automatic IP addressing              |
| Fast Forward Time             | Bottom toolbar                    | Speed up DHCP and simulation         |
| Web Browser                   | PC Desktop                        | Access router GUI                    |
| PC Wireless                   | Laptop Desktop                    | Connect to Wi-Fi                     |
| Save Settings                 | Router GUI                        | Apply every configuration change     |

---

## What I Learned

- Difference between coaxial (TV/internet delivery) and Ethernet (data network).
- Home wireless routers combine: modem connection + switch + DHCP server + wireless access point.
- Always change default admin password.
- Limit DHCP pool size for better control.
- SSID is the network name people see; WPA2 + strong passphrase protects it.
- Wired and wireless clients can coexist on the same network and share the same DHCP pool.
- Fast Forward Time is very useful when DHCP takes time in Packet Tracer.

---

## Common Issues & How I Fixed Them

| Problem                              | Solution                                              |
|--------------------------------------|-------------------------------------------------------|
| Lost connection after saving settings | Toggle Static → DHCP on Office PC and re-open browser |
| TV shows no picture                  | Check coaxial cables and turn TV power ON             |
| Laptop cannot see MyHome network     | Make sure 2.4 GHz radio is Enabled and SSID is saved  |
| IP not starting with 192             | Click Fast Forward Time several times                 |

---

## Final Result

- All physical connections correct
- Router configured with limited DHCP, strong password, and secured Wi-Fi
- Wired PCs + Wireless Laptop all have internet access
- Activity completed with **100%** score

---

## Next Lab

→ Lab 02 – Connect to a Web Server (`8_1_3_Packet_Tracer_Connect_to_a_Web_Server.pka`)
