# Privacy

This plugin is a set of instructions (skills) and one connector reference. It has no server of its own and no code that runs on its own.

## What we store

Nothing. The author of this plugin (highbrow_fame) does not run a server for it, does not receive your prompts, your results or your Apify account details, and keeps no logs, analytics or copies of your data.

## Where data goes

When you ask Claude to use one of the tools, data moves between three parties only:

1. **You and Claude.** Your request, and the results Claude shows you, are handled under your own Claude plan and Anthropic's terms and privacy policy.
2. **Claude and Apify.** The connector (`https://mcp.apify.com`) is operated by Apify Technologies s.r.o. Claude sends the tool inputs (for example a search phrase, a place, a YouTube link or a brand domain) to Apify, signed in with your own Apify account through OAuth. Apify runs the tool and returns the results to Claude. Apify's handling of that data, including run history and datasets kept in your Apify account, is described in Apify's privacy policy: https://apify.com/privacy-policy
3. **Apify and the public websites the tools read.** The tools request public pages (Google Maps, job boards, property portals, classified-ad sites, YouTube, AI search engines) to collect the results you asked for.

If you give a tool an optional alert webhook URL (the listing tools accept `alertWebhookUrl`), Apify sends a short summary of new results to that URL. Only give a URL that you control.

## Personal data

- The tools are built to leave out private contact details of individuals (for example listing tools omit phone numbers and seller names). The Google Maps lead tool returns business e-mail addresses published on business websites; these can be personal data under laws such as GDPR. You are responsible for lawful use, including consent and opt-out rules for any outreach.
- Do not paste secrets (API keys, passwords, tokens) into a conversation to use these tools. None of them needs one.
- The plugin is not directed at children under 18.

## Retention

The plugin retains nothing. Results and run history live in your Apify account under Apify's retention rules, and you can delete them in the Apify Console. Listing tools in feed mode keep a list of already-seen listing keys in a key-value store in your Apify account for 60 days.

## Contact

Questions about this plugin: open an issue at https://github.com/projectworks007/apify-data-mcp/issues
