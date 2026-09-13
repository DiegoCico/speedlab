SPEC = {
    "slug": "key-press-test",
    "kind": "counter",
    "name": "Key Press Speed Test",
    "crumb": "Key Press Speed Test",
    "title": "Key Press Speed Test — How Fast Can You Type Keys | SpeedLab",
    "desc": "Test how fast you can press keys on your keyboard. Mash any key as fast as you can and see your key presses per second, your rank, and how you compare.",
    "ld_desc": "Measure how many keys you can press per second.",
    "og_title": "Key Press Speed Test — Keys Per Second",
    "og_desc": "Mash the keyboard as fast as you can and see your key presses per second.",
    "og_image": "key-press-test.png",
    "h1": "Key Press Speed Test",
    "lead": "How fast can your fingers fly across the keyboard? Mash keys as fast as you can and see your key presses per second. On a phone, tap the pad instead.",
    "counter": {
        "testid": "keypress", "input": "key", "key": "",
        "durations": [5, 10, 30, 60], "default": 10,
        "name": "Key Press Speed Test", "marquee": "Key Press Speed Test",
        "count_label": "Presses", "hint": "Mash any key as fast as you can — or tap here on a phone",
    },
    "content": """      <h2>How the key press speed test works</h2>
      <p>The key press speed test counts how many keys you can press in a set number of seconds. Unlike a <a href="/typing-speed-test/">typing test</a>, it does not care <em>which</em> keys you hit or whether they spell anything &mdash; it is pure finger speed. Pick a duration and mash the keyboard as fast as you can; the timer starts on your first press and your score is key presses per second. On a touchscreen, tap the pad instead.</p>

      <h2>What is a good key press speed?</h2>
      <p>Because you can use many fingers and alternate keys, key-press speed runs a little higher than single-button clicking:</p>
      <ul>
        <li><strong>Under 5 KPS</strong> &mdash; a relaxed, one-or-two-finger pace.</li>
        <li><strong>7 to 8 KPS</strong> &mdash; a quick, practised typist's mash.</li>
        <li><strong>9 to 11 KPS</strong> &mdash; fast; you are using several fingers well.</li>
        <li><strong>12+ KPS</strong> &mdash; excellent finger independence and speed.</li>
      </ul>

      <h2>How to press keys faster</h2>
      <ul>
        <li><strong>Use both hands</strong> and spread the work across many fingers.</li>
        <li><strong>Alternate keys</strong> so no single finger has to reset before the next press.</li>
        <li><strong>Keep your wrists relaxed</strong> and let your fingers do the moving.</li>
      </ul>
      <p>Want to test real typing instead of raw mashing? The <a href="/typing-speed-test/">typing speed test</a> measures words per minute with accuracy, and the <a href="/spacebar-clicker/">spacebar clicker</a> focuses on a single key.</p>""",
    "faq": [
        ("What does the key press speed test measure?",
         "It counts how many keys you press per second, regardless of which keys. It is raw finger speed, not typing skill."),
        ("What is a good key press speed?",
         "Around 7 to 8 presses per second is a quick pace. 9 to 11 is fast, and above 12 shows excellent finger speed."),
        ("How is this different from a typing test?",
         "A typing test measures words per minute and accuracy on real words. This test only counts key presses, so any keys count."),
        ("Does it work on a phone?",
         "Yes. On a touchscreen, tap the pad instead of pressing keys and it counts your taps the same way."),
    ],
    "related": [
        {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute with accuracy."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "Focus on a single key."},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The mouse-click version."},
        {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z as fast as you can."},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
