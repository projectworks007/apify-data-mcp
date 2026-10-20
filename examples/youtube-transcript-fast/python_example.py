"""YouTube transcript API - Python example (apify-client).

Runs the "youtube-transcript-fast" Apify actor and prints the results.
Actor page: https://apify.com/highbrow_fame/youtube-transcript-fast

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
    python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {'videos': ['https://www.youtube.com/watch?v=aircAruvnKk'],
 'language': 'en',
 'includeSrt': False}

run = client.actor("highbrow_fame/youtube-transcript-fast").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print({k: item.get(k) for k in ['title', 'channel', 'language', 'text']})
