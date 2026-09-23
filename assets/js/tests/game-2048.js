/* ==========================================================================
   SPEEDLAB — tests/game-2048.js
   2048 / Number Merge: slide tiles with arrow keys or swipes; equal tiles
   slide together and merge into one worth double, with a quick collide+pop
   animation. Score is the running total; game ends when no move is left.
   Higher score is better. Best score is saved on this device.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var N = 4;
  var POS = [0, 25.75, 51.5, 77.25];   // % offsets matching the CSS grid
  var SLIDE = 100;                      // ms — matches the CSS left/top transition

  function init() {
    var root = $("game2048");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.g2048;
    var storageKey = "g2048", testName = "2048";
    var screen = $("screen"), play = $("play"), result = $("result");
    var tilesEl = $("g2048tiles"), scoreEl = $("score"), bestEl = $("best");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var cells, tiles, nextId, score, state, spawnDisabled = false;
    var pendingFn = null, pendingTimer = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb).toLocaleString();
      bestEl.textContent = pb === null ? "0" : Math.round(pb).toLocaleString();
    }
    function clearBoard() {
      tilesEl.innerHTML = ""; tiles = {}; nextId = 1;
      cells = []; for (var r = 0; r < N; r++) { cells.push([]); for (var c = 0; c < N; c++) cells[r].push(0); }
    }
    function addTile(r, c, v, cls) {
      var id = nextId++;
      var el = document.createElement("div");
      el.className = "g2048-tile" + (cls ? " " + cls : "");
      el.setAttribute("data-v", v); el.textContent = v;
      el.style.left = POS[c] + "%"; el.style.top = POS[r] + "%";
      tilesEl.appendChild(el);
      tiles[id] = { v: v, el: el }; cells[r][c] = id;
      return id;
    }
    function moveEl(id, r, c) {
      var t = tiles[id]; if (!t) return;
      t.el.style.left = POS[c] + "%"; t.el.style.top = POS[r] + "%";
    }
    function empties() {
      var out = [];
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (!cells[r][c]) out.push([r, c]);
      return out;
    }
    function spawn(cls) {
      var e = empties(); if (!e.length) return null;
      var cell = e[Math.floor(Math.random() * e.length)];
      addTile(cell[0], cell[1], Math.random() < 0.9 ? 2 : 4, cls || "new");
      return cell;
    }
    function valAt(r, c) { return cells[r][c] ? tiles[cells[r][c]].v : 0; }
    function getGridVals() {
      var g = []; for (var r = 0; r < N; r++) { g.push([]); for (var c = 0; c < N; c++) g[r].push(valAt(r, c)); } return g;
    }
    function lineCoords(dir, i) {
      var line = [];
      for (var j = 0; j < N; j++) {
        var r, c;
        if (dir === "left") { r = i; c = j; }
        else if (dir === "right") { r = i; c = N - 1 - j; }
        else if (dir === "up") { r = j; c = i; }
        else { r = N - 1 - j; c = i; }
        line.push({ r: r, c: c });
      }
      return line;
    }
    function flush() {
      if (pendingFn) { clearTimeout(pendingTimer); var f = pendingFn; pendingFn = null; f(); }
    }
    function isOver() {
      if (empties().length) return false;
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) {
        var v = valAt(r, c);
        if (c + 1 < N && valAt(r, c + 1) === v) return false;
        if (r + 1 < N && valAt(r + 1, c) === v) return false;
      }
      return true;
    }
    function maxTile() {
      var m = 0; for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (valAt(r, c) > m) m = valAt(r, c); return m;
    }
    function move(dir) {
      if (state !== "playing") return false;
      flush();
      if (state !== "playing") return false;   // flush may have ended the game

      var moved = false, gain = 0, mergePairs = [];
      var oldPos = {};
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (cells[r][c]) oldPos[cells[r][c]] = [r, c];
      var newCells = []; for (var i = 0; i < N; i++) { newCells.push([]); for (var j = 0; j < N; j++) newCells[i].push(0); }

      for (i = 0; i < N; i++) {
        var coords = lineCoords(dir, i);
        var ids = [];
        for (j = 0; j < N; j++) { var id0 = cells[coords[j].r][coords[j].c]; if (id0) ids.push(id0); }
        var target = 0, k = 0;
        while (k < ids.length) {
          var id = ids[k], dest = coords[target];
          if (k + 1 < ids.length && tiles[ids[k + 1]].v === tiles[id].v) {
            var absorbed = ids[k + 1];
            newCells[dest.r][dest.c] = id;
            moveEl(id, dest.r, dest.c); moveEl(absorbed, dest.r, dest.c);
            tiles[id].v *= 2; gain += tiles[id].v;
            mergePairs.push({ survivor: id, absorbed: absorbed });
            moved = true; k += 2; target++;
          } else {
            newCells[dest.r][dest.c] = id;
            var op = oldPos[id];
            if (op[0] !== dest.r || op[1] !== dest.c) { moveEl(id, dest.r, dest.c); moved = true; }
            k++; target++;
          }
        }
      }
      if (!moved) return false;

      cells = newCells;
      score += gain; scoreEl.textContent = score.toLocaleString();
      if (gain) S.sound.click();
      if (score > (S.getPB(storageKey) || 0)) bestEl.textContent = score.toLocaleString();

      var doCleanup = function () {
        mergePairs.forEach(function (m) {
          if (tiles[m.absorbed]) { tiles[m.absorbed].el.remove(); delete tiles[m.absorbed]; }
          var t = tiles[m.survivor];
          if (t) {
            t.el.setAttribute("data-v", t.v); t.el.textContent = t.v;
            t.el.classList.remove("pop"); void t.el.offsetWidth; t.el.classList.add("pop");
          }
        });
        if (!spawnDisabled) spawn("new");
        if (isOver()) finish();
      };
      pendingFn = doCleanup;
      pendingTimer = setTimeout(function () { pendingFn = null; doCleanup(); }, SLIDE);
      return true;
    }
    function finish() {
      state = "done"; play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: score, formatted: score.toLocaleString() + " pts",
        detail: "Best tile: " + maxTile(),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      flush(); clearTimeout(pendingTimer); pendingFn = null;
      state = "playing"; score = 0; scoreEl.textContent = "0";
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = false;
      clearBoard(); spawn("new"); spawn("new");
      paintPB();
    }

    var KEYMAP = {
      ArrowLeft: "left", ArrowRight: "right", ArrowUp: "up", ArrowDown: "down",
      a: "left", d: "right", w: "up", s: "down", A: "left", D: "right", W: "up", S: "down"
    };
    document.addEventListener("keydown", function (e) {
      var dir = KEYMAP[e.key]; if (!dir) return;
      var ae = document.activeElement;
      if (ae && /^(INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      e.preventDefault(); move(dir);
    });
    var board = $("g2048board"), sx = 0, sy = 0, tracking = false;
    board.addEventListener("touchstart", function (e) { tracking = true; sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
    board.addEventListener("touchmove", function (e) { if (tracking) e.preventDefault(); }, { passive: false });
    board.addEventListener("touchend", function (e) {
      if (!tracking) return; tracking = false;
      var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 24) return;
      move(Math.abs(dx) > Math.abs(dy) ? (dx > 0 ? "right" : "left") : (dy > 0 ? "down" : "up"));
    }, { passive: true });

    restart.addEventListener("click", reset);
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    if (new URLSearchParams(location.search).get("test") === "1") {
      window.__g2048 = {
        move: move, isOver: isOver, getScore: function () { return score; },
        setGrid: function (g) {
          flush(); clearTimeout(pendingTimer); pendingFn = null; clearBoard();
          for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (g[r][c]) addTile(r, c, g[r][c]);
        },
        getGrid: getGridVals,
        noSpawn: function (b) { spawnDisabled = b; },
        flush: flush,
        state: function () { return state; }
      };
    }

    reset();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
