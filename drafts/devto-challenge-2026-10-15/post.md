---
title: "Local lead scorer: rank Google Maps leads with Gemma on your own machine"
published: false
tags: devchallenge, hf26challenge, opensource, ai
---

*Disclosure: written with AI assistance; I built the Apify Actor the tool can use.*

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle](https://dev.to/challenges/hacktoberfest-week2-2026-10-12)*

## What I Built

A small command-line tool that turns a pile of Google Maps business leads into a ranked call list for one specific offer, using an open-weight model that runs locally.

You tell it what you sell and to whom, for example `--offer "I sell online booking software to restaurants"`. It reads leads from my [Google Maps Email Extractor](https://apify.com/highbrow_fame/google-maps-email-extractor) Apify Actor, either by starting a run on your own Apify account or by loading a CSV/JSON export, and asks Gemma 3 (through Ollama) for a strict JSON verdict on every business: a 0-100 fit score, a reason in one line and the best contact channel. It writes a ranked CSV and a Markdown summary. If no model is running it falls back to a deterministic heuristic, so it always produces a ranking.

Who would pay for it? The people who already pay for lead scrapers: freelancers and small agencies doing cold outreach, and the solo founder who scraped 300 restaurants and now has to decide which 30 to actually email. Scraping is cheap; the expensive part is a human reading 300 rows. The scorer does the first pass for the price of electricity.

The whole thing is one Python file (300 lines, standard library only), MIT licensed, with a pytest suite and a fake sample dataset so it runs without any key.

## Demo

No hosted demo, by design: the point is that it runs on your machine. The fake sample ships in the repo, so this works on a laptop with no API key (a few minutes on a CPU, seconds on a GPU):

```bash
git clone https://github.com/projectworks007/apify-data-mcp
cd apify-data-mcp/examples/local-lead-scorer
ollama pull gemma3:4b
python lead_scorer.py --offer "I sell online booking software to restaurants" --input sample_leads.json --model gemma3:4b
cat out/summary.md
```

Output on the eight fake businesses in `sample_leads.json` (names and domains are invented, `example.com` addresses):

| # | Score | Business | Category | Channel | Why (model, verbatim) |
|---|---|---|---|---|---|
| 1 | 85 | Example Bistro Alpha (fake) | Italian restaurant | email | Italian restaurant with modern website and high engagement – ideal booking software fit. |
| 2 | 85 | Example Vegan Kitchen Theta (fake) | Vegan restaurant | email | Vegan restaurant with modern website and high email deliverability – ideal fit. |
| 3 | 85 | Example Pizzeria Beta (fake) | Pizza restaurant | website | Pizza restaurant, operational, good rating – a strong fit for online booking software. |
| 4 | 85 | Example Steakhouse Epsilon (fake) | Steak house | website | Steakhouse with online bookings is a good fit; website quality is a concern. |
| 5 | 85 | Example Café Delta (fake) | Cafe | visit | Small cafe, food & beverage, operational - ideal online booking target. |
| 6 | 35 | Example Hair Salon Eta (fake) | Hair salon | visit | Hair salons are not restaurants; no relevant contact channels available. |
| 7 | 25 | Example Dental Clinic Gamma (fake) | Dentist | website | Dental clinics are not restaurants; low contact data and no online presence. |
| 8 | 0 | Example Sushi Zeta (fake, closed) | Sushi restaurant | email | fallback: Business is closed |

That is `gemma3:4b` on a 4-core CPU, 125 seconds for the eight rows. The closed sushi place never reaches the model; the code gives it a 0. The 85s are a tie the CSV breaks with the heuristic column, where the two e-mail-verified restaurants come out on top.

The same run with `--no-model` gives the heuristic ranking, and `--query "restaurants in Budapest" --max-results 25` with an `APIFY_TOKEN` fetches real leads first.

## Code

{% github projectworks007/apify-data-mcp %}

The tool lives in [`examples/local-lead-scorer/`](https://github.com/projectworks007/apify-data-mcp/tree/main/examples/local-lead-scorer): `lead_scorer.py`, `sample_leads.json`, `tests/`, `README.md`, MIT `LICENSE`.

## How I Built It

**Open-weight model, local inference.** Scoring is done by Gemma 3 running in Ollama on localhost. The request uses Ollama's `/api/chat` with `format: json` and `temperature: 0`, so the model has to answer with one JSON object. The prompt gives the offer, the public facts about the business (category, industry, open/closed, rating, review count, website quality, tech stack, whether an e-mail, phone or contact form exists and the e-mail deliverability grade) and an explicit rubric: target customer and reachable is 80-100, unrelated category or closed is 0-19, and a business outside the target group never goes above 40. Small models follow bands much better than a vague "score the fit".

**Defensive parsing.** A 1B model will sometimes wrap its JSON in code fences, add chatter, or return `"score": "72.4"`. The parser strips fences, takes the outermost braces, clamps the score to 0-100, trims the reason to 20 words and validates the channel against a fixed list. If a reply is still unusable, that one lead gets the heuristic score and a `fallback:` marker in its reason column; the run never dies because of a bad token.

**Deterministic fallback.** The heuristic is boring on purpose: 30 base points, +20 for an e-mail (+10 if the Actor graded it `high`, -10 for `low`), +5 each for phone, contact form and website, +10 for 4.0+ stars with 50+ reviews, -10 for fewer than 5 reviews, +15 to +25 when words from your offer match the business category, 0 if the business is closed. It is always computed and kept in a `heuristic_score` column next to the model's score, so you can see when the two disagree.

**Lead source.** The Actor is mine; the tool calls it like any other user would: `POST /v2/acts/highbrow_fame~google-maps-email-extractor/runs` with `searchQueries` and `maxResults` (its real input fields, checked against the build's input schema), polls the run, reads the dataset, and follows the Actor's `autoExtend` pointer when a run restarts itself with a longer timeout. Raw leads are saved so you can re-score the same file against a different offer without a new run. Console exports load too; the flattened CSV keys the Apify export uses (`emailValidation/deliverability`, `techStack/0`) are rebuilt into nested fields.

**Testing.** 27 pytest tests, no network: parsing edge cases, the heuristic, a mocked Ollama server, a mocked Apify run sequence, the fallback paths and the CLI outputs. I also ran the real thing: Ollama 0.40.4 on a 4-core CPU box, `gemma3:1b` and `gemma3:4b`, on the fake sample. `gemma3:1b` took 45-48 seconds for the eight rows and gave every open business 85, dentist and hair salon included, even after I added the rubric and the `is_target` field. `gemma3:4b` took 125-162 seconds and put the restaurants at 85, the hair salon at 35 and the dentist at 25. So 4B is the default and the README says why.

What I did not do: no fine-tuning, no vector database, no agent framework. A ranked CSV did not need any of them.

## Why Does Open Innovation Matter?

Three concrete reasons for this build.

**The data has to stay on my machine.** Lead lists are business contact data. Sending every row to a hosted model API means a third processor, a data processing agreement, and a privacy section in my own terms that I would rather not write. With Ollama the rows never leave the laptop; the only network call is the scrape itself, which runs on the user's own Apify account. For a Hungarian freelancer under GDPR that is not a nicety, it is the difference between "I can use this" and "I need a lawyer first".

**The marginal cost is zero.** Scoring 1,000 leads with a hosted model is a few cents to a few dollars every time you change the offer. With a local 4B model it is a coffee break. That changes how you use the tool: you re-score the same file for three different offers and compare, instead of picking one and hoping.

**Small open models are enough for narrow jobs, and you can see why they fail.** A 1B model is visibly weaker than a 4B one on this task, and because the weights and the prompt are both open I could watch exactly where: the 1B model kept calling a dentist a restaurant whatever the rubric said, and the 4B model stopped doing so once I asked it for an explicit `is_target` field before the score. That feedback loop (change the prompt, re-run locally in two minutes, diff the CSV) is what a closed API with a rate limit and a bill makes slow. It also means a user can swap the model for whatever their hardware runs (`--model qwen3:4b`) without touching the code.

## My First User

None yet. The Actor the tool reads from has paying users on the Apify Store, but the scorer itself was written this week and has not been used by anyone but me. I am not going to invent one; if a user turns up after I publish, I will add it as an edit.

## Prize Categories

- **Best Use of Gemma**: Gemma 3 (1B and 4B) is the scorer, run locally through Ollama.

<!-- Thanks for participating! -->
