/* ==========================================================================
   SPEEDLAB — tests/typing.js
   Typing Speed Test (WPM). Type the passage; the timer starts on your first
   keystroke. Live net WPM = (correct chars / 5) / minutes, plus accuracy.
   Durations 15 / 30 / 60s, each with its own personal best.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  var WORDS = ("the of to and a in is it you that he was for on are with as his they at be this from i have or " +
    "by one had not but what all were when we there can an your which their said if do will each about how up out " +
    "them then she many some so these would other into has more her two like him see time could no make than first " +
    "been its who now people my made over did down only way find use may water long little very after words called " +
    "just where most know get through back much go good new write our used me man too any day same right look think " +
    "also around another came come work three word must because does part even place well such here take why help " +
    "put different away again off went old number great tell men say small every found still between name should " +
    "home big give air line set own under read last never us left end along while might next sound below saw " +
    "something thought both few those always show large often together asked house world going want school important " +
    "until form food keep children feet land side without boy once animal life enough took four head above kind began").split(" ");

  function buildPassage(n) {
    var w = [], last = -1, idx;
    for (var i = 0; i < n; i++) {
      do { idx = Math.floor(Math.random() * WORDS.length); } while (idx === last);
      last = idx; w.push(WORDS[idx]);
    }
    return w.join(" ");
  }

  function init() {
    var root = $("typing");
    if (!root || !window.SPEEDLAB) return;

    var conf = SPEEDLAB.config.typing;
    var screen = $("screen"), play = $("play"), result = $("result");
    var passage = $("passage"), lines = $("lines"), input = $("typeInput");
    var wpmEl = $("wpm"), accEl = $("acc"), timerEl = $("timer");
    var restart = $("restart"), pbValEl = document.querySelector("[data-pb]");

    var duration = parseInt(root.getAttribute("data-duration") || "30", 10);
    function storageKey() { return "typing-" + duration + "s"; }
    function testName() { return "Typing Speed Test (" + duration + " Seconds)"; }
    function paintPB() {
      var pb = SPEEDLAB.getPB(storageKey());
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " WPM";
    }

    var target = "", spans = [], state = "idle", startTs = 0, raf = 0, endTimer = 0, lineH = 30;

    function renderPassage() {
      target = buildPassage(220);
      var html = "";
      for (var i = 0; i < target.length; i++) {
        var c = target.charAt(i);
        html += '<span class="ch">' + (c === " " ? "&nbsp;" : c) + "</span>";
      }
      lines.innerHTML = html;
      spans = lines.querySelectorAll(".ch");
      lines.style.transform = "translateY(0)";
      if (spans.length > 1) lineH = spans[0].offsetHeight || 30;
      paintCursor(0, 0);
    }

    function paintCursor(typedLen, correct) {
      for (var i = 0; i < spans.length; i++) {
        var s = spans[i], cls = "ch";
        if (i < typedLen) cls += (input.value.charAt(i) === target.charAt(i)) ? " good" : " bad";
        else if (i === typedLen) cls += " cur";
        s.className = cls;
      }
      // keep the current line one row from the top
      if (spans[typedLen]) {
        var top = spans[typedLen].offsetTop;
        var shift = Math.max(0, top - lineH);
        lines.style.transform = "translateY(" + (-shift) + "px)";
      }
    }

    function stats() {
      var v = input.value, correct = 0, n = Math.min(v.length, target.length);
      for (var i = 0; i < n; i++) if (v.charAt(i) === target.charAt(i)) correct++;
      var mins = state === "running" ? (performance.now() - startTs) / 60000 : (duration / 60);
      var wpm = mins > 0 ? (correct / 5) / mins : 0;
      var acc = v.length ? Math.round(correct / v.length * 100) : 100;
      return { correct: correct, wpm: wpm, acc: acc, typed: v.length };
    }

    function tick() {
      if (state !== "running") return;
      var elapsed = (performance.now() - startTs) / 1000;
      timerEl.textContent = Math.max(0, Math.ceil(duration - elapsed));
      var s = stats();
      wpmEl.textContent = Math.round(s.wpm);
      accEl.textContent = s.acc;
      raf = requestAnimationFrame(tick);
    }

    function begin() {
      state = "running"; startTs = performance.now();
      passage.classList.remove("blurred");
      restart.hidden = false;
      endTimer = setTimeout(finish, duration * 1000);
      tick();
    }

    function onInput() {
      if (state === "done") return;
      if (state === "idle") begin();
      if (input.value.length > target.length) input.value = input.value.slice(0, target.length);
      var s = stats();
      paintCursor(input.value.length, s.correct);
      wpmEl.textContent = Math.round(s.wpm);
      accEl.textContent = s.acc;
      if (input.value.length >= target.length) finish();
    }

    function finish() {
      if (state === "done") return;
      cancelAnimationFrame(raf); clearTimeout(endTimer);
      state = "done";
      var s = stats();
      play.hidden = true;
      input.blur();
      SPEEDLAB.renderResult({
        cfg: conf, storageKey: storageKey(), container: result,
        testName: testName(), score: Math.round(s.wpm), formatted: String(Math.round(s.wpm)),
        screen: screen, onRestart: reset
      });
      var extra = document.createElement("p");
      extra.className = "pct"; extra.style.color = "var(--c-ink-dim)";
      extra.textContent = "Accuracy " + s.acc + "% · " + s.correct + " correct characters";
      result.appendChild(extra);
      paintPB();
    }

    function reset() {
      cancelAnimationFrame(raf); clearTimeout(endTimer);
      state = "idle";
      input.value = "";
      play.hidden = false;
      result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true;
      wpmEl.textContent = "0"; accEl.textContent = "100";
      timerEl.textContent = duration;
      passage.classList.add("blurred");
      renderPassage();
    }

    // focusing the passage raises the mobile keyboard and starts capture
    passage.addEventListener("pointerdown", function (e) { e.preventDefault(); input.focus(); });
    input.addEventListener("input", onInput);
    input.addEventListener("focus", function () { if (state !== "done") passage.classList.remove("blurred"); });
    input.addEventListener("blur", function () { if (state === "idle") passage.classList.add("blurred"); });

    restart.addEventListener("click", reset);

    // duration selector
    var opts = root.querySelectorAll(".seg-select .opt");
    Array.prototype.forEach.call(opts, function (b) {
      b.addEventListener("click", function () {
        duration = parseInt(b.getAttribute("data-dur"), 10);
        Array.prototype.forEach.call(opts, function (o) { o.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        reset(); paintPB(); b.blur();
      });
    });

    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { SPEEDLAB.clearScores(storageKey()); paintPB(); });

    reset(); paintPB();
    SPEEDLAB.sound.initToggle($("soundToggle"));
    SPEEDLAB.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
