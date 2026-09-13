/* ==========================================================================
   SPEEDLAB — tests/stroop.js
   Color Match (Stroop Test): a colour word is shown in some ink colour. Answer
   whether the ink colour matches what the word says, as fast as you can.
   Score is the number of correct answers in 30 seconds.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 30;
  var COLORS = [
    ["red", "#E5484D"], ["green", "#2BE86B"], ["blue", "#00C2FF"],
    ["yellow", "#FFC531"], ["pink", "#FF3D7F"], ["purple", "#B36BFF"]
  ];

  function init() {
    var root = $("stroop");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.stroop;
    var storageKey = "stroop", testName = "Color Match";
    var screen = $("screen"), play = $("play"), result = $("result"), area = $("area");
    var wordEl = $("word"), correctEl = $("correct"), timerEl = $("timer");
    var startBtn = $("startBtn"), matchBtn = $("matchBtn"), noBtn = $("noBtn"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", correct = 0, startTs = 0, raf = 0, endTimer = 0, curMatch = false;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " correct";
    }
    function setEnabled(on) { matchBtn.disabled = !on; noBtn.disabled = !on; }
    function nextPrompt() {
      var wi = Math.floor(Math.random() * COLORS.length);
      var ii = Math.random() < 0.5 ? wi : Math.floor(Math.random() * COLORS.length);
      curMatch = (wi === ii);
      wordEl.textContent = COLORS[wi][0].toUpperCase();
      wordEl.style.color = COLORS[ii][1];
    }
    function flash(good) {
      if (S.reduceMotion) return;
      area.classList.remove("flash-good", "flash-bad");
      void area.offsetWidth;
      area.classList.add(good ? "flash-good" : "flash-bad");
    }
    function answer(said) {
      if (state !== "running") return;
      if (said === curMatch) { correct++; correctEl.textContent = correct; S.sound.click(); flash(true); }
      else { flash(false); }
      nextPrompt();
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function begin() {
      state = "running"; correct = 0; correctEl.textContent = "0"; startTs = performance.now();
      startBtn.hidden = true; restart.hidden = false; setEnabled(true);
      endTimer = setTimeout(finish, DURATION * 1000);
      tick(); nextPrompt();
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer); setEnabled(false);
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: correct, formatted: String(correct),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; correct = 0; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true; setEnabled(false);
      correctEl.textContent = "0"; timerEl.textContent = DURATION;
      wordEl.textContent = "READY"; wordEl.style.color = "var(--c-ink)";
    }

    startBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); begin(); });
    matchBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); answer(true); });
    noBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); answer(false); });
    restart.addEventListener("click", reset);
    document.addEventListener("keydown", function (e) {
      if (state !== "running") return;
      if (e.key === "ArrowLeft" || e.key === "1") { e.preventDefault(); answer(true); }
      else if (e.key === "ArrowRight" || e.key === "2") { e.preventDefault(); answer(false); }
    });
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
