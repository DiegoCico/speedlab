/* ==========================================================================
   SPEEDLAB — tests/reaction.js
   Reaction Time Test: red screen, wait, turns green, click as fast as you can.
   Five attempts, averaged. Clicking during red is "too soon" and doesn't count.
   Uses the shared result flow (lower ms is better).
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var NEEDED = 5;

  function init() {
    var root = $("reaction");
    if (!root || !window.SPEEDLAB) return;

    var conf = SPEEDLAB.config.reaction;
    var storageKey = "reaction";
    var testName = "Reaction Time Test";

    var stage = $("stage"), title = $("stageTitle"), sub = $("stageSub");
    var play = $("play"), result = $("result"), slotsEl = $("slots"), screen = $("screen");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", attempts = [], goTime = 0, timer = 0;

    function paintPB() {
      var pb = SPEEDLAB.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " ms";
    }
    function buildSlots() {
      var html = "";
      for (var i = 0; i < NEEDED; i++) {
        var v = attempts[i];
        html += '<div class="react-slot' + (v != null ? " filled" : "") + '">' +
          '<span class="n">' + (v != null ? v : "—") + '</span>' +
          (i + 1) + '</div>';
      }
      slotsEl.innerHTML = html;
    }
    function setStage(cls, t, s) {
      stage.className = "react-stage" + (cls ? " " + cls : "");
      title.textContent = t; sub.textContent = s || "";
    }

    function toIdle() {
      state = "idle";
      var n = attempts.length;
      setStage("", n ? "Ready?" : "Click to start",
        n ? ("Attempt " + (n + 1) + " of " + NEEDED) : "Wait for green, then click. " + NEEDED + " tries.");
    }
    function beginAttempt() {
      state = "waiting";
      setStage("is-wait", "Wait for green…", "Don't click yet");
      var delay = 1200 + Math.random() * 3200;
      clearTimeout(timer);
      timer = setTimeout(goGreen, delay);
    }
    function goGreen() {
      state = "go"; goTime = performance.now();
      setStage("is-go", "Click!", "");
    }
    function tooSoon() {
      clearTimeout(timer); state = "early";
      setStage("is-early", "Too soon!", "You clicked before green — click to try that one again");
    }
    function recordHit() {
      var ms = Math.round(performance.now() - goTime);
      attempts.push(ms); buildSlots(); SPEEDLAB.sound.click();
      state = "shown";
      setStage("", ms + " ms",
        attempts.length >= NEEDED ? "Click to see your result" : "Nice — click to continue");
    }
    function advance() {
      if (attempts.length >= NEEDED) finishAll(); else beginAttempt();
    }
    function finishAll() {
      state = "done";
      var sum = attempts.reduce(function (a, b) { return a + b; }, 0);
      var avg = sum / attempts.length;
      play.hidden = true;
      SPEEDLAB.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: avg, formatted: String(Math.round(avg)),
        detail: "Times: " + attempts.join(", ") + " ms",
        screen: screen, onRestart: fullReset
      });
      var p = document.createElement("p");
      p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = "Your " + attempts.length + " times: " + attempts.join(", ") + " ms";
      result.appendChild(p);
      paintPB();
    }
    function fullReset() {
      attempts = []; buildSlots();
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      toIdle();
    }

    function activate() {
      if (state === "idle" || state === "early") beginAttempt();
      else if (state === "waiting") tooSoon();
      else if (state === "go") recordHit();
      else if (state === "shown") advance();
    }

    stage.addEventListener("pointerdown", function (e) { e.preventDefault(); activate(); });
    stage.addEventListener("contextmenu", function (e) { e.preventDefault(); });
    document.addEventListener("keydown", function (e) {
      if (e.key !== " " && e.key !== "Enter" && e.code !== "Space") return;
      var ae = document.activeElement;
      if (ae && ae !== stage && /^(A|BUTTON|SUMMARY|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      e.preventDefault(); if (e.repeat) return; activate();
    });

    buildSlots(); toIdle(); paintPB();
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { SPEEDLAB.clearScores(storageKey); paintPB(); });

    SPEEDLAB.sound.initToggle($("soundToggle"));
    SPEEDLAB.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
