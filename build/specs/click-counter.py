CABINET = """    <section class="cabinet" id="clickcounter" aria-label="Click counter">
      <div class="marquee">Click Counter</div>

      <div class="screen" id="screen">
        <div class="readout-row">
          <div class="readout">
            <div class="seg-wrap"><span class="seg-value tnum" id="count">0</span></div>
            <div class="readout-label">Count</div>
          </div>
        </div>
        <div class="play-area">
          <button class="click-pad is-armed" id="pad" type="button" aria-label="Add one to the count">
            <span data-pad-title>Tap to count</span>
            <span class="hint">Click or tap here to add one</span>
          </button>
        </div>
      </div>

      <div class="counter-controls">
        <button class="btn btn-ghost" id="minus" type="button">&minus;&nbsp;1</button>
        <button class="btn btn-ghost" id="reset" type="button">Reset</button>
      </div>
      <p class="counter-note">Your count saves automatically on this device.</p>
    </section>"""

SPEC = {
    "slug": "click-counter",
    "name": "Click Counter",
    "crumb": "Click Counter",
    "skip_target": "pad",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/click-counter.js"],
    "title": "Click Counter — Free Online Tally Counter | SpeedLab",
    "desc": "A free online click counter and tally counter. Click or tap to count anything — laps, people, reps, inventory. Your count saves automatically in your browser.",
    "ld_desc": "A free online tally counter that saves your count in your browser.",
    "og_title": "Click Counter — Free Online Tally Counter",
    "og_desc": "Click or tap to count anything. Your count saves automatically.",
    "og_image": "click-counter.png",
    "h1": "Click Counter",
    "lead": "A simple tally counter for counting anything — laps, people, reps, or inventory. Tap the big button to add one; your count saves automatically on this device.",
    "content": """      <h2>How the click counter works</h2>
      <p>Tap or click the big button to add one to the count. Use the <strong>&minus; 1</strong> button to fix a miscount and <strong>Reset</strong> to start over from zero. There is no timer and no score &mdash; it is a plain tally counter, the kind people use for real tasks. Your current count is saved automatically in your browser, so you can close the page and pick up exactly where you left off.</p>

      <h2>What people use a tally counter for</h2>
      <ul>
        <li><strong>Counting people</strong> coming through a door or joining an event.</li>
        <li><strong>Laps or reps</strong> while running, swimming, or working out.</li>
        <li><strong>Stock and inventory</strong> when counting items by hand.</li>
        <li><strong>Games and hobbies</strong> &mdash; scores, stitches in knitting, or collectible counts.</li>
      </ul>
      <p>Because it works offline once loaded and keeps your number on your own device, it is a handy replacement for a physical handheld clicker &mdash; no batteries, and it is always in your pocket.</p>

      <h2>Tips</h2>
      <p>On a phone, add this page to your home screen for one-tap access. The keyboard works too: focus the button and press space or enter to count up. If you need to count how fast you can click instead of keeping a running tally, try the <a href="/cps-test/">CPS test</a>.</p>""",
    "faq": [
        ("Does my count get saved?",
         "Yes. Your count is stored in your browser on this device, so it stays even if you close the page. It is never uploaded anywhere."),
        ("How do I reset the counter?",
         "Press the Reset button to set the count back to zero. Use the minus button to subtract one if you miscount."),
        ("Does the click counter work offline?",
         "Yes. Once the page has loaded once, it works with no internet connection."),
        ("Can I count with my keyboard?",
         "Yes. Focus the count button and press space or enter to add one, which is handy for fast counting at a desk."),
    ],
    "related": [
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "Count clicks against the clock."},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "right-click-test", "kbd": "Mouse", "name": "Right Click Test", "desc": "How fast can you right click?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
