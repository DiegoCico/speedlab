#!/usr/bin/env python3
"""
SpeedLab duration-variant generator (standalone dev tool — NOT a build dep).

Stamps out per-duration variant pages (e.g. /cps-test/10-second/) from a single
template, so the 9 CPS variants are never hand-maintained. Reuses the shared
page shell in gen.py (header, footer, ad slots, JSON-LD) via its render().

Usage:  python3 build/gen-variants.py         # generate all configured variants
See build/SEO-VARIANTS.md for the strategy and rollout order.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen  # reuse render(), esc(), DOMAIN

ROOT = gen.ROOT

# --------------------------------------------------------------------------- #
# CPS variants. Hub /cps-test/ stays the general page; these are the timed ones.
CPS_DURATIONS = [1, 2, 5, 10, 15, 20, 30, 60, 100]

def cps_cabinet(active):
    # duration selector rendered as crawlable links to every variant + the hub
    opts = []
    for d in CPS_DURATIONS:
        href = "/cps-test/%d-second/" % d
        pressed = "true" if d == active else "false"
        opts.append('        <a class="opt" href="%s" aria-pressed="%s">%ds</a>' % (href, pressed, d))
    opts_html = "\n".join(opts)
    return """    <section class="cabinet" id="cps" data-duration="%d" aria-label="CPS test">
      <div class="marquee">%d Second Click Test</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="clicks">0</span></div>
              <div class="readout-label">Clicks</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">%d</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
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

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button>
      </div>

      <div class="seg-select" role="group" aria-label="Test duration" id="cps-help">
%s
      </div>

      <div class="pb-strip">
        <span>Personal best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>""" % (active, active, active, active, opts_html)

# per-duration flavour so pages are not thin duplicates
CPS_FLAVOUR = {
    1:   ("a pure one-second burst — no pacing, just explode",
          "The 1-second CPS test is all raw burst speed. There's no time to settle into a rhythm, so it rewards a single explosive flurry of clicks. Because it's so short, scores swing high — a good burst can read far above your steady rate."),
    2:   ("a two-second sprint that's still all burst",
          "The 2-second CPS test is long enough to get a second wind of clicks but short enough that it's still mostly burst speed. It's a popular quick check between longer runs."),
    5:   ("the standard, and the fairest all-round test",
          "The 5-second CPS test is the most common length and the fairest all-round measure: long enough that luck evens out, short enough to sprint the whole way. If you only run one, run this one."),
    10:  ("long enough that stamina starts to matter",
          "The 10-second CPS test is where stamina starts to show. You can't hold a peak burst for ten seconds, so your score settles closer to your true sustainable click rate."),
    15:  ("a real test of sustained clicking",
          "The 15-second CPS test rewards a steady, repeatable technique over a one-off burst. Watch your rate sag in the back half — closing strong is what separates good scores here."),
    20:  ("endurance clicking — pace yourself",
          "The 20-second CPS test is an endurance run. Going all-out early will leave your hand tired for the finish, so most people settle into a rhythm they can actually hold."),
    30:  ("half a minute of pure endurance",
          "The 30-second CPS test is a genuine stamina challenge. Your average will land well below your burst speed, and staying relaxed is the only way to keep the rate up for the whole run."),
    60:  ("a full minute — the endurance benchmark",
          "The 60-second CPS test is the classic endurance benchmark. A full minute of clicking punishes tension and rewards a loose, sustainable technique. Pace it like a run, not a sprint."),
    100: ("the famous 100-second marathon",
          "The 100-second CPS test is the marathon of click speed — a well-known challenge precisely because holding any real rate for over a minute and a half is brutal. Survival and consistency beat raw speed."),
}

def cps_variant_spec(d):
    tagline, intro = CPS_FLAVOUR[d]
    good = {1:"9+", 2:"8+", 5:"7-8", 10:"7", 15:"6.5", 20:"6.5", 30:"6", 60:"6", 100:"5.5"}[d]
    sec = "Second" if d == 1 else "Seconds"
    other_links = " · ".join(
        '<a href="/cps-test/%d-second/">%ds</a>' % (n, n) for n in CPS_DURATIONS if n != d)
    return {
        "slug": "cps-test/%d-second" % d,
        "parent": {"name": "CPS Test", "slug": "cps-test"},
        "name": "CPS Test (%d %s)" % (d, sec),
        "crumb": "%d %s" % (d, sec),
        "skip_target": "pad",
        "cabinet": cps_cabinet(d),
        "scripts": ["/assets/js/tests/cps.js"],
        "title": "CPS Test — %d Second Click Speed Test" % d,
        "desc": ("Take the %d second CPS test and measure your click speed in clicks per second. "
                 "Free, instant, works on any device — beat your best and see your rank." % d),
        "ld_desc": "Measure your click speed over %d seconds in clicks per second." % d,
        "og_title": "%d Second CPS Test — Click Speed" % d,
        "og_desc": "Measure your click speed over %d seconds. Beat your best." % d,
        "og_image": "cps-test.png",
        "h1": "%d Second CPS Test" % d,
        "lead": "Click as fast as you can for %d %s — %s. The clock starts on your first click." % (d, sec.lower(), tagline),
        "content": """      <h2>The %d second click speed test</h2>
      <p>%s Your score is your total clicks divided by %d, and every %d-second run keeps its own personal best on this device.</p>

      <h2>What is a good score on the %d second test?</h2>
      <p>On this length, around <strong>%s CPS</strong> is a solid result for a normal click. Shorter tests let you post a higher number from a single burst; longer tests pull your average down toward the rate you can truly sustain. Compare your result across lengths to see where your clicking falls off.</p>

      <h2>Try other lengths</h2>
      <p>Every CPS duration has its own page: %s. Prefer the standard? Use the main <a href="/cps-test/">CPS test</a>.</p>

      <h2>How to click faster</h2>
      <ul>
        <li><strong>Match your effort to the clock.</strong> Burst on the short tests; pace yourself on the long ones.</li>
        <li><strong>Stay loose.</strong> A tense hand slows down fast, especially past ten seconds.</li>
        <li><strong>Rest your hand on the mouse</strong> and let your finger do the work.</li>
      </ul>""" % (d, intro, d, d, d, good, other_links),
        "faq": [
            ("What is a good %d second CPS score?" % d,
             "About %s clicks per second is a solid score over %d seconds. Shorter tests read higher, longer tests lower." % (good, d)),
            ("How is the score calculated?",
             "It's your total clicks divided by %d seconds. Click 40 times in a %d-second test and that's %.1f CPS." % (d, d, 40.0/d)),
            ("Does each duration save its own best?",
             "Yes. Your personal best is stored separately for every CPS length on this device."),
            ("Which CPS test length is standard?",
             "The 5-second test is the most common and the fairest all-round measure of click speed."),
        ],
        "related": [
            {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "The standard click speed test."},
            {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
            {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "How fast can you tap?"},
            {"slug": "right-click-test", "kbd": "Mouse", "name": "Right Click Test", "desc": "How fast can you right click?"},
            {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
            {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed and reflex test."},
        ],
    }

def main():
    specs = [cps_variant_spec(d) for d in CPS_DURATIONS]
    for spec in specs:
        outdir = os.path.join(ROOT, spec["slug"])
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w") as f:
            f.write(gen.render(spec))
        print("wrote", spec["slug"] + "/index.html")
    print("done (%d variant pages)" % len(specs))

if __name__ == "__main__":
    main()
