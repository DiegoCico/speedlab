CABINET = """    <section class="cabinet" id="numbermemory" aria-label="Number memory test">
      <div class="marquee">Number Memory</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="level">1</span></div>
              <div class="readout-label">Digits</div>
            </div>
          </div>
          <div class="mem-stage">
            <div class="mem-center" id="startWrap">
              <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
              <p class="mem-hint">Memorize the number, then type it back. It gets one digit longer every round.</p>
            </div>
            <div class="mem-center" id="phaseShow" hidden>
              <div class="mem-number" id="numDisplay">0</div>
              <div class="mem-bar"><div class="mem-bar-fill" id="bar"></div></div>
            </div>
            <div class="mem-center" id="phaseInput" hidden>
              <input class="mem-input" id="numInput" type="text" inputmode="numeric"
                autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Type the number">
              <button class="btn btn-p1" id="submitBtn" type="button">Submit</button>
              <p class="mem-feedback" id="feedback"></p>
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
    "slug": "number-memory",
    "name": "Number Memory",
    "crumb": "Number Memory",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/number-memory.js"],
    "title": "Number Memory Test — How Many Digits? | SpeedLab",
    "desc": "Test your number memory. A number flashes, then you type it back — and it gets one digit longer each round. See how many digits you can remember.",
    "ld_desc": "See how many digits you can remember as the number grows each round.",
    "og_title": "Number Memory Test — How Many Digits?",
    "og_desc": "A number flashes, then you type it back. It grows each round.",
    "og_image": "number-memory.png",
    "h1": "Number Memory Test",
    "lead": "A number flashes on the screen, then disappears. Type it back from memory. Each round it grows by one digit — how far can you get?",
    "content": """      <h2>How the number memory test works</h2>
      <p>A number appears on the screen for a short time, shown a little longer as it gets bigger. When it disappears, type what you saw and press submit. Get it right and the next number is one digit longer; get it wrong and the game ends. Your score is the number of digits you managed to remember, so it climbs as high as your memory can carry it.</p>

      <h2>What is a good number memory score?</h2>
      <p>Most people can hold about seven digits in short-term memory &mdash; which is why phone numbers are around that length. Here is the rough scale:</p>
      <ul>
        <li><strong>Under 6 digits</strong> &mdash; a quick, casual attempt.</li>
        <li><strong>7 digits</strong> &mdash; right around the human average.</li>
        <li><strong>9 to 11 digits</strong> &mdash; a strong memory.</li>
        <li><strong>12+ digits</strong> &mdash; excellent; you are chunking like a pro.</li>
      </ul>

      <h2>How to remember more digits</h2>
      <ul>
        <li><strong>Chunk the number</strong> into small groups, like a phone number: 4 8 1 &mdash; 9 2 6 rather than one long string.</li>
        <li><strong>Say it in your head</strong> in a steady rhythm as it appears.</li>
        <li><strong>Turn digits into a story or a date</strong> for the longer numbers &mdash; meaning is easier to hold than random digits.</li>
      </ul>
      <p>Enjoy this? Try the pattern-based <a href="/sequence-memory/">sequence memory</a> and <a href="/visual-memory/">visual memory</a> tests, or the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("What is a good number memory score?",
         "About 7 digits is average. 9 to 11 is a strong memory, and 12 or more is excellent."),
        ("Why is the number shown longer as it grows?",
         "Longer numbers naturally take more time to read, so the display time scales with the number of digits to keep it fair."),
        ("How can I remember more digits?",
         "Break the number into small chunks, like a phone number, and repeat it in a steady rhythm as it appears."),
        ("Does it work on a phone?",
         "Yes. When it is time to answer, tap the box to bring up the numeric keypad and type the number."),
    ],
    "related": [
        {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the growing pattern."},
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Reproduce the flashed tiles."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
