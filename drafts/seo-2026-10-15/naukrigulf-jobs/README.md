# Naukrigulf Scraper & API — Gulf Jobs & Salaries, No Phones

Naukrigulf Scraper gets job ads from naukrigulf.com, the Gulf's big job board (UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain and more): title, company, whether a company or a recruitment consultant posted it, experience range, the salary as written plus its minimum and maximum in local currency and in US dollars, city and country, skills, summary, posting date, industry, department, education, nationality and employment type, and on request the full ad, the candidate profile and the company profile. Paste your naukrigulf search links, or just type a job title and a city. No phone numbers or recruiter names are delivered, and you pay only for jobs delivered.

## What data does Naukrigulf Scraper extract?

For every job:

- `title`, `jobId`, `url`
- `company`, `companyId`, `logo`, `companyWebsite`
- `postedBy`, `isConfidentialCompany` – `company` or `consultant` (a recruitment agency posting for a client); employers that hide their name
- `experience`, `experienceMin`, `experienceMax` – "5-10 years" and its years
- `salary`, `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` – the pay as written ("AED 5,300 - 8,900 a month"), its numbers, currency and period; empty when the employer hides it
- `salaryUsdMin`, `salaryUsdMax` – the same pay in US dollars, as naukrigulf converts it
- `locationText`, `locations`, `country`, `localities` – as shown, as a list of cities, the country, and areas such as "Business Bay"
- `workplace`, `employmentType` – `office` / `remote` / `hybrid`; full-time, part-time …
- `skills`, `summary`, `highlights`
- `industry`, `department`, `education`, `nationality`, `gender`
- `postedAt`, `vacancies`, `expiringSoon`, `isExpired`
- `isWebJob`, `appliesOnCompanySite`, `isTopEmployer`, `isFeaturedEmployer` – a "web job" naukrigulf lists from elsewhere, and naukrigulf's employer badges
- `input`, `position`, `scrapedAt`, `status`, `error`

With **Add the full job ad** also: `description`, `candidateProfile` and `companyProfile`; a job gone offline between the search and its page comes with `detailsError` instead.

## How to use Naukrigulf Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from naukrigulf.com, one per line, or type **Keywords** and **Places** ("accountant" in "Dubai"; every keyword is searched in every place) and choose experience, freshness, salary bands, "posted by" and the sort order.
3. Set **Max jobs per search**, and tick **Add the full job ad** if you need the description, the candidate profile and the company profile.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new jobs, save the input as a task with **Freshness** set to "Last 1 day" and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "BIM Modeler MEP",
  "company": "FALCON SURVEY ENGINEERING CONSULTANTS",
  "postedBy": "company",
  "experience": "5-10 years",
  "locations": ["Dubai"],
  "salary": "AED 5,300 - 8,900 a month",
  "salaryUsdMin": 1432,
  "salaryUsdMax": 2404
}
```

## How much does it cost?

**$0.0009 per job delivered on the Apify Free plan, $0.90 per 1,000 jobs**; paid plans are lower, down to $0.63 per 1,000 on Gold and above. Every job is opened on naukrigulf for its salary and details, and the full ad costs nothing extra. Links that are not naukrigulf searches and places naukrigulf does not know are free records.

Worked example: a live run read four searches (every job in Saudi Arabia from the last 15 days, UAE engineer jobs paying $2,001-4,000 a month for 5 years' experience, UAE accountant jobs from consultants, nurse jobs in Kuwait), 3,773 jobs with their full ads in 8.6 minutes, for **$3.40** on the Free plan.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/naukrigulf-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Gulf jobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Naukrigulf?

The Actor reads public job ads on naukrigulf.com only. Companies are named as naukrigulf publishes them; the contact block naukrigulf keeps with each job (the recruiter's name, title, address, phone and e-mail) is never read. In the ads, phone numbers and e-mail addresses become `[phone removed]` and `[e-mail removed]`, and the lines that name a recruiter ("please call Ahmed …", "Contact Person: …") are taken out; rules can miss an unusual wording, which is why the full ad is off by default. That keeps the output to job-market data rather than personal data under GDPR and similar laws; every record carries its `url`, and applicants apply on naukrigulf. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with naukrigulf.com or Info Edge.

## FAQ

**How many jobs per search?** As many as the search has: naukrigulf lets a search be read to its last page, 50 jobs a page, up to its own limit of 45,000, more than all of naukrigulf holds today (41,208 jobs). In the live run every search came back complete (1,951 of 1,951, 1,392 of 1,392, 384 of 384, 46 of 46).

**Are the filters obeyed?** Yes, naukrigulf applies them, and the run checks the salary bands itself: 1,392 of 1,392 jobs from an "experience 5 years" link had 5 years in their range, and 1,951 of 1,951 from a Saudi Arabia link were in Saudi Arabia.

**What if naukrigulf does not know my place?** Beside a keyword, naukrigulf quietly drops an unknown place and shows jobs from everywhere, so the run checks every place first and returns a free `NOT_FOUND` record instead. "KSA" is searched as Saudi Arabia, "Kuwait City" as Kuwait's capital.

**Why is the salary empty for most jobs?** The employer hid it: in the live run 456 of 3,773 jobs showed pay (384 in AED, 54 in SAR), none of the 1,943 web jobs that naukrigulf lists from elsewhere on the web (`isWebJob`).

**Last updated:** 2026-10-15.

## Related Actors

- [Naukri Jobs Scraper](https://apify.com/highbrow_fame/naukri-jobs) – Indian job ads and salaries
- [Foundit Scraper](https://apify.com/highbrow_fame/foundit-jobs) – Monster India, Gulf and Asia job ads
- [MyCareersFuture Scraper](https://apify.com/highbrow_fame/mycareersfuture-jobs) – Singapore job ads

Useful? A short Store review helps — your feedback decides what we improve next.
