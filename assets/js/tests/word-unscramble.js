/* ==========================================================================
   SPEEDLAB — tests/word-unscramble.js
   Word Unscramble: letters appear jumbled; type the real word. It checks
   itself the instant you spell it right. 60-second sprint; score is words
   solved (higher is better). A big, varied list keeps runs fresh.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 60;

  var WORDS = [
    "apple", "orange", "banana", "grape", "lemon", "peach", "cherry", "melon",
    "tiger", "panda", "eagle", "shark", "otter", "koala", "zebra", "moose",
    "river", "ocean", "cloud", "storm", "frost", "meadow", "canyon", "island",
    "planet", "rocket", "comet", "galaxy", "meteor", "saturn", "cosmos", "photon",
    "guitar", "violin", "drums", "piano", "trumpet", "melody", "rhythm", "chorus",
    "pencil", "eraser", "ruler", "folder", "marker", "binder", "crayon", "stapler",
    "castle", "bridge", "tunnel", "market", "temple", "palace", "cottage", "harbor",
    "dragon", "wizard", "knight", "goblin", "castle", "shield", "potion", "quest",
    "coffee", "butter", "cheese", "pepper", "cookie", "waffle", "noodle", "pickle",
    "silver", "copper", "bronze", "marble", "crystal", "diamond", "granite", "pebble",
    "winter", "summer", "spring", "autumn", "sunset", "sunrise", "shadow", "breeze",
    "puzzle", "riddle", "secret", "legend", "mystery", "wonder", "signal", "beacon",
    "camera", "screen", "button", "keyboard", "monitor", "battery", "cursor", "pixel",
    "jungle", "desert", "forest", "valley", "prairie", "glacier", "volcano", "lagoon",
    "rabbit", "falcon", "dolphin", "penguin", "lizard", "hamster", "cheetah", "walrus"
  ];

  function scramble(word) {
    var a = word.split(""), out;
    for (var tries = 0; tries < 12; tries++) {
      for (var i = a.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
      }
      out = a.join("");
      if (out !== word) return out;
    }
    return out;
  }

  function init() {
    var root = $("unscramble");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.unscramble;
    var storageKey = "unscramble", testName = "Word Unscramble";
    var screen = $("screen"), play = $("play"), result = $("result");
    var scrambledEl = $("scrambled"), input = $("answer"), solvedEl = $("solved"), timerEl = $("timer");
    var skipBtn = $("skipBtn"), startBtn = $("startBtn"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", solved = 0, startTs = 0, raf = 0, endTimer = 0, cur = "", last = "";

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " words";
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function nextWord() {
      do { cur = WORDS[Math.floor(Math.random() * WORDS.length)]; } while (cur === last && WORDS.length > 1);
      last = cur;
      scrambledEl.textContent = scramble(cur);
      input.value = "";
    }
    function begin() {
      state = "running"; solved = 0; solvedEl.textContent = "0";
      startBtn.hidden = true; restart.hidden = false; skipBtn.disabled = false;
      input.disabled = false;
      startTs = performance.now(); endTimer = setTimeout(finish, DURATION * 1000);
      tick(); nextWord(); input.focus();
    }
    function onInput() {
      if (state !== "running") return;
      if (input.value.trim().toLowerCase() === cur) {
        solved++; solvedEl.textContent = solved; S.sound.click();
        input.classList.remove("flash-good"); void input.offsetWidth; input.classList.add("flash-good");
        nextWord();
      }
    }
    function skip() {
      if (state !== "running") return;
      nextWord(); input.focus();
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer);
      input.disabled = true; input.blur(); skipBtn.disabled = true; play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: solved, formatted: String(solved),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; solved = 0; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true; skipBtn.disabled = true;
      solvedEl.textContent = "0"; timerEl.textContent = DURATION;
      scrambledEl.textContent = "SPEED"; input.value = ""; input.disabled = true;
    }

    startBtn.addEventListener("click", begin);
    input.addEventListener("input", onInput);
    skipBtn.addEventListener("click", skip);
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
