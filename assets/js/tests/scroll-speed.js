/* ==========================================================================
   SPEEDLAB — tests/scroll-speed.js
   Scroll Speed Test: how many pixels can you scroll in 10 seconds. Works with
   a mouse wheel, a trackpad, or a touchscreen. The scroll area loops so you
   can keep going forever; only real movement is counted.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var DURATION = 10;

  function init() {
    var root = $("scrollspeed");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.scroll;
    var storageKey = "scroll", testName = "Scroll Speed Test";
    var screen = $("screen"), play = $("play"), result = $("result");
    var box = $("box"), pxEl = $("px"), timerEl = $("timer"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var state = "idle", total = 0, startTs = 0, raf = 0, endTimer = 0, last = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " px";
    }
    function begin() {
      state = "running"; total = 0; startTs = performance.now();
      restart.hidden = false; box.scrollTop = 1500; last = box.scrollTop;
      endTimer = setTimeout(finish, DURATION * 1000); tick();
    }
    function onScroll() {
      if (state === "done") return;
      if (state === "idle") begin();
      var cur = box.scrollTop;
      var d = Math.abs(cur - last);
      // ignore the jump created when we loop the scroll position
      if (d < 1200) { total += d; pxEl.textContent = Math.round(total); }
      last = cur;
      // loop so scrolling never hits a hard end
      var max = box.scrollHeight - box.clientHeight;
      if (cur > max - 200) { box.scrollTop = 400; last = box.scrollTop; }
      else if (cur < 200) { box.scrollTop = max - 400; last = box.scrollTop; }
    }
    function tick() {
      if (state !== "running") return;
      timerEl.textContent = Math.max(0, Math.ceil(DURATION - (performance.now() - startTs) / 1000));
      raf = requestAnimationFrame(tick);
    }
    function finish() {
      state = "done"; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: Math.round(total), formatted: String(Math.round(total)),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "idle"; total = 0; cancelAnimationFrame(raf); clearTimeout(endTimer);
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; pxEl.textContent = "0"; timerEl.textContent = DURATION;
      box.scrollTop = 1500; last = box.scrollTop;
    }

    box.addEventListener("scroll", onScroll, { passive: true });
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
