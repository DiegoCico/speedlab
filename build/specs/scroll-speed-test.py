CABINET = """    <section class="cabinet" id="scrollspeed" aria-label="Scroll speed test">
      <div class="marquee">Scroll Speed</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="px">0</span></div>
              <div class="readout-label">Pixels</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">10</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="scroll-box" id="box" tabindex="0" aria-label="Scroll inside this box as fast as you can">
            <div class="scroll-inner">
              <div class="scroll-stripes"></div>
              <div class="scroll-hint">Scroll here as fast as you can</div>
            </div>
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
    "slug": "scroll-speed-test",
    "name": "Scroll Speed Test",
    "crumb": "Scroll Speed Test",
    "skip_target": "box",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/scroll-speed.js"],
    "title": "Scroll Speed Test — How Fast Can You Scroll | SpeedLab",
    "desc": "Test your scrolling speed. See how many pixels you can scroll in 10 seconds with a mouse wheel, trackpad, or touchscreen, then beat your best.",
    "ld_desc": "Measure how many pixels you can scroll in 10 seconds.",
    "og_title": "Scroll Speed Test — How Fast Can You Scroll",
    "og_desc": "How many pixels can you scroll in 10 seconds? Beat your best.",
    "og_image": "scroll-speed-test.png",
    "h1": "Scroll Speed Test",
    "lead": "How far can you scroll in 10 seconds? Scroll inside the box as fast as you can with a wheel, trackpad, or finger. The timer starts on your first scroll.",
    "content": """      <h2>How the scroll speed test works</h2>
      <p>Scroll inside the box as fast as you can. Every pixel you move &mdash; up or down &mdash; is added to your total, and the box loops so you never hit a dead end. The timer starts the moment you begin scrolling and stops after 10 seconds, and your score is the total distance in pixels. It works with a mouse wheel, a laptop trackpad, or a finger on a touchscreen.</p>

      <h2>What is a good scroll speed?</h2>
      <p>Your result depends a lot on your device &mdash; a free-spinning mouse wheel or a trackpad flick covers far more ground than a notched wheel. As a rough guide:</p>
      <ul>
        <li><strong>Under 6,000 px</strong> &mdash; a gentle scroll.</li>
        <li><strong>12,000 to 20,000 px</strong> &mdash; right around average.</li>
        <li><strong>30,000 to 45,000 px</strong> &mdash; fast; you are really flicking.</li>
        <li><strong>65,000+ px</strong> &mdash; excellent scroll speed.</li>
      </ul>

      <h2>Tips to scroll faster</h2>
      <ul>
        <li><strong>Use a flick, then release</strong> on a trackpad or touchscreen so momentum keeps the scroll going.</li>
        <li><strong>Unlock your mouse wheel</strong> if it has a free-spin mode &mdash; it scrolls much farther per flick.</li>
        <li><strong>Alternate up and down</strong> instead of scrolling one direction; both count.</li>
      </ul>
      <p>Looking for more mobile tests? Try the <a href="/tap-speed-test/">tap speed test</a> and the <a href="/swipe-speed-test/">swipe speed test</a>.</p>""",
    "faq": [
        ("What counts as scroll distance?",
         "Every pixel of movement, whether you scroll up or down. The box loops endlessly so you can keep scrolling for the full 10 seconds."),
        ("Does it work on a phone?",
         "Yes. Swipe up and down inside the box with your finger. A quick flick with momentum covers the most distance."),
        ("Why does my mouse scroll so much farther than a trackpad?",
         "A free-spinning mouse wheel moves a huge number of pixels per flick, so results vary a lot by device. Compare your scores on the same hardware."),
        ("Does scrolling the box move the whole page?",
         "No. Scrolling stays inside the test box, so the page around it does not move while you play."),
    ],
    "related": [
        {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
        {"slug": "emoji-hunt", "kbd": "Mobile", "name": "Emoji Hunt", "desc": "Find the odd emoji out."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
