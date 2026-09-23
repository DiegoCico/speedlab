CABINET = """    <section class="cabinet" id="game2048" aria-label="2048 number puzzle">
      <div class="marquee">2048</div>

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
          <div class="g2048-area">
            <div class="g2048-board" id="g2048board">
              <div class="g2048-grid" aria-hidden="true">
                <div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div>
                <div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div>
                <div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div>
                <div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div><div class="g2048-cell"></div>
              </div>
              <div class="g2048-tiles" id="g2048tiles" aria-label="Game board"></div>
            </div>
            <div class="g2048-hint">Use arrow keys or swipe. Merge equal tiles to reach 2048.</div>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button">New game</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "2048",
    "name": "2048",
    "crumb": "2048",
    "skip_target": "g2048board",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/game-2048.js"],
    "title": "2048 — Number Merge Puzzle Game | SpeedLab",
    "desc": "Play 2048 free: slide the tiles with arrow keys or swipes, merge matching numbers, and reach the 2048 tile. No sign-up, works on any device, best score saved.",
    "ld_desc": "Slide and merge numbered tiles to reach 2048; your score is the running total.",
    "og_title": "2048 — Number Merge Puzzle",
    "og_desc": "Slide, merge, and reach the 2048 tile.",
    "og_image": "default.png",
    "h1": "2048",
    "lead": "Slide the tiles with your arrow keys or a swipe. When two tiles with the same number touch, they merge into one. Keep going and try to build the 2048 tile.",
    "content": """      <h2>How to play 2048</h2>
      <p>Every move slides <strong>all</strong> the tiles in one direction — up, down, left or right. When two tiles showing the same number collide, they merge into a single tile worth double, and those points get added to your score. After each move a new 2 or 4 appears on an empty square. The board fills up fast, so plan ahead: the game ends when there's no move left that changes anything.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Reaching the 512 tile</strong> — a solid game.</li>
        <li><strong>The 1024 tile</strong> — you're playing well.</li>
        <li><strong>The 2048 tile</strong> — the classic win.</li>
        <li><strong>Beyond 2048</strong> — expert territory; 4096 and up are brutal.</li>
      </ul>

      <h2>Strategy tips</h2>
      <ul>
        <li><strong>Pick a corner</strong> and keep your biggest tile there — most players anchor bottom-right.</li>
        <li><strong>Only use three directions.</strong> Avoid the move that would pull your big tile out of its corner.</li>
        <li><strong>Build a chain</strong> of descending values along one edge so merges cascade.</li>
        <li><strong>Don't chase every merge</strong> — keep the board tidy rather than greedy.</li>
      </ul>
      <p>Want another number challenge? Try <a href="/number-memory/">number memory</a> or <a href="/mental-math/">mental math sprint</a>.</p>""",
    "faq": [
        ("How do you play 2048?", "Slide all the tiles with the arrow keys or a swipe. Tiles with the same number merge into one worth double. A new tile appears after each move, and the game ends when no move changes the board."),
        ("How is the score calculated?", "Every time two tiles merge, the value of the new tile is added to your score. Reaching bigger tiles means bigger merges and a higher total."),
        ("Does it work on a phone?", "Yes. Swipe up, down, left or right on the board to move the tiles. On a computer, use the arrow keys or WASD."),
        ("Is my best score saved?", "Yes, your best score is stored in your browser on this device. No account needed, and nothing is uploaded anywhere."),
    ],
    "related": [
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "memory-match", "kbd": "Memory", "name": "Memory Match", "desc": "Find all the pairs."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "word-unscramble", "kbd": "Brain", "name": "Word Unscramble", "desc": "Untangle jumbled words."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
