# OfferUp Scraper — Local Listings, Prices & Details, No Phones

OfferUp Scraper gets listings from OfferUp, the US local marketplace: title, price, condition, category, town and state, when it was posted, whether the price is firm, the photo and the full description, and for cars the make, model, year, trim and mileage. Paste your OfferUp search links or type keywords and a US city or ZIP code. No phone numbers and no seller names are delivered, and you pay only for listings delivered.

## What data does OfferUp Scraper extract?

For every listing:

- `listingId`, `url`, `title`
- `price`, `originalPrice`, `currency`, `isFirmPrice`, `callForPrice` – asking price in USD and the price before a cut
- `condition` – New, Open box, Reconditioned, Used, For parts, Other
- `category`, `categoryPath`
- `description` – the seller's text, with phones, e-mails and private street addresses removed
- `location`, `city`, `state` – town and state only, never a street or map point
- `postedAt`, `editedAt`
- `localPickup`, `shippingAvailable`, `shippingPrice`
- `sellerType`, `sellerName` – private or dealer; a name for car dealers only
- `isPromoted`
- `image`, `imageCount`
- `mileage`, `make`, `model`, `year`, `trim`, `titleStatus`, `color`, `fuel`, `body`, `transmission` – for cars and motorcycles
- `input`, `searchLocation`, `position`, `scrapedAt`, `status`, `error`

Listing details come in one extra request per 50 listings at no extra charge; untick **Include listing details** for a faster run with the search data only.

## How to use OfferUp Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example (a mountain-bike search around Seattle), so one click starts a run.
2. Paste **Search links** from offerup.com, one per line, or type **Keywords** and **Locations** (a ZIP code or "City, ST") and choose distance, category, price, condition and sort.
3. A link without a city or ZIP is searched around each place under **Locations**.
4. Set **Max listings per search**, press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "2008 Jeep Wrangler",
  "price": 9995,
  "condition": "Used",
  "city": "Lake Worth",
  "state": "TX",
  "sellerType": "dealer",
  "mileage": 174633
}
```

## How much does it cost?

**$0.0015 per listing delivered, $1.50 per 1,000 listings.** Listing details cost nothing extra, only time. Links that are not OfferUp searches and unknown places are free records.

Worked example: a live run read three searches with all details (cars at $5,000–15,000 around Dallas, sofas up to $300 near Chicago, iPhone 15s around Phoenix) and delivered 939 listings in 25 seconds, for **$1.41**. 2,000 bikes around Los Angeles without details took 60 seconds and cost $3.00.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item it has delivered for this exact search, in a key-value store in your own account. The first run returns everything; later runs with the same inputs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link; it works with Slack and Discord incoming webhooks and any HTTPS endpoint. Schedule it daily for a new-listings alert.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/offerup-listings` to Claude, ChatGPT or any MCP client and the assistant can search OfferUp with this Actor's own input fields. You pay per listing delivered, at the same rate.

## Is it legal to scrape OfferUp?

The Actor reads public OfferUp listings only. Almost every OfferUp seller is a private person, so seller names, profiles, ratings and map points are not delivered, and phone numbers, e-mail addresses and private sellers' street addresses in titles and descriptions are replaced with `[phone removed]`, `[e-mail removed]` and `[address removed]`. Car dealers keep their business name. This keeps the output to listing data rather than personal data under GDPR and similar laws; every record carries its `url`, and buyers contact the seller on OfferUp. You remain responsible for how you use the data and for OfferUp's terms. This is an independent tool, not affiliated with OfferUp.

## FAQ

**How many listings per search?** As many as OfferUp lets a search reach. A live run asked for every bike around Los Angeles and got 8,739 different listings in under 4 minutes without details.

**Where does a search end?** Where OfferUp's own search area ends: iPhone 15s within 20 miles of Phoenix gave 139 listings, all in Arizona.

**Are the filters obeyed?** Yes. In the live test all 939 listings were inside their price range; 15 were promoted and matched too.

**Why no phone numbers or seller names?** They are personal data. In the test run, phone numbers, e-mails and street addresses were removed from 106, 9 and 22 of 939 listings.

**Last updated:** 2026-10-15.

## Related Actors

- [Craigslist Marketplace Scraper](https://apify.com/highbrow_fame/craigslist-listings) – for sale, housing, cars and jobs across US cities
- [Kijiji Scraper](https://apify.com/highbrow_fame/kijiji-listings) – Canadian classifieds, cars and rentals
- [Vinted Scraper](https://apify.com/highbrow_fame/vinted-listings) – second-hand fashion listings from 27 countries

Useful? A short Store review helps — your feedback decides what we improve next.
