# Vinted Scraper — Listings from 27 Countries, No Usernames

Vinted Scraper gets second-hand fashion listings from any of Vinted's 27 country sites, from vinted.fr, vinted.de and vinted.co.uk to vinted.com (US), vinted.pl and vinted.com.au. For every listing: title, brand, size, condition, price in the site's currency, the buyer-protection fee and the total, favourites, the main photo and the link. Paste your Vinted search links, or type keywords with brand, size, condition and price filters. It reads past Vinted's own 960-listing limit, sellers stay anonymous, and you pay only for listings delivered.

## What data does Vinted Scraper extract?

For every listing:

- `listingId`, `url`, `title`, `market` – the listing, and the country site it is on (`fr`, `de`, `uk`, `us`, `pl` …)
- `brand`, `size`, `condition` – as Vinted shows them, in the site's language (`Very good`, `Très bon état`, `Sehr gut` …)
- `price`, `currency` – the seller's price, in the site's currency
- `serviceFee`, `totalPrice` – Vinted's buyer-protection fee, and what a buyer pays before postage
- `favourites`, `promoted` – how many people saved it, and whether the seller paid to push it up
- `photo` – the main photo
- `sellerType` – `private` or `business` (Vinted Pro), nothing else about the seller
- `input`, `position`, `scrapedAt`, `status`, `error` – which search it came from, and why a search gave nothing

Category, colour, description and upload date are not included (Vinted shows them only on the listing page); filter by them in your search link.

## How to use Vinted Scraper

1. Open the Actor page and press **Try for free**. The Input tab is prefilled with a working example, so one click starts a run.
2. Paste **Search links** from any Vinted country site, one per line: a search, a category or a brand page, with all its filters.
3. Or type **Keywords**, pick the **Country site**, and narrow them with **Brands** (by name), **Condition**, **Sizes** (`M`, `38`, `W32`), **Min / Max price** and **Sort**. Brands with no keyword search the whole brand.
4. Set **Max listings per search** and press **Start**. Download the results from the **Output** tab as JSON, CSV or Excel. To follow new listings or prices, sort by "Newest first", save the input as a task and schedule it daily.

## Example output

Values are examples, shortened from a live run:

```json
{
  "market": "uk",
  "title": "Nike windbreaker XXL",
  "brand": "Nike",
  "size": "XXL",
  "condition": "New with tags",
  "price": 10,
  "currency": "GBP",
  "serviceFee": 1.2,
  "totalPrice": 11.2,
  "sellerType": "private"
}
```

## How much does it cost?

**$0.0015 per listing delivered on the Apify Free plan, $1.50 per 1,000 listings**; paid plans are lower, down to $1.05 per 1,000 on Gold and above. Links that are not Vinted searches, searches without results and brands Vinted does not know come back as free records with the reason.

Worked example: a live run read vinted.de, vinted.com, vinted.co.uk and vinted.fr searches together, 6,000 listings in 129 seconds, for **$9.00** on the Free plan. One search of 2,000 listings costs $3.00.

## Use it from AI agents (MCP)

The Actor is available through the Apify MCP server. Add `https://mcp.apify.com/?tools=highbrow_fame/vinted-listings` to Claude, ChatGPT or any MCP client and the assistant can search Vinted with this Actor's own input fields. You pay per listing delivered, at the same rate.

## Is it legal to scrape Vinted?

The Actor reads public Vinted listings only. Vinted sellers are mostly private persons, so no username, seller id, profile link, photo or place is collected, only whether the seller is a private person or a business. Phone numbers and e-mail addresses in titles are replaced with `[phone removed]` and `[e-mail removed]`. That keeps the output to listing data rather than personal data under GDPR; every listing has its `url`, and buyers contact the seller on Vinted. You remain responsible for how you use the data and for Vinted's terms. This is an independent tool, not affiliated with Vinted.

## FAQ

**How many listings per search?** Vinted itself stops every search at 960. Ask for more and the search is read in price bands (and then by condition), each under the limit: in live runs every search that had more gave its full 1,500 or 2,000, with no listing twice. The listings then no longer come in the order you chose.

**Why a few less than 960?** Vinted shows some listings on more than one page of a search; each listing comes only once. In a live run the 960 places of "robe" held 948 different listings in Vinted's own order and 958 cheapest first.

**Why listings of other brands in a keyword search?** They are what Vinted shows for the words: its keyword search is loose. Add a brand, in the link or in **Brands**, for a clean brand list.

**Which country sites and currencies?** All 27. A live run read all 27 sites in 8 seconds: EUR, GBP, USD, PLN, CZK, SEK, HUF, DKK, RON and AUD, with brand and condition on every listing.

**Last updated:** 2026-10-15.

## Related Actors

- [OfferUp Scraper](https://apify.com/highbrow_fame/offerup-listings) – US local marketplace listings with prices and details
- [Marktplaats & 2dehands Scraper](https://apify.com/highbrow_fame/marktplaats-2dehands-listings) – Dutch and Belgian classifieds
- [Kleinanzeigen Scraper](https://apify.com/highbrow_fame/kleinanzeigen-listings) – German ads, cars and flats

Useful? A short Store review helps — your feedback decides what we improve next.
