# Data tools for AI agents (MCP)

Ready-made remote MCP servers that give Claude, ChatGPT, Cursor, VS Code and other MCP clients live data tools: job ads, property, car and marketplace listings, Google Maps business leads, AI-search brand visibility, YouTube transcripts and more.

Each tool is an [Apify](https://apify.com) Actor, served by Apify's hosted MCP server (`mcp.apify.com`). Connect with your Apify account (the client opens a sign-in page, or send `Authorization: Bearer <APIFY_TOKEN>`). Runs are billed to your Apify account per result, at each Actor's pay-per-event price; Apify's free plan includes a monthly usage credit.

## Servers

| Server | What it gives your agent | Tools |
|---|---|---|
| [Job Boards Data](#job-boards) | Live job ads from StepStone, XING, Welcome to the Jungle, Naukri, JobStreet and more. | 15 |
| [Job Boards Data (part 2)](#job-boards-2) | Live job ads from StepStone, XING, Welcome to the Jungle, Naukri, JobStreet and more. | 10 |
| [Real Estate Listings Data](#real-estate-listings) | Property listings for sale and rent from immowelt, Fotocasa, Immoweb, Otodom, Redfin, realtor.com. | 15 |
| [Real Estate Listings Data (part 2)](#real-estate-listings-2) | Property listings for sale and rent from immowelt, Fotocasa, Immoweb, Otodom, Redfin, realtor.com. | 1 |
| [Car & Vehicle Listings Data](#vehicle-listings) | Used and new car listings with prices and specs from national car marketplaces. | 2 |
| [Marketplace Listings Data](#marketplace-listings) | Classified ads from Kleinanzeigen (Germany) and second-hand items from Vinted's 27 country sites. | 9 |
| [Google Maps Business Leads](#google-maps-leads) | Business e-mails and leads from Google Maps, with every address graded (MX, SPF, DMARC). | 1 |
| [AI Search Brand Visibility](#ai-search-visibility) | See how ChatGPT, Perplexity, Gemini and Google AI Overviews mention and cite your brand. | 1 |
| [YouTube Transcripts](#youtube-transcripts) | Transcripts of YouTube videos, playlists and channels with timestamps; SRT or WebVTT too. | 1 |
| [App & Game Store Data](#app-store-data) | Apps, games and extensions with ratings and user reviews from app stores, Steam and Chrome. | 3 |
| [News & Trends Data](#news-and-trends) | Google Trends, Google News, Hacker News, Substack posts and podcasts for research and monitoring. | 4 |
| [E-commerce Product Data](#ecommerce-products) | Product catalogues, prices and stock from online stores and supermarkets. | 3 |
| [Events Data](#events-data) | Events with dates, venues, prices and organisers from Eventbrite and Meetup. | 2 |
| [Finance & Filings Data](#finance-data) | Stock quotes, price history and fundamentals, plus SEC EDGAR company filings. | 2 |
| [Hotel Prices Data](#hotel-prices) | Every booking site's price for chosen hotels and dates on Google Hotels. | 1 |
| [Web & Developer Data Tools](#web-and-dev-tools) | Website tech stacks, domain WHOIS/DNS/SSL, sitemaps, PDF text, GitHub trending and more. | 8 |

## Connect

**Claude (claude.ai / Claude Desktop):** Settings → Connectors → Add custom connector → paste a server URL from below.

**Cursor, VS Code, Windsurf and other clients** (`mcp.json`):

```json
{
  "mcpServers": {
    "job-boards": { "url": "https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs,highbrow_fame/arbeitsagentur-jobs,highbrow_fame/infojobs-jobs,highbrow_fame/reed-jobs,highbrow_fame/remote-jobs-aggregator,highbrow_fame/hellowork-jobs,highbrow_fame/totaljobs-jobs,highbrow_fame/rozee-jobs,highbrow_fame/mycareersfuture-jobs" }
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
| [StepStone](https://apify.com/highbrow_fame/stepstone-jobs) | StepStone jobs from stepstone.de, Germany: title, company, location, contract type, home office, posted date, full job ad and salary estimate. No recruiter names. Unofficial StepStone API. |
| [Naukri.com](https://apify.com/highbrow_fame/naukri-jobs) | Naukri jobs from naukri.com, India: title, company, experience, salary in rupees and lakhs, locations, work mode, skills, posted date, full ad on request. No phones. Unofficial Naukri API. |
| [Naukrigulf](https://apify.com/highbrow_fame/naukrigulf-jobs) | Gulf job ads from naukrigulf.com (UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain): title, company or consultant, experience, salary in local currency and US$, skills, posted date. No phones. |
| [JobStreet & JobsDB](https://apify.com/highbrow_fame/jobstreet-jobsdb-jobs) | JobStreet and JobsDB jobs from Malaysia, Singapore, Philippines, Indonesia, Hong Kong and Thailand: company, salary, work type, category, date and the full ad. Unofficial JobStreet and JobsDB API. |
| [XING Jobs](https://apify.com/highbrow_fame/xing-jobs) | XING jobs in Germany, Austria and Switzerland: title, company, town, type, career level, remote, salary (published or estimated), dates and the full ad. No contact persons. Unofficial XING API. |
| [Foundit](https://apify.com/highbrow_fame/foundit-jobs) | Job ads from foundit (ex Monster) in India, the Gulf, Singapore, Malaysia, Hong Kong, the Philippines and Indonesia: title, company, experience, salary, places, skills, date, full ad. No phones. |
| [Arbeitsagentur](https://apify.com/highbrow_fame/arbeitsagentur-jobs) | Job ads from the German Federal Employment Agency's Jobsuche: title, employer, place, working time, contract, salary, start and publication dates, and the full ad text. No phones, no contact persons. |
| [InfoJobs](https://apify.com/highbrow_fame/infojobs-jobs) | InfoJobs job offers in Spain: title, company, town and province, salary min/max, contract, working day, remote, full ad, applications, experience and studies asked. No names. Unofficial InfoJobs API. |
| [Reed.co.uk](https://apify.com/highbrow_fame/reed-jobs) | Reed jobs from reed.co.uk, UK: title, company, employer or agency, location, salary with min/max/period, contract type, hours, remote/hybrid, dates, full ad on request. No phones. Unofficial Reed API. |
| [Remote Jobs](https://apify.com/highbrow_fame/remote-jobs-aggregator) | Remote jobs from Himalayas, Remote OK, We Work Remotely and Arbeitnow in one list: title, company, salary, location rules, tags, date and apply link. Duplicates removed. |
| [HelloWork](https://apify.com/highbrow_fame/hellowork-jobs) | French job ads from HelloWork: title, company, city, département, contract (CDI, CDD, intérim, alternance, stage), salary min/max, remote work, date, full ad. No phones. |
| [Totaljobs & CWJobs](https://apify.com/highbrow_fame/totaljobs-jobs) | UK jobs from Totaljobs and CWJobs: title, company, location, salary as text and as min/max/period, contract type, posted date and the full job ad. No recruiter names or phones. |
| [Rozee.pk](https://apify.com/highbrow_fame/rozee-jobs) | Scrape job ads from rozee.pk, Pakistan's job board: title, company, city, salary in PKR, experience, job type, shift, posted and apply-before dates, skills and the full ad. No phones. |
| [MyCareersFuture](https://apify.com/highbrow_fame/mycareersfuture-jobs) | Singapore jobs from MyCareersFuture: title, company, salary range in SGD, employment type, level, experience, skills, category, district, dates and the full ad. No phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs,highbrow_fame/arbeitsagentur-jobs,highbrow_fame/infojobs-jobs,highbrow_fame/reed-jobs,highbrow_fame/remote-jobs-aggregator,highbrow_fame/hellowork-jobs,highbrow_fame/totaljobs-jobs,highbrow_fame/rozee-jobs,highbrow_fame/mycareersfuture-jobs`

Registry name: `io.github.projectworks007/job-boards`

<a id="job-boards-2"></a>
## Job Boards Data (part 2)

Search live job ads by keyword and place on national job boards. Title, company, location, salary where published, dates, full ad text. No recruiter names or phone numbers.

| Tool | What it returns |
|---|---|
| [No Fluff Jobs](https://apify.com/highbrow_fame/nofluffjobs-jobs) | IT jobs from nofluffjobs.com (Poland, Czechia, Slovakia, Hungary, Ukraine): title, company, cities, remote, seniority, salary per contract type (B2B net / UoP gross), skills, dates, full ad. |
| [jobs.ch & jobup.ch](https://apify.com/highbrow_fame/jobs-ch-jobs) | Swiss job ads from jobs.ch and jobup.ch: title, company, place, workload %, contract type, salary when published, date, snippet and optionally the full ad. Contact persons and phones taken out. |
| [Jobs.cz & Prace.cz](https://apify.com/highbrow_fame/jobs-cz-jobs) | Czech job ads from Jobs.cz and Prace.cz: title, company, place, salary in numbers, on-site/hybrid/remote, posting date, and optionally the full ad text. No contact persons, no phones. |
| [karriere.at](https://apify.com/highbrow_fame/karriere-at-jobs) | Job ads from karriere.at, Austria's largest job board: title, company, places, employment type, salary with minimum and period, posting date and the full ad text. No contact persons, no phones. |
| [stellenanzeigen.de](https://apify.com/highbrow_fame/stellenanzeigen-jobs) | Job ads from stellenanzeigen.de, a big German job board: title, company, places, hours, contract type, home office, salary, benefits, dates and the full ad text. No contact persons, no phones. |
| [BestJobs](https://apify.com/highbrow_fame/bestjobs-ro-jobs) | Romanian job ads from BestJobs (bestjobs.eu): title, company, towns, salary in EUR, employment type, level, remote/hybrid, languages, benefits and the full ad. Links or keywords + towns. |
| [Profession.hu](https://apify.com/highbrow_fame/profession-hu-jobs) | Hungarian job ads from Profession.hu: title, company, place, home office, salary parsed into numbers, category, contract type, posting date and the full ad text. By link, keyword or place. No phones. |
| [PNet](https://apify.com/highbrow_fame/pnet-jobs) | South African jobs from PNet: title, company, location, salary as text and as min/max/period, contract type, EE/AA, posted date and the full job ad. No recruiter names or phones. |
| [Elempleo](https://apify.com/highbrow_fame/elempleo-jobs) | Job offers from elempleo.com (Colombia): title, company, city, salary band in COP, contract, work modality, experience, education, full description. Search links or keywords. No phones. |
| [Job Bank Canada](https://apify.com/highbrow_fame/job-bank-canada-jobs) | Jobs from Job Bank, the Government of Canada job board, in English or French: title, employer, city, salary parsed, posted date, source and, if you want, the full ad. No phones or e-mails. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/nofluffjobs-jobs,highbrow_fame/jobs-ch-jobs,highbrow_fame/jobs-cz-jobs,highbrow_fame/karriere-at-jobs,highbrow_fame/stellenanzeigen-jobs,highbrow_fame/bestjobs-ro-jobs,highbrow_fame/profession-hu-jobs,highbrow_fame/pnet-jobs,highbrow_fame/elempleo-jobs,highbrow_fame/job-bank-canada-jobs`

Registry name: `io.github.projectworks007/job-boards-2`

<a id="real-estate-listings"></a>
## Real Estate Listings Data

Search property listings to buy or rent on national property portals: price, area, rooms, location, agency and listing details. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Fotocasa](https://apify.com/highbrow_fame/fotocasa-properties) | Spanish property listings from fotocasa.es, to buy or rent: price, price drops, m², bedrooms, floor, district, amenities, photos, agency, and optionally the energy certificate. No phones. |
| [Immowelt](https://apify.com/highbrow_fame/immowelt-properties) | German property listings from immowelt, to rent or for sale: price, cold and warm rent, living area, rooms, floor, city, district, postcode, energy class and seller type. No phones. |
| [Redfin](https://apify.com/highbrow_fame/redfin-properties) | Redfin homes in the US: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, days on market, address, map point, MLS id, broker. No agent names. Unofficial Redfin API. |
| [Immoweb](https://apify.com/highbrow_fame/immoweb-properties) | Immoweb property listings in Belgium, for sale or to rent: price, bedrooms, living area, EPC, town and postcode, agency, and optionally description and building details. Unofficial Immoweb API. |
| [Otodom](https://apify.com/highbrow_fame/otodom-properties) | Otodom property listings in Poland, for sale or to rent: price, price per m², area, rooms, floor, district, seller type, and optionally coordinates and building details. Unofficial Otodom API. |
| [Realtor.com](https://apify.com/highbrow_fame/realtor-properties) | Realtor.com homes in the US: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, list and sold dates, address, MLS id, brokerage. No agent names. Unofficial Realtor.com API. |
| [Rightmove](https://apify.com/highbrow_fame/rightmove-properties) | Rightmove property listings, UK, for sale or to rent: price, bedrooms, type, tenure, size, address with coordinates, key features, price changes and the agent. No phones. Unofficial Rightmove API. |
| [ImmoScout24 Austria](https://apify.com/highbrow_fame/immoscout24-at-properties) | Austrian property listings from immobilienscout24.at, to buy or rent: price, size, rooms, postcode and town, agency, features, optional details and energy data. Private owners stay anonymous. |
| [Funda](https://apify.com/highbrow_fame/funda-properties) | Dutch property listings from funda.nl, for sale, to rent or sold: price, m², rooms, energy label, address, agency, and optionally coordinates and all characteristics. No phones. |
| [Magicbricks](https://apify.com/highbrow_fame/magicbricks-properties) | Indian property listings from Magicbricks, to buy or rent: price in INR, BHK, area, floor, furnishing, locality, society, amenities and who posted it. Any city. Owners stay anonymous. No phones. |
| [Property Finder](https://apify.com/highbrow_fame/propertyfinder-properties) | Listings from Property Finder in the UAE, Saudi Arabia, Qatar, Bahrain and Egypt: price, size, bedrooms, location, coordinates, amenities, completion, agency. For sale and to rent. No phones. |
| [NoBroker](https://apify.com/highbrow_fame/nobroker-properties) | Owner-posted homes from NoBroker (India) to rent, for sale and PG: rent or price, deposit, BHK, area, furnishing, tenant preference, floor, amenities, locality. No phones, no owner names. |
| [Pisos.com](https://apify.com/highbrow_fame/pisos-properties) | Spanish property listings from pisos.com, for sale or to rent: price, price drops, bedrooms, bathrooms, m², floor, zone, postcode, seller type and agency, and optionally the full details. No phones. |
| [Gratka & Morizon](https://apify.com/highbrow_fame/gratka-morizon-properties) | Polish property listings from Gratka.pl and Morizon.pl, for sale or to rent: price, price per m², area, rooms, floor, market, city and district, seller type, full description. No phones. |
| [Sreality](https://apify.com/highbrow_fame/sreality-properties) | Czech property listings from Sreality.cz — sale, rent, auctions: price, area, layout (2+kk), town, district, region, agency, photos, and optionally description, dates and building details. No phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/fotocasa-properties,highbrow_fame/immowelt-properties,highbrow_fame/redfin-properties,highbrow_fame/immoweb-properties,highbrow_fame/otodom-properties,highbrow_fame/realtor-properties,highbrow_fame/rightmove-properties,highbrow_fame/immoscout24-at-properties,highbrow_fame/funda-properties,highbrow_fame/magicbricks-properties,highbrow_fame/propertyfinder-properties,highbrow_fame/nobroker-properties,highbrow_fame/pisos-properties,highbrow_fame/gratka-morizon-properties,highbrow_fame/sreality-properties`

Registry name: `io.github.projectworks007/real-estate-listings`

<a id="real-estate-listings-2"></a>
## Real Estate Listings Data (part 2)

Search property listings to buy or rent on national property portals: price, area, rooms, location, agency and listing details. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Imovirtual](https://apify.com/highbrow_fame/imovirtual-properties) | Portuguese property listings from Imovirtual, for sale or to rent: price, price per m², area, typology, floor, council and parish, seller type, and optionally coordinates and energy rating. No phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/imovirtual-properties`

Registry name: `io.github.projectworks007/real-estate-listings-2`

<a id="vehicle-listings"></a>
## Car & Vehicle Listings Data

Search car and vehicle listings on national car marketplaces: make, model, price, mileage, year, fuel, gearbox, location and seller type. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Coches.net](https://apify.com/highbrow_fame/cochesnet-listings) | Used and km 0 cars from coches.net, Spain's big car marketplace: price and coches.net's price rating, year, km, fuel, gearbox, power, body, province and dealer. No phone numbers. |
| [AutoTrader.ca](https://apify.com/highbrow_fame/autotrader-ca-listings) | AutoTrader.ca car listings from any search link or a make, model and place: price, mileage, model year, trim, fuel, gearbox, place and dealer; body, colour and drivetrain on request. No phone numbers. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/cochesnet-listings,highbrow_fame/autotrader-ca-listings`

Registry name: `io.github.projectworks007/vehicle-listings`

<a id="marketplace-listings"></a>
## Marketplace Listings Data

Search classified ads and second-hand listings on national marketplaces: title, price, condition, location, photos, seller type. No seller usernames or phone numbers.

| Tool | What it returns |
|---|---|
| [Kleinanzeigen](https://apify.com/highbrow_fame/kleinanzeigen-listings) | Kleinanzeigen ads from kleinanzeigen.de, Germany: marketplace, cars, flats, houses, jobs. Price, postcode, town, date, category, seller type. Private sellers anonymous. Unofficial Kleinanzeigen API. |
| [Vinted](https://apify.com/highbrow_fame/vinted-listings) | Vinted listings from 27 country sites by search link or keyword: title, brand, size, condition, price, buyer fee, favourites, photo. Reads past the 960 cap. No usernames. Unofficial Vinted API. |
| [Gumtree](https://apify.com/highbrow_fame/gumtree-uk-listings) | UK listings from gumtree.com: stuff for sale, cars and vans, property to rent and for sale, pets. Price, area, category, car and property details. No phones; private sellers stay anonymous. |
| [Craigslist](https://apify.com/highbrow_fame/craigslist-listings) | craigslist listings from any city and section — for sale, housing, cars, jobs, gigs, services: title, price, place, date, category, images, and optionally description and attributes. No phones. |
| [Blocket](https://apify.com/highbrow_fame/blocket-listings) | Swedish classifieds from Blocket — the marketplace, cars, motorbikes, boats, caravans and machines: price, place, seller type, vehicle data, descriptions on request. No phones. |
| [OfferUp](https://apify.com/highbrow_fame/offerup-listings) | OfferUp listings around any US city or ZIP: price, condition, category, town and state, post date, firm price, photos, car make, model and mileage. Links or keywords. No phones, no seller names. |
| [Kijiji](https://apify.com/highbrow_fame/kijiji-listings) | Kijiji.ca listings from any category — buy & sell, cars, rentals, homes, jobs, pets: price, place, seller type, car and property details, optional full description. No phones. |
| [Subito](https://apify.com/highbrow_fame/subito-listings) | Italian listings from Subito.it: flats and houses, cars and motorbikes, marketplace items. Price, town, full ad text, rooms, m², make, km, seller type. Private sellers stay anonymous. No phones. |
| [FINN.no](https://apify.com/highbrow_fame/finn-listings) | Norwegian listings from FINN.no — Torget, cars, boats, homes for sale and rent, commercial property and jobs: price, place, seller type and company, details on request. No phones. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/kleinanzeigen-listings,highbrow_fame/vinted-listings,highbrow_fame/gumtree-uk-listings,highbrow_fame/craigslist-listings,highbrow_fame/blocket-listings,highbrow_fame/offerup-listings,highbrow_fame/kijiji-listings,highbrow_fame/subito-listings,highbrow_fame/finn-listings`

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

<a id="app-store-data"></a>
## App & Game Store Data

Look up apps, games and browser extensions and their user reviews on the App Store, Google Play, Steam and the Chrome Web Store: ratings, versions, prices, review text and dates.

| Tool | What it returns |
|---|---|
| [Google Play](https://apify.com/highbrow_fame/google-play-apps-reviews) | Google Play apps and reviews from links, searches or developers: installs, rating, histogram, price, ads, versions, and reviews with developer replies, no reviewer names. Unofficial Google Play API. |
| [Chrome Web Store](https://apify.com/highbrow_fame/chrome-web-store-extensions) | Chrome Web Store extensions and themes from searches, categories or ids: users, rating, rating count, version, last update, size, languages, permissions, publisher and privacy disclosures. |
| [Steam](https://apify.com/highbrow_fame/steam-games-reviews) | Steam games by id, link or search: price and discount, release date, developers, genres, Metacritic, review totals — plus the written reviews with playtime, no reviewer names. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-play-apps-reviews,highbrow_fame/chrome-web-store-extensions,highbrow_fame/steam-games-reviews`

Registry name: `io.github.projectworks007/app-store-data`

<a id="news-and-trends"></a>
## News & Trends Data

Research and monitoring data: Google Trends interest and trending searches, Google News articles, Hacker News stories, Substack posts, RSS feeds and podcast episodes.

| Tool | What it returns |
|---|---|
| [Google Trends](https://apify.com/highbrow_fame/google-trends-reliable) | Google Trends data you can rely on: interest over time, interest by region, and top and rising related searches for any keyword, country and period. Pay only for keywords with data. |
| [Substack](https://apify.com/highbrow_fame/substack-posts) | Substack posts from any publication: title, date, authors, likes, comments, restacks, word count, paid or free, tags and optionally the full text. Many publications per run. |
| [Hacker News](https://apify.com/highbrow_fame/hacker-news-stories) | Hacker News stories from the front page, new, best, Ask HN, Show HN and jobs, or from a search over all of HN: title, link, points, comments, date, and the comment threads. |
| [Apple Podcasts](https://apify.com/highbrow_fame/apple-podcasts-shows-episodes) | Apple Podcasts shows by link, search or top chart (any country and genre) with rating, publisher, genres and feed, plus their episodes with audio links. No login. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-trends-reliable,highbrow_fame/substack-posts,highbrow_fame/hacker-news-stories,highbrow_fame/apple-podcasts-shows-episodes`

Registry name: `io.github.projectworks007/news-and-trends`

<a id="ecommerce-products"></a>
## E-commerce Product Data

Product data from online stores and supermarkets: names, prices, promotions, stock, categories and product details.

| Tool | What it returns |
|---|---|
| [Coles Australia](https://apify.com/highbrow_fame/coles-au-products) | Coles grocery prices and specials by store for Coles Australia supermarket products: price, was-price, unit price, multi-buy, availability; barcode and nutrition on request. Unofficial Coles API. |
| [Woolworths Australia](https://apify.com/highbrow_fame/woolworths-au-products) | Woolworths grocery prices and specials for Woolworths Australia supermarket products: price, was-price, unit price, stock, barcode, ingredients, allergens, nutrition. Unofficial Woolworths API. |
| [ALDI Australia](https://apify.com/highbrow_fame/aldi-au-products) | ALDI Australia grocery prices and Special Buys: product search and category links. Price, unit price, pack size, brand, category, on-sale dates, Super Savers flags. Unofficial ALDI Australia API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/coles-au-products,highbrow_fame/woolworths-au-products,highbrow_fame/aldi-au-products`

Registry name: `io.github.projectworks007/ecommerce-products`

<a id="events-data"></a>
## Events Data

Find events by place, date and topic: title, dates, venue, price, organiser and event page.

| Tool | What it returns |
|---|---|
| [Eventbrite Events](https://apify.com/highbrow_fame/eventbrite-events) | Eventbrite events by city, keyword, category and date: start and end times, venue with address and coordinates, ticket prices, sales status and organizer. Many cities per run. |
| [Meetup](https://apify.com/highbrow_fame/meetup-events) | Meetup events by keyword and city, from search links, or from groups (upcoming or past): date, time zone, venue city, group, fee, going count, topics, description. No hosts or attendees. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/eventbrite-events,highbrow_fame/meetup-events`

Registry name: `io.github.projectworks007/events-data`

<a id="finance-data"></a>
## Finance & Filings Data

Market and company data: quotes, price history and fundamentals from Yahoo Finance, and company filings from SEC EDGAR.

| Tool | What it returns |
|---|---|
| [Yahoo Finance](https://apify.com/highbrow_fame/yahoo-finance-quotes) | Yahoo Finance quotes for stocks, ETFs, crypto, currencies and indexes: price, change, volume, P/E, market cap, dividends. Price history and fundamentals on request. Unofficial Yahoo Finance API. |
| [SEC EDGAR Filings](https://apify.com/highbrow_fame/sec-edgar-filings) | SEC EDGAR filings by ticker, CIK or full-text search: form, dates, accession number, document links, 8-K items, and optional XBRL key financials for 10-K/10-Q. Official SEC APIs. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/yahoo-finance-quotes,highbrow_fame/sec-edgar-filings`

Registry name: `io.github.projectworks007/finance-data`

<a id="hotel-prices"></a>
## Hotel Prices Data

Get every booking site's price for the hotels and check-in dates you choose, from Google Hotels: per night and per stay, with and without taxes, the official site's rate and free-cancellation dates. It prices the hotels you list; it does not search a city.

| Tool | What it returns |
|---|---|
| [Google Hotels Prices](https://apify.com/highbrow_fame/google-hotels-prices) | Unofficial Google Hotels scraper & Google Travel hotel prices API: type a city or paste hotel links and get every booking site's price for any check-in dates. Per night and total stay, with and without taxes, plus the official site's rate. Pay only for results with prices. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-hotels-prices`

Registry name: `io.github.projectworks007/hotel-prices`

<a id="web-and-dev-tools"></a>
## Web & Developer Data Tools

Utility tools for agents: detect a website's tech stack, check domains (WHOIS, DNS, SSL), list sitemap URLs, extract text from PDFs, read RSS feeds, and find trending GitHub repos, Hugging Face models and OpenStreetMap places.

| Tool | What it returns |
|---|---|
| [PDF Text Extractor](https://apify.com/highbrow_fame/pdf-text-extractor) | The text of any PDF at a public link — whole or page by page — with page count, word count and metadata. Scanned PDFs without text are flagged and not charged. |
| [Domain Checker](https://apify.com/highbrow_fame/domain-whois-dns-ssl) | Check many domains at once: registrar, creation and expiry dates, status, name servers, DNS records with SPF and DMARC, SSL certificate expiry, and where the website redirects. |
| [Website Tech Stack Detector](https://apify.com/highbrow_fame/website-tech-stack) | The technologies behind any website: CMS, e-commerce platform, frameworks, analytics and ad tags, CDN, hosting, payment and more, with versions where visible. Many sites per run. |
| [Sitemap Extractor](https://apify.com/highbrow_fame/sitemap-url-extractor) | Every URL in a website's sitemaps — found through robots.txt, nested indexes and .gz files followed — with last-modified date, change frequency, priority, images, hreflang and news tags. |
| [Domain Authority & Website Rank Checker](https://apify.com/highbrow_fame/domain-authority-rank) | Bulk domain authority checker on open data: a 0-100 link strength score, website rank, referring subnets and IPs for up to 10,000 domains per run, from the Common Crawl web graph and Majestic Million. |
| [RSS & Atom Feed Reader](https://apify.com/highbrow_fame/rss-feed-reader) | Read any RSS, Atom, RDF or JSON feed — or just give a website and its feed is found — into one list: title, link, date, author, categories, summary, content and image. |
| [OpenStreetMap Places](https://apify.com/highbrow_fame/openstreetmap-places) | Points of interest from OpenStreetMap by place or map box: restaurants, shops, hotels, pharmacies, 62 categories or any OSM tag, with address, coordinates, opening hours and website. |
| [GitHub Trending](https://apify.com/highbrow_fame/github-trending-repos) | GitHub Trending repositories by programming language, date range and spoken language: rank, stars gained today/this week/this month, total stars, forks, and optionally topics, license and dates. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/pdf-text-extractor,highbrow_fame/domain-whois-dns-ssl,highbrow_fame/website-tech-stack,highbrow_fame/sitemap-url-extractor,highbrow_fame/domain-authority-rank,highbrow_fame/rss-feed-reader,highbrow_fame/openstreetmap-places,highbrow_fame/github-trending-repos`

Registry name: `io.github.projectworks007/web-and-dev-tools`

## Notes

- The tools read public pages only. Listing tools leave out private persons' phone numbers and e-mail addresses.
- Found a problem or missing a field? Open an issue on the Actor's Apify page.
