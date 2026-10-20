# Yahoo Finance quotes API - Python, n8n and LangChain example

> **[Run it on Apify](https://apify.com/highbrow_fame/yahoo-finance-quotes)** - **Yahoo Finance API & Scraper** returns stock, ETF, crypto, currency and index quotes - price, change, volume, market cap, P/E - with optional fundamentals and price history, as JSON.

Copy-paste integration examples for the [yahoo-finance-quotes](https://apify.com/highbrow_fame/yahoo-finance-quotes) Apify actor: call it from **Python**, an **n8n** workflow, or a **LangChain** agent. You need a free Apify account and an API token (`APIFY_TOKEN`). Start with a small limit to see the output, then scale up.

Keywords: yahoo finance api, yahoo finance scraper, stock quotes api, python stock prices, n8n stock price, langchain finance tool.

## What you can build

- Daily portfolio price alert via n8n
- Finance agent that quotes tickers on demand
- Pull history for backtests or charts

## What you get (output fields)

Field names from the actor's dataset schema:

| Field | Meaning |
|---|---|
| `symbol, name, quoteType, exchange, currency` | Instrument identity |
| `price, change, changePercent, previousClose` | Current price data |
| `open, dayLow, dayHigh, volume, averageVolume3Month` | Trading range and volume |
| `marketCap, trailingPE, forwardPE, dividendYield` | Valuation metrics |
| `fiftyTwoWeekLow, fiftyTwoWeekHigh, analystRating` | Range and sentiment |
| `profile, financials, keyStatistics` | Fundamentals (with includeFundamentals) |
| `history` | Price history (with includeHistory, historyRange, historyInterval) |

Example item (shortened; values are made-up placeholders, not real data):

```json
{
  "symbol": "EXMP",
  "name": "Example Corp (made-up)",
  "status": "ok",
  "currency": "USD",
  "price": 123.45,
  "changePercent": 0.8,
  "marketCap": 1000000000,
  "trailingPE": 21.3
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
  "symbols": [
    "AAPL",
    "MSFT",
    "BTC-USD"
  ],
  "includeFundamentals": false,
  "includeHistory": false
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

[langchain_tool.py](langchain_tool.py) wraps the actor with `ApifyActorsTool`, so an agent can call it like any other tool. Example prompt: *"What are the current prices of AAPL, MSFT and BTC-USD?"* Swap in any LangChain chat model.

## Why use this actor instead of building your own

- Ready-made and maintained: no browser, proxy or parsing code to write.
- Structured JSON with stable field names.
- One actor, many entry points: Python, n8n, LangChain, the Apify API or the Apify MCP server.
- Pay for what you run (see the Store page for current pricing).

## Try it now

**[Open yahoo-finance-quotes on Apify and run it](https://apify.com/highbrow_fame/yahoo-finance-quotes)**, then paste your token into the examples above.

---
Part of [apify-data-mcp](../../README.md), data tools for AI agents. More: [all integration examples](../README.md). Source: Yahoo Finance. Use the actor in line with the target site's terms and applicable law.
