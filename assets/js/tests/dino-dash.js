/* ==========================================================================
   SPEEDLAB — tests/dino-dash.js
   Dino Dash: an endless runner. Jump over cacti, duck under birds, and survive
   as the world speeds up. Score is the distance you cover (higher is better).
   Keyboard: Space/Up = jump, Down = duck. Touch: on-screen Jump/Duck + tap.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }

  // logical canvas world
  var CW = 900, CH = 260, GY = 222;
  var PX = 90, PW = 44, STAND_H = 46, DUCK_H = 26;
  var GRAV = 2400, JUMP_V = -830, SPEED0 = 340, ACCEL = 14, SPEED_MAX = 900;
  var COL = { screen: "#0B0716", ink: "#F6F1FF", dim: "#4b3d6b", amber: "#FFC531", cactus: "#2BE86B", bird: "#FF3D7F", ground: "#6b5c8f" };

  function init() {
    var root = $("dino");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.dino;
    var storageKey = "dino", testName = "Dino Dash";
    var screen = $("screen"), play = $("play"), result = $("result");
    var canvas = $("dinoCanvas"), ctx = canvas.getContext("2d");
    var hint = $("dinoHint"), scoreEl = $("score"), bestEl = $("best");
    var jumpBtn = $("jumpBtn"), duckBtn = $("duckBtn"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    canvas.width = CW; canvas.height = CH;

    var state, score, speed, elapsed, feetY, vy, jumping, ducking, obs, spawnTimer, frame, noSpawn = false, raf = 0, last = 0;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb).toLocaleString();
      bestEl.textContent = pb === null ? "0" : Math.round(pb).toLocaleString();
    }
    function reset() {
      cancelAnimationFrame(raf);
      state = "ready"; score = 0; speed = SPEED0; elapsed = 0;
      feetY = GY; vy = 0; jumping = false; ducking = false; obs = []; spawnTimer = 1.2; frame = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = true; hint.hidden = false; hint.textContent = "Press Space or tap to run";
      scoreEl.textContent = "0"; paintPB();
      last = 0; raf = requestAnimationFrame(loop);
    }
    function start() {
      if (state !== "ready") return;
      state = "playing"; hint.hidden = true; restart.hidden = false;
    }
    function jump() {
      if (state === "ready") start();
      if (state !== "playing") return;
      if (!jumping) { jumping = true; vy = JUMP_V; }
    }
    function setDuck(on) {
      ducking = !!on;
      if (on && state === "ready") start();
    }
    function gapTime() { return (300 + Math.random() * 260) / speed + Math.random() * 0.25; }
    function spawnObstacle(type) {
      if (!type) type = (score > 300 && Math.random() < 0.28) ? "bird" : "cactus";
      if (type === "bird") {
        obs.push({ type: "bird", x: CW + 10, y: GY - 48, w: 40, h: 20 });
      } else {
        var n = Math.random() < 0.3 ? 2 : 1, h = 34 + Math.floor(Math.random() * 20);
        obs.push({ type: "cactus", x: CW + 10, y: GY - h, w: 18 * n + 6, h: h });
      }
    }
    function rects() {
      var curH = (ducking && !jumping) ? DUCK_H : STAND_H;
      var top = feetY - curH;
      return { x: PX + 6, y: top + 4, w: PW - 12, h: curH - 6 };
    }
    function hits(p, o) {
      return p.x < o.x + o.w && p.x + p.w > o.x && p.y < o.y + o.h && p.y + p.h > o.y;
    }
    function update(dt) {
      if (state !== "playing") return;
      elapsed += dt; frame += dt;
      speed = Math.min(SPEED_MAX, SPEED0 + ACCEL * elapsed);
      if (jumping) { vy += GRAV * dt; feetY += vy * dt; if (feetY >= GY) { feetY = GY; vy = 0; jumping = false; } }
      if (!noSpawn) { spawnTimer -= dt; if (spawnTimer <= 0) { spawnObstacle(); spawnTimer = gapTime(); } }
      for (var i = obs.length - 1; i >= 0; i--) {
        obs[i].x -= speed * dt;
        if (obs[i].x + obs[i].w < -20) obs.splice(i, 1);
      }
      var p = rects();
      for (i = 0; i < obs.length; i++) if (hits(p, obs[i])) { gameOver(); return; }
      score += speed * dt / 10;
      scoreEl.textContent = Math.floor(score).toLocaleString();
      if (Math.floor(score) > (S.getPB(storageKey) || 0)) bestEl.textContent = Math.floor(score).toLocaleString();
    }
    function gameOver() {
      state = "over"; cancelAnimationFrame(raf);
      var sc = Math.floor(score);
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: sc, formatted: sc.toLocaleString(),
        detail: "Reached " + sc.toLocaleString() + " m",
        screen: screen, onRestart: reset
      });
      paintPB();
    }

    // ---- rendering ----
    function drawDino(top, curH) {
      ctx.fillStyle = COL.ink;
      if (curH === DUCK_H) {
        ctx.fillRect(PX, top + 4, 52, 18);            // long low body
        ctx.fillRect(PX + 40, top, 16, 14);           // head
        ctx.fillStyle = COL.screen; ctx.fillRect(PX + 50, top + 4, 3, 3); // eye
        ctx.fillStyle = COL.ink;
        var d = (Math.floor(frame * 14) % 2) ? 0 : 4;
        ctx.fillRect(PX + 8, top + 22, 8, 6 - d); ctx.fillRect(PX + 26, top + 22, 8, 2 + d);
        return;
      }
      ctx.fillRect(PX + 6, top + 10, 24, 26);         // body
      ctx.fillRect(PX + 24, top, 20, 20);             // head
      ctx.fillRect(PX, top + 16, 12, 8);              // tail
      ctx.fillStyle = COL.screen; ctx.fillRect(PX + 38, top + 5, 3, 3); ctx.fillStyle = COL.ink;
      // legs (alternate)
      var a = (Math.floor(frame * 14) % 2) ? 0 : 6;
      ctx.fillRect(PX + 10, top + 36, 8, 10 - a);
      ctx.fillRect(PX + 22, top + 36, 8, 4 + a);
    }
    function render() {
      ctx.fillStyle = COL.screen; ctx.fillRect(0, 0, CW, CH);
      // ground line + moving dashes
      ctx.fillStyle = COL.ground; ctx.fillRect(0, GY, CW, 3);
      ctx.fillStyle = COL.dim;
      var off = Math.floor((elapsed * (speed || SPEED0)) % 40);
      for (var x = -off; x < CW; x += 40) ctx.fillRect(x, GY + 10, 14, 3);
      // obstacles
      obs.forEach(function (o) {
        if (o.type === "cactus") {
          ctx.fillStyle = COL.cactus;
          ctx.fillRect(o.x, o.y, o.w, o.h);
          ctx.fillRect(o.x - 5, o.y + o.h * 0.4, 5, 10);
          ctx.fillRect(o.x + o.w, o.y + o.h * 0.25, 5, 10);
        } else {
          ctx.fillStyle = COL.bird;
          ctx.fillRect(o.x + 8, o.y + 7, 24, 7);       // body
          var up = (Math.floor(frame * 8) % 2) === 0;
          if (up) { ctx.fillRect(o.x, o.y - 4, 14, 6); ctx.fillRect(o.x + 26, o.y - 4, 14, 6); }
          else { ctx.fillRect(o.x, o.y + 12, 14, 6); ctx.fillRect(o.x + 26, o.y + 12, 14, 6); }
        }
      });
      // player
      var curH = (ducking && !jumping) ? DUCK_H : STAND_H;
      drawDino(feetY - curH, curH);
    }
    function loop(ts) {
      if (!last) last = ts;
      var dt = Math.min(0.05, (ts - last) / 1000); last = ts;
      update(dt); render();
      raf = requestAnimationFrame(loop);
    }

    // ---- input ----
    document.addEventListener("keydown", function (e) {
      var ae = document.activeElement;
      if (ae && /^(INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      if (e.key === " " || e.code === "Space" || e.key === "ArrowUp" || e.key === "w" || e.key === "W") {
        e.preventDefault(); if (state === "over") return; jump();
      } else if (e.key === "ArrowDown" || e.key === "s" || e.key === "S") {
        e.preventDefault(); setDuck(true);
      }
    });
    document.addEventListener("keyup", function (e) {
      if (e.key === "ArrowDown" || e.key === "s" || e.key === "S") setDuck(false);
    });
    var stage = $("dinoStage");
    stage.addEventListener("pointerdown", function (e) { e.preventDefault(); jump(); });
    jumpBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); jump(); });
    duckBtn.addEventListener("pointerdown", function (e) { e.preventDefault(); setDuck(true); });
    duckBtn.addEventListener("pointerup", function () { setDuck(false); });
    duckBtn.addEventListener("pointerleave", function () { setDuck(false); });
    duckBtn.addEventListener("pointercancel", function () { setDuck(false); });
    restart.addEventListener("click", function () { reset(); });
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    if (new URLSearchParams(location.search).get("test") === "1") {
      window.__dino = {
        start: start, jump: jump, setDuck: setDuck,
        update: function (dt) { update(dt); },
        spawn: function (t, x) { spawnObstacle(t); if (x != null) obs[obs.length - 1].x = x; },
        noSpawn: function (b) { noSpawn = b; },
        getState: function () { return { state: state, score: Math.floor(score), obs: obs.length, ox: obs.length ? obs[0].x : null, jumping: jumping, ducking: ducking, feetY: feetY }; },
        reset: reset
      };
    }

    reset();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
