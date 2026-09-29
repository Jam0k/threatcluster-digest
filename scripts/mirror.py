#!/usr/bin/env python3
"""Copy each issue of the ThreatCluster digest into this repository as Markdown.

Reads the public archive API, writes one file per issue under issues/<year>/,
and rebuilds the list in README.md. Issues already on disk are left alone, so
the script can run as often as you like. Standard library only.

    python3 scripts/mirror.py            # fetch what is missing
    python3 scripts/mirror.py --all      # rewrite every issue
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date

SITE = "https://threatcluster.io"
API = f"{SITE}/api/digest/issues"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENT = "threatcluster-digest-mirror (+https://github.com/Jam0k/threatcluster-digest)"
START, END = "<!-- issues:start -->", "<!-- issues:end -->"


def get(url: str) -> dict:
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            last = e
        except Exception as e:  # network trouble: wait and try again
            last = e
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"could not read {url}: {last}")


def long_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.strftime('%A')} {d.day} {d.strftime('%B %Y')}"


def path_for(issue_id: str, iso: str) -> str:
    return os.path.join("issues", iso[:4], f"{issue_id}.md")


def title_for(edition: str, iso: str) -> str:
    label = "ThreatCluster weekly digest" if edition == "weekly" else "ThreatCluster digest"
    prefix = "week to " if edition == "weekly" else ""
    return f"{label}, {prefix}{long_date(iso)}"


def clean(text) -> str:
    return " ".join(str(text or "").split())


def render(issue: dict) -> str:
    url = f"{SITE}/digest/archive/{issue['id']}"
    out = [f"# {title_for(issue['edition'], issue['date'])}", "",
           f"Originally published at <{url}>.", ""]
    for section in issue.get("sections") or []:
        out += [f"## {clean(section.get('title'))}", ""]
        for story in section.get("stories") or []:
            title = clean(story.get("title")).replace("[", "(").replace("]", ")")
            link = story.get("url") or ""
            out.append(f"### [{title}]({link})" if link.startswith("https://") else f"### {title}")
            out += ["", clean(story.get("summary")), ""]
            detail = []
            if story.get("sources"):
                detail.append(f"{story['sources']} sources")
            if story.get("score"):
                detail.append(f"score {story['score']}")
            if story.get("entities"):
                detail.append(", ".join(clean(e) for e in story["entities"]))
            if detail:
                out += [f"*{' · '.join(detail)}*", ""]
    leak = issue.get("leak_sites")
    if leak and leak.get("victims"):
        window = "7 days" if (leak.get("hours") or 24) >= 168 else "24 hours"
        out += ["## New on leak sites", "",
                f"{leak['victims']} organisations were listed on ransomware leak sites in the last "
                f"{window}, by {leak.get('group_total') or len(leak.get('groups') or [])} groups. "
                "ThreatCluster collects these from the sites directly.", ""]
        if leak.get("groups"):
            out += ["| Group | New listings |", "|---|---|"]
            out += [f"| [{clean(g['name'])}]({SITE}/dark-web/group/"
                    f"{urllib.request.quote(clean(g['name']).lower(), safe='')}) | {g['count']} |"
                    for g in leak["groups"]]
            out.append("")
    if issue.get("moving"):
        out += ["## Also moving", ""] + [f"- {clean(m)}" for m in issue["moving"]] + [""]
    out += ["---", "",
            f"Get the digest by email, free: <{SITE}/digest>. RSS: <{SITE}/digest/feed.xml>.", ""]
    return "\n".join(out)


def rebuild_readme(listing: list) -> None:
    path = os.path.join(ROOT, "README.md")
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        return
    rows = ["| Date | Edition | Issue |", "|---|---|---|"]
    for item in listing:
        rel = path_for(item["id"], item["date"]).replace(os.sep, "/")
        if os.path.exists(os.path.join(ROOT, rel)):
            subject = re.sub(r"^This week:\s*", "", clean(item.get("subject"))).replace("|", "/")
            rows.append(f"| {item['date']} | {item['edition']} | [{subject}]({rel}) |")
    block = START + "\n" + "\n".join(rows) + "\n" + END
    new = text[:text.index(START)] + block + text[text.index(END) + len(END):]
    if new != text:
        open(path, "w", encoding="utf-8").write(new)


def main() -> None:
    rewrite = "--all" in sys.argv
    listing, offset = [], 0
    while True:
        page = get(f"{API}?limit=100&offset={offset}")
        listing += page.get("issues") or []
        offset += 100
        if offset >= (page.get("total") or 0) or not page.get("issues"):
            break
    written = 0
    for item in listing:
        rel = path_for(item["id"], item["date"])
        full = os.path.join(ROOT, rel)
        if os.path.exists(full) and not rewrite:
            continue
        issue = get(f"{API}/{item['id']}")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8").write(render(issue))
        written += 1
        print("wrote", rel)
        time.sleep(1)
    rebuild_readme(listing)
    print(f"{len(listing)} issues in the archive, {written} written")


if __name__ == "__main__":
    main()
