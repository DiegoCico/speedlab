/* ==========================================================================
   SPEEDLAB — tests/emoji-hunt.js
   Emoji Hunt: find the one emoji that is different in the grid. Each round the
   grid grows and the pairs get more similar. One wrong tap ends the game.
   Score is the number of rounds you clear.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var PAIRS = [
    // easy — clearly different
    [["🐶","🐱"],["🍎","🍌"],["⭐","❤️"],["🔵","🔴"],["🌵","🌴"],["🐝","🦋"],["🍦","🍕"],["⚽","🏀"]],
    // medium
    [["🍎","🍏"],["😀","😄"],["🐶","🐺"],["🌚","🌝"],["🍊","🍋"],["😢","😭"],["🐰","🐭"],["🔶","🔸"]],
    // hard — very similar
    [["😀","😃"],["😐","😑"],["🙂","😊"],["🤔","🤨"],["😴","😪"],["😌","😔"],["🥲","🥹"],["😕","🙁"]]
  ];

  function init() {
    var root = $("emojihunt");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.emoji;
    var storageKey = "emoji", testName = "Emoji Hunt";
    var screen = $("screen"), play = $("play"), result = $("result");
    var grid = $("grid"), startWrap = $("startWrap"), startBtn = $("startBtn");
    var levelEl = $("level"), statusEl = $("status"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var level = 1, state = "idle";

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " level";
    }
    function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
    function newRound() {
      var cols = Math.min(2 + Math.floor((level - 1) / 2), 8);
      var tier = level <= 4 ? 0 : (level <= 9 ? 1 : 2);
      var pair = pick(PAIRS[tier]);
      if (Math.random() < 0.5) pair = [pair[1], pair[0]]; // vary which is "base"
      var base = pair[0], odd = pair[1];
      var n = cols * cols, oddIdx = Math.floor(Math.random() * n);
      grid.style.gridTemplateColumns = "repeat(" + cols + ", 1fr)";
      var fs = Math.max(1.0, 3.2 - (cols - 2) * 0.32) + "rem";
      var h = "";
      for (var i = 0; i < n; i++) {
        h += '<button class="emoji-cell" type="button" style="font-size:' + fs + '" data-odd="' +
          (i === oddIdx ? "1" : "0") + '" aria-label="emoji">' + (i === oddIdx ? odd : base) + "</button>";
      }
      grid.innerHTML = h;
      Array.prototype.forEach.call(grid.querySelectorAll(".emoji-cell"), function (c) {
        c.addEventListener("pointerdown", function (e) { e.preventDefault(); onCell(c); });
      });
      levelEl.textContent = level;
      statusEl.textContent = "Find the different one";
      state = "play";
    }
    function onCell(c) {
      if (state !== "play") return;
      if (c.dataset.odd === "1") { level++; S.sound.click(); newRound(); }
      else { c.classList.add("bad"); S.sound.tone(180, 0.14, "square", 0.05); gameOver(); }
    }
    function begin() { level = 1; startWrap.hidden = true; restart.hidden = false; newRound(); }
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
      state = "idle"; level = 1;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startWrap.hidden = false; restart.hidden = true;
      levelEl.textContent = 1; statusEl.textContent = ""; grid.innerHTML = "";
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
