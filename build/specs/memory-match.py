CABINET = """    <section class="cabinet" id="memorymatch" aria-label="Memory match">
      <div class="marquee">Memory Match</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="matches">0/8</span></div>
              <div class="readout-label">Pairs found</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">0.0</span></div>
              <div class="readout-label">Seconds</div>
            </div>
          </div>
          <div class="mm-board" id="board" role="grid" aria-label="Card grid"></div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button">New board</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "memory-match",
    "name": "Memory Match",
    "crumb": "Memory Match",
    "skip_target": "board",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/memory-match.js"],
    "title": "Memory Match — Concentration Card Game | SpeedLab",
    "desc": "Flip cards two at a time and find all eight pairs as fast as you can. The classic concentration memory game, timed and ranked. No sign-up.",
    "ld_desc": "Flip cards two at a time to find all eight matching pairs as fast as possible.",
    "og_title": "Memory Match — Concentration Card Game",
    "og_desc": "Find all eight pairs as fast as you can.",
    "og_image": "memory-match.png",
    "h1": "Memory Match",
    "lead": "Flip the cards two at a time and find all eight pairs. The clock starts on your first flip and stops when the board is clear — fastest time wins.",
    "content": """      <h2>How the memory match game works</h2>
      <p>Sixteen cards sit face down in a grid, hiding eight matching pairs. Flip one, then flip another. If they match, they stay up; if they don't, they flip back and you try again. The <strong>timer starts on your first flip</strong> and stops the moment the last pair is found, so your score is simply how fast you clear the board. It's the classic game of concentration — a pure working-memory workout.</p>

      <h2>What is a good time?</h2>
      <ul>
        <li><strong>Over 75 seconds</strong> — relying mostly on luck.</li>
        <li><strong>40 to 55 seconds</strong> — a solid, steady clear.</li>
        <li><strong>20 to 30 seconds</strong> — fast; you're remembering positions well.</li>
        <li><strong>Under 20 seconds</strong> — excellent recall.</li>
      </ul>

      <h2>Tips to clear it faster</h2>
      <ul>
        <li><strong>Build a mental map</strong> — remember where a symbol was even when it flips back.</li>
        <li><strong>Work in rows</strong> so positions are easier to picture.</li>
        <li><strong>Chase known pairs first</strong> once you've seen both of a kind.</li>
      </ul>
      <p>Want more memory tests? Try <a href="/visual-memory/">visual memory</a> or <a href="/sequence-memory/">sequence memory</a>.</p>""",
    "faq": [
        ("How is Memory Match scored?",
         "By the time it takes to clear the whole board. The clock starts on your first flip and stops when the last pair is matched, so a lower time is better."),
        ("How many pairs are there?",
         "Eight pairs — sixteen cards in a four-by-four grid — reshuffled every time you start a new board."),
        ("What is a good memory match time?",
         "Around 40 to 55 seconds is solid, 20 to 30 seconds is fast, and under 20 seconds is excellent."),
        ("Does it work on a phone?",
         "Yes. Tap the cards to flip them; the grid fits any screen size."),
    ],
    "related": [
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Remember the flashed tiles."},
        {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the growing pattern."},
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
