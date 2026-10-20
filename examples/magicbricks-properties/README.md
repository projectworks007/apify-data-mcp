# Magicbricks India property listings API - Python, n8n and LangChain example

> **[Run it on Apify](https://apify.com/highbrow_fame/magicbricks-properties)** - **Magicbricks Scraper** returns India property listings for sale or rent - price, area, bedrooms, locality, developer, RERA ID and more - as JSON for Python, n8n and AI agents.

Copy-paste integration examples for the [magicbricks-properties](https://apify.com/highbrow_fame/magicbricks-properties) Apify actor: call it from **Python**, an **n8n** workflow, or a **LangChain** agent. You need a free Apify account and an API token (`APIFY_TOKEN`). Start with a small limit to see the output, then scale up.

Keywords: magicbricks scraper, magicbricks api, india property listings, pune flats, real estate india data, n8n, langchain, python.

## What you can build

- Price tracker for an Indian city or locality
- Lead lists for brokers and investors
- Agent that answers 'what is a 2 BHK in Pune going for?'

## What you get (output fields)

Field names from the actor's dataset schema:

| Field | Meaning |
|---|---|
| `title, url, listingId` | Listing identity |
| `transaction, propertyType, bedrooms, bathrooms` | What and how big |
| `price, priceDisplay, pricePerSqft, currency` | Price data |
| `areaSqft, superArea, carpetArea, floor, furnishing` | Size and unit details |
| `city, locality, society, developer, reraId` | Where and who |
| `latitude, longitude, address` | Location |
| `sellerType, seller, postedAt` | Who lists it and when |
| `amenities, description, image` | Extras |

Example item (shortened; values are made-up placeholders, not real data):

```json
{
  "title": "Example 2 BHK flat (made-up)",
  "transaction": "sale",
  "propertyType": "flat",
  "bedrooms": 2,
  "areaSqft": 950,
  "city": "Pune",
  "locality": "Example Locality",
  "sellerType": "agent",
  "url": "https://www.magicbricks.com/..."
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
  "places": [
    "Pune"
  ],
  "transaction": "sale",
  "propertyType": "flat",
  "bedrooms": [
    "2",
    "3"
  ],
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

[langchain_tool.py](langchain_tool.py) wraps the actor with `ApifyActorsTool`, so an agent can call it like any other tool. Example prompt: *"Find 3 BHK flats for sale in Whitefield, Bangalore and show the cheapest five."* Swap in any LangChain chat model.

## Why use this actor instead of building your own

- Ready-made and maintained: no browser, proxy or parsing code to write.
- Structured JSON with stable field names.
- One actor, many entry points: Python, n8n, LangChain, the Apify API or the Apify MCP server.
- Pay for what you run (see the Store page for current pricing).

## Try it now

**[Open magicbricks-properties on Apify and run it](https://apify.com/highbrow_fame/magicbricks-properties)**, then paste your token into the examples above.

---
Part of [apify-data-mcp](../../README.md), data tools for AI agents. More: [all integration examples](../README.md). Source: Magicbricks. Use the actor in line with the target site's terms and applicable law.
