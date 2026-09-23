/* ==========================================================================
   SPEEDLAB — tests/game-2048.js
   2048 / Number Merge: slide tiles with arrow keys or swipes; equal tiles
   merge and double. Score is the running total; game ends when no move is
   left. Higher score is better. Best score is saved on this device.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var N = 4;
  var POS = [0, 25.75, 51.5, 77.25];   // % offsets matching the CSS grid

  function init() {
    var root = $("game2048");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.g2048;
    var storageKey = "g2048", testName = "2048";
    var screen = $("screen"), play = $("play"), result = $("result");
    var tilesEl = $("g2048tiles"), scoreEl = $("score"), bestEl = $("best");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var grid, score, state, spawnDisabled = false;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb).toLocaleString();
      bestEl.textContent = pb === null ? "0" : Math.round(pb).toLocaleString();
    }
    function empties() {
      var out = [];
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (!grid[r][c]) out.push([r, c]);
      return out;
    }
    function spawn() {
      var e = empties();
      if (!e.length) return null;
      var cell = e[Math.floor(Math.random() * e.length)];
      grid[cell[0]][cell[1]] = Math.random() < 0.9 ? 2 : 4;
      return cell;
    }
    function render(spawnCell, merged) {
      merged = merged || [];
      tilesEl.innerHTML = "";
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) {
        var v = grid[r][c];
        if (!v) continue;
        var t = document.createElement("div");
        t.className = "g2048-tile";
        t.setAttribute("data-v", v);
        t.textContent = v;
        t.style.left = POS[c] + "%";
        t.style.top = POS[r] + "%";
        if (spawnCell && spawnCell[0] === r && spawnCell[1] === c) t.className += " new";
        for (var m = 0; m < merged.length; m++) if (merged[m][0] === r && merged[m][1] === c) { t.className += " pop"; break; }
        tilesEl.appendChild(t);
      }
    }
    function slide(vals) {
      var packed = vals.filter(function (v) { return v; });
      var out = [], gain = 0, mergedIdx = [];
      for (var i = 0; i < packed.length; i++) {
        if (i + 1 < packed.length && packed[i] === packed[i + 1]) {
          var mv = packed[i] * 2; out.push(mv); gain += mv; mergedIdx.push(out.length - 1); i++;
        } else out.push(packed[i]);
      }
      while (out.length < N) out.push(0);
      var moved = out.some(function (v, idx) { return v !== vals[idx]; });
      return { line: out, gain: gain, moved: moved, merged: mergedIdx };
    }
    function lineCoords(dir, i) {
      var line = [];
      for (var j = 0; j < N; j++) {
        var r, c;
        if (dir === "left") { r = i; c = j; }
        else if (dir === "right") { r = i; c = N - 1 - j; }
        else if (dir === "up") { r = j; c = i; }
        else { r = N - 1 - j; c = i; }
        line.push([r, c]);
      }
      return line;
    }
    function move(dir) {
      if (state !== "playing") return false;
      var moved = false, gain = 0, merged = [];
      for (var i = 0; i < N; i++) {
        var coords = lineCoords(dir, i);
        var vals = coords.map(function (rc) { return grid[rc[0]][rc[1]]; });
        var res = slide(vals);
        if (res.moved) moved = true;
        gain += res.gain;
        coords.forEach(function (rc, idx) { grid[rc[0]][rc[1]] = res.line[idx]; });
        res.merged.forEach(function (idx) { merged.push(coords[idx]); });
      }
      if (!moved) return false;
      score += gain; scoreEl.textContent = score.toLocaleString();
      if (gain) S.sound.click();
      var sc = spawnDisabled ? null : spawn();
      render(sc, merged);
      if (score > (S.getPB(storageKey) || 0)) bestEl.textContent = score.toLocaleString();
      if (isOver()) finish();
      return true;
    }
    function isOver() {
      if (empties().length) return false;
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) {
        var v = grid[r][c];
        if (c + 1 < N && grid[r][c + 1] === v) return false;
        if (r + 1 < N && grid[r + 1][c] === v) return false;
      }
      return true;
    }
    function maxTile() {
      var m = 0;
      for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) if (grid[r][c] > m) m = grid[r][c];
      return m;
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
      state = "playing"; score = 0; scoreEl.textContent = "0";
      grid = [];
      for (var r = 0; r < N; r++) { grid.push([]); for (var c = 0; c < N; c++) grid[r].push(0); }
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = false;
      spawn(); spawn(); render();
      paintPB();
    }

    // input: keyboard
    var KEYMAP = {
      ArrowLeft: "left", ArrowRight: "right", ArrowUp: "up", ArrowDown: "down",
      a: "left", d: "right", w: "up", s: "down", A: "left", D: "right", W: "up", S: "down"
    };
    document.addEventListener("keydown", function (e) {
      var dir = KEYMAP[e.key];
      if (!dir) return;
      var ae = document.activeElement;
      if (ae && /^(INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      e.preventDefault();
      move(dir);
    });
    // input: swipe
    var board = $("g2048board"), sx = 0, sy = 0, tracking = false;
    board.addEventListener("touchstart", function (e) {
      tracking = true; sx = e.touches[0].clientX; sy = e.touches[0].clientY;
    }, { passive: true });
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

    // test seam (only with ?test=1) — lets headless drive deterministic boards
    if (new URLSearchParams(location.search).get("test") === "1") {
      window.__g2048 = {
        move: move, isOver: isOver, getScore: function () { return score; },
        setGrid: function (g) { grid = g.map(function (row) { return row.slice(); }); render(); },
        getGrid: function () { return grid; },
        noSpawn: function (b) { spawnDisabled = b; },
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
