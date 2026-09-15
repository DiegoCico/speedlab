CABINET = """    <section class="cabinet" id="stopclock" aria-label="Stop the clock">
      <div class="marquee">Stop the Clock</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="round">1/5</span></div>
              <div class="readout-label">Round</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="last">&mdash;</span></div>
              <div class="readout-label">Last miss (ms)</div>
            </div>
          </div>
          <div class="clock-area">
            <div class="clock-target" id="target">Stop at <b>3.500</b></div>
            <div class="clock-face" id="clock">0.000</div>
            <div class="clock-msg" id="msg">Press Start, then stop the clock on target.</div>
            <button class="arcade-btn p1" id="pad" type="button" aria-describedby="msg">
              <span data-pad-title>Start</span>
            </button>
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
    "slug": "stop-the-clock",
    "name": "Stop the Clock",
    "crumb": "Stop the Clock",
    "skip_target": "pad",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/stop-the-clock.js"],
    "title": "Stop the Clock — Timing Precision Game | SpeedLab",
    "desc": "Stop the running clock as close to the target time as you can. Five rounds, scored by your average miss in milliseconds. Test your timing precision.",
    "ld_desc": "Stop a running clock as close to the target time as possible, scored by your average miss in milliseconds.",
    "og_title": "Stop the Clock — Timing Precision Game",
    "og_desc": "How close can you stop the clock to the target?",
    "og_image": "stop-the-clock.png",
    "h1": "Stop the Clock",
    "lead": "A clock counts up — stop it as close to the target time as you can. Five rounds, and your score is the average miss in milliseconds. Lower is better.",
    "content": """      <h2>How the stop the clock game works</h2>
      <p>Each round shows a target time, like <strong>3.500</strong> seconds. Press Start and the clock counts up fast. Hit Stop the instant you think it has reached the target. Your <strong>miss</strong> is how far off you were, in milliseconds — and after five rounds your score is the average of all five. It's pure timing precision: no waiting for a random signal, just you against the clock.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Over 400 ms</strong> — still getting a feel for it.</li>
        <li><strong>150 to 250 ms</strong> — a decent sense of timing.</li>
        <li><strong>40 to 90 ms</strong> — sharp; you're reading the clock well.</li>
        <li><strong>Under 40 ms</strong> — bullseye territory.</li>
      </ul>

      <h2>Tips to stop closer</h2>
      <ul>
        <li><strong>Watch the tenths, not the thousandths</strong> — the last digits move too fast to track.</li>
        <li><strong>Pre-load the press</strong> so your finger fires the moment the tenths flip.</li>
        <li><strong>Note early vs late</strong> — the game tells you which, so adjust on the next round.</li>
      </ul>
      <p>Like timing challenges? Try the <a href="/reaction-time-test/">reaction time test</a> or <a href="/audio-reaction-test/">audio reaction test</a>.</p>""",
    "faq": [
        ("How is Stop the Clock scored?",
         "By your average miss across five rounds. Each round measures how far your stop was from the target, in milliseconds, and lower is better."),
        ("Is this the same as a reaction time test?",
         "No. A reaction test measures how fast you respond to a surprise signal. Here you know the target in advance, so it tests timing precision and anticipation instead."),
        ("What is a good stop the clock score?",
         "An average miss of 150 to 250 ms is decent, 40 to 90 ms is sharp, and under 40 ms is bullseye level."),
        ("Does it work on a phone?",
         "Yes. Tap Start, then tap Stop when the clock hits the target."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "audio-reaction-test", "kbd": "Reaction", "name": "Audio Reaction Test", "desc": "React to the beep."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets fast."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
