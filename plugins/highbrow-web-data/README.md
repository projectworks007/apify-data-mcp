# Web Data Tools by highbrow_fame

Live web data inside Claude. This plugin gives Claude four skills and ten data tools:

- **Business leads from Google Maps** with e-mail addresses, each graded for deliverability (MX, SPF, DMARC, catch-all).
- **AI-search brand visibility**: how ChatGPT, Perplexity, Gemini and Google AI Overviews mention and cite a brand.
- **YouTube transcripts** for videos, playlists and channels, with timestamps, SRT or WebVTT.
- **New job, property and marketplace listings**: StepStone and Naukri jobs, realtor.com, Rightmove and ImmoScout24 Austria properties, OfferUp and Craigslist ads, with an "only new since last run" feed mode and an optional alert webhook.

The tools are public Actors on [Apify](https://apify.com/highbrow_fame), served through Apify's hosted MCP server at `https://mcp.apify.com`. This plugin is independent and is not made or endorsed by Apify or Anthropic.

## What you need

An Apify account. A free account is enough to start, because Apify's free plan includes a monthly usage credit. Runs are billed by Apify to your account, per result (prices below). When you first use a tool, Claude opens an Apify sign-in page (OAuth); you never paste a token into the chat.

## Install

- **claude.ai or Cowork:** add the plugin from the directory (Customize > Plugins), then connect the plugin's `highbrow-web-data` connector and sign in to Apify.
- **Claude Code:** `/plugin directory`, or `claude --plugin-dir ./plugins/highbrow-web-data` from a clone of this repository.

## Try it

- "Find 25 dentists in Leeds with an e-mail address and tell me which e-mails are safe to send to."
- "How do ChatGPT and Perplexity answer 'best project management tool for small teams', and is example.com cited? Do a sample run first."
- "Get the transcript of this YouTube video and summarise it: <link>"
- "Show me new flats to rent in Manchester on Rightmove added in the last 3 days, under 1,500 a month."
- "Find Python developer jobs in Hamburg on StepStone posted this week."

## Tools and prices

Prices are Apify's pay-per-result prices on the free plan, per 1,000 results; paid Apify plans get lower prices on some tools. They can change; Apify shows the current price on each tool's page.

| Tool (Apify Actor) | Used for | Per 1,000 results |
|---|---|---|
| [google-maps-email-extractor](https://apify.com/highbrow_fame/google-maps-email-extractor) | Business leads and graded e-mails | $7.00, plus $0.015 per run start |
| [ai-search-visibility-tracker](https://apify.com/highbrow_fame/ai-search-visibility-tracker) | Brand mentions and citations in AI answers | $50 ($0.05 per answer record) |
| [youtube-transcript-fast](https://apify.com/highbrow_fame/youtube-transcript-fast) | YouTube transcripts | $1.00; videos without captions are free |
| [naukri-jobs](https://apify.com/highbrow_fame/naukri-jobs) | Jobs in India | $0.80 |
| [stepstone-jobs](https://apify.com/highbrow_fame/stepstone-jobs) | Jobs in Germany | $0.90 |
| [realtor-properties](https://apify.com/highbrow_fame/realtor-properties) | US homes for sale, sold, rent | $1.20 |
| [rightmove-properties](https://apify.com/highbrow_fame/rightmove-properties) | UK property | $0.80 |
| [immoscout24-at-properties](https://apify.com/highbrow_fame/immoscout24-at-properties) | Austrian property | $1.50 |
| [offerup-listings](https://apify.com/highbrow_fame/offerup-listings) | US OfferUp ads | $1.50 |
| [craigslist-listings](https://apify.com/highbrow_fame/craigslist-listings) | Craigslist ads (any city) | $1.20 |

The skills tell Claude to start with a small run and to say what a run will cost before it starts a large one.

## What the plugin does and does not do

- It sends your tool inputs (search phrases, places, links, brand domains) to Apify's server, using your Apify sign-in. Nothing else leaves your conversation. See [PRIVACY.md](PRIVACY.md).
- It stores nothing, has no server of its own, and bundles no code. The only executable part is the connector URL in `.mcp.json`.
- The tools read public web pages. Listing tools leave out phone numbers and the names of private individuals. The Google Maps tool returns business e-mails published on business websites, so follow the e-mail and data-protection law that applies to you.
- The tools are unofficial. They are not connected to Google, YouTube, StepStone, Naukri, realtor.com, Rightmove, ImmoScout24, OfferUp or Craigslist, and a site can change or block access at any time.
- Feed mode ("only new listings") compares with earlier runs, but a run only happens when someone starts it. To repeat it every day, create a Schedule in the Apify Console with the same input.

## Support

Issues and requests: https://github.com/projectworks007/apify-data-mcp/issues

## License

MIT, see [LICENSE](LICENSE).
