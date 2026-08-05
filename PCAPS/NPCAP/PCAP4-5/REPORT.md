# Security Blue Team -- PCAP 4 & PCAP 5 Write-up

## PCAP 4

### 1. How many UDP packets have been captured?

**Wireshark Filter**

``` text
udp
```

**Answer:** **3290**

------------------------------------------------------------------------

### 2. How many TCP packets have both the SYN and ACK flags set?

**Wireshark Filter**

``` text
tcp.flags.syn == 1 && tcp.flags.ack == 1
```

**Answer:** **20**

------------------------------------------------------------------------

### 3. Which version of Chrome was used to connect to `securityblue.team`?

**Wireshark Filter**

``` text
http.host contains "securityblue.team"
```

Inspect the **User-Agent** header.

**Answer:** **Chrome/80.0.3987.87**

------------------------------------------------------------------------

### 4. How many packets have a TTL value of 38?

**Wireshark Filter**

``` text
ip.ttl == 38
```

**Answer:** **710**

------------------------------------------------------------------------

# PCAP 5

### 1. What is the name of the PNG file on the webserver at `192.168.56.111`?

**Wireshark Filter**

``` text
ip.addr == 192.168.56.111 && http
```

**Answer:** **proprietary.png**

------------------------------------------------------------------------

### 2. Which version of OpenSSH is running on the server?

**Wireshark Filter**

``` text
ssh
```

Inspect the **Server Version String**.

**Answer:** **OpenSSH_7.9p1**

------------------------------------------------------------------------

### 3. On which port is the `.zip` file being served?

Inspect the TCP stream carrying the ZIP file.

**Answer:** **TCP Port 3016**

------------------------------------------------------------------------

### 4. When was a packet with a TCP checksum value of 53203 captured?

**Filter**

``` text
tcp.checksum == 0xcfd3
```

**Answer:** **11:04:46.207925**

(Original UTC timestamp: `2020-02-10T11:04:46.207925000Z`)

------------------------------------------------------------------------

## Repository

GitHub Repository: https://github.com/vatsayu/SOC_Lab
