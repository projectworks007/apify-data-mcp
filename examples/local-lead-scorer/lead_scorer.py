#!/usr/bin/env python3
"""Local lead scorer: rank Google Maps business leads for your offer with an open-weight
model (Gemma via Ollama) that runs on your own machine. Standard library only, MIT.

  python lead_scorer.py --offer "I sell online booking software to restaurants" --input sample_leads.json
  APIFY_TOKEN=... python lead_scorer.py --offer "..." --query "restaurants in Budapest" --max-results 25

"""
from __future__ import annotations

import argparse, csv, json, os, re, sys, time, urllib.error, urllib.request  # noqa: E401
from pathlib import Path

ACTOR = "highbrow_fame~google-maps-email-extractor"
APIFY_API = "https://api.apify.com/v2"
DEFAULT_MODEL = os.environ.get("LEAD_SCORER_MODEL", "gemma3:4b")
DEFAULT_OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
CHANNELS = ("email", "phone", "contact_form", "website", "social", "visit")
TERMINAL = ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT")
CLOSED = ("permanently_closed", "closed_permanently", "closed", "temporarily_closed")
STOPWORDS = set("i we you sell sells selling offer offers provide to for and the a an of in on at with our my your "
                "small local business businesses company companies service services who that".split())
COLUMNS = ["rank", "score", "model_score", "heuristic_score", "channel", "reason", "name", "category", "industry",
           "address", "phone", "primaryEmail", "deliverability", "website", "webQuality", "rating", "reviewCount",
           "businessStatus", "googleMapsUrl"]
SYSTEM_PROMPT = ("You are a B2B sales assistant. You judge how well a local business fits a seller's offer. "
                 "Reply with one JSON object and nothing else.")


def _http(method: str, url: str, body: dict | None = None, token: str | None = None, timeout: int = 120):
    """Minimal JSON HTTP helper (standard library only)."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode() or "null")


def unflatten(row: dict) -> dict:
    """Undo Apify's CSV flattening: 'emailValidation/deliverability' -> nested dict, 'techStack/0' -> list."""
    out: dict = {}
    for key, value in row.items():
        parts, target = key.split("/"), out
        for part in parts[:-1]:
            target = target.setdefault(part, {})
        target[parts[-1]] = {"true": True, "false": False}.get(str(value).lower(), value)

    def fix(obj):
        if isinstance(obj, dict) and obj and all(k.isdigit() for k in obj):
            return [fix(obj[k]) for k in sorted(obj, key=int) if obj[k] != ""]
        return {k: fix(v) for k, v in obj.items()} if isinstance(obj, dict) else obj
    return fix(out)


def load_leads(path: str | Path) -> list[dict]:
    """Read an Actor export: JSON (list or {"items": [...]}), JSONL, or CSV with flattened keys."""
    path = Path(path)
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".csv":
        return [unflatten(r) for r in csv.DictReader(text.splitlines())]
    if path.suffix.lower() == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    return data["items"] if isinstance(data, dict) and "items" in data else list(data)


def fetch_leads_from_apify(queries: list[str], max_results: int, token: str, language: str = "en",
                           poll_seconds: int = 10, log=print) -> list[dict]:
    """Run the Google Maps Email Extractor on your Apify account and return its dataset items."""
    body = {"searchQueries": queries, "maxResults": max_results, "language": language}
    run = _http("POST", f"{APIFY_API}/acts/{ACTOR}/runs", body, token)["data"]
    log(f"Apify run {run['id']} started; expect ~70 s of startup plus 5-8 s per lead")
    seen: set[str] = set()
    while True:
        seen.add(run["id"])
        while run["status"] not in TERMINAL:
            time.sleep(poll_seconds)
            run = _http("GET", f"{APIFY_API}/actor-runs/{run['id']}", token=token)["data"]
        msg = run.get("statusMessage") or ""
        if run["status"] != "SUCCEEDED":
            raise RuntimeError(f"Apify run ended with status {run['status']}: {msg}")
        items = _http("GET", f"{APIFY_API}/datasets/{run['defaultDatasetId']}/items?clean=true", token=token)
        pointer = [m for m in re.findall(r"\b[A-Za-z0-9]{17}\b", msg) if m not in seen]
        if items or not pointer:
            log(f"Apify run finished with {len(items)} leads. {msg}".strip())
            return items
        log(f"Run restarted itself with a longer timeout; following run {pointer[0]}")
        run = _http("GET", f"{APIFY_API}/actor-runs/{pointer[0]}", token=token)["data"]


def _num(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def deliverability(lead: dict) -> str:
    val = lead.get("emailValidation")
    return str((val or {}).get("deliverability") or "") if isinstance(val, dict) else str(val or "")


def is_closed(lead: dict) -> bool:
    return str(lead.get("businessStatus") or "").lower().replace(" ", "_") in CLOSED


def offer_keywords(offer: str) -> list[str]:
    words = [w for w in re.findall(r"[a-zà-ž0-9]+", offer.lower()) if len(w) > 2 and w not in STOPWORDS]
    return sorted({w[:-1] if w.endswith("s") and len(w) > 4 else w for w in words})


def matched_keywords(lead: dict, offer: str) -> list[str]:
    haystack = " ".join(str(lead.get(k) or "") for k in ("category", "industry", "cuisine", "name")).lower()
    return [w for w in offer_keywords(offer) if w in haystack]


def has_channel(lead: dict, channel: str) -> bool:
    socials = lead.get("socialMedia") if isinstance(lead.get("socialMedia"), dict) else {}
    return bool({"email": lead.get("primaryEmail"), "phone": lead.get("phone"), "website": lead.get("website"),
                 "contact_form": lead.get("hasContactForm"), "social": any(socials.values()), "visit": True}.get(channel))


def best_channel(lead: dict) -> str:
    if lead.get("primaryEmail") and deliverability(lead) != "low":
        return "email"
    return next(c for c in ("phone", "contact_form", "email", "website", "social", "visit") if has_channel(lead, c))


def limit_words(text, n: int = 20) -> str:
    return " ".join(str(text).split()[:n])


def heuristic_score(lead: dict, offer: str) -> tuple[int, str, str]:
    """Deterministic 0-100 score used when no model is available (and kept as a second opinion)."""
    if is_closed(lead):
        return 0, "Business is closed", best_channel(lead)
    score, why, deliv = 30, [], deliverability(lead)
    if lead.get("primaryEmail"):
        score += 20 + {"high": 10, "medium": 3, "low": -10}.get(deliv, 0)
        why.append(f"email {deliv or 'ungraded'}")
    else:
        why.append("no email")
    score += 5 * bool(lead.get("phone")) + 5 * bool(lead.get("hasContactForm")) + 5 * bool(lead.get("website"))
    rating, reviews = _num(lead.get("rating")), _num(lead.get("reviewCount"))
    if reviews >= 50 and rating >= 4.0:
        score += 10
        why.append(f"{rating:g} stars, {int(reviews)} reviews")
    elif reviews < 5:
        score -= 10
        why.append("few reviews")
    hits = matched_keywords(lead, offer)
    score += min(25, 15 + 5 * (len(hits) - 1)) if hits else 0
    why.append("matches " + "/".join(hits[:3]) if hits else "category does not match offer")
    return max(0, min(100, score)), limit_words("; ".join(why)), best_channel(lead)


def lead_summary(lead: dict) -> dict:
    """The public business facts the model sees (it never needs the raw e-mail address to score)."""
    socials = lead.get("socialMedia") if isinstance(lead.get("socialMedia"), dict) else {}
    return {"name": lead.get("name"), "category": lead.get("category"), "industry": lead.get("industry"),
            "address": lead.get("address"), "status": lead.get("businessStatus"), "rating": lead.get("rating"),
            "reviews": lead.get("reviewCount"), "has_website": bool(lead.get("website")),
            "website_quality": lead.get("webQuality"), "tech_stack": lead.get("techStack"),
            "has_email": bool(lead.get("primaryEmail")), "email_deliverability": deliverability(lead) or None,
            "has_phone": bool(lead.get("phone")), "has_contact_form": bool(lead.get("hasContactForm")),
            "social_profiles": sorted(k for k, v in socials.items() if v)}


def build_prompt(offer: str, lead: dict) -> str:
    return (f"Offer: {offer}\n\nBusiness (public Google Maps data):\n{json.dumps(lead_summary(lead), ensure_ascii=False)}"
            "\n\nScore how well this business fits the offer as a customer, 0-100:\n"
            "80-100: exactly the offer's target customer, open, with a working contact channel.\n"
            "50-79: target customer, but weak contact data or weak reputation.\n"
            "20-49: only loosely related to the target customer.\n0-19: unrelated category, or closed.\n"
            "Be strict: a business outside the target customer group never scores above 40.\n"
            "channel: email if has_email and deliverability is not low; else phone; else contact_form; else website.\n"
            'Return exactly: {"is_target": <true only if the business is the kind of customer the offer names>, '
            '"score": <integer 0-100>, "reason": "<at most 15 words>", '
            '"channel": "<one of email|phone|contact_form|website|social|visit>"}')


def parse_model_json(text) -> dict | None:
    """Parse the model's reply into {"score", "reason", "channel"}; None if unusable."""
    cleaned = re.sub(r"```(?:json)?", "", str(text or "")).strip()
    start, end = cleaned.find("{"), cleaned.rfind("}")
    try:
        data = json.loads(cleaned[start:end + 1]) if 0 <= start < end else None
        score = int(round(float(data["score"])))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None
    if str(data.get("is_target", True)).strip().lower() in ("false", "no", "0"):
        score = min(score, 40)  # the rubric cap for businesses outside the target group, enforced in code
    channel = str(data.get("channel") or "").strip().lower().replace(" ", "_").replace("-", "_")
    return {"score": max(0, min(100, score)), "reason": limit_words(data.get("reason") or "No reason given"),
            "channel": channel if channel in CHANNELS else None}


def ollama_ready(url: str, model: str, log=print) -> bool:
    try:
        names = [m.get("name") for m in _http("GET", f"{url}/api/tags", timeout=10).get("models", [])]
    except (urllib.error.URLError, OSError, ValueError) as exc:
        log(f"Ollama not reachable at {url} ({exc}); using the heuristic scorer")
        return False
    if model not in names and f"{model}:latest" not in names:
        log(f"Model {model!r} not found in Ollama (have: {', '.join(names) or 'none'}); run: ollama pull {model}")
        return False
    return True


def ask_model(offer: str, lead: dict, model: str, url: str, timeout: int = 120) -> dict | None:
    body = {"model": model, "stream": False, "format": "json", "options": {"temperature": 0, "num_predict": 160},
            "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                         {"role": "user", "content": build_prompt(offer, lead)}]}
    try:
        reply = _http("POST", f"{url}/api/chat", body, timeout=timeout)
    except (urllib.error.URLError, OSError, ValueError):
        return None
    return parse_model_json((reply.get("message") or {}).get("content", ""))


def score_leads(leads: list[dict], offer: str, model: str = DEFAULT_MODEL, url: str = DEFAULT_OLLAMA,
                use_model: bool = True, timeout: int = 120, log=print) -> list[dict]:
    """Score every lead; model first, deterministic heuristic as fallback. Returns rows sorted best first."""
    use_model = use_model and ollama_ready(url, model, log)
    rows = []
    for i, lead in enumerate(leads, 1):
        h_score, h_reason, h_channel = heuristic_score(lead, offer)
        verdict = ask_model(offer, lead, model, url, timeout) if use_model and not is_closed(lead) else None
        if verdict is None:
            score, reason, channel, model_score = h_score, ("fallback: " if use_model else "") + h_reason, h_channel, ""
        else:
            score, reason, model_score = verdict["score"], verdict["reason"], verdict["score"]
            channel = verdict["channel"] if verdict["channel"] and has_channel(lead, verdict["channel"]) else h_channel
        rows.append({**{c: lead.get(c, "") for c in COLUMNS}, "score": score, "model_score": model_score,
                     "heuristic_score": h_score, "channel": channel, "reason": reason,
                     "deliverability": deliverability(lead)})
        log(f"[{i}/{len(leads)}] {score:>3}  {lead.get('name')}  ({reason})")
    rows.sort(key=lambda r: (-int(r["score"]), -int(r["heuristic_score"]), str(r["name"])))
    for rank, row in enumerate(rows, 1):
        row["rank"] = rank
    return rows


def write_outputs(rows: list[dict], out_dir, offer: str, model_label: str, top: int = 10) -> tuple[Path, Path]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    csv_path, md_path = out / "leads_ranked.csv", out / "summary.md"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    by_model = sum(1 for r in rows if r["model_score"] != "")
    lines = [f"# Lead ranking for: {offer}", "",
             f"Scored {len(rows)} leads: {by_model} by the model ({model_label}), "
             f"{len(rows) - by_model} by the deterministic heuristic.", "",
             "| # | Score | Business | Category | Channel | Contact | Why |", "|---|---|---|---|---|---|---|"]
    for r in rows[:top]:
        contact = r["primaryEmail"] or r["phone"] or r["website"] or "-"
        lines.append(f"| {r['rank']} | {r['score']} | {r['name']} | {r['category']} | {r['channel']} | {contact} | "
                     f"{str(r['reason']).replace('|', '/')} |")
    lines += ["", f"Full table with every column: `{csv_path.name}`.", ""]
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return csv_path, md_path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--offer", required=True, help='what you sell and to whom, e.g. "I sell POS systems to cafes"')
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--input", help="CSV, JSON or JSONL export of the Actor (works offline, no key needed)")
    src.add_argument("--query", action="append", help="Google Maps search such as 'dentists in London' "
                     "(repeatable); runs the Actor on your Apify account, needs APIFY_TOKEN")
    p.add_argument("--max-results", type=int, default=25, help="leads per query to fetch from Apify (default 25)")
    p.add_argument("--language", default="en", help="Google Maps language code for the Actor (default en)")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Ollama model (default {DEFAULT_MODEL})")
    p.add_argument("--ollama-url", default=DEFAULT_OLLAMA, help=f"Ollama server (default {DEFAULT_OLLAMA})")
    p.add_argument("--no-model", action="store_true", help="skip the model and use only the heuristic")
    p.add_argument("--timeout", type=int, default=120, help="seconds allowed per model call (default 120)")
    p.add_argument("--out", default="out", help="output folder (default ./out)")
    p.add_argument("--top", type=int, default=10, help="rows in the Markdown summary (default 10)")
    a = p.parse_args(argv)
    if a.query:
        token = os.environ.get("APIFY_TOKEN") or p.error("--query runs the Apify Actor and needs APIFY_TOKEN set")
        leads = fetch_leads_from_apify(a.query, a.max_results, token, a.language)
        Path(a.out).mkdir(parents=True, exist_ok=True)
        (Path(a.out) / "leads_raw.json").write_text(json.dumps(leads, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Raw leads saved to {Path(a.out) / 'leads_raw.json'}; re-score later with --input at no extra charge")
    else:
        leads = load_leads(a.input)
    if not leads:
        return print("No leads to score.") or 1
    rows = score_leads(leads, a.offer, a.model, a.ollama_url, not a.no_model, a.timeout)
    csv_path, md_path = write_outputs(rows, a.out, a.offer, "none, heuristic only" if a.no_model else a.model, a.top)
    print(f"\nWrote {csv_path} and {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
