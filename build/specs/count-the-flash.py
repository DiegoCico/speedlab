CABINET = """    <section class="cabinet" id="subitize" aria-label="Count the flash">
      <div class="marquee">Count the Flash</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="level">1</span></div>
              <div class="readout-label">Level</div>
            </div>
          </div>
          <div class="subit-area">
            <div class="subit-field" id="field" aria-hidden="true"></div>
            <div class="subit-prompt" id="prompt">Count the dots that flash.</div>
            <div class="subit-input-row" id="inputRow" hidden>
              <input class="math-input" id="answer" type="text" inputmode="numeric" pattern="[0-9]*"
                autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="How many dots" disabled>
              <button class="arcade-btn p1" id="checkBtn" type="button">Check</button>
            </div>
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
    "slug": "count-the-flash",
    "name": "Count the Flash",
    "crumb": "Count the Flash",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/subitize.js"],
    "title": "Count the Flash — Subitizing Speed Test | SpeedLab",
    "desc": "Dots flash for a split second — count them before they vanish. Each level adds a dot and shortens the flash. Test how fast your brain counts at a glance.",
    "ld_desc": "Dots flash briefly; count how many there were. Each level adds a dot and shortens the flash.",
    "og_title": "Count the Flash — Subitizing Speed Test",
    "og_desc": "How many dots can you count in a flash?",
    "og_image": "count-the-flash.png",
    "h1": "Count the Flash",
    "lead": "Dots flash on screen for a split second — count them before they disappear. Every level adds another dot and makes the flash faster. How far can you get?",
    "content": """      <h2>How the count the flash test works</h2>
      <p>Press Start and a cluster of dots flashes on the screen for a fraction of a second, then vanishes. Type how many you saw. Get it right and you move up a level — one more dot, a shorter flash. Get it wrong and the run ends. Your score is the <strong>highest level you reached</strong>. It measures <em>subitizing</em>: your brain's ability to know a quantity at a glance, without counting one by one.</p>

      <h2>What is a good level?</h2>
      <ul>
        <li><strong>Level 3 or below</strong> — just warming up.</li>
        <li><strong>Level 5 to 7</strong> — a solid, quick eye.</li>
        <li><strong>Level 9 to 12</strong> — fast; you estimate large groups well.</li>
        <li><strong>Level 15+</strong> — exceptional.</li>
      </ul>

      <h2>Tips to count faster</h2>
      <ul>
        <li><strong>See groups, not dots</strong> — break the cluster into small chunks of two and three.</li>
        <li><strong>Soften your focus</strong> so you take in the whole field at once.</li>
        <li><strong>Trust your first impression</strong> — there's no time to recount.</li>
      </ul>
      <p>Enjoy quick-glance challenges? Try <a href="/visual-memory/">visual memory</a> or the <a href="/reaction-time-test/">reaction time test</a>.</p>""",
    "faq": [
        ("What is subitizing?",
         "Subitizing is instantly recognising how many objects are in a small group without counting them one by one. This test pushes that skill by flashing more dots for less time each level."),
        ("How is Count the Flash scored?",
         "By the highest level you reach. Each level adds a dot and shortens the flash, and one wrong answer ends the run."),
        ("What is a good score?",
         "Reaching level 5 to 7 is solid, level 9 to 12 is fast, and level 15 or higher is exceptional."),
        ("Does it work on a phone?",
         "Yes. Watch the flash, then tap the answer box to type how many dots you saw."),
    ],
    "related": [
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Remember the flashed tiles."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
