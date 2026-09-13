/* ==========================================================================
   SPEEDLAB — tests/whack-a-mole.js
   Whack-a-Mole: a 3x3 grid, moles pop up one at a time for a short window,
   click them before they disappear. Count your hits in 30 seconds.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 30, HOLES = 9;

  function init() {
    var root = $("whack");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.whack;
    var screen = $("screen"), play = $("play"), grid = $("grid"), result = $("result");
    var startBtn = $("startBtn"), hitsEl = $("hits"), timerEl = $("timer");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");
    var storageKey = "whack", testName = "Whack-a-Mole";

    var holes = grid.querySelectorAll(".mole-hole");
    var state = "idle", hits = 0, active = -1, startTs = 0;
    var raf = 0, moleTimer = 0, endTimer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " hits";
    }
    function clearActive() {
      if (active >= 0) holes[active].classList.remove("up");
      active = -1;
    }
    function popNext() {
      clearActive();
      if (state !== "running") return;
      var idx;
      do { idx = Math.floor(Math.random() * HOLES); } while (idx === active);
      active = idx; holes[idx].classList.add("up");
      // window shrinks slightly as time passes to ramp difficulty
      var elapsed = (performance.now() - startTs) / 1000;
      var win = Math.max(550, 1050 - elapsed * 15);
      moleTimer = setTimeout(popNext, win);
    }
    function onHole(i) {
      return function (e) {
        e.preventDefault();
        if (state !== "running" || i !== active) return;
        hits++; hitsEl.textContent = hits; S.sound.click();
        clearTimeout(moleTimer);
        holes[i].classList.remove("up"); active = -1;
        setTimeout(popNext, 90);
      };
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function begin() {
      state = "running"; hits = 0; startTs = performance.now();
      hitsEl.textContent = "0"; startBtn.hidden = true; restart.hidden = false;
      endTimer = setTimeout(finish, DURATION * 1000);
      tick(); popNext();
    }
    function finish() {
      state = "done";
      cancelAnimationFrame(raf); clearTimeout(moleTimer); clearTimeout(endTimer);
      clearActive();
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: hits, formatted: String(hits),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; hits = 0;
      cancelAnimationFrame(raf); clearTimeout(moleTimer); clearTimeout(endTimer);
      clearActive();
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true;
      hitsEl.textContent = "0"; timerEl.textContent = DURATION;
    }

    Array.prototype.forEach.call(holes, function (h, i) {
      h.addEventListener("pointerdown", onHole(i));
    });
    startBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); begin(); });
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
