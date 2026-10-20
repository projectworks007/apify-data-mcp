"""Magicbricks India property listings API - Python example (apify-client).

Runs the "magicbricks-properties" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/magicbricks-properties

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'places': ['Pune'],
 'transaction': 'sale',
 'propertyType': 'flat',
 'bedrooms': ['2', '3'],
 'maxListingsPerSearch': 50,
 'sortBy': 'newest'}

run = client.actor("highbrow_fame/magicbricks-properties").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['title', 'price', 'bedrooms', 'areaSqft', 'locality', 'url']})
