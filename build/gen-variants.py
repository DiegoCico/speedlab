#!/usr/bin/env python3
"""
SpeedLab duration-variant generator (standalone dev tool — NOT a build dep).

Stamps out per-duration variant pages (e.g. /cps-test/10-second/,
/typing-speed-test/1-minute/) from templates, so variants are never
hand-maintained. Reuses the shared page shell in gen.py via its render().

Usage:  python3 build/gen-variants.py            # all tests
        python3 build/gen-variants.py cps         # one test group
Groups: cps, typing, spacebar, tap.  See build/SEO-VARIANTS.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen  # reuse render(), esc(), DOMAIN
ROOT = gen.ROOT

def adj_of(sec):
    """Clean hyphenated adjective form, e.g. 15 -> '15-Second', 60 -> '1-Minute'."""
    if sec >= 60 and sec % 60 == 0:
        return "%d-Minute" % (sec // 60)
    return "%d-Second" % sec

def link_selector(parent_slug, items, active_slug):
    """items: list of (slug, short_label). Renders crawlable <a> duration links."""
    opts = []
    for slug, label in items:
        pressed = "true" if slug == active_slug else "false"
        opts.append('        <a class="opt" href="/%s/%s/" aria-pressed="%s">%s</a>'
                    % (parent_slug, slug, pressed, label))
    return "\n".join(opts)

# ===========================================================================
# CPS
# ===========================================================================
CPS = [1, 2, 5, 10, 15, 20, 30, 60, 100]
CPS_FLAVOUR = {
    1:  ("a pure one-second burst — no pacing, just explode",
         "The 1-second CPS test is all raw burst speed. There's no time to settle into a rhythm, so it rewards a single explosive flurry. Scores swing high — a good burst reads far above your steady rate."),
    2:  ("a two-second sprint that's still all burst",
         "The 2-second CPS test is long enough for a second flurry of clicks but short enough to still be mostly burst speed. It's a popular quick check between longer runs."),
    5:  ("the standard, and the fairest all-round test",
         "The 5-second CPS test is the most common length and the fairest all-round measure: long enough that luck evens out, short enough to sprint the whole way. If you run one, run this."),
    10: ("long enough that stamina starts to matter",
         "The 10-second CPS test is where stamina starts to show. You can't hold a peak burst for ten seconds, so your score settles closer to your true sustainable rate."),
    15: ("a real test of sustained clicking",
         "The 15-second CPS test rewards a steady, repeatable technique over a one-off burst. Watch your rate sag in the back half — closing strong is what separates good scores."),
    20: ("endurance clicking — pace yourself",
         "The 20-second CPS test is an endurance run. Going all-out early leaves your hand tired for the finish, so most people settle into a rhythm they can hold."),
    30: ("half a minute of pure endurance",
         "The 30-second CPS test is a genuine stamina challenge. Your average lands well below your burst speed, and staying relaxed is the only way to keep the rate up."),
    60: ("a full minute — the endurance benchmark",
         "The 60-second CPS test is the classic endurance benchmark. A full minute punishes tension and rewards a loose, sustainable technique. Pace it like a run, not a sprint."),
    100:("the famous 100-second marathon",
         "The 100-second CPS test is the marathon of click speed — a known challenge precisely because holding any real rate for over a minute and a half is brutal. Consistency beats raw speed."),
}

def cps_cabinet(active):
    items = [("%d-second" % d, "%ds" % d) for d in CPS]
    sel = link_selector("cps-test", items, "%d-second" % active)
    return """    <section class="cabinet" id="cps" data-duration="%d" aria-label="CPS test">
      <div class="marquee">%d Second Click Test</div>
      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout"><div class="seg-wrap"><span class="seg-value tnum" id="clicks">0</span></div><div class="readout-label">Clicks</div></div>
            <div class="readout small"><div class="seg-wrap"><span class="seg-value tnum" id="timer">%d</span></div><div class="readout-label">Seconds left</div></div>
          </div>
          <div class="play-area">
            <button class="click-pad is-armed" id="pad" type="button" aria-describedby="cps-help">
              <span data-pad-title>Click to start</span>
              <span class="hint" data-pad-hint>Click here as fast as you can for %ds</span>
            </button>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>
      <div style="text-align:center;margin-top:1rem"><button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button></div>
      <div class="seg-select" role="group" aria-label="Test duration" id="cps-help">
%s
      </div>
      <div class="pb-strip"><span>Personal best <span class="pb-val" data-pb>&mdash;</span></span><button data-clear type="button">Clear my scores</button></div>
    </section>""" % (active, active, active, active, sel)

def cps_specs():
    good = {1:"9+",2:"8+",5:"7-8",10:"7",15:"6.5",20:"6.5",30:"6",60:"6",100:"5.5"}
    out = []
    for d in CPS:
        tag, intro = CPS_FLAVOUR[d]
        sec = "Second" if d == 1 else "Seconds"
        others = " · ".join('<a href="/cps-test/%d-second/">%ds</a>' % (n, n) for n in CPS if n != d)
        out.append({
            "slug": "cps-test/%d-second" % d, "parent": {"name": "CPS Test", "slug": "cps-test"},
            "name": "CPS Test (%d %s)" % (d, sec), "crumb": "%d %s" % (d, sec), "skip_target": "pad",
            "cabinet": cps_cabinet(d), "scripts": ["/assets/js/tests/cps.js"],
            "title": "CPS Test — %d Second Click Speed Test" % d,
            "desc": "Take the %d second CPS test and measure your click speed in clicks per second. Free, instant, works on any device — beat your best and see your rank." % d,
            "ld_desc": "Measure your click speed over %d seconds in clicks per second." % d,
            "og_title": "%d Second CPS Test — Click Speed" % d, "og_desc": "Measure your click speed over %d seconds. Beat your best." % d,
            "og_image": "cps-test.png", "h1": "%d Second CPS Test" % d,
            "lead": "Click as fast as you can for %d %s — %s. The clock starts on your first click." % (d, sec.lower(), tag),
            "content": """      <h2>The %d second click speed test</h2>
      <p>%s Your score is total clicks divided by %d, and every %d-second run keeps its own personal best on this device.</p>

      <h2>What is a good score on the %d second test?</h2>
      <p>On this length, around <strong>%s CPS</strong> is a solid result for a normal click. Shorter tests let you post a higher number from a single burst; longer tests pull your average toward the rate you can truly sustain.</p>

      <h2>Try other lengths</h2>
      <p>Every CPS duration has its own page: %s. Prefer the standard? Use the main <a href="/cps-test/">CPS test</a>.</p>""" % (d, intro, d, d, d, good[d], others),
            "faq": [
                ("What is a good %d second CPS score?" % d, "About %s clicks per second is solid over %d seconds. Shorter tests read higher, longer tests lower." % (good[d], d)),
                ("How is the score calculated?", "Total clicks divided by %d seconds. Click 40 times in a %d-second test and that's %.1f CPS." % (d, d, 40.0/d)),
                ("Does each duration save its own best?", "Yes. Your personal best is stored separately for every CPS length on this device."),
                ("Which CPS length is standard?", "The 5-second test is the most common and fairest all-round measure of click speed."),
            ],
            "related": [
                {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The standard click speed test."},
                {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
                {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
                {"slug": "right-click-test", "kbd": "Mouse", "name": "Right Click Test", "desc": "How fast can you right click?"},
                {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
                {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
            ],
        })
    return out

# ===========================================================================
# Generic counter variants (Spacebar, Tap)
# ===========================================================================
def counter_cabinet(root_id, testid, input_, key, count_label, marquee, hint, active_sec, items, active_slug, parent_slug):
    key_attr = ' data-key="%s"' % key if input_ == "key" else ""
    sel = link_selector(parent_slug, items, active_slug)
    return """    <section class="cabinet" id="%s" data-testid="%s" data-input="%s"%s data-default="%d" data-name="%s" aria-label="%s">
      <div class="marquee">%s</div>
      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout"><div class="seg-wrap"><span class="seg-value tnum" id="clicks">0</span></div><div class="readout-label">%s</div></div>
            <div class="readout small"><div class="seg-wrap"><span class="seg-value tnum" id="timer">%d</span></div><div class="readout-label">Seconds left</div></div>
          </div>
          <div class="play-area">
            <button class="click-pad is-armed" id="pad" type="button" aria-describedby="c-help">
              <span data-pad-title>Start</span><span class="hint" data-pad-hint>%s</span>
            </button>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>
      <div style="text-align:center;margin-top:1rem"><button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button></div>
      <div class="seg-select" role="group" aria-label="Test duration" id="c-help">
%s
      </div>
      <div class="pb-strip"><span>Personal best <span class="pb-val" data-pb>&mdash;</span></span><button data-clear type="button">Clear my scores</button></div>
    </section>""" % (root_id, testid, input_, key_attr, active_sec, marquee, marquee, marquee, count_label, active_sec, hint, sel)

SPACEBAR = [(5,"5-second","5 Seconds","5s"),(10,"10-second","10 Seconds","10s"),
            (30,"30-second","30 Seconds","30s"),(60,"1-minute","1 Minute","1m"),
            (100,"100-second","100 Seconds","100s")]
SB_FLAVOUR = {5:"a quick burst of spacebar mashing",10:"the standard spacebar sprint",
              30:"half a minute of sustained tapping",60:"a full minute — the endurance benchmark",
              100:"the 100-second spacebar marathon"}

def spacebar_specs():
    items = [(s, lbl) for (sec, s, name, lbl) in SPACEBAR]
    out = []
    for sec, slug, name, lbl in SPACEBAR:
        tag = SB_FLAVOUR[sec]
        others = " · ".join('<a href="/spacebar-clicker/%s/">%s</a>' % (s, n) for (x, s, n, l) in SPACEBAR if s != slug)
        out.append({
            "slug": "spacebar-clicker/%s" % slug, "parent": {"name": "Spacebar Clicker", "slug": "spacebar-clicker"},
            "name": "Spacebar Clicker (%s)" % name, "crumb": name, "skip_target": "pad",
            "cabinet": counter_cabinet("clicker","spacebar","key"," ","Presses","Spacebar Speed Test",
                                       "Hit SPACEBAR as fast as you can — or tap here on a phone", sec, items, slug, "spacebar-clicker"),
            "scripts": ["/assets/js/tests/clicker.js"],
            "title": "Spacebar Clicker — %s Spacebar Test" % adj_of(sec),
            "desc": "How many times can you hit the spacebar in %s? Take the %s spacebar clicker, see your presses per second, and beat your best." % (name.lower(), name.lower()),
            "ld_desc": "Count how many times you can press the spacebar in %s." % name.lower(),
            "og_title": "%s Spacebar Clicker" % adj_of(sec), "og_desc": "How fast can you hit the spacebar in %s?" % name.lower(),
            "og_image": "spacebar-clicker.png", "h1": "%s Spacebar Clicker" % adj_of(sec),
            "lead": "Hit the spacebar as fast as you can for %s — %s. The clock starts on your first press." % (name.lower(), tag),
            "content": """      <h2>The %s spacebar test</h2>
      <p>%s. Your score is your presses per second over the full %s, and this length keeps its own personal best on this device. On a phone, tap the pad instead of pressing a key.</p>

      <h2>Try other lengths</h2>
      <p>Every spacebar length has its own page: %s. Or use the main <a href="/spacebar-clicker/">spacebar clicker</a>, which also has a no-timer mode.</p>

      <h2>How to press faster</h2>
      <ul>
        <li><strong>Alternate two fingers</strong> on the bar instead of one.</li>
        <li><strong>Match your effort to the clock</strong> — burst on short runs, pace the long ones.</li>
        <li><strong>Stay loose</strong>; a tense hand fades fast past 30 seconds.</li>
      </ul>""" % (name.lower(), tag.capitalize(), name.lower(), others),
            "faq": [
                ("What is a good spacebar speed?", "Around 6 to 7 presses per second is average. Above 8 is fast; shorter runs read higher than longer ones."),
                ("Does it work on a phone?", "Yes. Tap the pad instead of pressing a key and it counts your taps the same way."),
                ("Does each length save its own best?", "Yes. Your best is stored separately for every spacebar duration on this device."),
                ("Is there a no-timer mode?", "Yes, on the main spacebar clicker page you can count presses with no clock at all."),
            ],
            "related": [
                {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "The main spacebar test."},
                {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "How fast can you click?"},
                {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "Mash any keys."},
                {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
                {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute."},
                {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
            ],
        })
    return out

TAP = [(5,"5-second","5 Seconds","5s"),(10,"10-second","10 Seconds","10s")]
def tap_specs():
    items = [(s, lbl) for (sec, s, name, lbl) in TAP]
    out = []
    for sec, slug, name, lbl in TAP:
        tag = "a quick burst of tapping" if sec == 5 else "the standard tap sprint"
        others = " · ".join('<a href="/tap-speed-test/%s/">%s</a>' % (s, n) for (x, s, n, l) in TAP if s != slug)
        out.append({
            "slug": "tap-speed-test/%s" % slug, "parent": {"name": "Tap Speed Test", "slug": "tap-speed-test"},
            "name": "Tap Speed Test (%s)" % name, "crumb": name, "skip_target": "pad",
            "cabinet": counter_cabinet("clicker","tap","pointer",None,"Taps","Tap Speed Test",
                                       "Tap here as fast as you can", sec, items, slug, "tap-speed-test"),
            "scripts": ["/assets/js/tests/clicker.js"],
            "title": "Tap Speed Test — %s Tapping Test" % adj_of(sec),
            "desc": "How fast can you tap in %s? Take the %s tap speed test, see your taps per second, and beat your best on any phone or tablet." % (name.lower(), name.lower()),
            "ld_desc": "Measure how fast you can tap the screen in %s." % name.lower(),
            "og_title": "%s Tap Speed Test" % adj_of(sec), "og_desc": "How fast can you tap in %s?" % name.lower(),
            "og_image": "tap-speed-test.png", "h1": "%s Tap Speed Test" % adj_of(sec),
            "lead": "Tap the pad as fast as you can for %s — %s. The timer starts on your first tap." % (name.lower(), tag),
            "content": """      <h2>The %s tap test</h2>
      <p>%s. Your score is your taps per second over the full %s, and this length keeps its own personal best. It works with a finger on a touchscreen or a mouse on a computer.</p>

      <h2>Try other lengths</h2>
      <p>Other tap lengths: %s. Or use the main <a href="/tap-speed-test/">tap speed test</a>.</p>

      <h2>How to tap faster</h2>
      <ul>
        <li><strong>Use two fingers or thumbs</strong> alternating like a drum roll.</li>
        <li><strong>Rest your device</strong> on a surface so your hand is free to move.</li>
        <li><strong>Keep taps light and quick</strong> rather than hard.</li>
      </ul>""" % (name.lower(), tag.capitalize(), name.lower(), others),
            "faq": [
                ("What is a good tap speed?", "About 6 to 7 taps per second with one finger is average. Two fingers can push well past 10."),
                ("Does it work on a computer?", "Yes. Clicking the pad with a mouse works exactly like tapping."),
                ("Does each length save its own best?", "Yes. Your best is stored separately for every tap duration on this device."),
                ("Is tapping the same as CPS?", "It's measured the same way and lands in a similar range; tap speed is the touchscreen name for it."),
            ],
            "related": [
                {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "The main tap test."},
                {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The mouse version."},
                {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
                {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
                {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
                {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
            ],
        })
    return out

# ===========================================================================
# Typing
# ===========================================================================
TYPING = [(15,"15-second","15 Seconds","15s"),(30,"30-second","30 Seconds","30s"),
          (60,"1-minute","1 Minute","1m"),(180,"3-minute","3 Minutes","3m"),(300,"5-minute","5 Minutes","5m")]
TY_FLAVOUR = {
    15:"a fast burst where a hot streak reads high",
    30:"a short sprint — the popular quick check",
    60:"the classic one-minute benchmark most typing scores quote",
    180:"a three-minute run where consistency starts to matter",
    300:"a five-minute endurance test, closest to real typing",
}

def typing_cabinet(active_sec, active_slug):
    items = [(s, lbl) for (sec, s, name, lbl) in TYPING]
    sel = link_selector("typing-speed-test", items, active_slug)
    return """    <section class="cabinet" id="typing" data-duration="%d" aria-label="Typing speed test">
      <div class="marquee">Typing Speed Test</div>
      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout"><div class="seg-wrap"><span class="seg-value tnum" id="wpm">0</span></div><div class="readout-label">WPM</div></div>
            <div class="readout small"><div class="seg-wrap"><span class="seg-value tnum" id="acc">100</span></div><div class="readout-label">Accuracy %%</div></div>
            <div class="readout small"><div class="seg-wrap"><span class="seg-value tnum" id="timer">%d</span></div><div class="readout-label">Seconds left</div></div>
          </div>
          <div class="type-stage">
            <div class="type-passage blurred" id="passage" tabindex="-1" aria-label="Type this text"><div class="type-lines" id="lines"></div></div>
            <input class="type-input" id="typeInput" type="text" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Type here">
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>
      <div style="text-align:center;margin-top:1rem"><button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button></div>
      <div class="seg-select" role="group" aria-label="Test duration">
%s
      </div>
      <div class="pb-strip"><span>Personal best <span class="pb-val" data-pb>&mdash;</span></span><button data-clear type="button">Clear my scores</button></div>
    </section>""" % (active_sec, active_sec, sel)

def typing_specs():
    out = []
    for sec, slug, name, lbl in TYPING:
        tag = TY_FLAVOUR[sec]
        others = " · ".join('<a href="/typing-speed-test/%s/">%s</a>' % (s, n) for (x, s, n, l) in TYPING if s != slug)
        out.append({
            "slug": "typing-speed-test/%s" % slug, "parent": {"name": "Typing Speed Test", "slug": "typing-speed-test"},
            "name": "Typing Speed Test (%s)" % name, "crumb": name, "skip_target": "passage",
            "cabinet": typing_cabinet(sec, slug), "scripts": ["/assets/js/tests/typing.js"],
            "title": "%s Typing Test — Words Per Minute" % adj_of(sec),
            "desc": "Take the %s typing test and measure your speed in words per minute with live accuracy. Free, instant — beat your best and see how you rank." % name.lower(),
            "ld_desc": "Measure your typing speed in words per minute over %s." % name.lower(),
            "og_title": "%s Typing Test — WPM" % adj_of(sec), "og_desc": "Measure your typing speed in WPM over %s." % name.lower(),
            "og_image": "typing-speed-test.png", "h1": "%s Typing Test" % adj_of(sec),
            "lead": "Type the words as they appear for %s — %s. WPM and accuracy update live; the timer starts on your first letter." % (name.lower(), tag),
            "content": """      <h2>The %s typing test</h2>
      <p>This is %s. Type the passage as fast and accurately as you can; every five correct characters counts as one word, divided by the time. Longer tests reward steady accuracy over a hot streak, and this length keeps its own personal best on this device.</p>

      <h2>What is a good score?</h2>
      <p>The average typist manages around 40 WPM, comfortable touch typists 60 to 80, and pros push past 100. Shorter tests like 15 or 30 seconds read a little higher because you can ride a good streak; minute-plus tests settle closer to your real sustained speed.</p>

      <h2>Try other lengths</h2>
      <p>Every typing length has its own page: %s. Or use the main <a href="/typing-speed-test/">typing speed test</a>.</p>""" % (name.lower(), tag, others),
            "faq": [
                ("What is a good %s typing speed?" % name.lower(), "About 40 WPM is average, 60 to 80 is a comfortable touch typist, and over 100 is professional. Shorter tests read a little higher."),
                ("How is WPM calculated?", "Every five correct characters counts as one word, divided by the time. Mistakes lower your score, so accuracy matters."),
                ("Does each length save its own best?", "Yes. Your best is stored separately for every typing duration on this device."),
                ("Does it work on a phone?", "Yes. Tap the passage to bring up your keyboard and start typing."),
            ],
            "related": [
                {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "The main typing test."},
                {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z fast."},
                {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race 1 to 100."},
                {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Speed Test", "desc": "Raw finger speed."},
                {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
                {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
            ],
        })
    return out

# ===========================================================================
GROUPS = {"cps": cps_specs, "typing": typing_specs, "spacebar": spacebar_specs, "tap": tap_specs}

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    groups = [only] if only else list(GROUPS.keys())
    total = 0
    for g in groups:
        for spec in GROUPS[g]():
            outdir = os.path.join(ROOT, spec["slug"])
            os.makedirs(outdir, exist_ok=True)
            with open(os.path.join(outdir, "index.html"), "w") as f:
                f.write(gen.render(spec))
            print("wrote", spec["slug"] + "/index.html")
            total += 1
    print("done (%d variant pages)" % total)

if __name__ == "__main__":
    main()
