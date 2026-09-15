/* ==========================================================================
   SPEEDLAB — tests/go-no-go.js
   Go / No-Go: tap on GREEN (Go), hold still on RED (No-Go). 25 trials measuring
   impulse control. Score is how many you get right (higher is better).
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var TRIALS = 25, GO_PROB = 0.7, WINDOW = 1000;

  function init() {
    var root = $("gonogo");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.gonogo;
    var storageKey = "gonogo", testName = "Go / No-Go";
    var screen = $("screen"), play = $("play"), result = $("result");
    var stage = $("stage"), labelEl = $("stageLabel"), subEl = $("stageSub");
    var trialEl = $("trial"), correctEl = $("correct");
    var startBtn = $("startBtn"), restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var state = "idle", trial = 0, correct = 0, stimTimer = 0, gapTimer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " / " + TRIALS;
    }
    function setStage(cls, label, sub) {
      stage.className = "gng-stage" + (cls ? " " + cls : "");
      labelEl.textContent = label; subEl.textContent = sub || "";
    }
    function nextTrial() {
      if (trial >= TRIALS) { finish(); return; }
      trial++; trialEl.textContent = trial + "/" + TRIALS;
      state = "fixation"; setStage("", "+", "Get ready…");
      clearTimeout(gapTimer);
      gapTimer = setTimeout(showStimulus, 450 + Math.random() * 750);
    }
    function showStimulus() {
      var isGo = Math.random() < GO_PROB;
      state = isGo ? "go" : "nogo";
      if (isGo) setStage("go", "TAP!", "Green — go");
      else setStage("nogo", "STOP", "Red — don't tap");
      clearTimeout(stimTimer);
      stimTimer = setTimeout(windowEnd, WINDOW);
    }
    function resolve(good, label, sub) {
      if (good) { correct++; correctEl.textContent = correct; S.sound.click(); }
      setStage(good ? "ok" : "bad", label, sub);
      state = "between";
      clearTimeout(stimTimer);
      clearTimeout(gapTimer);
      gapTimer = setTimeout(nextTrial, 450);
    }
    function onTap() {
      if (state === "go") resolve(true, "Good!", "");
      else if (state === "nogo") resolve(false, "Oops", "That was a No-Go");
      // taps during fixation / between are ignored
    }
    function windowEnd() {
      if (state === "go") resolve(false, "Too slow", "You missed a Go");
      else if (state === "nogo") resolve(true, "Nice hold", "");
    }
    function finish() {
      state = "done"; clearTimeout(stimTimer); clearTimeout(gapTimer); play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: correct, formatted: correct + " / " + TRIALS,
        detail: correct + " correct out of " + TRIALS + " trials",
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      clearTimeout(stimTimer); clearTimeout(gapTimer);
      state = "idle"; trial = 0; correct = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true;
      trialEl.textContent = "0/" + TRIALS; correctEl.textContent = "0";
      setStage("", "Go / No-Go", "Tap on green, hold still on red.");
      startBtn.hidden = false;
    }
    function begin() { startBtn.hidden = true; restart.hidden = false; nextTrial(); }

    startBtn.addEventListener("click", function (e) { e.stopPropagation(); begin(); });
    stage.addEventListener("pointerdown", function (e) {
      if (e.target === startBtn) return;
      e.preventDefault(); onTap();
    });
    stage.addEventListener("contextmenu", function (e) { e.preventDefault(); });
    document.addEventListener("keydown", function (e) {
      if (e.key !== " " && e.key !== "Enter" && e.code !== "Space") return;
      var ae = document.activeElement;
      if (ae && /^(A|SUMMARY|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      if (state === "idle" || state === "done") return;
      e.preventDefault(); if (e.repeat) return; onTap();
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
