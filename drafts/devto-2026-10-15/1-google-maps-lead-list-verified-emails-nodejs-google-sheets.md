---
title: Build a local-business lead list with verified e-mails from Google Maps (Node.js + Google Sheets)
published: false
description: Scrape Google Maps leads with graded e-mail addresses in Node.js, keep only deliverable rows and push them to a Google Sheet or CSV.
tags: abotwrotethis, node, webscraping, tutorial
---

> Disclosure: I built the Apify Actor used in this tutorial. This post was written with AI assistance and checked by me.

A lead list for local outreach has three parts: find the businesses, find an e-mail address for each one, and decide which addresses are worth sending to. This tutorial does all three in about 60 lines of Node.js: Google Maps is the source, an Apify Actor scrapes and grades the e-mails, and the result lands in a Google Sheet or a CSV file.

What you need:

- Node.js 18 or newer
- An [Apify](https://apify.com) account and its API token (Settings, API & Integrations)
- For the Sheets part: a Google Cloud service account with the Sheets API enabled

The Actor is [Google Maps Email Extractor](https://apify.com/highbrow_fame/google-maps-email-extractor). It is pay-per-result: on Apify's free plan a delivered lead costs $0.007, so 1,000 leads are $7.00, plus a run-start fee of $0.015 per GB of run memory ($0.06 on the 4 GB default). Paid plans go down to $0.0045 per lead, and the free plan's monthly usage credit covers the test run below.

## 1. Install and configure

```bash
mkdir maps-leads && cd maps-leads
npm init -y
npm install apify-client googleapis
```

Keep your Apify token in the environment:

```bash
export APIFY_TOKEN=apify_api_xxxxxxxx
```

## 2. Run the Actor from Node.js

The two input fields that matter are `searchQueries` (an array of plain-language searches, one per market) and `maxResults` (leads per query, 0 for unlimited). E-mail grading is on by default through `validateEmails: true`, so you do not have to set it.

```javascript
// scrape.js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

export async function scrapeLeads(searchQueries, maxResults = 25) {
  const run = await client.actor('highbrow_fame/google-maps-email-extractor').call({
    searchQueries,
    maxResults,
    validateEmails: true,
  });
  const { items } = await client.dataset(run.defaultDatasetId).listItems();
  return items;
}
```

`call()` starts the run and waits until it finishes. Expect roughly 70 seconds of startup plus 5 to 8 seconds per lead, so a 25-lead run takes around 3 minutes. For a hard upper bound add `maxRunSeconds`; the run then saves what it has when the budget is spent and still ends as SUCCEEDED.

Each item is one business. The fields we care about:

```json
{
  "name": "Osteria Nonnino",
  "address": "123 Main Street, New York, NY 10013",
  "phone": "+1 (212) 555-1234",
  "website": "https://osteria-nonnino.com",
  "primaryEmail": "info@osteria-nonnino.com",
  "emails": ["info@osteria-nonnino.com", "reservations@osteria-nonnino.com"],
  "emailValidation": {
    "mxRecords": 5, "hasSpf": true, "hasDmarc": true,
    "smtpValid": null, "isCatchAll": null, "deliverability": "high"
  },
  "hasContactForm": true,
  "rating": 4.6,
  "reviewCount": 328,
  "category": "Italian restaurant",
  "leadScore": 95,
  "googleMapsUrl": "https://www.google.com/maps/place/Osteria+Nonnino"
}
```

`primaryEmail` is the address whose domain matches the website when one exists; `emails` holds every address found, ranked. Both are empty when the site publishes no address; `hasContactForm` then says whether there is a form instead.

## 3. What the e-mail grade actually means

Be precise about what `emailValidation` checks and what it cannot check.

- **`mxRecords`**: the number of MX records on the address's domain. Zero means the domain cannot receive mail, and the address is useless.
- **`hasSpf`** and **`hasDmarc`**: whether the domain publishes SPF and DMARC DNS records. These say nothing about whether a mailbox exists. They tell you the domain is actively administered for mail, which correlates with a real, monitored inbox.
- **`smtpValid`** and **`isCatchAll`**: a best-effort SMTP `RCPT TO` probe. A catch-all domain accepts mail for any local part, so a "valid" answer from it proves nothing, and bounces are likelier. These two fields are often `null`, because Apify's cloud frequently blocks outbound port 25. When they are `null`, the grade is DNS-only.
- **`deliverability`**: `high`, `medium` or `low`, combining the above.

In my own test runs, between 25% and 65% of rows had a `high` grade and between 53% and 85% had any e-mail, depending on the market. Plan for those numbers. A DNS-only grade cannot prove that `info@example.com` exists as a mailbox; it can tell you the domain receives mail and is maintained. Use it as a first filter before a cold send, not as a replacement for bounce handling.

## 4. Filter and flatten

Keep rows with a primary e-mail and a `high` grade, and flatten the nested fields, because Sheets and CSV want one value per cell.

```javascript
// transform.js
export function toRows(items) {
  return items
    .filter((it) => it.primaryEmail && it.emailValidation?.deliverability === 'high')
    .map((it) => [
      it.name ?? '',
      it.category ?? '',
      it.address ?? '',
      it.phone ?? '',
      it.website ?? '',
      it.primaryEmail,
      it.emailValidation?.hasSpf ? 'yes' : 'no',
      it.emailValidation?.hasDmarc ? 'yes' : 'no',
      it.emailValidation?.isCatchAll === null ? 'unknown' : String(it.emailValidation.isCatchAll),
      it.rating ?? '',
      it.reviewCount ?? '',
      it.leadScore ?? '',
      it.googleMapsUrl ?? '',
    ]);
}

export const HEADER = [
  'Name', 'Category', 'Address', 'Phone', 'Website', 'Email',
  'SPF', 'DMARC', 'Catch-all', 'Rating', 'Reviews', 'Lead score', 'Maps URL',
];
```

Too few rows? Widen the filter to include `medium` and sort by the SPF and DMARC columns later.

## 5a. Push to Google Sheets

Create a service account in Google Cloud, enable the Sheets API, download its JSON key, and share the target spreadsheet with the service account's e-mail address. The spreadsheet ID is the long string in the sheet's URL.

```javascript
// sheets.js
import { google } from 'googleapis';

export async function appendRows(spreadsheetId, rows) {
  const auth = new google.auth.GoogleAuth({
    keyFile: process.env.GOOGLE_KEY_FILE,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });
  const sheets = google.sheets({ version: 'v4', auth });
  await sheets.spreadsheets.values.append({
    spreadsheetId,
    range: 'Sheet1!A1',
    valueInputOption: 'RAW',
    requestBody: { values: rows },
  });
}
```

`append` writes under the last filled row of the range, so the sheet grows on every run. Write the header once by hand, or append `HEADER` on the first run.

## 5b. Or write a CSV

Without a Google Cloud project, write a CSV instead. The only thing to get right is quoting:

```javascript
// csv.js
import { writeFileSync } from 'node:fs';

const cell = (v) => `"${String(v).replaceAll('"', '""')}"`;

export function writeCsv(path, header, rows) {
  const lines = [header, ...rows].map((r) => r.map(cell).join(','));
  writeFileSync(path, lines.join('\n') + '\n', 'utf8');
}
```

## 6. Put it together

```javascript
// index.js
import { scrapeLeads } from './scrape.js';
import { toRows, HEADER } from './transform.js';
import { appendRows } from './sheets.js';
import { writeCsv } from './csv.js';

const items = await scrapeLeads(['dentists in Leeds', 'dentists in Sheffield'], 25);
const rows = toRows(items);
console.log(`${items.length} businesses scraped, ${rows.length} with a high-grade e-mail`);

if (process.env.SHEET_ID) {
  await appendRows(process.env.SHEET_ID, rows);
} else {
  writeCsv('leads.csv', HEADER, rows);
}
```

Add `"type": "module"` to `package.json` for the `import` syntax, then:

```bash
GOOGLE_KEY_FILE=./service-account.json SHEET_ID=1AbC... node index.js
```

Two queries at 25 leads each is 50 leads: 50 × $0.007 + $0.06 = $0.41 on the free plan.

## 7. Re-running without paying twice

For a weekly refresh, pass the previous run's dataset ID as `sinceDatasetId`. Places already in that dataset are matched by `placeId` and skipped before any charge, so a repeat run costs only the new businesses. Keep `run.defaultDatasetId` after each run and read it back next time.

## The GDPR and anti-spam caveat

Most of this list is a company's generic address (`info@`, `office@`), published on its own website to be contacted, which for B2B outreach is usually covered by legitimate interest under GDPR Art. 6(1)(f) with a clear opt-out. Some rows will contain a personal address (`firstname.lastname@`), and the Actor also returns an `ownerName` field when a site names one. Those are personal data: document a legitimate-interest assessment or get consent before using them.

Separately, cold e-mail is regulated by CAN-SPAM in the US, PECR in the UK and CASL in Canada, and several EU countries (Germany, France, Italy) require prior opt-in even for B2B. You are the data controller: honour opt-outs, keep a suppression list, delete rows you no longer need. The Actor and Apify are processors at most; the per-lead price covers infrastructure, not legal responsibility.

## Limits to know before you scale

- Google Maps caps a single search at roughly 120 results. The `geoGridTiles` option splits a city into an N×N grid and de-duplicates by `placeId`; 5 suits a big city.
- Google's terms of service prohibit automated access. Blocked requests are not charged, and `proxyConfiguration` can switch from the datacenter default to residential.
- The Actor collects addresses already published on the company's site; it does not guess or buy them, so businesses without a website will have no e-mail.
- Treat `smtpValid: null` as "not checked", not as "invalid".

The full output schema, pricing and measured hit rates per market are on the [Actor page](https://apify.com/highbrow_fame/google-maps-email-extractor).
