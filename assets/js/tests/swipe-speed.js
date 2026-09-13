/* ==========================================================================
   SPEEDLAB — tests/swipe-speed.js
   Swipe Speed Test: swipe across the pad as fast as you can for 10 seconds.
   Every chunk of swipe movement counts as one swipe, so back-and-forth
   flicking works too. Score is the number of swipes. Mouse or touch.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 10, THRESH = 80;

  function init() {
    var root = $("swipespeed");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.swipe;
    var storageKey = "swipe", testName = "Swipe Speed Test";
    var screen = $("screen"), play = $("play"), result = $("result");
    var pad = $("pad"), countEl = $("count"), timerEl = $("timer"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", count = 0, startTs = 0, raf = 0, endTimer = 0;
    var down = false, ax = 0, ay = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " swipes";
    }
    function begin() {
      state = "running"; count = 0; startTs = performance.now();
      restart.hidden = false; endTimer = setTimeout(finish, DURATION * 1000); tick();
    }
    function addSwipe() {
      if (state === "done") return;
      if (state === "idle") begin();
      count++; countEl.textContent = count; S.sound.click();
      if (!S.reduceMotion) { pad.classList.add("flash"); setTimeout(function () { pad.classList.remove("flash"); }, 70); }
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer); down = false;
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: count, formatted: String(count),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; count = 0; down = false; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; countEl.textContent = "0"; timerEl.textContent = DURATION;
    }

    pad.addEventListener("pointerdown", function (e) { e.preventDefault(); down = true; ax = e.clientX; ay = e.clientY; });
    pad.addEventListener("pointermove", function (e) {
      if (!down) return;
      var dx = e.clientX - ax, dy = e.clientY - ay;
      if (Math.sqrt(dx * dx + dy * dy) >= THRESH) { addSwipe(); ax = e.clientX; ay = e.clientY; }
    });
    function up() { down = false; }
    pad.addEventListener("pointerup", up);
    pad.addEventListener("pointercancel", up);
    pad.addEventListener("pointerleave", up);
    restart.addEventListener("click", reset);
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    reset(); paintPB();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
