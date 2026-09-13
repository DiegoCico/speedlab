CABINET = """    <section class="cabinet" id="emojihunt" aria-label="Emoji hunt">
      <div class="marquee">Emoji Hunt</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="level">1</span></div>
              <div class="readout-label">Level</div>
            </div>
          </div>
          <div class="mem-stage">
            <p class="mem-feedback" id="status"></p>
            <div class="emoji-grid" id="grid"></div>
            <div class="mem-center" id="startWrap">
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              <p class="mem-hint">One emoji is different from the rest. Tap it. The grid grows and the emojis get more alike each round.</p>
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
    "slug": "emoji-hunt",
    "name": "Emoji Hunt",
    "crumb": "Emoji Hunt",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/emoji-hunt.js"],
    "title": "Emoji Hunt — Find the Different Emoji | SpeedLab",
    "desc": "Find the one emoji that is different in the grid. Each round the grid grows and the emojis get more alike. How many rounds can you clear?",
    "ld_desc": "Find the one different emoji in a grid that grows harder each round.",
    "og_title": "Emoji Hunt — Find the Different Emoji",
    "og_desc": "Spot the odd emoji out. The grid grows harder each round.",
    "og_image": "emoji-hunt.png",
    "h1": "Emoji Hunt",
    "lead": "One emoji in the grid is different from all the others. Tap it. Each round the grid gets bigger and the emojis look more alike — how far can you get?",
    "content": """      <h2>How emoji hunt works</h2>
      <p>The grid fills with the same emoji &mdash; except one. Find the odd one out and tap it to move to the next round. Each round the grid grows and the two emojis get harder to tell apart, so what starts easy quickly becomes a real test of visual attention. One wrong tap ends the game, and your score is the number of rounds you clear. It is a pure spot-the-difference challenge that keeps ramping up.</p>

      <h2>What is a good emoji hunt score?</h2>
      <ul>
        <li><strong>Under 3 rounds</strong> &mdash; just warming up.</li>
        <li><strong>6 to 9 rounds</strong> &mdash; right around average.</li>
        <li><strong>13 to 18 rounds</strong> &mdash; sharp eyes.</li>
        <li><strong>24+ rounds</strong> &mdash; excellent visual attention.</li>
      </ul>

      <h2>Tips to spot the odd one</h2>
      <ul>
        <li><strong>Scan in rows,</strong> left to right, instead of staring at the whole grid at once.</li>
        <li><strong>Look for the shape or colour that breaks the pattern,</strong> not the whole emoji.</li>
        <li><strong>Slow down on the hard rounds</strong> &mdash; one wrong tap ends the run, so accuracy beats speed late on.</li>
      </ul>
      <p>Like spotting things fast? Try the <a href="/color-match/">color match</a> focus test or the <a href="/aim-trainer/">aim trainer</a>.</p>""",
    "faq": [
        ("What is a good emoji hunt score?",
         "Around 6 to 9 rounds is average. 13 to 18 is sharp, and 24 or more is excellent visual attention."),
        ("What happens if I tap the wrong emoji?",
         "One wrong tap ends the game. Your score is the number of rounds you cleared before the mistake."),
        ("Does it get harder?",
         "Yes. Each round the grid grows and the two emojis become more similar, so later rounds are much trickier."),
        ("Does it work on a phone?",
         "Yes. Tap the odd emoji with your finger. It works the same on touch and mouse."),
    ],
    "related": [
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match", "desc": "Does the word match the ink?"},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Reproduce the flashed tiles."},
        {"slug": "scroll-speed-test", "kbd": "Mobile", "name": "Scroll Speed Test", "desc": "How far can you scroll?"},
        {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
