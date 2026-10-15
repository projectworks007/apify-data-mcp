# AI Brand Monitor — AI Search Visibility in ChatGPT & Perplexity

AI Brand Monitor is an AI search visibility tracker: it tells you whether ChatGPT, Perplexity, Gemini and Google AI Overviews mention your brand, which sources they cite instead of you, and your share of voice against competitors. Enter your domain and your buyers' questions. The default engine, Perplexity, runs with no API key in 24 languages. Built for GEO (generative engine optimization) and AI SEO work: agencies reporting AI visibility to clients, and brands checking whether AI search recommends them or a competitor.

## What data does AI Brand Monitor extract?

One `citation` record per engine × query × sample:

- `engine`, `model`, `query`, `language`, `latencyMs`
- `answerText` – the full AI answer
- `citationCount`, `citations` – every source the engine used, with `url`, `host`, `registrable` domain and page `title`
- `brandMatches` – per tracked domain: `cited`, `viaCitation`, `viaText`, `matchedUrls`
- `competitorMatches` – the same for each competitor domain
- `citationShare` – `hits` and `sharePct` per domain

Also: a `stability` record per query and engine when `samplesPerQuery` is above 1 (how often each source held across N runs), a `delta` record when `previousRunDatasetId` is set (citations gained and lost), a closing `summary` record, and unbilled `empty` / `not_measured` records for work that produced nothing.

## How to use AI Brand Monitor

1. Open the Actor page and press **Try for free**; the Input tab comes prefilled with a working example, so one click starts a run.
2. Enter your **queries** (the questions your buyers ask an AI, such as "best CRM for small business") and your **brandDomains**; add **competitorDomains** for share of voice.
3. Pick **engines**. `perplexity-agent` needs no key and covers all 24 languages; `google-aio` reads Google's AI Overview (English only). Gemini and ChatGPT are included with a per-run allowance; add your own key for Claude or for more calls.
4. Set `samplesPerQuery` to 3 or 5 for a stability score, and set `language` (`de`, `hu`, `fr` …) to measure your own market.
5. Press **Start** and download the records from the **Output** tab as JSON or CSV. For a weekly report, schedule the run and pass last week's dataset ID as `previousRunDatasetId`.

## Example output

Values are examples:

```json
{
  "type": "citation",
  "engine": "perplexity-agent",
  "query": "best CRM for small business",
  "citationCount": 7,
  "brandMatches": { "yourcompany.com": { "cited": true, "viaCitation": true } },
  "citationShare": { "yourcompany.com": { "hits": 1, "sharePct": 14.3 } }
}
```

## How much does it cost?

**$0.05 per citation record, $50 per 1,000 records.** One record is one engine answering one question once. Each run also charges $0.0001 at start. Stability, delta, summary, empty and not_measured records are free.

Worked example: a 10-question check on one engine is 10 records = **$0.50**. An agency tracking 30 clients × 50 prompts a month on one engine delivers 1,500 records = $75 a month.

Included engine calls run on our keys: Perplexity 12 per run on a free Apify plan and 200 on a paid one; ChatGPT 3 and 60; Gemini 25 queries per run. Past the allowance, queries come back as unbilled `not_measured` records. With your own key you pay that vendor directly, with no markup.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server: add `https://mcp.apify.com/?tools=highbrow_fame/ai-search-visibility-tracker` as a custom connector in Claude, ChatGPT or any MCP client, and a question such as "is hubspot.com cited for 'best CRM for small business'?" starts a run. Runs bill to your own Apify account at the same per-record rate; the default engine still needs no key.

## Is it legal to monitor AI search answers?

The Actor sends your questions to AI engines through their APIs (OpenAI's Responses API with web search, Gemini grounding, Perplexity) and reads Google's AI Overview from the public result page. What comes back is the answer text and the public URLs it cites; the Actor collects no personal data by design. Your API keys are marked secret in the input schema, encrypted at rest and never logged. You are responsible for how you use the reports; this is general information, not legal advice.

## FAQ

**Why do citations change between runs?** AI answers are not deterministic. Set `samplesPerQuery` to 3 or 5 and ignore sources with `stability` below 0.5; the Actor never filters for you.

**Does it work for German, Hungarian or Polish keywords?** Yes, with the default engine, Gemini and ChatGPT. Measured 2026-08-23 on a Hungarian query: 15 sources, 8 of them `.hu`. Google AI Overview capture is English-only: Google withholds the locale bundle from automated access.

**Does it scrape ChatGPT.com?** No. It uses the official API with web search, which returns structured citations.

**How big is the free Gemini tier?** Measured 2026-08-02: 20 requests per day per model on a free Gemini key, so bring a paid key or use the default engine for volume.

**Last updated:** 2026-10-15. Price of $0.05 per record in force since 10 August 2026.

## Related Actors

- [Google Maps Email Extractor & Lead Scraper](https://apify.com/highbrow_fame/google-maps-email-extractor) – leads with validated emails; check whether AI engines cite them
- [Google Trends Scraper](https://apify.com/highbrow_fame/google-trends-reliable) – interest over time, regions and related queries
- [Domain Authority & Website Rank Checker](https://apify.com/highbrow_fame/domain-authority-rank) – bulk authority data for the domains the AI cites

Useful? A short Store review helps — your feedback decides what we improve next.
