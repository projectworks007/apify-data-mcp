# ImmoScout24 Austria Scraper — Property Listings, Rent & Sale

ImmoScout24 Austria Scraper gets property listings from immobilienscout24.at: price, price per m², price cuts, living area, rooms, postcode, town and state, the agency, features and when it was listed, and on request the full description, year built, condition, heating, energy certificate (HWB, fGEE), all the areas, running and one-off costs, commission and every photo. Flats, houses, plots and commercial property, to buy or to rent. Paste your ImmoScout24 search links, or just type a place. No phone numbers, and private owners stay anonymous.

## What data does ImmoScout24 Austria Scraper extract?

For every property:

- `price`, `priceText`, `currency`, `pricePerSqm` – the asking price in EUR (for rent: per month) and per m²
- `oldPrice`, `priceCutPercent` – the price before a cut, and the cut in %
- `transaction`, `propertyType`, `useType`, `title` – buy or rent; APARTMENT, HOUSE, PROPERTY (plot); RESIDENTIAL or COMMERCIAL
- `areaSqm`, `rooms`
- `postcode`, `town`, `state`
- `street`, `address`, `latitude`, `longitude`, `locationRadiusM` – agency listings only
- `sellerType`, `agency`, `agencyId` – private or business, and the company name (none for private owners)
- `features`, `transit` – GARDEN, BALCONY, TERRACE, FREE_OF_COMMISSION …; public transport nearby
- `isProject`, `projectAreaRange`, `projectRoomsRange` – new-build projects, only with **Also list new-build projects**
- `listingType`, `listedAt`, `image`, `url`, `listingId`
- `input`, `place`, `position`, `scrapedAt`, `status`, `error`

With **Open every listing for its details** also: `description`, `floor`, `yearBuilt`, `condition`, `heating`, `energySource`, `heatingDemand`, `heatingDemandClass`, `energyEfficiencyClass`, `livingAreaSqm`, `usableAreaSqm`, `plotAreaSqm`, `gardenAreaSqm`, `cellarAreaSqm`, `availableFrom`, `hasCommission`, `oneTimeCosts`, `monthlyCosts`, `parkingSpaces`, `images`, `nearbyTransit` and more.

## How to use ImmoScout24 Austria Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example (Vienna flats to rent), so one click starts a run.
2. Paste **Search links** from immobilienscout24.at with every filter set, one per line, or type **Places** (Graz, Döbling, 1100, Tirol) and choose buy or rent, property type, price, area, rooms, private or agency, a keyword and the order.
3. Set **Max listings per search**, and tick **Open every listing for its details** if you need the description, energy data and costs.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new listings in an area, choose **Newest first**, save the input as a task and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "title": "Magnus | mit Pool",
  "transaction": "buy",
  "propertyType": "HOUSE",
  "price": 480000,
  "areaSqm": 189,
  "rooms": 7.5,
  "town": "Traun",
  "heatingDemandClass": "E"
}
```

## How much does it cost?

**$0.0015 per property delivered on the Apify Free plan, $1.50 per 1,000 listings**; paid plans are lower, down to $1.05 per 1,000 on Gold and above. Opening listings for their details costs nothing extra, only time. A link that is not an immobilienscout24.at search, or a place ImmoScout24 does not know, comes back as a free record.

Worked example: a live run read 2,000 Vienna flats for sale up to €300,000 in 65 seconds, for **$3.00** on the Free plan. 693 Upper Austria houses with full details (58 seconds) cost $1.04.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/immoscout24-at-properties` to Claude, ChatGPT or any MCP client and the assistant can search Austrian property with this Actor's own input fields. You pay per property delivered, at the same rate.

## Is it legal to scrape ImmoScout24 Austria?

The Actor reads public listings only. Agencies and developers are named by their company; private owners get no name, no street and no map position, only postcode and town. Phone numbers, e-mail addresses and the names of contact persons written into titles and descriptions are replaced with `[phone removed]`, `[e-mail removed]` and `[name removed]`. That keeps the output to property data rather than personal data under GDPR; every record carries its `url`, and buyers and tenants contact the agency or owner on ImmoScout24. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with ImmoScout24.

## FAQ

**How many properties per search?** As many as ImmoScout24 counts. The site's own result pages stop at page 100 (1,500 listings); this reads further. A live run delivered 2,000 of the 5,469 Vienna flats for sale up to €300,000, then stopped at the limit it was given.

**Why a few fewer than the site's count?** New-build projects are listed once as a whole besides their units; the project record comes only with **Also list new-build projects**. Listings with "Preis auf Anfrage" or a symbolic €1 price are left out of price-range searches: 10 of 703 in the Upper Austria run.

**Which places can I type?** Whatever ImmoScout24's place search knows: cities, Vienna districts, postcodes and states. "Salzburg" is read as the state; for the city type 5020.

**Does it work for immobilienscout24.de?** No, Austria only. A .de link comes back as a free record saying so.

**Last updated:** 2026-10-15.

## Related Actors

- [Immowelt Scraper](https://apify.com/highbrow_fame/immowelt-properties) – German property listings and prices
- [Sreality Scraper](https://apify.com/highbrow_fame/sreality-properties) – Czech property listings
- [Immoweb Scraper](https://apify.com/highbrow_fame/immoweb-properties) – Belgian property listings

Useful? A short Store review helps — your feedback decides what we improve next.
