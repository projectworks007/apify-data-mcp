# ImmoScout24 Austria property listings API - Python, n8n and LangChain example

> **[Run it on Apify](https://apify.com/highbrow_fame/immoscout24-at-properties)** - **ImmoScout24 Austria Scraper** returns property listings for sale or rent in Austria - price, area, rooms, location, seller type and more - as clean JSON for Python, n8n or an AI agent.

Copy-paste integration examples for the [immoscout24-at-properties](https://apify.com/highbrow_fame/immoscout24-at-properties) Apify actor: call it from **Python**, an **n8n** workflow, or a **LangChain** agent. You need a free Apify account and an API token (`APIFY_TOKEN`). Start with a small limit to see the output, then scale up.

Keywords: immoscout24 austria scraper, immoscout24.at api, austrian real estate data, wien apartments, property listings api, n8n, langchain, python.

## What you can build

- Rental and price monitor for Austrian cities
- Investor or agency market dashboards
- Agent that answers 'what does a flat in Linz cost?'

## What you get (output fields)

Field names from the actor's dataset schema:

| Field | Meaning |
|---|---|
| `title, url, listingId` | What the listing is and where to find it |
| `transaction, propertyType` | Buy or rent; flat, house, plot, commercial |
| `price, priceText, currency, pricePerSqm` | Price data |
| `areaSqm, rooms` | Size |
| `floor, yearBuilt, heating, energyEfficiencyClass` | Building details (with includeDetails) |
| `postcode, town, state, street, latitude, longitude` | Location |
| `sellerType, agency` | Private seller or agency |
| `listedAt, image, scrapedAt` | Freshness and media |

Example item (shortened; values are made-up placeholders, not real data):

```json
{
  "title": "Example 2-room flat (made-up)",
  "transaction": "rent",
  "propertyType": "flat",
  "price": 1100,
  "currency": "EUR",
  "areaSqm": 55,
  "rooms": 2,
  "postcode": "1100",
  "town": "Wien",
  "sellerType": "agency",
  "url": "https://www.immobilienscout24.at/..."
}
```

## 1. Python (`python_example.py`)

```bash
pip install apify-client
export APIFY_TOKEN=your_token
python python_example.py
```

[python_example.py](python_example.py) runs the actor with this input and prints the results:

```json
{
  "locations": [
    "Wien"
  ],
  "transaction": "rent",
  "propertyType": "flat",
  "maxListingsPerSearch": 50,
  "sortBy": "newest"
}
```

## 2. n8n (`n8n_workflow.json`)

Import [n8n_workflow.json](n8n_workflow.json) (Workflows -> Import from file). It is Manual Trigger -> HTTP Request, which POSTs to the `run-sync-get-dataset-items` endpoint and returns the dataset items directly.

- Provide the token as an `APIFY_TOKEN` environment variable on your n8n instance. If your n8n blocks env access in nodes, use an HTTP Header Auth credential (`Authorization: Bearer <token>`) instead of the URL token.
- The sync endpoint waits up to about 5 minutes. For bigger jobs use the async run endpoint or the official Apify node, then fetch the dataset when the run finishes.
- Connect the output to Google Sheets, Airtable, Slack, a CRM or an LLM node.

## 3. LangChain agent (`langchain_tool.py`)

```bash
pip install langchain-apify langchain langgraph langchain-openai
export APIFY_TOKEN=your_token OPENAI_API_KEY=your_key
python langchain_tool.py
```

[langchain_tool.py](langchain_tool.py) wraps the actor with `ApifyActorsTool`, so an agent can call it like any other tool. Example prompt: *"List the 5 newest rental flats in Graz and show price, area and rooms."* Swap in any LangChain chat model.

## Why use this actor instead of building your own

- Ready-made and maintained: no browser, proxy or parsing code to write.
- Structured JSON with stable field names.
- One actor, many entry points: Python, n8n, LangChain, the Apify API or the Apify MCP server.
- Pay for what you run (see the Store page for current pricing).

## Try it now

**[Open immoscout24-at-properties on Apify and run it](https://apify.com/highbrow_fame/immoscout24-at-properties)**, then paste your token into the examples above.

---
Part of [apify-data-mcp](../../README.md), data tools for AI agents. More: [all integration examples](../README.md). Source: ImmoScout24 Austria. Use the actor in line with the target site's terms and applicable law.
