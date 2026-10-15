# Local lead scorer

Rank Google Maps business leads for *your* offer with an open-weight model (Gemma 3 via [Ollama](https://ollama.com)) that runs on your own machine. One Python file, standard library only, MIT.

You tell it what you sell and to whom ("I sell online booking software to restaurants"). It reads leads from the [Google Maps Email Extractor](https://apify.com/highbrow_fame/google-maps-email-extractor) Apify Actor (live run, or a CSV/JSON export) and, for every business, asks a local Gemma model for a strict JSON verdict: a 0-100 fit score, a one-line reason and the best contact channel. When no model is running it falls back to a deterministic heuristic, so the tool always produces a ranking. Output: a ranked CSV and a Markdown summary you can paste into a note or a CRM.

## Quick start (no key, no model needed)

```bash
cd examples/local-lead-scorer
python lead_scorer.py --offer "I sell online booking software to restaurants" --input sample_leads.json --no-model
cat out/summary.md
```

`sample_leads.json` contains eight **fake** businesses (example.com domains, fictional addresses) so the pipeline runs anywhere.

## With a local open-weight model

```bash
curl -fsSL https://ollama.com/install.sh | sh     # or download from ollama.com
ollama pull gemma3:4b                            # ~3.3 GB, the default; gemma3:1b (~0.8 GB) runs faster but judges badly
python lead_scorer.py --offer "I sell online booking software to restaurants" --input sample_leads.json
```

The scorer talks to Ollama at `http://localhost:11434` (`--ollama-url` or `OLLAMA_HOST` to change), uses `temperature 0` and Ollama's JSON mode, and parses the reply defensively: code fences, chatter and out-of-range values are tolerated; an unusable reply makes that one lead fall back to the heuristic, marked `fallback:` in the reason column. Any model Ollama serves works (`--model gemma3:1b`, `--model qwen3:4b`, ...); `LEAD_SCORER_MODEL` sets the default.

## With live leads from Google Maps

```bash
export APIFY_TOKEN=...   # https://console.apify.com/account/integrations
python lead_scorer.py --offer "I sell POS systems to cafes" --query "cafes in Budapest" --max-results 25 --model gemma3:4b
```

This starts the Actor on your Apify account with `searchQueries` and `maxResults` (the Actor's real input fields; `--language` sets its `language`), polls the run, reads the dataset, saves the raw rows to `out/leads_raw.json` and scores them. Re-score the saved file later with `--input out/leads_raw.json` and a different offer at no extra charge. Exports made in the Apify Console (CSV, JSON, JSONL) load the same way; flattened CSV columns such as `emailValidation/deliverability` are rebuilt into nested fields.

## Output

`out/leads_ranked.csv` has one row per lead, best first: `rank, score, model_score, heuristic_score, channel, reason, name, category, industry, address, phone, primaryEmail, deliverability, website, webQuality, rating, reviewCount, businessStatus, googleMapsUrl`. `out/summary.md` shows the top rows (`--top`). Sample heuristic output for the fake data:

| # | Score | Business | Category | Channel | Why |
|---|---|---|---|---|---|
| 1 | 100 | Example Bistro Alpha (fake) | Italian restaurant | email | email high; 4.6 stars, 312 reviews; matches restaurant |
| 2 | 90 | Example Vegan Kitchen Theta (fake) | Vegan restaurant | email | email high; matches restaurant |
| 3 | 73 | Example Dental Clinic Gamma (fake) | Dentist | email | email medium; 4.9 stars, 540 reviews; category does not match offer |
| 4 | 70 | Example Pizzeria Beta (fake) | Pizza restaurant | phone | no email; 4.1 stars, 87 reviews; matches restaurant |
| 8 | 0 | Example Sushi Zeta (fake, closed) | Sushi restaurant | email | Business is closed |

## How scoring works

- **Model** (default): the prompt carries the offer plus the public facts about the business (category, industry, status, rating, reviews, website quality, tech stack, whether an e-mail/phone/contact form exists and the e-mail deliverability grade). It does not need the raw e-mail address. The model must answer `{"is_target": true/false, "score": 0-100, "reason": "...", "channel": "email|phone|contact_form|website|social|visit"}` against an explicit rubric (target customer and reachable: 80-100; unrelated category or closed: 0-19). Two rules are enforced in code because small models bend them: a lead the model itself marks `is_target: false` is capped at 40, and a channel the lead does not have (no website, say) is replaced by the data-driven channel.
- **Heuristic** (fallback, and always kept in `heuristic_score` as a second opinion): 30 base points, +20 for an e-mail (+10 high deliverability, -10 low), +5 each for phone, contact form, website, +10 for 4.0+ stars with 50+ reviews, -10 for under 5 reviews, +15 to +25 when the offer's keywords match the business category/industry/name, 0 for a closed business. Deterministic, so two runs on the same file give the same ranking.
- Closed businesses skip the model and score 0. Ties are broken by the heuristic score, then by name.

## Cost

- The model runs locally and is free; a 1B/4B Gemma runs on a laptop CPU (the fake sample takes about 2.5 minutes with `gemma3:4b` on four CPU cores and under a minute with `gemma3:1b`; a GPU is much faster).
- `--query` runs the Actor on **your** Apify account. Its pricing, read from the Actor's `pricingInfos` on the Apify API at the time of writing: pay-per-event, **$0.007 per delivered lead on the Free plan** ($0.006 Bronze, $0.005 Silver, $0.0045 Gold and above) plus a **$0.015 per GB run-start fee** ($0.06 at the 4 GB default). Example from the Actor's own schema: 100 leads on the Free plan cost $0.76. Apify's free plan includes a monthly usage credit. Check the [Actor page](https://apify.com/highbrow_fame/google-maps-email-extractor) for the current price before a large run.
- Loading an export with `--input` costs nothing.

## Privacy

Lead data never leaves your machine except for the Apify run itself (when you use `--query`, the search runs on Apify's servers and the results are stored in your Apify account's dataset). Scoring happens locally in Ollama; nothing is sent to a hosted model API. The data is public business information from Google Maps (B2B). Processing it, and any outreach, is your responsibility under GDPR and your local rules: have a lawful basis, honour opt-outs, and do not use it for consumer marketing.

## Tests

```bash
pip install -r requirements.txt   # pytest only; the tool itself has no dependencies
python -m pytest -q tests
```

The tests cover model-output parsing (fenced, chatty, out-of-range, garbage), the heuristic, the fallback when Ollama is unreachable or a single reply is unusable, a mocked Ollama server, the Apify run/poll/dataset flow (mocked, including the Actor's `autoExtend` follow-up run), CSV unflattening and the CLI outputs. No network is needed.

## Limits

- `gemma3:1b` is fast (about 45 s for the sample on four CPU cores) but loose: in testing it gave nearly every business the same score regardless of the rubric. `gemma3:4b` (about 2.5 min for the sample on the same CPU) separates target from non-target businesses and is the default. Keep `heuristic_score` in view when you use a tiny model.
- Scores are a triage aid for a human, not a decision about a person.
- Built in the Hacktoberfest 2026 DEV challenge week (12-18 October 2026). Commits after the deadline, if any, are listed here: none yet.

## License

MIT, see `LICENSE`.
