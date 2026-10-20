"""AI search visibility tracking - Python example (apify-client).

Runs the "ai-search-visibility-tracker" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/ai-search-visibility-tracker

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'brand': 'example.com',
 'queries': ['best CRM for small business', 'HubSpot alternatives'],
 'competitorDomains': ['competitor-one.com'],
 'engines': ['perplexity-agent'],
 'sampleRun': True}

run = client.actor("highbrow_fame/ai-search-visibility-tracker").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['query', 'engine', 'brandCited', 'competitorsCited', 'citationShare']})
