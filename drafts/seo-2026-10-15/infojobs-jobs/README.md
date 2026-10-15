# InfoJobs Scraper + New Jobs Feed & Alerts, No Phones

InfoJobs Scraper gets job offers from InfoJobs (infojobs.net), Spain's largest job board: title, company, town and province, the salary range per year, month or hour, contract type, working day, on-site, hybrid or remote, when it was published and the full ad text, plus the job page's applications, category, experience and studies asked, requirements, languages and skills. Paste your InfoJobs search links, or type keywords and places. No contact names, phone numbers or e-mail addresses are delivered, a feed mode returns only new jobs, and you pay only for jobs delivered.

## What data does InfoJobs Scraper extract?

For every job:

- `offerId`, `url`, `title`
- `company`, `companyHidden`, `companyUrl`, `companyLogo` – `companyHidden` when the employer hides its name ("Empresa confidencial")
- `city`, `province`, `postalCode`
- `salaryMin`, `salaryMax`, `salaryPeriod`, `salaryType`, `currency`, `salaryText` – the salary range, gross, in EUR, and as InfoJobs writes it ("1.500€ - 1.700€ Bruto/mes")
- `contractType`, `workday`, `teleworking` – Indefinido…; Completa, Parcial…; Presencial, Híbrido, Solo teletrabajo
- `publishedAt`, `isNew`, `isPromoted`, `isExecutive`, `multiProvince`
- `description` – the full ad text
- `input`, `keyword`, `place`, `position`, `scrapedAt`, `status`, `error`, `detailsError`

With **Add the job page's details** (on by default) also:

- `applications`, `category`, `subcategory`, `jobLevel`, `normalizedJobTitle` – how many have applied
- `minimumExperience`, `minimumStudies`, `studiesDetail`, `minimumRequirements`, `desiredRequirements`
- `languages`, `skills`, `vacancies`, `staffInCharge`, `contractDuration`, `workingHours`, `benefits`, `department`, `industry`

In a live run 943 of 2,011 jobs showed a salary. Untick the details for the list fields only, faster.

## How to use InfoJobs Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from infojobs.net, one per line, or type **Keywords** (camarero, programador java) and **Places** (Madrid, Móstoles) and choose category, contract type, working day, remote work, minimum salary, **Published within** and newest first.
3. Set **Max jobs per search**, and untick **Add the job page's details** if the list fields are enough.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Camarero/a",
  "company": "InfoJobs Assistance",
  "city": "Móstoles",
  "province": "Madrid",
  "salaryMin": 1500,
  "salaryMax": 1700,
  "salaryPeriod": "month",
  "applications": 60
}
```

## How much does it cost?

**$0.0015 per job delivered, $1.50 per 1,000 jobs.** The job page's details cost nothing extra, only time. Links that are not InfoJobs searches and places InfoJobs does not know are free records.

Worked example: a live run read three searches (Santa Cruz de Tenerife, IT jobs in all of Spain, drivers in Valencia), 2,011 jobs with details in 6 minutes 39 seconds, for **$3.02**. "programador" in all of Spain without details, 447 jobs in 21 seconds, cost $0.67.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item it has delivered for this exact search, in a key-value store in your own account. The first run returns everything; later runs with the same inputs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link; it works with Slack and Discord incoming webhooks and any HTTPS endpoint.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/infojobs-jobs` to Claude, ChatGPT or any MCP client and the assistant can search InfoJobs with this Actor's own input fields. You pay per job delivered, at the same rate.

## Is it legal to scrape InfoJobs?

The Actor reads public InfoJobs job offers only. Employers are companies and keep their name; phone numbers, e-mail addresses and the names of contact persons written into the ads are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]` (23 names and 1 e-mail address in a live run of 2,011 jobs). That keeps the output to job-market data rather than personal data under GDPR; every record carries its `url`, and candidates apply on InfoJobs. You remain responsible for how you use the data and for InfoJobs' terms. This is an independent tool, not affiliated with InfoJobs.

## FAQ

**How many jobs per search?** As many as InfoJobs lists, up to your maximum. In a live run the all-of-Spain search stopped at the 1,500 set as the maximum, of 64,324.

**Why is a job from another province in my search?** A job posted for several provinces is listed in each of them; `multiProvince` is `true` for those, and with the details `province` is the job's own.

**What does the minimum salary filter do?** It is InfoJobs' own filter and compares year, month and hour salaries: a live run asking for 1,400 a month also got jobs at 23,000-33,000 a year.

**Why no phone numbers or contact names?** They are personal data. Every job has its `url`; you apply on InfoJobs.

**Last updated:** 2026-10-15.

## Related Actors

- [Reed.co.uk Scraper](https://apify.com/highbrow_fame/reed-jobs) – UK jobs and salaries from reed.co.uk
- [HelloWork Scraper](https://apify.com/highbrow_fame/hellowork-jobs) – job ads from France
- [Elempleo Scraper](https://apify.com/highbrow_fame/elempleo-jobs) – job ads from Colombia

Useful? A short Store review helps — your feedback decides what we improve next.
