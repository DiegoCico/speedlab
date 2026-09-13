CABINET = """    <section class="cabinet" id="chimp" aria-label="Chimp test">
      <div class="marquee">Chimp Test</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="num">4</span></div>
              <div class="readout-label">Numbers</div>
            </div>
            <div class="readout small">
              <div class="mem-lives" id="strikes" aria-label="Strikes left"></div>
              <div class="readout-label">Strikes left</div>
            </div>
          </div>
          <div class="mem-stage">
            <p class="mem-feedback" id="status"></p>
            <div class="mem-grid" id="grid"></div>
            <div class="mem-center" id="startWrap">
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              <p class="mem-hint">Numbers appear, then hide. Click them in order, 1 upward. One more number each round; three strikes and you're out.</p>
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
    "slug": "chimp-test",
    "name": "Chimp Test",
    "crumb": "Chimp Test",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/chimp-test.js"],
    "title": "Chimp Test — Working Memory Challenge | SpeedLab",
    "desc": "Take the chimp test: numbers appear then hide, and you click them in order from memory. One more number each round. How high can your working memory go?",
    "ld_desc": "Numbers appear then hide; click them in order from memory as the count grows.",
    "og_title": "Chimp Test — Working Memory Challenge",
    "og_desc": "Numbers appear then hide. Click them in order. One more each round.",
    "og_image": "chimp-test.png",
    "h1": "Chimp Test",
    "lead": "Numbers appear on the grid, then hide behind blank tiles. Click them in order from memory, 1 upward. Each round adds one more number — how high can you go?",
    "content": """      <h2>How the chimp test works</h2>
      <p>A set of numbers appears scattered across the grid. The moment you click <strong>1</strong>, the rest hide behind blank tiles, and you have to click the remaining numbers in order from memory: 2, 3, 4, and so on. Clear them all and the next round adds one more number. Click out of order and you take a strike &mdash; three strikes and the game ends. Your score is the highest count of numbers you clear.</p>
      <p>The test is named after research showing that chimpanzees can beat humans at exactly this kind of quick spatial recall, so a high score puts you in genuinely impressive company.</p>

      <h2>What is a good chimp test score?</h2>
      <ul>
        <li><strong>Under 6</strong> &mdash; a casual attempt.</li>
        <li><strong>8 to 10</strong> &mdash; right around average.</li>
        <li><strong>12 to 14</strong> &mdash; a strong working memory.</li>
        <li><strong>16+</strong> &mdash; excellent; chimp-level recall.</li>
      </ul>

      <h2>How to score higher</h2>
      <ul>
        <li><strong>Photograph the layout</strong> with your eyes before clicking 1 &mdash; take that free moment.</li>
        <li><strong>Group nearby numbers</strong> so you remember clusters, not single positions.</li>
        <li><strong>Don't rush the click on 1.</strong> Once you start, the numbers are hidden, so lock in the picture first.</li>
      </ul>
      <p>Round out your brain training with <a href="/number-memory/">number memory</a>, <a href="/sequence-memory/">sequence memory</a>, and <a href="/visual-memory/">visual memory</a>.</p>""",
    "faq": [
        ("What is the chimp test?",
         "A working-memory test where numbers appear then hide, and you click them in order from memory. It is named after chimpanzees, who excel at this kind of recall."),
        ("What is a good chimp test score?",
         "Around 8 to 10 numbers is average. 12 to 14 is strong, and 16 or more is excellent."),
        ("How many strikes do I get?",
         "Three. Clicking out of order costs a strike, and the game ends at three. Your score is the highest count of numbers you cleared."),
        ("When do the numbers hide?",
         "As soon as you click 1, the rest are covered. So study their positions before you make your first click."),
    ],
    "related": [
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the growing pattern."},
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Reproduce the flashed tiles."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
