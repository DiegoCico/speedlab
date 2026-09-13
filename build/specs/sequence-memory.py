CELLS = "\n".join(['            <button class="mem-cell" type="button" aria-label="Tile"></button>'] * 9)

CABINET = ("""    <section class="cabinet" id="sequencemem" aria-label="Sequence memory test">
      <div class="marquee">Sequence Memory</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="level">0</span></div>
              <div class="readout-label">Level</div>
            </div>
          </div>
          <div class="mem-stage">
            <p class="mem-feedback" id="status"></p>
            <div class="mem-grid" id="grid" style="grid-template-columns:repeat(3,1fr);max-width:340px">
%CELLS%
            </div>
            <div class="mem-center" id="startWrap">
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              <p class="mem-hint">Watch the pattern light up, then repeat it. It grows by one each round.</p>
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
    </section>""").replace("%CELLS%", CELLS)

SPEC = {
    "slug": "sequence-memory",
    "name": "Sequence Memory",
    "crumb": "Sequence Memory",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/sequence-memory.js"],
    "title": "Sequence Memory Test — Repeat the Pattern | SpeedLab",
    "desc": "Test your sequence memory. Watch the tiles light up, then repeat the pattern back. It grows by one each round — how long a sequence can you remember?",
    "ld_desc": "Watch a growing pattern of tiles light up and repeat it back from memory.",
    "og_title": "Sequence Memory Test — Repeat the Pattern",
    "og_desc": "Watch the tiles light up, then repeat the growing pattern.",
    "og_image": "sequence-memory.png",
    "h1": "Sequence Memory Test",
    "lead": "Watch the tiles light up in a pattern, then click them back in the same order. Every round adds one more step. How long a sequence can you hold?",
    "content": """      <h2>How the sequence memory test works</h2>
      <p>The grid plays a pattern by lighting up tiles one at a time. When it finishes, repeat the pattern by clicking the tiles in the same order. Get it right and the pattern grows by one extra step; get one wrong and the game ends. Your score is the length of the longest sequence you complete. It is the same idea as the classic Simon game, and it is a great test of short-term spatial memory.</p>

      <h2>What is a good sequence memory score?</h2>
      <ul>
        <li><strong>Under 5</strong> &mdash; a casual attempt.</li>
        <li><strong>6 to 8</strong> &mdash; right around average.</li>
        <li><strong>10 to 12</strong> &mdash; a strong, focused run.</li>
        <li><strong>14+</strong> &mdash; excellent sequence memory.</li>
      </ul>

      <h2>How to remember longer sequences</h2>
      <ul>
        <li><strong>Watch the whole grid,</strong> not one tile at a time, so you catch the shape of the path.</li>
        <li><strong>Turn the pattern into a route</strong> &mdash; up, corner, middle &mdash; instead of separate tiles.</li>
        <li><strong>Stay calm on the long ones.</strong> Rushing the playback is where most mistakes happen.</li>
      </ul>
      <p>For more memory challenges, try <a href="/number-memory/">number memory</a>, <a href="/visual-memory/">visual memory</a>, and the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("What is a good sequence memory score?",
         "Around 6 to 8 is average. 10 to 12 is a strong run, and 14 or more is excellent."),
        ("Is this the same as Simon?",
         "Yes, it uses the same idea as the classic Simon game: watch a growing pattern light up, then repeat it back in order."),
        ("What happens when I make a mistake?",
         "One wrong tile ends the game. Your score is the length of the longest sequence you completed correctly."),
        ("Does it work on a phone?",
         "Yes. Tap the tiles to repeat the pattern. It works the same on touch and mouse."),
    ],
    "related": [
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Reproduce the flashed tiles."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
