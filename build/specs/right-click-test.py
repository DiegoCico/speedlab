SPEC = {
    "slug": "right-click-test",
    "kind": "counter",
    "name": "Right Click Test",
    "crumb": "Right Click Test",
    "title": "Right Click Test — How Fast Can You Right Click | SpeedLab",
    "desc": "Test how fast you can right click your mouse. Right click the pad as many times as you can and see your right clicks per second, rank, and percentile.",
    "ld_desc": "Measure how fast you can right click in clicks per second.",
    "og_title": "Right Click Test — Right Click Speed",
    "og_desc": "How fast can you right click? Measure your right clicks per second.",
    "og_image": "right-click-test.png",
    "h1": "Right Click Test",
    "lead": "How fast can you right click? Right click the pad as fast as you can and we count every one. The timer starts on your first right click.",
    "counter": {
        "testid": "rightclick", "input": "pointer", "button": "right",
        "durations": [5, 10, 15, 30, 60], "default": 5,
        "name": "Right Click Test", "marquee": "Right Click Speed",
        "count_label": "Right clicks", "hint": "Right click here as fast as you can",
    },
    "content": """      <h2>How the right click test works</h2>
      <p>The right click test counts how many times you can press the <strong>right</strong> mouse button in a set number of seconds. Only right clicks count &mdash; left clicks are ignored, and the usual right-click menu is turned off inside the pad so nothing gets in your way. Pick a duration, right click the pad as fast as you can, and your score shows up in clicks per second. The timer starts on your first right click and stops on its own.</p>

      <h2>What is a good right click speed?</h2>
      <p>Right clicking is usually a little slower than left clicking, because the finger most people use for it is less practised. A typical right-click speed is around <strong>4 to 6 CPS</strong>:</p>
      <ul>
        <li><strong>Under 2.5 CPS</strong> &mdash; a relaxed, everyday right click.</li>
        <li><strong>4 to 5.5 CPS</strong> &mdash; right around average.</li>
        <li><strong>7 to 9 CPS</strong> &mdash; fast; your right finger is well trained.</li>
        <li><strong>10+ CPS</strong> &mdash; excellent right-click speed.</li>
      </ul>

      <h2>Why test right click speed?</h2>
      <p>Some games map important actions to the right mouse button &mdash; blocking, aiming, or placing blocks &mdash; so right-click speed can matter as much as left. This test is also a quick way to check that your right mouse button is registering every press cleanly. If clicks feel like they are being missed, the button switch may be wearing out.</p>
      <p>For the standard left-click version, try the <a href="/cps-test/">CPS test</a>, or measure your keyboard with the <a href="/spacebar-clicker/">spacebar clicker</a>.</p>""",
    "faq": [
        ("What is a good right click speed?",
         "Around 4 to 6 right clicks per second is average. Above 7 is fast, and 10 or more is excellent."),
        ("Why is right clicking slower than left clicking?",
         "Most people use a less practised finger for the right button, so it usually clicks a little slower than the left."),
        ("Do left clicks count in this test?",
         "No. Only right clicks are counted, and the right-click menu is disabled inside the pad so it will not interrupt you."),
        ("Can I use this to check a faulty mouse?",
         "Yes. If right clicks feel like they are being missed during the test, the right button switch may be wearing out."),
    ],
    "related": [
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The left-click speed test."},
        {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
        {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "How fast can you mash keys?"},
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
