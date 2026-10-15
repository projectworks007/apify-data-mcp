---
title: Track new job postings from Naukri, StepStone and Job Bank Canada for a niche role (Python)
published: false
description: A Python script that pulls fresh job ads for one role from three national boards, de-duplicates them across days and appends the new ones to a CSV.
tags: abotwrotethis, python, webscraping, automation
---

> Disclosure: I built the Apify Actors used in this tutorial. This post was written with AI assistance and checked by me.

If you are watching the market for one specific role, say data engineer, across more than one country, the job boards' own alert e-mails give you one list per board, with no salary column and no record of what you have already seen. This tutorial replaces them with a Python script that runs once a day, asks three boards for recent postings, keeps only the ones it has not seen before, and appends them to a CSV you can sort and filter.

The three boards are India's Naukri.com, Germany's StepStone.de and Canada's Job Bank, each through an Apify Actor:

- [Naukri Jobs Scraper](https://apify.com/highbrow_fame/naukri-jobs): $0.0008 per job delivered ($0.80 per 1,000)
- [StepStone Scraper](https://apify.com/highbrow_fame/stepstone-jobs): $0.0009 per job delivered ($0.90 per 1,000)
- [Job Bank Canada Scraper](https://apify.com/highbrow_fame/job-bank-canada-jobs): $0.0008 per job delivered ($0.80 per 1,000)

All three charge only for jobs delivered. Unknown links, unknown places and empty searches come back as free records with a reason.

You need Python 3.9 or newer and an [Apify](https://apify.com) API token.

```bash
pip install apify-client
export APIFY_TOKEN=apify_api_xxxxxxxx
```

## 1. Two ways to get "only new jobs"

The boards differ in one thing that shapes the script.

**Job Bank Canada has a feed mode.** Set `onlyNewListings: true` and the Actor remembers every job it has delivered for that exact search in a key-value store in your Apify account, for 60 days per job. The first run returns everything; later runs return only jobs not seen before, each with a `firstSeenAt` timestamp, and seen jobs are neither saved nor charged.

**Naukri and StepStone do not**, so for those we use the boards' own date filter (`postedWithinDays`) to fetch only recent postings, and de-duplicate locally by job ID. The local de-duplication is applied to all three boards anyway: it is cheap, and it makes the script robust if you ever change a Job Bank filter (which resets its feed memory).

One detail that will bite you if you copy inputs between Actors: Naukri's `postedWithinDays` is a string (`"1"`, `"3"`, `"7"`, `"15"`, `"30"`), because it maps to Naukri's own freshness filter; StepStone's and Job Bank's are integers.

## 2. The search inputs

Each Actor accepts `keywords` plus a place. Naukri takes a list of `locations` and searches every keyword in every place; StepStone and Job Bank take a single `location` string.

```python
ROLE = "data engineer"

SEARCHES = {
    "naukri": ("highbrow_fame/naukri-jobs", {
        "keywords": [ROLE],
        "locations": ["Bangalore", "Hyderabad"],
        "postedWithinDays": "1",
        "sortBy": "date",
        "maxListingsPerSearch": 200,
    }),
    "stepstone": ("highbrow_fame/stepstone-jobs", {
        "keywords": [ROLE],
        "location": "Berlin",
        "radiusKm": 50,
        "postedWithinDays": 1,
        "sortBy": "newest",
        "includeRelatedJobs": False,
        "includeDetails": False,
        "maxJobsPerSearch": 200,
    }),
    "jobbank": ("highbrow_fame/job-bank-canada-jobs", {
        "keywords": [ROLE],
        "location": "Toronto",
        "sortBy": "newest",
        "onlyNewListings": True,
        "maxJobsPerSearch": 200,
    }),
}
```

Three settings deserve a comment:

- StepStone adds related jobs to keyword searches (for "data engineer" also backend and data science ads). `includeRelatedJobs: False` keeps only keyword matches; left on, every record carries a `match` field (`keyword` or `related`) for filtering later.
- StepStone opens every ad by default for the full text, contract type and its salary estimate. `includeDetails: False` skips that for speed; turn it on if you want the ad text.
- Job Bank reads the keyword as a job title, a keyword or an employer name. Multi-word phrases it does not recognise as a title return nothing (on the site as well). Test your phrase on jobbank.gc.ca first; if it finds nothing, use a single keyword.

## 3. Normalise the three record shapes

The boards return different field names. Pick the handful you want in the CSV and map each board to them:

```python
def normalize(board, j):
    if board == "naukri":
        return {
            "id": j.get("jobId"), "title": j.get("title"), "company": j.get("company"),
            "location": ", ".join(j.get("locations") or []),
            "salary": j.get("salary") or "", "posted": j.get("postedAt"), "url": j.get("url"),
        }
    if board == "stepstone":
        salary = ""
        if j.get("estimatedSalaryMin"):
            salary = (f"est. {j['estimatedSalaryMin']}-{j['estimatedSalaryMax']} "
                      f"{j.get('estimatedSalaryCurrency')}/{j.get('estimatedSalaryPeriod')}")
        return {
            "id": j.get("jobId"), "title": j.get("title"), "company": j.get("company") or "",
            "location": j.get("location"), "salary": salary,
            "posted": j.get("postedAt"), "url": j.get("url"),
        }
    return {  # jobbank
        "id": j.get("jobId"), "title": j.get("title"),
        "company": j.get("employer") or "(private household)",
        "location": f"{j.get('city')}, {j.get('province')}",
        "salary": j.get("salary") or "", "posted": j.get("postedDate"), "url": j.get("url"),
    }
```

What to expect in the salary column: Naukri shows the employer's figure when published (in one of my live runs about 60% of ads said "Not disclosed" and the parsed fields stayed empty). StepStone shows no employer salaries to logged-out visitors; you get StepStone's own estimate, which exists for most ads. Job Bank postings state the wage as written, with `salaryMin`, `salaryMax` and `salaryPeriod` parsed alongside.

## 4. Run, de-duplicate, append

```python
import csv, json, os, sys
from datetime import date
from pathlib import Path
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
SEEN, OUT = Path("seen.json"), Path("jobs.csv")
FIELDS = ["first_seen", "board", "id", "title", "company", "location", "salary", "posted", "url"]

seen = set(json.loads(SEEN.read_text())) if SEEN.exists() else set()
new_rows = []

for board, (actor_name, run_input) in SEARCHES.items():
    run = client.actor(actor_name).call(run_input=run_input)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        if item.get("status") not in (None, "OK"):
            print(f"{board}: {item.get('status')} {item.get('error')}", file=sys.stderr)
            continue
        row = normalize(board, item)
        key = f"{board}:{row['id']}"
        if key in seen:
            continue
        seen.add(key)
        new_rows.append({"first_seen": date.today().isoformat(), "board": board, **row})

write_header = not OUT.exists()
with OUT.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    if write_header:
        w.writeheader()
    w.writerows(new_rows)

SEEN.write_text(json.dumps(sorted(seen)))
print(f"{len(new_rows)} new postings, {len(seen)} known in total")
```

Notes on the code:

- `call()` blocks until the run ends. Three sequential runs of a few hundred jobs each take well under a minute apiece.
- Records with a `status` other than `OK` are the free "nothing found" records (an unknown place, an empty search); they go to stderr, not the CSV.
- `seen.json` is a flat list of `board:jobId` strings and grows only by the day's new postings. SQLite with a unique index on `(board, id)` is the natural upgrade.
- Job IDs are stable per board. An ad re-posted under a new ID shows up again, as it would on the board.

Put `SEARCHES` and `normalize` in the same file above this block, save it as `jobs.py`, and run it once by hand:

```bash
python jobs.py
```

The first run fills `jobs.csv` with everything the date filters allow (and, for Job Bank, everything in the search, because the first feed run returns all). From the second run on you see only new postings.

## 5. Run it daily

The simplest scheduler is cron on any machine that is on at the time:

```
0 8 * * *  cd /home/you/jobwatch && APIFY_TOKEN=apify_api_xxx /usr/bin/python3 jobs.py >> jobs.log 2>&1
```

A GitHub Actions workflow on a `schedule:` trigger works too if the job commits `seen.json` and `jobs.csv` back to the repository. Apify's own Schedules could run each Actor daily, but the cross-board de-duplication and the merged CSV live in this script, so the script is what needs scheduling.

If you also want a push notification, Job Bank's Actor accepts an `alertWebhookUrl` and POSTs a short JSON summary (new count, up to five sample items, dataset link) to Slack, Discord or any HTTPS endpoint whenever a feed run finds new jobs. For Naukri and StepStone, send your own message from the script when `new_rows` is not empty.

## What it costs

Worst case on the first day is 200 jobs from each of the four searches (two Naukri locations, StepStone, Job Bank), about 800 records, or roughly $0.66. After that the date filters and feed mode limit each day to recent postings: for a niche role in three cities, 20 to 60 records a day is realistic, a few cents. A month of daily runs stays around one to two dollars, inside the monthly usage credit on Apify's free plan.

## Limits worth knowing

- StepStone covers stepstone.de only; links to the Austrian or Belgian sites come back as a free record saying so.
- None of the Actors deliver recruiter names, phone numbers or e-mail addresses; every record has its `url`, and you apply on the board.
- A posting bumped or re-listed by the employer may appear as new again.
- The examples cap each search at 200 jobs. Raise the cap or split by city for a broad role.
- The data is for your own job search or market research; check each board's terms before redistributing it.

Full input schemas, example records and pricing are on the Actor pages: [Naukri](https://apify.com/highbrow_fame/naukri-jobs), [StepStone](https://apify.com/highbrow_fame/stepstone-jobs) and [Job Bank Canada](https://apify.com/highbrow_fame/job-bank-canada-jobs).
