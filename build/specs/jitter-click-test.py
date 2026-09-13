SPEC = {
    "slug": "jitter-click-test",
    "kind": "counter",
    "name": "Jitter Click Test",
    "crumb": "Jitter Click Test",
    "title": "Jitter Click Test — Measure Jitter Clicking CPS | SpeedLab",
    "desc": "Test your jitter clicking speed in CPS. Learn what jitter clicking is, how it works, and measure how fast your rapid-fire clicks really are.",
    "ld_desc": "Measure your jitter clicking speed in clicks per second.",
    "og_title": "Jitter Click Test — Jitter Clicking CPS",
    "og_desc": "Learn what jitter clicking is and measure how fast your rapid-fire clicks really are.",
    "og_image": "jitter-click-test.png",
    "h1": "Jitter Click Test",
    "lead": "Jitter click as fast as you can and see your clicks per second. If you have never heard of jitter clicking, there is a quick explainer below the test.",
    "counter": {
        "testid": "jitter", "input": "pointer",
        "durations": [5, 10, 15, 30, 60], "default": 10,
        "name": "Jitter Click Test", "marquee": "Jitter Click Test",
        "count_label": "Clicks", "hint": "Jitter click here as fast as you can",
    },
    "content": """      <h2>What is jitter clicking?</h2>
      <p>Jitter clicking is a technique for clicking a mouse much faster than a normal press. Instead of moving just your finger, you tense the muscles in your forearm and wrist so your hand vibrates &mdash; that shaking motion &ldquo;jitters&rdquo; the mouse button up and down very quickly. Done well, it can roughly double a normal click rate, which is why it became popular in Minecraft PvP and other games where click speed matters.</p>
      <p>It takes practice, and it should never hurt. If you feel strain in your arm or wrist, stop &mdash; no score is worth an injury.</p>

      <h2>What is a good jitter click speed?</h2>
      <p>A normal click tops out around 7 CPS for most people. Jitter clicking pushes that higher:</p>
      <ul>
        <li><strong>Under 8 CPS</strong> &mdash; you are still clicking fairly normally.</li>
        <li><strong>10 to 12 CPS</strong> &mdash; solid jitter clicking.</li>
        <li><strong>13 to 16 CPS</strong> &mdash; fast and well-practised.</li>
        <li><strong>16+ CPS</strong> &mdash; excellent control of the technique.</li>
      </ul>

      <h2>How to jitter click</h2>
      <ol>
        <li>Rest your hand lightly on the mouse &mdash; grip it, don't strangle it.</li>
        <li>Tense your forearm so your hand starts to shake, and guide that shake onto the mouse button.</li>
        <li>Keep bursts short. Jitter clicking is hard to hold for long, so shorter tests usually give a higher CPS.</li>
      </ol>
      <p>Prefer a gentler method? <a href="/butterfly-click-test/">Butterfly clicking</a> alternates two fingers and is easier on your hand, while the plain <a href="/cps-test/">CPS test</a> measures a normal click. Many games and servers restrict clicking techniques, so check the rules where you play.</p>""",
    "faq": [
        ("What is jitter clicking?",
         "Jitter clicking is tensing your arm so your hand vibrates, which presses the mouse button very rapidly and clicks far faster than a normal press."),
        ("Is jitter clicking bad for you?",
         "It can strain your hand and wrist if you overdo it. Keep bursts short, stay relaxed, and stop immediately if anything aches."),
        ("What is a good jitter click CPS?",
         "Around 10 to 12 CPS is solid jitter clicking. 13 to 16 is fast, and above 16 shows excellent control of the technique."),
        ("Can jitter clicking get me banned in games?",
         "Some servers ban certain clicking techniques or cap CPS. This test is only for practice; always follow the rules of the game you play."),
    ],
    "related": [
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "Measure a normal click."},
        {"slug": "butterfly-click-test", "kbd": "Mouse", "name": "Butterfly Click Test", "desc": "Two fingers alternating."},
        {"slug": "drag-click-test", "kbd": "Mouse", "name": "Drag Click Test", "desc": "Rapid clicks from one drag."},
        {"slug": "kohi-click-test", "kbd": "Mouse", "name": "Kohi Click Test", "desc": "Click speed for Minecraft."},
        {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "Spacebar speed test."},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
