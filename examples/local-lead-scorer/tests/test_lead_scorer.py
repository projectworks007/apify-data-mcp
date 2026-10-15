"""Unit tests for the local lead scorer: parsing, heuristic scoring, model fallback, Apify flow, outputs."""
import csv
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lead_scorer as ls  # noqa: E402

SAMPLE = Path(__file__).resolve().parents[1] / "sample_leads.json"
OFFER = "I sell online booking software to restaurants"


def lead(**over):
    base = {"name": "Example Bistro (fake)", "category": "Italian restaurant", "industry": "Food & Beverage",
            "phone": "+36 1 555 0000", "website": "https://bistro.example.com", "primaryEmail": "hi@bistro.example.com",
            "emailValidation": {"deliverability": "high"}, "hasContactForm": True, "rating": 4.5, "reviewCount": 120,
            "businessStatus": "operational", "webQuality": "modern", "socialMedia": {}}
    base.update(over)
    return base


# ------------------------------------------------------------------ model output parsing
def test_parse_plain_json():
    out = ls.parse_model_json('{"score": 83, "reason": "Restaurant with verified email", "channel": "email"}')
    assert out == {"score": 83, "reason": "Restaurant with verified email", "channel": "email"}


def test_parse_fenced_and_chatty_output():
    text = 'Sure! ```json\n{"score": "72.4", "reason": "Dated site, good fit", "channel": "Contact Form"}\n``` done'
    out = ls.parse_model_json(text)
    assert out["score"] == 72 and out["channel"] == "contact_form"


def test_parse_clamps_score_and_trims_reason():
    out = ls.parse_model_json(json.dumps({"score": 250, "reason": " ".join(["w"] * 40), "channel": "fax"}))
    assert out["score"] == 100
    assert len(out["reason"].split()) == 20
    assert out["channel"] is None  # unknown channel -> caller falls back to the heuristic channel


def test_parse_caps_score_when_model_says_not_target():
    out = ls.parse_model_json('{"is_target": false, "score": 85, "reason": "nice dentist", "channel": "email"}')
    assert out["score"] == 40
    assert ls.parse_model_json('{"is_target": true, "score": 85, "reason": "x", "channel": "email"}')["score"] == 85


def test_model_channel_must_exist_on_the_lead(monkeypatch):
    def fake_http(method, url, body=None, token=None, timeout=120):
        if url.endswith("/api/tags"):
            return {"models": [{"name": "gemma3:4b"}]}
        return {"message": {"content": '{"is_target": true, "score": 70, "reason": "ok", "channel": "website"}'}}
    monkeypatch.setattr(ls, "_http", fake_http)
    [row] = ls.score_leads([lead(website="", primaryEmail="", emailValidation={})], OFFER, log=lambda *_: None)
    assert row["channel"] == "phone"  # no website on this lead, so the heuristic channel wins


@pytest.mark.parametrize("bad", ["", None, "not json", "{}", '{"score": "high"}', "[1,2]"])
def test_parse_rejects_garbage(bad):
    assert ls.parse_model_json(bad) is None


# ----------------------------------------------------------------------- heuristic scoring
def test_offer_keywords_strip_filler_and_plurals():
    assert ls.offer_keywords(OFFER) == ["booking", "online", "restaurant", "software"]


def test_heuristic_prefers_matching_reachable_business():
    good, _, channel = ls.heuristic_score(lead(), OFFER)
    other, _, _ = ls.heuristic_score(lead(category="Dentist", industry="Healthcare"), OFFER)
    no_email, _, ch2 = ls.heuristic_score(lead(primaryEmail="", emailValidation={}), OFFER)
    assert good > other and good > no_email and 0 <= good <= 100
    assert channel == "email" and ch2 == "phone"


def test_heuristic_closed_business_scores_zero():
    score, reason, _ = ls.heuristic_score(lead(businessStatus="permanently_closed"), OFFER)
    assert score == 0 and "closed" in reason


def test_heuristic_penalises_low_deliverability_and_picks_phone():
    low, _, channel = ls.heuristic_score(lead(emailValidation={"deliverability": "low"}), OFFER)
    high, _, _ = ls.heuristic_score(lead(), OFFER)
    assert low < high and channel == "phone"


def test_heuristic_is_deterministic_and_reason_short():
    a = ls.heuristic_score(lead(), OFFER)
    b = ls.heuristic_score(lead(), OFFER)
    assert a == b and len(a[1].split()) <= 20


# ------------------------------------------------------------------------------- loading
def test_load_csv_unflattens_apify_export(tmp_path):
    rows = [{"name": "Example Shop (fake)", "emailValidation/deliverability": "medium", "techStack/0": "WordPress",
             "techStack/1": "", "hasContactForm": "true", "socialMedia/facebook": "https://facebook.example.com/x"}]
    path = tmp_path / "export.csv"
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    [item] = ls.load_leads(path)
    assert item["emailValidation"] == {"deliverability": "medium"}
    assert item["techStack"] == ["WordPress"] and item["hasContactForm"] is True
    assert item["socialMedia"] == {"facebook": "https://facebook.example.com/x"}


def test_load_json_variants(tmp_path):
    assert len(ls.load_leads(SAMPLE)) == 8
    wrapped = tmp_path / "w.json"
    wrapped.write_text(json.dumps({"items": [lead()]}))
    assert ls.load_leads(wrapped)[0]["name"].startswith("Example")
    jsonl = tmp_path / "l.jsonl"
    jsonl.write_text(json.dumps(lead()) + "\n\n" + json.dumps(lead(name="Two")) + "\n")
    assert [x["name"] for x in ls.load_leads(jsonl)][1] == "Two"


# --------------------------------------------------------------------- model use / fallback
def test_fallback_when_ollama_is_unreachable(monkeypatch):
    monkeypatch.setattr(ls, "DEFAULT_OLLAMA", "http://127.0.0.1:9")  # nothing listens here
    log = []
    rows = ls.score_leads(ls.load_leads(SAMPLE), OFFER, url="http://127.0.0.1:9", log=log.append)
    assert all(r["model_score"] == "" for r in rows)
    assert any("not reachable" in line for line in log)
    assert [r["rank"] for r in rows] == list(range(1, 9))
    assert rows[-1]["businessStatus"] == "permanently_closed" and rows[-1]["score"] == 0


def test_mocked_model_response_drives_ranking(monkeypatch):
    """Simulate Ollama: /api/tags lists the model, /api/chat returns strict JSON that favours cafes."""
    def fake_http(method, url, body=None, token=None, timeout=120):
        if url.endswith("/api/tags"):
            return {"models": [{"name": "gemma3:4b"}]}
        assert url.endswith("/api/chat") and body["format"] == "json" and body["options"]["temperature"] == 0
        summary = json.loads(body["messages"][1]["content"].split("\n\n")[1].split("\n", 1)[1])
        score = 95 if "Cafe" in (summary["category"] or "") else 40
        return {"message": {"content": json.dumps({"score": score, "reason": "mocked verdict", "channel": "phone"})}}
    monkeypatch.setattr(ls, "_http", fake_http)
    leads = ls.load_leads(SAMPLE)
    rows = ls.score_leads(leads, "I sell espresso machines to cafes", log=lambda *_: None)
    assert rows[0]["category"] == "Cafe" and rows[0]["model_score"] == 95
    assert rows[0]["channel"] == "visit"  # the mock said "phone" but this cafe has no phone: data wins
    assert rows[0]["reason"] == "mocked verdict"
    assert rows[-1]["score"] == 0 and rows[-1]["model_score"] == ""  # closed business skips the model


def test_per_lead_model_failure_falls_back(monkeypatch):
    calls = {"n": 0}

    def fake_http(method, url, body=None, token=None, timeout=120):
        if url.endswith("/api/tags"):
            return {"models": [{"name": "gemma3:4b"}]}
        calls["n"] += 1
        return {"message": {"content": "I cannot answer that." if calls["n"] == 1 else '{"score": 60, "reason": "ok", "channel": "email"}'}}
    monkeypatch.setattr(ls, "_http", fake_http)
    rows = ls.score_leads([lead(name="A (fake)"), lead(name="B (fake)")], OFFER, log=lambda *_: None)
    by_name = {r["name"]: r for r in rows}
    assert by_name["A (fake)"]["model_score"] == "" and by_name["A (fake)"]["reason"].startswith("fallback:")
    assert by_name["B (fake)"]["model_score"] == 60


def test_prompt_contains_offer_and_no_raw_email():
    prompt = ls.build_prompt(OFFER, lead())
    assert OFFER in prompt and "hi@bistro.example.com" not in prompt and '"has_email": true' in prompt


# ------------------------------------------------------------------------------- Apify flow
def test_fetch_leads_from_apify_polls_and_reads_dataset(monkeypatch):
    seq = iter([
        {"data": {"id": "RUN00000000000001", "status": "RUNNING", "defaultDatasetId": "DS1"}},
        {"data": {"id": "RUN00000000000001", "status": "RUNNING", "defaultDatasetId": "DS1"}},
        {"data": {"id": "RUN00000000000001", "status": "SUCCEEDED", "defaultDatasetId": "DS1",
                  "statusMessage": "Finished: 2 leads"}},
        [lead(), lead(name="Second (fake)")],
    ])
    calls = []

    def fake_http(method, url, body=None, token=None, timeout=120):
        calls.append((method, url, body, token))
        return next(seq)
    monkeypatch.setattr(ls, "_http", fake_http)
    monkeypatch.setattr(ls.time, "sleep", lambda s: None)
    items = ls.fetch_leads_from_apify(["cafes in Budapest"], 10, "tok", "hu", log=lambda *_: None)
    assert len(items) == 2
    assert calls[0][0] == "POST" and calls[0][1].endswith(f"/acts/{ls.ACTOR}/runs")
    assert calls[0][2] == {"searchQueries": ["cafes in Budapest"], "maxResults": 10, "language": "hu"}
    assert all(c[3] == "tok" for c in calls) and "token=" not in calls[0][1]
    assert calls[-1][1].endswith("/datasets/DS1/items?clean=true")


def test_fetch_follows_autoextend_pointer(monkeypatch):
    seq = iter([
        {"data": {"id": "RUN00000000000001", "status": "SUCCEEDED", "defaultDatasetId": "DS1",
                  "statusMessage": "Timeout too short, restarted as run RUN00000000000002"}},
        [],
        {"data": {"id": "RUN00000000000002", "status": "SUCCEEDED", "defaultDatasetId": "DS2"}},
        [lead()],
    ])
    monkeypatch.setattr(ls, "_http", lambda *a, **k: next(seq))
    monkeypatch.setattr(ls.time, "sleep", lambda s: None)
    assert len(ls.fetch_leads_from_apify(["x"], 5, "tok", log=lambda *_: None)) == 1


def test_fetch_raises_on_failed_run(monkeypatch):
    monkeypatch.setattr(ls, "_http", lambda *a, **k: {"data": {"id": "RUN00000000000003", "status": "FAILED",
                                                                "defaultDatasetId": "DS", "statusMessage": "boom"}})
    with pytest.raises(RuntimeError, match="FAILED"):
        ls.fetch_leads_from_apify(["x"], 5, "tok", log=lambda *_: None)


# --------------------------------------------------------------------------------- outputs
def test_write_outputs_and_cli(tmp_path, capsys):
    rc = ls.main(["--offer", OFFER, "--input", str(SAMPLE), "--no-model", "--out", str(tmp_path), "--top", "3"])
    assert rc == 0
    rows = list(csv.DictReader((tmp_path / "leads_ranked.csv").open(encoding="utf-8")))
    assert [r["rank"] for r in rows] == [str(i) for i in range(1, 9)]
    assert list(rows[0]) == ls.COLUMNS and int(rows[0]["score"]) >= int(rows[1]["score"])
    md = (tmp_path / "summary.md").read_text(encoding="utf-8")
    assert md.startswith(f"# Lead ranking for: {OFFER}") and md.count("\n| ") == 1 + 3  # header + --top rows
    assert "heuristic only" in md and "Wrote" in capsys.readouterr().out


def test_cli_requires_token_for_query(monkeypatch):
    monkeypatch.delenv("APIFY_TOKEN", raising=False)
    with pytest.raises(SystemExit):
        ls.main(["--offer", OFFER, "--query", "cafes in Budapest"])
