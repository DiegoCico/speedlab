/* ==========================================================================
   SPEEDLAB — tests/typing.js
   Typing Speed Test (WPM). Type the passage; the timer starts on your first
   keystroke. Live net WPM = (correct chars / 5) / minutes, plus accuracy.
   Durations 15 / 30 / 60s, each with its own personal best.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  /* A big library of varied, general-audience sentences. Each run shuffles
     and samples these, so the passage is effectively never the same twice and
     covers a wide vocabulary — no single text to memorise. */
  var SENTENCES = [
    "The quick brown fox jumps over the lazy dog near the river.",
    "A cup of hot chocolate tastes best on a cold winter morning.",
    "Bright yellow buses lined up outside the school gates at eight.",
    "The old lighthouse blinked steadily through the thick grey fog.",
    "She packed her bag with snacks, a map, and a warm jacket.",
    "Deep in the forest, an owl watched the moon rise over the pines.",
    "Every planet in our solar system travels around the sun.",
    "The chef sliced fresh tomatoes and scattered basil on the pizza.",
    "A gentle breeze carried the smell of rain across the open field.",
    "Curious dolphins followed the small boat all the way to shore.",
    "He tightened his laces and sprinted the last lap of the race.",
    "The library was silent except for the soft turning of pages.",
    "Colorful kites danced above the beach on that windy afternoon.",
    "Fresh bread from the bakery filled the whole street with warmth.",
    "The train rattled past green hills and quiet little villages.",
    "Stars appeared one by one as the sky slowly turned dark blue.",
    "Her drawing showed a castle, a dragon, and a bright orange sun.",
    "The scientist recorded every result carefully in her notebook.",
    "Tall waves crashed against the rocks and sprayed the wooden pier.",
    "A tiny spider spun a perfect web between the garden fence posts.",
    "They roasted marshmallows and told stories around the campfire.",
    "The city lights sparkled like scattered jewels far below the plane.",
    "Grandma's recipe called for two eggs, some sugar, and fresh lemon.",
    "The puppy chased its tail in happy circles across the lawn.",
    "Snow fell quietly, covering the rooftops in a soft white blanket.",
    "The museum displayed ancient coins, old maps, and giant fossils.",
    "A rainbow stretched across the valley after the summer storm.",
    "He fixed the bike chain, pumped the tires, and rode off grinning.",
    "The band practiced late, filling the garage with loud, happy noise.",
    "Bees moved from flower to flower, gathering pollen in the sun.",
    "The astronaut floated gently past the window of the space station.",
    "Warm sand slipped between our toes as we walked along the coast.",
    "The clever raccoon opened the latch and stole the picnic basket.",
    "Autumn leaves crunched under our boots on the long forest trail.",
    "She solved the tricky puzzle just before the timer ran out.",
    "The market buzzed with music, bright stalls, and the smell of spice.",
    "A single candle lit the room while the storm raged outside.",
    "The farmer watched the wheat sway like golden waves in the wind.",
    "Two friends built a fort out of blankets and old cardboard boxes.",
    "The river wound slowly through the canyon, carving the red stone.",
    "He counted the stars until his eyes grew heavy and he fell asleep.",
    "The robot rolled across the floor, beeping softly as it worked.",
    "Fresh mint and cold lemonade made the hot afternoon feel easy.",
    "The mountain peak vanished into a ring of thick white clouds.",
    "Her kite climbed higher and higher until it was just a tiny dot.",
    "The cat stretched, yawned, and curled up in the warm patch of sun.",
    "We followed the winding path down to the quiet hidden beach.",
    "The teacher smiled as the class finally understood the puzzle.",
    "A brave little mouse crept past the sleeping cat to reach the cheese.",
    "Thunder rumbled far away while we played cards by the window.",
    "The garden burst into color when spring finally arrived that year.",
    "Sailboats drifted across the bay under a clear and endless sky.",
    "He wrote a short note, folded it twice, and slid it under the door.",
    "The bakery sold out of donuts before the morning was even over.",
    "Fireflies blinked in the tall grass as the summer night grew cool."
  ];

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function buildPassage(minWords) {
    var pool = shuffle(SENTENCES.slice()), out = [], count = 0, k = 0;
    while (count < minWords) {
      if (k >= pool.length) { pool = shuffle(SENTENCES.slice()); k = 0; }
      var s = pool[k++];
      out.push(s); count += s.split(" ").length;
    }
    return out.join(" ");
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
      var words = buildPassage(220).split(" ");
      target = words.join(" ");
      // Each word is one wrap unit (letters stay together); a space span sits
      // between words as the wrap point. Span order matches target char order.
      var html = "";
      for (var w = 0; w < words.length; w++) {
        html += '<span class="word">';
        for (var j = 0; j < words[w].length; j++) html += '<span class="ch">' + words[w].charAt(j) + "</span>";
        html += "</span>";
        if (w < words.length - 1) html += '<span class="ch sp"> </span>';
      }
      lines.innerHTML = html;
      spans = lines.querySelectorAll(".ch");
      lines.style.transform = "translateY(0)";
      if (spans.length > 1) lineH = spans[0].offsetHeight || 30;
      paintCursor(0, 0);
    }

    function paintCursor(typedLen, correct) {
      for (var i = 0; i < spans.length; i++) {
        var s = spans[i], cls = "ch" + (target.charAt(i) === " " ? " sp" : "");
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
