# Google Maps Email Extractor & Lead Scraper

Google Maps Email Extractor turns a search such as "dentists in Berlin" into B2B leads: the business details from the Google Maps listing, the email addresses published on each company's own website, a deliverability grade for every address and a 0-100 lead score. It finds the contact page under its native name (impressum, kapcsolat, contatti and 44 more across ten languages) and grades each address with MX, SPF and DMARC checks plus a best-effort SMTP probe. Measured across 12 runs and 181 businesses: 71% of delivered rows carried an email. You pay only for leads delivered.

## What data does Google Maps Email Extractor extract?

One record per business:

- `name`, `address`, `latitude`, `longitude`, `plusCode`, `googleMapsUrl` – the listing and where it is
- `phone`, `whatsapp`, `website`
- `primaryEmail`, `emails` – the primary address (domain-matched when possible) and every address found on the company's site, ranked
- `emailValidation` – `mxRecords`, `hasSpf`, `hasDmarc`, `smtpValid`, `isCatchAll` and a `deliverability` grade (high / medium / low)
- `hasContactForm` – the site has a form when no address is published
- `rating`, `reviewCount`, `reviewKeywords`, `category`, `industry`, `cuisine`, `priceLevel`, `openingHours`, `serviceOptions`
- `businessStatus`, `isClaimed`, `businessDescription`
- `socialMedia`, `bookingUrl`, `menuUrl`
- `techStack`, `webQuality`, `webSignals` – 40+ detected technologies and a modern / dated / poor grade
- `leadScore`, `leadReadiness`, `suggestedOpener`, `aiLeadProfile` – 0-100 score, hot / warm / cold / dead, and an outreach profile
- `ownerName` – when the website names one
- `placeId`, `cid`, `searchQuery`, `scrapedAt`

The SMTP and catch-all probe is best effort; when Apify's cloud blocks port 25 the grade is DNS-only.

## How to use Google Maps Email Extractor

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example (`restaurants in Budapest`, 25 leads), so one click starts a run.
2. Replace the example with your own **Search Queries**, such as `plumbers in Chicago`, or paste Google Maps search or place URLs into **Start URLs**.
3. Set **Max results** per query. For a whole city raise `geoGridTiles` (3 for a mid-size city, 5 for a big one) to get past Google's ~120-result cap.
4. Optionally set `maxRunSeconds` as a hard stop; a run that reaches it saves everything collected and ends SUCCEEDED.
5. Press **Start** and download the leads from the **Output** tab as JSON, CSV or Excel.

For a weekly re-run, pass the previous run's dataset ID as `sinceDatasetId`: places already delivered are skipped before any charge.

## Example output

Values are examples, shortened:

```json
{
  "name": "Osteria Nonnino",
  "website": "https://osteria-nonnino.com",
  "primaryEmail": "info@osteria-nonnino.com",
  "emailValidation": { "mxRecords": 5, "hasSpf": true, "hasDmarc": true, "deliverability": "high" },
  "leadScore": 95,
  "leadReadiness": "hot"
}
```

## How much does it cost?

Pay per delivered lead, with no subscription or compute fee. On the Apify Free plan the price is **$0.007 per lead, $7.00 per 1,000 leads**; paid plans are lower, down to $4.50 per 1,000 on Gold and above. Every run also charges a start fee of $0.015 per GB of run memory, $0.06 at the 4 GB default.

Worked example: 100 plumbers in Chicago on the Free plan = 100 × $0.007 + $0.06 = **$0.76**; 1,000 leads = $7.06. Failures, blocks and duplicates are free; a run that delivers nothing costs only the start fee.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/google-maps-email-extractor` to Claude, ChatGPT or any MCP client and the assistant sees one tool with this Actor's input fields, so "dentists in Szeged with email addresses" starts a run. Runs bill to your own Apify account at the same per-lead rate.

## Is it legal to scrape Google Maps?

This is general information, not legal advice; you are the data controller for what you collect. Public business data (name, address, phone, website, hours, rating) and generic addresses such as `info@` are corporate contact data, usually covered by legitimate interest for B2B outreach under GDPR Art. 6(1)(f) with a clear opt-out. Personal addresses (`firstname.lastname@`) and `ownerName` are personal data: document a legitimate-interest assessment or get consent. Google's Terms of Service prohibit automated access, a contractual restriction, so expect technical blocks. Do not send email without an opt-out (GDPR, CAN-SPAM, PECR, CASL), honour suppression lists and delete data you no longer need.

## FAQ

**Does it work outside English-speaking markets?** Yes. Contact-page names are covered in ten languages (Hungarian, German, French, Italian, Spanish, Portuguese, Polish, Dutch, Czech, English). Measured hit rates: 85% for Berlin Mitte dentists (20 businesses), 70% for Shoreditch coffee shops (20), 64% for Manhattan Italian restaurants (25), 53% for Austin dentists (168).

**Is it an email finder?** In the narrow sense: it collects addresses already published on the company's website. It does not guess addresses from name patterns or query third-party databases.

**What does it not do?** No phone validation, no follower counts, no CAPTCHA bypass; blocked requests are not charged.

**Last updated:** 2026-10-15. Measurements: 12 runs, 181 businesses, verified 28 August 2026; prices verified 15 October 2026.

## Related Actors

- [AI Brand Monitor — AI Search Visibility Tracker](https://apify.com/highbrow_fame/ai-search-visibility-tracker) – see whether ChatGPT, Perplexity and Gemini cite the businesses you scrape
- [OpenStreetMap Places Scraper](https://apify.com/highbrow_fame/openstreetmap-places) – POIs, addresses and opening hours from OpenStreetMap
- [Website Tech Stack Detector](https://apify.com/highbrow_fame/website-tech-stack) – CMS, frameworks and analytics for a list of domains

Useful? A short Store review helps — your feedback decides what we improve next.
