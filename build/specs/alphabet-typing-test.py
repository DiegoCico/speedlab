def cabinet(mode, marquee, label, seconds_label="Seconds"):
    return """    <section class="cabinet" id="seq" data-mode="%s" aria-label="%s">
      <div class="marquee">%s</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">0.0</span></div>
              <div class="readout-label">%s</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="prog">0</span></div>
              <div class="readout-label">Progress %%</div>
            </div>
          </div>
          <div class="type-stage">
            <div class="type-passage blurred" id="passage" tabindex="-1" aria-label="Type this">
              <div class="type-lines" id="lines"></div>
            </div>
            <input class="type-input" id="typeInput" type="text" autocomplete="off"
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
    </section>""" % (mode, label, marquee, seconds_label)

SPEC = {
    "slug": "alphabet-typing-test",
    "name": "Alphabet Typing Test",
    "crumb": "Alphabet Typing Test",
    "skip_target": "passage",
    "cabinet": cabinet("alphabet", "Alphabet Typing", "Alphabet typing test"),
    "scripts": ["/assets/js/tests/sequence-type.js"],
    "title": "Alphabet Typing Test — Type A to Z Fast | SpeedLab",
    "desc": "How fast can you type the whole alphabet? Type A to Z as quickly as you can and get your time in seconds, your rank, and how you compare to everyone else.",
    "ld_desc": "Type the alphabet from A to Z as fast as you can and time yourself.",
    "og_title": "Alphabet Typing Test — Type A to Z Fast",
    "og_desc": "How fast can you type A to Z? Time yourself and see your rank.",
    "og_image": "alphabet-typing-test.png",
    "h1": "Alphabet Typing Test",
    "lead": "Type the alphabet from A to Z as fast as you can. The timer starts on your first letter and stops the instant you finish. Wrong letters must be fixed to continue.",
    "content": """      <h2>How the alphabet typing test works</h2>
      <p>The whole alphabet appears on the screen. Start typing from <strong>a</strong> and race to <strong>z</strong>; the timer begins on your first key and stops the moment the sequence is complete and correct. Each letter turns green when it is right and pink when it is wrong &mdash; and a wrong letter must be corrected before you can finish, so accuracy counts as much as speed. Your score is your completion time in seconds, and lower is better.</p>

      <h2>What is a good alphabet time?</h2>
      <p>Typing the alphabet is partly about typing skill and partly about how well you know the key positions without thinking. As a rough guide:</p>
      <ul>
        <li><strong>Over 15 seconds</strong> &mdash; still finding the keys.</li>
        <li><strong>8 to 11 seconds</strong> &mdash; a solid, steady run.</li>
        <li><strong>6 to 8 seconds</strong> &mdash; fast and confident.</li>
        <li><strong>Under 6 seconds</strong> &mdash; excellent; you barely pause.</li>
      </ul>

      <h2>How to get faster</h2>
      <ul>
        <li><strong>Use both hands</strong> and let each finger cover its own part of the keyboard.</li>
        <li><strong>Don't look down.</strong> Trusting your muscle memory is faster than hunting for each key.</li>
        <li><strong>Stay smooth, not frantic.</strong> A steady rhythm beats stabbing at keys and having to fix mistakes.</li>
      </ul>
      <p>Ready for real words? Try the <a href="/typing-speed-test/">typing speed test</a> for words per minute, or race the numbers in the <a href="/number-typing-test/">number typing test</a>.</p>""",
    "faq": [
        ("What is a good alphabet typing time?",
         "Around 8 to 11 seconds is a solid run. Under 8 is fast, and under 6 seconds is excellent."),
        ("Do I have to fix mistakes?",
         "Yes. A wrong letter turns pink and you must correct it before the sequence counts as complete, so accuracy matters."),
        ("Does it work on a phone?",
         "Yes. Tap the letters area to bring up your keyboard, then type A to Z. It works with any keyboard."),
        ("Why time the alphabet instead of words?",
         "The alphabet is a simple, fair test of how well you know the keys. For real typing skill, try the words-per-minute typing test."),
    ],
    "related": [
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race from 1 to 100."},
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "Raw finger speed, any keys."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
