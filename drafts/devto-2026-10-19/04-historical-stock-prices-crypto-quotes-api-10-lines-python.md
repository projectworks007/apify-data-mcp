---
title: "Historical stock prices and crypto quotes API in 10 lines of Python"
published: false
description: "Fetch live quotes, daily price history and company fundamentals for stocks, ETFs and crypto with one Apify Actor, then build a small portfolio report."
tags: python, finance, api, tutorial
---

> Disclosure: I built the Apify Actor used in this tutorial. This post was written with AI assistance.

You want today's price for a handful of tickers, a year of daily closes for a backtest, and the sector and margins for a screen, without signing up for three different market-data plans. The **Yahoo Finance Scraper** (`highbrow_fame/yahoo-finance-quotes`) on Apify returns all three for stocks on any exchange, ETFs, crypto, currencies and indexes, from a single input, for $1.00 per 1,000 symbols on the free Apify plan. Price history and company data cost nothing extra. Here is the ten-line version, then the options, then a small portfolio report you can run after the close every day.

## The 10 lines

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("highbrow_fame/yahoo-finance-quotes").call(
    run_input={"symbols": ["AAPL", "VOD.L", "SAP.DE", "SPY", "BTC-USD", "EURUSD=X", "^GSPC"]}
)
for q in client.dataset(run.default_dataset_id).iterate_items():
    if q.get("price") is None:
        continue
    print(f'{q["symbol"]:<9} {q["price"]:>12,.2f} {q.get("changePercent") or 0:+6.2f}%  {q["currency"]} {q["exchange"]}')
```

Symbols are written exactly as Yahoo Finance writes them: `VOD.L` for London, `SAP.DE` for Xetra, `7203.T` for Tokyo, `BTC-USD` for Bitcoin, `EURUSD=X` for a currency pair, `GC=F` for gold futures and `^GSPC` for the S&P 500. Quotes come 50 symbols to a request, so a 300-symbol watchlist is a handful of requests rather than 300. A symbol Yahoo does not know comes back as a free record with `error` set and no `price`, which is why the loop skips those.

Each record carries the full quote: `price`, `change`, `changePercent`, `previousClose`, `open`, `dayLow`, `dayHigh`, `volume`, `bid`, `ask`, `marketTime` and `marketState`, the ranges `fiftyTwoWeekLow`, `fiftyTwoWeekHigh`, `fiftyDayAverage` and `twoHundredDayAverage`, valuation fields `marketCap`, `trailingPE`, `forwardPE`, `epsTrailingTwelveMonths` and `priceToBook`, and `dividendRate`, `dividendYield`, `dividendDate`, `earningsDate` and `analystRating`. `exchangeDelayMinutes` tells you whether the quote is real-time or delayed for that exchange.

## Option 1: price history

Set `includeHistory: true` and pick a range and interval. `historyRange` takes `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd` or `max`; `historyInterval` takes `1m`, `5m`, `15m`, `30m`, `60m`, `1d`, `1wk` or `1mo`, with minute intervals available for recent days only. Exact dates go in `historyFrom` and `historyTo` as `YYYY-MM-DD` and override the range. The history lands in `history.points`, a list of `{date, open, high, low, close, adjClose, volume}`, plus `history.dividends` and `history.splits`.

```python
run = client.actor("highbrow_fame/yahoo-finance-quotes").call(run_input={
    "symbols": ["AAPL", "BTC-USD"],
    "includeHistory": True,
    "historyRange": "1y",
    "historyInterval": "1d",
})
for q in client.dataset(run.default_dataset_id).iterate_items():
    points = q.get("history", {}).get("points") or []
    if not points:
        continue
    first, last = points[0], points[-1]
    total_return = (last["adjClose"] / first["adjClose"] - 1) * 100
    print(f'{q["symbol"]}: {len(points)} days, {first["date"]} to {last["date"]}, '
          f'{total_return:+.1f}% total return, {len(q["history"].get("dividends") or [])} dividends')
```

If you work in pandas, `pd.DataFrame(points).set_index("date")` gives you a frame per symbol. Dividends and splits are already applied in `adjClose`, so return maths uses that column; `close` is the raw print.

For a growing local archive, store the last date you have per symbol and pass it as `historyFrom` on the next run, so each day fetches only the missing points. Intraday work uses the minute intervals with a short range such as `5d`; Yahoo keeps minute bars for recent days only, so archive them as you go if you need them later.

## Option 2: company data

`includeFundamentals: true` adds three objects per symbol: `profile` (sector, industry, website, employees, business summary), `financials` (revenue, growth, margins, EBITDA, cash, debt, free cash flow, ROE, analyst targets and recommendation) and `keyStatistics` (enterprise value, beta, PEG, short interest). Crypto, currencies and indexes are not companies, so they say so in `fundamentalsUnavailable` instead of returning empty objects.

```python
run = client.actor("highbrow_fame/yahoo-finance-quotes").call(run_input={
    "symbols": ["AAPL", "SAP.DE", "BTC-USD"],
    "includeFundamentals": True,
})
for q in client.dataset(run.default_dataset_id).iterate_items():
    if q.get("fundamentalsUnavailable"):
        print(q["symbol"], "-", q["fundamentalsUnavailable"])
        continue
    p, f = q.get("profile") or {}, q.get("financials") or {}
    print(q["symbol"], p.get("sector"), "/", p.get("industry"), "| margins:", f.get("profitMargins"),
          "| target:", f.get("targetMeanPrice"), "| rec:", f.get("recommendationKey"))
```

The inner keys of `financials` and `keyStatistics` follow Yahoo's own names, so print one record once with `json.dumps(q, indent=2)` to see exactly which fields your symbols carry before you build a screen on them.

## A small portfolio report

Put the holdings in a dict, fetch one run, and print value, day change and weight. This is the script to schedule after the close:

```python
HOLDINGS = {"AAPL": 25, "SAP.DE": 40, "SPY": 10, "BTC-USD": 0.15, "VOD.L": 500}

run = client.actor("highbrow_fame/yahoo-finance-quotes").call(
    run_input={"symbols": list(HOLDINGS)}
)
rows = []
for q in client.dataset(run.default_dataset_id).iterate_items():
    if q.get("price") is None:
        continue
    qty = HOLDINGS[q["symbol"]]
    rows.append({
        "symbol": q["symbol"], "currency": q["currency"], "qty": qty,
        "price": q["price"], "value": qty * q["price"],
        "day_change": qty * (q.get("change") or 0), "day_pct": q.get("changePercent") or 0,
    })

total = sum(r["value"] for r in rows)
print(f'{"symbol":<9}{"ccy":<5}{"qty":>8}{"price":>12}{"value":>14}{"day":>12}{"weight":>8}')
for r in sorted(rows, key=lambda r: -r["value"]):
    print(f'{r["symbol"]:<9}{r["currency"]:<5}{r["qty"]:>8}{r["price"]:>12,.2f}'
          f'{r["value"]:>14,.2f}{r["day_change"]:>+12,.2f}{r["value"]/total:>8.1%}')
print(f'total (mixed currencies): {total:,.2f}')
```

Values are in each symbol's own currency, so VOD.L is in GBp and SAP.DE in EUR; add the `EURUSD=X` and `GBPUSD=X` symbols to the same run and multiply if you want one base currency. Wrap the script in a cron entry for 22:30 UTC on weekdays, or save the input as a task in the Apify Console and schedule it there, then read the newest dataset from your code.

## The same call with curl

No Python at hand? The synchronous endpoint runs the Actor and returns the dataset in one request:

```bash
curl -sS -X POST "https://api.apify.com/v2/acts/highbrow_fame~yahoo-finance-quotes/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"symbols": ["AAPL", "BTC-USD"], "includeHistory": true, "historyRange": "1mo"}'
```

Add `&format=csv` to the URL for a spreadsheet-ready response.

## Cost per 1,000 symbols

The Actor charges $0.001 per symbol delivered on the free Apify plan, which is $1.00 per 1,000 symbols, falling to $0.70 per 1,000 on Gold and higher plans. The price is the same with or without history and company data, and unknown symbols are not charged. The seven-symbol quote run at the top costs $0.007; a 500-symbol watchlist refreshed every trading day costs $0.50 a day.

Try it with the prefilled input: https://apify.com/highbrow_fame/yahoo-finance-quotes
