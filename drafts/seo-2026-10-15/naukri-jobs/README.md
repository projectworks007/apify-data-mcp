# Naukri Jobs Scraper — India Jobs, Salary in Lakhs, Skills

Naukri Jobs Scraper gets job ads from naukri.com, India's largest job board: title, company or placement consultant, experience range, salary as naukri shows it plus its minimum and maximum in rupees and lakhs, locations, office / hybrid / remote, skills, posting date, walk-in dates and company rating, and on request the full ad, role, industry, education and applicants. Paste naukri search links or type a job title and a city. No phone numbers or recruiter names, and you pay only for jobs delivered.

## What data does Naukri Jobs Scraper extract?

For every job:

- `title`, `jobId`, `url`
- `company`, `companyId`, `companyJobsUrl`, `logo` – who posted it
- `postedBy`, `hiringFor` – `company` or `consultant`; a consultant's client label
- `experience`, `experienceMin`, `experienceMax` – naukri's experience line and its years
- `salary`, `salaryMin`, `salaryMax`, `salaryMinLakhs`, `salaryMaxLakhs`, `salaryCurrency`, `salaryPeriod` – naukri's salary line and its numbers (INR a year)
- `locationText`, `locations`, `workplace` – cities, and `office` / `hybrid` / `remote`
- `skills`
- `postedAt`, `postedAgo`
- `vacancies`, `isWalkIn`, `walkInDates`, `appliesOnCompanySite`
- `companyRating`, `companyReviews`
- `snippet`
- `input`, `position`, `scrapedAt`, `status`, `error`

With **Open every job for the full ad** also: `description`, `role`, `roleCategory`, `department`, `industry`, `employmentType`, `educationUG`, `educationPG`, `educationDoctorate`, `keySkills`, `otherSkills`, `localities`, `hybridDetail`, `applicants`, `views`, `walkIn`, `companyWebsite` and `detailsError`.

## How to use Naukri Jobs Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from naukri.com with every filter set, one per line, or type **Keywords** and **Places** (every keyword is searched in every place) and choose the filters.
3. Set **Max jobs per search**, and tick **Open every job for the full ad** if you need the description, role, industry, education and applicants.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new jobs, set **Freshness** to "Last 1 day" and schedule the task daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Walk-in || Phone Banking Officer (Customer Care Executive )",
  "company": "Hdfc Bank",
  "salary": "2.25-3 Lacs PA",
  "salaryMinLakhs": 2.25,
  "salaryMaxLakhs": 3,
  "locations": ["Hyderabad"],
  "isWalkIn": true
}
```

## How much does it cost?

**$0.0008 per job delivered, $0.80 per 1,000 jobs.** Full ads cost nothing extra, only time (900 jobs with full ads in 236 seconds in a live run). Links that are not naukri searches and places naukri does not know come back as free records with the reason.

Worked example: a live run read four searches (data analysts in Hyderabad, hybrid or remote jobs in Pune, sales jobs at 50 lakhs and more, accountant jobs in Mumbai), 5,219 jobs in about 2 minutes, for **$4.18**. All 11,480 python developer jobs in Bangalore cost $9.18.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/naukri-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Indian jobs with this Actor's input fields, paying per job delivered at the same rate.

## Is it legal to scrape Naukri?

The Actor reads public job ads on naukri.com. Companies and agencies are named by company only. The walk-in contact person and phone that naukri keeps with a job are never read; phone numbers and e-mail addresses in the ads become `[phone removed]` and `[e-mail removed]`, and the sentences and sign-off lines that name a recruiter ("HR Contact Person: …", "Regards, / <name>") are taken out. Rules can miss an unusual wording: in the last two live runs with 1,920 full ads, a recruiter's first name got through in 3 jobs, which is why the full ad is off by default. That keeps the output to job-market data rather than personal data under GDPR; every job has its `url`, and applicants apply on naukri. You remain responsible for your use of the data and the site's terms. This is an independent tool, not affiliated with Naukri.com or Info Edge.

## FAQ

**How many jobs per search?** As many as the search has: naukri lets a search be read to its last page. A live run read "python developer" in Bangalore to the end, 11,480 of the 11,709 jobs naukri counted, in 7.5 minutes.

**Are the filters obeyed?** Yes, and the run checks the salary bands itself. In one live run, 405 of 405 data analyst jobs from a "last 15 days" link were posted within 15 days, 2,000 of 2,000 "hybrid or remote" jobs were hybrid or remote, and 486 of 486 shown salaries in a "10-15 and 15-25 lakhs" link were in those bands.

**How many jobs show a salary?** When the employer hides the pay ("Not disclosed"), 3,141 of 5,219 jobs in a live run, the salary fields stay empty.

**What if naukri does not know my place?** naukri quietly ignores it and shows jobs from all of India; the run checks every place first and returns a free `NOT_FOUND` record instead.

**Last updated:** 2026-10-15.

## Related Actors

- [Naukrigulf Scraper & API](https://apify.com/highbrow_fame/naukrigulf-jobs) – Gulf jobs and salaries in local currency and USD
- [Foundit Scraper](https://apify.com/highbrow_fame/foundit-jobs) – Monster India jobs, Gulf and Asia
- [Rozee.pk Scraper](https://apify.com/highbrow_fame/rozee-jobs) – Pakistan jobs and salaries

Useful? A short Store review helps — your feedback decides what we improve next.
