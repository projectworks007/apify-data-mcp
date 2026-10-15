# BestJobs Scraper — Romania Jobs & Salaries, No Phones

BestJobs Scraper gets job ads from BestJobs (bestjobs.eu), one of Romania's big job boards: title, company, towns, the salary in euros (the employer's range or BestJobs' own estimate), employment type, experience level, remote or hybrid, languages asked for, benefits, number of applicants and the full ad text. Paste your BestJobs search links, or type keywords and towns. No phone numbers, e-mail addresses or contact persons are delivered, and you pay only for jobs delivered.

## What data does BestJobs Scraper extract?

For every job:

- `title`, `jobId`, `url`
- `company`, `companyLogo`, `companyRating`, `companyHidden` – who is hiring; `companyHidden` is true for a confidential employer
- `locations`, `cities` – the places as the employer entered them, and just the towns
- `remote`, `hybrid`, `relocation`
- `salary`, `salaryMin`, `salaryMax` – the employer's salary as shown ("1100 - 1600") and in numbers
- `estimatedSalaryMin`, `estimatedSalaryMax` – BestJobs' estimate when the employer gave none
- `salaryCurrency`, `salaryPeriod` – EUR, month (BestJobs shows net monthly salaries)
- `applicants`, `listingState` – how many applied; `active`, or `passive` for an "Interesat" listing
- `applyUrl` – the employer's own application page, when there is one
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

With **Full job ad and details** (on by default) also:

- `description` – the full ad as plain text, without contact persons, phones and e-mails
- `employmentTypes` – full-time, part-time, internship, project, volunteer
- `careerLevels` – no-experience, entry, middle, senior, executive
- `languages` – with level ("Engleză", "Avansat")
- `benefits`, `skills`, `vacancies`, `views`, `companyUrl`

## How to use BestJobs Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from bestjobs.eu, one per line, or type **Keywords** and/or **Places**. Every keyword is searched in every place; a keyword alone searches all of Romania, a place alone gives all its jobs.
3. Optionally pick **Employment type**, **Experience level**, **Spoken language**, **Remote jobs only**, the **Order**, and whether remote jobs may appear in town searches.
4. Set **Max jobs per search**, and turn off **Full job ad and details** if the list fields are enough (about four times faster).
5. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. For a daily feed, save the input as a task with **Order** set to "Newest first" and schedule it every morning.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Economist",
  "company": "MYOMOBILE TRADING",
  "cities": ["Timișoara"],
  "salaryMin": 1100,
  "salaryMax": 1600,
  "salaryCurrency": "EUR",
  "careerLevels": ["middle", "senior"]
}
```

## How much does it cost?

**$0.0012 per job delivered, $1.20 per 1,000 jobs.** The full ad and details cost nothing extra, only time. Links that are not BestJobs searches, places BestJobs does not know and searches without jobs are free records.

Worked example: a live run read Timișoara (full-time, newest first), "sofer" and "customer support" with German, 2,470 jobs with full ads in 218 seconds, for **$2.96**. All 1,891 jobs of Cluj-Napoca cost $2.27.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/bestjobs-ro-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Romanian jobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape BestJobs?

The Actor reads the public job listings of bestjobs.eu. Companies are named, people are not: contact persons, phone numbers (also in employers' address lines) and e-mail addresses are removed from the ads. In three test runs of 11,264 jobs, no phone number or e-mail address was left. That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply on BestJobs. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with BestJobs.

## FAQ

**How many jobs per search?** As many as BestJobs lists, up to your maximum. Cluj-Napoca gave 1,891 jobs in a live run. A search with neither keyword nor place ends after about 6,600 jobs (6,612 in a live run), BestJobs' own limit; search town by town or by keyword to go further.

**Are the salaries gross or net?** BestJobs asks employers for the net monthly salary in euros and shows its estimate in the same unit. In the live runs 1,606 of 4,036 jobs had the employer's range and 1,703 more had the estimate.

**Can I use the category filter (IT, sales …)?** No. BestJobs turns down category searches from outside its own pages (status 403); use a keyword instead.

**Is there a posting date?** No, BestJobs does not show one. Use **Order: Newest first**.

**Why are there remote jobs in my town search?** BestJobs adds remote-only jobs to a town's results (733 of 1,891 in Cluj-Napoca). Turn off **Include remote jobs in place searches** to keep only jobs located in the town.

**Last updated:** 2026-10-15.

## Related Actors

- [Jobs.cz & Prace.cz Scraper](https://apify.com/highbrow_fame/jobs-cz-jobs) – Czech jobs and salaries
- [Profession.hu Scraper](https://apify.com/highbrow_fame/profession-hu-jobs) – Hungarian jobs and salaries
- [MojPosao Scraper](https://apify.com/highbrow_fame/mojposao-jobs) – Croatian job ads with full text

Useful? A short Store review helps — your feedback decides what we improve next.
