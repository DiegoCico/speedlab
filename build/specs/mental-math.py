CABINET = """    <section class="cabinet" id="mathsprint" aria-label="Mental math sprint">
      <div class="marquee">Mental Math</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="correct">0</span></div>
              <div class="readout-label">Correct</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">60</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="math-area">
            <div class="math-problem" id="problem">7 &times; 8 =</div>
            <input class="math-input" id="answer" type="text" inputmode="numeric" pattern="[0-9]*"
              autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Your answer" disabled>
            <button class="arcade-btn p1" id="startBtn" type="button">Start</button>
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
    "slug": "mental-math",
    "name": "Mental Math",
    "crumb": "Mental Math",
    "skip_target": "answer",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/math-sprint.js"],
    "title": "Mental Math Sprint — Math Speed Test | SpeedLab",
    "desc": "Test your mental math speed. Solve as many quick addition, subtraction and multiplication problems as you can in 60 seconds, and see how you rank.",
    "ld_desc": "Solve as many quick arithmetic problems as you can in 60 seconds.",
    "og_title": "Mental Math Sprint — Math Speed Test",
    "og_desc": "How many math problems can you solve in 60 seconds?",
    "og_image": "mental-math.png",
    "h1": "Mental Math Sprint",
    "lead": "Solve as many quick math problems as you can in 60 seconds. Just type the answer — it checks itself the instant it's right, then throws the next one at you.",
    "content": """      <h2>How the mental math test works</h2>
      <p>Press Start and a problem appears — addition, subtraction, or multiplication. Type the answer and it's checked <strong>automatically</strong> the moment it's correct, so there's no button to press between problems. You have <strong>60 seconds</strong>, and your score is how many you solve. It's a pure test of mental arithmetic speed, and it gets addictive fast.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 8</strong> — taking your time on each one.</li>
        <li><strong>14 to 20</strong> — a solid, quick pace.</li>
        <li><strong>27 to 35</strong> — fast; your times tables are locked in.</li>
        <li><strong>45+</strong> — excellent mental math.</li>
      </ul>

      <h2>Tips to go faster</h2>
      <ul>
        <li><strong>Know your times tables cold</strong> — multiplication is where most people slow down.</li>
        <li><strong>Break big additions apart</strong>: 47 + 38 → 47 + 40 − 2.</li>
        <li><strong>Don't second-guess</strong> the easy ones — trust the first answer and move on.</li>
      </ul>
      <p>Want a different kind of brain test? Try <a href="/number-memory/">number memory</a> or the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("What kind of math is on the test?",
         "Quick addition, subtraction, and multiplication with small numbers — the kind you can do in your head. No calculators needed or allowed."),
        ("How is it scored?",
         "One point for each correct answer in 60 seconds. The answer checks itself as you type, so you never lose time pressing submit."),
        ("What is a good mental math score?",
         "Around 14 to 20 in 60 seconds is solid. 27 to 35 is fast, and 45 or more is excellent."),
        ("Does it work on a phone?",
         "Yes. Tap the answer box to bring up the number pad and type your answers."),
    ],
    "related": [
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race from 1 to 100."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
