CABINET = """    <section class="cabinet" id="audioreaction" aria-label="Audio reaction test">
      <div class="marquee">Audio Reaction</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <button class="react-stage" id="stage" type="button">
            <span class="react-big" id="stageTitle">Tap to start</span>
            <span class="react-sub" id="stageSub">Listen for the beep, then tap. 5 tries.</span>
          </button>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div class="react-slots" id="slots" aria-label="Your attempts"></div>

      <div class="pb-strip">
        <span>Best average <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

SPEC = {
    "slug": "audio-reaction-test",
    "name": "Audio Reaction Test",
    "crumb": "Audio Reaction Test",
    "skip_target": "stage",
    "cabinet": CABINET,
    "scripts": ["/assets/js/tests/audio-reaction.js"],
    "title": "Audio Reaction Test — React to a Beep | SpeedLab",
    "desc": "Test your reaction time to sound. Wait for the beep, then tap as fast as you can. Five tries, averaged in milliseconds, with your rank and percentile.",
    "ld_desc": "Measure how fast you react to a sound over five tries.",
    "og_title": "Audio Reaction Test — React to a Beep",
    "og_desc": "Wait for the beep, then tap as fast as you can. Measure your audio reaction time.",
    "og_image": "audio-reaction-test.png",
    "h1": "Audio Reaction Test",
    "lead": "React to sound instead of sight. Wait for the beep, then tap as fast as you can. Five tries, averaged in milliseconds. You will need sound turned on.",
    "content": """      <h2>How the audio reaction test works</h2>
      <p>When you start, wait quietly &mdash; after a random delay you will hear a <strong>beep</strong>, and a timer starts the instant it plays. Tap, click, or press space as fast as you can once you hear it. The delay changes every time so you cannot guess it, and tapping before the beep counts as &ldquo;too soon&rdquo; and lets you retry. After five clean tries we average them into your score. Because it is an audio test, you will be asked to turn sound on first.</p>

      <h2>What is a good audio reaction time?</h2>
      <p>People generally react to sound a little <em>faster</em> than to what they see, because sound reaches the brain more quickly. Typical results:</p>
      <ul>
        <li><strong>Over 320 ms</strong> &mdash; tired, distracted, or just warming up.</li>
        <li><strong>220 to 260 ms</strong> &mdash; right around average for sound.</li>
        <li><strong>185 to 220 ms</strong> &mdash; sharp and focused.</li>
        <li><strong>Under 185 ms</strong> &mdash; excellent audio reflexes.</li>
      </ul>

      <h2>Audio vs visual reaction</h2>
      <p>Compare your score here with the <a href="/reaction-time-test/">visual reaction time test</a> &mdash; most people are 20 to 40 milliseconds quicker reacting to a beep than to a colour change. Reacting to sound matters in music, sprint starts, and any situation where a signal is a noise rather than a sight. To improve, stay relaxed and alert, and react to the beep rather than trying to anticipate it.</p>""",
    "faq": [
        ("Why do I need sound on?",
         "The signal in this test is a beep, so it only works with sound turned on. Tap the screen once to enable sound and begin."),
        ("What is a good audio reaction time?",
         "Around 220 to 260 ms is average for sound. Under 220 ms is fast, and under 185 ms is excellent."),
        ("Is reacting to sound faster than sight?",
         "For most people, yes. Sound reaches the brain slightly faster, so audio reaction times are usually a bit quicker than visual ones."),
        ("Why did it say too soon?",
         "You tapped before the beep played. That try does not count &mdash; just tap again to retry it."),
    ],
    "related": [
        {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "React to a colour instead of a beep."},
        {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets, measure ms each."},
        {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles for 30 seconds."},
        {"slug": "color-match", "kbd": "Reaction", "name": "Color Match", "desc": "Does the word match the ink colour?"},
        {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
        {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
    ],
}
