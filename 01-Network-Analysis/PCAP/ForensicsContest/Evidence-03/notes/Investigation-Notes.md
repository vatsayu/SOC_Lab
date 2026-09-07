 # Evidence-03 — Investigation Notes

## Target

```text
Challenge: ForensicsContest Puzzle #3 — Ann's AppleTV
AppleTV IP: 192.168.1.10
PCAP: evidence03.pcap
```

## Initial Host Filtering

Started by isolating the known AppleTV:

```text
ip.addr == 192.168.1.10
```

Then narrowed the traffic to HTTP GET requests:

```text
ip.addr == 192.168.1.10 && http.request.method == "GET"
```

---

## Q1 — MAC Address

Inspected the Ethernet header of AppleTV traffic.

Observed:

```text
00:25:00:fe:07:c4
```

Answer:

```text
00:25:00:fe:07:c4
```

---

## Q2 — User-Agent

Inspected HTTP request headers.

Observed:

```http
User-Agent: AppleTV/2.4
```

Answer:

```text
AppleTV/2.4
```

---

## Q3 — First Four Searches

Used:

```text
ip.addr == 192.168.1.10 && http.request.uri contains "incrementalSearch"
```

Found the following requests chronologically:

```http
GET /WebObjects/MZSearch.woa/wa/incrementalSearch?media=movie&q=h HTTP/1.1
```

```http
GET /WebObjects/MZSearch.woa/wa/incrementalSearch?media=movie&q=ha HTTP/1.1
```

```http
GET /WebObjects/MZSearch.woa/wa/incrementalSearch?media=movie&q=hac HTTP/1.1
```

```http
GET /WebObjects/MZSearch.woa/wa/incrementalSearch?media=movie&q=hack HTTP/1.1
```

Answer:

```text
h
ha
hac
hack
```

### Important observation

Requests beginning with:

```text
/b/ss/applesuperglobal/
```

were associated analytics requests. They were not counted as separate searches.

---

## Q4 — First Movie

After the `hack` search sequence, followed the related HTTP traffic and identified the first selected movie.

Answer:

```text
Hackers
```

---

## Q5 — Trailer URL

Located the movie metadata response and followed the HTTP stream.

The response was:

```text
Content-Type: text/xml
Content-Encoding: gzip
```

The decoded XML contained:

```text
preview-url
```

Recovered URL:

```text
http://a227.v.phobos.apple.com/us/r1000/008/Video/62/bd/1b/mzm.plqacyqb..640x278.h264lc.d2.p.m4v
```

---

## Q6 — Second Movie

Continued chronological analysis of the AppleTV movie-detail requests.

Second movie:

```text
Sneakers
```

---

## Q7 — Purchase Price

Located the movie metadata response.

The response was gzip-compressed XML, so the HTTP response needed to be decompressed/decoded.

Found:

```xml
<key>price-display</key><string>$9.99</string>
```

Answer:

```text
$9.99
```

---

## Q8 — Final Search Term

Filtered for incremental searches:

```text
ip.addr == 192.168.1.10 && http.request.uri contains "incrementalSearch"
```

The final search sequence included:

```text
iknowyourewa
iknowyourewatchingm
iknowyourewatching
iknowyourewatchingme
```

Final search:

```text
iknowyourewatchingme
```

---

## Final Answer Checklist

```text
[+] Q1  00:25:00:fe:07:c4
[+] Q2  AppleTV/2.4
[+] Q3  h, ha, hac, hack
[+] Q4  Hackers
[+] Q5  Apple trailer URL recovered
[+] Q6  Sneakers
[+] Q7  $9.99
[+] Q8  iknowyourewatchingme
```

## Lessons From Investigation

1. Filter by the known host first.
2. Separate primary application requests from analytics traffic.
3. Analyze HTTP requests chronologically.
4. Incremental APIs can expose user input character-by-character.
5. Important evidence may exist inside HTTP response bodies rather than headers.
6. Gzip compression may require HTTP stream reconstruction/decompression.
7. XML metadata can reveal application-level information such as media URLs and prices.

## Status

Puzzle #3 solved and ready for final reporting.

