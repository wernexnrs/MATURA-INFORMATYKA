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


def gh_get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "matura-informatyka-stats"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=headers), timeout=60) as r:
        return json.load(r)


BOT_COMMITS = ("Przebuduj stronę", "Aktualizacja statystyk", "Merge ")


def github_stats():
    """Publiczne dane społeczności z GitHuba (bez żadnych danych prywatnych)."""
    repo = os.environ.get("GITHUB_REPOSITORY", "wernexnrs/MATURA-INFORMATYKA")
    r = gh_get("/repos/" + repo)
    contributors = [c for c in gh_get("/repos/%s/contributors?per_page=40" % repo)
                    if c.get("type") == "User" and not c.get("login", "").endswith("[bot]")]
    commits = []
    for c in gh_get("/repos/%s/commits?per_page=40" % repo):
        msg = (c.get("commit", {}).get("message") or "").splitlines()[0] if c.get("commit", {}).get("message") else ""
        if msg.startswith(BOT_COMMITS) or (c.get("author") or {}).get("type") == "Bot":
            continue
        commits.append({"message": msg[:120], "date": c["commit"]["author"]["date"],
                        "author": (c.get("author") or {}).get("login") or c["commit"]["author"]["name"],
                        "url": c.get("html_url")})
        if len(commits) == 8:
            break
    count = lambda q: gh_get("/search/issues?q=" + urllib.parse.quote("repo:%s %s" % (repo, q)) + "&per_page=1").get("total_count", 0)
    return {"stars": r.get("stargazers_count", 0), "forks": r.get("forks_count", 0),
            "watchers": r.get("subscribers_count", 0), "open_issues": count("is:issue is:open"),
            "closed_issues": count("is:issue is:closed"), "merged_prs": count("is:pr is:merged"),
            "contributors": [{"login": c["login"], "avatar": c.get("avatar_url"), "url": c.get("html_url"),
                              "contributions": c.get("contributions", 0)} for c in contributors],
            "commits": commits, "url": r.get("html_url")}


def main():
    token = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
    if not token:
        # bez klucza GoatCounter aktualizujemy tylko dane z GitHuba, zachowując zebrane odwiedziny
        data = {}
        if os.path.exists(OUT):
            with open(OUT, encoding="utf-8") as f:
                data = json.load(f)
        try:
            data["github"] = github_stats()
        except Exception as e:  # noqa: BLE001
            print("Nie udało się pobrać danych z GitHuba: %s" % e)
            return 0
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print("Brak GOATCOUNTER_TOKEN - zaktualizowano tylko dane z GitHuba.")
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
        # suma odwiedzin w poszczególnych godzinach doby (strefa czasowa jak w ustawieniach GoatCounter)
        hours = [0] * 24
        for st in days.get("stats", []):
            for h, v in enumerate((st.get("hourly") or [])[:24]):
                hours[h] += v or 0
        out["hourly"] = hours

    # strony: wszystkie (stronicowanie przez exclude_paths)
    hits, events, seen = [], [], []
    for _ in range(10):
        res = safe("hits", lambda: get(token, "stats/hits", start=START_ALL, end=iso(now), limit=100,
                                      exclude_paths=seen or None))
        if not res:
            break
        for h in res.get("hits", []):
            seen.append(str(h.get("path_id")))
            item = {"path": h.get("path"), "title": h.get("title") or "", "count": h.get("count", 0)}
            (events if h.get("event") else hits).append(item)
        if not res.get("more"):
            break
    out["pages"] = sorted(hits, key=lambda h: -h["count"])
    # zdarzenia z app.js: jezyk/<x>, kopiuj/<x>, szukaj/<fraza>
    out["events"] = sorted(events, key=lambda h: -h["count"])
    week = safe("week", lambda: get(token, "stats/hits", start=iso(now - timedelta(days=7)), end=iso(now), limit=50))
    if week:
        out["pages_week"] = [{"path": h.get("path"), "title": h.get("title") or "", "count": h.get("count", 0)}
                             for h in week.get("hits", []) if not h.get("event")]
    if "total" not in out:
        # zapas: suma z danych dziennych albo ze stron
        out["total"] = max(sum(d["count"] for d in out.get("daily", [])), sum(h["count"] for h in hits))

    for page in PAGES:
        res = safe(page, lambda p=page: get(token, "stats/" + p, start=START_ALL, end=iso(now), limit=20))
        if res:
            out[page] = [{"name": s.get("name") or "(nieznane)", "count": s.get("count", 0)} for s in res.get("stats", [])]

    gh = safe("github", github_stats)
    if gh:
        out["github"] = gh

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("Zapisano %s (stron: %d, błędów: %d)" % (OUT, len(out["pages"]), len(out["errors"])))
    for e in out["errors"]:
        print("  ! " + e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
