# Agent-demand research for ~100 new Apify actors (highbrow_fame), 2026-10-19

Research only. No actors were built, published or renamed. Data: Apify Store API, Apify MCP docs and blog, read on 2026-10-19.

## 1. Summary

- Swept **833 agent-style Store queries** (two passes, limit=100 each) and scored **144 candidate actors**; `candidates.json` holds the full ranked list with per-query competition data.
- In **663 of 833 queries (79%) at least 8 of the top-10 results have fewer than 20 users/30d** — the "<task> api" phrasing is wide open almost everywhere. Only **47 queries (5%)** have a top-10 actor with 1,000+ users/30d, and those are nearly all the "<site> scraper" phrasings (Google Maps, Reddit, LinkedIn jobs, Amazon, YouTube transcript, website content crawler).
- The winning pattern in the data is the same one that already worked for the catalog: **exact query words in the title + "Unofficial <X> API." in the description**, aimed at the "api" phrasing of a topic whose "scraper" phrasing proves real demand.
- Top of the list: `web-fetch-api`, `google-news-api`, `website-screenshot-api`, `pdf-to-markdown-api`, `article-extractor-api`, `careers-page-jobs-api`, `markdown-site-crawler`, `url-to-markdown-api`, `news-search-api`, `pagespeed-api`. The full top 30 is in section 4; the 100-actor build order in section 5.
- Honest baseline (section 7): the current 87 public actors total **98 users/30d combined** (median 1). Comparable exact-match "api" actors by other developers sit at 10–250 users/30d. Expect a median of ~5–15 users/30d per new actor and a long tail; the money is in the 10–15 actors that reach 100+ users/30d.

## 2. Method

**Demand signals.** `GET https://api.apify.com/v2/store?search=<q>&limit=100` for every query; per result: `stats.totalUsers30Days`, `totalUsers`, `actorReviewCount/Rating`, `bookmarkCount`, `lastRunStartedAt`, `currentPricingInfo`, `categories`. Also pulled Store categories AGENTS (4,058 actors) and MCP_SERVERS (2,779 actors), our own 87 public actors, the Apify MCP docs (default tools are `apify/rag-web-browser` and `apify/web-fetch`; agents discover everything else via `search-actors`, which queries the Store index; rental-priced actors are excluded from that index), and the Apify blog post on how the MCP server rewrites an actor before agents see it (Store description becomes the tool description; input field descriptions cut at 500 chars; `default` on a required field makes it look optional; output schema is inferred from recent runs).

**Queries.** 545 primary queries across 23 task families (web search/SERP, page-to-markdown/fetch, structured extraction, company enrichment, contact verification, documents, news, social/public content, e-commerce, travel, maps, jobs, real estate, finance/crypto, weather/geo, government/open data, academic, developer data, domain/SEO, text utilities, screenshots, sitemaps/RSS, other) plus 288 second-pass phrasings (plain "<site> scraper" demand proxies and extra "<x> api" forms). Full per-query metrics are in `queries_metrics.csv`.

**Per query.** competing actors (`total`), users/30d of the top 3, our rank if any actor of ours is in the top 100, share of the top 10 with <20 users/30d ("weak"), unreviewed, or not run in 30 days ("stale"), and whether the target site has an official free API (hand-annotated per candidate).

**Score** = agent relevance (1–5, curated: how often an assistant needs it) × demand (1–5, log of the geometric mean of the primary query's top-3 users/30d and the best related query's top-3 users/30d) × beatability (1–5: weak/unreviewed/stale share of the top 10, bonus when no top-10 actor has 100+ users, penalty when a 5,000+ user giant sits in the top 10) × buildability (1–5, curated: public pages or open API, no login, no captcha, low compute) ÷ 625 × 100, then × 0.85–1.0 when an official free API exists (0.85 free-no-key, 0.9 free-but-restricted, 0.95 free-with-key, 1.0 none/paid).

**Exclusions applied before scoring.** Anything needing login or cookies, captcha solving or bot-wall circumvention as the core (LinkedIn people, Instagram, Facebook, TikTok, X, Threads, Pinterest, Quora, Glassdoor-with-login), personal-profile harvesting, email *finding* by name, bulk copyrighted content resale (video downloaders), adult, gambling (odds, lottery). A few bot-walled but very-high-demand sites (Amazon, Walmart, Zillow, Indeed, LinkedIn *jobs*, G2) are kept in the list with buildability 2 and explicit risk notes so the owner can decide; they are not in the first 100.

## 3. What the data says

| Fact | Numbers |
|---|---|
| Queries swept | 833 |
| Queries where ≥8 of top-10 have <20 users/30d | 663 (79%) |
| Queries with a 1,000+ users/30d actor in the top 10 | 47 (5%) |
| Our actors (public) / combined users 30d / median | 87 / 98 / 1 |
| Our best actor | google-maps-email-extractor, 12 users/30d |
| Store category sizes | AGENTS 4,058 · MCP_SERVERS 2,779 |

Observed exact-match "api"-titled actors by other developers (what winning a phrase is worth today): `johnvc/google-images-api` 245 users/30d, `cheapapi/website-screenshot-api` 171, `s-r/backlinks-checker` 111, `michael.g/email-verifier-validator` 489, `johnvc/Google-AI-Overview-API` 89, `johnvc/apple-maps-api` 12, `johnvc/walmart-api` 10, `clearpath/brave-search-api` 12, `automation-lab/pdf-text-extractor` 126, `grow_media/youtube-search-api` 594, `fantastic-jobs/career-site-job-listing-api` 1,577.

Phrasing matters more than topic: `google search api` top-3 = 18/40/2 users while `google search results scraper` = 23,182/203/89; `reddit api` = 25/60/4 vs `reddit scraper` = 8,121/3,076/4,096; `google places api` = 1/86/25 vs `google maps scraper` = 42,772/7,952/2,601; `zillow api` = 23/1/9 vs `zillow scraper` = 1,184/681/58; `amazon product api` = 1/2/2 vs `amazon scraper` = 3,436/2,160/721. Agents type the left-hand phrasing.

Where our current catalog already ranks top-10 on an agent phrase (retitle/upgrade instead of new build, see section 6): `catch all email detection` #1, `text extraction api` #2, `github trending api` #3, `apple podcasts api` #3, `chatgpt search monitor` #4, `sitemap api` #4, `financial data api` #4, `crypto price api` #5, `dns lookup api` #6, `pdf to text api` #6, `domain authority api` #7, `rss feed api` #7, `substack api` #8, `podcast api` #8, `hotel prices api` #9, `openstreetmap api` #9, `whois api` #10, `google play api` #10.

## 4. Top 30 candidates

Columns: primary query we would title for; demand = top-3 users/30d on the primary query / on the strongest related query; incumbent = #1 result for the primary query (users/30d); R/D/B/B = relevance/demand/beatability/buildability.

| # | slug | title (short) | primary query | demand prim / topic | #1 incumbent (u30) | R/D/B/B | score |
|---|---|---|---|---|---|---|---|
| 1 | `web-fetch-api` | Web Fetch API | `fetch url content` | 2 / 20665 | gentle_cloud/pandoc-document-converter (1) | 5/3.44/4.07/5 | 55.9 |
| 2 | `google-news-api` | Google News API | `google news api` | 37 / 794 | s-r/google-news (16) | 5/3.27/4.27/5 | 55.8 |
| 3 | `website-screenshot-api` | Website Screenshot API | `screenshot api` | 297 / 1699 | cheapapi/website-screenshot-api (171) | 5/3.94/3.5/5 | 55.2 |
| 4 | `pdf-to-markdown-api` | PDF to Markdown API | `pdf to markdown` | 57 / 311 | gochujang/pdf-text-extractor (54) | 5/3.15/4.26/5 | 53.7 |
| 5 | `article-extractor-api` | Article Extractor API | `article extractor api` | 8 / 259 | vonsensey/linkedin-pulse-article-scraper-api (7) | 5/2.66/4.36/5 | 46.5 |
| 6 | `careers-page-jobs-api` | Careers Page Scraper | `careers page scraper` | 104 / 1592 | conserving_celerytop/live-career-page-jobs-api (42) | 4/3.67/3.92/5 | 46.1 |
| 7 | `markdown-site-crawler` | Markdown Crawler API | `markdown crawler` | 150 / 13431 | xtech/news-source-crawler (12) | 5/4.27/3.27/4 | 44.6 |
| 8 | `url-to-markdown-api` | URL to Markdown API | `url to markdown` | 18 / 26 | apify/url-to-markdown (11) | 5/2.31/4.48/5 | 41.4 |
| 9 | `news-search-api` | News Search API | `news search api` | 3 / 794 | tidytools/news-scraper (1) | 5/2.73/4.34/5 | 40.3 |
| 10 | `pagespeed-api` | PageSpeed Insights API | `page speed api` | 89 / 89 | lost.fany/pagespeed-insights-core-web-vitals (0) | 4/2.95/4.3/5 | 38.6 |
| 11 | `company-enrichment-api` | Company Enrichment API | `company enrichment api` | 20 / 156 | renzomacar/company-enrichment (7) | 5/2.74/4.31/4 | 37.8 |
| 12 | `reddit-api` | Reddit API | `reddit api` | 89 / 15293 | clearpath/reddit-answers-api (25) | 5/4.18/3.91/3 | 37.2 |
| 13 | `google-search-api` | Google Search API | `google search api` | 60 / 25279 | theagents/google-maps-search (18) | 5/4.2/3.66/3 | 36.9 |
| 14 | `youtube-channel-api` | YouTube Channel API | `youtube channel api` | 434 / 3642 | apidojo/youtube-channel-information-scraper (427) | 4/4.21/3.41/4 | 34.9 |
| 15 | `trustpilot-api` | Trustpilot API | `trustpilot api` | 72 / 1754 | johnvc/trustpilot-reviews-api (64) | 4/3.61/3.65/4 | 33.8 |
| 16 | `url-status-checker-api` | URL Status Checker API | `http status checker` | 18 / 44 | automation-lab/http-status-checker (11) | 4/2.43/4.29/5 | 33.4 |
| 17 | `ocr-api` | OCR API | `ocr api` | 151 / 318 | zen-studio/google-lens-ocr (59) | 4/3.38/3.83/4 | 33.1 |
| 18 | `office-document-to-text-api` | DOCX, PPTX, XLSX & EPUB to Text API | `docx to text` | 10 / 45 | marielise.dev/pdf-to-mp3 (9) | 4/2.31/4.47/5 | 33.0 |
| 19 | `app-store-api` | App Store API | `app store api` | 136 / 766 | johnvc/apple-app-store-reviews-api (125) | 4/3.56/3.4/5 | 33.0 |
| 20 | `google-reviews-api` | Google Reviews API | `google reviews api` | 477 / 8576 | thewolves/google-play-reviews-scraper (368) | 5/4.44/3.08/3 | 32.8 |
| 21 | `weather-api` | Weather API | `weather api` | 59 / 59 | bigdavidson/kalshi-weather-markets (49) | 4/2.76/4.36/5 | 32.8 |
| 22 | `github-repo-api` | GitHub Repo API | `github api` | 5 / 36 | andok/github-api-scraper (3) | 5/2.12/4.48/5 | 32.3 |
| 23 | `shopify-store-products-api` | Shopify Store Scraper & Products API | `shopify products api` | 2 / 212 | sourcing-data-studio/shopify-products-api (1) | 4/2.36/4.27/5 | 32.3 |
| 24 | `web-search-api` | Web Search API for AI Agents | `web search api` | 10 / 2427 | tugelbay/rag-web-browser (8) | 5/3.24/4.15/3 | 32.2 |
| 25 | `seo-audit-api` | SEO Audit API | `seo audit api` | 8 / 499 | fetchbase/website-seo-audit (2) | 4/2.82/4.4/4 | 31.7 |
| 26 | `product-page-extractor-api` | Product Data Extractor API | `product data extractor` | 17 / 323 | azzouzana/canadiantire-ca-scraper (5) | 4/2.88/4.23/4 | 31.1 |
| 27 | `companies-house-api` | Companies House API | `companies house api` | 3 / 90 | nexgendata/uk-startup-funding-tracker (1) | 4/2.23/4.47/5 | 30.3 |
| 28 | `semantic-scholar-api` | Semantic Scholar API | `semantic scholar api` | 4 / 66 | gochujang/semantic-scholar-papers (1) | 4/2.21/4.48/5 | 30.2 |
| 29 | `youtube-video-details-api` | YouTube Video Details API | `youtube video info api` | 8 / 740 | coder2077/youtube-video-info (0) | 4/2.91/4.25/4 | 30.0 |
| 30 | `y-combinator-companies-api` | Y Combinator Companies API | `y combinator companies` | 47 / 172 | haketa/ycombinator-companies-scraper (19) | 3/2.96/4.21/5 | 29.9 |

## 5. Which 100 to build first (batches of 10)

Order follows the score, with two manual rules: (a) each batch mixes 2–3 cheap open-API wrappers with heavier scraper builds so a batch ships in about a week; (b) buildability-2 items (bot-walled giants) are pushed out of the first 100 unless the owner explicitly accepts proxy cost and maintenance. Titles must carry the primary query words verbatim; descriptions end with "Unofficial <X> API."; every actor pay-per-event, no rental (rental actors are invisible to MCP `search-actors`).

**Batch 1** — `web-fetch-api`, `google-news-api`, `website-screenshot-api`, `pdf-to-markdown-api`, `article-extractor-api`, `careers-page-jobs-api`, `markdown-site-crawler`, `url-to-markdown-api`, `news-search-api`, `pagespeed-api`

**Batch 2** — `company-enrichment-api`, `reddit-api`, `google-search-api`, `youtube-channel-api`, `trustpilot-api`, `url-status-checker-api`, `ocr-api`, `office-document-to-text-api`, `app-store-api`, `google-reviews-api`

**Batch 3** — `weather-api`, `github-repo-api`, `shopify-store-products-api`, `web-search-api`, `seo-audit-api`, `product-page-extractor-api`, `companies-house-api`, `semantic-scholar-api`, `youtube-video-details-api`, `y-combinator-companies-api`

**Batch 4** — `google-docs-sheets-reader`, `google-autocomplete-api`, `google-places-api`, `translation-api`, `youtube-search-api`, `phone-number-validation-api`, `arxiv-api`, `stock-price-api`, `js-render-api`, `government-tenders-api`

**Batch 5** — `tripadvisor-api`, `json-ld-extractor-api`, `keyword-rank-checker-api`, `wikipedia-api`, `duckduckgo-search-api`, `website-contact-extractor-api`, `link-extractor-api`, `link-preview-api`, `google-flights-api`, `airbnb-api`

**Batch 6** — `ebay-api`, `stock-photos-api`, `company-logo-api`, `cve-vulnerability-api`, `html-table-extractor-api`, `email-verification-api`, `youtube-comments-api`, `stack-overflow-api`, `google-shopping-api`, `company-financials-api`

**Batch 7** — `ai-extractor-api`, `geocoding-api`, `sports-scores-api`, `financial-news-api`, `patent-search-api`, `yelp-api`, `url-to-pdf-api`, `pubmed-api`, `npm-package-api`, `press-release-api`

**Batch 8** — `website-ranking-api`, `trademark-search-api`, `crypto-price-api`, `hugging-face-api`, `rss-feed-finder-api`, `exchange-rate-api`, `vscode-marketplace-api`, `pypi-package-api`, `ai-crawler-access-checker`, `ticketmaster-events-api`

**Batch 9** — `css-selector-scraper-api`, `forum-scraper-api`, `doi-lookup-api`, `ip-geolocation-api`, `recipe-scraper-api`, `disposable-email-checker-api`, `dice-jobs-api`, `domain-availability-api`, `website-change-monitor-api`, `booking-com-api`

**Batch 10** — `yellow-pages-api`, `etsy-api`, `pdf-table-extraction-api`, `notion-page-reader`, `capterra-api`, `medium-api`, `earnings-calendar-api`, `clinical-trials-api`, `backlink-checker-api`, `public-holidays-api`

Held back (buildability 2: heavy bot walls, proxy cost, legal exposure) — build only with explicit owner sign-off: `amazon-product-api` (21.1), `zillow-api` (17.0), `google-scholar-api` (15.6), `indeed-api` (15.0), `walmart-api` (13.4), `audio-transcription-api` (13.3), `keyword-search-volume-api` (12.9), `g2-reviews-api` (12.5), `google-jobs-api` (12.4), `podcast-transcript-api` (11.7), `aliexpress-api` (11.6), `glassdoor-api` (11.3), `linkedin-jobs-api` (11.0).

The 31 scored candidates not in this first 100 (lower scores or buildability 2) are ranked in `candidates.json`.

## 6. Quick wins on existing actors (not counted in the 100)

These need a retitle/description change, not a build; each already ranks or nearly ranks for an agent phrase:

- `hacker-news-stories` → title "Hacker News API — Stories, Comments & Search" (currently #12 for `hacker news api`; top-3 there have 1/0/1 users).
- `sec-edgar-filings` → add "SEC EDGAR API" to the title (does not rank for `sec edgar api`; top-3 have 0/1/2 users).
- `yahoo-finance-quotes` → "Yahoo Finance API — Stock Quotes…" (#14 for `yahoo finance api`, #42 for `stock price api`; tops have 0–10 users).
- `youtube-transcript-fast` → "YouTube Transcript API — …" (#49 for `youtube transcript api`, a phrase whose top-3 have 51/12/41 users while `youtube transcript` has 2,531/3,144/3,729).
- `google-trends-reliable` → "Google Trends API — …" (not in top 10 for `google trends api`; tops have 5/3/18 users).
- `remote-jobs-aggregator` → "Remote Jobs API — …" (#43; tops 22/6/0).
- `website-tech-stack` → "Tech Stack Detector API / Wappalyzer API — …" (#67 for `wappalyzer api`; tops 14/1/26).
- `rss-feed-reader` → "RSS Feed API / RSS to JSON — …" (#7 and #16).
- `openstreetmap-places` → "OpenStreetMap API — Places/POI…" (#9; tops 3/11/0).
- `domain-whois-dns-ssl` → "WHOIS API, DNS Lookup API & SSL Checker" (#10/#6/#43).
- `google-play-apps-reviews` → "Google Play API — Apps, Reviews…" (#10; tops 1/0/1).
- `pdf-text-extractor` → "PDF to Text API" (#6 for `pdf to text api`) or fold into the new `pdf-to-markdown-api`.
- `apple-podcasts-shows-episodes` → "Apple Podcasts API" (#3) and `substack-posts` → "Substack API" (#8).

## 7. Honest expectations

**Users.** Our 87 actors average ~1 user/30d each. Other developers' exact-match "api" actors on uncontested phrases sit mostly at 5–50 users/30d, with a top decile at 100–600 (google-images-api 245, email-verifier 489, youtube-search-api 594, career-site-job-listing-api 1,577). A realistic distribution for 100 new actors after 3–6 months: ~40 at 0–5 users/30d, ~40 at 5–30, ~15 at 30–150, ~5 above 150. That is roughly 1,500–3,500 users/30d combined, versus 98 today.

**Revenue.** Pay-per-event revenue per active user is low: most Store users run small free-tier jobs; a typical actor earns $1–5 per active user per month, and the Store takes its share. With the distribution above: ~$1.5k–6k/month in gross actor revenue at steady state, with the large majority coming from 10–15 actors. The cheap open-API wrappers (Wikipedia, arXiv, npm, weather, exchange rates) will likely each earn under $20/month but cost under a day to build and raise the catalog's search footprint; the mid-size scrapers (news, screenshots, PDF, careers pages, company enrichment, Google Places/Reviews) carry the revenue case. Proxy-heavy actors (Google SERP, Google Places, Reddit, Booking, flights) have real COGS: budget $1–4 per 1k results in Apify proxy/compute before margin.

**What could make this fail.**

- Store ranking changes: the measured "exact title words rank within hours" behaviour and the "Unofficial <X> API" trick are ranking quirks Apify can change at any time (they already weight a quality score in MCP ranking). Diversify: real READMEs, output schemas that match the description, reviews.
- Apify's own defaults: MCP agents start with `apify/web-fetch` and `apify/rag-web-browser`; agents that already have fetch/search rarely search for another one. The fetch/markdown candidates win Store-search users, not default-tool users.
- Agents that reach an actor via `fetch-actor-details` read the inferred output schema — if the first runs produce thin or inconsistent datasets, the schema looks wrong and the agent moves on. Seed every new actor with a few clean public runs.
- Official free APIs (Wikipedia, arXiv, PubMed, CoinGecko, Open-Meteo, GitHub, npm, PyPI): a capable agent with HTTP access calls them directly; the actors sell convenience, keyless access and rate-limit pooling. Users here will be fewer but the builds are nearly free.
- Copycats: nothing in this list is defensible; once a phrase shows users, other developers clone the title within weeks (the sweep shows 10–40 near-identical actors on many queries). Speed and being first on the phrase is the edge; expect erosion.
- Bot walls and ToS: Amazon, Walmart, Zillow, Indeed, LinkedIn jobs, G2, Glassdoor, Booking, Yelp and Google SERP all need residential or SERP proxies and periodic repair; margins can go negative on the free tier. The first 100 excludes buildability-2 items for this reason.
- Rental-pricing retirement and pricing changes on Apify's side could change per-event economics; keep all actors pay-per-event.
- Demand proxies are indirect: Store search counts are not visible; users/30d of incumbents measures satisfied demand, not searches. Phrases where every incumbent is weak may be weak because nobody searches them (e.g. `wayback machine api`, `ev charging stations api`).

## 8. Files

- `candidates.json` — all scored candidates (slug, title proposal, description with "Unofficial <X> API.", target queries, input essentials, output fields, pricing per 1k vs incumbents, competition summary, per-query metrics, top-3 incumbents with price per 1k where pay-per-event, scores, risks).
- `queries_metrics.csv` — the 833 swept queries with total results, top-3 users/30d, weak/stale/unreviewed counts, our rank and the top-3 actors.
- `store_category_snapshot.json` — the AGENTS and MCP_SERVERS category pages (top 100 each) and our 87 actors as returned by the Store API on 2026-10-19.