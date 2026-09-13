SPEC = {
    "slug": "tap-speed-test",
    "kind": "counter",
    "name": "Tap Speed Test",
    "crumb": "Tap Speed Test",
    "title": "Tap Speed Test — How Fast Can You Tap? | SpeedLab",
    "desc": "Test your tapping speed on your phone or tablet. Tap as fast as you can and see your taps per second, your rank, and how you compare to everyone else.",
    "ld_desc": "Measure how fast you can tap the screen in taps per second.",
    "og_title": "Tap Speed Test — How Fast Can You Tap?",
    "og_desc": "Tap as fast as you can and see your taps per second and rank.",
    "og_image": "tap-speed-test.png",
    "h1": "Tap Speed Test",
    "lead": "Tap the pad as fast as you can and see your taps per second. Built for phones and tablets, but a mouse works just as well. The timer starts on your first tap.",
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
      <p>On a computer? The <a href="/cps-test/">CPS test</a> and <a href="/spacebar-clicker/">spacebar clicker</a> are the mouse and keyboard versions of the same idea.</p>""",
    "faq": [
        ("What is a good tap speed?",
         "About 6 to 7 taps per second with one finger is average. Above 8 is fast, and holding over 10 usually means using two fingers."),
        ("How do I tap faster?",
         "Use two fingers or two thumbs alternating, rest your device on a surface, and keep your taps light and quick rather than tense."),
        ("Does the tap speed test work on a computer?",
         "Yes. Clicking the pad with a mouse works exactly like tapping, so you can take the test on any device."),
        ("Is tapping speed the same as CPS?",
         "It is measured the same way and lands in a similar range. Tap speed is just the touchscreen name for it, shown in taps per second."),
    ],
    "related": [
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The mouse version of this test."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "kohi-click-test", "kbd": "Mouse", "name": "Kohi Click Test", "desc": "Click speed for Minecraft."},
        {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
