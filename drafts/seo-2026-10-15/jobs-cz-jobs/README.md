# Jobs.cz & Prace.cz Scraper — Czech Jobs & Salaries, No Phones

Jobs.cz & Prace.cz Scraper gets job ads from Jobs.cz and Prace.cz, the two biggest Czech job boards: title, company, place, the salary parsed into minimum, maximum and period, on-site, hybrid or remote, posting date, professions and fields, and on request the full ad text with the education and languages asked for, contract, benefits and workplace address. Paste search links from either site, or type keywords and places; a job found on both boards is delivered once. No contact persons, phone numbers or e-mail addresses are delivered, and you pay only for jobs delivered.

## What data does Jobs.cz & Prace.cz Scraper extract?

For every job:

- `title`, `jobId`, `url` – `jobId` is Jobs.cz's number, which Prace.cz uses too
- `source`, `praceAdId` – `jobs.cz` or `prace.cz`
- `company`
- `location`, `extraLocations`
- `salary`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` – as shown and in numbers
- `workplace` – `on-site`, `hybrid` or `remote`
- `postedDate`, `postedAt`, `validTo`, `dateLabel`, `isPromoted`
- `employmentTypes` – `full-time`, `part-time`, `temporary`, `internship`
- `professions`, `fields`, `suitableFor`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

With **Full job ad and details** also: `description` (without contact persons, phones and e-mails), `detailsFrom` (`jobs.cz`, `prace.cz` or `career site`), `educationRequired`, `languages`, `contractTypes` (`employment`, `freelance`, `agreement`), `employmentText`, `employmentDuration`, `employerType`, `benefits`, `workplaceAddress`, `firstPostedAt`.

In a live run 1,666 of 3,515 jobs showed a salary.

## How to use Jobs.cz & Prace.cz Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from jobs.cz or prace.cz, one per line, or type **Keywords** and/or **Places** (Brno, Praha, Jihomoravský kraj) and choose the **Job board** (Jobs.cz, Prace.cz or both). Every keyword is searched in every place; a keyword alone searches the whole Czech Republic.
3. Optionally pick a **Radius**, **Posted within**, **Minimum salary** and the other filters.
4. Set **Max jobs per search**, and turn on **Full job ad and details** if you need the text.
5. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. For a daily feed, save the input as a task with **Posted within** set to the last 24 hours and schedule it every morning.

## Example output

Values are examples, shortened from a live run:

```json
{
  "source": "jobs.cz",
  "title": "Samostatná účetní bez nutnosti AJ — DEK a.s.",
  "company": "DEK a.s.",
  "location": "Praha – Malešice",
  "salaryMin": 45000,
  "salaryMax": 60000,
  "salaryCurrency": "CZK",
  "workplace": "hybrid"
}
```

## How much does it cost?

**$0.0009 per job delivered, $0.90 per 1,000 jobs.** The full ad and details cost nothing extra, only time (400 ads in 155 seconds in a live run). Links that are not Jobs.cz or Prace.cz searches, places Jobs.cz does not know and searches without jobs are free records.

Worked example: a live run read three searches, 3,515 jobs in 85 seconds, for **$3.16**. The 10,000 jobs Prace.cz shows of its whole list, read in 336 seconds, cost $9.00.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/jobs-cz-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Czech jobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Jobs.cz?

The Actor reads the job ads Jobs.cz and Prace.cz publish on their websites. Companies are named; people are not. The site's contact block is never read, and contact lines, names after "paní/pan", titles and names ("Mgr. …"), phone numbers and e-mail addresses are taken out of the ad text. A sole trader's name is kept as the site publishes it. That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply through the site or the employer. You remain responsible for how you use the data and for the sites' terms. This is an independent tool, not affiliated with Jobs.cz, Prace.cz or Alma Career.

## FAQ

**How many jobs per search?** Jobs.cz shows at most 45 pages, 1,350 jobs, of any search: a live run of all of Praha (8,340 jobs found) delivered those 1,350. Prace.cz shows up to 250 pages, 10,000 jobs.

**Why do Jobs.cz and Prace.cz give different jobs?** They are separate boards with different ads: "řidič" around Ostrava found 84 jobs on Jobs.cz and 119 on Prace.cz, only 38 on both, and the run delivered 165, each once. With **Job board → Both**, a job found on both comes from Jobs.cz.

**Why is the salary empty for some jobs?** The employer chose not to show it; this scraper does not deliver what the site does not show. With **Minimum salary**, a job whose shown monthly salary is entirely below it is left out.

**Why do some Jobs.cz jobs have no `postedDate`?** Jobs.cz labels promoted ads "Příležitost dne" and ads about to end "Končí za 3 dny" instead of a date; those have `validTo` or `isPromoted` instead. Prace.cz jobs always have `postedAt`.

**Last updated:** 2026-10-15.

## Related Actors

- [BestJobs Scraper](https://apify.com/highbrow_fame/bestjobs-ro-jobs) – Romanian jobs and salaries
- [Profession.hu Scraper](https://apify.com/highbrow_fame/profession-hu-jobs) – Hungarian jobs and salaries
- [No Fluff Jobs Scraper](https://apify.com/highbrow_fame/nofluffjobs-jobs) – IT jobs across Central and Eastern Europe

Useful? A short Store review helps — your feedback decides what we improve next.
