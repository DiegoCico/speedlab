CABINET = """    <section class="cabinet" id="visualmem" aria-label="Visual memory test">
      <div class="marquee">Visual Memory</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="level">1</span></div>
              <div class="readout-label">Level</div>
            </div>
            <div class="readout small">
              <div class="mem-lives" id="lives" aria-label="Lives"></div>
              <div class="readout-label">Lives</div>
            </div>
          </div>
          <div class="mem-stage">
            <p class="mem-feedback" id="status"></p>
            <div class="mem-grid" id="grid"></div>
            <div class="mem-center" id="startWrap">
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              <p class="mem-hint">Some tiles flash. Click them all from memory. The grid grows each level; three lives.</p>
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
    "slug": "visual-memory",
    "name": "Visual Memory",
    "crumb": "Visual Memory",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/visual-memory.js"],
    "title": "Visual Memory Test — Remember the Tiles | SpeedLab",
    "desc": "Test your visual memory. Tiles flash on a grid, then you click them from memory. The grid grows each level. How many levels can you clear?",
    "ld_desc": "Tiles flash on a grid and you reproduce them from memory as the grid grows.",
    "og_title": "Visual Memory Test — Remember the Tiles",
    "og_desc": "Tiles flash, then you click them from memory. The grid grows each level.",
    "og_image": "visual-memory.png",
    "h1": "Visual Memory Test",
    "lead": "A set of tiles flashes on the grid, then vanishes. Click every tile you saw from memory. The grid grows each level — how far can you go on three lives?",
    "content": """      <h2>How the visual memory test works</h2>
      <p>Each level, a group of tiles lights up for a moment and then goes dark. Your job is to click exactly those tiles from memory. Clear them all and you move up a level, where the grid is bigger and more tiles flash. Click a wrong tile and you lose one of your three lives; lose all three and the game ends. Your score is the highest level you reach, so it rewards a sharp eye and a steady memory.</p>

      <h2>What is a good visual memory score?</h2>
      <ul>
        <li><strong>Under 4</strong> &mdash; a casual attempt.</li>
        <li><strong>6 to 8</strong> &mdash; right around average.</li>
        <li><strong>10 to 12</strong> &mdash; a strong, focused run.</li>
        <li><strong>15+</strong> &mdash; excellent visual memory.</li>
      </ul>

      <h2>How to remember more tiles</h2>
      <ul>
        <li><strong>See the shape,</strong> not the tiles &mdash; group them into lines, corners, or clusters.</li>
        <li><strong>Look at the whole grid</strong> while it flashes rather than darting between tiles.</li>
        <li><strong>Click the ones you are sure of first</strong> to protect your lives.</li>
      </ul>
      <p>For more brain tests, try <a href="/number-memory/">number memory</a>, <a href="/sequence-memory/">sequence memory</a>, and the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("What is a good visual memory score?",
         "Around level 6 to 8 is average. Level 10 to 12 is strong, and 15 or higher is excellent."),
        ("How many lives do I get?",
         "Three. Each wrong tile costs one life, and the game ends when all three are gone. Your score is the level you reached."),
        ("Does the grid get bigger?",
         "Yes. As you level up the grid grows and more tiles flash, so each level is harder than the last."),
        ("Does it work on a phone?",
         "Yes. Tap the tiles you remember. It works the same on touch and mouse."),
    ],
    "related": [
        {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the growing pattern."},
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
