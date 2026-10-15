# Totaljobs & CWJobs Scraper & API — UK Jobs & Salaries

Totaljobs & CWJobs Scraper gets UK job listings from Totaljobs and its sister site for IT and tech jobs, CWJobs: job title, company, location and postcode, the salary as written plus the parsed minimum, maximum, currency and period, posted date and a short snippet, and on request the full ad, contract type, on-site, hybrid or remote, industry and the date the ad runs until. Paste your Totaljobs or CWJobs search links, or type a keyword and a place. No recruiter names, phone numbers or e-mail addresses are delivered, and you pay only for jobs delivered.

## What data does Totaljobs & CWJobs Scraper extract?

For every job:

- `jobId`, `url`, `title`, `site` – `site` is Totaljobs or CWJobs
- `company`, `companyId`, `companyUrl`, `companyLogo` – the employer or recruitment agency (none when the ad is anonymous)
- `location`, `postcode`
- `salary`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` – the salary as written ("£30000 - £40000 per annum") and parsed (`year`, `month`, `week`, `day` or `hour`)
- `postedAt`, `featured`
- `match`, `snippet` – `keyword` or `related`, and the start of the ad text
- `input`, `position`, `scrapedAt`, `status`, `error`

With **Open every job ad** also: `description`, `contractType`, `workplace` (`on-site`, `hybrid` or `remote`), `workType`, `employmentType`, `industry`, `city`, `region`, `countryCode`, `validThrough`.

In a live run 1,253 of 1,301 jobs showed a salary and 746 of them became numbers; the rest said "Competitive", "Unspecified" or "Negotiable". The sites' own "posted within" filter lets older ads through (a "care assistant in Bristol, last 3 days" search listed 40 jobs, 32 of them older); the run checks the posting date and leaves those out.

## How to use Totaljobs & CWJobs Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from totaljobs.com or cwjobs.co.uk, one per line, or type **Keywords** and a **Place**, pick the **Site** and choose **Radius**, **Posted within (days)**, job type, direct employers or agencies, and newest first.
3. Set **Max jobs per search**, and tick **Open every job ad** if you need the full ads.
4. Leave the proxy on Apify's UK residential proxies, since the sites turn away data-centre requests.
5. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new jobs, save the input as a task with **Posted within (days)** set to 1 and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "site": "Totaljobs",
  "title": "Management Accountant",
  "company": "Marks Sattin (UK) Ltd",
  "location": "Bradford (BD1), BD1",
  "salaryMin": 48000,
  "salaryMax": 53000,
  "salaryPeriod": "year",
  "workplace": "hybrid"
}
```

## How much does it cost?

**$0.0012 per job delivered, $1.20 per 1,000 jobs.** Opening the job ads costs nothing extra, only time. Links that are not Totaljobs or CWJobs searches and places the site does not know are free records.

Worked example: a live run read three searches (CWJobs software developers, Totaljobs nurses around Manchester, HGV drivers around Leeds), 1,301 jobs in 70 seconds, for **$1.56**. 88 jobs with their full ads in 22 seconds cost $0.11.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/totaljobs-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Totaljobs and CWJobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Totaljobs?

The Actor reads public Totaljobs and CWJobs job listings only. Contact persons are not output, and phone numbers, e-mail addresses and recruiters' names written into the ads are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]` (in a live run of 46 ads: 5 phone numbers and 5 names). Companies and agencies keep their name. That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply on the site. You remain responsible for how you use the data and for the sites' terms. This is an independent tool, not affiliated with Totaljobs or CWJobs.

## FAQ

**How many jobs per search?** As many as the site lists, up to your maximum: in the live run the CWJobs software developer search stopped at the 1,000 set as the maximum, of 3,114.

**Why are some jobs outside the place I typed?** The site searches a radius around the place (**Radius**, 0 to 30 miles), so in a live run an accountant search in Leeds also brought jobs in Bradford. The `location` and `postcode` fields say where each job is.

**Why does a CWJobs job link go to totaljobs.com?** The two sites share their jobs; CWJobs itself links its jobs to totaljobs.com (all 1,000 in the live run), and the link opens the same ad.

**Why no recruiter names or phone numbers?** They are personal data. Every job has its `url`; you apply on the site.

**Last updated:** 2026-10-15.

## Related Actors

- [Reed.co.uk Scraper](https://apify.com/highbrow_fame/reed-jobs) – UK jobs and salaries from reed.co.uk
- [Job Bank Canada Scraper](https://apify.com/highbrow_fame/job-bank-canada-jobs) – Canada's government job board, in English or French
- [Remote Jobs Scraper](https://apify.com/highbrow_fame/remote-jobs-aggregator) – remote job ads

Useful? A short Store review helps — your feedback decides what we improve next.
