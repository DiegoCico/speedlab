CABINET = """    <section class="cabinet" id="wordspam" aria-label="Word Spammer">
      <div class="marquee">Word Spammer</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="reps">0</span></div>
              <div class="readout-label">Times typed</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">10</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>

          <div class="math-area">
            <div id="setup">
              <label class="ws-label" for="wordInput">Pick a word to spam</label>
              <div style="margin:0.6rem 0 1rem">
                <input class="math-input ws-input-wide" id="wordInput" type="text" maxlength="24"
                  autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false"
                  placeholder="e.g. speed" aria-label="Word to type">
              </div>
              <div class="seg-select" role="group" aria-label="Duration" id="durSelect">
                <button class="opt" data-dur="5" type="button" aria-pressed="false">5s</button>
                <button class="opt" data-dur="10" type="button" aria-pressed="true">10s</button>
                <button class="opt" data-dur="30" type="button" aria-pressed="false">30s</button>
                <button class="opt" data-dur="60" type="button" aria-pressed="false">60s</button>
              </div>
              <div style="margin-top:1rem">
                <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              </div>
            </div>

            <div id="active" hidden>
              <div class="ws-label">Type this word again and again</div>
              <div class="ws-target" id="target">speed</div>
              <input class="math-input ws-input-wide" id="typeInput" type="text"
                autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false"
                aria-label="Type the word" disabled>
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
    "slug": "word-spammer",
    "name": "Word Spammer",
    "crumb": "Word Spammer",
    "skip_target": "wordInput",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/word-spammer.js"],
    "title": "Word Spammer — Type a Word Fast Test | SpeedLab",
    "desc": "Pick any word and type it as many times as you can in 5, 10, 30 or 60 seconds. A fast, addictive typing test — see your reps and words-per-minute, beat your best.",
    "ld_desc": "Pick a word and type it repeatedly as fast as possible within a chosen time limit.",
    "og_title": "Word Spammer — Type a Word Fast",
    "og_desc": "Pick a word and spam it as fast as you can. How many reps?",
    "og_image": "default.png",
    "h1": "Word Spammer",
    "lead": "Pick any word, choose a time limit, and type that word over and over as fast as you possibly can. Count your reps and see your words-per-minute — then beat it.",
    "content": """      <h2>How Word Spammer works</h2>
      <p>Type any word into the box &mdash; your name, <em>speed</em>, a game you love, anything &mdash; and pick a time limit of <strong>5, 10, 30 or 60 seconds</strong>. When you hit Start, that word appears and the clock begins. Type it correctly and it instantly resets for the next go. Every clean rep counts. When the timer hits zero you get your total <strong>reps</strong> plus an equivalent <strong>words-per-minute</strong> score, so runs with different words and lengths still compare fairly.</p>

      <h2>Why let you pick the word?</h2>
      <p>Because a short, familiar word plays completely differently from a long or awkward one. <em>Cat</em> is a pure burst of finger speed; <em>rhythm</em> or <em>keyboard</em> tests your accuracy under pressure. Picking your own word turns it into a personal challenge &mdash; and it's a fun way to see which words your fingers already know cold.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 70 WPM</strong> &mdash; a relaxed pace.</li>
        <li><strong>100 to 130 WPM</strong> &mdash; fast; your muscle memory is kicking in.</li>
        <li><strong>160+ WPM</strong> &mdash; seriously quick repeat typing.</li>
      </ul>
      <p>Repeating one word is faster than normal typing, so these numbers run higher than a <a href="/typing-speed-test/">typing speed test</a> &mdash; that's expected.</p>

      <h2>Tips to spam faster</h2>
      <ul>
        <li><strong>Pick a short word</strong> for pure speed, a longer one for a real challenge.</li>
        <li><strong>Find a rhythm</strong> rather than mashing &mdash; smooth beats frantic.</li>
        <li><strong>Don't overshoot.</strong> One wrong letter means you have to fix it before the rep counts.</li>
      </ul>
      <p>Love keyboard challenges? Try the <a href="/typing-speed-test/">typing speed test</a>, <a href="/key-press-test/">key press test</a>, or <a href="/alphabet-typing-test/">alphabet typing test</a>.</p>""",
    "faq": [
        ("How is Word Spammer scored?",
         "You get your total reps (how many times you typed the word) and an equivalent words-per-minute score. WPM is used for the rank so different words and time limits still compare fairly."),
        ("Can I use any word?",
         "Yes — type any word or short phrase you like, up to 24 characters. Short familiar words are fastest; longer ones are a bigger challenge."),
        ("Why is my WPM higher than on a normal typing test?",
         "Because you're repeating one word your fingers already know, instead of reading new text. Repeat typing is naturally faster, so scores here run higher than a standard typing test."),
        ("Does it work on a phone?",
         "Yes. Tap the box to bring up your keyboard, pick a time limit, and type your word on repeat."),
    ],
    "related": [
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "How fast can you mash a key?"},
        {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z fast."},
        {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race from 1 to 100."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
