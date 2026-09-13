CABINET = """    <section class="cabinet" id="swipespeed" aria-label="Swipe speed test">
      <div class="marquee">Swipe Speed</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="count">0</span></div>
              <div class="readout-label">Swipes</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">10</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="swipe-pad" id="pad">
            <span>Swipe here</span>
            <span class="hint">Swipe back and forth as fast as you can for 10s</span>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button>
      </div>

      <div class="pb-strip">
        <span>Best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "swipe-speed-test",
    "name": "Swipe Speed Test",
    "crumb": "Swipe Speed Test",
    "skip_target": "pad",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/swipe-speed.js"],
    "title": "Swipe Speed Test — How Fast Can You Swipe | SpeedLab",
    "desc": "Test your swipe speed. Swipe back and forth as fast as you can for 10 seconds and see how many swipes you rack up, your rank, and how you compare.",
    "ld_desc": "Count how many swipes you can make in 10 seconds.",
    "og_title": "Swipe Speed Test — How Fast Can You Swipe",
    "og_desc": "Swipe back and forth as fast as you can for 10 seconds.",
    "og_image": "swipe-speed-test.png",
    "h1": "Swipe Speed Test",
    "lead": "Swipe across the pad as fast as you can, back and forth, for 10 seconds. Every flick of movement counts as a swipe. Built for touchscreens; a mouse drag works too.",
    "content": """      <h2>How the swipe speed test works</h2>
      <p>Drag your finger &mdash; or the mouse &mdash; across the pad as fast as you can. Every chunk of swipe movement counts as one swipe, so quick back-and-forth flicking racks up your count fastest. The timer starts on your first swipe and runs for 10 seconds, and your score is the total number of swipes. It is the swiping cousin of the <a href="/tap-speed-test/">tap speed test</a>, built for thumbs on a phone.</p>

      <h2>What is a good swipe speed?</h2>
      <ul>
        <li><strong>Under 8 swipes</strong> &mdash; a gentle pace.</li>
        <li><strong>14 to 20 swipes</strong> &mdash; right around average.</li>
        <li><strong>26 to 34 swipes</strong> &mdash; fast; your thumb is flying.</li>
        <li><strong>44+ swipes</strong> &mdash; excellent swipe speed.</li>
      </ul>

      <h2>Tips to swipe faster</h2>
      <ul>
        <li><strong>Swipe back and forth</strong> in short, sharp flicks rather than long slow drags.</li>
        <li><strong>Use your thumb</strong> on a phone and keep the motion loose from the wrist.</li>
        <li><strong>Stay on the pad</strong> &mdash; swipes only count while your finger is down on it.</li>
      </ul>
      <p>More mobile tests: the <a href="/scroll-speed-test/">scroll speed test</a> and the <a href="/tap-speed-test/">tap speed test</a>.</p>""",
    "faq": [
        ("What counts as one swipe?",
         "Each chunk of swipe movement across the pad counts as a swipe, so continuous back-and-forth flicking adds up quickly."),
        ("What is a good swipe speed?",
         "Around 14 to 20 swipes in 10 seconds is average. 26 to 34 is fast, and 44 or more is excellent."),
        ("Does it work with a mouse?",
         "Yes. Hold the button and drag across the pad. It is designed for touch, but a mouse drag counts the same way."),
        ("Do swipes count if I lift my finger?",
         "Swipes only register while your finger or mouse button is down on the pad. Lifting off just pauses the count."),
    ],
    "related": [
        {"slug": "scroll-speed-test", "kbd": "Mobile", "name": "Scroll Speed Test", "desc": "How far can you scroll in 10s?"},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
        {"slug": "emoji-hunt", "kbd": "Mobile", "name": "Emoji Hunt", "desc": "Find the odd emoji out."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
