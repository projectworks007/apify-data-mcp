# Job Bank Canada Scraper + New Jobs Feed & Alerts, No Phones

Job Bank Canada Scraper gets job postings from Job Bank, the Government of Canada's job board (jobbank.gc.ca), in English or in French from Guichet-Emplois: title, employer, city and province, the salary as written and parsed, posted date, source, on-site, hybrid or remote and LMIA, and on request the full ad and the posting's details. Paste your Job Bank search links, or type keywords and a place. No phone numbers, e-mail addresses or contact persons are delivered, a feed mode returns only new jobs, and you pay only for jobs delivered.

## What data does Job Bank Canada Scraper extract?

For every job:

- `jobId`, `url`, `title`, `language` – `en` or `fr`
- `employer`, `privateHousehold` – empty for a private household (`true`)
- `city`, `province`, `location`, `distance`
- `salary`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`, `salaryNegotiable` – as written and parsed
- `postedDate`, `isNew`
- `source`, `sourceJobNumber`, `postedOnJobBank` – Job Bank itself or a partner board
- `workLocation`, `directApply`, `lmia`
- `greenJob`, `studentJob`, `apprenticeJob`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

With **Open every job posting** also: `description`, `originalTitle`, `employmentTerm`, `workHours`, `hoursPerWeek`, `workSchedule`, `startDate`, `vacancies`, `languages`, `education`, `experience`, `nocCode`, `validThrough`, `externalUrl`, `streetAddress` and `postalCode` (not for private households).

## How to use Job Bank Canada Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from jobbank.gc.ca or guichetemplois.gc.ca, one per line, or type **Keywords** and a **Place**, pick the **Language** and the filters (**Posted within (days)**, **Job source**, **Sort**…).
3. Set **Max jobs per search**, and tick **Open every job posting** if you need the full ads.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "accountant",
  "employer": "ATLANTIC BRIDGE INVESTMENTS (CANADA) INC.",
  "city": "North York",
  "province": "ON",
  "salary": "$42.00 hourly",
  "salaryMin": 42,
  "salaryPeriod": "hour",
  "source": "Job Bank"
}
```

## How much does it cost?

**$0.0008 per job delivered, $0.80 per 1,000 jobs.** Opening job postings costs nothing extra, only time (877 postings in 88 seconds in a live run). Links that are not Job Bank searches, places Job Bank does not know and searches with no jobs are free records.

Worked example: a live run read four searches, 1,104 jobs in 26 seconds, for **$0.88**. The 2,000 Ontario jobs of a week, read in 63 seconds, cost $1.60.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item it has delivered for this exact search. The first run returns everything; later runs with the same inputs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link; it works with Slack and Discord incoming webhooks and any HTTPS endpoint.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/job-bank-canada-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Job Bank with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Job Bank?

The Actor reads the public job postings on Job Bank and Guichet-Emplois only. Job Bank's "How to apply" block is not read; in partner ads, phone numbers, e-mail addresses and contact names are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]` (13, 71 and 9 of 641 partner ads in a live run). Private households' jobs come without the employer's name, street and postal code (`privateHousehold: true`). That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply on Job Bank. You remain responsible for how you use the data and for Job Bank's terms of use. This is an independent tool, not affiliated with Job Bank or the Government of Canada.

## FAQ

**How many jobs per search?** As many as Job Bank lists: a live run read 2,000 (its limit) of the 3,305 Ontario jobs posted in the last 7 days, in 63 seconds.

**Why is the employer empty on some jobs?** A private household, a family hiring a nanny or a caregiver, is hiring (173 of 2,000 Ontario jobs in a live run). Businesses, agencies and institutions keep their name.

**Why did my search find nothing?** Job Bank reads the words as a job title, a keyword or an employer name, so "python developer" finds none (on Job Bank too) while "python" found 187 jobs in a live run. Try a job title or one keyword.

**Why do jobs from partner boards show up?** Job Bank lists partner boards' jobs next to its own; `source` says which, and **Job source** picks one or the other.

**Last updated:** 2026-10-15.

## Related Actors

- [Reed.co.uk Scraper](https://apify.com/highbrow_fame/reed-jobs) – UK jobs and salaries
- [Totaljobs & CWJobs Scraper](https://apify.com/highbrow_fame/totaljobs-jobs) – UK jobs with parsed salaries
- [Remote Jobs Scraper](https://apify.com/highbrow_fame/remote-jobs-aggregator) – remote job ads

Useful? A short Store review helps — your feedback decides what we improve next.
