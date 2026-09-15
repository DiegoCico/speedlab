/* ==========================================================================
   SPEEDLAB — tests/memory-match.js
   Memory Match (Concentration): flip cards two at a time to find all eight
   pairs. Timer starts on the first flip; score is the time to clear the board
   in seconds (lower is better).
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var SYMBOLS = ["🚀", "⚡", "🎮", "🔥", "⭐", "🎯", "💎", "🏆"];
  var PAIRS = SYMBOLS.length;

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function init() {
    var root = $("memorymatch");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.memorymatch;
    var storageKey = "memorymatch", testName = "Memory Match";
    var screen = $("screen"), play = $("play"), result = $("result");
    var board = $("board"), matchesEl = $("matches"), timerEl = $("timer");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var first = null, lock = false, matched = 0, started = false, startTs = 0, raf = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : (Math.round(pb * 10) / 10) + " s";
    }
    function tick() {
      if (!started) return;
      timerEl.textContent = ((performance.now() - startTs) / 1000).toFixed(1);
      raf = requestAnimationFrame(tick);
    }
    function build() {
      var deck = shuffle(SYMBOLS.concat(SYMBOLS));
      board.innerHTML = "";
      deck.forEach(function (sym) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "mm-card";
        b.setAttribute("aria-label", "Card");
        b.dataset.sym = sym;
        b.innerHTML = '<span class="sym" aria-hidden="true">' + sym + "</span>";
        b.addEventListener("click", function () { flip(b); });
        board.appendChild(b);
      });
    }
    function flip(card) {
      if (lock || card.classList.contains("up") || card.classList.contains("matched")) return;
      if (!started) { started = true; startTs = performance.now(); tick(); }
      card.classList.add("up");
      if (!first) { first = card; return; }
      if (first.dataset.sym === card.dataset.sym) {
        first.classList.add("matched"); card.classList.add("matched");
        first.disabled = true; card.disabled = true;
        matched++; matchesEl.textContent = matched + "/" + PAIRS; S.sound.click();
        first = null;
        if (matched >= PAIRS) finish();
      } else {
        lock = true;
        var a = first, b = card; first = null;
        setTimeout(function () {
          a.classList.remove("up"); b.classList.remove("up"); lock = false;
        }, 700);
      }
    }
    function finish() {
      started = false; cancelAnimationFrame(raf);
      var secs = (performance.now() - startTs) / 1000;
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: secs, formatted: secs.toFixed(1) + " s",
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      cancelAnimationFrame(raf);
      first = null; lock = false; matched = 0; started = false;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = false;
      matchesEl.textContent = "0/" + PAIRS; timerEl.textContent = "0.0";
      build();
    }

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
