HOLES = "\n".join(
    ['          <button class="mole-hole" type="button" aria-label="Mole hole"></button>'] * 9)

CABINET = """    <section class="cabinet" id="whack" aria-label="Whack-a-mole">
      <div class="marquee">Whack-a-Mole</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="hits">0</span></div>
              <div class="readout-label">Hits</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">30</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="mole-wrap">
            <div class="mole-grid" id="grid">
%HOLES%
            </div>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
        <button class="arcade-btn" id="restart" type="button" hidden>Restart</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>""".replace("%HOLES%", HOLES)

SPEC = {
    "slug": "whack-a-mole",
    "name": "Whack-a-Mole",
    "crumb": "Whack-a-Mole",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/whack-a-mole.js"],
    "title": "Whack-a-Mole — Reflex &amp; Reaction Game | SpeedLab",
    "desc": "Play whack-a-mole and test your reflexes. Bop as many moles as you can in 30 seconds, see your rank, and beat your best. Works on mouse and touch.",
    "ld_desc": "Bop as many moles as you can in 30 seconds in this reflex game.",
    "og_title": "Whack-a-Mole — Reflex Game",
    "og_desc": "Bop as many moles as you can in 30 seconds. Test your reflexes.",
    "og_image": "whack-a-mole.png",
    "h1": "Whack-a-Mole",
    "lead": "Moles pop up around the grid, one at a time. Bop as many as you can before they duck back down. You have 30 seconds — how many can you hit?",
    "content": """      <h2>How whack-a-mole works</h2>
      <p>Press start and moles begin popping up in the nine holes, one at a time. Click or tap a mole while it is up to score a hit; if you are too slow it ducks back down and the next one appears somewhere else. You have <strong>30 seconds</strong>, and your score is the number of moles you bop. The moles get a little quicker as the clock runs down, so a strong finish really counts.</p>

      <h2>What is a good score?</h2>
      <p>Because the moles speed up, the last ten seconds are where good players pull ahead. As a rough guide:</p>
      <ul>
        <li><strong>Under 10 hits</strong> &mdash; just getting warmed up.</li>
        <li><strong>16 to 22 hits</strong> &mdash; a solid, steady round.</li>
        <li><strong>28 to 35 hits</strong> &mdash; fast reflexes and good accuracy.</li>
        <li><strong>40+ hits</strong> &mdash; excellent; you barely miss a mole.</li>
      </ul>

      <h2>Tips to score higher</h2>
      <ul>
        <li><strong>Rest your gaze on the centre</strong> of the grid so you can see every hole at once.</li>
        <li><strong>Move to the mole, don't hunt for it</strong> &mdash; trust the movement you catch out of the corner of your eye.</li>
        <li><strong>Don't over-click.</strong> One accurate tap per mole beats mashing the grid.</li>
      </ul>
      <p>Enjoy this? The <a href="/aim-trainer/">aim trainer</a> is the precision version, and the <a href="/reaction-time-test/">reaction time test</a> measures your raw reflexes.</p>""",
    "faq": [
        ("How long is a round of whack-a-mole?",
         "Each round lasts 30 seconds. Your score is the total number of moles you hit before time runs out."),
        ("What is a good whack-a-mole score?",
         "Around 16 to 22 hits is a solid round. 28 to 35 is fast, and 40 or more is excellent."),
        ("Do the moles get faster?",
         "Yes. The time each mole stays up slowly shrinks as the clock counts down, so the final seconds are the hardest."),
        ("Does it work on a phone?",
         "Yes. Tap the moles instead of clicking. The grid and timing work exactly the same on touch."),
    ],
    "related": [
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
