CABINET = """    <section class="cabinet" id="gonogo" aria-label="Go / No-Go test">
      <div class="marquee">Go / No-Go</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="trial">0/10</span></div>
              <div class="readout-label">Trial</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="correct">0</span></div>
              <div class="readout-label">Correct</div>
            </div>
          </div>
          <div class="gng-stage" id="stage" role="button" tabindex="0" aria-label="Tap on green, hold still on red">
            <div class="gng-label" id="stageLabel">Go / No-Go</div>
            <div class="gng-sub" id="stageSub">Tap on green, hold still on red.</div>
            <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
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
    "slug": "go-no-go",
    "name": "Go / No-Go",
    "crumb": "Go / No-Go",
    "skip_target": "stage",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/go-no-go.js"],
    "title": "Go / No-Go Test — Impulse Control Game | SpeedLab",
    "desc": "Tap on green, hold still on red. The Go/No-Go test measures your impulse control and reaction across 10 quick trials. See how many you get right.",
    "ld_desc": "Tap on green (Go) and hold still on red (No-Go) across 10 trials measuring impulse control.",
    "og_title": "Go / No-Go Test — Impulse Control Game",
    "og_desc": "Tap on green, hold still on red. Can you resist?",
    "og_image": "go-no-go.png",
    "h1": "Go / No-Go Test",
    "lead": "Tap the instant the screen turns green — but hold still when it turns red. Ten quick trials that test your reaction and, harder still, your impulse control.",
    "content": """      <h2>How the Go / No-Go test works</h2>
      <p>Each trial flashes a signal. When it's <strong>green (Go)</strong>, tap as fast as you can. When it's <strong>red (No-Go)</strong>, do nothing at all. Green comes up most of the time, so your reflex builds a habit of tapping — and the red trials test whether you can stop yourself in time. You get one point for every correct response across 10 trials. Tapping on red, or missing a green, costs you.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 5 / 10</strong> — jumping the gun a lot.</li>
        <li><strong>6 to 7 / 10</strong> — good control.</li>
        <li><strong>8 to 9 / 10</strong> — sharp reflexes and discipline.</li>
        <li><strong>10 / 10</strong> — flawless.</li>
      </ul>

      <h2>Tips to score higher</h2>
      <ul>
        <li><strong>Don't pre-commit</strong> your tap — wait until you actually see the colour.</li>
        <li><strong>Stay relaxed</strong>; tension makes you fire early on the red trials.</li>
        <li><strong>Recover fast</strong> after a mistake so it doesn't throw off the next trial.</li>
      </ul>
      <p>Like reaction challenges? Try the <a href="/reaction-time-test/">reaction time test</a> or <a href="/color-match/">color match</a>.</p>""",
    "faq": [
        ("What does the Go / No-Go test measure?",
         "Response inhibition — your ability to act quickly on a Go signal while stopping yourself from acting on a No-Go signal. It's a classic measure of impulse control."),
        ("How is it scored?",
         "One point for each correct response across 10 trials: tapping on green, and holding still on red. Tapping on red or missing a green loses the point."),
        ("What is a good Go / No-Go score?",
         "6 to 7 out of 10 is good control, 8 to 9 is sharp, and 10 is flawless."),
        ("Does it work on a phone?",
         "Yes. Tap the screen on green and keep your hands off on red."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match (Stroop)", "desc": "Word vs ink colour."},
        {"slug": "audio-reaction-test", "kbd": "Reaction", "name": "Audio Reaction Test", "desc": "React to the beep."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets fast."},
        {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Stop the timer on target."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
