/* ==========================================================================
   SPEEDLAB — tests/sequence-memory.js
   Sequence Memory (Simon-style): watch a pattern of cells light up, then
   repeat it. The pattern grows by one each round. Score is how far you get.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var TONES = [262, 294, 330, 349, 392, 440, 494, 523, 587];

  function init() {
    var root = $("sequencemem");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.sequencemem;
    var storageKey = "sequencemem", testName = "Sequence Memory";
    var screen = $("screen"), play = $("play"), result = $("result");
    var grid = $("grid"), startWrap = $("startWrap"), startBtn = $("startBtn");
    var levelEl = $("level"), statusEl = $("status"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");
    var cells = grid.querySelectorAll(".mem-cell");

    var seq = [], userIdx = 0, level = 0, state = "idle", t = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " level";
    }
    function flash(i, cls, dur, cb) {
      cells[i].classList.add(cls);
      S.sound.tone(TONES[i % TONES.length], 0.18, "sine", 0.06);
      setTimeout(function () { cells[i].classList.remove(cls); if (cb) setTimeout(cb, 140); }, dur);
    }
    function playSeq() {
      state = "watch"; statusEl.textContent = "Watch…";
      var i = 0;
      (function step() {
        if (i >= seq.length) { state = "input"; userIdx = 0; statusEl.textContent = "Your turn"; return; }
        flash(seq[i], "lit", 380, function () { i++; step(); });
      })();
    }
    function nextRound() {
      level++; levelEl.textContent = level;
      seq.push(Math.floor(Math.random() * cells.length));
      clearTimeout(t); t = setTimeout(playSeq, 500);
    }
    function begin() { seq = []; level = 0; startWrap.hidden = true; restart.hidden = false; nextRound(); }
    function onCell(i) {
      if (state !== "input") return;
      if (i === seq[userIdx]) {
        flash(i, "good", 180); userIdx++;
        if (userIdx >= seq.length) { state = "between"; statusEl.textContent = "Nice!"; clearTimeout(t); t = setTimeout(nextRound, 650); }
      } else { flash(i, "bad", 300); gameOver(); }
    }
    function gameOver() {
      state = "done";
      var score = level - 1;   // rounds completed before the miss
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: score, formatted: String(score),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      clearTimeout(t); state = "idle"; seq = []; level = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startWrap.hidden = false; restart.hidden = true;
      levelEl.textContent = 0; statusEl.textContent = "";
    }

    Array.prototype.forEach.call(cells, function (c, i) {
      c.addEventListener("pointerdown", function (e) { e.preventDefault(); onCell(i); });
    });
    startBtn.addEventListener("click", begin);
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
