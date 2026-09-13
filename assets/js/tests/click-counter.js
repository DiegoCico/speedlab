/* ==========================================================================
   SPEEDLAB — tests/click-counter.js
   A plain tally counter. No timer, no rank — people use these for real tasks
   (counting laps, people, reps...). The count saves automatically per device.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("clickcounter");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB;
    var countEl = $("count"), pad = $("pad"), minus = $("minus"), reset = $("reset");
    var KEY = "counter:value";
    var n = parseInt(S.store.get(KEY) || "0", 10) || 0;

    function paint() {
      countEl.textContent = n;
      if (!S.reduceMotion) { countEl.classList.remove("tick"); void countEl.offsetWidth; countEl.classList.add("tick"); }
    }
    function change(d) { n = Math.max(0, n + d); paint(); S.store.set(KEY, String(n)); S.sound.click(); }

    pad.addEventListener("pointerdown", function (e) { e.preventDefault(); change(1); pad.classList.add("is-pressed"); });
    pad.addEventListener("pointerup", function () { pad.classList.remove("is-pressed"); });
    pad.addEventListener("pointercancel", function () { pad.classList.remove("is-pressed"); });
    pad.addEventListener("keydown", function (e) {
      if (e.key === " " || e.key === "Enter" || e.code === "Space") { e.preventDefault(); if (e.repeat) return; change(1); }
    });
    pad.addEventListener("keyup", function () { pad.classList.remove("is-pressed"); });
    minus.addEventListener("click", function () { change(-1); });
    reset.addEventListener("click", function () { n = 0; paint(); S.store.set(KEY, "0"); });

    paint();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
