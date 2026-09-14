/* ==========================================================================
   SPEEDLAB — tests/word-guess.js
   A Wordle-style word game. Guess the hidden 5-letter word in 6 tries; tiles
   turn green (right spot), amber (in the word), or grey (not in it). Tracks a
   live timer and the number of guesses; score is guesses used (fewer is
   better), with your solve time shown alongside. Physical + on-screen keyboard.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var ROWS = 6, COLS = 5;

  var WORDS = ("about above actor acute admit adopt adult after again agent agree ahead alarm album alert " +
    "alike alive allow alone along alter angel anger angle ankle apart apple apply arena argue arise armor " +
    "arrow aside asset audio avoid awake award aware badly baker basic beach began begin begun being below " +
    "bench birth black blade blame blank blast blaze blend bless blind block blood bloom board boost booth " +
    "bound brain brake brand brave bread break breed brick bride brief bring broad brown brush build built " +
    "bunch burst cabin cable candy cargo carry catch cause chain chair chalk charm chart chase cheap check " +
    "cheer chess chest chief child chill chose civil claim class clean clear clerk click cliff climb clock " +
    "close cloth cloud coach coast could count court cover crack craft crash crazy cream crisp cross crowd " +
    "crown curve cycle daily dairy dance death delay depth diary dirty ditch dizzy dodge donor doubt dozen " +
    "draft drain drama drank dream dress drift drill drink drive drove drown eagle early earth eaten elbow " +
    "elder elect empty enemy enjoy enter entry equal error essay event every exact exist extra faint fairy " +
    "faith false fancy fault feast fence ferry fever fiber field fiery fight final first flame flash fleet " +
    "flesh float flock flood floor flour fluid flush focus force forge forth forty found frame fresh front " +
    "frost fruit fully funny ghost giant given glass gleam globe glory glove grace grade grain grand grant " +
    "grape graph grass grave great green greet grief grill grind group grove growl grown guard guess guest " +
    "guide habit happy harsh haste hatch haven heart heavy hedge hello honey honor horse hotel house human " +
    "humor hurry ideal image index inner input irony issue ivory jelly jewel joint jolly joker juice kayak " +
    "kneel knife knock known label labor large laser later laugh layer learn lemon level light limit linen " +
    "liver lobby local lodge logic loose lucky lunar lunch magic major maker mango march match maybe mayor " +
    "meant medal melon mercy merge merit metal meter might minor minus mixed model money month moral motor " +
    "mount mouse mouth movie music naive nasty naval nerve never newly night noble noise north novel nurse " +
    "ocean offer often olive onion order organ other ought ounce outer owner ozone panel panic paper party " +
    "pasta patch pause peace pearl pedal penny phase phone photo piano piece pilot pinch pitch pivot pizza " +
    "place plain plane plant plate plaza plead pluck point porch pound power press price pride prime print " +
    "prize proof proud prove pulse punch pupil quest queen quick quiet quite quote radar radio raise rally " +
    "ranch range rapid reach ready realm rebel refer relax reply rider ridge rifle right rigid rinse risky " +
    "rival river roast robot rocky roman round route royal rugby ruler rumor rural saint salad sauce scale " +
    "scare scarf scene scent scoop scope score scout scrap screw sense serve seven shade shake shame shape " +
    "share shark sharp sheep sheet shelf shell shine shiny shirt shock shoot shore short shout showy shrub " +
    "sight silly since sixth sixty skate skill skull slate sleep slice slide slope small smart smash smile " +
    "smoke snack snail snake sneak solar solid solve sorry sound south space spare spark speak spear speed " +
    "spell spend spice spicy spike spine spite split spoke spoon sport spray squad stack staff stage stair " +
    "stamp stand stare start state steam steel steep stern stick stiff still sting stock stone stood stool " +
    "store storm story stove strap straw strip study stuff stump style sugar sunny super surge sweep sweet " +
    "swept swift swing sword table taken taste teach teeth thank theft their theme there thick thief thing " +
    "think third those three threw throw thumb tiger tight timer title toast today token tooth topic torch " +
    "total touch tough tower toxic trace track trade trail train trait tramp trash tread treat trend trial " +
    "tribe trick tried tulip truck truly trunk trust truth twice twist ultra uncle under undue union unite " +
    "unity until upper upset urban usage usual valid value valve vapor vault vigor virus visit vital vocal " +
    "voice voter wagon waist waste watch water wheat wheel where which while white whole whose widen wider " +
    "widow width witch woman world worry worse worst worth would wound woven wrist write wrong wrote yield " +
    "young youth zebra").split(/\s+/).filter(function (w) { return w.length === 5; });

  function init() {
    var root = $("wordguess");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.wordguess;
    var storageKey = "wordguess", testName = "Woordle";
    var screen = $("screen"), play = $("play"), result = $("result");
    var board = $("board"), kbd = $("kbd"), msgEl = $("msg");
    var guessesEl = $("guesses"), timerEl = $("timer"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var answer = "", row = 0, col = 0, cur = "", state = "idle", startTs = 0, raf = 0;
    var tiles = [], keyEls = {};

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " guesses";
    }
    function buildBoard() {
      board.innerHTML = ""; tiles = [];
      for (var r = 0; r < ROWS; r++) {
        for (var c = 0; c < COLS; c++) {
          var t = document.createElement("div"); t.className = "wg-tile"; board.appendChild(t); tiles.push(t);
        }
      }
    }
    function tileAt(r, c) { return tiles[r * COLS + c]; }
    var LAYOUT = ["qwertyuiop", "asdfghjkl", "↵zxcvbnm⌫"]; // enter + backspace glyphs
    function buildKbd() {
      kbd.innerHTML = ""; keyEls = {};
      LAYOUT.forEach(function (rowStr) {
        var rowEl = document.createElement("div"); rowEl.className = "wg-kbd-row";
        rowStr.split("").forEach(function (ch) {
          var k = document.createElement("button"); k.type = "button"; k.className = "wg-key";
          if (ch === "↵") { k.textContent = "Enter"; k.className += " wide"; k.dataset.k = "enter"; }
          else if (ch === "⌫") { k.textContent = "Del"; k.className += " wide"; k.dataset.k = "back"; }
          else { k.textContent = ch; k.dataset.k = ch; keyEls[ch] = k; }
          k.addEventListener("pointerdown", function (e) { e.preventDefault(); handle(k.dataset.k); });
          rowEl.appendChild(k);
        });
        kbd.appendChild(rowEl);
      });
    }

    function newGame() {
      cancelAnimationFrame(raf);
      answer = WORDS[Math.floor(Math.random() * WORDS.length)].toUpperCase();
      row = 0; col = 0; cur = ""; state = "idle";
      buildBoard();
      Object.keys(keyEls).forEach(function (k) { keyEls[k].className = "wg-key"; });
      guessesEl.textContent = "0"; timerEl.textContent = "0"; msgEl.textContent = "";
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = false;
    }
    function tick() {
      if (state !== "playing") return;
      timerEl.textContent = Math.floor((performance.now() - startTs) / 1000);
      raf = requestAnimationFrame(tick);
    }
    function beginIfNeeded() { if (state === "idle") { state = "playing"; startTs = performance.now(); tick(); } }
    function flash(m) { msgEl.textContent = m; setTimeout(function () { if (msgEl.textContent === m) msgEl.textContent = ""; }, 1400); }

    function handle(k) {
      if (state === "done") return;
      if (k === "enter") return submit();
      if (k === "back") { if (col > 0) { col--; cur = cur.slice(0, -1); var t = tileAt(row, col); t.textContent = ""; t.className = "wg-tile"; } return; }
      if (/^[a-z]$/.test(k) && col < COLS) {
        beginIfNeeded();
        var tl = tileAt(row, col); tl.textContent = k; tl.className = "wg-tile filled";
        cur += k.toUpperCase(); col++;
      }
    }
    function submit() {
      if (cur.length < COLS) { flash("Not enough letters"); shakeRow(); return; }
      // two-pass evaluation so duplicate letters colour correctly
      var res = new Array(COLS).fill("absent");
      var counts = {}; var i, ch;
      for (i = 0; i < COLS; i++) { ch = answer[i]; counts[ch] = (counts[ch] || 0) + 1; }
      for (i = 0; i < COLS; i++) { if (cur[i] === answer[i]) { res[i] = "correct"; counts[cur[i]]--; } }
      for (i = 0; i < COLS; i++) {
        if (res[i] === "correct") continue;
        if (counts[cur[i]] > 0) { res[i] = "present"; counts[cur[i]]--; }
      }
      for (i = 0; i < COLS; i++) {
        var t = tileAt(row, i); t.className = "wg-tile " + res[i];
        var kEl = keyEls[cur[i].toLowerCase()];
        if (kEl) {  // upgrade key colour only (absent < present < correct)
          var rank = { absent: 1, present: 2, correct: 3 };
          var have = kEl.classList.contains("correct") ? 3 : kEl.classList.contains("present") ? 2 : kEl.classList.contains("absent") ? 1 : 0;
          if (rank[res[i]] > have) { kEl.classList.remove("absent", "present", "correct"); kEl.classList.add(res[i]); }
        }
      }
      S.sound.click();
      guessesEl.textContent = row + 1;
      if (cur === answer) return win(row + 1);
      row++; col = 0; cur = "";
      if (row >= ROWS) return lose();
    }
    function shakeRow() {
      for (var c = 0; c < COLS; c++) { var t = tileAt(row, c); t.classList.add("wg-row-shake"); (function (tt) { setTimeout(function () { tt.classList.remove("wg-row-shake"); }, 250); })(t); }
    }
    function win(n) {
      cancelAnimationFrame(raf); state = "done";
      var secs = Math.round((performance.now() - startTs) / 1000);
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: n, formatted: String(n),
        screen: screen, onRestart: newGame
      });
      var p = document.createElement("p"); p.className = "pct"; p.style.color = "var(--c-ink-dim)";
      p.textContent = "Solved “" + answer + "” in " + n + (n === 1 ? " guess" : " guesses") + " · " + secs + "s";
      result.appendChild(p);
      paintPB();
    }
    function lose() {
      cancelAnimationFrame(raf); state = "done";
      play.hidden = true; result.classList.add("show");
      result.innerHTML =
        '<div class="readout-row"><div class="readout"><div class="seg-wrap">' +
        '<span class="seg-value">X</span></div><div class="readout-label">Out of guesses</div></div></div>' +
        '<p class="pct">The word was <b style="color:var(--c-amber)">' + answer + '</b></p>' +
        '<div class="result-actions"><button class="btn btn-p1" data-act="again">Play again</button></div>';
      result.querySelector('[data-act="again"]').addEventListener("click", newGame);
      S.shake(screen);
    }

    document.addEventListener("keydown", function (e) {
      if (state === "done") return;
      var ae = document.activeElement;
      if (ae && /^(A|INPUT|SELECT|TEXTAREA)$/.test(ae.tagName)) return;
      if (e.key === "Enter") { e.preventDefault(); handle("enter"); }
      else if (e.key === "Backspace") { e.preventDefault(); handle("back"); }
      else if (/^[a-zA-Z]$/.test(e.key)) { handle(e.key.toLowerCase()); }
    });

    restart.addEventListener("click", newGame);
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    buildKbd(); newGame(); paintPB();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
