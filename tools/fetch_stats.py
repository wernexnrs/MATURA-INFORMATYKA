"""Pobiera statystyki odwiedzin z GoatCounter i zapisuje je do docs/assets/stats.json.

Uruchamiane codziennie przez GitHub Actions (.github/workflows/stats.yml).
Wymaga klucza API w zmiennej środowiskowej GOATCOUNTER_TOKEN
(GoatCounter -> nazwa użytkownika w menu -> API -> nowy klucz z prawem odczytu statystyk).

    GOATCOUNTER_TOKEN=... python tools/fetch_stats.py

Bez klucza skrypt kończy się bez zmian w pliku.
Na stronę trafiają tylko zbiorcze liczby - żadnych danych pozwalających zidentyfikować osoby.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

SITE = os.environ.get("GOATCOUNTER_SITE", "https://wernexnrs.goatcounter.com")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "assets", "stats.json")
START_ALL = "2026-11-14T00:00:00Z"   # początek zbierania statystyk (założenie licznika)
PAGES = ["browsers", "systems", "locations", "languages", "sizes", "toprefs"]


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:00:00Z")


def get(token, path, **params):
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}, doseq=True)
    url = "%s/api/v0/%s%s" % (SITE, path, ("?" + query) if query else "")
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token,
                                               "Content-Type": "application/json",
                                               "User-Agent": "matura-informatyka-stats"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                time.sleep(0.35)  # limit API: 4 zapytania na sekundę
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 + attempt * 2)
                continue
            raise


def main():
    token = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
    if not token:
        print("Brak GOATCOUNTER_TOKEN - pomijam pobieranie statystyk.")
        return 0
    now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    start90 = max(now - timedelta(days=90), datetime(2026, 11, 14, tzinfo=timezone.utc))
    out = {"generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "since": START_ALL[:10], "errors": []}

    def safe(name, fn):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 - zapisujemy błąd, strona pokaże resztę
            out["errors"].append("%s: %s" % (name, e))
            return None

    total = safe("total", lambda: get(token, "stats/total", start=START_ALL, end=iso(now)))
    if total:
        out["total"] = total.get("total", 0)
    days = safe("daily", lambda: get(token, "stats/total", start=iso(start90), end=iso(now)))
    if days:
        out["daily"] = [{"day": s.get("day"), "count": s.get("daily", 0)} for s in days.get("stats", []) if s.get("day")]

    # strony: wszystkie (stronicowanie przez exclude_paths)
    hits, seen = [], []
    for _ in range(10):
        res = safe("hits", lambda: get(token, "stats/hits", start=START_ALL, end=iso(now), limit=100,
                                      exclude_paths=seen or None))
        if not res:
            break
        for h in res.get("hits", []):
            if h.get("event"):
                continue
            hits.append({"path": h.get("path"), "title": h.get("title") or "", "count": h.get("count", 0)})
            seen.append(str(h.get("path_id")))
        if not res.get("more"):
            break
    out["pages"] = sorted(hits, key=lambda h: -h["count"])
    if "total" not in out:
        # zapas: suma z danych dziennych albo ze stron
        out["total"] = max(sum(d["count"] for d in out.get("daily", [])), sum(h["count"] for h in hits))

    for page in PAGES:
        res = safe(page, lambda p=page: get(token, "stats/" + p, start=START_ALL, end=iso(now), limit=20))
        if res:
            out[page] = [{"name": s.get("name") or "(nieznane)", "count": s.get("count", 0)} for s in res.get("stats", [])]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("Zapisano %s (stron: %d, błędów: %d)" % (OUT, len(out["pages"]), len(out["errors"])))
    for e in out["errors"]:
        print("  ! " + e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
