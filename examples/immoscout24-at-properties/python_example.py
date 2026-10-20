"""ImmoScout24 Austria property listings API - Python example (apify-client).

Runs the "immoscout24-at-properties" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/immoscout24-at-properties

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'locations': ['Wien'],
 'transaction': 'rent',
 'propertyType': 'flat',
 'maxListingsPerSearch': 50,
 'sortBy': 'newest'}

run = client.actor("highbrow_fame/immoscout24-at-properties").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['title', 'price', 'areaSqm', 'rooms', 'town', 'url']})
