---
title: "Austria apartments for rent: a daily new-listings feed from ImmoScout24 (Python)"
published: false
description: "Build a daily feed of new Vienna rental flats from ImmoScout24 Austria: filters, a 15-line dedupe in Python, rent per m² maths, and CSV or Google Sheets export."
tags: python, realestate, automation, webscraping
---

> Disclosure: I built the Apify Actor used in this tutorial. This post was written with AI assistance.

Finding a flat to rent in Vienna rewards whoever sees a listing first, and the comparisons you actually want, like rent per square metre by district, are not on the listing page. This tutorial builds a daily feed of new ImmoScout24 Austria rentals with the **ImmoScout24 Austria Scraper** (`highbrow_fame/immoscout24-at-properties`) on Apify. You set the filters once, a Python script runs every morning, keeps only listings it has not shown you before, computes rent per m², and writes a CSV you can open or push to Google Sheets. The Actor charges $1.50 per 1,000 properties on the free plan, so a 100-listing daily check costs about 15 cents a day.

## What a listing record contains

Every property comes back with `price` (the monthly rent for rentals), `priceText`, `currency`, `pricePerSqm`, `areaSqm`, `rooms`, `postcode`, `town`, `state`, `transaction`, `propertyType`, `title`, `features` (for example `BALCONY`, `GARDEN`, `FREE_OF_COMMISSION`), `sellerType`, `agency`, `listedAt`, `image`, `url` and `listingId`. Reduced listings carry `oldPrice` and `priceCutPercent`. Private owners are anonymous: no name, no street, no map point, only postcode and town. With `includeDetails: true` you also get `description`, `floor`, `yearBuilt`, `condition`, `heating`, the energy certificate (`heatingDemand`, `heatingDemandClass`, `energyEfficiencyClass`), `availableFrom`, `hasCommission`, `oneTimeCosts` and `monthlyCosts`.

## Step 1: set the filters

`locations` accepts Austrian cities, towns, Vienna districts, postcodes and states, so "Wien" covers the whole city and "1070" or "Neubau" narrows it to one district. The filters are plain fields:

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")

SEARCH = {
    "locations": ["Wien"],
    "transaction": "rent",
    "propertyType": "flat",
    "minArea": 50,
    "maxPrice": 1500,
    "minRooms": 2,
    "keyword": "Balkon",
    "sortBy": "newest",
    "maxListingsPerSearch": 100,
    "includeDetails": False,
}

run = client.actor("highbrow_fame/immoscout24-at-properties").call(run_input=SEARCH)
listings = [
    item for item in client.dataset(run.default_dataset_id).iterate_items()
    if not item.get("error") and item.get("price")
]
print(len(listings), "flats")
```

If you already have a search set up on immobilienscout24.at with every filter you want, paste its results URL into `searchUrls` instead and leave the field filters out. `sortBy: "newest"` is the right order for a feed: the newest 100 of a large search are the ones that changed since yesterday. `maxPrice` is the monthly rent in EUR.

The same input works outside Vienna. `["Graz", "Linz"]` searches two cities in one run, `["Tirol"]` a whole state, and because the place search reads "Salzburg" as the state, type the postcode `5020` for the city itself. Each place is one search, so `maxListingsPerSearch` applies per place. When you reach the shortlist stage, re-run the chosen `searchUrls` with `includeDetails: true` to get `monthlyCosts`, `oneTimeCosts`, `hasCommission`, `availableFrom` and the energy certificate, which together tell you what the flat really costs to move into and to heat.

## Step 2: feed mode in 15 lines

The Actor has no built-in only-new switch, so the feed lives in your script: remember every `listingId` you have delivered in a key-value store in your Apify account and skip the ones you have seen. The first run seeds the memory and reports everything.

```python
store = client.key_value_stores().get_or_create(name="immoscout-wien-feed")
kv = client.key_value_store(store.id)

record = kv.get_record("seen-ids")
seen = set(record["value"]) if record else set()

new_listings = [l for l in listings if l["listingId"] not in seen]
seen.update(l["listingId"] for l in listings)
kv.set_record("seen-ids", sorted(seen))

print(len(new_listings), "new since last run")
```

Run the script once a day from cron, a GitHub Actions schedule, or any other timer, and `new_listings` is your feed. If you ever change the filters, give the store a new name so the feed starts clean. Keep `maxListingsPerSearch` a little larger than a day's worth of new listings for your filters; if `len(listings)` keeps hitting the limit, raise it.

## Step 3: rent per m² and the district comparison

The Actor already fills `pricePerSqm` when the site shows it. Compute it yourself from `price` and `areaSqm` as a fallback, then compare each new flat with the median of its postcode across everything you fetched today:

```python
from statistics import median
from collections import defaultdict

def rent_per_sqm(l):
    if l.get("pricePerSqm"):
        return round(l["pricePerSqm"], 2)
    if l.get("areaSqm"):
        return round(l["price"] / l["areaSqm"], 2)
    return None

by_postcode = defaultdict(list)
for l in listings:
    r = rent_per_sqm(l)
    if r:
        by_postcode[l["postcode"]].append(r)
district_median = {pc: median(v) for pc, v in by_postcode.items()}

for l in new_listings:
    r = rent_per_sqm(l)
    l["rentPerSqm"] = r
    l["vsDistrictMedianPct"] = (
        round((r / district_median[l["postcode"]] - 1) * 100, 1)
        if r and l["postcode"] in district_median else None
    )
    pct = l["vsDistrictMedianPct"]
    vs = f"{pct:+}% vs district" if pct is not None else "no district median"
    cut = f' (cut {l["priceCutPercent"]}% from {l["oldPrice"]})' if l.get("oldPrice") else ""
    print(f'{l["postcode"]} {l["town"]:<10} {l["price"]:>5} EUR {l.get("areaSqm") or "?":>4} m2 '
          f'{r} EUR/m2 {vs}{cut}')
    print("   ", l["url"])
```

A flat at `-18%` against its postcode median deserves a look today, not next week. A `priceCutPercent` on a listing you saw last week is the other signal worth acting on, so you may want to keep reduced listings in the feed even when the ID is already known.

## Step 4: CSV and Google Sheets export

Write the enriched feed to a CSV that opens straight in Excel, Numbers or Sheets. The `features` list is joined into one cell:

```python
import csv
from datetime import date

FIELDS = ["listedAt", "postcode", "town", "price", "areaSqm", "rooms", "rentPerSqm",
          "vsDistrictMedianPct", "oldPrice", "priceCutPercent", "sellerType", "agency",
          "features", "url"]

path = f"wien-rent-{date.today()}.csv"
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
    w.writeheader()
    for l in new_listings:
        w.writerow({**l, "features": ", ".join(l.get("features") or [])})
print("wrote", path)
```

For Google Sheets you have two routes. The no-code one: in the Apify Console, save the input as a task and add the Google Sheets integration under the task's Integrations tab, which appends every run's dataset to a sheet. The code one: upload the CSV above with `gspread` or the Sheets API from the same cron job. The raw dataset is also available as CSV from the API, if you want it without any Python: `https://api.apify.com/v2/datasets/<datasetId>/items?format=csv`.

## Running costs

The Actor charges $0.0015 per property delivered on the free Apify plan, which is $1.50 per 1,000 properties, and less on paid plans down to $1.05 per 1,000. Opening listings for their details costs nothing extra, only time. A 100-listing daily run is $0.15 a day, or about $4.50 a month, and a place ImmoScout24 does not know comes back as a free record rather than a charged one.

Try it with the prefilled input: https://apify.com/highbrow_fame/immoscout24-at-properties
