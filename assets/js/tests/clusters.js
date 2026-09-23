/* ==========================================================================
   SPEEDLAB — tests/clusters.js
   Clusters: sort 16 words into 4 hidden groups of 4. Four mistakes allowed.
   Score is out of 100 — perfect (no mistakes) is 100; each mistake costs 20;
   a failed board scores by how many groups you found. Higher is better.
   ========================================================================== */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var MAX_MISTAKES = 4;

  /* Each puzzle: 4 groups of 4 words, ordered easiest -> hardest (colour). */
  var PUZZLES = [
    {groups:[
      {name:"Colours",words:["Red","Blue","Green","Pink"]},
      {name:"Fruits",words:["Apple","Mango","Peach","Grape"]},
      {name:"Animals",words:["Tiger","Zebra","Otter","Koala"]},
      {name:"Sports",words:["Rugby","Tennis","Boxing","Hockey"]}]},
    {groups:[
      {name:"___ Ball",words:["Base","Basket","Foot","Volley"]},
      {name:"Planets",words:["Mars","Venus","Earth","Saturn"]},
      {name:"Card suits",words:["Hearts","Spades","Clubs","Diamonds"]},
      {name:"Chess pieces",words:["King","Queen","Rook","Knight"]}]},
    {groups:[
      {name:"Emotions",words:["Happy","Angry","Bored","Proud"]},
      {name:"Weather",words:["Rain","Snow","Wind","Storm"]},
      {name:"Trees",words:["Oak","Pine","Maple","Birch"]},
      {name:"Metals",words:["Gold","Iron","Copper","Zinc"]}]},
    {groups:[
      {name:"Toppings",words:["Cheese","Olive","Onion","Bacon"]},
      {name:"Dances",words:["Salsa","Tango","Waltz","Hiphop"]},
      {name:"Body parts",words:["Elbow","Ankle","Wrist","Spine"]},
      {name:"Bugs",words:["Ant","Wasp","Moth","Beetle"]}]},
    {groups:[
      {name:"Ocean life",words:["Shark","Whale","Squid","Crab"]},
      {name:"Board games",words:["Chess","Clue","Risk","Sorry"]},
      {name:"Instruments",words:["Piano","Flute","Drums","Cello"]},
      {name:"Continents",words:["Asia","Africa","Europe","Oceania"]}]},
    {groups:[
      {name:"Ice cream",words:["Vanilla","Mint","Mocha","Cookie"]},
      {name:"Subjects",words:["Math","Science","History","Art"]},
      {name:"Shapes",words:["Circle","Square","Oval","Hexagon"]},
      {name:"Money",words:["Dollar","Euro","Yen","Pound"]}]},
    {groups:[
      {name:"Days",words:["Monday","Friday","Sunday","Tuesday"]},
      {name:"Months",words:["March","April","June","August"]},
      {name:"Seasons",words:["Spring","Summer","Autumn","Winter"]},
      {name:"Directions",words:["North","South","East","West"]}]},
    {groups:[
      {name:"Reptiles",words:["Snake","Gecko","Cobra","Iguana"]},
      {name:"Big cats",words:["Lion","Puma","Jaguar","Leopard"]},
      {name:"Birds",words:["Robin","Eagle","Sparrow","Owl"]},
      {name:"Fast movers",words:["Cheetah","Falcon","Horse","Hare"]}]},
    {groups:[
      {name:"Pasta",words:["Penne","Ravioli","Fusilli","Lasagna"]},
      {name:"Breakfast",words:["Eggs","Toast","Cereal","Waffle"]},
      {name:"Drinks",words:["Water","Juice","Cola","Cocoa"]},
      {name:"Desserts",words:["Cake","Donut","Pie","Brownie"]}]},
    {groups:[
      {name:"In space",words:["Comet","Nebula","Meteor","Galaxy"]},
      {name:"Code langs",words:["Python","Java","Ruby","Swift"]},
      {name:"Time units",words:["Second","Minute","Hour","Week"]},
      {name:"Gaming",words:["Level","Score","Boss","Quest"]}]},
    {groups:[
      {name:"Landforms",words:["Valley","Plateau","Canyon","Dune"]},
      {name:"Water",words:["River","Lake","Ocean","Pond"]},
      {name:"Rocks",words:["Granite","Marble","Slate","Basalt"]},
      {name:"Weather",words:["Thunder","Fog","Hail","Breeze"]}]},
    {groups:[
      {name:"Vegetables",words:["Carrot","Potato","Onion","Pea"]},
      {name:"Berries",words:["Straw","Blue","Rasp","Black"]},
      {name:"Nuts",words:["Cashew","Almond","Peanut","Walnut"]},
      {name:"Herbs",words:["Basil","Mint","Thyme","Sage"]}]},
    {groups:[
      {name:"Tools",words:["Hammer","Wrench","Drill","Pliers"]},
      {name:"Furniture",words:["Chair","Table","Sofa","Shelf"]},
      {name:"Clothing",words:["Shirt","Jacket","Jeans","Scarf"]},
      {name:"Kitchen",words:["Spoon","Whisk","Ladle","Grater"]}]},
    {groups:[
      {name:"Colours",words:["Amber","Teal","Coral","Olive"]},
      {name:"Gems",words:["Ruby","Pearl","Opal","Topaz"]},
      {name:"Flowers",words:["Rose","Tulip","Daisy","Lily"]},
      {name:"Spices",words:["Pepper","Ginger","Nutmeg","Clove"]}]},
    {groups:[
      {name:"Vehicles",words:["Truck","Van","Bus","Scooter"]},
      {name:"Boats",words:["Canoe","Yacht","Ferry","Kayak"]},
      {name:"Aircraft",words:["Jet","Glider","Chopper","Blimp"]},
      {name:"Trains",words:["Metro","Tram","Bullet","Freight"]}]},
    {groups:[
      {name:"Card games",words:["Poker","Rummy","Bridge","Snap"]},
      {name:"Pool/Snooker",words:["Cue","Pocket","Break","Rack"]},
      {name:"Darts",words:["Bull","Treble","Oche","Flight"]},
      {name:"Bowling",words:["Strike","Spare","Pin","Lane"]}]}
  ];

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  function init() {
    var root = $("clusters");
    if (!root || !window.SPEEDLAB) return;
    var S = window.SPEEDLAB, conf = S.config.clusters;
    var storageKey = "clusters", testName = "Clusters";
    var screen = $("screen"), play = $("play"), result = $("result");
    var solvedEl = $("clSolved"), gridEl = $("clGrid"), msgEl = $("clMsg");
    var livesEl = $("lives"), countEl = $("solvedCount");
    var submitBtn = $("submitBtn"), shuffleBtn = $("shuffleBtn"), restart = $("restart");
    var pbValEl = document.querySelector("[data-pb]");

    var puzzle, selected, solvedIdx, mistakes, state;

    function paintPB() {
      var pb = S.getPB(storageKey);
      pbValEl.textContent = pb === null ? "—" : Math.round(pb) + " pts";
    }
    function wordToGroup(w) {
      for (var i = 0; i < puzzle.groups.length; i++) if (puzzle.groups[i].words.indexOf(w) >= 0) return i;
      return -1;
    }
    function renderGrid() {
      gridEl.innerHTML = "";
      var remaining = [];
      puzzle.groups.forEach(function (g, gi) {
        if (solvedIdx.indexOf(gi) < 0) remaining = remaining.concat(g.words);
      });
      shuffle(remaining).forEach(function (w) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "cl-tile"; b.textContent = w; b.dataset.word = w;
        if (selected.indexOf(w) >= 0) b.classList.add("sel");
        b.addEventListener("click", function () { toggle(w, b); });
        gridEl.appendChild(b);
      });
    }
    function renderSolvedRow(gi, revealed) {
      var g = puzzle.groups[gi];
      var row = document.createElement("div");
      row.className = "cl-solved-row cl-g" + gi + (revealed ? " rev" : "");
      row.innerHTML = '<span class="cat">' + g.name + '</span><span class="ws">' + g.words.join(" · ") + '</span>';
      solvedEl.appendChild(row);
    }
    function toggle(w, b) {
      if (state !== "playing") return;
      var i = selected.indexOf(w);
      if (i >= 0) { selected.splice(i, 1); b.classList.remove("sel"); }
      else if (selected.length < 4) { selected.push(w); b.classList.add("sel"); }
      submitBtn.disabled = selected.length !== 4;
      msgEl.textContent = "";
    }
    function updateHud() {
      livesEl.textContent = MAX_MISTAKES - mistakes;
      countEl.textContent = solvedIdx.length + "/4";
    }
    function solveGroup(gi) {
      solvedIdx.push(gi);
      renderSolvedRow(gi, false);
      selected = []; submitBtn.disabled = true;
      S.sound.click();
      updateHud();
      // solving three leaves exactly one group — auto-complete it
      if (solvedIdx.length === 3) {
        for (var i = 0; i < 4; i++) if (solvedIdx.indexOf(i) < 0) { solveGroup(i); break; }
        return;
      }
      if (solvedIdx.length === 4) { renderGrid(); finish(true); return; }
      renderGrid();
      msgEl.textContent = "Nice!";
    }
    function wrong() {
      mistakes++; updateHud();
      // "one away" if 3 of the 4 selected share a group
      var counts = {};
      selected.forEach(function (w) { var g = wordToGroup(w); counts[g] = (counts[g] || 0) + 1; });
      var max = Math.max.apply(null, Object.keys(counts).map(function (k) { return counts[k]; }));
      msgEl.textContent = max === 3 ? "So close — one away!" : "Not a group.";
      var tiles = gridEl.querySelectorAll(".cl-tile.sel");
      tiles.forEach(function (t) { t.classList.add("shake"); setTimeout(function () { t.classList.remove("shake", "sel"); }, 320); });
      selected = []; submitBtn.disabled = true;
      if (mistakes >= MAX_MISTAKES) lose();
    }
    function submit() {
      if (state !== "playing" || selected.length !== 4) return;
      var gi = -1;
      for (var i = 0; i < puzzle.groups.length; i++) {
        if (solvedIdx.indexOf(i) >= 0) continue;
        if (selected.every(function (w) { return puzzle.groups[i].words.indexOf(w) >= 0; })) { gi = i; break; }
      }
      if (gi >= 0) solveGroup(gi); else wrong();
    }
    function lose() {
      state = "revealing";
      msgEl.textContent = "Out of tries — here were the groups.";
      puzzle.groups.forEach(function (g, gi) { if (solvedIdx.indexOf(gi) < 0) renderSolvedRow(gi, true); });
      gridEl.innerHTML = "";
      setTimeout(function () { finish(false); }, 1500);
    }
    function finish(win) {
      state = "done";
      var scoreVal = win ? Math.max(0, 100 - 20 * mistakes) : 20 * solvedIdx.length;
      play.hidden = true;
      S.renderResult({
        cfg: conf, storageKey: storageKey, container: result,
        testName: testName, score: scoreVal, formatted: scoreVal + " pts",
        detail: win ? ("Solved with " + mistakes + " mistake" + (mistakes === 1 ? "" : "s"))
                    : ("Found " + solvedIdx.length + " of 4 groups"),
        screen: screen, onRestart: reset
      });
      paintPB();
    }
    function reset() {
      state = "playing";
      puzzle = PUZZLES[Math.floor(Math.random() * PUZZLES.length)];
      selected = []; solvedIdx = []; mistakes = 0;
      play.hidden = false; result.classList.remove("show"); result.innerHTML = "";
      restart.hidden = false; solvedEl.innerHTML = ""; msgEl.textContent = "Find the four hidden groups of four.";
      submitBtn.disabled = true;
      updateHud(); renderGrid();
    }

    submitBtn.addEventListener("click", submit);
    shuffleBtn.addEventListener("click", function () { if (state === "playing") renderGrid(); });
    restart.addEventListener("click", reset);
    var clearBtn = document.querySelector("[data-clear]");
    if (clearBtn) clearBtn.addEventListener("click", function () { S.clearScores(storageKey); paintPB(); });

    if (new URLSearchParams(location.search).get("test") === "1") {
      window.__clusters = {
        groups: function () { return puzzle.groups; },
        selectWords: function (arr) {
          selected = [];
          gridEl.querySelectorAll(".cl-tile").forEach(function (b) {
            b.classList.remove("sel");
            if (arr.indexOf(b.dataset.word) >= 0) { selected.push(b.dataset.word); b.classList.add("sel"); }
          });
          submitBtn.disabled = selected.length !== 4;
        },
        submit: submit,
        state: function () { return { mistakes: mistakes, solved: solvedIdx.length, state: state }; }
      };
    }

    reset(); paintPB();
    S.sound.initToggle($("soundToggle"));
    S.streak.record();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
