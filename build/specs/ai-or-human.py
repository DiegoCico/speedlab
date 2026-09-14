CABINET = """    <section class="cabinet" id="aihuman" aria-label="AI or Human game">
      <div class="marquee">AI or Human?</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="correct">0</span></div>
              <div class="readout-label">Correct</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="wrong">0</span></div>
              <div class="readout-label">Wrong</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">0</span></div>
              <div class="readout-label">Seconds</div>
            </div>
          </div>
          <div class="aih-area" id="area">
            <div class="aih-progress" id="progress"></div>
            <p class="aih-prompt" id="prompt">Tap Start, then decide for each line: human or AI?</p>
            <div class="aih-btns">
              <button class="btn btn-p2" id="humanBtn" type="button" disabled>Human</button>
              <button class="btn btn-p1" id="aiBtn" type="button" disabled>AI</button>
            </div>
            <button class="arcade-btn p1 aih-start" id="startBtn" type="button">Start</button>
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
    "slug": "ai-or-human",
    "name": "AI or Human",
    "crumb": "AI or Human",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/ai-or-human.js"],
    "title": "AI or Human? — Spot the AI Text Game | SpeedLab",
    "desc": "Can you tell AI writing from a real person? Read each line and call it Human or AI against the clock. 60 seconds, tracking correct vs wrong, with your rank.",
    "ld_desc": "Decide whether each line of text was written by a human or an AI, against a 60-second clock.",
    "og_title": "AI or Human? — Spot the AI",
    "og_desc": "Read each line and call it Human or AI against the clock. Can you tell?",
    "og_image": "ai-or-human.png",
    "h1": "AI or Human?",
    "lead": "Five lines of text, one at a time — decide whether a real person or an AI wrote each, as fast as you can. The timer counts up and we track your correct and wrong calls.",
    "content": """      <h2>How the AI or Human game works</h2>
      <p>Press Start and a short line of text appears. Your job: decide whether it was written by a <strong>human</strong> or an <strong>AI</strong>, and tap the matching button. You get <strong>5 lines</strong> in a row, and the timer <strong>counts up</strong> so you can see how quickly you called them. We keep a running tally of your <strong>correct</strong> and <strong>wrong</strong> answers, and your score is how many of the 5 you get right. On a keyboard, the left arrow is Human and the right arrow is AI.</p>
      <p>The lines are labelled based on <em>common</em> tells, so treat it as a fun, educational game rather than a perfect detector — real AI and real people don't always follow the pattern.</p>

      <h2>Tells that a line might be AI</h2>
      <ul>
        <li><strong>Over-polished and generic</strong> — tidy, balanced, and could apply to anything.</li>
        <li><strong>Hedging phrases</strong> like "it's important to note" or "results may vary."</li>
        <li><strong>Lists of three</strong> and neat conclusions ("in conclusion…").</li>
        <li><strong>Buzzwords</strong> — "delve," "tapestry," "seamlessly," "unlock your potential."</li>
      </ul>

      <h2>Tells that a line is probably human</h2>
      <ul>
        <li><strong>Specific, odd details</strong> — a broken L key, a jello salad, a howling dog.</li>
        <li><strong>Mess and feeling</strong> — typos, slang, mild complaints, real opinions.</li>
        <li><strong>Incomplete thoughts</strong> that trail off the way people actually type.</li>
      </ul>
      <p>Enjoy word puzzles? Try <a href="/woordle/">Woordle</a> or the focus-testing <a href="/color-match/">color match</a>.</p>""",
    "faq": [
        ("How is the AI or Human game scored?",
         "You get 5 lines and score one point for each you call correctly, so your score is out of 5. Wrong calls are tracked too, and the timer shows how fast you answered."),
        ("Is this a real AI detector?",
         "No. The lines are labelled using common AI writing tells, so it's a fun, educational game — not a reliable way to detect AI in the wild."),
        ("How do I answer with a keyboard?",
         "Press the left arrow (or H) for Human and the right arrow (or A) for AI. On a phone, just tap the Human or AI buttons."),
        ("What's a good score?",
         "4 or 5 out of 5 shows a sharp eye for AI writing. 3 is around a coin-flip, so aim to beat that consistently and quickly."),
    ],
    "related": [
        {"slug": "woordle", "kbd": "Word", "name": "Woordle", "desc": "Guess the word in 6 tries."},
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match", "desc": "Does the word match the ink?"},
        {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the growing number."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
