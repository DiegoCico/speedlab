CABINET = """    <section class="cabinet" id="dino" aria-label="Dino Dash runner">
      <div class="marquee">Dino Dash</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="score">0</span></div>
              <div class="readout-label">Score</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="best">0</span></div>
              <div class="readout-label">Best</div>
            </div>
          </div>
          <div class="dino-area">
            <div class="dino-stage" id="dinoStage">
              <canvas id="dinoCanvas" width="900" height="260" aria-label="Dino Dash game"></canvas>
              <div class="dino-hint" id="dinoHint">Press Space or tap to run</div>
            </div>
            <div class="dino-controls" id="dinoControls">
              <button class="arcade-btn p1" id="jumpBtn" type="button">Jump</button>
              <button class="arcade-btn p2" id="duckBtn" type="button">Duck</button>
            </div>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn" id="restart" type="button" hidden>Restart</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "dino-game",
    "name": "Dino Dash",
    "crumb": "Dino Dash",
    "skip_target": "jumpBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/dino-dash.js"],
    "title": "Dino Game — Jump & Duck Endless Runner | SpeedLab",
    "desc": "Play the dino game: run, jump over cacti and duck under birds as it speeds up. A free offline-style dinosaur runner that tests your reflexes. No sign-up, works on any device.",
    "ld_desc": "Run, jump over cacti and duck under birds in an endless runner that gets faster over time.",
    "og_title": "Dino Dash — Jump & Duck Runner",
    "og_desc": "Jump the cacti, duck the birds, survive as it speeds up.",
    "og_image": "dino-game.png",
    "h1": "Dino Dash",
    "lead": "Run, jump over the cacti, and duck under the birds. The longer you last the faster it gets — how far can your reflexes take you?",
    "content": """      <h2>How to play Dino Dash</h2>
      <p>Your dino runs on its own. Your job is to react in time: <strong>jump</strong> over the cacti coming along the ground, and <strong>duck</strong> under the birds flying at head height. Every second the whole world speeds up, so the gaps get tighter and your reactions have to get sharper. One hit ends the run, and your score is the distance you covered. It's a pure reflex-and-timing test in the style of the offline dinosaur game.</p>

      <h2>Controls</h2>
      <ul>
        <li><strong>Jump:</strong> Space, Up arrow, W, tap the game, or the Jump button.</li>
        <li><strong>Duck:</strong> hold the Down arrow, S, or the Duck button.</li>
        <li>It works the same with a keyboard, a mouse, or a touchscreen.</li>
      </ul>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 350</strong> — still finding your rhythm.</li>
        <li><strong>600 to 1000</strong> — solid; your timing is dialled in.</li>
        <li><strong>1600 to 2500</strong> — fast reflexes under real pressure.</li>
        <li><strong>2500+</strong> — excellent.</li>
      </ul>

      <h2>Tips to last longer</h2>
      <ul>
        <li><strong>Jump late, not early.</strong> Jumping too soon lands you right on the next cactus.</li>
        <li><strong>Only duck for birds</strong> — stay standing so you're ready to jump the moment a cactus appears.</li>
        <li><strong>Look ahead</strong>, not at your dino, so you read obstacles sooner as the speed climbs.</li>
      </ul>
      <p>Want more reflex challenges? Try the <a href="/reaction-time-test/">reaction time test</a>, <a href="/aim-trainer/">aim trainer</a>, or <a href="/go-no-go/">Go / No-Go</a>.</p>""",
    "faq": [
        ("How do you play the dino game?",
         "Your dino runs automatically. Jump over the cacti and duck under the birds. It gets faster over time, and one hit ends the run — your score is how far you got."),
        ("How do I duck?",
         "Hold the Down arrow or S on a keyboard, or press and hold the Duck button on a touchscreen. Ducking lowers your dino so birds pass safely overhead."),
        ("Does it work on mobile?",
         "Yes. Tap the game or the Jump button to jump, and hold the Duck button to duck. The game scales to any screen size."),
        ("Is it like the Chrome offline dinosaur game?",
         "It's the same style of endless runner — jump and duck through obstacles that speed up — built as its own original game that runs right in your browser."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets fast."},
        {"slug": "go-no-go", "kbd": "Reaction", "name": "Go / No-Go", "desc": "Tap green, hold on red."},
        {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles."},
        {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Stop the timer on target."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
