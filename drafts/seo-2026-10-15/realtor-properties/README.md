# Realtor.com Scraper + New Listings Feed & Alerts, No Phones

Realtor.com Scraper gets US property listings from Realtor.com: homes for sale, sold homes and rentals, with price or rent, beds, baths, square feet, lot size, year built, HOA fee, list and sold dates, price cuts, full address and map point, MLS number, listing office and brokerage. Paste your Realtor.com search links, or just type a city, ZIP code, county, neighborhood or state. No agent names or phone numbers, no start fee, and you pay only for homes delivered.

## What data does Realtor.com Scraper extract?

For every home:

- `searchType`, `listingStatus` – `for-sale`, `sold` or `for-rent`, and status
- `price`, `priceMax`, `pricePerSqft`, `hoaPerMonth` – asking price, sale price or rent per month
- `listPrice`, `soldDate` – for sold homes: the last list price and the sale date
- `lastSoldPrice`, `lastSoldDate`, `priceReducedBy` – the previous sale and the last price cut
- `beds`, `bedsMax`, `baths`, `bathsMax`, `fullBaths`, `halfBaths`, `sqft`, `sqftMax`, `lotSqft`, `yearBuilt`, `stories`, `garage`
- `propertyType`, `propertySubType` – single_family, condos, townhomes, multi_family, land…
- `address`, `unit`, `city`, `state`, `zip`, `county`, `neighborhood`, `fullAddress`, `latitude`, `longitude`
- `isNewConstruction`, `isForeclosure`, `isPending`, `isContingent`, `isNewListing`, `isPriceReduced` and other flags
- `listedBy`, `mlsId`, `mlsSource`, `listingOffice`, `listingBroker`, `builder` – who sells it, companies only
- `buildingName`, `propertyManager`, `unitsAvailable`, `catsAllowed`, `dogsAllowed` – rentals
- `features`, `description`
- `url`, `propertyId`, `listingId`, `image`, `photoCount`, `has3DTour`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

## How to use Realtor.com Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from realtor.com, one per line, or type **Places** and choose **For sale, sold or for rent** and filters.
3. Set **Max results per search**.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel.

## Example output

Values are examples, shortened from a live run:

```json
{
  "searchType": "sold",
  "price": 1653000,
  "soldDate": "2026-09-24",
  "beds": 3,
  "sqft": 2050,
  "city": "Seattle",
  "listingOffice": "The Saki Group LLC"
}
```

## How much does it cost?

**$0.0012 per home delivered on the Apify Free plan, $1.20 per 1,000 homes**; paid plans are lower, down to $0.84 per 1,000 on Gold and above. No start fee; links that are not Realtor.com searches and unknown places are free records.

Worked example: a live run read four searches (Los Angeles for sale, Seattle sold, Chicago rentals, Austin houses), 8,000 homes in 164 seconds, for **$9.60** on the Free plan; one search's 10,000-home maximum costs $12.00.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item delivered for this exact search in a key-value store in your account. The first run returns everything; later runs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link to Slack, Discord or any HTTPS endpoint; schedule it daily for a new-listings alert.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/realtor-properties` to Claude, ChatGPT or any MCP client and the assistant can search US homes with this Actor's input fields, paying per home delivered at the same rate.

## Is it legal to scrape Realtor.com?

The Actor reads public Realtor.com listings only. Brokerages, builders and property managers are named by their company; agent names and phone numbers are not delivered, and phones, e-mails and names after "call", "text" or "contact" in a description are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]`. Landlord-listed rentals keep their town and ZIP code, not their street or map point. That keeps the output to listing data rather than personal data under GDPR; every home has its `url`, and buyers contact the agent on Realtor.com. You remain responsible for your use of the data and the site's terms. This is an independent tool, not affiliated with Realtor.com.

## FAQ

**How many homes per search?** Up to 10,000, the most Realtor.com shows for one search; a live run read 10,000 of the 12,226 homes for sale in Los Angeles in 302 seconds. For more, split a search by price or place.

**Which filters of my link are used?** The link is read the way realtor.com reads it (price, beds, baths, size, home type, HOA, days on site, new construction, price reduced, features, sort, sold within, pets). A live run checked them: 293 King County condos with HOA up to $500 and 600 Austin rentals at $1,200–2,000 that allow cats, every one inside the filters.

**Why no sale price for sold homes in Texas?** Texas and a few other states do not publish sale prices: `listPrice` has the last list price (all 600 Texas sales in a live run).

**In which order?** Newest first (sold homes: most recently sold) unless your link asks for another order.

**Last updated:** 2026-10-15.

## Related Actors

- [Redfin Scraper](https://apify.com/highbrow_fame/redfin-properties) – US homes from Redfin, same feed mode
- [Rightmove Scraper](https://apify.com/highbrow_fame/rightmove-properties) – UK property for sale and to rent
- [Funda Scraper](https://apify.com/highbrow_fame/funda-properties) – Dutch homes for sale, rent and sold

Useful? A short Store review helps — your feedback decides what we improve next.
