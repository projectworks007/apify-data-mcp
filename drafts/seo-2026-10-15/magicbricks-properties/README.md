# Magicbricks Scraper — India Property for Sale & Rent, No Phones

Magicbricks Scraper gets property listings from Magicbricks, one of India's largest property portals: price in rupees (lakh and crore as plain numbers), BHK, bathrooms, super and carpet area, price per sq ft, floor, furnishing, possession, deposit and maintenance for rentals, amenities, locality, society, developer, RERA number, and whether an owner, an agent or a builder posted it. Flats, houses, plots, offices and shops, to buy or rent, in any city. Paste your Magicbricks search links, or just type a city or locality. Owners stay anonymous, no phone numbers are delivered, and you pay only for properties delivered.

## What data does Magicbricks Scraper extract?

For every property:

- `price`, `priceDisplay`, `currency`, `pricePerSqft` – price or monthly rent in INR as a number ("1.2 Cr" → 12000000), as shown, and per sq ft
- `securityDeposit`, `bookingAmount`, `maintenance`, `maintenanceFrequency`
- `transaction`, `listingType`, `propertyType`, `title` – sale or rent; Resale / New Property / Rent; Apartment, Villa, Plot, Office …
- `bedrooms`, `bathrooms`, `balconies`
- `areaSqft`, `superArea`, `carpetArea`, `plotArea` (+ units), `plotDimensions` – `areaSqft` is the super area, or the carpet area when that is all there is
- `floor`, `totalFloors`, `furnishing`, `facing`, `overlooking`, `flooring`, `parking` – floor 0 = ground floor
- `ageOfProperty`, `possession`, `availableFrom`, `ownership`, `tenantsPreferred`
- `amenities` – Lift, Swimming Pool, Gymnasium …
- `city`, `locality`, `society`, `developer`, `reraId`, `address`, `landmark`, `latitude`, `longitude` – society, address, landmark and map point not for owners
- `sellerType`, `seller` – owner / agent / builder, and the company name (none for owners)
- `description`, `highlights` – the ad text, contact details removed
- `postedAt`, `expiresAt`, `image`, `imageCount`, `url`, `listingId`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

## How to use Magicbricks Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from magicbricks.com, one per line, or type **Cities or localities** (Pune, Whitefield) and choose buy or rent, property type, BHK, price and "posted by".
3. Set **Max listings per search**, and keep the residential proxy from India the input comes set to.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new listings, set **Sort** to "Newest first", save the input as a task and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "3BHK Villa for New Property in Radiance Edgewood at Siruseri",
  "transaction": "sale",
  "propertyType": "Villa",
  "price": 23900000,
  "bedrooms": 3,
  "areaSqft": 2181,
  "city": "Chennai",
  "sellerType": "agent"
}
```

## How much does it cost?

**$0.0012 per property delivered, $1.20 per 1,000 listings.** Links that are not Magicbricks searches and unknown places are free records; a listing outside your budget is left out and not charged.

Worked example: a live run read five searches (Mumbai flats for sale by owners, Bangalore 2-3 BHK rentals at ₹10,000-30,000, Gurgaon offices to rent, 2 BHK agent rentals in Gurgaon and Whitefield), 7,550 properties in about 10 minutes, for **$9.06**. 2,998 Hyderabad homes and plots for sale in 8 minutes cost $3.60.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/magicbricks-properties` to Claude, ChatGPT or any MCP client and the assistant can search Indian property with this Actor's own input fields. You pay per property delivered, at the same rate.

## Is it legal to scrape Magicbricks?

The Actor reads public Magicbricks listings only. A property posted by its owner comes without the owner's name, society, street address, landmark or map point, only locality and city. Agents and builders are named by their registered company, never by the person. Phone numbers and e-mail addresses written into titles and descriptions, even ones spelled out in words, are replaced with `[phone removed]` and `[e-mail removed]`. That keeps the output to property data rather than personal data under GDPR and similar laws; every record carries its `url`, and buyers and tenants contact the advertiser on Magicbricks. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with Magicbricks.

## FAQ

**How many properties per search?** Up to about 3,000: Magicbricks itself shows no more than 100 pages of 30 for one search. For more, split the search by locality, BHK or budget.

**Which links work?** Search result pages (`…-pppfs` for sale, `…-pppfr` to rent, `…/property-for-sale/residential-real-estate?…`). Single property, new-project and PG pages come back as `INVALID_INPUT`.

**Why is "Newest first" sometimes followed by older listings?** After a few hundred listings sorted newest first, Magicbricks repeats one page, on its own website too; the rest then comes in its default order, so you still get every listing once.

**Why a residential proxy from India?** Magicbricks' firewall turns away Apify's servers, datacenter proxies and about one in six residential addresses from other countries; Indian residential addresses got through every time in our tests.

**Last updated:** 2026-10-15.

## Related Actors

- [NoBroker Scraper](https://apify.com/highbrow_fame/nobroker-properties) – owner-posted Indian homes to rent, for sale and PG
- [Property Finder Scraper](https://apify.com/highbrow_fame/propertyfinder-properties) – UAE and Gulf property listings
- [Rightmove Scraper](https://apify.com/highbrow_fame/rightmove-properties) – UK property for sale and to rent

Useful? A short Store review helps — your feedback decides what we improve next.
