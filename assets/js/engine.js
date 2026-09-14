/* ==========================================================================
   SPEEDLAB — engine.js
   Shared test engine: config registry, localStorage personal bests, rank
   mapping, percentile interpolation, sound (off by default), a reusable
   "counter test" harness (CPS / spacebar / tap / key-press ...), the
   result flow, confetti/shake, and streak + daily-challenge helpers.

   Everything hangs off a single global: window.SPEEDLAB
   ========================================================================== */
(function () {
  "use strict";

  var SPEEDLAB = window.SPEEDLAB || {};
  var NS = "speedlab:";
  var reduceMotion = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Rank tiers (shared across all tests) ----------------------------- */
  var TIERS = ["Snail", "Sloth", "Turtle", "Rabbit", "Cheetah", "Falcon", "Lightning"];
  var TIER_COLORS = ["#5A6A99", "#00C2FF", "#2BE86B", "#B6FF3D", "#FFC531", "#FF8A00", "#FF3D7F"];

  /* ---- Per-test config registry ----------------------------------------
     One place to tune ranks + percentile tables (see spec).
     bounds: 6 ascending cut points splitting scores into the 7 tiers.
     dist:   [value, %ofPeopleAtOrBelowValue] ascending — for interpolation.
     Derived from published human averages (CPS ~6.5, reaction ~270ms).      */
  SPEEDLAB.config = {
    cps: {
      unit: "CPS", higherIsBetter: true,
      bounds: [3, 4.5, 6, 7.5, 9, 11],
      dist: [[1,1],[2,4],[3,9],[4,19],[5,33],[6,48],[6.5,55],[7,63],
             [8,78],[9,88],[10,93],[11,96],[12,98],[14,99.5],[16,99.9]]
    },
    spacebar: {
      unit: "CPS", higherIsBetter: true,
      bounds: [3, 4.5, 6, 7.5, 9, 11],
      dist: [[1,1],[2,4],[3,9],[4,19],[5,33],[6,48],[6.5,55],[7,63],
             [8,78],[9,88],[10,93],[11,96],[12,98],[14,99.5],[16,99.9]]
    },
    reaction: {
      unit: "ms", higherIsBetter: false,
      bounds: [180, 210, 240, 280, 330, 400],
      dist: [[150,1],[180,4],[200,10],[220,22],[240,38],[260,52],[270,58],
             [285,66],[300,74],[330,85],[360,92],[400,96],[450,98.5],[550,99.7]]
    },
    /* Tap mirrors a normal click; Key Press mirrors the spacebar. */
    tap: {
      unit: "TPS", higherIsBetter: true,
      bounds: [3, 4.5, 6, 7.5, 9, 11],
      dist: [[1,1],[2,4],[3,9],[4,19],[5,33],[6,48],[6.5,55],[7,63],
             [8,78],[9,88],[10,93],[11,96],[12,98],[14,99.5],[16,99.9]]
    },
    keypress: {
      unit: "KPS", higherIsBetter: true,
      bounds: [4, 5.5, 7, 8.5, 10, 12],
      dist: [[2,2],[3,6],[4,14],[5,26],[6,40],[7,54],[8,68],[9,80],
             [10,88],[11,93],[12,96],[14,99],[16,99.8]]
    },
    rightclick: {
      unit: "CPS", higherIsBetter: true,
      bounds: [2.5, 4, 5.5, 7, 8.5, 10],
      dist: [[1,2],[2,8],[3,18],[4,33],[5,50],[6,66],[7,79],[8,88],
             [9,93],[10,96],[12,99],[14,99.8]]
    },
    typing: {
      unit: "WPM", higherIsBetter: true,
      bounds: [25, 40, 55, 70, 90, 110],
      dist: [[10,1],[20,8],[30,22],[40,42],[45,52],[50,62],[60,78],[70,88],
             [80,94],[90,97],[100,98.5],[120,99.6],[140,99.9]]
    },
    aim: {                       /* milliseconds per target — lower is better */
      unit: "ms", higherIsBetter: false,
      bounds: [300, 400, 500, 650, 850, 1100],
      dist: [[220,1],[280,6],[340,18],[400,32],[470,48],[550,63],[650,77],
             [800,88],[950,94],[1200,98],[1600,99.6]]
    },
    whack: {                     /* moles bopped in 30s — higher is better */
      unit: "hits", higherIsBetter: true,
      bounds: [10, 16, 22, 28, 35, 43],
      dist: [[4,3],[8,12],[12,26],[16,42],[22,60],[28,76],[35,88],
             [43,95],[52,99]]
    },
    alphabet: {                  /* seconds to type A-Z — lower is better */
      unit: "s", higherIsBetter: false,
      bounds: [6, 8, 11, 15, 20, 28],
      dist: [[4,1],[6,10],[8,28],[10,45],[13,62],[16,76],[20,88],[26,95],[35,99]]
    },
    number: {                    /* seconds to type 1-100 — lower is better */
      unit: "s", higherIsBetter: false,
      bounds: [35, 50, 70, 95, 130, 180],
      dist: [[25,1],[35,12],[45,28],[55,42],[70,58],[90,74],[115,87],[150,95],[210,99]]
    },
    audioreaction: {             /* ms to react to a beep — lower is better */
      unit: "ms", higherIsBetter: false,
      bounds: [160, 190, 220, 260, 320, 400],
      dist: [[130,1],[160,6],[185,18],[210,34],[235,50],[260,64],[290,77],
             [330,88],[400,95],[480,99]]
    },
    stroop: {                    /* correct answers in 30s — higher is better */
      unit: "correct", higherIsBetter: true,
      bounds: [8, 14, 20, 26, 33, 40],
      dist: [[4,3],[8,14],[14,32],[20,52],[26,70],[33,85],[40,94],[48,99]]
    },
    numbermemory: {              /* digits remembered — higher is better */
      unit: "digits", higherIsBetter: true,
      bounds: [4, 6, 8, 10, 12, 14],
      dist: [[3,2],[5,15],[6,30],[7,48],[8,63],[9,75],[10,85],[11,91],[13,97],[16,99.5]]
    },
    sequencemem: {               /* longest sequence — higher is better */
      unit: "level", higherIsBetter: true,
      bounds: [4, 6, 8, 10, 13, 16],
      dist: [[2,2],[4,16],[6,38],[8,60],[10,78],[12,89],[15,96],[20,99.5]]
    },
    visualmem: {                 /* level reached — higher is better */
      unit: "level", higherIsBetter: true,
      bounds: [4, 6, 8, 10, 12, 15],
      dist: [[2,2],[4,18],[6,40],[8,62],[10,80],[12,90],[15,97],[18,99.5]]
    },
    chimp: {                     /* numbers reached — higher is better */
      unit: "numbers", higherIsBetter: true,
      bounds: [6, 8, 10, 12, 15, 18],
      dist: [[4,3],[6,15],[8,35],[10,58],[12,76],[14,88],[16,94],[20,99]]
    },
    scroll: {                    /* pixels scrolled in 10s — higher is better */
      unit: "px", higherIsBetter: true,
      bounds: [6000, 12000, 20000, 30000, 45000, 65000],
      dist: [[2000,2],[6000,15],[12000,35],[20000,55],[30000,72],[45000,87],[65000,96],[90000,99.5]]
    },
    swipe: {                     /* swipes in 10s — higher is better */
      unit: "swipes", higherIsBetter: true,
      bounds: [8, 14, 20, 26, 34, 44],
      dist: [[4,3],[8,15],[14,35],[20,55],[26,72],[34,87],[44,96],[55,99]]
    },
    emoji: {                     /* rounds cleared — higher is better */
      unit: "level", higherIsBetter: true,
      bounds: [3, 6, 9, 13, 18, 24],
      dist: [[1,3],[3,18],[6,40],[9,60],[13,78],[18,90],[24,97],[30,99.5]]
    },
    wordguess: {                 /* guesses to solve — lower is better */
      unit: "guesses", higherIsBetter: false,
      bounds: [1, 2, 3, 4, 5, 6],
      dist: [[1,2],[2,10],[3,35],[4,68],[5,88],[6,97],[7,100]]
    },
    aihuman: {                   /* correct out of 5 — higher is better */
      unit: "correct", higherIsBetter: true,
      bounds: [0, 1, 2, 3, 4, 5],
      dist: [[0,4],[1,14],[2,32],[3,56],[4,80],[5,95]]
    }
  };

  /* ---- Storage (safe against private-mode / disabled localStorage) ------ */
  var store = {
    get: function (k) {
      try { return window.localStorage.getItem(NS + k); } catch (e) { return null; }
    },
    set: function (k, v) {
      try { window.localStorage.setItem(NS + k, v); } catch (e) {}
    },
    del: function (k) {
      try { window.localStorage.removeItem(NS + k); } catch (e) {}
    },
    keys: function () {
      var out = [];
      try {
        for (var i = 0; i < window.localStorage.length; i++) {
          var key = window.localStorage.key(i);
          if (key && key.indexOf(NS) === 0) out.push(key);
        }
      } catch (e) {}
      return out;
    }
  };
  SPEEDLAB.store = store;

  /* ---- Personal bests --------------------------------------------------- */
  SPEEDLAB.getPB = function (storageKey) {
    var v = store.get("pb:" + storageKey);
    return v === null ? null : parseFloat(v);
  };
  SPEEDLAB.savePB = function (storageKey, value, higherIsBetter) {
    var cur = SPEEDLAB.getPB(storageKey);
    var better = cur === null ||
      (higherIsBetter ? value > cur : value < cur);
    if (better) { store.set("pb:" + storageKey, String(value)); return true; }
    return false;
  };
  SPEEDLAB.clearScores = function (storageKey) { store.del("pb:" + storageKey); };
  SPEEDLAB.clearAll = function () { store.keys().forEach(function (k) { try { window.localStorage.removeItem(k); } catch (e) {} }); };

  /* ---- Ranks ------------------------------------------------------------ */
  SPEEDLAB.rankFor = function (cfg, value) {
    var b = cfg.bounds, idx = 0, i;
    if (cfg.higherIsBetter) {
      for (i = 0; i < b.length; i++) if (value >= b[i]) idx++;
    } else {
      for (i = 0; i < b.length; i++) if (value <= b[i]) idx++;
    }
    if (idx > 6) idx = 6; if (idx < 0) idx = 0;
    return { index: idx, name: TIERS[idx], color: TIER_COLORS[idx] };
  };

  /* ---- Percentile: "faster than X% of people" --------------------------- */
  SPEEDLAB.percentile = function (cfg, value) {
    var d = cfg.dist, atOrBelow;
    if (value <= d[0][0]) atOrBelow = d[0][1];
    else if (value >= d[d.length - 1][0]) atOrBelow = d[d.length - 1][1];
    else {
      atOrBelow = d[d.length - 1][1];
      for (var i = 0; i < d.length - 1; i++) {
        if (value >= d[i][0] && value <= d[i + 1][0]) {
          var t = (value - d[i][0]) / (d[i + 1][0] - d[i][0]);
          atOrBelow = d[i][1] + t * (d[i + 1][1] - d[i][1]);
          break;
        }
      }
    }
    var faster = cfg.higherIsBetter ? atOrBelow : (100 - atOrBelow);
    faster = Math.round(faster);
    if (faster > 99) faster = 99; if (faster < 1) faster = 1;
    return faster;
  };

  /* ---- Sound (OFF by default — non-negotiable for school devices) ------- */
  var sound = {
    enabled: store.get("sound") === "on",
    ctx: null,
    _ac: function () {
      if (!this.ctx) {
        var AC = window.AudioContext || window.webkitAudioContext;
        if (AC) this.ctx = new AC();
      }
      if (this.ctx && this.ctx.state === "suspended") this.ctx.resume();
      return this.ctx;
    },
    tone: function (freq, dur, type, vol) {
      if (!this.enabled) return;
      var ac = this._ac(); if (!ac) return;
      var o = ac.createOscillator(), g = ac.createGain();
      o.type = type || "square"; o.frequency.value = freq;
      g.gain.value = vol || 0.05;
      o.connect(g); g.connect(ac.destination);
      var now = ac.currentTime;
      g.gain.setValueAtTime(g.gain.value, now);
      g.gain.exponentialRampToValueAtTime(0.0001, now + (dur || 0.05));
      o.start(now); o.stop(now + (dur || 0.05));
    },
    click: function () { this.tone(880, 0.03, "square", 0.04); },
    beep: function () { this.tone(660, 0.15, "sine", 0.08); },
    success: function () {
      if (!this.enabled) return;
      var self = this, notes = [523, 659, 784, 1047];
      notes.forEach(function (f, i) { setTimeout(function () { self.tone(f, 0.12, "square", 0.06); }, i * 70); });
    },
    setEnabled: function (on) {
      this.enabled = on; store.set("sound", on ? "on" : "off");
      if (on) this._ac();
    },
    initToggle: function (btn) {
      if (!btn) return; var self = this;
      function paint() {
        btn.setAttribute("aria-pressed", self.enabled ? "true" : "false");
        btn.querySelector("[data-sound-label]").textContent = self.enabled ? "Sound: On" : "Sound: Off";
      }
      paint();
      btn.addEventListener("click", function () { self.setEnabled(!self.enabled); paint(); });
    }
  };
  SPEEDLAB.sound = sound;

  /* ---- Motion helpers --------------------------------------------------- */
  SPEEDLAB.shake = function (el) {
    if (reduceMotion || !el) return;
    el.classList.remove("shake"); void el.offsetWidth; el.classList.add("shake");
  };
  SPEEDLAB.confetti = function () {
    if (reduceMotion) return;
    var layer = document.createElement("div");
    layer.className = "confetti-layer";
    var colors = ["#FF3D7F", "#00C2FF", "#FFC531", "#2BE86B", "#F6F1FF"];
    for (var i = 0; i < 70; i++) {
      var b = document.createElement("i");
      b.className = "confetti-bit";
      b.style.left = Math.random() * 100 + "vw";
      b.style.background = colors[i % colors.length];
      b.style.animationDuration = (0.9 + Math.random() * 0.9) + "s";
      b.style.animationDelay = (Math.random() * 0.25) + "s";
      layer.appendChild(b);
    }
    document.body.appendChild(layer);
    setTimeout(function () { layer.remove(); }, 2200);
  };

  /* ---- Rank badge markup ------------------------------------------------ */
  SPEEDLAB.rankBadgeHTML = function (rank) {
    var cells = "";
    for (var i = 0; i < 7; i++) {
      cells += '<span class="cell' + (i <= rank.index ? " on" : "") +
        '" style="--tier:' + rank.color + '"></span>';
    }
    return '<span class="rank-badge"><span class="r-name" style="color:' + rank.color +
      '">' + rank.name + '</span><span class="meter" aria-hidden="true">' + cells +
      '</span></span>';
  };

  /* ---- Result flow (shared by every test) -------------------------------
     opts: { cfg, storageKey, container, testName, score, formatted,
             onRestart, screen (el to shake) }                              */
  SPEEDLAB.renderResult = function (opts) {
    var cfg = opts.cfg;
    var rank = SPEEDLAB.rankFor(cfg, opts.score);
    var pct = SPEEDLAB.percentile(cfg, opts.score);
    var isNew = SPEEDLAB.savePB(opts.storageKey, opts.score, cfg.higherIsBetter);
    var pb = SPEEDLAB.getPB(opts.storageKey);
    var unit = cfg.unit;

    var html =
      '<div class="result-rank">' + SPEEDLAB.rankBadgeHTML(rank) + '</div>' +
      '<div class="readout-row"><div class="readout"><div class="seg-wrap">' +
        '<span class="seg-ghost" aria-hidden="true">' + ghostFor(opts.formatted) + '</span>' +
        '<span class="seg-value go">' + opts.formatted + '</span>' +
      '</div><div class="readout-label">' + unit + '</div></div></div>' +
      '<p class="pct">Faster than <b>' + pct + '%</b> of people</p>' +
      '<div class="stat-line"><span>This run <span class="v">' + opts.formatted + ' ' + unit + '</span></span>' +
        '<span>Best <span class="v' + (isNew ? " new" : "") + '">' + fmtPB(pb) + ' ' + unit + '</span>' +
        (isNew ? ' ⭐ New best!' : '') + '</span></div>' +
      '<div class="result-actions">' +
        '<button class="btn btn-p1" data-act="again">Play again</button>' +
        '<button class="btn btn-p2" data-act="share">Share</button>' +
        '<button class="btn btn-ghost" data-act="copy">Copy result</button>' +
      '</div>' +
      '<p class="visually-hidden" role="status">You scored ' + opts.formatted + ' ' + unit +
        ', rank ' + rank.name + ', faster than ' + pct + ' percent of people.</p>';

    opts.container.innerHTML = html;
    opts.container.classList.add("show");

    if (isNew) { SPEEDLAB.confetti(); SPEEDLAB.shake(opts.screen); sound.success(); }

    var pageUrl = (window.location && window.location.origin)
      ? (window.location.origin + window.location.pathname) : "https://speedlab.lol/";
    var shareData = {
      testName: opts.testName, score: opts.formatted, unit: unit,
      rankName: rank.name, rankColor: rank.color, pct: pct, url: pageUrl,
      shareText: opts.testName + ": " + opts.formatted + " " + unit + " — " +
        rank.name + ", faster than " + pct + "% of people. Beat it:"
    };
    opts.container.querySelector('[data-act="again"]').addEventListener("click", function () {
      opts.container.classList.remove("show");
      opts.container.innerHTML = "";
      if (opts.onRestart) opts.onRestart();
    });
    opts.container.querySelector('[data-act="share"]').addEventListener("click", function () {
      if (SPEEDLAB.shareCard) SPEEDLAB.shareCard.shareResult(shareData);
    });
    var copyBtn = opts.container.querySelector('[data-act="copy"]');
    copyBtn.addEventListener("click", function () {
      var text = opts.testName + ": " + opts.formatted + " " + unit + " — " +
        rank.name + ", faster than " + pct + "% of people. Try it: https://speedlab.lol/";
      copyToClipboard(text, copyBtn);
    });

    return { rank: rank, pct: pct, isNewBest: isNew, pb: pb };
  };

  function fmtPB(pb) { return pb === null ? "—" : (Math.round(pb * 10) / 10); }
  function ghostFor(str) { return String(str).replace(/[0-9]/g, "8"); }

  function copyToClipboard(text, btn) {
    function ok() { if (!btn) return; var old = btn.textContent; btn.textContent = "Copied!"; setTimeout(function () { btn.textContent = old; }, 1400); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok, function () { legacy(); });
    } else { legacy(); }
    function legacy() {
      var ta = document.createElement("textarea"); ta.value = text;
      ta.style.position = "fixed"; ta.style.opacity = "0"; document.body.appendChild(ta);
      ta.select(); try { document.execCommand("copy"); ok(); } catch (e) {}
      ta.remove();
    }
  }
  SPEEDLAB.copyText = copyToClipboard;

  /* ---- PB strip (always-visible "beat this" line under the screen) ------ */
  SPEEDLAB.mountPBStrip = function (el, storageKey, cfg, onClear) {
    if (!el) return;
    function paint() {
      var pb = SPEEDLAB.getPB(storageKey);
      el.querySelector("[data-pb]").textContent = pb === null ? "—" : fmtPB(pb) + " " + cfg.unit;
    }
    paint();
    var clr = el.querySelector("[data-clear]");
    if (clr) clr.addEventListener("click", function () {
      SPEEDLAB.clearScores(storageKey); paint(); if (onClear) onClear();
    });
    el._paint = paint;
    return { paint: paint };
  };

  /* ---- Counter-test harness --------------------------------------------
     Powers every "count events in a window" test (CPS, spacebar, tap,
     key-press...). A new such test is just a config object. Wires input,
     timer, live readout, and the result flow.

     cfg = {
       testId, storageKey, duration (sec; 0 = no timer / forever),
       input: "pointer" | "key", key: " " (optional filter for key mode),
       score: fn(count, elapsedSec) -> number,   default count/elapsed
       formatScore: fn(number) -> string,         default 1 decimal
       testName,                                   for share text
       els: { screen, pad, count, timer, result, pbStrip, restart }
     }                                                                     */
  SPEEDLAB.counterTest = function (cfg) {
    var conf = SPEEDLAB.config[cfg.testId];
    var els = cfg.els;
    // Read live so a single instance can switch between timed and ∞ modes.
    function isForever() { return !cfg.duration || cfg.duration <= 0; }
    var scoreFn = cfg.score || function (c, sec) { return sec > 0 ? c / sec : 0; };
    var fmtFn = cfg.formatScore || function (n) { return (Math.round(n * 10) / 10).toFixed(1); };

    var state = "idle", count = 0, startTs = 0, raf = 0, endTimer = 0;

    function setCount(n) {
      count = n;
      els.count.textContent = n;
      if (!reduceMotion) {
        els.count.classList.remove("tick"); void els.count.offsetWidth; els.count.classList.add("tick");
      }
    }
    function setTimer(sec) {
      if (els.timer) els.timer.textContent = isForever() ? "∞" : Math.ceil(sec);
    }

    function reset() {
      cancelAnimationFrame(raf); clearTimeout(endTimer);
      state = "idle"; count = 0;
      els.count.textContent = "0";
      setTimer(cfg.duration || 0);
      if (els.play) els.play.hidden = false;
      els.result.classList.remove("show"); els.result.innerHTML = "";
      els.pad.classList.remove("is-pressed"); els.pad.classList.add("is-armed");
      els.pad.querySelector("[data-pad-title]").textContent = startWord();
      els.pad.querySelector("[data-pad-hint]").textContent = hintText();
      els.pad.disabled = false;
      if (els.restart) els.restart.hidden = true;
    }
    function startWord() { return cfg.input === "key" ? "PRESS TO START" : "CLICK TO START"; }
    function hintText() {
      if (cfg.input === "key") {
        var k = cfg.key === " " ? "SPACEBAR" : (cfg.key ? ("the " + cfg.key + " key") : "any key");
        return isForever() ? "Hit " + k + " — no timer, count as high as you can" : "Hit " + k + " as fast as you can for " + cfg.duration + "s";
      }
      return isForever() ? "Click here — no timer, count as high as you can" : "Click here as fast as you can for " + cfg.duration + "s";
    }

    function begin() {
      state = "running"; startTs = performance.now();
      var fv = isForever();
      els.pad.classList.remove("is-armed");
      els.pad.querySelector("[data-pad-title]").textContent = fv ? "KEEP GOING" : "GO!";
      els.pad.querySelector("[data-pad-hint]").textContent = fv ? "Hit Stop when you're done" : "";
      if (els.restart) { els.restart.hidden = false; els.restart.textContent = fv ? "Stop" : "Reset"; }
      if (!fv) {
        endTimer = setTimeout(finish, cfg.duration * 1000);
      }
      loop();
    }
    function loop() {
      if (state !== "running") return;
      var elapsed = (performance.now() - startTs) / 1000;
      if (!isForever()) setTimer(Math.max(0, cfg.duration - elapsed));
      raf = requestAnimationFrame(loop);
    }
    function bump() {
      if (state === "done") return;
      if (state === "idle") begin();
      setCount(count + 1);
      sound.click();
      els.pad.classList.add("is-pressed");
    }
    function release() { els.pad.classList.remove("is-pressed"); }

    function finish() {
      if (state === "done") return;
      cancelAnimationFrame(raf); clearTimeout(endTimer);
      state = "done";
      els.pad.disabled = true;
      if (els.play) els.play.hidden = true;
      if (els.restart) els.restart.hidden = true;
      var elapsed = isForever() ? (performance.now() - startTs) / 1000 : cfg.duration;
      var s = scoreFn(count, elapsed);
      SPEEDLAB.renderResult({
        cfg: conf, storageKey: cfg.storageKey, container: els.result,
        testName: cfg.testName, score: s, formatted: fmtFn(s),
        screen: els.screen, onRestart: reset
      });
      if (els.pbStrip && els.pbStrip._paint) els.pbStrip._paint();
    }

    /* input wiring */
    if (cfg.input === "key") {
      // pointer also arms/starts so mobile users aren't stuck
      els.pad.addEventListener("pointerdown", function (e) { e.preventDefault(); bump(); });
      els.pad.addEventListener("pointerup", release);
      document.addEventListener("keydown", function (e) {
        if (state === "done") return;
        // Don't hijack keys aimed at other controls (links, sound toggle...).
        var ae = document.activeElement;
        if (ae && ae !== els.pad && /^(A|BUTTON|SUMMARY|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
        if (cfg.key && e.key !== cfg.key) return;
        if (cfg.key === " " && (e.key === " " || e.code === "Space")) { e.preventDefault(); }
        if (e.repeat) return;               // ignore held-key auto-repeat
        if (!cfg.key && (e.key === "Tab" || e.key === "Enter")) return;
        bump();
      });
      document.addEventListener("keyup", release);
    } else {
      // cfg.button: undefined = any button, 0 = left only, 2 = right only
      els.pad.addEventListener("pointerdown", function (e) {
        e.preventDefault();
        if (cfg.button != null && e.button !== cfg.button) return;
        bump();
      });
      els.pad.addEventListener("pointerup", release);
      els.pad.addEventListener("pointercancel", release);
      els.pad.addEventListener("contextmenu", function (e) { e.preventDefault(); });
      // keyboard users play the pad with Space/Enter while it is focused
      els.pad.addEventListener("keydown", function (e) {
        if (state === "done") return;
        if (e.key === " " || e.key === "Enter" || e.code === "Space") {
          e.preventDefault(); if (e.repeat) return; bump();
        }
      });
      els.pad.addEventListener("keyup", release);
    }

    if (els.restart) els.restart.addEventListener("click", function () {
      if (isForever() && state === "running") { finish(); } else { reset(); }
    });

    reset();
    return { reset: reset, finish: finish, getState: function () { return state; } };
  };

  /* ---- Streak + daily challenge (seeded from the date) ------------------ */
  function todayKey() {
    var d = new Date();
    return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();
  }
  SPEEDLAB.streak = {
    record: function () {
      var last = store.get("streak:last");
      var n = parseInt(store.get("streak:count") || "0", 10) || 0;
      var t = todayKey();
      if (last === t) return n;               // already counted today
      var y = new Date(); y.setDate(y.getDate() - 1);
      var yKey = y.getFullYear() + "-" + (y.getMonth() + 1) + "-" + y.getDate();
      n = (last === yKey) ? n + 1 : 1;
      store.set("streak:last", t); store.set("streak:count", String(n));
      return n;
    },
    get: function () { return parseInt(store.get("streak:count") || "0", 10) || 0; }
  };
  SPEEDLAB.dailyChallenge = function (slugs) {
    if (!slugs || !slugs.length) return null;
    var d = new Date();
    var seed = d.getFullYear() * 1000 + (d.getMonth() * 31) + d.getDate();
    return slugs[seed % slugs.length];
  };

  SPEEDLAB.reduceMotion = reduceMotion;
  window.SPEEDLAB = SPEEDLAB;
})();
