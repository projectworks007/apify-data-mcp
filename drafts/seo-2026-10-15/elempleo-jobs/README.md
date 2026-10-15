# Elempleo Scraper — Colombia Job Offers & Salaries, No Phones

Elempleo Scraper gets job offers from elempleo.com, one of Colombia's largest job boards: title, company (or "confidential"), city, the salary band in pesos a month as numbers, contract type, on-site, hybrid or remote, posting date, related positions, key skills and the ad text, and from each job's page the experience and education asked, job level, work area, vacancies, every city of the offer, the closing date and the full description. Paste your Elempleo search links, or just type a keyword and a city. No phone numbers or contact names are delivered, and you pay only for jobs delivered.

## What data does Elempleo Scraper extract?

For every job:

- `jobId`, `url`, `title`
- `company`, `companyConfidential`, `companyId`, `companyLogo` – no name, id or logo when the offer is confidential
- `city`, `multipleCities` – true when the offer is posted for several cities
- `salaryText`, `salaryMin`, `salaryMax`, `currency`, `salaryPeriod` – the band ("$6 a $8 millones") and as numbers, COP a month; empty when confidential
- `contractType`, `workModality` – Indefinido, Definido, Por obra o labor …; Presencial, Híbrido, Remoto
- `postedAt`, `relatedPositions`, `keywords`
- `description` – the ad text (the result list cuts it at 2,000 characters; the job page gives all of it)
- `input`, `keyword`, `searchedCity`, `position`, `scrapedAt`, `status`, `error`

With **Open every job for its details** (on by default) also: `jobLevel`, `experience`, `minExperienceYears`, `educationLevel`, `professions`, `area`, `workingHours`, `vacancies`, `cities`, `department`, `sectors`, `inclusiveHiring`, `employmentType`, `validThrough` and the full `description`.

## How to use Elempleo Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from elempleo.com, one per line, or type **Keywords** (contador, enfermera) and **Cities** (Bogotá, Medellín) and choose salary, contract type, work modality, job level, work area and "published within".
3. Set **Max jobs per search**, and untick **Open every job for its details** for a faster run with the list data only.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new jobs, save the input as a task with **Published within** set to "Today and yesterday" and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Desarrollador full stack .net",
  "company": "HITSS",
  "city": "Bogotá",
  "salaryMin": 6000000,
  "salaryMax": 8000000,
  "currency": "COP",
  "contractType": "Indefinido",
  "minExperienceYears": 5
}
```

## How much does it cost?

**$0.0009 per job delivered, $0.90 per 1,000 jobs.** The job page's details cost nothing extra, only time. Links that are not Elempleo searches, links with filters Elempleo does not understand, unknown cities and jobs whose page has closed are free.

Worked example: a live run read four searches (all of Medellín, all remote jobs, developers paid 6-10 million on a permanent contract, "analista" in Bogotá from 4 million a month), 2,552 jobs with their details in 6 minutes 57 seconds, for **$2.30**. Without details, 10,173 jobs from all of Bogotá and "enfermera" took 8 minutes 55 seconds and cost $9.16.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/elempleo-jobs` to Claude, ChatGPT or any MCP client and the assistant can search Colombian jobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape Elempleo?

The Actor reads public Elempleo job offers only. Employers keep their company name, and "Empresa confidencial" stays unnamed. Phone numbers, WhatsApp links, e-mail addresses and the names of contact persons written into the ads are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]` (98 phone numbers, 65 e-mail addresses and 6 names in the 2,552-job run); salaries in the text stay as they are. That keeps the output to job-market data rather than personal data under GDPR and similar laws; every record carries its `url`, and candidates apply on Elempleo. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with Elempleo.

## FAQ

**How many jobs per search?** Elempleo serves the first 10,000 jobs of a search and no more: in a live run, all of Bogotá gave 9,976 of its 13,991. Split a bigger search by city or by a filter to get the rest.

**Why a few jobs less than Elempleo's count?** Jobs of the same day change places between Elempleo's pages, so one can be listed twice while another is skipped. The run counts every job once and reads the list again when it came up short: Medellín gave 1,490 of 1,494 jobs, the remote search 616 of 616.

**Do all jobs show a salary?** No. `salaryMin` and `salaryMax` come for every job that shows its band, 1,883 of 2,552 in the live run; the others keep it confidential. **Min salary** and **Max salary** work on Elempleo's bands and leave confidential salaries out.

**Why fewer jobs than the search shows?** Elempleo's result list still shows some offers whose page has already closed: 48 of 2,552 in a live run. With details on, these are left out and not charged.

**Last updated:** 2026-10-15.

## Related Actors

- [InfoJobs Scraper](https://apify.com/highbrow_fame/infojobs-jobs) – Spanish job ads and salaries
- [BestJobs Scraper](https://apify.com/highbrow_fame/bestjobs-ro-jobs) – Romanian jobs and net salaries
- [Naukri Jobs Scraper](https://apify.com/highbrow_fame/naukri-jobs) – Indian job ads and salaries

Useful? A short Store review helps — your feedback decides what we improve next.
