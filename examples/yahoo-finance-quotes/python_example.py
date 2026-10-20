"""Yahoo Finance quotes API - Python example (apify-client).

Runs the "yahoo-finance-quotes" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/yahoo-finance-quotes

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'symbols': ['AAPL', 'MSFT', 'BTC-USD'],
 'includeFundamentals': False,
 'includeHistory': False}

run = client.actor("highbrow_fame/yahoo-finance-quotes").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['symbol', 'name', 'price', 'changePercent', 'currency', 'marketCap']})
