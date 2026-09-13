/* ==========================================================================
   SPEEDLAB — tests/cps.js
   CPS (clicks-per-second) test. A thin config over SPEEDLAB.counterTest.
   Duration is switchable in-place; personal bests are stored per duration.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("cps");
    if (!root || !window.SPEEDLAB) return;

    var pbValEl = document.querySelector("[data-pb]");
    function ordinalName(n) { return "CPS Test (" + n + " Second" + (n === 1 ? "" : "s") + ")"; }
    function paintPB() {
      var pb = SPEEDLAB.getPB(conf.storageKey);
      pbValEl.textContent = pb === null ? "—" : (Math.round(pb * 10) / 10).toFixed(1) + " CPS";
    }

    var current = parseInt(root.getAttribute("data-duration") || "5", 10);

    var conf = {
      testId: "cps",
      input: "pointer",
      duration: current,
      storageKey: "cps-" + current + "s",
      testName: ordinalName(current),
      formatScore: function (n) { return n.toFixed(1); },
      els: {
        screen: $("screen"),
        play: $("play"),
        pad: $("pad"),
        count: $("clicks"),
        timer: $("timer"),
        result: $("result"),
        restart: $("restart"),
        pbStrip: { _paint: paintPB }
      }
    };

    var game = SPEEDLAB.counterTest(conf);
    paintPB();

    // Duration selector — switches the live test and its stored best.
    var opts = root.querySelectorAll(".seg-select .opt");
    Array.prototype.forEach.call(opts, function (b) {
      b.addEventListener("click", function () {
        var n = parseInt(b.getAttribute("data-dur"), 10);
        conf.duration = n;
        conf.storageKey = "cps-" + n + "s";
        conf.testName = ordinalName(n);
        current = n;
        Array.prototype.forEach.call(opts, function (o) { o.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        game.reset();
        paintPB();
      });
    });

    // Clear-scores button in the PB strip (clears the current duration).
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () {
      SPEEDLAB.clearScores(conf.storageKey);
      paintPB();
    });

    // Sound toggle + daily streak.
    SPEEDLAB.sound.initToggle($("soundToggle"));
    SPEEDLAB.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
