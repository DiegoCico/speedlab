CABINET = """    <section class="cabinet" id="unscramble" aria-label="Word unscramble">
      <div class="marquee">Word Unscramble</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="solved">0</span></div>
              <div class="readout-label">Solved</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">60</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="math-area">
            <div class="math-problem scram-word" id="scrambled">SPEED</div>
            <input class="math-input" id="answer" type="text" inputmode="text"
              autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Your word" disabled>
            <div class="rot-buttons">
              <button class="arcade-btn p2" id="skipBtn" type="button" disabled>Skip</button>
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
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
    "slug": "word-unscramble",
    "name": "Word Unscramble",
    "crumb": "Word Unscramble",
    "skip_target": "answer",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/word-unscramble.js"],
    "title": "Word Unscramble — Anagram Speed Game | SpeedLab",
    "desc": "Jumbled letters, one real word. Unscramble as many as you can in 60 seconds. A fast anagram game that checks itself as you type — no sign-up.",
    "ld_desc": "Unscramble jumbled letters into real words, as many as you can in 60 seconds.",
    "og_title": "Word Unscramble — Anagram Speed Game",
    "og_desc": "How many jumbled words can you solve in 60s?",
    "og_image": "word-unscramble.png",
    "h1": "Word Unscramble",
    "lead": "Jumbled letters, one real word hiding inside. Type it out — it checks itself the instant you get it right, then serves the next. How many can you solve in 60 seconds?",
    "content": """      <h2>How the word unscramble game works</h2>
      <p>Press Start and a scrambled word appears. Rearrange the letters in your head and type the real word — it's checked <strong>automatically</strong> the moment you spell it correctly, so there's nothing to submit. Stuck on one? Hit Skip for a fresh word, though it costs you time. You have <strong>60 seconds</strong>, and your score is how many words you unscramble. The word list is large and varied, so no two runs feel the same.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 3</strong> — just warming up.</li>
        <li><strong>6 to 9</strong> — a good, steady pace.</li>
        <li><strong>13 to 17</strong> — fast; you spot anagrams quickly.</li>
        <li><strong>22+</strong> — excellent word power.</li>
      </ul>

      <h2>Tips to solve faster</h2>
      <ul>
        <li><strong>Look for common endings</strong> like -ing, -er, or -le and build backwards.</li>
        <li><strong>Spot pairs</strong> — th, ch, st — that often sit together.</li>
        <li><strong>Say the letters aloud</strong> in your head; the word often jumps out.</li>
      </ul>
      <p>Love word games? Try <a href="/woordle/">Woordle</a> or the <a href="/typing-speed-test/">typing speed test</a>.</p>""",
    "faq": [
        ("How is Word Unscramble scored?",
         "By how many words you unscramble in 60 seconds. Each word checks itself as you type it correctly, so you never lose time submitting."),
        ("Where do the words come from?",
         "From a large, varied built-in list of common English words, so runs stay fresh and you can't just memorise a fixed set."),
        ("What is a good score?",
         "Solving 6 to 9 words is a good pace, 13 to 17 is fast, and 22 or more is excellent."),
        ("Does it work on a phone?",
         "Yes. Tap the answer box to bring up the keyboard and type each word; use Skip to pass a tricky one."),
    ],
    "related": [
        {"slug": "woordle", "kbd": "Brain", "name": "Woordle", "desc": "Guess the word in 6 tries."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z fast."},
        {"slug": "same-or-mirror", "kbd": "Brain", "name": "Same or Mirror", "desc": "Rotated shape or mirror?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
