# AI search visibility tracking (is your brand cited by ChatGPT, Perplexity and Google AI?) - Python, n8n and LangChain example

> **[Run it on Apify](https://apify.com/highbrow_fame/ai-search-visibility-tracker)** - **AI Brand Monitor - AI Search Visibility Tracker** asks AI search engines your customers' questions and reports whether your domain is cited, which competitors are cited instead, and your citation share.

Copy-paste integration examples for the [ai-search-visibility-tracker](https://apify.com/highbrow_fame/ai-search-visibility-tracker) Apify actor: call it from **Python**, an **n8n** workflow, or a **LangChain** agent. You need a free Apify account and an API token (`APIFY_TOKEN`). Start with a small limit to see the output, then scale up.

Keywords: ai search visibility, generative engine optimization, GEO, ai brand monitor, perplexity citations, chatgpt brand mentions, n8n, langchain, python.

## What you can build

- Weekly AI-visibility (GEO) report sent from n8n to Slack or email
- Agent that audits a client's brand against competitors
- Track citation share over time by re-running the same queries

## What you get (output fields)

Field names from the actor's dataset schema:

| Field | Meaning |
|---|---|
| `query, engine, model` | Which question was asked on which AI engine |
| `brandCited` | Was your domain cited? (true/false) |
| `competitorsCited` | Which tracked competitors were cited instead |
| `citationShare` | Your share of cited sources per tracked domain |
| `brandMatches, competitorMatches` | Per-domain detail: citation vs text mention, matched URLs |
| `citationCount, language, startedAt` | Run metadata |

Tip: `sampleRun: true` is a good first test run; remove it for a full tracked run. Check the Store page for the current engines and pricing.

Example item (shortened; values are made-up placeholders, not real data):

```json
{
  "query": "best CRM for small business",
  "engine": "perplexity-agent",
  "brandCited": false,
  "competitorsCited": [
    "competitor-one.com"
  ],
  "citationShare": {
    "example.com": 0,
    "competitor-one.com": 0.25
  },
  "citationCount": 8
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
  "brand": "example.com",
  "queries": [
    "best CRM for small business",
    "HubSpot alternatives"
  ],
  "competitorDomains": [
    "competitor-one.com"
  ],
  "engines": [
    "perplexity-agent"
  ],
  "sampleRun": true
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

[langchain_tool.py](langchain_tool.py) wraps the actor with `ApifyActorsTool`, so an agent can call it like any other tool. Example prompt: *"Check whether example.com is cited by AI search for 'best CRM for small business' and tell me who is cited instead."* Swap in any LangChain chat model.

## Why use this actor instead of building your own

- Ready-made and maintained: no browser, proxy or parsing code to write.
- Structured JSON with stable field names.
- One actor, many entry points: Python, n8n, LangChain, the Apify API or the Apify MCP server.
- Pay for what you run (see the Store page for current pricing).

## Try it now

**[Open ai-search-visibility-tracker on Apify and run it](https://apify.com/highbrow_fame/ai-search-visibility-tracker)**, then paste your token into the examples above.

---
Part of [apify-data-mcp](../../README.md), data tools for AI agents. More: [all integration examples](../README.md). Source: AI search engines. Use the actor in line with the target site's terms and applicable law.
