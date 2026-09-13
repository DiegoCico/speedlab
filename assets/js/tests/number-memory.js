/* ==========================================================================
   SPEEDLAB — tests/number-memory.js
   Number Memory: a number flashes, then hides — type it back. Each round the
   number gets one digit longer. Score is how many digits you recall.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("numbermemory");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.numbermemory;
    var storageKey = "numbermemory", testName = "Number Memory";
    var screen = $("screen"), play = $("play"), result = $("result");
    var startWrap = $("startWrap"), phaseShow = $("phaseShow"), phaseInput = $("phaseInput");
    var numDisplay = $("numDisplay"), bar = $("bar"), input = $("numInput");
    var levelEl = $("level"), feedback = $("feedback"), restart = $("restart");
    var startBtn = $("startBtn"), submitBtn = $("submitBtn");
    var pbValEl = document.querySelector("[data-pb]");

    var level = 1, current = "", state = "idle", t = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " digits";
    }
    function genNumber(digits) {
      var s = String(1 + Math.floor(Math.random() * 9));
      for (var i = 1; i < digits; i++) s += Math.floor(Math.random() * 10);
      return s;
    }
    function showLevel() {
      current = genNumber(level);
      levelEl.textContent = level;
      startWrap.hidden = true; phaseInput.hidden = true; phaseShow.hidden = false;
      numDisplay.textContent = current;
      var showTime = 1000 + (level - 1) * 300;
      bar.style.transition = "none"; bar.style.width = "100%"; void bar.offsetWidth;
      bar.style.transition = "width " + showTime + "ms linear"; bar.style.width = "0%";
      state = "show";
      clearTimeout(t); t = setTimeout(toInput, showTime);
    }
    function toInput() {
      state = "input";
      phaseShow.hidden = true; phaseInput.hidden = false;
      input.value = ""; feedback.textContent = ""; feedback.className = "mem-feedback";
      input.focus();
    }
    function submit() {
      if (state !== "input") return;
      if (input.value === current) { level++; showLevel(); }
      else { gameOver(); }
    }
    function begin() { level = 1; restart.hidden = false; showLevel(); }
    function gameOver() {
      state = "done";
      var score = level - 1;      // digits successfully recalled
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: score, formatted: String(score),
        screen: screen, onRestart: reset
      });
      var p = document.createElement("p"); p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = "The number was " + current;
      result.appendChild(p);
      paintPB();
    }
    function reset() {
      clearTimeout(t); state = "idle"; level = 1;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startWrap.hidden = false; phaseShow.hidden = true; phaseInput.hidden = true;
      restart.hidden = true; levelEl.textContent = 1;
    }

    startBtn.addEventListener("click", begin);
    submitBtn.addEventListener("click", submit);
    input.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); submit(); } });
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
