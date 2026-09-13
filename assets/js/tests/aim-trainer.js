/* ==========================================================================
   SPEEDLAB — tests/aim-trainer.js
   Aim Trainer: 30 targets appear one at a time at random spots. Click them
   all as fast as you can; score is the average milliseconds per target.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var TOTAL = 30, SIZE = 54;

  function init() {
    var root = $("aim");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.aim;
    var screen = $("screen"), play = $("play"), arena = $("arena"), result = $("result");
    var startBtn = $("startTarget"), remainingEl = $("remaining"), avgEl = $("avg");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");
    var storageKey = "aim", testName = "Aim Trainer";

    var state = "idle", hits = 0, startTs = 0, target = null;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " ms";
    }
    function place() {
      var r = arena.getBoundingClientRect();
      var maxX = Math.max(0, r.width - SIZE), maxY = Math.max(0, r.height - SIZE);
      target.style.left = Math.round(Math.random() * maxX) + "px";
      target.style.top = Math.round(Math.random() * maxY) + "px";
    }
    function spawn() {
      if (!target) {
        target = document.createElement("button");
        target.type = "button"; target.className = "aim-target";
        target.setAttribute("aria-label", "Target");
        target.addEventListener("pointerdown", onHit);
        arena.appendChild(target);
      }
      place();
    }
    function onHit(e) {
      e.preventDefault(); e.stopPropagation();
      if (state !== "running") return;
      hits++; S.sound.click();
      remainingEl.textContent = Math.max(0, TOTAL - hits);
      avgEl.textContent = Math.round((performance.now() - startTs) / hits);
      if (hits >= TOTAL) finish(); else place();
    }
    function begin() {
      state = "running"; hits = 0; startTs = performance.now();
      startBtn.hidden = true; restart.hidden = false;
      remainingEl.textContent = TOTAL; avgEl.textContent = 0;
      spawn();
    }
    function finish() {
      state = "done";
      if (target) { target.remove(); target = null; }
      play.hidden = true;
      var avg = (performance.now() - startTs) / TOTAL;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: avg, formatted: String(Math.round(avg)),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; hits = 0;
      if (target) { target.remove(); target = null; }
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true;
      remainingEl.textContent = TOTAL; avgEl.textContent = 0;
    }

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
