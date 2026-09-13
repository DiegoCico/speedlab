/* ==========================================================================
   SPEEDLAB — tests/spacebar.js
   Spacebar Clicker. A key-input config over SPEEDLAB.counterTest, with an
   extra "no timer / count forever" mode (duration 0). Bests stored per mode.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  function init() {
    var root = $("spacebar");
    if (!root || !window.SPEEDLAB) return;

    var pbValEl = document.querySelector("[data-pb]");
    function keyFor(n) { return n > 0 ? "spacebar-" + n + "s" : "spacebar-inf"; }
    function nameFor(n) { return n > 0 ? "Spacebar Clicker (" + n + " Seconds)" : "Spacebar Clicker (No Timer)"; }
    function paintPB() {
      var pb = SPEEDLAB.getPB(conf.storageKey);
      pbValEl.textContent = pb === null ? "—" : (Math.round(pb * 10) / 10).toFixed(1) + " CPS";
    }

    var current = parseInt(root.getAttribute("data-duration") || "10", 10);

    var conf = {
      testId: "spacebar",
      input: "key",
      key: " ",
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

    var game = SPEEDLAB.counterTest(conf);
    paintPB();

    var opts = root.querySelectorAll(".seg-select .opt");
    Array.prototype.forEach.call(opts, function (b) {
      b.addEventListener("click", function () {
        var n = parseInt(b.getAttribute("data-dur"), 10);
        conf.duration = n;
        conf.storageKey = keyFor(n);
        conf.testName = nameFor(n);
        current = n;
        Array.prototype.forEach.call(opts, function (o) { o.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        game.reset();
        paintPB();
        b.blur(); // release focus so the next spacebar press counts as a play
        if (window.getSelection) { try { window.getSelection().removeAllRanges(); } catch (e) {} }
      });
    });

    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () {
      SPEEDLAB.clearScores(conf.storageKey); paintPB();
    });

    SPEEDLAB.sound.initToggle($("soundToggle"));
    SPEEDLAB.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
