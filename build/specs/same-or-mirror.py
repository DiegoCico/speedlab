CABINET = """    <section class="cabinet" id="mentalrotation" aria-label="Same or mirror">
      <div class="marquee">Same or Mirror</div>

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
          <div class="rot-area" id="rotArea">
            <div class="rot-pair">
              <div class="rot-glyph ref" id="refShape" aria-label="Reference shape">F</div>
              <div class="rot-vs">vs</div>
              <div class="rot-glyph" id="testShape" aria-label="Shape to compare" style="transform:rotate(90deg)">F</div>
            </div>
            <div class="rot-buttons">
              <button class="arcade-btn p2" id="sameBtn" type="button" disabled>Same</button>
              <button class="arcade-btn p1" id="mirrorBtn" type="button" disabled>Mirror</button>
            </div>
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
    "slug": "same-or-mirror",
    "name": "Same or Mirror",
    "crumb": "Same or Mirror",
    "skip_target": "startBtn",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/mental-rotation.js"],
    "title": "Same or Mirror — Mental Rotation Test | SpeedLab",
    "desc": "Is the rotated letter the same shape or a mirror image? A fast mental rotation test — decide as many as you can in 60 seconds and see how you rank.",
    "ld_desc": "Decide whether a rotated letter is the same shape or a mirror image, as fast as you can in 60 seconds.",
    "og_title": "Same or Mirror — Mental Rotation Test",
    "og_desc": "Same shape or mirror image? Decide fast.",
    "og_image": "same-or-mirror.png",
    "h1": "Same or Mirror",
    "lead": "One letter, then a rotated copy. Is it the same shape just turned around, or a mirror image? Decide as many as you can in 60 seconds.",
    "content": """      <h2>How the mental rotation test works</h2>
      <p>You see a reference letter on the left and a rotated copy on the right. Your job: tell whether the copy is the <strong>same</strong> shape simply turned to a new angle, or a <strong>mirror</strong> image of it. Press Same or Mirror. Right answers score a point; wrong answers cost you a moment before the next pair. You have 60 seconds, and your score is how many you get right. It measures <em>mental rotation</em> — spinning a shape in your mind's eye.</p>

      <h2>What is a good score?</h2>
      <ul>
        <li><strong>Under 6</strong> — still finding the trick.</li>
        <li><strong>10 to 15</strong> — a good pace.</li>
        <li><strong>20 to 26</strong> — fast spatial reasoning.</li>
        <li><strong>32+</strong> — excellent.</li>
      </ul>

      <h2>Tips to decide faster</h2>
      <ul>
        <li><strong>Find one distinctive feature</strong> — like which way an F's arms point — and track just that.</li>
        <li><strong>Mentally rotate the copy upright</strong>, then check if it matches or is flipped.</li>
        <li><strong>Don't guess</strong> — a wrong answer costs more time than thinking for a beat.</li>
      </ul>
      <p>Keyboard shortcuts: press <strong>S</strong> or Left for Same, <strong>M</strong> or Right for Mirror. Enjoy spatial puzzles? Try <a href="/visual-memory/">visual memory</a> or the <a href="/chimp-test/">chimp test</a>.</p>""",
    "faq": [
        ("What is mental rotation?",
         "Mental rotation is the ability to picture how a shape would look if it were turned to a different angle. This test challenges it by asking whether a rotated letter is the same shape or a mirror image."),
        ("How is Same or Mirror scored?",
         "By how many pairs you answer correctly in 60 seconds. Right answers score a point; wrong answers add a short delay before the next pair."),
        ("What is a good score?",
         "Getting 10 to 15 correct is a good pace, 20 to 26 is fast, and 32 or more is excellent."),
        ("Can I use the keyboard?",
         "Yes. Press S or the Left arrow for Same, and M or the Right arrow for Mirror. On a phone, just tap the buttons."),
    ],
    "related": [
        {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Remember the flashed tiles."},
        {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Click the numbers in order."},
        {"slug": "count-the-flash", "kbd": "Brain", "name": "Count the Flash", "desc": "Count the dots in a flash."},
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match (Stroop)", "desc": "Word vs ink colour."},
        {"slug": "mental-math", "kbd": "Brain", "name": "Mental Math Sprint", "desc": "Solve as many as you can."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
