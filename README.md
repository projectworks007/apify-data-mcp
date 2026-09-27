# Data tools for AI agents (MCP)

Ready-made remote MCP servers that give Claude, ChatGPT, Cursor, VS Code and other MCP clients live data tools: job ads, property, car and marketplace listings, Google Maps business leads, AI-search brand visibility, YouTube transcripts and more.

Each tool is an [Apify](https://apify.com) Actor, served by Apify's hosted MCP server (`mcp.apify.com`). Connect with your Apify account (the client opens a sign-in page, or send `Authorization: Bearer <APIFY_TOKEN>`). Runs are billed to your Apify account per result, at each Actor's pay-per-event price; Apify's free plan includes a monthly usage credit.

## Servers

| Server | What it gives your agent | Tools |
|---|---|---|
| [Job Boards Data](#job-boards) | Live job ads from StepStone, XING, Welcome to the Jungle, Naukri, JobStreet and more. | 7 |
| [Real Estate Listings Data](#real-estate-listings) | Property listings for sale and rent from immowelt, Fotocasa, Immoweb, Otodom, Redfin, realtor.com. | 6 |
| [Marketplace Listings Data](#marketplace-listings) | Classified ads from Kleinanzeigen (Germany) and second-hand items from Vinted's 27 country sites. | 2 |
| [Google Maps Business Leads](#google-maps-leads) | Business e-mails and leads from Google Maps, with every address graded (MX, SPF, DMARC). | 1 |
| [AI Search Brand Visibility](#ai-search-visibility) | See how ChatGPT, Perplexity, Gemini and Google AI Overviews mention and cite your brand. | 1 |
| [YouTube Transcripts](#youtube-transcripts) | Transcripts of YouTube videos, playlists and channels with timestamps; SRT or WebVTT too. | 1 |

## Connect

**Claude (claude.ai / Claude Desktop):** Settings → Connectors → Add custom connector → paste a server URL from below.

**Cursor, VS Code, Windsurf and other clients** (`mcp.json`):

```json
{
  "mcpServers": {
    "job-boards": { "url": "https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs" }
  }
}
```

You can combine tools from several servers in one URL: `https://mcp.apify.com/?tools=<actor>,<actor>,…`.

<a id="job-boards"></a>
## Job Boards Data

Search live job ads by keyword and place on national job boards. Title, company, location, salary where published, dates, full ad text. No recruiter names or phone numbers.

| Tool | What it returns |
|---|---|
| [Welcome to the Jungle](https://apify.com/highbrow_fame/welcome-to-the-jungle-jobs) | Job ads from Welcome to the Jungle: title, company, size, sectors, offices, contract, remote policy, salary, experience, date and the full ad. Search links, keywords or places. No recruiter names. |
| [StepStone](https://apify.com/highbrow_fame/stepstone-jobs) | German jobs from StepStone.de: title, company, location, contract type, full/part time, home office, posted date, the full job ad and StepStone's salary estimate. No recruiter names or phones. |
| [Naukri.com](https://apify.com/highbrow_fame/naukri-jobs) | India job ads from naukri.com: title, company or consultant, experience, salary with min/max in rupees and lakhs, locations, work mode, skills, posted date, and the full ad if you want. No phones. |
| [Naukrigulf](https://apify.com/highbrow_fame/naukrigulf-jobs) | Gulf job ads from naukrigulf.com (UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain): title, company or consultant, experience, salary in local currency and US$, skills, posted date. No phones. |
| [JobStreet & JobsDB](https://apify.com/highbrow_fame/jobstreet-jobsdb-jobs) | JobStreet and JobsDB jobs from Malaysia, Singapore, the Philippines, Indonesia, Hong Kong and Thailand: company, salary with numbers, work type, category, date and the full ad. No phones. |
| [XING Jobs](https://apify.com/highbrow_fame/xing-jobs) | Job ads from XING in Germany, Austria and Switzerland: title, company, town, type, career level, remote, salary (published or XING's estimate), dates and the full ad. No contact persons, no phones. |
| [Foundit](https://apify.com/highbrow_fame/foundit-jobs) | Job ads from foundit (ex Monster) in India, the Gulf, Singapore, Malaysia, Hong Kong, the Philippines and Indonesia: title, company, experience, salary, places, skills, date, full ad. No phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs`

Registry name: `io.github.projectworks007/job-boards`

<a id="real-estate-listings"></a>
## Real Estate Listings Data

Search property listings to buy or rent on national property portals: price, area, rooms, location, agency and listing details. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Fotocasa](https://apify.com/highbrow_fame/fotocasa-properties) | Spanish property listings from fotocasa.es, to buy or rent: price, price drops, m², bedrooms, floor, district, amenities, photos, agency, and optionally the energy certificate. No phones. |
| [Immowelt](https://apify.com/highbrow_fame/immowelt-properties) | German property listings from immowelt, to rent or for sale: price, cold and warm rent, living area, rooms, floor, city, district, postcode, energy class and seller type. No phones. |
| [Redfin](https://apify.com/highbrow_fame/redfin-properties) | US homes from Redfin: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, days on market, address, map point, MLS id, broker. No agent names or phones. |
| [Immoweb](https://apify.com/highbrow_fame/immoweb-properties) | Belgian property listings from Immoweb, for sale or to rent: price, bedrooms, living area, EPC, town and postcode, agency, and optionally the description and building details. No phones. |
| [Otodom](https://apify.com/highbrow_fame/otodom-properties) | Polish property listings from Otodom, for sale or to rent: price, price per m², area, rooms, floor, district, seller type, and optionally coordinates and building details. No phones. |
| [Realtor.com](https://apify.com/highbrow_fame/realtor-properties) | US homes from Realtor.com: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, list and sold dates, address, map point, MLS id, brokerage. No agent names or phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/fotocasa-properties,highbrow_fame/immowelt-properties,highbrow_fame/redfin-properties,highbrow_fame/immoweb-properties,highbrow_fame/otodom-properties,highbrow_fame/realtor-properties`

Registry name: `io.github.projectworks007/real-estate-listings`

<a id="marketplace-listings"></a>
## Marketplace Listings Data

Search classified ads and second-hand listings on national marketplaces: title, price, condition, location, photos, seller type. No seller usernames or phone numbers.

| Tool | What it returns |
|---|---|
| [Kleinanzeigen](https://apify.com/highbrow_fame/kleinanzeigen-listings) | German classifieds from kleinanzeigen.de: marketplace, cars, flats, houses, jobs. Price, postcode and town, date, category, seller type, car and flat facts. Private sellers stay anonymous. |
| [Vinted](https://apify.com/highbrow_fame/vinted-listings) | Vinted listings from 27 country sites by search link or keyword: title, brand, size, condition, price, buyer fee, favourites, photo. Reads past Vinted's 960 cap. No seller usernames. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/kleinanzeigen-listings,highbrow_fame/vinted-listings`

Registry name: `io.github.projectworks007/marketplace-listings`

<a id="google-maps-leads"></a>
## Google Maps Business Leads

Find local businesses on Google Maps by search term and place and collect their public business e-mails: the tool finds each website's contact page under its native name (impressum, kontakt, contatti and more in ten languages) and grades every address with MX, SPF, DMARC and catch-all checks.

| Tool | What it returns |
|---|---|
| [google-maps-email-extractor](https://apify.com/highbrow_fame/google-maps-email-extractor) |  |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-maps-email-extractor`

Registry name: `io.github.projectworks007/google-maps-leads`

<a id="ai-search-visibility"></a>
## AI Search Brand Visibility

See how ChatGPT, Perplexity, Gemini and Google AI Overviews cite your brand: citations, share of voice against competitors, and the sources AI answers use. 24 languages. Start with just your domain, no API key.

| Tool | What it returns |
|---|---|
| [ai-search-visibility-tracker](https://apify.com/highbrow_fame/ai-search-visibility-tracker) |  |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/ai-search-visibility-tracker`

Registry name: `io.github.projectworks007/ai-search-visibility`

<a id="youtube-transcripts"></a>
## YouTube Transcripts

Transcripts from YouTube videos, playlists and channels: timestamps, plain text, SRT or WebVTT. No browser, so it is fast. You pay only for transcripts delivered; videos without captions are free.

| Tool | What it returns |
|---|---|
| [youtube-transcript-fast](https://apify.com/highbrow_fame/youtube-transcript-fast) |  |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/youtube-transcript-fast`

Registry name: `io.github.projectworks007/youtube-transcripts`

## Notes

- The tools read public pages only. Listing tools leave out private persons' phone numbers and e-mail addresses.
- Found a problem or missing a field? Open an issue on the Actor's Apify page.
