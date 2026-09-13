/* ==========================================================================
   SPEEDLAB — tests/chimp-test.js
   Chimp Test: numbers appear on a grid, then hide. Click them in order, 1, 2,
   3... Each round adds one more number. Three strikes and you're out.
   Score is the highest count of numbers you clear.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var COLS = 6, ROWS = 5, START_N = 4;

  function init() {
    var root = $("chimp");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.chimp;
    var storageKey = "chimp", testName = "Chimp Test";
    var screen = $("screen"), play = $("play"), result = $("result");
    var grid = $("grid"), startWrap = $("startWrap"), startBtn = $("startBtn");
    var numEl = $("num"), strikesEl = $("strikes"), statusEl = $("status"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var N = START_N, expected = 1, strikes = 0, best = 0, state = "idle";
    var cells = [];

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " numbers";
    }
    function paintStrikes() {
      var h = ""; for (var i = 0; i < 3; i++) h += '<span class="life' + (i < (3 - strikes) ? "" : " gone") + '"></span>';
      strikesEl.innerHTML = h;
    }
    function buildGrid() {
      grid.style.gridTemplateColumns = "repeat(" + COLS + ", 1fr)";
      var h = "";
      for (var i = 0; i < COLS * ROWS; i++) h += '<button class="mem-cell blank" type="button" data-i="' + i + '"></button>';
      grid.innerHTML = h;
      cells = grid.querySelectorAll(".mem-cell");
      Array.prototype.forEach.call(cells, function (c, i) {
        c.addEventListener("pointerdown", function (e) { e.preventDefault(); onCell(i, c); });
      });
    }
    function startRound() {
      numEl.textContent = N; expected = 1;
      buildGrid();
      var slots = [], i;
      for (i = 0; i < cells.length; i++) slots.push(i);
      for (i = slots.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var tmp = slots[i]; slots[i] = slots[j]; slots[j] = tmp; }
      for (i = 1; i <= N; i++) {
        var c = cells[slots[i - 1]];
        c.className = "mem-cell numbered"; c.textContent = i; c.dataset.num = i;
      }
      state = "reveal"; statusEl.textContent = "Click the numbers in order";
    }
    function cover() {
      Array.prototype.forEach.call(cells, function (c) {
        if (c.dataset.num) { c.classList.remove("numbered"); c.classList.add("hidden-num"); }
      });
    }
    function onCell(i, c) {
      if (state !== "reveal" && state !== "play") return;
      var num = parseInt(c.dataset.num || "0", 10);
      if (!num) return;
      if (num === expected) {
        if (expected === 1) { cover(); state = "play"; }
        c.classList.remove("hidden-num", "numbered"); c.classList.add("blank"); c.textContent = ""; delete c.dataset.num;
        S.sound.click();
        expected++;
        if (expected > N) { best = N; N++; state = "between"; statusEl.textContent = "Nice!"; setTimeout(startRound, 600); }
      } else {
        strikes++; paintStrikes(); S.sound.tone(180, 0.14, "square", 0.05);
        if (strikes >= 3) gameOver(); else { statusEl.textContent = "Strike! Try that round again"; setTimeout(startRound, 700); }
      }
    }
    function begin() { N = START_N; strikes = 0; best = 0; paintStrikes(); startWrap.hidden = true; restart.hidden = false; startRound(); }
    function gameOver() {
      state = "done";
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: best, formatted: String(best),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; N = START_N; strikes = 0; best = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startWrap.hidden = false; restart.hidden = true;
      numEl.textContent = START_N; statusEl.textContent = ""; grid.innerHTML = ""; paintStrikes();
    }

    startBtn.addEventListener("click", begin);
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
