# NoBroker Scraper + New Listings Feed & Alerts, No Phones

NoBroker Scraper gets owner-posted homes from NoBroker, India's no-brokerage property portal: flats and houses to rent, for sale, and PG / hostel rooms. Rent or price, deposit, maintenance, BHK, area, furnishing, tenant preference, floor, building age, amenities, locality, city, dates, photos, and for PGs the rooms by sharing with their rent, meals and house rules. Paste your NoBroker search links, or just type a place. No phones, no owner names and no addresses are delivered, and you pay only for properties delivered.

## What data does NoBroker Scraper extract?

For every property:

- `section`, `title`, `homeType`, `bhk` – rent, buy or pg; "1 RK" … "4+ BHK"
- `rent`, `deposit`, `maintenance`, `maintenanceIncluded`, `negotiable` – to rent, in INR
- `price`, `pricePerSqft`, `ownershipType`, `underLoan` – for sale: price in INR, freehold or leasehold
- `areaSqft`, `carpetAreaSqft`, `plotAreaSqft`
- `furnishing`, `preferredTenants` – full, semi or unfurnished; family, bachelors, anyone
- `floor`, `totalFloors`, `propertyAgeYears`, `bathrooms`, `balconies`, `facing`, `parking`, `waterSupply`, `powerBackup`, `flooring` – floor 0 = ground floor
- `amenities` – lift, gym, swimming pool …
- `locality`, `city`
- `availableFrom`, `postedAt`, `lastUpdatedAt`
- `description` – the owner's text, contacts removed
- `photoCount`, `image`, `hasVideo`, `transitScore`, `lifestyleScore` – NoBroker's 0-10 scores
- `url`, `listingId`, `propertyCode`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

For a PG also: `pgFor`, `rent` and `deposit` of the cheapest room, `rooms` (each sharing with its rent, deposit and amenities), `foodIncluded`, `meals`, `houseRules` and `gateClosingTime`.

## How to use NoBroker Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from nobroker.in, one per line, or type **Places** ("Koramangala, Bangalore") and choose rent, buy or PG, BHK, price, furnishing, tenant type and sort order.
3. Set **Max listings per search**.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new listings, turn on feed mode below and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "1 BHK Flat for Rent in Andheri Kurla Road",
  "section": "rent",
  "bhk": "1 BHK",
  "rent": 31000,
  "deposit": 70000,
  "areaSqft": 630,
  "furnishing": "semi",
  "city": "Mumbai"
}
```

## How much does it cost?

**$0.0015 per property delivered, $1.50 per 1,000 listings.** Links that are not NoBroker searches, unknown places and commercial links are free records.

Worked example: a live run read four searches (1-2 BHK rentals in Mumbai, girls' PGs in Bangalore, flats for sale in Whitefield, furnished rentals in Hinjewadi), 4,008 listings in 100 seconds, for **$6.01**.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item it has delivered for this exact search, in a key-value store in your own account. The first run returns everything; later runs with the same inputs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link; it works with Slack and Discord incoming webhooks and any HTTPS endpoint.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/nobroker-properties` to Claude, ChatGPT or any MCP client and the assistant can search NoBroker homes with this Actor's own input fields. You pay per property delivered, at the same rate.

## Is it legal to scrape NoBroker?

The Actor reads public NoBroker listings only. NoBroker's listings come from owners, private persons, so you get the locality and city, never the owner's name, street, society or building name, flat number or map point. Phone numbers, e-mail addresses, names and addresses that owners write into their descriptions are replaced with `[phone removed]`, `[e-mail removed]`, `[name removed]`, `[address removed]` or `[building name removed]`. That keeps the output to property data rather than personal data under GDPR; every record carries its `url`, and tenants and buyers contact the owner on NoBroker. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with NoBroker.

## FAQ

**Which cities?** The ones NoBroker covers: Bangalore, Mumbai (with Thane and Navi Mumbai), Pune, Chennai, Hyderabad, Gurgaon, Delhi, Noida, Ghaziabad, Faridabad and Greater Noida. Type "locality, city", or a city alone.

**How many properties per search?** As many as NoBroker shows; every page is read: all 856 flats for sale in Whitefield and all 152 matching rentals in Hinjewadi came through.

**Why are a few results from another city?** A city-wide search covers the area around the city: 1,180 of 1,200 Gurgaon flats for sale were in Gurgaon and 17 in Delhi; `city` says where each one is.

**Commercial properties?** Not supported: a commercial link comes back as a free record that says so.

**Last updated:** 2026-10-15.

## Related Actors

- [Magicbricks Scraper](https://apify.com/highbrow_fame/magicbricks-properties) – Indian property for sale and rent, any city
- [Property Finder Scraper](https://apify.com/highbrow_fame/propertyfinder-properties) – UAE and Gulf property listings
- [Rightmove Scraper](https://apify.com/highbrow_fame/rightmove-properties) – UK property for sale and to rent

Useful? A short Store review helps — your feedback decides what we improve next.
