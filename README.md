# ThreatCluster digest

Every issue of the [ThreatCluster](https://threatcluster.io) threat intelligence digest, as Markdown.

Each issue sorts the day's security stories into sections (vulnerabilities, ransomware, breaches, threat actors and malware) and counts what is new on ransomware leak sites, which ThreatCluster collects from the sites directly. Stories link to the full record on threatcluster.io, where every source is listed.

| | |
|---|---|
| By email, free | <https://threatcluster.io/digest> |
| RSS | <https://threatcluster.io/digest/feed.xml> |
| On the web | <https://threatcluster.io/digest/archive> |
| As JSON | <https://threatcluster.io/api/digest/issues> |

The daily edition goes out at 06:00 UTC. The weekly edition goes out on Mondays.

## Issues

<!-- issues:start -->
| Date | Edition | Issue |
|---|---|---|
| 2026-10-20 | daily | [CVE-2026-112377: TLS Relay Vulnerability Disclosed (+7 more)](issues/2026/2026-10-20.md) |
| 2026-10-19 | daily | [Palo Alto Networks Firewalls Exploited Amid AI Security Concerns (+5 more)](issues/2026/2026-10-19.md) |
| 2026-10-19 | weekly | [AI-Driven Breach Exposes Data of 16 South Korean… (+8 more)](issues/2026/weekly-2026-10-19.md) |
| 2026-10-18 | daily | [Discover-Tech's AdFection Scheme Delivers Candiru Spyware via Ads (+6 more)](issues/2026/2026-10-18.md) |
| 2026-10-17 | daily | [PEERSTITCH Malware Compromises 500+ Firewalls via FortiManager… (+6 more)](issues/2026/2026-10-17.md) |
| 2026-10-16 | daily | [Critical Zero-Day Exploit Found in BeyondTrust Remote Support (+7 more)](issues/2026/2026-10-16.md) |
| 2026-10-15 | daily | [Critical Cisco Secure Email Gateway Vulnerability Exploited (+7 more)](issues/2026/2026-10-15.md) |
| 2026-10-14 | daily | [Ivanti Connect Secure Zero-Day Exploited: Urgent Patching Required (+5 more)](issues/2026/2026-10-14.md) |
| 2026-10-13 | daily | [Two Turkish Nationals Arrested Over Russian Sabotage of Starlink… (+4 more)](issues/2026/2026-10-13.md) |
| 2026-10-12 | daily | [CISA Adds 7 Flaws to KEV Amid Active Exploitation by Flax Typhoon (+6 more)](issues/2026/2026-10-12.md) |
| 2026-10-12 | weekly | [CISA Adds 7 Flaws to KEV Amid Active Exploitation by Flax… (+9 more)](issues/2026/weekly-2026-10-12.md) |
| 2026-10-11 | daily | [FBI Seizes Domains and Tools Used by Chinese Hackers (+5 more)](issues/2026/2026-10-11.md) |
| 2026-10-10 | daily | [Critical RCE Vulnerability in Cisco NX-API Disclosed (+6 more)](issues/2026/2026-10-10.md) |
| 2026-10-09 | daily | [Urgent CVE-2021-3199 Vulnerability in ONLYOFFICE Exploited in the Wild (+7 more)](issues/2026/2026-10-09.md) |
| 2026-10-08 | daily | [PoeLLM Malware Compromises 3,400+ AI Servers for Cryptomining (+7 more)](issues/2026/2026-10-08.md) |
| 2026-10-07 | daily | [GlassWorm Campaign Targets Developers with Malicious VS Code… (+1 more)](issues/2026/2026-10-07.md) |
| 2026-10-06 | daily | [ZITADEL Identity Provider Vulnerabilities Expose Critical… (+7 more)](issues/2026/2026-10-06.md) |
| 2026-10-05 | daily | [Bitget Suffers $388M Hack Attributed to North Korean Lazarus Group (+7 more)](issues/2026/2026-10-05.md) |
| 2026-10-05 | weekly | [Critical Citrix NetScaler Zero-Day Vulnerabilities… (+11 more)](issues/2026/weekly-2026-10-05.md) |
| 2026-10-04 | daily | [Critical Authentication Bypass in Rejetto HFS Exploited Within 24… (+7 more)](issues/2026/2026-10-04.md) |
| 2026-10-03 | daily | [Bitget Suffers $388 Million Hack Linked to North Korean Hackers (+6 more)](issues/2026/2026-10-03.md) |
| 2026-10-02 | daily | [Citrix NetScaler Critical Vulnerabilities Exploited: Urgent Patching… (+5 more)](issues/2026/2026-10-02.md) |
| 2026-10-01 | daily | [Apple Addresses CoreGraphics Zero-Day Vulnerability Amid (+7 more)](issues/2026/2026-10-01.md) |
| 2026-09-30 | daily | [New Spectre v2 Variant BTR Exposes CPUs to Data Leaks (+7 more)](issues/2026/2026-09-30.md) |
| 2026-09-29 | daily | [Citrix NetScaler Zero-Day Exploitation Targets Multiple Sectors (+7 more)](issues/2026/2026-09-29.md) |
<!-- issues:end -->

## How this repository is kept up to date

A scheduled GitHub Action runs [`scripts/mirror.py`](scripts/mirror.py), which reads the public archive API and adds a file for each new issue under `issues/<year>/`. The script uses only the Python standard library, so you can run it yourself:

```
python3 scripts/mirror.py
```

The website is the original; each file links back to its page there.

## About the content

Story summaries are generated from the source articles and can be wrong. Follow the link on any story to check it against its sources. Corrections are published at <https://threatcluster.io/corrections>.

Leak-site figures count listings that groups have published. A listing is a claim by the group, not confirmation of a breach.
