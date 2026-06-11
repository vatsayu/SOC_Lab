# Network Forensic Investigation: AIM Chat and File Exfiltration Analysis

## Executive Summary

This investigation reconstructs a covert Instant Messaging (IM) session conducted over an obfuscated protocol and recovers an exfiltrated Microsoft Word document (`recipe.docx`) containing sensitive corporate information. The analysis leverages packet capture (PCAP) examination in Wireshark to identify the communication partner, extract conversation transcripts, and carve the transferred file for forensic validation.

**Key Findings:**
1. **IM Buddy**: Sec558user1
2. **First Comment in IM Conversation**: "Here's the secret recipe... I just downloaded it from the file server. Just copy to a thumb drive and you're good to go >:-)"
3. **Transferred File**: `recipe.docx`
4. **File Magic Number**: `504B0304` (PK\x03\x04 - ZIP archive header, consistent with DOCX format)
5. **MD5 Hash**: `8350582774e1d4dbe1d61d64c89e0ea1`
6. **Secret Recipe Contents**: Detailed in the recovered document (a satirical "Recipe for Disaster" instructing sabotage via sugar in gas tanks).

The suspect utilized port 443 (typically HTTPS) to tunnel AIM traffic, evading standard protocol detection.

---

## Investigation Methodology

### 1. Initial Protocol Baseline Scouting
- Open the PCAP file in Wireshark.
- Navigate to **Statistics > Protocol Hierarchy** to establish a high-level overview of network traffic.
- Identify dominant protocols and note the prevalence of SSL/TLS traffic on port 443, which initially masked the underlying AIM (AOL Instant Messenger) protocol.

### 2. Identifying the Port Trap (Defense Evasion Technique)
- Apply initial display filters for AIM-related traffic (e.g., `aim`).
- Observe zero results due to protocol obfuscation.
- Confirm the chat software was configured to operate over port 443, causing Wireshark to classify packets as encrypted SSL/TLS.

### 3. Overriding Decoder Framework (Decode As)
- Select a TCP packet on port 443.
- Right-click and choose **Decode As...**
- Force the protocol decoder to **AIM** for the selected port.
- This reveals cleartext AIM parameters, buddy names, and message contents in the packet details pane.

### 4. Reconstructing Session Streams
- Apply the display filter: `tcp.stream eq 2` (or appropriate stream index identified via conversation analysis).
- Right-click a packet in the stream and select **Follow > TCP Stream**.
- This reconstructs the full application-layer transcript of the IM conversation.

**Alternative Approach**:
- Use `tcp.port == 443` combined with manual stream following for comprehensive session reconstruction.

---

## File Transfer Recovery and Carving

### 5. Locating the File Transfer
- Apply the display filter: `tcp contains "recipe.docx"` (or `tcp contains "reciepe.docx"` accounting for possible typos in traffic).
- Identify the TCP stream containing the binary file transfer (typically **stream 5**).
- Right-click and select **Follow > TCP Stream**.
- In the TCP Stream window, switch the display format to **Raw** to view the binary payload.

### 6. Saving the Raw Payload
- In the TCP Stream dialog, click **Save As...**
- Save the raw stream data as `recipe.raw` (or similar).

### 7. Hex Editor Analysis and File Carving
- Open the saved raw file in a hex editor (e.g., `hexedit`, HxD, Bless, or 010 Editor).
- Locate the DOCX/ZIP magic number signature: `50 4B 03 04` (first four bytes of a valid ZIP archive).
- Remove any preceding protocol headers, AIM framing, or extraneous bytes before the magic number.
- Scan for and truncate trailing garbage data after the end of the ZIP structure (often indicated by the `50 4B 05 06` central directory end signature).
- Save the cleaned binary as `recipe.docx`.

**Verification Steps in Hex Editor**:
- Confirm the first four bytes are exactly `504B0304`.
- Validate the overall file structure resembles a standard Office Open XML (OOXML) package.

### 8. Hash Verification
- Compute the MD5 hash of the carved `recipe.docx`:
  ```bash
  md5sum recipe.docx