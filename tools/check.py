"""Sprawdza pliki Markdown w `dzialy/` - uruchom przed wysłaniem pull requesta.

    python tools/check.py            # struktura Markdown + składnia Pythona
    python tools/check.py --run      # dodatkowo uruchamia kod algorytmów (Python, C++, Java)

Co jest sprawdzane:
  * zamknięte bloki ``` oraz znaczniki <details>,
  * linki w spisie treści (#kotwica) mają swoje <a name="kotwica">,
  * każdy blok ```python ma poprawną składnię,
  * z --run: bloki z plików algorytmów są uruchamiane, a C++ (g++ -std=c++23) i Java (javac)
    kompilowane i uruchamiane - jeśli kompilator jest zainstalowany (inaczej są pomijane).
Bloki z arkuszy nie są uruchamiane, bo potrzebują plików z danymi CKE.
"""

import ast
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_FILES = ("algorytmy_wymagania.md", "dodatkowe_algorytmy.md", "funkcje_wbudowane.md", "metody.md", "biblioteki.md")
BLOCK = re.compile(r"^```([\w+#-]*)[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def find_tool(name, extra=()):
    path = shutil.which(name)
    if path:
        return path
    for p in extra:
        if os.path.exists(p):
            return p
    return None


GPP = os.environ.get("CXX") or find_tool("g++",[r"C:\msys64\ucrt64\bin\g++.exe"])
JAVAC = find_tool("javac")
JAVA = find_tool("java")


ENV = dict(os.environ)
if GPP and os.path.dirname(GPP):
    # g++ z MSYS2 i skompilowane programy potrzebują bibliotek DLL z folderu kompilatora
    ENV["PATH"] = os.path.dirname(GPP) + os.pathsep + ENV.get("PATH", "")


def run(cmd, cwd, timeout=60):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, input="", env=ENV)
    except subprocess.TimeoutExpired:
        return False, "przekroczono czas %ds" % timeout
    return r.returncode == 0, (r.stderr or r.stdout).strip()[-600:]


def check_file(path, do_run):
    rel = os.path.relpath(path, ROOT)
    errors = []
    text = open(path, encoding="utf-8").read()
    lines_before = lambda pos: text.count("\n", 0, pos) + 1

    if len(re.findall(r"^\s*```", text, re.M)) % 2:
        errors.append("niezamknięty blok ``` (liczba znaczników ``` jest nieparzysta)")
    if text.count("<details") != text.count("</details>"):
        errors.append("liczba <details> i </details> się nie zgadza")
    anchors = set(re.findall(r'<a name="([^"]+)"', text))
    for a in re.findall(r"\]\(#([^)]+)\)", text):
        if a not in anchors and a not in ("", "main"):
            errors.append("link do #%s, a w pliku nie ma <a name=\"%s\">" % (a, a))

    blocks = list(BLOCK.finditer(text))
    tmp = tempfile.mkdtemp(prefix="matura_check_")
    stats = {"py": 0, "cpp": 0, "java": 0, "pominięte": 0}
    try:
        for i, m in enumerate(blocks):
            lang, code, line = m.group(1).lower(), m.group(2), lines_before(m.start())
            where = "%s:%d" % (rel, line)
            if lang in ("python", "py"):
                try:
                    ast.parse(code)
                except SyntaxError as e:
                    errors.append("%s: błąd składni Pythona: %s" % (where, e.msg))
                    continue
                if do_run and os.path.basename(path) in RUN_FILES and "turtle" not in code:
                    f = os.path.join(tmp, "blok%d.py" % i)
                    open(f, "w", encoding="utf-8").write(code)
                    ok, out = run([sys.executable, "-I", f], tmp)
                    stats["py"] += 1
                    if not ok:
                        errors.append("%s: Python zakończył się błędem: %s" % (where, out.splitlines()[-1] if out else ""))
            elif lang in ("cpp", "c++") and do_run and os.path.basename(path) in RUN_FILES:
                if not GPP:
                    stats["pominięte"] += 1
                    continue
                d = os.path.join(tmp, "cpp%d" % i)
                os.makedirs(d)
                open(os.path.join(d, "main.cpp"), "w", encoding="utf-8").write(code)
                exe = os.path.join(d, "main.exe")
                ok, out = run([GPP, "-std=c++23", "-O2", "-o", exe, "main.cpp", "-lstdc++exp"], d, 120)
                if not ok and "stdc++exp" in out:
                    ok, out = run([GPP, "-std=c++23", "-O2", "-o", exe, "main.cpp"], d, 120)
                stats["cpp"] += 1
                if not ok:
                    errors.append("%s: C++ nie kompiluje się: %s" % (where, out.splitlines()[0] if out else ""))
                    continue
                ok, out = run([exe], d)
                if not ok:
                    errors.append("%s: program C++ zakończył się błędem" % where)
            elif lang == "java" and do_run and os.path.basename(path) in RUN_FILES:
                if not (JAVAC and JAVA):
                    stats["pominięte"] += 1
                    continue
                cls = re.search(r"public\s+(?:final\s+)?class\s+(\w+)", code)
                if not cls:
                    errors.append("%s: blok Javy nie ma klasy public class" % where)
                    continue
                d = os.path.join(tmp, "java%d" % i)
                os.makedirs(d)
                open(os.path.join(d, cls.group(1) + ".java"), "w", encoding="utf-8").write(code)
                ok, out = run([JAVAC, "-encoding", "UTF-8", cls.group(1) + ".java"], d, 120)
                stats["java"] += 1
                if not ok:
                    errors.append("%s: Java nie kompiluje się: %s" % (where, out.splitlines()[0] if out else ""))
                    continue
                ok, out = run([JAVA, "-cp", ".", cls.group(1)], d)
                if not ok:
                    errors.append("%s: program Java zakończył się błędem" % where)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return errors, stats


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    do_run = "--run" in sys.argv
    files = sorted(glob.glob(os.path.join(ROOT, "dzialy", "**", "*.md"), recursive=True))
    all_errors = []
    total = {"py": 0, "cpp": 0, "java": 0, "pominięte": 0}
    for f in files:
        errors, stats = check_file(f, do_run)
        all_errors += errors
        for k in total:
            total[k] += stats[k]
    print("Sprawdzono %d plików Markdown." % len(files))
    if do_run:
        print("Uruchomiono: Python %(py)d, C++ %(cpp)d, Java %(java)d; pominięte (brak kompilatora): %(pominięte)d" % total)
    if all_errors:
        print("\nZnalezione problemy (%d):" % len(all_errors))
        for e in all_errors:
            print("  - " + e)
            if os.environ.get("GITHUB_ACTIONS"):
                # adnotacja widoczna w zakładce Actions / w pull requeście
                m = re.match(r"^(.+?\.md):(\d+): (.*)$", e)
                if m:
                    print("::error file=%s,line=%s::%s" % (m.group(1).replace(os.sep, "/"), m.group(2), m.group(3)[:300]))
                else:
                    print("::error::%s" % e[:300])
        sys.exit(1)
    print("Wszystko w porządku ✔")


if __name__ == "__main__":
    main()
