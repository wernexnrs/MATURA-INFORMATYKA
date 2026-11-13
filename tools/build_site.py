"""Generator strony GitHub Pages dla repozytorium MATURA-INFORMATYKA.

Czyta pliki Markdown z folderu `dzialy/` i tworzy statyczną stronę w `docs/`.
Nie wymaga żadnych dodatkowych bibliotek - wystarczy Python 3.8+.

Użycie (z głównego folderu repozytorium):
    python tools/build_site.py
"""

import html
import json
import os
import posixpath
import re
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
SITE_URL = "https://wernexnrs.github.io/MATURA-INFORMATYKA/"
REPO_URL = "https://github.com/wernexnrs/MATURA-INFORMATYKA"
SITE_NAME = "Matura z informatyki"

# Strony główne: plik źródłowy -> (plik wyjściowy, tytuł, krótka nazwa w menu, rodzaj, opis)
MAIN_PAGES = [
    ("dzialy/algorytmy_wymagania.md", "algorytmy.html", "Algorytmy z wymagań CKE", "Algorytmy CKE", "algo",
     "Wszystkie algorytmy z wymagań egzaminacyjnych CKE z informatyki w Pythonie, z pseudokodem: "
     "systemy liczbowe, liczby pierwsze, NWD, sortowania, wyszukiwanie binarne, Horner, szyfry i geometria."),
    ("dzialy/dodatkowe_algorytmy.md", "dodatkowe.html", "Dodatkowe algorytmy", "Dodatkowe", "algo",
     "Dodatkowe algorytmy przydatne na maturze z informatyki: średnie, mediana, moda, silnia, symbol Newtona, "
     "algorytmy tekstowe (KMP, Boyer-Moore, Karp-Rabin, Manacher) i geometria w Pythonie."),
    ("dzialy/zadania_arkusze.md", "arkusze.html", "Rozwiązania arkuszy maturalnych", "Arkusze", "index",
     "Rozwiązania zadań z arkuszy maturalnych z informatyki (CKE) w Pythonie - matura rozszerzona, "
     "podstawowa, próbna i zbiór zadań CKE, z odpowiedziami."),
    ("dzialy/funkcje_wbudowane.md", "funkcje.html", "Najważniejsze funkcje wbudowane Pythona", "Funkcje", "doc",
     "Najważniejsze funkcje wbudowane Pythona przydatne na maturze z informatyki."),
    ("dzialy/metody.md", "metody.html", "Metody napisów, list, słowników i zbiorów", "Metody", "doc",
     "Metody napisów, list, słowników i zbiorów w Pythonie - ściąga na maturę z informatyki."),
    ("dzialy/biblioteki.md", "biblioteki.html", "Przydatne moduły Pythona", "Moduły", "doc",
     "Przydatne moduły Pythona na maturę: collections, math, statistics, re, fractions, itertools."),
    ("dzialy/przydatne_linki.md", "linki.html", "Przydatne linki", "Linki", "doc",
     "Sprawdzone materiały do nauki do matury z informatyki: Python, algorytmy, Excel, Access, C++."),
]

BADGES = {
    "py": "Python", "c++": "C++", "java": "Java", "excel": "Excel", "access": "Access",
}
NEGATIVE_BADGES = {"nopy": "py", "notpy": "py"}

GH_BLOB = re.compile(r"https?://github\.com/wernexnrs(?:123)?/MATURA-INFORMATYKA/(?:blob|tree)/master/(.+)")
GH_RAW = re.compile(r"https?://raw\.githubusercontent\.com/wernexnrs(?:123)?/MATURA-INFORMATYKA/master/(.+)")


# --------------------------------------------------------------------------- pomocnicze

def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").replace("\t", "    ")


def write(out, text):
    path = os.path.join(DOCS, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def slugify(text):
    text = text.lower()
    repl = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
    text = "".join(repl.get(c, c) for c in text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "sekcja"


def strip_tags(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def rel(from_out, to_out):
    """Ścieżka względna z jednej strony wyjściowej do innej."""
    base = posixpath.dirname(from_out)
    return posixpath.relpath(to_out, base or ".")


def exam_out(src):
    """dzialy/zadania_arkusze/... lub dzialy/zadania_zbior/... -> plik html."""
    name = posixpath.splitext(posixpath.basename(src))[0]
    if src.startswith("dzialy/zadania_zbior/"):
        return "zbior/zadanie-" + slugify(name) + ".html"
    return "arkusze/" + slugify(name) + ".html"


def exam_title(src, text):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if m and strip_tags(m.group(1)).strip():
        return " ".join(strip_tags(m.group(1)).split())
    name = posixpath.splitext(posixpath.basename(src))[0]
    if src.startswith("dzialy/zadania_zbior/"):
        return "Zbiór zadań CKE - zadanie " + name
    parts = name.replace("kwiecen", "kwiecień").replace("grudzien", "grudzień").split("_")
    title = "Matura " + " ".join(parts)
    title = title.replace(" pr", " (próbna)").replace(" stare", " (stara formuła)")
    return title.replace(" podstawa", " - poziom podstawowy")


# --------------------------------------------------------------------------- Markdown -> HTML

class Ctx:
    """Kontekst renderowania jednej strony."""

    def __init__(self, src, out, kind):
        self.src = src
        self.out = out
        self.kind = kind
        self.refs = {}
        self.page_map = {}


def resolve_link(url, ctx):
    url = html.unescape(url.strip())
    if url.startswith("#") or url.startswith("mailto:"):
        return url
    frag = ""
    if "#" in url:
        url, frag = url.split("#", 1)
        frag = "#" + frag
    m = GH_RAW.match(url)
    if m and m.group(1).startswith("dzialy/images/"):
        return rel(ctx.out, "assets/img/" + posixpath.basename(m.group(1))) + frag
    m = GH_BLOB.match(url)
    if m:
        path = m.group(1)
        if path in ctx.page_map:
            return rel(ctx.out, ctx.page_map[path]) + frag
        return REPO_URL + "/tree/master/" + path + frag
    if not re.match(r"^[a-z]+:", url) and url:
        path = posixpath.normpath(posixpath.join(posixpath.dirname(ctx.src), url))
        if path in ctx.page_map:
            return rel(ctx.out, ctx.page_map[path]) + frag
        if path.startswith("dzialy/images/"):
            return rel(ctx.out, "assets/img/" + posixpath.basename(path)) + frag
        return REPO_URL + "/blob/master/" + path + frag
    return url.replace("wernexnrs123", "wernexnrs") + frag


def badge_html(key):
    key = key.lower()
    if key in BADGES:
        return '<span class="chip chip-%s">%s</span>' % (slugify(key) or "cpp", BADGES[key])
    if key in NEGATIVE_BADGES:
        return '<span class="chip chip-off" title="Brak rozwiązania w Pythonie">Python ✗</span>'
    return ""


def inline(text, ctx):
    """Formatowanie w linii: kod, obrazki, linki, pogrubienie, kursywa."""
    codes = []

    def keep(s):
        codes.append(s)
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", lambda m: keep("<code>%s</code>" % html.escape(m.group(1))), text)
    # surowe tagi HTML zostawiamy, resztę escapujemy
    text = re.sub(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^<>]*)?/?>", lambda m: keep(m.group(0)), text)
    text = re.sub(r"&(#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);", lambda m: keep(m.group(0)), text)
    text = html.escape(text, quote=False)

    def image(m):
        alt, url = m.group(1), m.group(2)
        return keep('<img src="%s" alt="%s" loading="lazy">' % (html.escape(resolve_link(url, ctx)), html.escape(alt)))

    def ref_image(m):
        key = m.group(1)
        if key.lower() in BADGES or key.lower() in NEGATIVE_BADGES or key.lower().startswith("no"):
            return keep(badge_html(key))
        url = ctx.refs.get(key.lower())
        if not url:
            return m.group(0)
        return keep('<img src="%s" alt="%s" loading="lazy">' % (html.escape(resolve_link(url, ctx)), html.escape(key)))

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", image, text)
    text = re.sub(r"!\[([^\]]+)\](?!\()", ref_image, text)

    def link(m):
        label, url = m.group(1), m.group(2)
        if label.strip() in ("⬆️", "⬆"):
            return ""
        href = resolve_link(url, ctx)
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return keep('<a href="%s"%s>' % (html.escape(href), ext)) + label + keep("</a>")

    def ref_link(m):
        label, key = m.group(1), (m.group(2) or m.group(1))
        url = ctx.refs.get(key.lower())
        if not url:
            return m.group(0)
        href = resolve_link(url, ctx)
        return keep('<a href="%s" target="_blank" rel="noopener">' % html.escape(href)) + label + keep("</a>")

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]*)\)", link, text)
    text = re.sub(r"\[([^\]]+)\]\[([^\]]*)\]", ref_link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w])__(.+?)__(?![\w])", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    for _ in range(3):
        text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


LANG_NAMES = {"python": "Python", "py": "Python", "cpp": "C++", "c++": "C++", "java": "Java",
              "sql": "SQL", "pascal": "Pascal", "text": "Wynik", "": "Pseudokod"}


NOTE_PL = {"iterated version": "iteracyjnie", "iterative version": "iteracyjnie",
           "recursive version": "rekurencyjnie", "recursive one-liner version": "rekurencyjnie, 1 linia",
           "in place": "w miejscu", "not in place": "nie w miejscu", "with sorting": "z sortowaniem",
           "with list and slices": "lista i wycinki", "with 2 strings": "dwa napisy"}


def code_block(lang, lines, ctx):
    lang = (lang or "").strip().lower()
    code = "\n".join(lines).rstrip("\n")
    # wspólne wcięcie (np. kod zagnieżdżony w liście)
    indents = [len(l) - len(l.lstrip(" ")) for l in code.split("\n") if l.strip()]
    cut = min(indents) if indents else 0
    if cut:
        code = "\n".join(l[cut:] for l in code.split("\n"))
    label = LANG_NAMES.get(lang, lang.upper() or "Kod")
    if not lang and ctx.kind not in ("algo",):
        label = "Kod"
    first = code.split("\n", 1)[0].strip()
    note = ""
    comment = r"^#\s*\S" if lang in ("python", "py") else r"^//\s*\S"
    if lang in ("python", "py", "cpp", "c++") and re.match(comment, first) and len(first) < 60:
        note = re.sub(r"^(#|//)\s*", "", first).strip()
        note = NOTE_PL.get(note.lower(), note)
    hl = {"python": "python", "py": "python", "cpp": "cpp", "c++": "cpp", "java": "java", "sql": "sql"}.get(lang)
    cls = "language-%s" % hl if hl else "nohighlight"
    return {"label": label, "note": note, "html": '<pre><code class="%s">%s</code></pre>' % (cls, html.escape(code))}


def render_code_group(blocks):
    if len(blocks) == 1:
        b = blocks[0]
        title = b["label"] + (" · " + html.escape(b["note"]) if b["note"] else "")
        pseudo = " pseudo" if b["label"] == "Pseudokod" else ""
        return ('<div class="code%s"><div class="code-bar"><span>%s</span>'
                '<button class="copy" type="button">Kopiuj</button></div>%s</div>' % (pseudo, title, b["html"]))
    tabs, panes = [], []
    titles = [b["label"] + (" · " + html.escape(b["note"]) if b["note"] else "") for b in blocks]
    for i, t in enumerate(titles):
        if titles.count(t) > 1:
            titles[i] = "%s %d" % (t, titles[:i + 1].count(t))
    for i, b in enumerate(blocks):
        title = titles[i]
        sel = "true" if i == 0 else "false"
        tabs.append('<button type="button" role="tab" aria-selected="%s" class="tab" data-lang="%s">%s</button>'
                    % (sel, slugify(b["label"]), title))
        panes.append('<div class="pane%s"%s>%s</div>' % (" pseudo" if b["label"] == "Pseudokod" else "",
                                                         "" if i == 0 else " hidden", b["html"]))
    return ('<div class="code tabs"><div class="code-bar"><div class="tablist" role="tablist">%s</div>'
            '<button class="copy" type="button">Kopiuj</button></div>%s</div>' % ("".join(tabs), "".join(panes)))


def render_list(lines, ctx):
    """Lista (także zagnieżdżona) na podstawie wcięć."""
    items = []  # (indent, ordered, text)
    for line in lines:
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            items.append([len(m.group(1)), m.group(2)[-1] == ".", m.group(3)])
        elif items:
            items[-1][2] += " " + line.strip()
    out = []
    stack = []  # (indent, tag)
    for indent, ordered, text in items:
        tag = "ol" if ordered else "ul"
        while stack and indent < stack[-1][0]:
            out.append("</li></%s>" % stack.pop()[1])
        if not stack or indent > stack[-1][0]:
            out.append("<%s>" % tag)
            stack.append((indent, tag))
        else:
            out.append("</li>")
        out.append("<li>" + inline(text, ctx))
    while stack:
        out.append("</li></%s>" % stack.pop()[1])
    return "".join(out)


def render_table(lines, ctx):
    def cells(line):
        line = line.strip().strip("|")
        return [c.strip() for c in line.split("|")]

    head = cells(lines[0])
    aligns = []
    for c in cells(lines[1]):
        if c.startswith(":") and c.endswith(":"):
            aligns.append("center")
        elif c.endswith(":"):
            aligns.append("right")
        else:
            aligns.append("")
    def td(tag, c, i):
        a = aligns[i] if i < len(aligns) and aligns[i] else ""
        return "<%s%s>%s</%s>" % (tag, ' style="text-align:%s"' % a if a else "", inline(c, ctx), tag)
    rows = ["<tr>" + "".join(td("th", c, i) for i, c in enumerate(head)) + "</tr>"]
    for line in lines[2:]:
        rows.append("<tr>" + "".join(td("td", c, i) for i, c in enumerate(cells(line))) + "</tr>")
    return '<div class="table-wrap"><table>%s</table></div>' % "".join(rows)


STRIP_LINE = re.compile(r"^\s*(</?details[^>]*>|<summary>.*?</summary>|</?b>|<details[^>]*><summary>.*?</summary>)\s*$", re.I)


def markdown_blocks(text, ctx):
    """Zwraca listę bloków: ('h', poziom, tekst, kotwice) | ('html', str) | ('code', blok)."""
    # definicje odnośników
    def ref(m):
        ctx.refs[m.group(1).lower()] = m.group(2)
        return ""
    text = re.sub(r"^\s{0,3}\[([^\]]+)\]:\s*(\S+).*$", ref, text, flags=re.M)

    lines = text.split("\n")
    blocks = []
    i = 0
    para = []

    def flush():
        if para:
            rendered = inline(" ".join(l.strip() for l in para), ctx)
            links = re.findall(r"<a [^>]*>.*?</a>", rendered)
            rest = re.sub(r"<a [^>]*>.*?</a>", "", rendered)
            if links and not re.sub(r"[-–—|·\s]", "", rest):
                # akapit z samych linków, np. "[ARKUSZ](..) --- [DANE](..)"
                if ctx.kind == "exam":
                    links = [l for l in links if "SPIS ARKUSZY" not in l]
                if not links:
                    para.clear()
                    return
                blocks.append(("html", '<p class="links">%s</p>' % "".join(links)))
            elif rendered.startswith("<strong>Odpowiedź"):
                blocks.append(("html", '<p class="answer">%s</p>' % rendered))
            elif re.fullmatch(r"<em>.*</em>", rendered):
                blocks.append(("html", '<p class="note">%s</p>' % rendered[4:-5]))
            else:
                blocks.append(("html", "<p>%s</p>" % rendered))
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        fence = re.match(r"^(\s*)(```+|~~~+)\s*([\w+#-]*)\s*$", line)
        if fence:
            flush()
            mark = fence.group(2)
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(mark[:3]):
                body.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", code_block(fence.group(3), body, ctx)))
            continue
        if not s:
            flush()
            i += 1
            continue
        if STRIP_LINE.match(s):
            flush()
            i += 1
            continue
        m = re.match(r'^<a name="([^"]+)">\s*</a>$', s)
        if m:
            flush()
            blocks.append(("anchor", m.group(1)))
            i += 1
            continue
        m = re.match(r"^<h([1-6])[^>]*>(.*?)</h\1>$", s)
        if m:
            flush()
            blocks.append(("h", int(m.group(1)), strip_tags(m.group(2)).strip(), []))
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", s)
        if m:
            flush()
            title = re.sub(r"\[⬆️?\]\([^)]*\)", "", m.group(2)).strip()
            # linki w nagłówku (np. "## 5 [[EXCEL] POBIERZ](plik.xlsx)") -> przyciski pod nagłówkiem
            links = re.findall(r"\[((?:\[[^\]]*\])?[^\]]*)\]\(([^)\s]+)\)", title)
            title = re.sub(r"\[((?:\[[^\]]*\])?[^\]]*)\]\(([^)\s]+)\)", "", title).strip(" -—")
            title = strip_tags(inline(title, ctx)).strip()
            blocks.append(("h", len(m.group(1)), title, []))
            if links:
                btns = []
                for label, url in links:
                    kind_m = re.search(r"\[(\w+)\]", label)
                    label = ("Pobierz plik " + kind_m.group(1).capitalize()) if kind_m else label.strip()
                    btns.append('<a href="%s" target="_blank" rel="noopener">%s</a>'
                                % (html.escape(resolve_link(url, ctx)), html.escape(label)))
                blocks.append(("html", '<p class="links">%s</p>' % "".join(btns)))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            flush()
            blocks.append(("html", "<hr>"))
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            blocks.append(("html", render_table(tbl, ctx)))
            continue
        if s.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append(("html", '<blockquote class="callout">%s</blockquote>' % inline(" ".join(quote), ctx)))
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush()
            lst = []
            while i < len(lines):
                l = lines[i]
                if re.match(r"^\s*([-*+]|\d+\.)\s+", l):
                    lst.append(l)
                elif l.strip() and l.startswith(" ") and not re.match(r"^\s*(```|~~~)", l) \
                        and not STRIP_LINE.match(l.strip()):
                    lst.append(l)
                elif not l.strip():
                    # pusta linia - lista trwa dalej, jeśli następna linia to element listy
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and re.match(r"^\s*([-*+]|\d+\.)\s+", lines[j]):
                        i = j
                        continue
                    break
                else:
                    break
                i += 1
            blocks.append(("html", render_list(lst, ctx)))
            continue
        if s.startswith("<") and re.match(r"^</?[a-zA-Z]", s):
            flush()
            blocks.append(("html", inline(s, ctx)))
            i += 1
            continue
        para.append(line)
        i += 1
    flush()
    return blocks


def blocks_to_html(blocks):
    """Skleja bloki; kolejne bloki kodu łączy w zakładki."""
    out = []
    group = []
    for b in blocks:
        if b[0] == "code":
            group.append(b[1])
            continue
        if group:
            out.append(render_code_group(group))
            group = []
        if b[0] == "html":
            out.append(b[1])
        elif b[0] == "anchor":
            out.append('<span id="%s" class="anchor"></span>' % html.escape(b[1]))
        elif b[0] == "h":
            out.append("<h%d>%s</h%d>" % (b[1], html.escape(b[2]), b[1]))
    if group:
        out.append(render_code_group(group))
    return "".join(out)


# --------------------------------------------------------------------------- strona

def build_page(src, out, kind, page_map):
    ctx = Ctx(src, out, kind)
    ctx.page_map = page_map
    text = read(src)
    blocks = markdown_blocks(text, ctx)

    # tytuł strony = pierwszy nagłówek h1
    title = None
    if blocks and blocks[0][0] == "h" and blocks[0][1] == 1:
        title = blocks.pop(0)[2]
    for k, b in enumerate(blocks):
        if b[0] == "h" and b[1] == 1 and title is None:
            title = b[2]
            blocks.pop(k)
            break

    # poziom sekcji: h2, a jeśli brak - h3, a jeśli brak - h1
    levels = [b[1] for b in blocks if b[0] == "h"]
    sec_level = 2 if 2 in levels else (3 if 3 in levels else (1 if 1 in levels else None))

    intro, sections = [], []
    pending_anchors = []
    cur = None
    part = None
    for b in blocks:
        if b[0] == "h" and sec_level and b[1] < sec_level:
            part = b[2]  # np. "# Arkusz I" - grupa sekcji
            pending_anchors = []
            continue
        if b[0] == "h" and b[1] == sec_level:
            if pending_anchors:
                # kotwica tuż przed nagłówkiem należy do nowej sekcji, nie do poprzedniej
                prev = cur["blocks"] if cur else intro
                prev[:] = [x for x in prev if not (x[0] == "anchor" and x[1] in pending_anchors)]
                if cur:
                    cur["anchors"] = [a for a in cur["anchors"] if a not in pending_anchors]
            cur = {"title": b[2], "blocks": [], "anchors": list(pending_anchors)}
            if part:
                cur["group"] = part
            pending_anchors = []
            sections.append(cur)
            continue
        if b[0] == "anchor":
            pending_anchors.append(b[1])
            if cur is not None and not any(x[0] in ("html", "code") for x in cur["blocks"]):
                cur["anchors"].append(b[1])
            (cur["blocks"] if cur else intro).append(b)
            continue
        pending_anchors = [] if b[0] != "h" else pending_anchors
        (cur["blocks"] if cur else intro).append(b)

    used = set()
    for s in sections:
        sid = slugify(s["title"])
        while sid in used:
            sid += "-2"
        used.add(sid)
        s["id"] = sid
        raw = blocks_to_html([x for x in s["blocks"] if x[0] == "html"])
        s["text"] = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", raw)).split())[:160]

    # grupy w spisie treści (strony z algorytmami): numerowana lista z linkami do kotwic
    groups = []
    if kind == "algo":
        anchor_to_sec = {}
        for s in sections:
            for a in s["anchors"]:
                anchor_to_sec[a] = s
        group = None
        for line in text.split("\n"):
            m = re.match(r"^\d+\.\s+(.*)$", line.strip())
            if m and not line.startswith(" " * 6):
                gtitle = strip_tags(inline(m.group(1), ctx)).strip(" :")
                group = {"title": gtitle[:1].upper() + gtitle[1:], "items": []}
                groups.append(group)
                continue
            for label, anchor in re.findall(r"\[([^\]]+)\]\(#([^)]+)\)", line):
                if group is not None and anchor in anchor_to_sec:
                    sec = anchor_to_sec[anchor]
                    if sec not in group["items"]:
                        group["items"].append(sec)
                        sec["group"] = group["title"]
                        sub = label.strip().rstrip(",").strip()
                        sub = sub[:1].upper() + sub[1:]
                        if slugify(sub) != slugify(sec["title"]):
                            sec["subtitle"] = sub
        rest = [s for s in sections if "group" not in s]
        if rest:
            groups.append({"title": "Inne", "items": rest})
    else:
        groups = []
        for s in sections:
            g = s.get("group", "")
            if not groups or groups[-1]["title"] != g:
                groups.append({"title": g, "items": []})
            groups[-1]["items"].append(s)

    # kolory, ikony i numeracja
    for gi, g in enumerate([g for g in groups if g["items"]], 1):
        g["color"] = (gi - 1) % 7 + 1
        g["icon"] = group_icon(g["title"])
        for ii, s in enumerate(g["items"], 1):
            if kind == "algo":
                s["idx"] = "%d.%d" % (gi, ii)
                s["color"] = g["color"]
    for s in sections:
        s["langs"] = []
        for b in s["blocks"]:
            if b[0] == "code" and b[1]["label"] not in s["langs"]:
                s["langs"].append(b[1]["label"])
        if kind == "doc":
            s["color"] = sections.index(s) % 7 + 1
        if kind == "exam":
            m = re.match(r"^\D*?(\d+)", s["title"])
            s["color"] = (int(m.group(1)) - 1) % 7 + 1 if m else 1
            s["idx"] = ""

    body = []
    if kind == "algo":
        body.append('<div class="groups">')
        for g in groups:
            if not g["items"]:
                continue
            n = len(g["items"])
            body.append('<section class="group" style="--c:var(--g%d)"><header class="group-head">'
                        '<span class="gicon" aria-hidden="true">%s</span><div><h2>%s</h2><p>%d %s</p></div></header><ol>'
                        % (g["color"], g["icon"], html.escape(g["title"]), n, plural(n)))
            for s in g["items"]:
                sub = '<small>%s</small>' % html.escape(s["subtitle"]) if s.get("subtitle") else ""
                body.append('<li><a href="#%s"><span class="idx">%s</span><span class="t"><b>%s</b>%s</span></a></li>'
                            % (s["id"], s["idx"], html.escape(s["title"]), sub))
            body.append("</ol></section>")
        body.append("</div>")
    else:
        body.append(blocks_to_html(intro))

    for s in sections:
        extra = "".join('<span id="%s" class="anchor"></span>' % html.escape(a) for a in s["anchors"] if a != s["id"])
        inner = blocks_to_html([b for b in s["blocks"] if not (b[0] == "anchor" and b[1] in s["anchors"])])
        group = '<p class="eyebrow">%s</p>' % html.escape(s["group"]) if s.get("group") else ""
        idx = '<span class="idx">%s</span>' % s["idx"] if s.get("idx") else ""
        sub = '<p class="sub">%s</p>' % html.escape(s["subtitle"]) if s.get("subtitle") else ""
        langs = "".join('<span class="lang lang-%s">%s</span>' % (slugify(l), html.escape(l)) for l in s["langs"])
        langs = '<div class="langs">%s</div>' % langs if langs else ""
        style = ' style="--c:var(--g%d)"' % s["color"] if s.get("color") else ""
        body.append('<section class="card%s" id="%s"%s>%s<header class="card-head">%s<div class="head-text">%s'
                    '<h2><a class="self" href="#%s">%s</a></h2>%s</div>%s</header>%s'
                    '<a class="to-top" href="#top" aria-label="Do góry">↑</a></section>'
                    % (" tinted" if style else "", s["id"], style, extra, idx, group, s["id"],
                       html.escape(s["title"]), sub, langs, inner))
    return {"title": title, "html": "".join(body), "sections": sections, "groups": groups}


LOCK_SVG = ('<svg viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M12 2a5 5 0 0 1 5 5v3h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h1V7a5 5 0 0 1 5-5Zm0 2a3 3 0 0 0-3 3v3h6V7a3 3 0 0 0-3-3Zm0 9a2 2 0 0 0-1 3.73V19h2v-2.27A2 2 0 0 0 12 13Z"/></svg>')
TRI_SVG = ('<svg viewBox="0 0 24 24" width="22" height="22"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" d="M12 3 2.5 20h19L12 3Z"/><circle cx="12" cy="3.5" r="1.8" fill="currentColor"/><circle cx="2.8" cy="20" r="1.8" fill="currentColor"/><circle cx="21.2" cy="20" r="1.8" fill="currentColor"/></svg>')


def group_icon(title):
    t = title.lower()
    for keys, icon in ((("całkow",), "17"), (("sort", "wyszuk"), "⇅"), (("numer",), "√x"), (("arytm",), "x̄"),
                       (("tekst", "łańcuch"), "Aa"), (("kompres", "szyfr"), LOCK_SVG), (("kombinat",), "n!"),
                       (("geometr",), TRI_SVG)):
        if any(k in t for k in keys):
            return icon
    return "{ }"


def plural(n, forms=("algorytm", "algorytmy", "algorytmów")):
    if n == 1:
        return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return forms[1]
    return forms[2]


NAV = [("index.html", "Start"), ("algorytmy.html", "Algorytmy CKE"), ("dodatkowe.html", "Dodatkowe"),
       ("arkusze.html", "Arkusze"), ("funkcje.html", "Python")]


def layout(out, title, description, content, sidebar="", crumbs=None, wide=False):
    root = rel(out, "index.html")[:-len("index.html")]
    canonical = SITE_URL + ("" if out == "index.html" else out)
    nav = []
    current = out
    if out.startswith(("arkusze/", "zbior/")):
        current = "arkusze.html"
    if out in ("metody.html", "biblioteki.html"):
        current = "funkcje.html"
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        nav.append('<a href="%s%s"%s>%s</a>' % (root, href, cur, label))
    crumb_html = ""
    if crumbs:
        parts = ['<a href="%s%s">%s</a>' % (root, h, html.escape(t)) for h, t in crumbs]
        crumb_html = '<nav class="crumbs" aria-label="Okruszki">%s<span>%s</span></nav>' % (
            " / ".join(parts) + " / ", html.escape(title))
    full_title = title if out == "index.html" else "%s | %s" % (title, SITE_NAME)
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": title,
          "description": description, "inLanguage": "pl", "url": canonical,
          "educationalLevel": "Szkoła średnia - matura", "isAccessibleForFree": True,
          "license": "https://opensource.org/licenses/MIT", "learningResourceType": "Materiały do nauki"}
    side = ""
    if sidebar:
        side = ('<aside class="sidebar" id="sidebar"><button class="side-toggle" type="button" '
                'aria-expanded="false" aria-controls="side-list">Spis treści</button>'
                '<div class="side-list" id="side-list">%s</div></aside>' % sidebar)
    return """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="pl_PL">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0f172a">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
<script>try{{var t=localStorage.getItem("motyw");if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="topbar" id="top">
  <a class="brand" href="{root}index.html"><span class="logo">&lt;/&gt;</span><span>Matura <b>informatyka</b></span></a>
  <nav class="mainnav" aria-label="Główne">{nav}</nav>
  <div class="tools">
    <button class="search-btn" type="button" data-open-search aria-label="Szukaj"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M10 2a8 8 0 0 1 6.32 12.9l5.39 5.4-1.41 1.4-5.4-5.39A8 8 0 1 1 10 2Zm0 2a6 6 0 1 0 0 12 6 6 0 0 0 0-12Z"/></svg><span>Szukaj</span><kbd>/</kbd></button>
    <button class="theme-btn" type="button" data-theme-toggle aria-label="Zmień motyw"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg></button>
    <a class="gh" href="{repo}" target="_blank" rel="noopener" aria-label="Repozytorium na GitHubie"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.1c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.9 1.3 3.6 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.7 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/></svg></a>
  </div>
</header>
<div class="shell{wide}">
{side}
<main id="tresc" tabindex="-1">
{crumbs}
{content}
</main>
</div>
<footer class="footer">
  <p class="slogan">Wiedza nie powinna mieć ceny.</p>
  <p>Darmowe materiały do matury z informatyki, tworzone przez społeczność. Kod i treść na licencji <a href="{repo}/blob/master/LICENSE" target="_blank" rel="noopener">MIT</a>.</p>
  <p class="powered"><span class="spark" aria-hidden="true">✦</span> Powered by AI · Claude Opus 5.5 (High)</p>
  <p><a href="{repo}" target="_blank" rel="noopener">GitHub</a> · <a href="{repo}/issues" target="_blank" rel="noopener">Zgłoś błąd</a> · <a href="{root}linki.html">Przydatne linki</a></p>
</footer>
<div class="search" id="search" hidden>
  <div class="search-box" role="dialog" aria-modal="true" aria-label="Wyszukiwarka">
    <input id="search-input" type="search" placeholder="Szukaj algorytmu, arkusza, zadania…" autocomplete="off" spellcheck="false">
    <ul id="search-results" role="listbox"></ul>
    <p class="search-hint"><kbd>↑</kbd><kbd>↓</kbd> wybór · <kbd>Enter</kbd> otwórz · <kbd>Esc</kbd> zamknij</p>
  </div>
</div>
<script>window.ROOT="{root}";</script>
<script src="{root}assets/search-index.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" defer></script>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
""".format(full_title=html.escape(full_title), desc=html.escape(description), canonical=canonical,
           site=SITE_NAME, title=html.escape(title), root=root, ld=json.dumps(ld, ensure_ascii=False),
           nav="".join(nav), repo=REPO_URL, side=side, crumbs=crumb_html, content=content,
           wide=" no-side" if not sidebar else "")


def sidebar_html(page, out):
    parts = []
    for g in page["groups"]:
        if not g["items"]:
            continue
        style = ' style="--c:var(--g%d)"' % g["color"] if g.get("color") else ""
        if g["title"]:
            parts.append('<p class="side-title"%s>%s</p>' % (style, html.escape(g["title"])))
        parts.append('<ul%s>' % style)
        for s in g["items"]:
            idx = '<span class="sidx">%s</span>' % s["idx"] if s.get("idx") else ""
            li_style = ' style="--c:var(--g%d)"' % s["color"] if s.get("color") and not g.get("color") else ""
            parts.append('<li%s><a href="#%s">%s%s</a></li>' % (li_style, s["id"], idx, html.escape(s["title"])))
        parts.append("</ul>")
    return "".join(parts)


def main():
    if os.path.isdir(os.path.join(DOCS, "assets", "img")):
        shutil.rmtree(os.path.join(DOCS, "assets", "img"))
    for sub in ("arkusze", "zbior"):
        if os.path.isdir(os.path.join(DOCS, sub)):
            shutil.rmtree(os.path.join(DOCS, sub))

    # mapa: plik md -> strona html
    page_map = {}
    main_pages = [p for p in MAIN_PAGES if os.path.exists(os.path.join(ROOT, p[0]))]
    for src, out, *_ in main_pages:
        page_map[src] = out
    exams = []
    for folder in ("dzialy/zadania_arkusze", "dzialy/zadania_zbior"):
        for dirpath, _, files in os.walk(os.path.join(ROOT, folder)):
            for f in sorted(files):
                if f.endswith(".md"):
                    src = posixpath.relpath(os.path.join(dirpath, f).replace(os.sep, "/"), ROOT.replace(os.sep, "/"))
                    page_map[src] = exam_out(src)
                    exams.append(src)

    index_entries = []
    built = []
    stats = {}
    exam_info = {}
    exam_entries = []

    exam_titles = {}
    for src in exams:
        out = page_map[src]
        text = read(src)
        title = exam_title(src, text)
        exam_titles[src] = title
        page = build_page(src, out, "exam", page_map)
        tasks = [s["title"] for s in page["sections"]]
        desc = "%s - rozwiązania zadań w Pythonie z odpowiedziami%s." % (
            title, (" (zadania " + ", ".join(tasks[:12]) + ")") if tasks else "")
        if not page["sections"] and not page["html"].strip():
            content = ('<h1 class="page-title">%s</h1><div class="empty"><p>Rozwiązania tego arkusza jeszcze nie ma.</p>'
                       '<p><a href="%s" target="_blank" rel="noopener">Dodaj je na GitHubie</a> - każda pomoc się przyda.</p></div>'
                       % (html.escape(title), REPO_URL + "/blob/master/" + src))
        else:
            content = '<h1 class="page-title">%s</h1>%s<p class="source"><a href="%s" target="_blank" rel="noopener">Edytuj na GitHubie</a></p>' % (
                html.escape(title), page["html"], REPO_URL + "/blob/master/" + src)
        side = sidebar_html(page, out) if len(page["sections"]) > 1 else ""
        write(out, layout(out, title, desc, content, side, [("index.html", "Start"), ("arkusze.html", "Arkusze")]))
        built.append(out)
        exam_info[src] = {"title": title, "out": out, "tasks": len(tasks)}
        exam_entries.append({"t": title, "p": "Arkusz" if src.startswith("dzialy/zadania_arkusze") else "Zbiór CKE",
                             "u": out, "x": ("Zadania: " + ", ".join(tasks)) if tasks else ""})

    for src, out, title, short, kind, desc in main_pages:
        crumbs = [("index.html", "Start")]
        if kind == "index":
            page = {"html": exam_index_html(src, out, page_map, exam_info), "sections": [], "groups": []}
        else:
            page = build_page(src, out, kind, page_map)
        content = '<h1 class="page-title">%s</h1><p class="lead">%s</p>%s' % (html.escape(title), html.escape(desc), page["html"])
        side = sidebar_html(page, out) if kind != "index" else ""
        write(out, layout(out, title, desc, content, side, crumbs))
        built.append(out)
        stats[out] = len(page["sections"])
        if kind == "algo":
            stats[out + ":groups"] = [g for g in page["groups"] if g["items"]]
        for s in page["sections"]:
            index_entries.append({"t": s["title"], "p": short, "u": out + "#" + s["id"],
                                  "x": (s.get("subtitle", "") + " " + s["text"]).strip()[:120]})
        if kind != "algo":
            index_entries.append({"t": title, "p": "Strona", "u": out, "x": desc[:120]})
    index_entries += exam_entries

    # strona główna
    write("index.html", home_page(stats, exams, exam_titles, page_map))
    built.insert(0, "index.html")

    # zasoby
    os.makedirs(os.path.join(DOCS, "assets", "img"), exist_ok=True)
    img_dir = os.path.join(ROOT, "dzialy", "images")
    if os.path.isdir(img_dir):
        for f in os.listdir(img_dir):
            shutil.copy(os.path.join(img_dir, f), os.path.join(DOCS, "assets", "img", f))
    write("assets/search-index.js", "window.SEARCH_INDEX=" + json.dumps(index_entries, ensure_ascii=False) + ";\n")

    # SEO
    today = date.today().isoformat()
    urls = "".join("<url><loc>%s</loc><lastmod>%s</lastmod></url>" % (SITE_URL + ("" if u == "index.html" else u), today) for u in built)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % SITE_URL)
    write(".nojekyll", "")
    write("404.html", layout("404.html", "Nie znaleziono strony", "Strona nie istnieje.",
                             '<div class="empty"><h1 class="page-title">404</h1><p>Tej strony nie ma. '
                             '<a href="./index.html">Wróć na start</a> albo użyj wyszukiwarki (<kbd>/</kbd>).</p></div>'))
    print("Zbudowano %d stron w %s" % (len(built) + 1, DOCS))


EXAM_GROUP_COLORS = {"zbiór": 4, "matura próbna": 3, "matura podstawowa": 2, "matura": 1}


def exam_index_html(src, out, page_map, exam_info):
    """Spis arkuszy jako siatka kart pogrupowanych wg rodzaju matury."""
    ctx = Ctx(src, out, "index")
    ctx.page_map = page_map
    text = read(src)
    markdown_blocks(text, ctx)  # zbiera definicje odnośników (znaczki)
    parts, cards, intro = [], [], []
    group_title = None

    def close_group():
        if group_title is None:
            return
        color = 1
        for key, c in EXAM_GROUP_COLORS.items():
            if group_title.lower().startswith(key):
                color = c
                break
        parts.append('<section class="exam-group" style="--c:var(--g%d)"><header class="group-head">'
                     '<span class="gicon" aria-hidden="true">%s</span><div><h2 id="%s">%s</h2><p>%d %s</p></div></header>%s'
                     '<div class="exam-grid">%s</div></section>'
                     % (color, "Σ" if "zbi" in group_title.lower() else "✎", slugify(group_title),
                        html.escape(group_title), len(cards),
                        plural(len(cards), ("zadanie", "zadania", "zadań") if "zbi" in group_title.lower()
                               else ("arkusz", "arkusze", "arkuszy")),
                        "".join(intro), "".join(cards)))

    for line in text.split("\n"):
        s = line.strip()
        m = re.match(r"^##\s+(.*)$", s)
        if m:
            close_group()
            group_title, cards, intro = m.group(1).strip(), [], []
            continue
        if group_title is None or not s:
            continue
        m = re.match(r"^[-*]\s+(.*?)\[([^\]]+)\]\(([^)]+\.md)\)(.*)$", s)
        if m:
            badges, label, path, rest = m.groups()
            path = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
            info = exam_info.get(path, {})
            href = rel(out, page_map[path]) if path in page_map else resolve_link(path, ctx)
            chips = "".join(badge_html(b) for b in re.findall(r"!\[([^\]]+)\]", badges)
                            if b.lower() in BADGES)
            ext = re.search(r"\[[^\]]+\]\((https?://[^)]+)\)", rest)
            year = re.search(r"(19|20)\d{2}", label)
            if year:
                big = year.group(0)
                small = " ".join(label.replace(big, "").replace("Matura", "").split()) or "Matura"
            else:
                zm = re.match(r"Zadanie\s+(\d+)\.\s*(.*?)(\s*-\s*str\..*)?$", label)
                big, small = (zm.group(1), zm.group(2)) if zm else (label, "")
            n = info.get("tasks", 0)
            meta = "%d %s" % (n, plural(n, ("zadanie", "zadania", "zadań"))) if n else ""
            src_link = ('<a class="exam-src" href="%s" target="_blank" rel="noopener">Treść arkusza ↗</a>'
                        % html.escape(ext.group(1))) if ext else ""
            cards.append('<article class="exam-card"><a class="exam-main" href="%s"><span class="exam-year">%s</span>'
                         '<span class="exam-name">%s</span><span class="exam-meta">%s</span></a>'
                         '<div class="exam-foot"><span class="chips">%s</span>%s</div></article>'
                         % (html.escape(href), html.escape(big), html.escape(small), meta, chips, src_link))
            continue
        if not s.startswith(("-", "*")):
            rendered = inline(s, ctx)
            links = re.findall(r"<a [^>]*>.*?</a>", rendered)
            if links and not re.sub(r"[-–—|·\s]", "", re.sub(r"<a [^>]*>.*?</a>", "", rendered)):
                links = [re.sub(r"<a ", '<a target="_blank" rel="noopener" ', l, count=1) if "target=" not in l else l
                         for l in links]
                intro.append('<p class="links">%s</p>' % "".join(links))
            else:
                intro.append('<p class="group-intro">%s</p>' % rendered)
    close_group()
    return "".join(parts)


def home_page(stats, exams, exam_titles, page_map):
    groups = stats.get("algorytmy.html:groups", [])
    n_algo = stats.get("algorytmy.html", 0)
    n_extra = stats.get("dodatkowe.html", 0)
    n_exam = len([e for e in exams if e.startswith("dzialy/zadania_arkusze")])
    n_zb = len([e for e in exams if e.startswith("dzialy/zadania_zbior")])
    quick = []
    for g in groups:
        links = "".join('<li><a href="algorytmy.html#%s"><span class="idx">%s</span><span class="t"><b>%s</b></span></a></li>'
                        % (s["id"], s.get("idx", ""), html.escape(s["title"])) for s in g["items"])
        quick.append('<section class="group compact" style="--c:var(--g%d)"><header class="group-head">'
                     '<span class="gicon" aria-hidden="true">%s</span><div><h3>%s</h3></div></header><ol>%s</ol></section>'
                     % (g["color"], g["icon"], html.escape(g["title"]), links))
    content = """
<section class="hero">
  <p class="eyebrow">Matura z informatyki · Python · CKE</p>
  <h1>Wiedza nie powinna mieć&nbsp;ceny.</h1>
  <p class="lead">Wszystkie algorytmy z wymagań CKE z kodem w Pythonie i pseudokodem, dodatkowe algorytmy oraz rozwiązania arkuszy maturalnych z odpowiedziami. Inni chowają to za paywallem — tu masz wszystko za darmo.</p>
  <ul class="manifest" aria-label="Zasady">
    <li><b>0 zł</b><span>bez opłat i abonamentów</span></li>
    <li><b>0 reklam</b><span>nic nie rozprasza</span></li>
    <li><b>0 logowania</b><span>otwierasz i się uczysz</span></li>
    <li><b>100% otwarte</b><span>licencja MIT</span></li>
  </ul>
  <button class="hero-search" type="button" data-open-search><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M10 2a8 8 0 0 1 6.32 12.9l5.39 5.4-1.41 1.4-5.4-5.39A8 8 0 1 1 10 2Zm0 2a6 6 0 1 0 0 12 6 6 0 0 0 0-12Z"/></svg><span>Szukaj: sito, NWD, bisekcja, 2019 maj…</span><kbd>/</kbd></button>
  <p class="powered"><span class="spark" aria-hidden="true">✦</span> Powered by AI · Claude Opus 5.5 (High)</p>
</section>
<section class="tiles">
  <a class="tile" style="--c:var(--g1)" href="algorytmy.html"><span class="tile-icon" aria-hidden="true">⇅</span><span class="num">{n_algo}</span><h2>Algorytmy z wymagań CKE</h2><p>Liczby, sortowania, wyszukiwanie, numeryczne, teksty, szyfry, geometria.</p></a>
  <a class="tile" style="--c:var(--g5)" href="dodatkowe.html"><span class="tile-icon" aria-hidden="true">+</span><span class="num">{n_extra}</span><h2>Dodatkowe algorytmy</h2><p>Średnie, mediana, moda, KMP, Boyer-Moore, Manacher, geometria analityczna.</p></a>
  <a class="tile" style="--c:var(--g3)" href="arkusze.html"><span class="tile-icon" aria-hidden="true">✎</span><span class="num">{n_exam}</span><h2>Rozwiązane arkusze</h2><p>Matury 2005–2021: rozszerzona, podstawowa, próbne + {n_zb} zadań ze zbioru CKE.</p></a>
  <a class="tile" style="--c:var(--g2)" href="funkcje.html"><span class="tile-icon" aria-hidden="true">Py</span><span class="num">3</span><h2>Ściągi z Pythona</h2><p>Funkcje wbudowane, metody i przydatne moduły.</p></a>
</section>
<h2 class="section-title">Szybki dostęp: wymagania CKE</h2>
<div class="groups">{quick}</div>
<section class="howto">
  <h2 class="section-title">Jak się uczyć z tej strony</h2>
  <ol>
    <li>Zacznij od <a href="algorytmy.html">algorytmów z wymagań</a> - przy każdym jest kod w Pythonie i pseudokod (przełączasz zakładkami).</li>
    <li>Przepisz algorytm samodzielnie, a dopiero potem porównaj z kodem. Przycisk <b>Kopiuj</b> przyda się do testów.</li>
    <li>Rozwiązuj <a href="arkusze.html">arkusze</a> na danych z CKE i sprawdzaj wynik z odpowiedzią pod kodem.</li>
    <li>Wyszukiwarka (<kbd>/</kbd> lub <kbd>Ctrl</kbd>+<kbd>K</kbd>) znajdzie każdy algorytm i arkusz.</li>
  </ol>
</section>
""".format(n_algo=n_algo, n_extra=n_extra, n_exam=n_exam, n_zb=n_zb, quick="".join(quick))
    desc = ("Darmowe materiały do matury z informatyki: wszystkie algorytmy z wymagań CKE w Pythonie z pseudokodem, "
            "dodatkowe algorytmy i rozwiązania arkuszy maturalnych 2005-2021 z odpowiedziami.")
    return layout("index.html", "Matura z informatyki - algorytmy i arkusze w Pythonie", desc, content)


if __name__ == "__main__":
    main()
