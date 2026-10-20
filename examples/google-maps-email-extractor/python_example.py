"""Google Maps leads with emails - Python example (apify-client).

Runs the "google-maps-email-extractor" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/google-maps-email-extractor

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'searchQueries': ['dentists in Vienna'],
 'maxResults': 25,
 'scrapeEmails': True,
 'validateEmails': True,
 'language': 'en'}

run = client.actor("highbrow_fame/google-maps-email-extractor").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['name', 'category', 'phone', 'website', 'primaryEmail', 'leadScore']})
