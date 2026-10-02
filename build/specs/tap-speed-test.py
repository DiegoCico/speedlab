SPEC = {
    "slug": "tap-speed-test",
    "kind": "counter",
    "name": "Tap Speed Test",
    "crumb": "Tap Speed Test",
    "title": "Tap Speed Test — How Many Taps Per Second? | SpeedLab",
    "desc": "Tap as fast as you can and see your taps per second. A free tapping speed test for phone or desktop — pick a timer, beat your best, and see how you rank.",
    "ld_desc": "Measure how fast you can tap the screen in taps per second over a chosen time limit.",
    "og_title": "Tap Speed Test — Taps Per Second",
    "og_desc": "Tap as fast as you can and see your taps per second and rank.",
    "og_image": "tap-speed-test.png",
    "h1": "Tap Speed Test",
    "lead": "Tap as fast as you can and watch your taps per second climb. It's the tapping speed test built for phones and tablets — a mouse works just as well. Pick a time limit; the timer starts on your first tap.",
    "counter": {
        "testid": "tap", "input": "pointer",
        "durations": [5, 10, 15, 30, 60, 100], "default": 10,
        "name": "Tap Speed Test", "marquee": "Tap Speed Test",
        "count_label": "Taps", "hint": "Tap here as fast as you can",
    },
    "content": """      <h2>How the tap speed test works</h2>
      <p>The tap speed test measures how many times you can tap the screen in a set number of seconds. It is the touchscreen version of the <a href="/cps-test/">CPS test</a>: choose a duration, tap the pad as fast as you can, and your speed shows up in taps per second. The timer starts on your first tap and stops on its own, so the whole run counts. Each duration keeps its own personal best on this device.</p>

      <h2>What is a good tapping speed?</h2>
      <p>Tapping speed is close to clicking speed for most people &mdash; around <strong>6 to 7 taps per second</strong> with one finger. Push past 8 and you are quick; hold above 10 and you are among the fastest. Short runs reward a fast burst, longer ones test whether you can keep the pace.</p>
      <ul>
        <li><strong>Under 4 TPS</strong> &mdash; a relaxed, everyday tap.</li>
        <li><strong>6 to 7.5 TPS</strong> &mdash; right around average.</li>
        <li><strong>8 to 11 TPS</strong> &mdash; fast; you have practised.</li>
        <li><strong>11+ TPS</strong> &mdash; usually two fingers rather than one.</li>
      </ul>

      <h2>How to tap faster</h2>
      <ul>
        <li><strong>Use two fingers or two thumbs</strong>, alternating them like a drum roll.</li>
        <li><strong>Rest your device</strong> on a table so your hand is free to move fast.</li>
        <li><strong>Stay loose</strong> &mdash; light, quick taps beat hard, tense ones.</li>
      </ul>
      <p>On a computer? The <a href="/cps-test/">CPS test</a> and <a href="/spacebar-clicker/">spacebar clicker</a> are the mouse and keyboard versions of the same idea. Want the full breakdown of what's fast and how to get there? Read our guide on <a href="/guides/what-is-a-good-tapping-speed/">what a good tapping speed is</a>.</p>

      <h2>Tap test by length</h2>
      <p>Each timed length of the tapping test has its own page and personal best: <a href="/tap-speed-test/5-second/">5 second</a> &middot; <a href="/tap-speed-test/10-second/">10 second</a>. Whichever you pick, the goal is the same &mdash; tap as fast as you can and push your taps-per-second up.</p>""",
    "faq": [
        ("What is a good tap speed?",
         "About 6 to 7 taps per second with one finger is average. Above 8 is fast, and holding over 10 taps per second usually means using two fingers."),
        ("What is the average taps per second?",
         "Most people tap around 6 to 7 times per second with a single finger on a tap speed test. Two fingers alternating can push well past 10."),
        ("How do I tap faster?",
         "Use two fingers or two thumbs alternating like a drum roll, rest your device on a surface, and keep your taps light and quick rather than tense."),
        ("Does the tap speed test work on a computer?",
         "Yes. Clicking the pad with a mouse works exactly like tapping, so you can take the tapping test on a phone, tablet, or desktop."),
        ("Is tapping speed the same as CPS?",
         "It is measured the same way and lands in a similar range. Tap speed is just the touchscreen name for it, shown in taps per second."),
    ],
    "related": [
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The mouse version of this test."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "guides/what-is-a-good-tapping-speed", "kbd": "Guide", "name": "Good tapping speed?", "desc": "What's fast and how to improve."},
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "How fast can you mash keys?"},
        {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
