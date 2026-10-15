---
title: Get an alert when a new rental appears on Rightmove, Realtor.com or Otodom (feed mode + webhook)
published: false
description: Turn a property search into a daily Slack or Discord alert with Apify feed mode, a webhook and a schedule. No polling code, pay only for new listings.
tags: abotwrotethis, automation, webhooks, javascript
---

> Disclosure: I built the Apify Actors used in this tutorial. This post was written with AI assistance and checked by me.

Flat hunting is a race against everyone else who set up the same search. Portals send their own e-mail alerts, but you cannot route them to a team channel or feed them into your own code. This tutorial builds the alert yourself: a scheduled scrape that remembers what it has already shown you, returns only new listings, and posts a summary to Slack or Discord the moment something new appears.

The same recipe works for three portals through three Apify Actors with identical feed and alert fields:

- [Rightmove](https://apify.com/highbrow_fame/rightmove-properties) (UK): $0.0008 per property delivered, so $0.80 per 1,000
- [Realtor.com](https://apify.com/highbrow_fame/realtor-properties) (US): $0.0012 per home delivered on Apify's free plan ($1.20 per 1,000), down to $0.00084 on paid plans
- [Otodom](https://apify.com/highbrow_fame/otodom-properties) (Poland): $0.0012 per listing on the free plan ($1.20 per 1,000), same paid-plan discount

You pay only for listings delivered. In feed mode, listings you have already seen are neither saved nor charged, which keeps a daily alert cheap.

You need an [Apify](https://apify.com) account with its API token, and a Slack or Discord incoming webhook URL.

## 1. Define the search

Each Actor takes either `searchUrls` (a results page from the portal, with every filter you set there) or `locations` plus filters. Here is a rental search per portal, as the JSON input you hand to the Actor.

Rightmove, two-bedroom flats to rent in Bristol up to £1,500 a month:

```json
{
  "locations": ["Bristol"],
  "channel": "rent",
  "minBedrooms": 2,
  "maxPrice": 1500,
  "maxListingsPerSearch": 200,
  "onlyNewListings": true,
  "alertWebhookUrl": "https://hooks.slack.com/services/T000/B000/XXXX"
}
```

Realtor.com, rentals in Austin that allow cats, up to $2,000 a month:

```json
{
  "locations": ["Austin, TX"],
  "searchType": "forRent",
  "maxPrice": 2000,
  "catsAllowed": true,
  "sortBy": "newest",
  "maxListingsPerSearch": 200,
  "onlyNewListings": true,
  "alertWebhookUrl": "https://hooks.slack.com/services/T000/B000/XXXX"
}
```

Otodom, two- and three-room flats to rent in Kraków up to 4,000 PLN:

```json
{
  "locations": ["Kraków"],
  "transaction": "rent",
  "propertyType": "flat",
  "rooms": ["2", "3"],
  "maxPrice": 4000,
  "sortBy": "newest",
  "maxListingsPerSearch": 200,
  "onlyNewListings": true,
  "alertWebhookUrl": "https://hooks.slack.com/services/T000/B000/XXXX"
}
```

`onlyNewListings` and `alertWebhookUrl` are shared by all three. Everything else mirrors the portal's own filters (monthly price for rentals, bedrooms, pets, radius). Otodom's `rooms` values are strings, as in its input schema.

## 2. Run it once by hand

The first run in feed mode returns everything that matches, so run it from your terminal before scheduling anything. With `curl`:

```bash
export APIFY_TOKEN=apify_api_xxxxxxxx

curl -X POST "https://api.apify.com/v2/acts/highbrow_fame~rightmove-properties/runs?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d @rightmove-input.json
```

Or with the Node client, which also waits for the run to finish:

```javascript
import { ApifyClient } from 'apify-client';
import { readFileSync } from 'node:fs';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = JSON.parse(readFileSync('rightmove-input.json', 'utf8'));

const run = await client.actor('highbrow_fame/rightmove-properties').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} listings`);
```

A Rightmove record looks like this (illustrative values, shortened):

```json
{
  "price": 1350,
  "displayPrice": "£1,350 pcm",
  "priceFrequency": "monthly",
  "bedrooms": 2,
  "propertyType": "Flat",
  "address": "Clifton, Bristol, BS8",
  "addedOrReduced": "Added on 14/10/2026",
  "letAvailableDate": "01/11/2026",
  "agent": "Example Lettings",
  "url": "https://www.rightmove.co.uk/properties/123456789",
  "firstSeenAt": "2026-10-15T07:00:12.000Z"
}
```

`firstSeenAt` is added in feed mode. Realtor.com records use `price`, `beds`, `baths`, `sqft`, `fullAddress` and `listingOffice`; Otodom records `price`, `pricePerSqm`, `areaSqm`, `rooms`, `district` and `agency`. None delivers agent names or phone numbers: every record has its `url`.

If 200 listings matched, the first Rightmove run cost 200 × $0.0008 = $0.16. From now on you only pay for what is new.

## 3. How the 60-day memory works

Feed mode keeps a list of seen listings in a key-value store in your own Apify account, named `feed-<actor>-<hash>`. The hash is computed from your search inputs, leaving out the feed, alert, proxy and concurrency settings. Three consequences follow from that design:

- **One memory per search.** Two different searches (say Bristol and Bath) have two separate memories and never interfere.
- **Changing a filter starts a fresh memory.** If you raise `maxPrice` from 1500 to 1600, the hash changes, and the next run returns everything again, charged as a first run. Decide on the search before you schedule it.
- **A listing is remembered for 60 days after it was last seen**, up to 50,000 per search. While it keeps appearing in the daily results the clock resets. If it disappears and comes back after more than 60 days, it is reported as new again, which is usually what you want.

Items already in the memory are filtered before anything is written to the dataset, so they cost nothing and do not clutter your results.

## 4. The webhook payload

When a run finds at least one new listing, the Actor sends a single POST to `alertWebhookUrl` with a 10-second timeout. A failed delivery is logged and never fails the run. The body:

```json
{
  "text": "rightmove-properties: 3 new items — https://console.apify.com/storage/datasets/<datasetId>",
  "actor": "rightmove-properties",
  "newCount": 3,
  "sampleItems": [
    { "url": "https://www.rightmove.co.uk/properties/123456789", "firstSeenAt": "2026-10-15T07:00:12.000Z" }
  ],
  "datasetUrl": "https://console.apify.com/storage/datasets/<datasetId>",
  "runId": "<runId>"
}
```

`sampleItems` holds at most five entries; the full list is in the run's dataset.

**Slack:** create an incoming webhook (Slack app, Incoming Webhooks, Add New Webhook to Workspace) and paste its URL. Slack reads the `text` field and ignores the rest.

**Discord:** Discord's native webhook expects a `content` field, not `text`, so a plain Discord webhook URL would reject the payload. Discord also offers a Slack-compatible endpoint: append `/slack` to the webhook URL you copied from the channel settings and use that as `alertWebhookUrl`:

```
https://discord.com/api/webhooks/<id>/<token>/slack
```

**Your own endpoint:** any HTTPS URL works. The useful field for code is `runId`: it lets you fetch all new items, not just the five samples. A minimal Node handler:

```javascript
import express from 'express';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const app = express();
app.use(express.json());

app.post('/new-listings', async (req, res) => {
  res.sendStatus(200); // answer fast, work after
  const { actor, newCount, runId } = req.body;
  const { items } = await client.run(runId).dataset().listItems();
  for (const item of items) {
    console.log(`[${actor}] ${item.price} ${item.url} first seen ${item.firstSeenAt}`);
    // send an e-mail, write to a database, push to a phone...
  }
  console.log(`${newCount} new listings handled`);
});

app.listen(3000);
```

Answer the request before doing the work; the Actor gives up after 10 seconds.

## 5. Schedule it

Apify Schedules run an Actor with a fixed input on a cron expression. In the Console: Schedules, Create new, add your Actor under Actions, paste the JSON input from step 1, set cron and timezone, enable. `0 7 * * *` in `Europe/London` runs daily at 07:00.

The same thing through the API, with the Node client. The schedule needs the Actor's ID rather than its name, which `actor().get()` returns:

```javascript
import { ApifyClient } from 'apify-client';
import { readFileSync } from 'node:fs';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = JSON.parse(readFileSync('rightmove-input.json', 'utf8'));
const actor = await client.actor('highbrow_fame/rightmove-properties').get();

const schedule = await client.schedules().create({
  name: 'bristol-rentals-daily',
  cronExpression: '0 7 * * *',
  timezone: 'Europe/London',
  isEnabled: true,
  isExclusive: true,
  actions: [{
    type: 'RUN_ACTOR',
    actorId: actor.id,
    runInput: {
      body: JSON.stringify(input),
      contentType: 'application/json; charset=utf-8',
    },
  }],
});
console.log('schedule', schedule.id);
```

`isExclusive: true` skips a run if the previous one is still going; `runInput.body` is a string, hence the `JSON.stringify`.

Running more often than daily is allowed, but every run still has to read the search results to find out what is new, so twice a day is a reasonable upper limit for a personal search.

## What this costs over a month

Take the Bristol search: 200 listings on day one ($0.16), then perhaps 5 to 15 new listings a day. Thirty days at 10 a day is 300 listings, or $0.24: under half a dollar for the month on Rightmove, roughly $0.60 on Realtor.com or Otodom at the free-plan rate, inside the free plan's monthly usage credit.

## Limits

- Each portal caps a single search: about 1,000 listings on Rightmove, 10,000 on Realtor.com. For a broad search, split it by price band or area, each with its own feed.
- Feed memory is 50,000 items per search and 60 days per item.
- The webhook is one POST per run, not one per listing. Fan-out is your endpoint's job.
- The Actors read public listing pages and deliver no agent names, phone numbers or e-mails. You remain responsible for each portal's terms of use.

Input schemas with every filter, example output and the pricing tables are on the three Actor pages: [Rightmove](https://apify.com/highbrow_fame/rightmove-properties), [Realtor.com](https://apify.com/highbrow_fame/realtor-properties) and [Otodom](https://apify.com/highbrow_fame/otodom-properties).
