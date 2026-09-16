/* ==========================================================================
   SPEEDLAB — tests/subitize.js
   Count the Flash (subitizing): dots flash on screen for a split second, then
   you type how many there were. Each level adds a dot and shortens the flash.
   One wrong answer ends the run; score is the level you reached (higher wins).
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function dotsFor(level) {
    // Centre grows with level, but the exact count jiggles ±2 so no two runs
    // (and no two players' level 1) are the same. Never below 1 dot.
    var center = level + 2;
    var spread = Math.floor(Math.random() * 5) - 2;   // -2 .. +2
    return Math.max(1, center + spread);
  }
  function flashFor(level) { return Math.max(240, 950 - level * 55); } // ms

  function init() {
    var root = $("subitize");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.subitize;
    var storageKey = "subitize", testName = "Count the Flash";
    var screen = $("screen"), play = $("play"), result = $("result");
    var field = $("field"), promptEl = $("prompt"), levelEl = $("level");
    var input = $("answer"), checkBtn = $("checkBtn"), startBtn = $("startBtn");
    var inputRow = $("inputRow"), restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var level = 1, cleared = 0, count = 0, state = "idle", flashTimer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : "Level " + Math.round(pb);
    }
    function placeDots(n) {
      field.innerHTML = "";
      for (var i = 0; i < n; i++) {
        var d = document.createElement("div");
        d.className = "subit-dot";
        d.style.left = (10 + Math.random() * 80) + "%";
        d.style.top = (12 + Math.random() * 76) + "%";
        field.appendChild(d);
      }
    }
    function showInput(show) {
      inputRow.hidden = !show;
      input.disabled = !show;
      if (show) { input.value = ""; input.focus(); }
    }
    function runRound() {
      state = "watch";
      count = dotsFor(level);
      levelEl.textContent = level;
      promptEl.textContent = "Watch…";
      showInput(false); startBtn.hidden = true;
      placeDots(count);
      clearTimeout(flashTimer);
      flashTimer = setTimeout(function () {
        field.innerHTML = "";
        promptEl.textContent = "How many dots?";
        state = "answer";
        showInput(true);
      }, flashFor(level));
    }
    function submit() {
      if (state !== "answer") return;
      var val = parseInt(input.value, 10);
      if (isNaN(val)) { input.focus(); return; }
      if (val === count) {
        cleared = level; level++; S.sound.click();
        promptEl.textContent = "Correct! " + count + " dots.";
        showInput(false);
        state = "between";
        setTimeout(runRound, 650);
      } else {
        finish(val);
      }
    }
    function finish(guess) {
      state = "done"; clearTimeout(flashTimer); play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: cleared, formatted: "Level " + cleared,
        detail: "Missed at " + count + " dots (you said " + guess + ")",
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      clearTimeout(flashTimer);
      level = 1; cleared = 0; count = 0; state = "idle";
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; field.innerHTML = "";
      levelEl.textContent = "1"; promptEl.textContent = "Count the dots that flash.";
      showInput(false); startBtn.hidden = false;
    }
    function begin() { restart.hidden = false; runRound(); }

    startBtn.addEventListener("click", begin);
    checkBtn.addEventListener("click", submit);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { e.preventDefault(); submit(); }
    });
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
