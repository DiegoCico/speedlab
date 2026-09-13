CABINET = """    <section class="cabinet" id="stroop" aria-label="Color match test">
      <div class="marquee">Color Match</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="correct">0</span></div>
              <div class="readout-label">Correct</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">30</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="stroop-area" id="area">
            <div class="stroop-prompt">Does the word match the ink colour?</div>
            <div class="stroop-word" id="word">READY</div>
            <div class="stroop-btns">
              <button class="btn btn-go" id="matchBtn" type="button" disabled>Match</button>
              <button class="btn btn-p1" id="noBtn" type="button" disabled>No match</button>
            </div>
            <button class="arcade-btn p1 stroop-start" id="startBtn" type="button">Start</button>
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
    "slug": "color-match",
    "name": "Color Match",
    "crumb": "Color Match (Stroop)",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/stroop.js"],
    "title": "Color Match — Stroop Test Speed Game | SpeedLab",
    "desc": "Play the Stroop color match test. Decide fast whether the word matches its ink colour and score as many correct answers as you can in 30 seconds.",
    "ld_desc": "Decide whether a colour word matches its ink colour, as fast as you can, in this Stroop test.",
    "og_title": "Color Match — Stroop Test Speed Game",
    "og_desc": "Does the word match its ink colour? Answer fast and score in 30 seconds.",
    "og_image": "color-match.png",
    "h1": "Color Match (Stroop Test)",
    "lead": "A colour word appears in a colour of ink. Decide whether the ink matches what the word says, as fast as you can. Score as many as possible in 30 seconds.",
    "content": """      <h2>How the color match test works</h2>
      <p>A colour word &mdash; like <em>RED</em> or <em>BLUE</em> &mdash; appears painted in some ink colour. Your job is to answer one question as fast as you can: <strong>does the ink colour match what the word says?</strong> Tap <strong>Match</strong> if they are the same and <strong>No match</strong> if they are different, and a new word appears instantly. You have 30 seconds, and your score is the number of correct answers. On a keyboard, the left arrow is Match and the right arrow is No match.</p>

      <h2>What is the Stroop effect?</h2>
      <p>This is a speed version of the famous <strong>Stroop test</strong>. Your brain reads words automatically, so when the word &ldquo;RED&rdquo; is printed in blue ink, the meaning and the colour fight each other and slow you down. That little clash is the Stroop effect, and it is why this test is trickier than it looks &mdash; you have to hold back the urge to just read the word.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 8 correct</strong> &mdash; the word keeps tricking you.</li>
        <li><strong>14 to 20 correct</strong> &mdash; a solid, focused round.</li>
        <li><strong>26 to 33 correct</strong> &mdash; fast and very accurate.</li>
        <li><strong>40+ correct</strong> &mdash; excellent focus under pressure.</li>
      </ul>
      <p>To improve, look at the <em>colour</em> of the letters first and let the meaning come second. For pure speed with no trick, try the <a href="/reaction-time-test/">reaction time test</a>.</p>""",
    "faq": [
        ("What is the Stroop test?",
         "It is a classic focus test where a colour word is shown in a different ink colour. Naming the ink is hard because your brain reads the word automatically."),
        ("How do I answer?",
         "Tap Match if the ink colour matches what the word says, or No match if they differ. On a keyboard, left arrow is Match and right arrow is No match."),
        ("What is a good color match score?",
         "Around 14 to 20 correct in 30 seconds is solid. 26 to 33 is fast, and 40 or more is excellent."),
        ("Why is it so tricky?",
         "Because you read words without meaning to. When the word and the ink colour disagree, the two clash and slow your answer down."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles for 30 seconds."},
        {"slug": "audio-reaction-test", "kbd": "Reaction", "name": "Audio Reaction Test", "desc": "React to a beep."},
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
