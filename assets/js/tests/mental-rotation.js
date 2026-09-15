/* ==========================================================================
   SPEEDLAB — tests/mental-rotation.js
   Same or Mirror: a reference letter and a rotated copy. Decide whether the
   copy is the SAME letter (just rotated) or a MIRROR image. 60-second sprint;
   score is correct answers (higher is better). Wrong answers cost a moment.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 60;
  var GLYPHS = ["F", "R", "P", "G", "J", "b", "d"];   // chiral: mirror is always distinct from rotation
  var ANGLES = [45, 90, 135, 180, 225, 270, 315];

  function init() {
    var root = $("mentalrotation");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.mentalrotation;
    var storageKey = "mentalrotation", testName = "Same or Mirror";
    var screen = $("screen"), play = $("play"), result = $("result");
    var area = $("rotArea"), refEl = $("refShape"), testEl = $("testShape");
    var correctEl = $("correct"), timerEl = $("timer");
    var sameBtn = $("sameBtn"), mirrorBtn = $("mirrorBtn"), startBtn = $("startBtn");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var state = "idle", correct = 0, startTs = 0, raf = 0, endTimer = 0, fbTimer = 0, isMirror = false, locked = false;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " correct";
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function newPair() {
      area.className = "rot-area";
      var g = GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
      var deg = ANGLES[Math.floor(Math.random() * ANGLES.length)];
      isMirror = Math.random() < 0.5;
      refEl.textContent = g; refEl.style.transform = "";
      testEl.textContent = g;
      testEl.style.transform = "rotate(" + deg + "deg)" + (isMirror ? " scaleX(-1)" : "");
      locked = false;
    }
    function answer(saidMirror) {
      if (state !== "running" || locked) return;
      var right = (saidMirror === isMirror);
      if (right) {
        correct++; correctEl.textContent = correct; S.sound.click();
        area.className = "rot-area ok";
        newPair();
      } else {
        locked = true;
        area.className = "rot-area bad";
        clearTimeout(fbTimer);
        fbTimer = setTimeout(function () { if (state === "running") newPair(); }, 550);
      }
    }
    function begin() {
      state = "running"; correct = 0; correctEl.textContent = "0";
      startBtn.hidden = true; restart.hidden = false;
      sameBtn.disabled = false; mirrorBtn.disabled = false;
      startTs = performance.now(); endTimer = setTimeout(finish, DURATION * 1000);
      tick(); newPair();
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer); clearTimeout(fbTimer);
      sameBtn.disabled = true; mirrorBtn.disabled = true; play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: correct, formatted: String(correct),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; correct = 0; cancelAnimationFrame(raf); clearTimeout(endTimer); clearTimeout(fbTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true;
      sameBtn.disabled = true; mirrorBtn.disabled = true;
      correctEl.textContent = "0"; timerEl.textContent = DURATION;
      area.className = "rot-area";
      refEl.textContent = "F"; refEl.style.transform = "";
      testEl.textContent = "F"; testEl.style.transform = "rotate(90deg)";
    }

    startBtn.addEventListener("click", begin);
    sameBtn.addEventListener("click", function () { answer(false); });
    mirrorBtn.addEventListener("click", function () { answer(true); });
    document.addEventListener("keydown", function (e) {
      if (state !== "running") return;
      var ae = document.activeElement;
      if (ae && /^(A|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      if (e.key === "ArrowLeft" || e.key === "s" || e.key === "S") { e.preventDefault(); answer(false); }
      else if (e.key === "ArrowRight" || e.key === "m" || e.key === "M") { e.preventDefault(); answer(true); }
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
