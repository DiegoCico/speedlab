CABINET = """    <section class="cabinet" id="typing" data-duration="30" aria-label="Typing speed test">
      <div class="marquee">Typing Speed Test</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="wpm">0</span></div>
              <div class="readout-label">WPM</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="acc">100</span></div>
              <div class="readout-label">Accuracy %</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">30</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="type-stage">
            <div class="type-passage blurred" id="passage" tabindex="-1" aria-label="Type this text">
              <div class="type-lines" id="lines"></div>
            </div>
            <input class="type-input" id="typeInput" type="text" autocomplete="off"
              autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Type here">
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button>
      </div>

      <div class="seg-select" role="group" aria-label="Test duration">
        <button class="opt" data-dur="15" type="button" aria-pressed="false">15s</button>
        <button class="opt" data-dur="30" type="button" aria-pressed="true">30s</button>
        <button class="opt" data-dur="60" type="button" aria-pressed="false">60s</button>
      </div>

      <div class="pb-strip">
        <span>Personal best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "typing-speed-test",
    "name": "Typing Speed Test",
    "crumb": "Typing Speed Test",
    "skip_target": "passage",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/typing.js"],
    "title": "Typing Speed Test — Words Per Minute (WPM) | SpeedLab",
    "desc": "Test your typing speed in words per minute with live WPM and accuracy. Choose 15, 30 or 60 seconds, beat your best, and see how fast you really type.",
    "ld_desc": "Measure your typing speed in words per minute with live WPM and accuracy.",
    "og_title": "Typing Speed Test — Words Per Minute",
    "og_desc": "Test your typing speed in WPM with live accuracy. Beat your best.",
    "og_image": "typing-speed-test.png",
    "h1": "Typing Speed Test",
    "lead": "Type the words as they appear and watch your speed climb. We measure words per minute and accuracy live; the timer starts the moment you type your first letter.",
    "content": """      <h2>How the typing speed test works</h2>
      <p>Start typing the passage shown on the screen. The timer begins on your first keystroke and counts down from the duration you picked. As you type, each letter turns green when it is correct and pink when it is wrong, and your <strong>words per minute</strong> and <strong>accuracy</strong> update live. When time runs out we show your final WPM, how accurate you were, and your rank.</p>
      <p>WPM here is the standard measure: every five correct characters counts as one word, divided by the minutes you spent. That means errors cost you &mdash; typing fast is only worth it if the letters are right. Each duration keeps its own personal best on this device.</p>

      <h2>What is a good typing speed?</h2>
      <p>The average adult types around <strong>40 words per minute</strong>. Touch typists who don't look at the keyboard usually land between 60 and 80, and professional typists push past 100. Here is the scale on this test:</p>
      <ul>
        <li><strong>Under 25 WPM</strong> &mdash; still hunting and pecking for keys.</li>
        <li><strong>40 to 55 WPM</strong> &mdash; a solid, everyday typing speed.</li>
        <li><strong>70 to 90 WPM</strong> &mdash; fast; you touch type comfortably.</li>
        <li><strong>110+ WPM</strong> &mdash; professional-level speed.</li>
      </ul>

      <h2>How to type faster</h2>
      <ul>
        <li><strong>Learn touch typing</strong> &mdash; keep your fingers on the home row and don't look down. It feels slower at first, then much faster.</li>
        <li><strong>Aim for accuracy first.</strong> Speed follows accuracy, not the other way around. Fixing mistakes wastes more time than typing carefully.</li>
        <li><strong>Use all ten fingers</strong> and let each one cover its own keys.</li>
        <li><strong>Practise little and often.</strong> A few short tests a day build real muscle memory.</li>
      </ul>
      <p>Want raw finger speed instead of real words? Try the <a href="/key-press-test/">key press speed test</a>, or race the <a href="/alphabet-typing-test/">alphabet</a> from A to Z.</p>

      <h2>Typing test by length</h2>
      <p>Each length has its own page and personal best: <a href="/typing-speed-test/15-second/">15 second</a> &middot; <a href="/typing-speed-test/30-second/">30 second</a> &middot; <a href="/typing-speed-test/1-minute/">1 minute</a> &middot; <a href="/typing-speed-test/3-minute/">3 minute</a> &middot; <a href="/typing-speed-test/5-minute/">5 minute</a>.</p>""",
    "faq": [
        ("What is a good typing speed?",
         "The average is about 40 WPM. Comfortable touch typists reach 60 to 80, and professionals type over 100 words per minute."),
        ("How is WPM calculated?",
         "Every five correct characters counts as one word, divided by the time in minutes. Mistakes lower your score, so accuracy matters."),
        ("What is a good accuracy percentage?",
         "Aim for 95% or higher. High accuracy usually means a higher WPM too, because you waste less time fixing errors."),
        ("Does the typing test work on a phone?",
         "Yes. Tap the passage to bring up your keyboard and start typing. It works with any keyboard, on-screen or physical."),
    ],
    "related": [
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "Raw finger speed, any keys."},
        {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z as fast as you can."},
        {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race from 1 to 100."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
