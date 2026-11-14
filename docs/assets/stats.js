/* Strona "Statystyki": rysuje wykresy z assets/stats.json (aktualizowanego codziennie przez GitHub Actions). */
(function () {
  "use strict";
  var box = document.getElementById("stats-live");
  if (!box) return;

  var fmt = function (n) { return Number(n || 0).toLocaleString("pl-PL"); };
  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  };
  var dayPl = function (iso) {
    var d = new Date(iso + "T00:00:00");
    return isNaN(d) ? iso : d.toLocaleDateString("pl-PL", { day: "numeric", month: "short" });
  };

  function empty(msg) {
    box.innerHTML = '<div class="stats-empty"><p><b>Statystyki dopiero się zbierają.</b></p><p>' + msg + "</p></div>";
  }

  fetch(box.dataset.src, { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(render)
    .catch(function () {
      empty("Licznik działa od listopada 2026 r. Pierwsze wykresy pojawią się tutaj po pierwszej codziennej aktualizacji.");
    });

  /* ---------- kategorie stron ---------- */
  function category(path) {
    var p = (path || "").replace(/^\/MATURA-INFORMATYKA/, "");
    if (p === "/" || p === "" || p === "/index.html") return "Strona główna";
    if (/^\/algorytmy/.test(p)) return "Algorytmy CKE";
    if (/^\/dodatkowe/.test(p)) return "Dodatkowe algorytmy";
    if (/^\/arkusze/.test(p)) return "Arkusze maturalne";
    if (/^\/zbior\//.test(p)) return "Zbiór zadań CKE";
    if (/^\/(funkcje|metody|biblioteki)/.test(p)) return "Ściągi z Pythona";
    if (/^\/statystyki/.test(p)) return "Statystyki";
    return "Inne";
  }
  function pageLabel(h) {
    var t = (h.title || "").replace(/\s*\|\s*Matura z informatyki\s*$/, "");
    return t || (h.path || "").replace(/^\/MATURA-INFORMATYKA/, "") || "/";
  }
  function pageHref(path) {
    return (path || "").replace(/^\/MATURA-INFORMATYKA\//, "").replace(/^\//, "") || "index.html";
  }

  /* ---------- poziome słupki (jedna seria) ---------- */
  function bars(title, rows, opts) {
    opts = opts || {};
    rows = rows.filter(function (r) { return r.count > 0; }).slice(0, opts.limit || 10);
    if (!rows.length) return "";
    var max = Math.max.apply(null, rows.map(function (r) { return r.count; }));
    var sum = rows.reduce(function (a, r) { return a + r.count; }, 0);
    var html = '<section class="chart-card"><h3>' + esc(title) + "</h3>" +
      (opts.note ? '<p class="chart-note">' + esc(opts.note) + "</p>" : "") + '<ol class="hbars">';
    rows.forEach(function (r) {
      var pct = Math.max(1.5, (r.count / max) * 100);
      var share = opts.share ? ' <span class="share">' + Math.round((r.count / (opts.total || sum)) * 100) + "%</span>" : "";
      var label = r.href ? '<a href="' + esc(r.href) + '">' + esc(r.name) + "</a>" : esc(r.name);
      html += '<li title="' + esc(r.name) + ": " + fmt(r.count) + '"><span class="hb-label">' + label +
        '</span><span class="hb-track"><span class="hb-bar" style="width:' + pct.toFixed(1) + '%"></span></span>' +
        '<span class="hb-val">' + fmt(r.count) + share + "</span></li>";
    });
    html += "</ol>" + table(rows, ["Nazwa", "Odwiedziny"]) + "</section>";
    return html;
  }

  function table(rows, head) {
    return '<details class="chart-table"><summary>Pokaż tabelę</summary><table><thead><tr><th>' + head[0] +
      '</th><th style="text-align:right">' + head[1] + "</th></tr></thead><tbody>" +
      rows.map(function (r) { return "<tr><td>" + esc(r.name) + '</td><td style="text-align:right">' + fmt(r.count) + "</td></tr>"; }).join("") +
      "</tbody></table></details>";
  }

  /* ---------- wykres odwiedzin w czasie (SVG, crosshair + podpowiedź) ---------- */
  function lineChart(daily) {
    var W = 800, H = 240, L = 44, R = 12, T = 14, B = 28;
    var n = daily.length;
    var max = Math.max(1, Math.max.apply(null, daily.map(function (d) { return d.count; })));
    var step = Math.pow(10, Math.floor(Math.log10(max)));
    var top = Math.ceil(max / step) * step;
    if (top / step > 5) step *= 2;
    var x = function (i) { return L + (n === 1 ? (W - L - R) / 2 : (i / (n - 1)) * (W - L - R)); };
    var y = function (v) { return T + (1 - v / top) * (H - T - B); };
    var grid = "", ticks = "";
    for (var v = 0; v <= top; v += step) {
      grid += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y(v) + '" y2="' + y(v) + '" class="gridline"/>';
      ticks += '<text x="' + (L - 8) + '" y="' + (y(v) + 4) + '" class="tick" text-anchor="end">' + fmt(v) + "</text>";
    }
    var every = Math.max(1, Math.ceil(n / 8));
    for (var i = 0; i < n; i += every) {
      ticks += '<text x="' + x(i) + '" y="' + (H - 8) + '" class="tick" text-anchor="middle">' + dayPl(daily[i].day) + "</text>";
    }
    var pts = daily.map(function (d, i) { return x(i).toFixed(1) + "," + y(d.count).toFixed(1); });
    var area = "M" + x(0) + "," + y(0) + " L" + pts.join(" L") + " L" + x(n - 1) + "," + y(0) + " Z";
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '" class="line-svg" role="img" aria-label="Odwiedziny dziennie">' +
      grid + '<path d="' + area + '" class="area"/><polyline points="' + pts.join(" ") + '" class="line"/>' + ticks +
      '<line class="cross" y1="' + T + '" y2="' + y(0) + '" x1="0" x2="0" visibility="hidden"/>' +
      '<circle class="cross-dot" r="5" cx="0" cy="0" visibility="hidden"/>' +
      '<rect class="hit" x="' + L + '" y="0" width="' + (W - L - R) + '" height="' + H + '"/></svg>';
    var sum30 = daily.slice(-30).reduce(function (a, d) { return a + d.count; }, 0);
    var html = '<section class="chart-card wide"><h3>Odwiedziny dzień po dniu</h3><p class="chart-note">Ostatnie ' + n +
      " dni · w ostatnich 30 dniach " + fmt(sum30) + '</p><div class="line-wrap">' + svg +
      '<div class="tip" hidden></div></div>' +
      table(daily.slice().reverse().map(function (d) { return { name: d.day, count: d.count }; }), ["Dzień", "Odwiedziny"]) + "</section>";
    return { html: html, bind: function (root) {
      var s = root.querySelector(".line-svg"), tip = root.querySelector(".tip");
      var cross = s.querySelector(".cross"), dot = s.querySelector(".cross-dot"), hit = s.querySelector(".hit");
      function show(ev) {
        var r = s.getBoundingClientRect();
        var px = (ev.clientX - r.left) * (W / r.width);
        var i = Math.round(((px - L) / (W - L - R)) * (n - 1));
        i = Math.max(0, Math.min(n - 1, i));
        cross.setAttribute("x1", x(i)); cross.setAttribute("x2", x(i)); cross.setAttribute("visibility", "visible");
        dot.setAttribute("cx", x(i)); dot.setAttribute("cy", y(daily[i].count)); dot.setAttribute("visibility", "visible");
        tip.hidden = false;
        tip.innerHTML = "<b>" + fmt(daily[i].count) + "</b> odwiedzin<br><span>" +
          new Date(daily[i].day + "T00:00:00").toLocaleDateString("pl-PL", { weekday: "long", day: "numeric", month: "long" }) + "</span>";
        var left = (x(i) / W) * r.width;
        tip.style.left = Math.min(Math.max(left, 70), r.width - 70) + "px";
      }
      function hide() { tip.hidden = true; cross.setAttribute("visibility", "hidden"); dot.setAttribute("visibility", "hidden"); }
      hit.addEventListener("mousemove", show);
      hit.addEventListener("touchstart", function (e) { show(e.touches[0]); }, { passive: true });
      hit.addEventListener("mouseleave", hide);
    } };
  }

  /* ---------- całość ---------- */
  function render(d) {
    var pages = (d.pages || []).filter(function (p) { return p.count > 0; });
    var daily = (d.daily || []).filter(function (x) { return x.day; });
    var total = d.total || pages.reduce(function (a, p) { return a + p.count; }, 0);
    if (!total && !daily.some(function (x) { return x.count > 0; })) {
      empty("Licznik działa od " + (d.since || "listopada 2026") + ". Pierwsze wykresy pojawią się, gdy zbierzemy pierwsze odwiedziny.");
      return;
    }
    var last = function (k) { return daily.slice(-k).reduce(function (a, x) { return a + x.count; }, 0); };
    var best = daily.reduce(function (a, x) { return x.count > a.count ? x : a; }, { count: 0 });
    var arkusze = pages.filter(function (p) { return category(p.path) === "Arkusze maturalne" && !/arkusze\.html$/.test(p.path); });
    var algos = pages.filter(function (p) { return /algorytmy|dodatkowe/.test(category(p.path)); });

    var cats = {};
    pages.forEach(function (p) { var c = category(p.path); cats[c] = (cats[c] || 0) + p.count; });
    var catRows = Object.keys(cats).map(function (k) { return { name: k, count: cats[k] }; })
      .sort(function (a, b) { return b.count - a.count; });

    var tiles = [
      ["Odwiedzin łącznie", fmt(total), "od " + new Date((d.since || "2026-11-01") + "T00:00:00").toLocaleDateString("pl-PL", { day: "numeric", month: "long", year: "numeric" })],
      ["Ostatnie 30 dni", fmt(last(30)), "średnio " + fmt(Math.round(last(30) / Math.max(1, Math.min(30, daily.length)))) + " dziennie"],
      ["Ostatnie 7 dni", fmt(last(7)), "wczoraj i dziś: " + fmt(last(2))],
      ["Rekordowy dzień", fmt(best.count), best.day ? new Date(best.day + "T00:00:00").toLocaleDateString("pl-PL", { day: "numeric", month: "long" }) : "—"]
    ];
    var html = '<div class="stats-grid">' + tiles.map(function (t) {
      return '<div class="stat accent"><span class="stat-num">' + t[1] + '</span><span class="stat-label">' + t[0] +
        '</span><span class="stat-sub">' + esc(t[2]) + "</span></div>";
    }).join("") + "</div>";

    var line = daily.length ? lineChart(daily) : null;
    if (line) html += line.html;

    var toRows = function (list) { return (list || []).map(function (s) { return { name: s.name, count: s.count }; }); };
    var pageRows = function (list) { return list.map(function (p) { return { name: pageLabel(p), count: p.count, href: pageHref(p.path) }; }); };

    html += '<div class="charts">' +
      bars("Działy", catRows, { share: true, total: total, note: "Które części strony są najczęściej odwiedzane" }) +
      bars("Najpopularniejsze strony", pageRows(pages), { limit: 12 }) +
      bars("Najczęściej otwierane arkusze", pageRows(arkusze), { limit: 10 }) +
      bars("Najczęściej czytane algorytmy", pageRows(algos), { limit: 10 }) +
      bars("Skąd przychodzą odwiedzający", toRows(d.toprefs), { limit: 10, note: "Strony i wyszukiwarki, z których kliknięto link" }) +
      bars("Urządzenia (szerokość ekranu)", toRows(d.sizes), { share: true }) +
      bars("Kraje", toRows(d.locations), { limit: 10, share: true }) +
      bars("Przeglądarki", toRows(d.browsers), { limit: 8, share: true }) +
      bars("Systemy operacyjne", toRows(d.systems), { limit: 8, share: true }) +
      bars("Języki przeglądarki", toRows(d.languages), { limit: 8, share: true }) +
      "</div>";
    if (d.generated_at) {
      html += '<p class="source">Ostatnia aktualizacja: ' + new Date(d.generated_at).toLocaleString("pl-PL", { dateStyle: "long", timeStyle: "short" }) + ".</p>";
    }
    box.innerHTML = html;
    if (line) line.bind(box);
  }
})();
