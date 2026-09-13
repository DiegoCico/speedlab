/* ==========================================================================
   SPEEDLAB — site.js
   Wires shared header controls (sound toggle), records the visit streak, and
   renders the homepage daily-challenge card + streak count when present.
   Test pages do the sound/streak wiring inside their own script.
   ========================================================================== */
(function () {
  "use strict";

  function renderDaily() {
    var el = document.getElementById("daily");
    if (!el || !window.SPEEDLAB) return;
    // data-tests="slug:Name,slug:Name" — only built tests, so the pick is valid.
    var pairs = (el.getAttribute("data-tests") || "").split(",")
      .map(function (s) { return s.trim(); }).filter(Boolean)
      .map(function (s) { var i = s.indexOf(":"); return { slug: s.slice(0, i), name: s.slice(i + 1) }; });
    if (!pairs.length) return;
    var slugs = pairs.map(function (p) { return p.slug; });
    var pick = SPEEDLAB.dailyChallenge(slugs) || slugs[0];
    var chosen = pairs.filter(function (p) { return p.slug === pick; })[0] || pairs[0];

    var nameEl = el.querySelector("[data-daily-name]");
    var linkEl = el.querySelector("[data-daily-link]");
    if (nameEl) nameEl.textContent = chosen.name;
    if (linkEl) linkEl.setAttribute("href", "/" + chosen.slug + "/");

    var streak = SPEEDLAB.streak.get();
    var streakEl = document.getElementById("streakCount");
    if (streakEl) {
      streakEl.textContent = streak;
      var lbl = document.getElementById("streakLabel");
      if (lbl) lbl.textContent = streak === 1 ? "day streak" : "day streak";
    }
  }

  function init() {
    if (!window.SPEEDLAB) return;
    SPEEDLAB.sound.initToggle(document.getElementById("soundToggle"));
    SPEEDLAB.streak.record();
    renderDaily();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
