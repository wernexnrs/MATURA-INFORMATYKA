/* Matura z informatyki - interakcje strony: motyw, zakładki kodu, kopiowanie, wyszukiwarka, spis treści. */
(function () {
  "use strict";

  /* ---------- motyw ---------- */
  var themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var root = document.documentElement;
      var dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      root.dataset.theme = dark ? "light" : "dark";
      try { localStorage.setItem("motyw", root.dataset.theme); } catch (e) { /* brak dostępu */ }
    });
  }

  /* ---------- przewinięcie do #kotwicy po wczytaniu (czcionki i kod zmieniają wysokość) ---------- */
  function goToHash() {
    if (!location.hash) return;
    var el = null;
    try { el = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { /* zły hash */ }
    if (el) el.scrollIntoView({ block: "start" });
  }
  window.addEventListener("load", function () { setTimeout(goToHash, 0); });

  /* ---------- podświetlanie składni ---------- */
  function highlight() {
    if (!window.hljs) return;
    document.querySelectorAll("pre code[class^='language-']").forEach(function (el) {
      window.hljs.highlightElement(el);
    });
  }
  if (window.hljs) highlight(); else window.addEventListener("load", highlight);

  /* ---------- przełącznik języków (zapamiętany dla całej strony) i kopiowanie ---------- */
  var LANG_KEY = "jezyk";
  function showLang(box, lang) {
    var btns = box.querySelectorAll(".lang-btn");
    if (!box.querySelector('.lang-pane[data-lang="' + lang + '"]')) return false;
    btns.forEach(function (b) { b.setAttribute("aria-selected", b.dataset.lang === lang ? "true" : "false"); });
    box.querySelectorAll(".lang-pane").forEach(function (p) { p.hidden = p.dataset.lang !== lang; });
    return true;
  }
  function showLangEverywhere(lang, except) {
    document.querySelectorAll(".code.multi").forEach(function (box) { if (box !== except) showLang(box, lang); });
  }
  var saved = null;
  try { saved = localStorage.getItem(LANG_KEY); } catch (e) { /* brak dostępu */ }
  if (saved) showLangEverywhere(saved, null);

  document.querySelectorAll(".code.multi").forEach(function (box) {
    box.querySelectorAll(".lang-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var lang = btn.dataset.lang;
        var top = btn.getBoundingClientRect().top;
        showLang(box, lang);
        showLangEverywhere(lang, box);
        // zachowaj pozycję klikniętego przełącznika (inne bloki mogły zmienić wysokość)
        window.scrollBy(0, btn.getBoundingClientRect().top - top);
        try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* brak dostępu */ }
      });
    });
  });

  document.querySelectorAll(".variant .copy").forEach(function (copy) {
    copy.addEventListener("click", function () {
      var code = copy.closest(".variant").querySelector("code");
      var text = code ? code.textContent : "";
      var done = function () {
        copy.textContent = "Skopiowano";
        copy.classList.add("done");
        setTimeout(function () { copy.textContent = "Kopiuj"; copy.classList.remove("done"); }, 1500);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
      } else { fallbackCopy(text); done(); }
    });
  });

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); } catch (e) { /* nic */ }
    document.body.removeChild(ta);
  }

  /* ---------- spis treści: telefon + aktywna sekcja ---------- */
  var sidebar = document.getElementById("sidebar");
  if (sidebar) {
    var toggle = sidebar.querySelector(".side-toggle");
    toggle.addEventListener("click", function () {
      var open = sidebar.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    sidebar.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        sidebar.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    var links = {};
    sidebar.querySelectorAll("a[href^='#']").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    if ("IntersectionObserver" in window) {
      var current = null;
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && links[e.target.id]) {
            if (current) current.classList.remove("active");
            current = links[e.target.id];
            current.classList.add("active");
            var list = sidebar.querySelector(".side-list");
            if (list && window.innerWidth > 900) {
              var top = current.offsetTop - list.offsetTop;
              if (top < sidebar.scrollTop || top > sidebar.scrollTop + sidebar.clientHeight - 40) {
                sidebar.scrollTop = top - 80;
              }
            }
          }
        });
      }, { rootMargin: "-80px 0px -70% 0px" });
      document.querySelectorAll("section.card[id]").forEach(function (s) { obs.observe(s); });
    }
  }

  /* ---------- wyszukiwarka ---------- */
  var overlay = document.getElementById("search");
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var root = window.ROOT || "";
  var selected = -1;

  function norm(s) {
    return (s || "").toLowerCase()
      .replace(/ą/g, "a").replace(/ć/g, "c").replace(/ę/g, "e").replace(/ł/g, "l").replace(/ń/g, "n")
      .replace(/ó/g, "o").replace(/ś/g, "s").replace(/[źż]/g, "z");
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function search(q) {
    var index = window.SEARCH_INDEX || [];
    var words = norm(q).split(/\s+/).filter(Boolean);
    if (!words.length) return index.filter(function (e) { return e.p !== "Strona"; }).slice(0, 8);
    var scored = [];
    index.forEach(function (e) {
      var t = norm(e.t), x = norm(e.x + " " + e.p), score = 0;
      for (var i = 0; i < words.length; i++) {
        var w = words[i];
        if (t.indexOf(w) === 0) score += 6;
        else if (t.indexOf(w) > -1) score += 4;
        else if (x.indexOf(w) > -1) score += 1;
        else return;
      }
      scored.push([score, e]);
    });
    scored.sort(function (a, b) { return b[0] - a[0]; });
    return scored.slice(0, 30).map(function (s) { return s[1]; });
  }

  function render() {
    var found = search(input.value);
    selected = found.length ? 0 : -1;
    if (!found.length) {
      results.innerHTML = '<li class="r-empty">Nic nie znaleziono. Spróbuj innego słowa, np. „sortowanie”.</li>';
      return;
    }
    results.innerHTML = found.map(function (e, i) {
      return '<li role="option" aria-selected="' + (i === 0) + '"><a href="' + esc(root + e.u) + '">' +
        '<span class="r-title">' + esc(e.t) + '</span><span class="r-page">' + esc(e.p) + "</span>" +
        (e.x ? '<span class="r-text">' + esc(e.x) + "</span>" : "") + "</a></li>";
    }).join("");
  }

  function move(d) {
    var items = results.querySelectorAll("li[role='option']");
    if (!items.length) return;
    items[selected].setAttribute("aria-selected", "false");
    selected = (selected + d + items.length) % items.length;
    items[selected].setAttribute("aria-selected", "true");
    items[selected].scrollIntoView({ block: "nearest" });
  }

  function open() {
    overlay.hidden = false;
    input.value = "";
    render();
    input.focus();
  }
  function close() { overlay.hidden = true; }

  document.querySelectorAll("[data-open-search]").forEach(function (b) { b.addEventListener("click", open); });
  overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
  results.addEventListener("click", function (e) { if (e.target.closest("a")) close(); });
  input.addEventListener("input", render);
  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
    else if (e.key === "Enter") {
      var a = results.querySelector("li[aria-selected='true'] a");
      if (a) { close(); window.location.href = a.href; }
    }
  });
  document.addEventListener("keydown", function (e) {
    var typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName);
    if (e.key === "Escape" && !overlay.hidden) close();
    else if ((e.key === "/" && !typing) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
      e.preventDefault();
      open();
    }
  });
})();
