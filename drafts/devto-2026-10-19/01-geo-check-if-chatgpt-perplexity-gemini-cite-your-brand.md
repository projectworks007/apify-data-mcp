---
title: "Generative engine optimization (GEO): check if ChatGPT, Perplexity and Gemini cite your brand"
published: false
description: "A hands-on GEO tutorial: run a free sample check, read which sources AI answers cite, track the weekly delta in Python, and act when competitors are cited instead of you."
tags: ai, seo, marketing, python
---

> Disclosure: I built the Apify Actor used in this tutorial. This post was written with AI assistance.

If a buyer asks ChatGPT or Perplexity "which CRM should a 10-person sales team use" and the answer names three other companies, you have a visibility problem that no Google ranking report will show you. This tutorial fixes the measurement half of that problem with the **AI Search Visibility Tracker** (`highbrow_fame/ai-search-visibility-tracker`) on Apify. In about ten minutes you will know, for your own questions, whether the AI engines cite your domain, what share of the citations you hold against named competitors, and the exact URLs the models read. The first check is a free sample run, so you can see real output before paying a cent for results.

## What GEO means in plain terms

Generative engine optimization (GEO) is the practice of getting your brand into the answers that AI assistants generate. Classic SEO targets a ranked list of links. GEO targets a paragraph of prose with a short list of sources behind it. The model writes that paragraph from the pages it retrieves, so the lever is the same as it always was: be present on the pages the model reads. The difference is that you cannot see those pages in a rank tracker. You need the source list for each answer, and you need it repeatedly, because AI answers change from run to run.

That is what the Actor returns: one record per question, per engine, per sample, with the answer text, every cited URL, and a match against the domains you care about.

## Step 1: the free sample run

Install the client and start a sample run. `sampleRun: true` runs your first three queries three times each on the included Perplexity engine. The result fee is zero for a sample run; only the platform run-start fee of $0.0004 at the default memory applies.

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")

QUERIES = [
    "CRM for a 10-person sales team recommendations",
    "simple CRM with a free plan for startups",
    "CRM that integrates with Slack for small agencies",
]

run_input = {
    "sampleRun": True,
    "queries": QUERIES,
    "brandDomains": ["lumenly.example"],
    "competitorDomains": ["brightdesk.example", "pipeflow.example"],
    "engines": ["perplexity-agent"],
    "language": "en",
}

run = client.actor("highbrow_fame/ai-search-visibility-tracker").call(run_input=run_input)
records = list(client.dataset(run.default_dataset_id).iterate_items())
print(len(records), "records in dataset", run.default_dataset_id)
```

Swap `lumenly.example` and the competitor domains for real bare hostnames (no `https://`, no `www.`). If you pass only `brand`, the Actor writes a starter set of questions for that domain, but your own buyer questions always beat generated ones. Keep the sample on the default engine: Perplexity needs no API key from you and answers in 24 languages, so `"language": "de"` gives you German sources for the German market.

## Step 2: read brandCited, citation share and the source URLs

Every engine call writes a record with `"type": "citation"`. The three fields that matter are the brand match, the `citationShare` map, and the `citations` list with the URLs the model used. The brand verdict is exposed as `brandCited`, with the per-domain detail in `brandMatches`, so the helper below reads whichever is present.

```python
def brand_cited(rec):
    if "brandCited" in rec:
        return bool(rec["brandCited"])
    return any(m.get("cited") for m in rec.get("brandMatches", {}).values())

for rec in records:
    if rec.get("type") != "citation":
        continue
    print(f'\n[{rec["engine"]}] {rec["query"]}')
    print("  brand cited:", brand_cited(rec))
    for domain, share in rec.get("citationShare", {}).items():
        print(f'  {domain:<22} {share["hits"]} hits  {share["sharePct"]}% share')
    for c in rec.get("citations", []):
        print("  source:", c["url"])
```

Because the sample runs three samples per query, you also get one `stability` record per query. It tells you how many of the three samples cited each domain. A domain at `1.0` is the model's settled answer. A domain at `0.33` showed up once and may be noise. Filter on it before you draw conclusions:

```python
for rec in records:
    if rec.get("type") != "stability":
        continue
    stable = {d: s["stability"] for d, s in rec["stability"].items() if s["stability"] >= 0.5}
    print(rec["query"], "->", stable)
```

The `summary` record at the end of the dataset closes the run and is never billed, same as `stability`, `delta` and error records.

## Step 3: track it weekly with the previous-run delta

A snapshot is interesting once. The weekly change is what goes into a report. Pass the dataset ID of last week's run as `previousRunDatasetId` and the Actor writes a `delta` record with the domains gained and lost per query. The script below keeps the last dataset ID in a key-value store in your Apify account, so it works unchanged from any weekly cron job or CI schedule.

```python
store = client.key_value_stores().get_or_create(name="geo-tracker-state")
kv = client.key_value_store(store.id)

weekly_input = {
    "queries": QUERIES,
    "brandDomains": ["lumenly.example"],
    "competitorDomains": ["brightdesk.example", "pipeflow.example"],
    "engines": ["perplexity-agent"],
    "samplesPerQuery": 3,
}
previous = kv.get_record("last-dataset-id")
if previous:
    weekly_input["previousRunDatasetId"] = previous["value"]

run = client.actor("highbrow_fame/ai-search-visibility-tracker").call(run_input=weekly_input)
kv.set_record("last-dataset-id", run.default_dataset_id)

for rec in client.dataset(run.default_dataset_id).iterate_items():
    if rec.get("type") != "delta":
        continue
    for query, domains in rec["gained"].items():
        print("GAINED", query, domains)
    for query, domains in rec["lost"].items():
        print("LOST  ", query, domains)
    print("unchanged queries:", rec["unchangedQueryCount"])
```

A line such as `LOST  "simple CRM with a free plan for startups" ['lumenly.example']` is the sentence that gets read in a Monday meeting. Post it to Slack from the same script if you like.

Mind the included allowance on the default engine: a free Apify plan covers 12 engine calls per run, a paid plan 200. Queries beyond that come back as `not_measured` records, unbilled, with a note on how to lift the limit. Four queries at three samples fits the free allowance exactly.

## Step 4: what to do when competitors are cited instead

The `competitorMatches` map tells you which rival domains were cited for each question. The instinct is to rewrite your own landing page. Resist it for a moment and look at the `citations` list instead. Those URLs are the pages the model retrieved: a review site, a comparison article, a community thread, a vendor blog. If a competitor appears there and you do not, that list is your work list.

- **Review and directory pages** cited across several queries: get listed and get reviews there.
- **Comparison articles** on third-party sites: pitch an inclusion, or publish your own honest comparison on your domain so it can be retrieved.
- **Community threads**: answer the question there with real substance.
- **Your own pages** that never appear: check that the page answers the literal question in its first paragraph, with the product name and the use case spelled out.

Then re-run next week and read the delta. Nobody can force a citation, and this Actor measures rather than promises, but the source list turns a vague "be more visible to AI" into a short list of pages to earn.

## What it costs

A full run charges $0.05 per citation record, which is $50 per 1,000 citation records. One record is one engine answering one question once, so ten questions on one engine at one sample cost $0.50, and the same at three samples cost $1.50. Stability, delta, summary and error records are free. The sample run has no result fee at all.

Try it with the prefilled input: https://apify.com/highbrow_fame/ai-search-visibility-tracker
