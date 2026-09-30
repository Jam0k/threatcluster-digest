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
