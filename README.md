# Data tools for AI agents (MCP)

Ready-made remote MCP servers that give Claude, ChatGPT, Cursor, VS Code and other MCP clients live data tools: job ads, property, car and marketplace listings, Google Maps business leads, AI-search brand visibility, YouTube transcripts and more.

Each tool is an [Apify](https://apify.com) Actor, served by Apify's hosted MCP server (`mcp.apify.com`). Connect with your Apify account (the client opens a sign-in page, or send `Authorization: Bearer <APIFY_TOKEN>`). Runs are billed to your Apify account per result, at each Actor's pay-per-event price; Apify's free plan includes a monthly usage credit.

## Servers

| Server | What it gives your agent | Tools |
|---|---|---|
| [Job Boards Data](#job-boards) | Live job ads from StepStone, XING, Welcome to the Jungle, Naukri, JobStreet and more. | 15 |
| [Job Boards Data (part 2)](#job-boards-2) | Live job ads from StepStone, XING, Welcome to the Jungle, Naukri, JobStreet and more. | 11 |
| [Real Estate Listings Data](#real-estate-listings) | Property listings for sale and rent from immowelt, Fotocasa, Immoweb, Otodom, Redfin, realtor.com. | 15 |
| [Real Estate Listings Data (part 2)](#real-estate-listings-2) | Property listings for sale and rent from immowelt, Fotocasa, Immoweb, Otodom, Redfin, realtor.com. | 5 |
| [Car & Vehicle Listings Data](#vehicle-listings) | Used and new car listings with prices and specs from national car marketplaces. | 3 |
| [Marketplace Listings Data](#marketplace-listings) | Classified ads from Kleinanzeigen (Germany) and second-hand items from Vinted's 27 country sites. | 10 |
| [Google Maps Business Leads](#google-maps-leads) | Business e-mails and leads from Google Maps, with every address graded (MX, SPF, DMARC). | 1 |
| [AI Search Brand Visibility](#ai-search-visibility) | See how ChatGPT, Perplexity, Gemini and Google AI Overviews mention and cite your brand. | 4 |
| [YouTube Transcripts](#youtube-transcripts) | Transcripts of YouTube videos, playlists and channels with timestamps; SRT or WebVTT too. | 3 |
| [App & Game Store Data](#app-store-data) | Apps, games and extensions with ratings and user reviews from app stores, Steam and Chrome. | 4 |
| [News & Trends Data](#news-and-trends) | Google Trends, Google News, Hacker News, Substack posts and podcasts for research and monitoring. | 8 |
| [E-commerce Product Data](#ecommerce-products) | Product catalogues, prices and stock from online stores and supermarkets. | 5 |
| [Events Data](#events-data) | Events with dates, venues, prices and organisers from Eventbrite and Meetup. | 2 |
| [Finance & Filings Data](#finance-data) | Stock quotes, price history and fundamentals, plus SEC EDGAR company filings. | 2 |
| [Hotel Prices Data](#hotel-prices) | Every booking site's price for chosen hotels and dates on Google Hotels. | 1 |
| [Web Tools for AI Agents](#ai-agent-web-tools) | Web tools for AI agents: URL to clean Markdown, site crawl, screenshots, PDF/Office to text, OCR. | 9 |
| [Company Data](#company-data) | Company data for AI agents: enrich a domain, UK Companies House records, Y Combinator companies. | 3 |
| [Web & Developer Data Tools](#web-and-dev-tools) | Website tech stacks, domain WHOIS/DNS/SSL, sitemaps, PDF text, GitHub trending and more. | 10 |
| [Shopify Store Audits](#shopify-store-audits) | Audit Shopify stores: AI readiness, EU customs SKU/GTIN coverage, ScriptTags ending 1 Mar 2027. | 2 |

## Connect

**Claude (claude.ai / Claude Desktop):** Settings → Connectors → Add custom connector → paste a server URL from below.

**Cursor, VS Code, Windsurf and other clients** (`mcp.json`):

```json
{
  "mcpServers": {
    "job-boards": { "url": "https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs,highbrow_fame/arbeitsagentur-jobs,highbrow_fame/infojobs-jobs,highbrow_fame/reed-jobs,highbrow_fame/remote-jobs-aggregator,highbrow_fame/hellowork-jobs,highbrow_fame/totaljobs-jobs,highbrow_fame/mycareersfuture-jobs,highbrow_fame/nofluffjobs-jobs" }
  }
}
```

You can combine tools from several servers in one URL: `https://mcp.apify.com/?tools=<actor>,<actor>,…`.

<a id="job-boards"></a>
## Job Boards Data

Search live job ads by keyword and place on national job boards. Title, company, location, salary where published, dates, full ad text. No recruiter names or phone numbers.

| Tool | What it returns |
|---|---|
| [Welcome to the Jungle](https://apify.com/highbrow_fame/welcome-to-the-jungle-jobs) | Job ads from Welcome to the Jungle: title, company, size, sectors, offices, contract, remote policy, salary, experience, date and the full ad. Search links, keywords or places. No recruiter names. Unofficial Welcome to the Jungle API. |
| [StepStone](https://apify.com/highbrow_fame/stepstone-jobs) | StepStone jobs from stepstone.de, Germany: title, company, location, contract type, home office, posted date, full job ad and salary estimate. No recruiter names. Unofficial StepStone API. |
| [Naukri Jobs](https://apify.com/highbrow_fame/naukri-jobs) | Naukri jobs from naukri.com, India: title, company, experience, salary in rupees and lakhs, locations, work mode, skills, posted date, full ad on request. No phones. Unofficial Naukri API. |
| [Naukrigulf](https://apify.com/highbrow_fame/naukrigulf-jobs) | Gulf job ads from naukrigulf.com (UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain): title, company or consultant, experience, salary in local currency and US$, skills, posted date. No phones. |
| [JobStreet & JobsDB](https://apify.com/highbrow_fame/jobstreet-jobsdb-jobs) | JobStreet and JobsDB jobs from Malaysia, Singapore, Philippines, Indonesia, Hong Kong and Thailand: company, salary, work type, category, date and the full ad. Unofficial JobStreet and JobsDB API. |
| [XING Jobs](https://apify.com/highbrow_fame/xing-jobs) | XING jobs in Germany, Austria and Switzerland: title, company, town, type, career level, remote, salary (published or estimated), dates and the full ad. No contact persons. Unofficial XING API. |
| [Foundit](https://apify.com/highbrow_fame/foundit-jobs) | Job ads from foundit (ex Monster) in India, the Gulf, Singapore, Malaysia, Hong Kong, the Philippines and Indonesia: title, company, experience, salary, places, skills, date, full ad. No phones. Unofficial Foundit API. |
| [Arbeitsagentur](https://apify.com/highbrow_fame/arbeitsagentur-jobs) | Job ads from the German Federal Employment Agency's Jobsuche: title, employer, place, working time, contract, salary, start and publication dates, and the full ad text. No phones, no contact persons. Unofficial Arbeitsagentur API. |
| [InfoJobs](https://apify.com/highbrow_fame/infojobs-jobs) | InfoJobs job offers in Spain: title, company, town and province, salary min/max, contract, working day, remote, full ad, applications, experience and studies asked. No names. Unofficial InfoJobs API. |
| [Reed.co.uk](https://apify.com/highbrow_fame/reed-jobs) | Reed jobs from reed.co.uk, UK: title, company, employer or agency, location, salary with min/max/period, contract type, hours, remote/hybrid, dates, full ad on request. No phones. Unofficial Reed API. |
| [Remote Jobs API &](https://apify.com/highbrow_fame/remote-jobs-aggregator) | Remote jobs from Himalayas, Remote OK, We Work Remotely and Arbeitnow in one list: title, company, salary, location rules, tags, date and apply link. Duplicates removed. Remote jobs API. |
| [HelloWork](https://apify.com/highbrow_fame/hellowork-jobs) | French job ads from HelloWork: title, company, city, département, contract (CDI, CDD, intérim, alternance, stage), salary min/max, remote work, date, full ad. No phones. Unofficial HelloWork API. |
| [Totaljobs & CWJobs](https://apify.com/highbrow_fame/totaljobs-jobs) | UK jobs from Totaljobs and CWJobs: title, company, location, salary as text and as min/max/period, contract type, posted date and the full job ad. No recruiter names or phones. |
| [MyCareersFuture](https://apify.com/highbrow_fame/mycareersfuture-jobs) | Singapore jobs from MyCareersFuture: title, company, salary range in SGD, employment type, level, experience, skills, category, district, dates and the full ad. No phones. Unofficial MyCareersFuture API. |
| [No Fluff Jobs](https://apify.com/highbrow_fame/nofluffjobs-jobs) | No Fluff Jobs IT jobs API: title, company, remote, seniority, salary per contract type and skills for $1.50 per 1,000 jobs. nofluffjobs.com in Poland, Czechia, Slovakia, Hungary, Ukraine; cities, B2B net / UoP gross, dates, full ad. Unofficial No Fluff Jobs API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/welcome-to-the-jungle-jobs,highbrow_fame/stepstone-jobs,highbrow_fame/naukri-jobs,highbrow_fame/naukrigulf-jobs,highbrow_fame/jobstreet-jobsdb-jobs,highbrow_fame/xing-jobs,highbrow_fame/foundit-jobs,highbrow_fame/arbeitsagentur-jobs,highbrow_fame/infojobs-jobs,highbrow_fame/reed-jobs,highbrow_fame/remote-jobs-aggregator,highbrow_fame/hellowork-jobs,highbrow_fame/totaljobs-jobs,highbrow_fame/mycareersfuture-jobs,highbrow_fame/nofluffjobs-jobs`

Registry name: `io.github.projectworks007/job-boards`

<a id="job-boards-2"></a>
## Job Boards Data (part 2)

Search live job ads by keyword and place on national job boards. Title, company, location, salary where published, dates, full ad text. No recruiter names or phone numbers.

| Tool | What it returns |
|---|---|
| [jobs.ch & jobup.ch](https://apify.com/highbrow_fame/jobs-ch-jobs) | Swiss job ads from jobs.ch and jobup.ch: title, company, place, workload %, contract type, salary when published, date, snippet and optionally the full ad. Contact persons and phones taken out. Unofficial jobs.ch API. |
| [Jobs.cz & Prace.cz](https://apify.com/highbrow_fame/jobs-cz-jobs) | Czech job ads from Jobs.cz and Prace.cz: title, company, place, salary in numbers, on-site/hybrid/remote, posting date, and optionally the full ad text. No contact persons, no phones. Unofficial Jobs.cz API. |
| [karriere.at](https://apify.com/highbrow_fame/karriere-at-jobs) | Job ads from karriere.at, Austria's largest job board: title, company, places, employment type, salary with minimum and period, posting date and the full ad text. No contact persons, no phones. Unofficial karriere.at API. |
| [stellenanzeigen.de](https://apify.com/highbrow_fame/stellenanzeigen-jobs) | stellenanzeigen.de jobs API: title, company, places, salary, contract type and full ad text for $1.20 per 1,000 jobs. Job ads from a big German job board: hours, home office, benefits, dates. No contact persons, no phones. Unofficial Stellenanzeigen.de API. |
| [BestJobs](https://apify.com/highbrow_fame/bestjobs-ro-jobs) | Romanian job ads from BestJobs (bestjobs.eu): title, company, towns, salary in EUR, employment type, level, remote/hybrid, languages, benefits and the full ad. Links or keywords + towns. Unofficial BestJobs API. Europe job scraper, job ads scraper, Romania job board. |
| [PNet](https://apify.com/highbrow_fame/pnet-jobs) | PNet jobs API: South African job title, company, location, parsed salary, contract type and full ad for $0.90 per 1,000 jobs. pnet.co.za, EE/AA, posted date. No recruiter names or phones. Unofficial PNet API. |
| [Elempleo](https://apify.com/highbrow_fame/elempleo-jobs) | Job offers from elempleo.com (Colombia): title, company, city, salary band in COP, contract, work modality, experience, education, full description. Search links or keywords. No phones. Unofficial elempleo API. |
| [Job Bank Canada](https://apify.com/highbrow_fame/job-bank-canada-jobs) | Jobs from Job Bank, the Government of Canada job board, in English or French: title, employer, city, salary parsed, posted date, source and, if you want, the full ad. No phones or e-mails. Unofficial Job Bank Canada API. |
| [MojPosao](https://apify.com/highbrow_fame/mojposao-jobs) | MojPosao jobs API: Croatian job title, company, places, salary in EUR, employment type, remote and full ad for $1.20 per 1,000 jobs. mojposao.hr, education, languages. Links or keywords + places. Unofficial MojPosao API. |
| [Arbeidsplassen](https://apify.com/highbrow_fame/arbeidsplassen-nav-jobs) | Job ads from Arbeidsplassen (NAV), Norway's public job board: title, employer, place, occupation, employment type, full-/part-time, sector, dates, apply link, full text. No contacts, no phones. Unofficial Arbeidsplassen API. |
| [Careers Page](https://apify.com/highbrow_fame/careers-page-jobs-api) | Give career page or ATS board URLs; get open jobs with title, location, department, remote flag, description and apply URL. Greenhouse, Lever, Ashby, Workable and more. Unofficial Careers Page API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/jobs-ch-jobs,highbrow_fame/jobs-cz-jobs,highbrow_fame/karriere-at-jobs,highbrow_fame/stellenanzeigen-jobs,highbrow_fame/bestjobs-ro-jobs,highbrow_fame/pnet-jobs,highbrow_fame/elempleo-jobs,highbrow_fame/job-bank-canada-jobs,highbrow_fame/mojposao-jobs,highbrow_fame/arbeidsplassen-nav-jobs,highbrow_fame/careers-page-jobs-api`

Registry name: `io.github.projectworks007/job-boards-2`

<a id="real-estate-listings"></a>
## Real Estate Listings Data

Search property listings to buy or rent on national property portals: price, area, rooms, location, agency and listing details. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Fotocasa](https://apify.com/highbrow_fame/fotocasa-properties) | Spanish property listings from fotocasa.es, to buy or rent: price, price drops, m², bedrooms, floor, district, amenities, photos, agency, and optionally the energy certificate. No phones. Unofficial Fotocasa API. |
| [Immowelt](https://apify.com/highbrow_fame/immowelt-properties) | German property listings from immowelt, to rent or for sale: price, cold and warm rent, living area, rooms, floor, city, district, postcode, energy class and seller type. No phones. Unofficial Immowelt API. |
| [Redfin](https://apify.com/highbrow_fame/redfin-properties) | Redfin homes in the US: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, days on market, address, map point, MLS id, broker. No agent names. Unofficial Redfin API. |
| [Immoweb](https://apify.com/highbrow_fame/immoweb-properties) | Immoweb property listings in Belgium, for sale or to rent: price, bedrooms, living area, EPC, town and postcode, agency, and optionally description and building details. Unofficial Immoweb API. |
| [Otodom](https://apify.com/highbrow_fame/otodom-properties) | Otodom property listings in Poland, for sale or to rent: price, price per m², area, rooms, floor, district, seller type, and optionally coordinates and building details. Unofficial Otodom API. |
| [Realtor.com](https://apify.com/highbrow_fame/realtor-properties) | Realtor.com homes in the US: for sale, sold or for rent — price, beds, baths, sq ft, lot, year built, HOA, list and sold dates, address, MLS id, brokerage. No agent names. Unofficial Realtor.com API. US real estate data, sold homes data, home prices API. |
| [Rightmove](https://apify.com/highbrow_fame/rightmove-properties) | Rightmove property listings, UK, for sale or to rent: price, bedrooms, type, tenure, size, address with coordinates, key features, price changes and the agent. No phones. Unofficial Rightmove API. UK real estate, UK house prices, UK property scraper. |
| [ImmoScout24 Austria](https://apify.com/highbrow_fame/immoscout24-at-properties) | ImmoScout24 Austria property API: price, price per m², area, rooms, postcode, agency for $1.50 per 1,000 properties. immobilienscout24.at to buy or rent; energy data. Private owners anonymous. Unofficial ImmoScout24 Austria API. Austrian real estate scraper: Austria apartments, Austria real estate. |
| [Magicbricks](https://apify.com/highbrow_fame/magicbricks-properties) | Indian property listings from Magicbricks, to buy or rent: price in INR, BHK, area, floor, furnishing, locality, society, amenities and who posted it. Any city. Owners stay anonymous. No phones. Unofficial Magicbricks API. |
| [Property Finder](https://apify.com/highbrow_fame/propertyfinder-properties) | Listings from Property Finder in the UAE, Saudi Arabia, Qatar, Bahrain and Egypt: price, size, bedrooms, location, coordinates, amenities, completion, agency. For sale and to rent. No phones. Unofficial Property Finder API. |
| [NoBroker](https://apify.com/highbrow_fame/nobroker-properties) | NoBroker property API: rent or price, deposit, BHK, area, furnishing, floor and locality for $1.50 per 1,000 properties. Owner-posted homes in India to rent, for sale and PG; tenant preference, amenities. No phones, no owner names. Unofficial NoBroker API. |
| [Pisos.com](https://apify.com/highbrow_fame/pisos-properties) | Spanish property listings from pisos.com, for sale or to rent: price, price drops, bedrooms, bathrooms, m², floor, zone, postcode, seller type and agency, and optionally the full details. No phones. Unofficial Pisos.com API. |
| [Gratka & Morizon](https://apify.com/highbrow_fame/gratka-morizon-properties) | Polish property listings from Gratka.pl and Morizon.pl, for sale or to rent: price, price per m², area, rooms, floor, market, city and district, seller type, full description. No phones. Unofficial Gratka and Morizon API. |
| [Sreality](https://apify.com/highbrow_fame/sreality-properties) | Czech property listings from Sreality.cz — sale, rent, auctions: price, area, layout (2+kk), town, district, region, agency, photos, and optionally description, dates and building details. No phones. Unofficial Sreality API. |
| [Imovirtual](https://apify.com/highbrow_fame/imovirtual-properties) | Portuguese property listings from Imovirtual, for sale or to rent: price, price per m², area, typology, floor, council and parish, seller type, and optionally coordinates and energy rating. No phones. Unofficial Imovirtual API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/fotocasa-properties,highbrow_fame/immowelt-properties,highbrow_fame/redfin-properties,highbrow_fame/immoweb-properties,highbrow_fame/otodom-properties,highbrow_fame/realtor-properties,highbrow_fame/rightmove-properties,highbrow_fame/immoscout24-at-properties,highbrow_fame/magicbricks-properties,highbrow_fame/propertyfinder-properties,highbrow_fame/nobroker-properties,highbrow_fame/pisos-properties,highbrow_fame/gratka-morizon-properties,highbrow_fame/sreality-properties,highbrow_fame/imovirtual-properties`

Registry name: `io.github.projectworks007/real-estate-listings`

<a id="real-estate-listings-2"></a>
## Real Estate Listings Data (part 2)

Search property listings to buy or rent on national property portals: price, area, rooms, location, agency and listing details. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Emlakjet](https://apify.com/highbrow_fame/emlakjet-properties) | Turkish property listings from Emlakjet, for sale or to rent: price in TRY, gross/net m², rooms (3+1), building age, floor, heating, district, agency and description. No phones. Unofficial Emlakjet API. |
| [Imot.bg](https://apify.com/highbrow_fame/imot-bg-properties) | Bulgarian property listings from imot.bg, for sale or to rent: price, area, rooms, floor, building type and year, town and district, agency or private, full description. No phones. Unofficial imot.bg API. |
| [Bien'ici](https://apify.com/highbrow_fame/bienici-properties) | French property listings from Bien'ici, for sale or to rent: price, price per m², surface, rooms, bedrooms, floor, town, postcode, energy class (DPE/GES), agency and full description. No phones. Unofficial Bien'ici API. |
| [Oikotie](https://apify.com/highbrow_fame/oikotie-properties) | Finnish homes for sale and rent from Oikotie: debt-free and selling price, rent, charges, area, rooms, floor, year, energy class, postcode, agency, description. No phones. Unofficial Oikotie API. |
| [Etuovi](https://apify.com/highbrow_fame/etuovi-properties) | Finnish properties for sale from Etuovi: debt-free and selling price, area, rooms, floor, year, condition, energy class, maintenance charge, postcode, description. No phones. Unofficial Etuovi API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/emlakjet-properties,highbrow_fame/imot-bg-properties,highbrow_fame/bienici-properties,highbrow_fame/oikotie-properties,highbrow_fame/etuovi-properties`

Registry name: `io.github.projectworks007/real-estate-listings-2`

<a id="vehicle-listings"></a>
## Car & Vehicle Listings Data

Search car and vehicle listings on national car marketplaces: make, model, price, mileage, year, fuel, gearbox, location and seller type. Private sellers stay anonymous; no phone numbers.

| Tool | What it returns |
|---|---|
| [Coches.net](https://apify.com/highbrow_fame/cochesnet-listings) | Used and km 0 cars from coches.net, Spain's big car marketplace: price and coches.net's price rating, year, km, fuel, gearbox, power, body, province and dealer. No phone numbers. Unofficial Coches.net API. |
| [AutoTrader.ca](https://apify.com/highbrow_fame/autotrader-ca-listings) | AutoTrader.ca car listings from any search link or a make, model and place: price, mileage, model year, trim, fuel, gearbox, place and dealer; body, colour and drivetrain on request. No phone numbers. Unofficial AutoTrader.ca API. |
| [Otomoto](https://apify.com/highbrow_fame/otomoto-listings) | Polish vehicle listings from otomoto — cars, motorbikes, vans, trucks: price, make, model, year, mileage, fuel, gearbox, power, body type, town, seller type and dealer. No phones. Unofficial Otomoto API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/cochesnet-listings,highbrow_fame/autotrader-ca-listings,highbrow_fame/otomoto-listings`

Registry name: `io.github.projectworks007/vehicle-listings`

<a id="marketplace-listings"></a>
## Marketplace Listings Data

Search classified ads and second-hand listings on national marketplaces: title, price, condition, location, photos, seller type. No seller usernames or phone numbers.

| Tool | What it returns |
|---|---|
| [Kleinanzeigen](https://apify.com/highbrow_fame/kleinanzeigen-listings) | Kleinanzeigen ads from kleinanzeigen.de, Germany: marketplace, cars, flats, houses, jobs. Price, postcode, town, date, category, seller type. Private sellers anonymous. Unofficial Kleinanzeigen API. |
| [Vinted](https://apify.com/highbrow_fame/vinted-listings) | Vinted listings from 27 country sites by search link or keyword: title, brand, size, condition, price, buyer fee, favourites, photo. Reads past the 960 cap. No usernames. Unofficial Vinted API. |
| [Gumtree](https://apify.com/highbrow_fame/gumtree-uk-listings) | UK listings from gumtree.com: stuff for sale, cars and vans, property to rent and for sale, pets. Price, area, category, car and property details. No phones; private sellers stay anonymous. Unofficial Gumtree API. |
| [Craigslist Marketplace](https://apify.com/highbrow_fame/craigslist-listings) | craigslist listings from any city and section — for sale, housing, cars, jobs, gigs, services: title, price, place, date, category, images, and optionally description and attributes. No phones. Unofficial Craigslist API. Craigslist apartments, craigslist cars. |
| [Blocket](https://apify.com/highbrow_fame/blocket-listings) | Swedish classifieds from Blocket — the marketplace, cars, motorbikes, boats, caravans and machines: price, place, seller type, vehicle data, descriptions on request. No phones. Unofficial Blocket API. |
| [OfferUp](https://apify.com/highbrow_fame/offerup-listings) | OfferUp listings around any US city or ZIP: price, condition, category, town and state, post date, firm price, photos, car make, model and mileage. Links or keywords. No phones, no seller names. Unofficial OfferUp API. OfferUp scraper, classifieds API, secondhand marketplace data. |
| [Kijiji](https://apify.com/highbrow_fame/kijiji-listings) | Kijiji.ca listings from any category — buy & sell, cars, rentals, homes, jobs, pets: price, place, seller type, car and property details, optional full description. No phones. Unofficial Kijiji API. |
| [Subito.it](https://apify.com/highbrow_fame/subito-listings) | Italian listings from Subito.it: flats and houses, cars and motorbikes, marketplace items. Price, town, full ad text, rooms, m², make, km, seller type. Private sellers stay anonymous. No phones. Unofficial Subito API. |
| [FINN.no](https://apify.com/highbrow_fame/finn-listings) | Norwegian listings from FINN.no — Torget, cars, boats, homes for sale and rent, commercial property and jobs: price, place, seller type and company, details on request. No phones. Unofficial FINN.no API. |
| [Marktplaats & 2dehands](https://apify.com/highbrow_fame/marktplaats-2dehands-listings) | Listings from Marktplaats (NL), 2dehands and 2ememain (BE): price, place, condition, category, car data, date. Search links or keywords. Private sellers stay anonymous. Unofficial Marktplaats API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/kleinanzeigen-listings,highbrow_fame/vinted-listings,highbrow_fame/gumtree-uk-listings,highbrow_fame/craigslist-listings,highbrow_fame/blocket-listings,highbrow_fame/offerup-listings,highbrow_fame/kijiji-listings,highbrow_fame/subito-listings,highbrow_fame/finn-listings,highbrow_fame/marktplaats-2dehands-listings`

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
| [Google AI Overview Checker](https://apify.com/highbrow_fame/ai-overview-citation-checker) | AI Overview citation checker: which sites Google AI Overviews cite for your keywords ($0.03 per keyword). Shows if your domain is cited, at what position, and who else is. English Google. |
| [Brand Share of Voice in AI Search](https://apify.com/highbrow_fame/ai-brand-share-of-voice) | AI share of voice: how often ChatGPT, Perplexity and Gemini name your brand vs competitors ($0.08 per prompt). Ranked by mention rate, citation share and position, plus top-cited sources. |
| [AI Citation Checker](https://apify.com/highbrow_fame/ai-page-citation-checker) | Page citation checker: is this URL cited by ChatGPT, Perplexity or Gemini ($0.12 per URL). It writes buyer questions from each page, asks the engines, and shows who is cited instead. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/ai-search-visibility-tracker,highbrow_fame/ai-overview-citation-checker,highbrow_fame/ai-brand-share-of-voice,highbrow_fame/ai-page-citation-checker`

Registry name: `io.github.projectworks007/ai-search-visibility`

<a id="youtube-transcripts"></a>
## YouTube Transcripts

Transcripts from YouTube videos, playlists and channels: timestamps, plain text, SRT or WebVTT. No browser, so it is fast. You pay only for transcripts delivered; videos without captions are free.

| Tool | What it returns |
|---|---|
| [youtube-transcript-fast](https://apify.com/highbrow_fame/youtube-transcript-fast) |  |
| [YouTube Channel API](https://apify.com/highbrow_fame/youtube-channel-api) | YouTube channel info (subscribers, video count, description, avatar, links) plus its videos and shorts with views, dates and durations. No key, no login. Unofficial YouTube Channel API. |
| [YouTube Video Details API](https://apify.com/highbrow_fame/youtube-video-details-api) | Title, channel, views, likes, duration, publish date, description, tags, category, chapters, caption languages and thumbnails for any YouTube video link or id. No API key. Unofficial YouTube API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/youtube-transcript-fast,highbrow_fame/youtube-channel-api,highbrow_fame/youtube-video-details-api`

Registry name: `io.github.projectworks007/youtube-transcripts`

<a id="app-store-data"></a>
## App & Game Store Data

Look up apps, games and browser extensions and their user reviews on the App Store, Google Play, Steam and the Chrome Web Store: ratings, versions, prices, review text and dates.

| Tool | What it returns |
|---|---|
| [Google Play API &](https://apify.com/highbrow_fame/google-play-apps-reviews) | Google Play apps and reviews from links, searches or developers: installs, rating, histogram, price, ads, versions, and reviews with developer replies, no reviewer names. Unofficial Google Play API. Android app reviews scraper, Android apps data, mobile app reviews. |
| [Chrome Web Store](https://apify.com/highbrow_fame/chrome-web-store-extensions) | Chrome Web Store extensions and themes from searches, categories or ids: users, rating, rating count, version, last update, size, languages, permissions, publisher and privacy disclosures. Unofficial Chrome Web Store API. |
| [Steam](https://apify.com/highbrow_fame/steam-games-reviews) | Steam games by id, link or search: price and discount, release date, developers, genres, Metacritic, review totals — plus the written reviews with playtime, no reviewer names. Unofficial Steam API. |
| [App Store API](https://apify.com/highbrow_fame/app-store-api) | App Store app details (price, rating, version, screenshots), keyword search, top charts by country and customer reviews, from Apple's public endpoints. No key. Unofficial App Store API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-play-apps-reviews,highbrow_fame/chrome-web-store-extensions,highbrow_fame/steam-games-reviews,highbrow_fame/app-store-api`

Registry name: `io.github.projectworks007/app-store-data`

<a id="news-and-trends"></a>
## News & Trends Data

Research and monitoring data: Google Trends interest and trending searches, Google News articles, Hacker News stories, Substack posts, RSS feeds and podcast episodes.

| Tool | What it returns |
|---|---|
| [Google Trends API &](https://apify.com/highbrow_fame/google-trends-reliable) | Google Trends data you can rely on: interest over time, interest by region, and top and rising related searches for any keyword, country and period. Pay only for keywords with data. Unofficial Google Trends API. |
| [Substack API &](https://apify.com/highbrow_fame/substack-posts) | Substack posts from any publication: title, date, authors, likes, comments, restacks, word count, paid or free, tags and optionally the full text. Many publications per run. Unofficial Substack API. |
| [Hacker News API &](https://apify.com/highbrow_fame/hacker-news-stories) | Hacker News stories from the front page, new, best, Ask HN, Show HN and jobs, or from a search over all of HN: title, link, points, comments, date, and the comment threads. Unofficial Hacker News API. |
| [Apple Podcasts API &](https://apify.com/highbrow_fame/apple-podcasts-shows-episodes) | Apple Podcasts shows by link, search or top chart (any country and genre) with rating, publisher, genres and feed, plus their episodes with audio links. No login. Unofficial Apple Podcasts API. |
| [Google Trends Trending Now](https://apify.com/highbrow_fame/google-trends-trending-now) | Every search trending on Google Trends right now, for any country: search volume, increase, start and end time, category and related searches — not just the 10 the RSS feed shows. |
| [Google News API](https://apify.com/highbrow_fame/google-news-api) | Google News headlines as JSON by keyword, topic or publication, any country and language, with title, source, publish date and decoded article URL. Unofficial Google News API. |
| [Article Extractor API](https://apify.com/highbrow_fame/article-extractor-api) | Extracts the article from any news or blog URL: title, author, published date, full text, Markdown, lead image and language. Works on paywall-free pages. Unofficial Article Extractor API. |
| [News Search API](https://apify.com/highbrow_fame/news-search-api) | Keyword news search over Google News (thousands of sources) with date range, language, country, dedup, source, publish time and optional full-text extraction. Unofficial News Search API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-trends-reliable,highbrow_fame/substack-posts,highbrow_fame/hacker-news-stories,highbrow_fame/apple-podcasts-shows-episodes,highbrow_fame/google-trends-trending-now,highbrow_fame/google-news-api,highbrow_fame/article-extractor-api,highbrow_fame/news-search-api`

Registry name: `io.github.projectworks007/news-and-trends`

<a id="ecommerce-products"></a>
## E-commerce Product Data

Product data from online stores and supermarkets: names, prices, promotions, stock, categories and product details.

| Tool | What it returns |
|---|---|
| [Coles Australia](https://apify.com/highbrow_fame/coles-au-products) | Coles grocery prices API: price, was-price, unit price, specials and availability by store for $1 per 1,000 products. Coles Australia supermarket products, multi-buy; barcode and nutrition on request. Unofficial Coles API. |
| [Woolworths Australia](https://apify.com/highbrow_fame/woolworths-au-products) | Woolworths grocery prices API: price, was-price, unit price, specials and stock for $0.70 per 1,000 products. Woolworths Australia supermarket products, barcode, ingredients, allergens, nutrition. Unofficial Woolworths API. |
| [ALDI Australia](https://apify.com/highbrow_fame/aldi-au-products) | ALDI Australia grocery prices and Special Buys: product search and category links. Price, unit price, pack size, brand, category, on-sale dates, Super Savers flags. Unofficial ALDI Australia API. |
| [Shopify Store](https://apify.com/highbrow_fame/shopify-store-products-api) | Full product catalogue of any Shopify store from its public products.json: title, vendor, type, tags, variants with price, SKU and stock, images, collections. Unofficial Shopify API. |
| [Product Data Extractor API](https://apify.com/highbrow_fame/product-page-extractor-api) | Name, brand, price, currency, stock, rating, images, SKU/GTIN and variants from a product page's schema.org JSON-LD, microdata or Open Graph tags. One JSON record per URL. Product Data Extractor API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/coles-au-products,highbrow_fame/woolworths-au-products,highbrow_fame/aldi-au-products,highbrow_fame/shopify-store-products-api,highbrow_fame/product-page-extractor-api`

Registry name: `io.github.projectworks007/ecommerce-products`

<a id="events-data"></a>
## Events Data

Find events by place, date and topic: title, dates, venue, price, organiser and event page.

| Tool | What it returns |
|---|---|
| [Eventbrite Events](https://apify.com/highbrow_fame/eventbrite-events) | Eventbrite events by city, keyword, category and date: start and end times, venue with address and coordinates, ticket prices, sales status and organizer. Many cities per run. Unofficial Eventbrite API. |
| [Meetup](https://apify.com/highbrow_fame/meetup-events) | Meetup events by keyword and city, from search links, or from groups (upcoming or past): date, time zone, venue city, group, fee, going count, topics, description. No hosts or attendees. Unofficial Meetup API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/eventbrite-events,highbrow_fame/meetup-events`

Registry name: `io.github.projectworks007/events-data`

<a id="finance-data"></a>
## Finance & Filings Data

Market and company data: quotes, price history and fundamentals from Yahoo Finance, and company filings from SEC EDGAR.

| Tool | What it returns |
|---|---|
| [Yahoo Finance API &](https://apify.com/highbrow_fame/yahoo-finance-quotes) | Yahoo Finance quotes API: price, change, volume, P/E, market cap and dividends for stocks, ETFs and crypto for $1 per 1,000 symbols. Currencies, indexes. Price history and fundamentals on request. Unofficial Yahoo Finance API. Historical stock prices, financial data API and crypto prices API. |
| [SEC EDGAR API & Filings](https://apify.com/highbrow_fame/sec-edgar-filings) | SEC EDGAR filings by ticker, CIK or full-text search: form, dates, accession number, document links, 8-K items, and optional XBRL key financials for 10-K/10-Q. Official SEC APIs. SEC filings API and SEC EDGAR scraper. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/yahoo-finance-quotes,highbrow_fame/sec-edgar-filings`

Registry name: `io.github.projectworks007/finance-data`

<a id="hotel-prices"></a>
## Hotel Prices Data

Get every booking site's price for the hotels and check-in dates you choose, from Google Hotels: per night and per stay, with and without taxes, the official site's rate and free-cancellation dates. It prices the hotels you list; it does not search a city.

| Tool | What it returns |
|---|---|
| [Google Hotels Prices](https://apify.com/highbrow_fame/google-hotels-prices) | Unofficial Google Hotels scraper & Google Travel hotel prices API: type a city or paste hotel links and get every booking site's price for any check-in dates. Per night and total stay, with and without taxes, plus the official site's rate. Pay only for results with prices. Hotel price comparison. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/google-hotels-prices`

Registry name: `io.github.projectworks007/hotel-prices`

<a id="ai-agent-web-tools"></a>
## Web Tools for AI Agents

Give your AI agent the web: fetch any public URL as clean Markdown, crawl a whole site, take screenshots, turn PDF and Office files into text, read text from images and check URLs. Pay per page or document.

| Tool | What it returns |
|---|---|
| [Web Fetch API](https://apify.com/highbrow_fame/web-fetch-api) | Bulk HTTP fetch for agents: returns status, headers and body (raw HTML, text, Markdown or parsed JSON), follows redirects, optional browser rendering. Unofficial Web Fetch API. |
| [Website Screenshot API](https://apify.com/highbrow_fame/website-screenshot-api) | Screenshots of any URL: viewport or full page, mobile/desktop, dark mode, element selector, delay, blocking cookie banners; returns PNG/JPEG/WebP links. Unofficial Screenshot API. |
| [PDF to Markdown API](https://apify.com/highbrow_fame/pdf-to-markdown-api) | Converts PDFs at public links to Markdown and plain text with page markers, headings, links and metadata; scanned pages are flagged, never charged. Unofficial PDF to Markdown API. |
| [Markdown Crawler API](https://apify.com/highbrow_fame/markdown-site-crawler) | Crawls a site (links or sitemap, depth and page limits, robots.txt respected) into one Markdown document per page with title, URL, headings and links, for RAG. Unofficial Website to Markdown API. |
| [URL to Markdown API](https://apify.com/highbrow_fame/url-to-markdown-api) | Fetches any URL and returns clean Markdown (readability-extracted main content), title, metadata and links; optional headless browser for JS pages. Unofficial URL to Markdown API. |
| [URL Status Checker API](https://apify.com/highbrow_fame/url-status-checker-api) | Check thousands of URLs at once: HTTP status, redirect chain, final URL, response time, content type, SSL expiry and a dead-link flag. Unofficial URL Status Checker API. |
| [OCR API](https://apify.com/highbrow_fame/ocr-api) | OCR API: text, confidence, paragraphs and word boxes from images and scanned PDFs for $2 per 1,000 images. Tesseract OCR by URL, optional hOCR/TSV, many languages. Unofficial OCR API. |
| [DOCX, PPTX, XLSX & EPUB to Text API](https://apify.com/highbrow_fame/office-document-to-text-api) | Convert Word, PowerPoint, Excel, OpenDocument and EPUB files at public links to Markdown and text, with metadata, sheets as JSON rows and slides with notes. Office Document to Text API. |
| [SEO Audit API](https://apify.com/highbrow_fame/seo-audit-api) | On-page SEO audit of any URL over plain HTTP: title, meta, canonical, robots, hreflang, headings, images alt, links, JSON-LD, redirects, a 0-100 score with issues. SEO Audit API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/web-fetch-api,highbrow_fame/website-screenshot-api,highbrow_fame/pdf-to-markdown-api,highbrow_fame/markdown-site-crawler,highbrow_fame/url-to-markdown-api,highbrow_fame/url-status-checker-api,highbrow_fame/ocr-api,highbrow_fame/office-document-to-text-api,highbrow_fame/seo-audit-api`

Registry name: `io.github.projectworks007/ai-agent-web-tools`

<a id="company-data"></a>
## Company Data

Look up companies for research, sales and AI agents: enrich a company domain (name, description, social links, tech hints), UK Companies House records and Y Combinator startups. No personal data.

| Tool | What it returns |
|---|---|
| [Company Enrichment API](https://apify.com/highbrow_fame/company-enrichment-api) | Company name, legal name, logo, founding year, HQ, socials, generic mailboxes, phone and tech hints from a domain's own site and schema.org markup. No people data. Unofficial Company Enrichment API. |
| [Companies House API](https://apify.com/highbrow_fame/companies-house-api) | Search UK companies and read the public register: number, status, type, SIC codes, dates, registered office, accounts dates, latest filings, officer and charge counts. Unofficial Companies House API. |
| [Y Combinator Companies API](https://apify.com/highbrow_fame/y-combinator-companies-api) | All YC companies with batch, status, industry, team size, location, website, one-liner and tags from the public YC Startup Directory; search by keyword, batch or industry. Unofficial Y Combinator API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/company-enrichment-api,highbrow_fame/companies-house-api,highbrow_fame/y-combinator-companies-api`

Registry name: `io.github.projectworks007/company-data`

<a id="web-and-dev-tools"></a>
## Web & Developer Data Tools

Utility tools for agents: detect a website's tech stack, check domains (WHOIS, DNS, SSL), list sitemap URLs, extract text from PDFs, read RSS feeds, and find trending GitHub repos, Hugging Face models and OpenStreetMap places.

| Tool | What it returns |
|---|---|
| [PDF Text Extractor &](https://apify.com/highbrow_fame/pdf-text-extractor) | The text of any PDF at a public link — whole or page by page — with page count, word count and metadata. Scanned PDFs without text are flagged and not charged. PDF to text API and PDF text extraction API. |
| [Domain Checker](https://apify.com/highbrow_fame/domain-whois-dns-ssl) | Check many domains at once: registrar, creation and expiry dates, status, name servers, DNS records with SPF and DMARC, SSL certificate expiry, and where the website redirects. Domain WHOIS API, DNS lookup API and SSL checker API. |
| [Website Tech Stack Detector API](https://apify.com/highbrow_fame/website-tech-stack) | The technologies behind any website: CMS, e-commerce platform, frameworks, analytics and ad tags, CDN, hosting, payment and more, with versions where visible. Many sites per run. Website tech stack detector API. |
| [Sitemap Extractor &](https://apify.com/highbrow_fame/sitemap-url-extractor) | Every URL in a website's sitemaps — found through robots.txt, nested indexes and .gz files followed — with last-modified date, change frequency, priority, images, hreflang and news tags. Sitemap API and sitemap URL extractor API. |
| [Domain Authority & Website Rank Checker API](https://apify.com/highbrow_fame/domain-authority-rank) | Bulk domain authority checker on open data: a 0-100 link strength score, website rank, referring subnets and IPs for up to 10,000 domains per run, from the Common Crawl web graph and Majestic Million. |
| [RSS Feed API & Atom Feed Reader](https://apify.com/highbrow_fame/rss-feed-reader) | Read any RSS, Atom, RDF or JSON feed — or just give a website and its feed is found — into one list: title, link, date, author, categories, summary, content and image. RSS feed API and RSS to JSON API. |
| [OpenStreetMap API & Places](https://apify.com/highbrow_fame/openstreetmap-places) | Points of interest from OpenStreetMap by place or map box: restaurants, shops, hotels, pharmacies, 62 categories or any OSM tag, with address, coordinates, opening hours and website. OpenStreetMap places API and POI data API. |
| [GitHub Trending](https://apify.com/highbrow_fame/github-trending-repos) | GitHub Trending repositories by programming language, date range and spoken language: rank, stars gained today/this week/this month, total stars, forks, and optionally topics, license and dates. Unofficial GitHub Trending API. |
| [Weather API](https://apify.com/highbrow_fame/weather-api) | Current conditions, hourly and 16-day forecast, air quality and historical weather back to 1940 for any city or coordinates. No key, one record per location. Unofficial Open-Meteo API. |
| [GitHub Repo API](https://apify.com/highbrow_fame/github-repo-api) | Repo details, stars, forks, topics, license, languages, latest releases, README, contributor count and recent commits from GitHub's public API, by name, link or search. Unofficial GitHub API. |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/pdf-text-extractor,highbrow_fame/domain-whois-dns-ssl,highbrow_fame/website-tech-stack,highbrow_fame/sitemap-url-extractor,highbrow_fame/domain-authority-rank,highbrow_fame/rss-feed-reader,highbrow_fame/openstreetmap-places,highbrow_fame/github-trending-repos,highbrow_fame/weather-api,highbrow_fame/github-repo-api`

Registry name: `io.github.projectworks007/web-and-dev-tools`

<a id="shopify-store-audits"></a>
## Shopify Store Audits

Check any list of Shopify stores from public data: product feed completeness, AI crawler access, EU customs identifier coverage (SKUs, GTIN) and the ScriptTags Shopify stops running on 1 March 2027.

| Tool | What it returns |
|---|---|
| [Shopify ScriptTag Checker](https://apify.com/highbrow_fame/shopify-script-tag-checker) | Will your Shopify store break on 1 March 2027? Lists the ScriptTags Shopify stops injecting, the app vendors behind them and legacy customer accounts ($0.01 per store) |
| [Shopify AI Readiness Audit](https://apify.com/highbrow_fame/shopify-ai-readiness-audit) | Shopify AI readiness audit: bulk products.json audit and AI crawler access check for any list of Shopify stores ($0.01 per store, 500 stores = $5) |

Server URL: `https://mcp.apify.com/?tools=highbrow_fame/shopify-script-tag-checker,highbrow_fame/shopify-ai-readiness-audit`

Registry name: `io.github.projectworks007/shopify-store-audits`

## Notes

- The tools read public pages only. Listing tools leave out private persons' phone numbers and e-mail addresses.
- Found a problem or missing a field? Open an issue on the Actor's Apify page.
