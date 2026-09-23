/* ==========================================================================
   SPEEDLAB — intro.js  (homepage only)
   Full-screen dotted overlay: the speedlab.lol wordmark stamps in, holds, then
   the overlay fades while the wordmark flies to the header's exact position
   (a FLIP hand-off). Runs once per browser session; honours reduced-motion.
   The <html class="intro-on"> gate is set by a tiny inline script in the head
   so the overlay covers the page before first paint (no flash).
   ========================================================================== */
(function () {
  "use strict";
  var html = document.documentElement;
  if (!html.classList.contains("intro-on")) return;

  function run() {
    var intro = document.getElementById("intro");
    var mark = document.getElementById("introMark");
    var brand = document.querySelector(".site-header .brand");
    var done = false;

    function cleanup() {
      if (done) return; done = true;
      try { sessionStorage.setItem("sl_intro", "1"); } catch (e) {}
      html.classList.remove("intro-on");
      if (intro && intro.parentNode) intro.parentNode.removeChild(intro);
      window.removeEventListener("pointerdown", skip, true);
      window.removeEventListener("keydown", skip, true);
    }
    function skip() { cleanup(); }

    if (!intro || !mark || !brand) { cleanup(); return; }

    // Position the mark exactly over the header brand (identity == header).
    var hb = brand.getBoundingClientRect();
    var mw = hb.width || 150, mh = hb.height || 30;
    var vw = window.innerWidth, vh = window.innerHeight;
    mark.style.left = hb.left + "px";
    mark.style.top = hb.top + "px";

    // Big centered start state (transform-origin: top left).
    var K = Math.max(2, Math.min(7, Math.min(vw * 0.62, 560) / mw));
    var cx = vw / 2, cy = vh * 0.44;
    var Tx = cx - hb.left - (mw * K) / 2;
    var Ty = cy - hb.top - (mh * K) / 2;
    mark.style.transform = "translate(" + Tx + "px," + Ty + "px) scale(" + K + ")";
    void mark.offsetWidth;  // commit start state before transition

    window.addEventListener("pointerdown", skip, true);
    window.addEventListener("keydown", skip, true);

    // stamp (~0.55s) + hold, then fly to the header.
    setTimeout(function () {
      if (done) return;
      mark.style.transition = "transform .66s cubic-bezier(.5,0,.15,1)";
      intro.style.transition = "opacity .6s ease .06s";
      mark.style.transform = "translate(0,0) scale(1)";
      intro.style.opacity = "0";
      mark.addEventListener("transitionend", function (e) {
        if (e.propertyName === "transform") cleanup();
      });
      setTimeout(cleanup, 1100);   // fallback if transitionend doesn't fire
    }, 1150);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else { run(); }
})();
