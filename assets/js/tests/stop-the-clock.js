/* ==========================================================================
   SPEEDLAB — tests/stop-the-clock.js
   Stop the Clock: a timer counts up; stop it as close to the target as you can.
   Five rounds, scored by your average miss in milliseconds (lower is better).
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var ROUNDS = 5;

  function fmt(ms) { return (ms / 1000).toFixed(3); }
  function pickTarget() {
    // 2.0s to 6.0s, snapped to the nearest half second, so the aim point is clean.
    return Math.round((2 + Math.random() * 4) * 2) / 2 * 1000;
  }

  function init() {
    var root = $("stopclock");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.stopclock;
    var storageKey = "stopclock", testName = "Stop the Clock";
    var screen = $("screen"), play = $("play"), result = $("result");
    var targetEl = $("target"), clockEl = $("clock"), msgEl = $("msg");
    var pad = $("pad"), padTitle = pad.querySelector("[data-pad-title]");
    var roundEl = $("round"), lastEl = $("last");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var state = "idle", round = 0, target = 0, startTs = 0, raf = 0, misses = [];

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " ms";
    }
    function setPad(t) { padTitle.textContent = t; }
    function tick() {
      if (state !== "running") return;
      clockEl.textContent = fmt(performance.now() - startTs);
      raf = requestAnimationFrame(tick);
    }
    function newRound() {
      target = pickTarget();
      targetEl.innerHTML = "Stop at <b>" + fmt(target) + "</b>";
      clockEl.textContent = "0.000"; clockEl.classList.remove("win");
      roundEl.textContent = (round + 1) + "/" + ROUNDS;
      msgEl.textContent = round === 0 ? "Press Start, then stop the clock on target." : "";
      state = "ready"; setPad("Start");
    }
    function start() {
      state = "running"; startTs = performance.now(); msgEl.textContent = "";
      setPad("STOP"); tick();
    }
    function stop() {
      cancelAnimationFrame(raf);
      var elapsed = performance.now() - startTs;
      clockEl.textContent = fmt(elapsed);
      var miss = Math.round(Math.abs(elapsed - target));
      misses.push(miss);
      lastEl.textContent = miss;
      clockEl.classList.toggle("win", miss <= 40);
      var early = elapsed < target;
      msgEl.textContent = (miss <= 40 ? "Bullseye! " : "") + miss + " ms " +
        (miss === 0 ? "" : early ? "early" : "late");
      S.sound.click();
      round++;
      if (round >= ROUNDS) { state = "done"; setPad("See result"); }
      else { state = "shown"; setPad("Next"); }
    }
    function advance() {
      if (round >= ROUNDS) finish(); else newRound();
    }
    function finish() {
      state = "final"; cancelAnimationFrame(raf); play.hidden = true;
      var sum = misses.reduce(function (a, b) { return a + b; }, 0);
      var avg = Math.round(sum / misses.length);
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: avg, formatted: String(avg) + " ms",
        detail: "Misses: " + misses.join(", ") + " ms",
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      cancelAnimationFrame(raf); misses = []; round = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; lastEl.textContent = "—";
      newRound();
    }

    function activate() {
      if (state === "ready") { restart.hidden = false; start(); }
      else if (state === "running") stop();
      else if (state === "shown" || state === "done") advance();
    }

    pad.addEventListener("pointerdown", function (e) { e.preventDefault(); activate(); });
    pad.addEventListener("contextmenu", function (e) { e.preventDefault(); });
    document.addEventListener("keydown", function (e) {
      if (e.key !== " " && e.key !== "Enter" && e.code !== "Space") return;
      var ae = document.activeElement;
      if (ae && ae !== pad && /^(A|BUTTON|SUMMARY|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      e.preventDefault(); if (e.repeat) return; activate();
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
