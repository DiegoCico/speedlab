/* ==========================================================================
   SPEEDLAB — tests/clicker.js
   Generic "count events in a window" test, driven entirely by data-* on the
   root <section id="clicker">. Powers Tap Speed and Key Press from one file —
   a new counter test is just markup + a config entry.

   Root attributes:
     data-testid     key into SPEEDLAB.config (ranks + percentiles + unit)
     data-input      "pointer" | "key"
     data-key        for key input: " " for spacebar, "a" for a letter, ""=any
     data-durations  comma list of seconds; "0" means the no-timer option
     data-default    which duration is active on load
     data-name       base test name (duration is appended for share text)
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("clicker");
    if (!root || !window.SPEEDLAB) return;

    var testId = root.getAttribute("data-testid");
    var conf = SPEEDLAB.config[testId];
    if (!conf) return;
    var input = root.getAttribute("data-input") || "pointer";
    var key = root.getAttribute("data-key");
    if (key === "") key = null;                 // empty attr = "any key"
    var buttonAttr = root.getAttribute("data-button");   // "right" = right button only
    var baseName = root.getAttribute("data-name") || "Speed Test";
    var unit = conf.unit;

    var pbValEl = document.querySelector("[data-pb]");
    function keyFor(n) { return n > 0 ? testId + "-" + n + "s" : testId + "-inf"; }
    function nameFor(n) {
      return n > 0 ? baseName + " (" + n + " Second" + (n === 1 ? "" : "s") + ")"
                   : baseName + " (No Timer)";
    }
    function paintPB() {
      var pb = SPEEDLAB.getPB(conf2.storageKey);
      pbValEl.textContent = pb === null ? "—" : (Math.round(pb * 10) / 10).toFixed(1) + " " + unit;
    }

    var current = parseInt(root.getAttribute("data-default") || "10", 10);

    var conf2 = {
      testId: testId,
      input: input,
      key: key,
      button: buttonAttr === "right" ? 2 : (buttonAttr === "left" ? 0 : null),
      duration: current,
      storageKey: keyFor(current),
      testName: nameFor(current),
      formatScore: function (n) { return n.toFixed(1); },
      els: {
        screen: $("screen"), play: $("play"), pad: $("pad"),
        count: $("clicks"), timer: $("timer"),
        result: $("result"), restart: $("restart"),
        pbStrip: { _paint: paintPB }
      }
    };

    var game = SPEEDLAB.counterTest(conf2);
    paintPB();

    var opts = root.querySelectorAll(".seg-select .opt");
    Array.prototype.forEach.call(opts, function (b) {
      if (b.tagName === "A") return;   // variant pages use links; let them navigate
      b.addEventListener("click", function () {
        var n = parseInt(b.getAttribute("data-dur"), 10);
        conf2.duration = n;
        conf2.storageKey = keyFor(n);
        conf2.testName = nameFor(n);
        current = n;
        Array.prototype.forEach.call(opts, function (o) { o.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        game.reset();
        paintPB();
        b.blur(); // release focus so the next key press counts as a play
        if (window.getSelection) { try { window.getSelection().removeAllRanges(); } catch (e) {} }
      });
    });

    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () {
      SPEEDLAB.clearScores(conf2.storageKey); paintPB();
    });

    SPEEDLAB.sound.initToggle($("soundToggle"));
    SPEEDLAB.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
