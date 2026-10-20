# Google Maps leads with emails - Python, n8n and LangChain example

> **[Run it on Apify](https://apify.com/highbrow_fame/google-maps-email-extractor)** - **Google Maps Email Extractor & Lead Scraper** turns a search like "dentists in Vienna" into a list of businesses with website, phone and validated email addresses, ready for outreach, CRMs and AI agents.

Copy-paste integration examples for the [google-maps-email-extractor](https://apify.com/highbrow_fame/google-maps-email-extractor) Apify actor: call it from **Python**, an **n8n** workflow, or a **LangChain** agent. You need a free Apify account and an API token (`APIFY_TOKEN`). Start with a small limit to see the output, then scale up.

Keywords: google maps scraper, google maps leads, google maps email extractor, local business leads, b2b lead generation, n8n, langchain, python.

## What you can build

- Build a prospect list for a local-business agency
- Feed a CRM or cold-email tool from an n8n workflow
- Give an AI agent a live 'find businesses near X' tool

## What you get (output fields)

Field names from the actor's dataset schema:

| Field | Meaning |
|---|---|
| `name` | Business name |
| `category, industry` | What the business does |
| `address, phone, website` | Core contact data |
| `primaryEmail, primaryEmailType, emailValidation` | Best email found on the site, with deliverability grading |
| `whatsapp, hasContactForm, ownerName` | Extra contact signals when present |
| `rating, reviewCount, businessStatus` | Google Maps reputation data |
| `leadScore, leadReadiness` | 0-100 lead score and readiness label |
| `suggestedOpener, aiLeadProfile` | Outreach hints for LLM workflows |
| `googleMapsUrl` | Link back to the place |

Example item (shortened; values are made-up placeholders, not real data):

```json
{
  "name": "Example Dental Studio (made-up)",
  "category": "Dentist",
  "address": "1 Example Street, Vienna",
  "phone": "+00 000 000000",
  "website": "https://example-dental.invalid",
  "primaryEmail": "info@example-dental.invalid",
  "leadScore": 72,
  "leadReadiness": "warm",
  "googleMapsUrl": "https://www.google.com/maps/place/..."
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
  "searchQueries": [
    "dentists in Vienna"
  ],
  "maxResults": 25,
  "scrapeEmails": true,
  "validateEmails": true,
  "language": "en"
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

[langchain_tool.py](langchain_tool.py) wraps the actor with `ApifyActorsTool`, so an agent can call it like any other tool. Example prompt: *"Find 10 plumbers in Dublin and list the ones that have an email address."* Swap in any LangChain chat model.

## Why use this actor instead of building your own

- Ready-made and maintained: no browser, proxy or parsing code to write.
- Structured JSON with stable field names.
- One actor, many entry points: Python, n8n, LangChain, the Apify API or the Apify MCP server.
- Pay for what you run (see the Store page for current pricing).

## Try it now

**[Open google-maps-email-extractor on Apify and run it](https://apify.com/highbrow_fame/google-maps-email-extractor)**, then paste your token into the examples above.

---
Part of [apify-data-mcp](../../README.md), data tools for AI agents. More: [all integration examples](../README.md). Source: Google Maps. Use the actor in line with the target site's terms and applicable law.
