/* ==========================================================================
   SPEEDLAB — tests/math-sprint.js
   Mental Math Sprint: solve as many quick arithmetic problems as you can in
   60 seconds. Answer auto-checks as you type; score is correct answers.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 60;

  function makeProblem() {
    var ops = ["+", "-", "×"], op = ops[Math.floor(Math.random() * ops.length)], a, b, ans;
    if (op === "+") { a = 2 + Math.floor(Math.random() * 98); b = 2 + Math.floor(Math.random() * 98); ans = a + b; }
    else if (op === "-") { a = 5 + Math.floor(Math.random() * 95); b = 1 + Math.floor(Math.random() * (a - 1)); ans = a - b; }
    else { a = 2 + Math.floor(Math.random() * 11); b = 2 + Math.floor(Math.random() * 11); ans = a * b; }
    return { text: a + " " + op + " " + b, ans: ans };
  }

  function init() {
    var root = $("mathsprint");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.mathsprint;
    var storageKey = "mathsprint", testName = "Mental Math";
    var screen = $("screen"), play = $("play"), result = $("result");
    var problemEl = $("problem"), input = $("answer"), correctEl = $("correct"), timerEl = $("timer");
    var startBtn = $("startBtn"), restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var state = "idle", correct = 0, startTs = 0, raf = 0, endTimer = 0, cur = null;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " correct";
    }
    function nextProblem() { cur = makeProblem(); problemEl.textContent = cur.text + " ="; input.value = ""; }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function begin() {
      state = "running"; correct = 0; correctEl.textContent = "0";
      startBtn.hidden = true; restart.hidden = false; input.disabled = false;
      startTs = performance.now(); endTimer = setTimeout(finish, DURATION * 1000);
      tick(); nextProblem(); input.focus();
    }
    function onInput() {
      if (state !== "running" || !cur) return;
      if (input.value === String(cur.ans)) {
        correct++; correctEl.textContent = correct; S.sound.click(); nextProblem();
      }
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer); input.disabled = true; input.blur();
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
      startBtn.hidden = false; restart.hidden = true;
      correctEl.textContent = "0"; timerEl.textContent = DURATION;
      problemEl.textContent = "7 × 8 ="; input.value = ""; input.disabled = true;
    }

    startBtn.addEventListener("click", begin);
    input.addEventListener("input", onInput);
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
