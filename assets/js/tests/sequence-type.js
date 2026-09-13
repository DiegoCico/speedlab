/* ==========================================================================
   SPEEDLAB — tests/sequence-type.js
   "Type the sequence" test: type a fixed target (A-Z, or 1-100) as fast as
   you can. The timer counts up from your first keystroke and stops the moment
   the whole sequence is correct. Score is the completion time in seconds.
   Driven by data-mode on <section id="seq">.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function buildTarget(mode) {
    if (mode === "number") {
      var a = []; for (var i = 1; i <= 100; i++) a.push(String(i));
      return { words: a, spaced: true, text: a.join(" ") };
    }
    var l = []; for (var c = 97; c <= 122; c++) l.push(String.fromCharCode(c));
    return { words: l, spaced: false, text: l.join("") };
  }

  function init() {
    var root = $("seq");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB;
    var mode = root.getAttribute("data-mode") || "alphabet";
    var conf = S.config[mode];
    var testName = mode === "number" ? "Number Typing Test" : "Alphabet Typing Test";
    var storageKey = mode === "number" ? "number-type" : "alphabet-type";

    var screen = $("screen"), play = $("play"), result = $("result");
    var passage = $("passage"), lines = $("lines"), input = $("typeInput");
    var timerEl = $("timer"), progEl = $("prog"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var T = buildTarget(mode), spans = [], state = "idle", startTs = 0, raf = 0, lineH = 30;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : (Math.round(pb * 10) / 10).toFixed(1) + " s";
    }
    function renderSeq() {
      var html = "";
      for (var w = 0; w < T.words.length; w++) {
        html += '<span class="word">';
        for (var j = 0; j < T.words[w].length; j++) html += '<span class="ch">' + T.words[w].charAt(j) + "</span>";
        html += "</span>";
        if (T.spaced && w < T.words.length - 1) html += '<span class="ch sp"> </span>';
      }
      lines.innerHTML = html;
      spans = lines.querySelectorAll(".ch");
      lines.style.transform = "translateY(0)";
      if (spans.length > 1) lineH = spans[0].offsetHeight || 30;
      paint(0);
    }
    function paint(typedLen) {
      var v = input.value, correct = 0, keep = true;
      for (var i = 0; i < spans.length; i++) {
        var s = spans[i], cls = "ch" + (T.spaced && spans[i].classList.contains("sp") ? " sp" : "");
        if (i < v.length) {
          if (v.charAt(i) === T.text.charAt(i)) { cls += " good"; if (keep) correct++; }
          else { cls += " bad"; keep = false; }
        } else if (i === v.length) cls += " cur";
        s.className = cls;
      }
      if (spans[v.length]) {
        var top = spans[v.length].offsetTop;
        lines.style.transform = "translateY(" + (-Math.max(0, top - lineH)) + "px)";
      }
      progEl.textContent = Math.round(correct / T.text.length * 100);
      return correct;
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = ((performance.now() - startTs) / 1000).toFixed(1);
      raf = requestAnimationFrame(tick);
    }
    function begin() { state = "running"; startTs = performance.now(); passage.classList.remove("blurred"); restart.hidden = false; tick(); }
    function onInput() {
      if (state === "done") return;
      if (state === "idle") begin();
      if (input.value.length > T.text.length) input.value = input.value.slice(0, T.text.length);
      paint();
      if (input.value === T.text) finish();
    }
    function finish() {
      cancelAnimationFrame(raf); state = "done";
      var secs = (performance.now() - startTs) / 1000;
      play.hidden = true; input.blur();
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: secs, formatted: secs.toFixed(1),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      cancelAnimationFrame(raf); state = "idle"; input.value = "";
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; timerEl.textContent = "0.0"; progEl.textContent = "0";
      passage.classList.add("blurred"); renderSeq();
    }

    passage.addEventListener("pointerdown", function (e) { e.preventDefault(); input.focus(); });
    input.addEventListener("input", onInput);
    input.addEventListener("focus", function () { if (state !== "done") passage.classList.remove("blurred"); });
    input.addEventListener("blur", function () { if (state === "idle") passage.classList.add("blurred"); });
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
