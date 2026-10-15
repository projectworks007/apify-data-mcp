# Reed.co.uk Scraper — UK Jobs & Salaries, No Phones

Reed.co.uk Scraper gets job ads from reed.co.uk, one of the UK's largest job boards: title, company, whether it is a direct employer or a recruitment agency, location, the salary as reed shows it plus its minimum, maximum and period, contract type, full-time or part-time, remote, hybrid or on-site, when it was posted and when it closes, and on request the full ad, sector, skills, region and yearly salary. Paste your reed search links, or type a job title and a place. No phone numbers, e-mail addresses or recruiter names are delivered, and you pay only for jobs delivered.

## What data does Reed.co.uk Scraper extract?

For every job:

- `title`, `jobId`, `url`
- `company`, `companyType`, `companyJobsUrl`, `logo` – `employer`, `recruitment agency` or `charity or non-profit`
- `location`, `county`
- `salary`, `salaryMin`, `salaryMax`, `salaryPeriod`, `salaryCurrency` – reed's salary line and its numbers
- `contractType`, `hours`, `workplace`
- `postedAt`, `createdAt`, `expiresAt`
- `occupation`, `occupationGroup`
- `snippet` – the start of the ad
- `isPromoted`, `isFeatured`, `isEasyApply`, `isTrainingCourse`, `ukWorkRightRequired`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

With **Open every job for the full ad** also: `description`, `sector`, `sectorGroup`, `skills`, `town`, `region`, `country`, `postcodeArea`, `contractLength`, `salaryMinPerYear`, `salaryMaxPerYear`, `isGraduate`, `jobReference`, `isLive`, and `detailsError` for a job that went offline meanwhile (4 of 565 in a live run).

Training courses reed lists among the jobs (132 in 501 results in a live run) are left out unless you untick **Leave out training courses**.

## How to use Reed.co.uk Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from reed.co.uk, one per line, or type **Keywords** and **Places** ("accountant" in "Leeds"); every keyword is searched in every place. Choose distance, salary, contract type, hours, remote or hybrid and **Posted within**.
3. Set **Max jobs per search**, and tick **Open every job for the full ad** for the description, skills and sector.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new jobs, save the input as a task with **Posted within** set to 1 day and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Sales Administrator",
  "company": "RMLFS Limited",
  "companyType": "employer",
  "location": "Liverpool",
  "salary": "£25,000 - £28,000 per annum",
  "salaryMin": 25000,
  "salaryMax": 28000,
  "contractType": "permanent"
}
```

## How much does it cost?

**$0.0005 per job delivered, $0.50 per 1,000 jobs.** Opening jobs for the full ad costs nothing extra, only time (about 3.5 jobs a second). Links that are not reed searches and places reed does not know are free records.

Worked example: a live run read three searches (hybrid jobs in South East London, temporary jobs in Birmingham, accountants around Manchester from £35,000), 854 jobs in 15 seconds, for **$0.43**. 565 jobs with their full ads in 151 seconds cost $0.28.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/reed-jobs` to Claude, ChatGPT or any MCP client and the assistant can search reed with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Reed?

The Actor reads public job ads on reed.co.uk only. Companies and agencies are named; people are not. Reed takes phone numbers and e-mail addresses out of the ads itself; anything it misses is replaced with `[phone removed]` and `[e-mail removed]`, and sentences that name a recruiter are taken out of the ad text and the `snippet`. In five live runs with 3,415 full ads, a recruiter's name or e-mail address got through in 6 ads; the full ad is off by default. That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply on reed. You remain responsible for how you use the data and for reed's terms. This is an independent tool, not affiliated with Reed.

## FAQ

**How many jobs per search?** Reed shows at most the first 10,000 jobs of any search. A live run asked for all of London (21,058 jobs on reed) and got 9,998. For more, split the search by keyword, town or contract type.

**Are the filters obeyed?** Yes: reed applies them, and the run checks the salary range itself. In live runs, 299 of 299 remote software developer jobs were remote, and 88 of 88 jobs in a "permanent, from £30,000" search in Glasgow were permanent, none paid under £30,000 a year.

**Why does the same job show up in two of my searches?** Reed shows some nationwide "work from home" ads in many searches (9 came in both "nurse" in Manchester and "warehouse" in Leeds in a live run). Use `jobId` to drop them.

**Why no phone numbers or recruiter names?** They are personal data. Every job has its `url`; applicants apply on reed.

**Last updated:** 2026-10-15.

## Related Actors

- [Totaljobs & CWJobs Scraper](https://apify.com/highbrow_fame/totaljobs-jobs) – UK jobs with parsed salaries from Totaljobs and CWJobs
- [Job Bank Canada Scraper](https://apify.com/highbrow_fame/job-bank-canada-jobs) – Canada's government job board, in English or French
- [Remote Jobs Scraper](https://apify.com/highbrow_fame/remote-jobs-aggregator) – remote job ads

Useful? A short Store review helps — your feedback decides what we improve next.
