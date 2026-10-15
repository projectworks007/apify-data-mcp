# Rightmove Scraper + New Listings Feed & Alerts, No Phones

Rightmove Scraper gets property listings from Rightmove, the UK's largest property portal: price and price qualifier, bedrooms, bathrooms, property type, tenure, size, address with coordinates, key features, when it was added or reduced, and the agent. For sale and to rent. Paste your Rightmove search links, or just type a town, a city or a postcode district. No phone numbers are delivered, and you pay only for properties delivered.

## What data does Rightmove Scraper extract?

For every property:

- `displayPrice`, `price`, `priceQualifier`, `priceFrequency`, `currency` – the asking price as shown (£233,000, "Offers in Excess of"), as a number, and per month / week for rentals
- `bedrooms`, `bathrooms`, `propertyType`, `description` – the property (Flat, Terraced, Detached …)
- `tenure`, `size` – freehold / leasehold, and floor area when the agent gives it
- `address`, `latitude`, `longitude` – where it is
- `summary`, `keyFeatures` – the agent's text
- `addedOrReduced`, `listingUpdate`, `listingUpdateDate`, `firstListed` – new or reduced, and when
- `letAvailableDate`, `displayStatus` – for rentals: available from; "Sold STC" / "Let agreed" when included
- `isNewHome`, `isAuction`, `isStudent`, `isFeatured` – listing flags
- `agent`, `agentBranch` – the agency and branch (no phone numbers)
- `image`, `imageCount`, `floorplanCount`, `virtualTourCount`, `url`, `propertyId`
- `input`, `place`, `position`, `channel`, `scrapedAt`, `status`, `error`

## How to use Rightmove Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from rightmove.co.uk (for sale or to rent), one per line, or type **Places** (Manchester, Bristol, SW1A), choose **For sale or to rent** and set price, bedrooms, property type, radius and "added within".
3. Set **Max listings per search**, and tick **Include sold STC / let agreed** if you want those too.
4. Press **Start**, and download the results from the **Output** tab as JSON, CSV or Excel. To follow new listings and price cuts in an area, save the input as a task with **Added within (days)** set to 1 and schedule it daily, or turn on feed mode below.

## Example output

Values are examples, shortened from a live run:

```json
{
  "price": 233000,
  "displayPrice": "£233,000",
  "bedrooms": 2,
  "propertyType": "Apartment",
  "tenure": "LEASEHOLD",
  "address": "Hulme Hall Road, Manchester, Greater Manchester, M15",
  "addedOrReduced": "Added on 02/04/2026",
  "agent": "TK Property Group Ltd"
}
```

## How much does it cost?

**$0.0008 per property delivered, $0.80 per 1,000 listings.** Links that are not Rightmove searches and places Rightmove does not know are free records.

Worked example: a live run read three searches (London for sale, Bristol and Edinburgh to rent), 1,963 properties in 62 seconds, for **$1.57**.

## Only new listings + alerts (feed mode)

Tick **Only new listings (feed mode)** and the Actor remembers every item it has delivered for this exact search, in a key-value store in your own account; each distinct search has its own memory, and changing a filter starts a fresh one. The first run returns everything; later runs with the same inputs return only items not seen before, each with a `firstSeenAt` timestamp, and seen items are neither saved nor charged. An item is remembered for 60 days (up to 50,000 per search). Set **Alert webhook URL** and the Actor sends one POST with the new count, sample items and the dataset link; it works with Slack and Discord incoming webhooks and any HTTPS endpoint. Schedule it daily for a new-listings alert.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/rightmove-properties` to Claude, ChatGPT or any MCP client and the assistant can search UK property with this Actor's own input fields. You pay per property delivered, at the same rate.

## Is it legal to scrape Rightmove?

The Actor reads public Rightmove listings only. Agents are named by their agency and branch only; a phone number or e-mail address written into a summary or key feature is replaced with `[phone removed]` / `[e-mail removed]`. That keeps the output to property data rather than personal data under GDPR; every record carries its `url`, and buyers and tenants contact the agent on Rightmove. You remain responsible for how you use the data and for the site's terms. This is an independent tool, not affiliated with Rightmove.

## FAQ

**How many properties per search?** Rightmove shows up to about 1,000 listings (42 pages) for one search; London alone has over 60,000 for sale. For more, split the search by price band, bedrooms or smaller areas.

**Sold STC and let agreed?** Left out by default, as on Rightmove. Tick **Include sold STC / let agreed** to get them too; `displayStatus` then says which.

**Are price changes included?** Yes. Every listing says whether it is new or reduced, and when (`listingUpdate`, `listingUpdateDate`, `addedOrReduced`), plus when it was first listed (`firstListed`).

**Why no agent phone numbers?** Every listing has its `url`; buyers and tenants contact the agent on Rightmove.

**Last updated:** 2026-10-15.

## Related Actors

- [Gumtree Scraper](https://apify.com/highbrow_fame/gumtree-uk-listings) – UK classifieds, cars and property
- [Funda Scraper](https://apify.com/highbrow_fame/funda-properties) – Dutch property listings
- [Realtor.com Scraper](https://apify.com/highbrow_fame/realtor-properties) – US property listings

Useful? A short Store review helps — your feedback decides what we improve next.
