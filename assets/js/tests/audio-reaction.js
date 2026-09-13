/* ==========================================================================
   SPEEDLAB — tests/audio-reaction.js
   Audio Reaction Test: wait, a beep plays, react as fast as you can. Five
   attempts, averaged. Needs sound on (it's an audio test), so it prompts to
   enable sound first. Clicking before the beep is "too soon".
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var NEEDED = 5;

  function init() {
    var root = $("audioreaction");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.audioreaction;
    var storageKey = "audioreaction", testName = "Audio Reaction Test";
    var stage = $("stage"), title = $("stageTitle"), sub = $("stageSub");
    var play = $("play"), result = $("result"), slotsEl = $("slots"), screen = $("screen");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", attempts = [], goTime = 0, timer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " ms";
    }
    function buildSlots() {
      var html = "";
      for (var i = 0; i < NEEDED; i++) {
        var v = attempts[i];
        html += '<div class="react-slot' + (v != null ? " filled" : "") + '"><span class="n">' +
          (v != null ? v : "—") + "</span>" + (i + 1) + "</div>";
      }
      slotsEl.innerHTML = html;
    }
    function setStage(cls, t, s) { stage.className = "react-stage" + (cls ? " " + cls : ""); title.textContent = t; sub.textContent = s || ""; }

    function toIdle() {
      state = "idle";
      if (!S.sound.enabled) { setStage("", "Turn on sound", "This is an audio test — tap to enable sound and start"); return; }
      var n = attempts.length;
      setStage("", n ? "Ready?" : "Tap to start", n ? ("Attempt " + (n + 1) + " of " + NEEDED) : "Listen for the beep, then tap. " + NEEDED + " tries.");
    }
    function beginAttempt() {
      state = "waiting";
      setStage("is-wait", "Wait for the beep…", "Don't tap yet");
      clearTimeout(timer);
      timer = setTimeout(goBeep, 1200 + Math.random() * 3200);
    }
    function goBeep() { state = "go"; goTime = performance.now(); S.sound.beep(); setStage("is-go", "TAP!", "React to the beep"); }
    function tooSoon() { clearTimeout(timer); state = "early"; setStage("is-early", "Too soon!", "You tapped before the beep — tap to try again"); }
    function recordHit() {
      var ms = Math.round(performance.now() - goTime);
      attempts.push(ms); buildSlots(); S.sound.click(); state = "shown";
      setStage("", ms + " ms", attempts.length >= NEEDED ? "Tap to see your result" : "Nice — tap to continue");
    }
    function advance() { if (attempts.length >= NEEDED) finishAll(); else beginAttempt(); }
    function finishAll() {
      state = "done";
      var avg = attempts.reduce(function (a, b) { return a + b; }, 0) / attempts.length;
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: avg, formatted: String(Math.round(avg)),
        screen: screen, onRestart: fullReset
      });
      var p = document.createElement("p"); p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = "Your " + attempts.length + " times: " + attempts.join(", ") + " ms";
      result.appendChild(p);
      paintPB();
    }
    function fullReset() {
      attempts = []; buildSlots(); play.hidden = false;
      result.classList.remove("show"); result.innerHTML = ""; toIdle();
    }

    function activate() {
      if (state === "idle") {
        if (!S.sound.enabled) { S.sound.setEnabled(true); var b = $("soundToggle"); if (b) { b.setAttribute("aria-pressed", "true"); b.querySelector("[data-sound-label]").textContent = "Sound: On"; } toIdle(); return; }
        beginAttempt();
      } else if (state === "early") beginAttempt();
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

    buildSlots();
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    S.sound.initToggle($("soundToggle"));
    toIdle(); paintPB();
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
