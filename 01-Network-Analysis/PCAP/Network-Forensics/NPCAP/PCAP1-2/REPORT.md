# Wireshark Activity Write-up (Security Blue Team)

This repository contains my solutions and methodology for the **Security
Blue Team Wireshark Activity**. Each answer was obtained by analyzing
the provided PCAP files in Wireshark using display filters, statistics,
and protocol inspection.

------------------------------------------------------------------------

# PCAP 1

## Questions & Solutions

### 1. Which protocol was used over port 3942?

**Method**

-   Apply the filter:

``` text
tcp.port == 3942 || udp.port == 3942
```

-   Inspect the packet details or use **Decode As** if required.

**Answer**

> **SSDP**

------------------------------------------------------------------------

### 2. What is the IP address of the host that was pinged twice?

**Method**

Filter ICMP Echo Requests:

``` text
icmp.type == 8
```

Count the Echo Requests and identify the destination IP that appears
exactly twice.

**Answer**

> **8.8.4.4**

------------------------------------------------------------------------

### 3. How many DNS query response packets were captured?

**Method**

``` text
dns.flags.response == 1
```

Read the **Displayed** packet count from the status bar.

**Answer**

> **90**

------------------------------------------------------------------------

### 4. What is the IP address of the host which sent the most number of bytes?

**Method**

Navigate to:

    Statistics → Endpoints → IPv4

Sort by **Tx Bytes** to identify the host that transmitted the most
data.

**Answer**

> **115.178.9.18**

------------------------------------------------------------------------

# PCAP 2

## Questions & Solutions

### 1. What is the WebAdmin password?

**Method**

Inspect the HTTP authentication request.

    Follow → HTTP Stream

or search for:

``` text
password
```

**Answer**

> **sbt123**

------------------------------------------------------------------------

### 2. What is the version number of the attacker's FTP server?

**Method**

Filter:

``` text
ftp
```

Inspect the FTP banner.

Example:

``` text
220 pyftpdlib 1.5.5 ready.
```

**Answer**

> **pyftpdlib 1.5.5**

------------------------------------------------------------------------

### 3. Which port was used to gain access to the victim Windows host?

**Method**

Inspect TCP conversations and follow the relevant stream associated with
the compromise.

    Statistics → Conversations → TCP

**Answer**

> **8081**

------------------------------------------------------------------------

### 4. What is the name of a confidential file on the Windows host?

**Method**

Inspect the FTP directory listing or transferred files.

Search:

``` text
CONFIDENTIAL
```

**Answer**

> **Employee_Information_CONFIDENTIAL.txt**

------------------------------------------------------------------------

### 5. What is the name of the log file that was created at 4:51 AM on the Windows host?

**Method**

Inspect the FTP directory listing and locate the entry with timestamp
**04:51 AM**.

**Answer**

> **LogFile.log**

------------------------------------------------------------------------

# Skills Practiced

-   Wireshark Display Filters
-   Protocol Identification
-   ICMP Analysis
-   DNS Traffic Analysis
-   FTP Banner Enumeration
-   HTTP Credential Analysis
-   Endpoint Statistics
-   TCP Conversations
-   File Transfer Investigation

------------------------------------------------------------------------

# Tools Used

-   Wireshark
-   Display Filters
-   Follow TCP/HTTP Stream
-   Statistics → Endpoints
-   Statistics → Conversations
-   FTP Directory Listing Analysis

------------------------------------------------------------------------

**Repository:** https://github.com/vatsayu/SOC_Lab
