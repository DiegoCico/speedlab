/* ==========================================================================
   SPEEDLAB — tests/word-spammer.js
   Word Spammer: pick your own word, then type it over and over as fast as you
   can before the clock runs out (5 / 10 / 30 / 60 s). Score is your rep count,
   ranked by the equivalent WPM so any word length compares fairly.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("wordspam");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.wordspam;
    var storageKey = "wordspam", testName = "Word Spammer";
    var screen = $("screen"), play = $("play"), result = $("result");
    var setup = $("setup"), active = $("active");
    var wordInput = $("wordInput"), startBtn = $("startBtn");
    var targetEl = $("target"), typeInput = $("typeInput");
    var repsEl = $("reps"), timerEl = $("timer");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");
    var durWrap = $("durSelect");

    var DURATION = 10, word = "", reps = 0, state = "setup", startTs = 0, raf = 0, endTimer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " WPM";
    }
    function setDur(d) {
      DURATION = d;
      Array.prototype.forEach.call(durWrap.querySelectorAll(".opt"), function (b) {
        b.setAttribute("aria-pressed", String(Number(b.dataset.dur) === d));
      });
      if (state === "setup") timerEl.textContent = d;
    }
    function tick() {
      if (state !== "running") return;
      var left = Math.max(0, DURATION - (performance.now() - startTs) / 1000);
      timerEl.textContent = Math.ceil(left);
      raf = requestAnimationFrame(tick);
    }
    function begin() {
      word = (wordInput.value || "").trim();
      if (!word) { wordInput.focus(); return; }
      state = "running"; reps = 0; repsEl.textContent = "0";
      setup.hidden = true; active.hidden = false; restart.hidden = false;
      targetEl.textContent = word; typeInput.value = ""; typeInput.disabled = false;
      startTs = performance.now(); endTimer = setTimeout(finish, DURATION * 1000);
      tick(); typeInput.focus();
    }
    function onType() {
      if (state !== "running") return;
      var v = typeInput.value;
      if (v === word) {
        reps++; repsEl.textContent = reps; typeInput.value = "";
        typeInput.classList.remove("flash-bad"); typeInput.classList.remove("flash-good");
        void typeInput.offsetWidth; typeInput.classList.add("flash-good");
        S.sound.click();
      } else if (v.length && word.indexOf(v) !== 0) {
        // typed something that isn't a valid prefix of the word
        typeInput.classList.remove("flash-bad"); void typeInput.offsetWidth; typeInput.classList.add("flash-bad");
      }
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer);
      typeInput.disabled = true; typeInput.blur(); play.hidden = true;
      var chars = reps * word.length;
      var wpm = Math.round((chars / 5) / (DURATION / 60));
      var line = "Typed “" + word + "” " + reps + " time" + (reps === 1 ? "" : "s") + " in " + DURATION + "s";
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: wpm, formatted: wpm + " WPM",
        sub: DURATION + "s", detail: line,
        screen: screen, onRestart: reset
      });
      var p = document.createElement("p");
      p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = line;
      result.appendChild(p);
      paintPB();
    }
    function reset() {
      state = "setup"; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      setup.hidden = false; active.hidden = true; restart.hidden = true;
      reps = 0; repsEl.textContent = "0"; timerEl.textContent = DURATION;
      typeInput.value = ""; typeInput.disabled = true;
      wordInput.focus();
    }

    startBtn.addEventListener("click", begin);
    wordInput.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); begin(); } });
    typeInput.addEventListener("input", onType);
    restart.addEventListener("click", reset);
    Array.prototype.forEach.call(durWrap.querySelectorAll(".opt"), function (b) {
      b.addEventListener("click", function () { setDur(Number(b.dataset.dur)); });
    });
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    setDur(DURATION); reset(); paintPB();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
