CABINET = """    <section class="cabinet" id="wordguess" aria-label="Woordle word game">
      <div class="marquee">Woordle</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="guesses">0</span></div>
              <div class="readout-label">Guesses</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">0</span></div>
              <div class="readout-label">Seconds</div>
            </div>
          </div>
          <div class="wg-stage">
            <div class="wg-board" id="board" aria-label="Guess grid"></div>
            <p class="wg-msg" id="msg"></p>
            <div class="wg-kbd" id="kbd" aria-label="On-screen keyboard"></div>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button">New word</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "woordle",
    "name": "Woordle",
    "crumb": "Woordle",
    "skip_target": "board",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/word-guess.js"],
    "title": "Woordle — Daily Word Guessing Game | SpeedLab",
    "desc": "Play Woordle, a Wordle-style word game. Guess the hidden 5-letter word in 6 tries with a live timer and guess counter, green and amber hints, and a rank.",
    "ld_desc": "Guess the hidden 5-letter word in six tries in Woordle, a Wordle-style word game.",
    "og_title": "Woordle — Word Guessing Game",
    "og_desc": "Guess the hidden 5-letter word in 6 tries. Live timer and guess counter.",
    "og_image": "woordle.png",
    "h1": "Woordle",
    "lead": "Guess the hidden five-letter word in six tries. Green means the letter is in the right spot, amber means it's in the word somewhere. We time you and count your guesses.",
    "content": """      <h2>How Woordle works</h2>
      <p>Woordle is a Wordle-style word game: there's a hidden <strong>five-letter word</strong>, and you have <strong>six guesses</strong> to find it. Type any five-letter word and press Enter. Each tile then changes colour:</p>
      <ul>
        <li><strong>Green</strong> — that letter is correct and in the right spot.</li>
        <li><strong>Amber</strong> — that letter is in the word, but somewhere else.</li>
        <li><strong>Grey</strong> — that letter isn't in the word at all.</li>
      </ul>
      <p>The on-screen keyboard fills in with those colours too, so you can keep track of what you've ruled out. A timer counts up from your first letter and your guess count is shown live, so you're racing on two fronts: solve it in as few guesses as possible, as fast as possible. Your score is the number of guesses (fewer is better), with your solve time shown next to it.</p>

      <h2>What is a good Woordle score?</h2>
      <ul>
        <li><strong>1–2 guesses</strong> — outstanding (and a bit lucky on 1).</li>
        <li><strong>3 guesses</strong> — genuinely sharp.</li>
        <li><strong>4 guesses</strong> — right around average; solid solving.</li>
        <li><strong>5–6 guesses</strong> — you got there under pressure.</li>
      </ul>

      <h2>Tips to solve faster</h2>
      <ul>
        <li><strong>Open with a vowel-heavy word</strong> so you learn a lot on guess one.</li>
        <li><strong>Use your greys.</strong> The keyboard shows every letter you've eliminated — don't reuse them.</li>
        <li><strong>Place the ambers.</strong> A letter that's in the word but wrong-spot narrows things fast.</li>
      </ul>
      <p>Want a memory challenge instead? Try <a href="/number-memory/">number memory</a> or the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("How many guesses do I get in Woordle?",
         "Six. You have to find the hidden five-letter word within six tries, and your score is how many guesses it takes — fewer is better."),
        ("What do the colours mean?",
         "Green means the letter is correct and in the right spot, amber means it's in the word but in a different spot, and grey means it isn't in the word."),
        ("Is Woordle the same as Wordle?",
         "No. Woordle is an independent, Wordle-style word game and is not affiliated with Wordle or The New York Times. The rules are similar because it's a classic format."),
        ("Does it work on a phone?",
         "Yes. Use the on-screen keyboard to type your guesses; it colours in your used letters just like the grid."),
    ],
    "related": [
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the growing pattern."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match", "desc": "Does the word match the ink?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
