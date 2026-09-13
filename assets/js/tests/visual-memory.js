/* ==========================================================================
   SPEEDLAB — tests/visual-memory.js
   Visual Memory: tiles flash on a grid, then reproduce them from memory. The
   grid and the number of tiles grow each level. Three lives. Score = level.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("visualmem");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.visualmem;
    var storageKey = "visualmem", testName = "Visual Memory";
    var screen = $("screen"), play = $("play"), result = $("result");
    var grid = $("grid"), startWrap = $("startWrap"), startBtn = $("startBtn");
    var levelEl = $("level"), livesEl = $("lives"), statusEl = $("status"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var level = 1, lives = 3, size = 3, count = 3, target = {}, found = 0, state = "idle", t = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " level";
    }
    function paintLives() {
      var h = ""; for (var i = 0; i < 3; i++) h += '<span class="life' + (i < lives ? "" : " gone") + '"></span>';
      livesEl.innerHTML = h;
    }
    function build(n) {
      grid.style.gridTemplateColumns = "repeat(" + n + ", 1fr)";
      var h = "";
      for (var i = 0; i < n * n; i++) h += '<button class="mem-cell" type="button" data-i="' + i + '" aria-label="Tile"></button>';
      grid.innerHTML = h;
      Array.prototype.forEach.call(grid.querySelectorAll(".mem-cell"), function (c, i) {
        c.addEventListener("pointerdown", function (e) { e.preventDefault(); onCell(i, c); });
      });
    }
    function showLevel() {
      size = Math.min(3 + Math.floor(level / 3), 7);
      count = Math.min(level + 2, size * size - 2);
      levelEl.textContent = level;
      build(size);
      var cells = grid.querySelectorAll(".mem-cell");
      target = {}; found = 0;
      var chosen = 0;
      while (chosen < count) { var r = Math.floor(Math.random() * cells.length); if (!target[r]) { target[r] = true; chosen++; } }
      state = "show"; statusEl.textContent = "Memorize…";
      for (var k in target) cells[k].classList.add("lit");
      var showTime = 700 + count * 120;
      clearTimeout(t); t = setTimeout(function () {
        for (var k2 in target) cells[k2].classList.remove("lit");
        state = "input"; statusEl.textContent = "Click the tiles";
      }, showTime);
    }
    function onCell(i, cell) {
      if (state !== "input") return;
      if (cell.classList.contains("good") || cell.classList.contains("bad")) return;
      if (target[i]) {
        cell.classList.add("good"); found++;
        if (found >= count) { state = "between"; statusEl.textContent = "Nice!"; level++; clearTimeout(t); t = setTimeout(showLevel, 650); }
      } else {
        cell.classList.add("bad"); S.sound.tone(180, 0.12, "square", 0.05);
        lives--; paintLives();
        if (lives <= 0) gameOver();
      }
    }
    function begin() { level = 1; lives = 3; paintLives(); startWrap.hidden = true; restart.hidden = false; showLevel(); }
    function gameOver() {
      state = "done";
      var score = level - 1;
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: score, formatted: String(score),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      clearTimeout(t); state = "idle"; level = 1; lives = 3;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startWrap.hidden = false; restart.hidden = true;
      levelEl.textContent = 1; statusEl.textContent = ""; grid.innerHTML = ""; paintLives();
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
