/* ==========================================================================
   SPEEDLAB — site.js
   Wires shared header controls (sound toggle) + records the visit streak on
   pages that are not test pages. Test pages do this inside their own script.
   ========================================================================== */
(function () {
  "use strict";
  function init() {
    if (!window.SPEEDLAB) return;
    SPEEDLAB.sound.initToggle(document.getElementById("soundToggle"));
    SPEEDLAB.streak.record();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
