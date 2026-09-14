/* ==========================================================================
   SPEEDLAB — tests/ai-or-human.js
   AI or Human? A short line of text appears; decide whether a person or an AI
   wrote it, as fast as you can. 60-second round, tracking correct vs wrong.
   Score is correct calls (higher is better), with accuracy shown.
   The labels reflect common "AI writing tells" — it's a fun/learning game,
   not a definitive detector.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 60;

  // ai:true = written to sound like generic AI; ai:false = a human's messy, specific line
  var SNIPPETS = [
    { t: "It's important to note that both options have their own unique advantages and disadvantages.", ai: true },
    { t: "honestly the bus was 20 min late again and i almost missed my chem exam lol", ai: false },
    { t: "In today's fast-paced world, staying organized is more important than ever before.", ai: true },
    { t: "my cat knocked my coffee onto my laptop this morning, the L key is completely toast now", ai: false },
    { t: "Ultimately, the best choice depends on your individual needs, preferences, and goals.", ai: true },
    { t: "we lost 3-2 in overtime and i'm still kind of mad about that ref call tbh", ai: false },
    { t: "This dish offers a delightful balance of flavors that is sure to please any palate.", ai: true },
    { t: "the wifi in my dorm dies every night around 11 and it is driving me insane", ai: false },
    { t: "By leveraging these strategies, you can unlock your full potential and achieve success.", ai: true },
    { t: "planted tomatoes in april, forgot about them, somehow they're thriving??", ai: false },
    { t: "There are several key factors to consider when making this important decision.", ai: true },
    { t: "my little brother beat me at mario kart and now he won't stop bringing it up", ai: false },
    { t: "Whether you're a beginner or an expert, there's truly something here for everyone.", ai: true },
    { t: "took the long way home just to avoid that one awful intersection, worth it", ai: false },
    { t: "Let's delve into the rich tapestry of possibilities this topic has to offer.", ai: true },
    { t: "there's a dog on my street that howls at the garbage truck every single tuesday", ai: false },
    { t: "Overall, it was a memorable experience that I would highly recommend to others.", ai: true },
    { t: "got caught in the rain with no jacket, my shoes still aren't dry two days later", ai: false },
    { t: "Remember, consistency is truly key when it comes to building lasting habits.", ai: true },
    { t: "the printer at work jams every single time i'm in a hurry, i swear it knows", ai: false },
    { t: "In conclusion, the benefits clearly outweigh the drawbacks in most scenarios.", ai: true },
    { t: "spent way too much on concert tickets but zero regrets, front row baby", ai: false },
    { t: "Navigating the complexities of modern life can feel overwhelming at times.", ai: true },
    { t: "my grandma makes this weird jello salad every thanksgiving and nobody eats it but her", ai: false },
    { t: "This product seamlessly combines style, functionality, and affordability.", ai: true },
    { t: "watched the sunrise after an all-nighter, kinda regret it but the sky was unreal", ai: false },
    { t: "It's worth mentioning that results may vary depending on a range of factors.", ai: true },
    { t: "my roommate labeled all his food in the fridge, even the ketchup. who does that", ai: false },
    { t: "From bustling cities to serene countryside, this region truly has it all.", ai: true },
    { t: "i keep meaning to fix my bike tire but it's been flat for like a month now", ai: false },
    { t: "Embracing change is the first step toward meaningful personal growth and development.", ai: true },
    { t: "the coffee machine at the office only works if you hit it in exactly the right spot", ai: false },
    { t: "With its sleek design and powerful features, this device truly stands out.", ai: true },
    { t: "i can't believe they cancelled the show after one season, it was actually good", ai: false },
    { t: "Each chapter builds upon the last, creating a cohesive and engaging journey.", ai: true },
    { t: "ok i tried the new ramen place and the broth was way too salty, wouldn't go back", ai: false }
  ];

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  function init() {
    var root = $("aihuman");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.aihuman;
    var storageKey = "aihuman", testName = "AI or Human";
    var screen = $("screen"), play = $("play"), result = $("result"), area = $("area");
    var promptEl = $("prompt"), correctEl = $("correct"), wrongEl = $("wrong"), timerEl = $("timer");
    var humanBtn = $("humanBtn"), aiBtn = $("aiBtn"), startBtn = $("startBtn"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", correct = 0, wrong = 0, startTs = 0, raf = 0, endTimer = 0;
    var pool = [], idx = 0, curAI = false;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " correct";
    }
    function setEnabled(on) { humanBtn.disabled = !on; aiBtn.disabled = !on; }
    function nextPrompt() {
      if (idx >= pool.length) { pool = shuffle(pool); idx = 0; }
      var s = pool[idx++]; curAI = s.ai;
      promptEl.textContent = "“" + s.t + "”";
    }
    function flash(good) {
      if (S.reduceMotion) return;
      area.classList.remove("flash-good", "flash-bad"); void area.offsetWidth;
      area.classList.add(good ? "flash-good" : "flash-bad");
    }
    function answer(saidAI) {
      if (state !== "running") return;
      if (saidAI === curAI) { correct++; correctEl.textContent = correct; S.sound.click(); flash(true); }
      else { wrong++; wrongEl.textContent = wrong; flash(false); }
      nextPrompt();
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function begin() {
      state = "running"; correct = 0; wrong = 0; correctEl.textContent = "0"; wrongEl.textContent = "0";
      pool = shuffle(SNIPPETS.slice()); idx = 0;
      startBtn.hidden = true; restart.hidden = false; setEnabled(true);
      startTs = performance.now(); endTimer = setTimeout(finish, DURATION * 1000);
      tick(); nextPrompt();
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer); setEnabled(false);
      play.hidden = true;
      var total = correct + wrong, acc = total ? Math.round(correct / total * 100) : 0;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: correct, formatted: String(correct),
        screen: screen, onRestart: reset
      });
      var p = document.createElement("p"); p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = correct + " correct · " + wrong + " wrong · " + acc + "% accuracy";
      result.appendChild(p);
      paintPB();
    }
    function reset() {
      state = "idle"; correct = 0; wrong = 0; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      startBtn.hidden = false; restart.hidden = true; setEnabled(false);
      correctEl.textContent = "0"; wrongEl.textContent = "0"; timerEl.textContent = DURATION;
      promptEl.textContent = "Tap Start, then decide: did a human or an AI write each line?";
    }

    startBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); begin(); });
    humanBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); answer(false); });
    aiBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); answer(true); });
    restart.addEventListener("click", reset);
    document.addEventListener("keydown", function (e) {
      if (state !== "running") return;
      if (e.key === "ArrowLeft" || e.key === "h" || e.key === "H") { e.preventDefault(); answer(false); }
      else if (e.key === "ArrowRight" || e.key === "a" || e.key === "A") { e.preventDefault(); answer(true); }
    });
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
