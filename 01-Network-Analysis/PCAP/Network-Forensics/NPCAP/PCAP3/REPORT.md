# PCAP 3 -- Wireshark Activity Write-up

## Objective

Investigate the supplied PCAP using Wireshark to identify the attacker,
determine the attack technique, inspect transferred files, recover
employee information, and identify compromised credentials.

------------------------------------------------------------------------

# Questions & Solutions

## 1. What is the MAC address of the attacker?

### Method

Filter ARP traffic:

``` text
arp
```

Look for duplicate IP warnings or suspicious unsolicited ARP replies.

Useful display filter:

``` text
arp.src.hw_mac == 0a:00:27:00:00:00
```

Packet details showed:

``` text
Duplicate IP address detected for 192.168.56.103
(08:00:27:3d:27:5d)
also in use by
08:00:27:10:b8:d0
```

### Answer

**08:00:27:3d:27:5d**

------------------------------------------------------------------------

## 2. What type of attack is taking place?

### Method

Inspect ARP packets for duplicate IP addresses and repeated ARP replies.

The attacker poisoned ARP tables to position themselves between the
client and the server.

### Answer

**Man-in-the-Middle (MITM) using ARP Spoofing/ARP Poisoning**

------------------------------------------------------------------------

## 3. What file was downloaded from the central server?

### Method

Filter:

``` text
ftp
```

Locate the FTP `RETR` command.

Example:

``` text
RETR Alevis_Employee_Information_Chart.csv
```

`RETR` indicates the requested file was downloaded.

### Answer

**Alevis_Employee_Information_Chart.csv**

------------------------------------------------------------------------

## 4. What department does Borden Danilevich work in?

### Method

Follow the FTP Data stream or inspect the downloaded CSV.

Search (`Ctrl + F`) for:

``` text
Borden
```

CSV entry:

``` text
Borden,Danilevich,bdanilevich83@oaic.gov.au,Sales,31.164.36.60,bdanilevich83,YKNBcV
```

The fourth column contains the employee's department.

### Answer

**Sales**

------------------------------------------------------------------------

## 5. What is the SSH password of the Domain Administrator?

### Method

Search the packet bytes for:

``` text
administrator
```

or

``` text
ssh
```

Inspect transferred files and recovered credentials until the Domain
Administrator password is located.

### Answer

**gMR\<4eXf\]e6W**

------------------------------------------------------------------------

# Key Wireshark Features Used

-   Display Filters
-   Follow TCP Stream
-   Follow FTP Data Stream
-   Statistics → Endpoints
-   Statistics → Conversations
-   Ctrl + F (Packet Bytes)
-   Protocol Hierarchy

------------------------------------------------------------------------

# Skills Practiced

-   ARP analysis
-   Detecting ARP spoofing
-   MITM investigation
-   FTP traffic analysis
-   Recovering transferred files
-   Credential discovery
-   CSV inspection
-   Network forensics

------------------------------------------------------------------------

Repository: https://github.com/vatsayu/SOC_Lab
