CABINET = """    <section class="cabinet" id="clusters" aria-label="Clusters word groups">
      <div class="marquee">Clusters</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="solvedCount">0/4</span></div>
              <div class="readout-label">Groups</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="lives">4</span></div>
              <div class="readout-label">Mistakes left</div>
            </div>
          </div>
          <div class="cl-area">
            <div class="cl-solved" id="clSolved"></div>
            <div class="cl-grid" id="clGrid" aria-label="Word grid"></div>
            <div class="cl-msg" id="clMsg">Find the four hidden groups of four.</div>
            <div class="cl-buttons">
              <button class="arcade-btn" id="shuffleBtn" type="button">Shuffle</button>
              <button class="arcade-btn p1" id="submitBtn" type="button" disabled>Submit</button>
            </div>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn" id="restart" type="button">New puzzle</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "clusters",
    "name": "Clusters",
    "crumb": "Clusters",
    "skip_target": "clGrid",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/clusters.js"],
    "title": "Clusters — Word Grouping Puzzle Game | SpeedLab",
    "desc": "Sort 16 words into 4 hidden groups of four. A free word-grouping puzzle in the style of Connections — four mistakes allowed. No sign-up, new puzzle every time.",
    "ld_desc": "Sort 16 words into 4 hidden groups of four, with four mistakes allowed.",
    "og_title": "Clusters — Word Grouping Puzzle",
    "og_desc": "Sort 16 words into 4 hidden groups. Can you find them all?",
    "og_image": "default.png",
    "h1": "Clusters",
    "lead": "Sixteen words, four hidden groups of four. Tap four words you think belong together and submit. Find all four groups before you run out of your four mistakes.",
    "content": """      <h2>How to play Clusters</h2>
      <p>The board shows <strong>16 words</strong>. Hidden among them are <strong>four groups of four</strong> that share something — a theme, a category, a common word. Select four words you think go together and hit Submit. Guess a full group correctly and it locks in with its colour and category name. Guess wrong and you lose one of your <strong>four mistakes</strong>. Find all four groups to win. The catch: some words look like they fit more than one group, and only one arrangement is correct.</p>

      <h2>How scoring works</h2>
      <ul>
        <li><strong>100 points</strong> — a flawless solve with no mistakes.</li>
        <li><strong>80 / 60 / 40</strong> — solved with one, two or three mistakes.</li>
        <li><strong>Ran out of tries?</strong> You still score for the groups you found.</li>
      </ul>

      <h2>Tips for solving</h2>
      <ul>
        <li><strong>Start with what's obvious</strong>, but stay suspicious — the easy-looking group often hides a trap word.</li>
        <li><strong>Look for the trap.</strong> If five words seem to fit one theme, one of them belongs elsewhere.</li>
        <li><strong>Use the Shuffle button</strong> to rearrange the board and see the words fresh.</li>
        <li><strong>Save the group you're unsure of for last</strong> — the final four are decided for you.</li>
      </ul>
      <p>Like word puzzles? Try <a href="/woordle/">Woordle</a> or <a href="/word-unscramble/">Word Unscramble</a>.</p>""",
    "faq": [
        ("How do you play Clusters?",
         "Sort 16 words into 4 hidden groups of four. Select four words and submit; a correct group locks in, a wrong guess costs one of your four mistakes. Find all four groups to win."),
        ("How is Clusters scored?",
         "A perfect solve with no mistakes is 100 points, dropping by 20 for each mistake. If you run out of tries, you still score 20 points for each group you found."),
        ("Is this the same as Connections?",
         "It's the same style of word-grouping puzzle, but Clusters is its own game with its own puzzles, and it serves a fresh random board every time rather than one shared daily puzzle."),
        ("Does it work on a phone?",
         "Yes. Tap words to select them, then tap Submit. The board and buttons are sized for touchscreens."),
    ],
    "related": [
        {"slug": "woordle", "kbd": "Brain", "name": "Woordle", "desc": "Guess the word in 6 tries."},
        {"slug": "word-unscramble", "kbd": "Brain", "name": "Word Unscramble", "desc": "Untangle jumbled words."},
        {"slug": "2048", "kbd": "Brain", "name": "2048", "desc": "Merge tiles to reach 2048."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
