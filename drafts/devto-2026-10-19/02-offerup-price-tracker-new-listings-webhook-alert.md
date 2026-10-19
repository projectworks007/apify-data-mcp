---
title: "OfferUp price tracker: get new listings for any search as a webhook alert"
published: false
description: "Turn any OfferUp search into a daily feed of only-new listings, post alerts to Slack or Discord, and filter price drops in a few lines of Python."
tags: python, automation, webscraping, ecommerce
---

> Disclosure: I built the Apify Actor used in this tutorial. This post was written with AI assistance.

Refreshing an OfferUp search every morning to catch a fairly priced road bike or a used camera body is a job for a script, not a person. This tutorial builds that script around the **OfferUp Scraper** (`highbrow_fame/offerup-listings`) on Apify. It has a feed mode that returns only listings you have not seen before, it can POST a summary to a Slack or Discord webhook on its own, and it charges $1.50 per 1,000 listings delivered, so a daily check of one search costs cents rather than dollars a month. You will end up with a scheduled daily run, a webhook alert, and a short Python filter that only pings you for price drops.

## What the Actor returns

One record per listing: `listingId`, `url`, `title`, `price`, `originalPrice`, `currency`, `isFirmPrice`, `condition`, `category`, `description`, `city`, `state`, `postedAt`, `localPickup`, `shippingAvailable`, `shippingPrice`, `sellerType`, `image` and `imageCount`. For vehicles you also get `make`, `model`, `year`, `trim`, `mileage` and `titleStatus` as separate fields. Phone numbers and private sellers' names are not delivered, and contact details inside descriptions are stripped. In feed mode each new listing also carries `firstSeenAt`.

## Step 1: define the search

You can paste a search URL from offerup.com into `searchUrls`, or describe the search with fields. The field version is easier to version-control:

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")

SEARCH = {
    "keywords": ["road bike"],
    "locations": ["Austin, TX"],
    "radiusMiles": "20",
    "category": "sports-and-outdoors",
    "minPrice": 200,
    "maxPrice": 900,
    "conditions": ["used", "open-box"],
    "sortBy": "newest",
    "maxListingsPerSearch": 60,
    "includeDetails": True,
}

run = client.actor("highbrow_fame/offerup-listings").call(run_input=SEARCH)
for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("error"):
        continue
    print(f'${item["price"]:>6}  {item["condition"]:<9} {item["city"]}, {item["state"]}  {item["title"]}')
    print("        ", item["url"])
```

`locations` takes US ZIP codes or "City, ST". `radiusMiles` is a string from the set 5, 10, 20, 30 or 50. `sortBy: "newest"` matters for a daily run: OfferUp's default relevance order reshuffles between runs, while newest-first is stable, so the same input returns a predictable window. `includeDetails` adds description, condition, post date and firm-price flag in one extra request per 50 listings at no extra charge.

## Step 2: switch on feed mode and the webhook

Two fields turn a search into a feed:

- `onlyNewListings: true` makes the Actor remember every listing it delivered for this exact input, in a key-value store in your own Apify account named `feed-<actor>-<hash>`. The first run returns everything. Every later run with the same input returns only listings not seen before, and seen items are neither saved nor charged. Memory lasts 60 days per item.
- `alertWebhookUrl` makes the Actor POST one JSON message when new items appear: `{actor, newCount, sampleItems, datasetUrl, runId}` with up to five sample items, plus a `text` field so a Slack or Discord incoming webhook renders it directly.

```python
FEED = {
    **SEARCH,
    "onlyNewListings": True,
    "alertWebhookUrl": "https://hooks.slack.com/services/T000/B000/XXXX",
}
```

Create the incoming webhook in Slack (Apps → Incoming Webhooks) or Discord (channel settings → Integrations → Webhooks) and paste its URL. Treat the URL as a secret: it sits in the run input, and the sample items are sent to it. Change any filter and the hash changes, so a new feed starts from scratch, which is what you want.

## Step 3: schedule it daily on Apify

The cleanest place to run the feed is Apify itself, so nothing on your laptop has to stay awake. In the Apify Console open the Actor, fill the input above, save it as a task, and add a schedule from the task's Schedules tab. Or create the schedule from Python once:

```python
import json

actor_id = client.actor("highbrow_fame/offerup-listings").get().id

schedule = client.schedules().create(
    name="offerup-road-bike-austin",
    cron_expression="0 13 * * *",
    timezone="America/Chicago",
    is_enabled=True,
    is_exclusive=True,
    actions=[{
        "type": "RUN_ACTOR",
        "actorId": actor_id,
        "runInput": {
            "body": json.dumps(FEED),
            "contentType": "application/json; charset=utf-8",
        },
    }],
)
print("schedule", schedule.id, "next run", schedule.next_run_at)
```

From now on, every day at 13:00 Central the Actor searches, drops everything it has seen, and posts to your channel only when there is something new. Schedules themselves carry no charge; you pay only for the runs.

## Step 4: price-drop filtering in a few lines of Python

The webhook tells you about every new listing in range. Sometimes you only want the ones that were marked down, or that sit well under the market. OfferUp exposes the earlier asking price as `originalPrice`, so a price drop is simply `price < originalPrice`. Run this from cron in place of the Apify schedule; it calls the same feed input, so deduplication still happens in the Actor:

```python
import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/0000/XXXX"
CEILING = 500  # alert on anything at or under this price even without a cut

run = client.actor("highbrow_fame/offerup-listings").call(run_input=FEED)
hits = []
for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("error") or item.get("price") is None:
        continue
    dropped = item.get("originalPrice") and item["price"] < item["originalPrice"]
    if dropped or item["price"] <= CEILING:
        tag = f'was ${item["originalPrice"]}' if dropped else "under ceiling"
        hits.append(f'${item["price"]} ({tag}) {item["title"]} - {item["city"]}, {item["state"]}\n{item["url"]}')

if hits:
    requests.post(DISCORD_WEBHOOK, json={"content": "New OfferUp price alerts:\n" + "\n".join(hits[:10])}, timeout=10)
```

The input is the unchanged `FEED`, so the Actor keeps the same feed memory and still posts its full new-listings summary to Slack, while this script sends only the price drops to Discord. If you want a single channel, drop `alertWebhookUrl` from the input before the first run and let the script do all the posting. Swap the Discord `content` payload for `{"text": ...}` if the target is Slack. Extend the filter however you like: `isFirmPrice` is `False` on listings open to offers, `postedAt` lets you skip anything older than a day, and for cars `mileage` and `year` are plain integers you can compare.

## What it costs

The Actor charges $0.0015 per listing delivered, which is $1.50 per 1,000 listings, with listing details included at no extra charge. Feed mode only bills the new listings, so after the first run a daily check of a 60-listing search typically delivers a handful of records a day and costs well under a dollar a month. Links that are not OfferUp searches and places OfferUp cannot find come back as free records.

Try it with the prefilled input: https://apify.com/highbrow_fame/offerup-listings
