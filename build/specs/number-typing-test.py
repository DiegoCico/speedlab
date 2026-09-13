CABINET = """    <section class="cabinet" id="seq" data-mode="number" aria-label="Number typing test">
      <div class="marquee">Number Typing</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">0.0</span></div>
              <div class="readout-label">Seconds</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="prog">0</span></div>
              <div class="readout-label">Progress %</div>
            </div>
          </div>
          <div class="type-stage">
            <div class="type-passage blurred" id="passage" tabindex="-1" aria-label="Type these numbers">
              <div class="type-lines" id="lines"></div>
            </div>
            <input class="type-input" id="typeInput" type="text" inputmode="numeric" autocomplete="off"
              autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Type here">
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Restart</button>
      </div>

      <div class="pb-strip">
        <span>Best time <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "number-typing-test",
    "name": "Number Typing Test",
    "crumb": "Number Typing Test",
    "skip_target": "passage",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/sequence-type.js"],
    "title": "Number Typing Test — Type 1 to 100 Fast | SpeedLab",
    "desc": "How fast can you type the numbers 1 to 100? Type them all in order as quickly as you can, with a space between each, and get your time, rank, and percentile.",
    "ld_desc": "Type the numbers 1 to 100 in order as fast as you can and time yourself.",
    "og_title": "Number Typing Test — Type 1 to 100 Fast",
    "og_desc": "How fast can you type 1 to 100? Time yourself and see your rank.",
    "og_image": "number-typing-test.png",
    "h1": "Number Typing Test",
    "lead": "Type the numbers from 1 to 100 in order, with a space between each. The timer starts on your first key and stops the instant you reach 100. Speed and accuracy both count.",
    "content": """      <h2>How the number typing test works</h2>
      <p>The numbers 1 through 100 appear on the screen. Type them in order &mdash; <strong>1</strong>, space, <strong>2</strong>, space, and so on &mdash; as fast as you can. The timer starts on your first key and stops the moment you correctly type 100. Each character turns green when it is right and pink when it is wrong, and mistakes must be fixed before you can finish. Your score is your completion time in seconds, so lower is better.</p>

      <h2>What is a good time?</h2>
      <p>Typing 1 to 100 is a real test of number-row speed and stamina, since it is nearly 200 characters. As a rough guide:</p>
      <ul>
        <li><strong>Over 95 seconds</strong> &mdash; taking it steady.</li>
        <li><strong>55 to 70 seconds</strong> &mdash; a solid, consistent run.</li>
        <li><strong>35 to 50 seconds</strong> &mdash; fast; your number row is dialled in.</li>
        <li><strong>Under 35 seconds</strong> &mdash; excellent number-typing speed.</li>
      </ul>

      <h2>How to get faster</h2>
      <ul>
        <li><strong>Learn the number row</strong> so you are not glancing up for every digit.</li>
        <li><strong>Use your thumb for the space bar</strong> and keep a steady one-two rhythm between numbers.</li>
        <li><strong>Don't rush the two-digit numbers</strong> &mdash; smooth beats frantic, because fixing errors costs more time.</li>
      </ul>
      <p>Prefer letters? Race the <a href="/alphabet-typing-test/">alphabet typing test</a>, or measure real typing with the <a href="/typing-speed-test/">typing speed test</a>.</p>""",
    "faq": [
        ("How do I type the numbers?",
         "Type each number in order with a single space between them: 1, space, 2, space, 3, and so on up to 100."),
        ("What is a good number typing time?",
         "Around 55 to 70 seconds is a solid run. Under 50 is fast, and under 35 seconds is excellent."),
        ("Do mistakes matter?",
         "Yes. A wrong character turns pink and must be fixed before you can finish, so accuracy affects your time."),
        ("Does it work on a phone?",
         "Yes. Tap the numbers area to open your keyboard. A numeric keypad layout makes it much quicker on mobile."),
    ],
    "related": [
        {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z as fast as you can."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "Raw finger speed, any keys."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
