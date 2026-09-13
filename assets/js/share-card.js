/* ==========================================================================
   SPEEDLAB — share-card.js
   Draws a 1080×1080 result card on a <canvas> (score + rank + site name)
   and downloads it as a PNG. No network — everything is drawn locally.
   ========================================================================== */
(function () {
  "use strict";
  var SPEEDLAB = window.SPEEDLAB || (window.SPEEDLAB = {});

  var C = {
    bg: "#1A1030", dot: "#241640", screen: "#0B0716", ink: "#F6F1FF",
    dim: "#A99FC7", amber: "#FFC531", line: "#000000", p1: "#FF3D7F"
  };
  var TIER_COLORS = ["#5A6A99", "#00C2FF", "#2BE86B", "#B6FF3D", "#FFC531", "#FF8A00", "#FF3D7F"];

  function rr(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }
  // filled panel with a hard black keyline (no soft shadow)
  function panel(ctx, x, y, w, h, r, fill, lw) {
    ctx.fillStyle = C.line; rr(ctx, x - lw, y - lw, w + lw * 2, h + lw * 2, r + lw); ctx.fill();
    ctx.fillStyle = fill; rr(ctx, x, y, w, h, r); ctx.fill();
  }

  function render(ctx, S, data) {
    var tierIndex = Math.max(0, TIER_COLORS.indexOf(data.rankColor));
    // background + dot texture
    ctx.fillStyle = C.bg; ctx.fillRect(0, 0, S, S);
    ctx.fillStyle = C.dot;
    for (var y = 0; y < S; y += 44) for (var x = 0; x < S; x += 44) {
      ctx.beginPath(); ctx.arc(x, y, 2.5, 0, Math.PI * 2); ctx.fill();
    }
    // outer cabinet frame
    ctx.strokeStyle = C.line; ctx.lineWidth = 14;
    ctx.strokeRect(28, 28, S - 56, S - 56);

    // marquee
    panel(ctx, 90, 80, S - 180, 130, 16, C.p1, 8);
    ctx.fillStyle = C.line;
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.font = '900 78px Archivo, system-ui, sans-serif';
    ctx.fillText("SPEEDLAB", S / 2, 148);

    // screen with the score
    panel(ctx, 90, 250, S - 180, 470, 20, C.screen, 8);
    // scanlines
    ctx.fillStyle = "rgba(0,0,0,0.28)";
    for (var sy = 250; sy < 720; sy += 6) ctx.fillRect(90, sy, S - 180, 2);

    ctx.fillStyle = C.dim;
    ctx.font = '800 34px Archivo, system-ui, sans-serif';
    ctx.fillText((data.testName || "").toUpperCase(), S / 2, 320);

    // big segmented score
    ctx.save();
    ctx.shadowColor = "rgba(255,197,49,0.55)"; ctx.shadowBlur = 40;
    ctx.fillStyle = C.amber;
    ctx.font = '700 260px DSEG7, "Archivo", monospace';
    ctx.fillText(String(data.score), S / 2, 500);
    ctx.restore();

    ctx.fillStyle = C.dim;
    ctx.font = '800 46px Archivo, system-ui, sans-serif';
    ctx.fillText(String(data.unit || ""), S / 2, 650);

    // rank name + power meter
    ctx.fillStyle = data.rankColor || C.amber;
    ctx.font = '900 92px Archivo, system-ui, sans-serif';
    ctx.fillText(String(data.rankName || "").toUpperCase(), S / 2, 820);

    var cells = 7, cw = 46, gap = 12, totalW = cells * cw + (cells - 1) * gap;
    var mx = (S - totalW) / 2, my = 880;
    for (var i = 0; i < cells; i++) {
      var cx = mx + i * (cw + gap);
      ctx.fillStyle = C.line; ctx.fillRect(cx - 3, my - 3, cw + 6, 60 + 6);
      ctx.fillStyle = i <= tierIndex ? (data.rankColor || C.amber) : "#2a1f47";
      ctx.fillRect(cx, my, cw, 60);
    }

    // percentile
    ctx.fillStyle = C.ink;
    ctx.font = '800 42px Archivo, system-ui, sans-serif';
    ctx.fillText("Faster than " + data.pct + "% of people", S / 2, 995);

    // footer url
    ctx.fillStyle = C.dim;
    ctx.font = '700 34px Archivo, system-ui, sans-serif';
    ctx.fillText("speedlab.lol", S / 2, 1045);
  }

  function build(data, cb) {
    var S = 1080;
    var canvas = document.createElement("canvas");
    canvas.width = S; canvas.height = S;
    var ctx = canvas.getContext("2d");
    var fonts = window.document.fonts;
    var ready = fonts && fonts.load
      ? Promise.all([
          fonts.load('900 78px Archivo'),
          fonts.load('700 100px "DSEG7"')
        ]).catch(function () {})
      : Promise.resolve();
    ready.then(function () { render(ctx, S, data); cb(canvas); });
  }

  SPEEDLAB.shareCard = {
    build: build,
    download: function (data) {
      build(data, function (canvas) {
        var name = "speedlab-" + slug(data.testName) + "-" +
          String(data.score).replace(/[^0-9]/g, "-") + ".png";
        if (canvas.toBlob) {
          canvas.toBlob(function (blob) {
            var url = URL.createObjectURL(blob);
            trigger(url, name);
            setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
          }, "image/png");
        } else {
          trigger(canvas.toDataURL("image/png"), name);
        }
      });
    }
  };

  function trigger(href, name) {
    var a = document.createElement("a");
    a.href = href; a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
  }
  function slug(s) { return String(s || "score").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }
})();
