CABINET = """    <section class="cabinet" id="aim" aria-label="Aim trainer">
      <div class="marquee">Aim Trainer</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="remaining">30</span></div>
              <div class="readout-label">Targets left</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="avg">0</span></div>
              <div class="readout-label">Avg ms</div>
            </div>
          </div>
          <div class="aim-arena" id="arena">
            <button class="aim-target aim-start" id="startTarget" type="button">Start</button>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Restart</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "aim-trainer",
    "name": "Aim Trainer",
    "crumb": "Aim Trainer",
    "skip_target": "startTarget",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/aim-trainer.js"],
    "title": "Aim Trainer — Click Target Speed Test | SpeedLab",
    "desc": "Test your aim and mouse accuracy. Click 30 targets as fast as you can and get your average time per target in milliseconds, with your rank and percentile.",
    "ld_desc": "Click 30 targets as fast as you can and measure your average time per target.",
    "og_title": "Aim Trainer — Click Target Speed Test",
    "og_desc": "Click 30 targets as fast as you can. Measure your average ms per target.",
    "og_image": "aim-trainer.png",
    "h1": "Aim Trainer",
    "lead": "Thirty targets, one at a time, as fast as you can. Click each one the instant it appears — we measure your average time per target in milliseconds.",
    "content": """      <h2>How the aim trainer works</h2>
      <p>Press start and a target appears somewhere in the arena. Click it and the next one instantly pops up in a new random spot. Keep going until you have hit all 30. Your score is the <strong>average time per target</strong> in milliseconds &mdash; lower is better &mdash; so it rewards both quick reactions and accurate mouse movement. The running average updates as you play so you can see how you are doing.</p>

      <h2>What is a good time per target?</h2>
      <p>A good aim time depends on your mouse, your screen, and how much you play. As a rough guide:</p>
      <ul>
        <li><strong>Over 650 ms</strong> &mdash; casual; take your time to line up each click.</li>
        <li><strong>450 to 550 ms</strong> &mdash; right around average.</li>
        <li><strong>300 to 400 ms</strong> &mdash; fast and accurate.</li>
        <li><strong>Under 300 ms</strong> &mdash; excellent; genuinely sharp aim.</li>
      </ul>

      <h2>How to improve your aim</h2>
      <ul>
        <li><strong>Lower your mouse sensitivity</strong> a little. Most people aim more accurately with a bit more hand movement.</li>
        <li><strong>Move and click in one motion</strong> instead of stopping over the target first.</li>
        <li><strong>Use your arm, not just your wrist,</strong> for the bigger jumps across the screen.</li>
        <li><strong>Warm up.</strong> A few rounds makes a real difference to your average.</li>
      </ul>
      <p>Want a pure reflex test instead? Try the <a href="/reaction-time-test/">reaction time test</a>. To measure raw clicking, use the <a href="/cps-test/">CPS test</a>.</p>""",
    "faq": [
        ("What is a good aim trainer score?",
         "Around 450 to 550 ms per target is average. Under 400 ms is fast, and under 300 ms is excellent."),
        ("How many targets are there?",
         "Thirty targets, one at a time. Your score is the total time divided by 30, so it is your average per target."),
        ("Does mouse sensitivity affect my score?",
         "Yes. Most people are more accurate at a slightly lower sensitivity, which usually lowers their average time."),
        ("Does the aim trainer work on a phone?",
         "It works with touch, but a mouse gives the most accurate and fastest results on a larger screen."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go — pure reflexes."},
        {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles for 30 seconds."},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
