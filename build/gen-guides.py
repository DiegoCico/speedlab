#!/usr/bin/env python3
"""
SpeedLab guides generator (standalone dev tool — NOT part of the served site).

Builds the editorial /guides/ section: a hub page plus in-depth articles that
explain the metrics behind the tests (CPS, reaction time, WPM, memory). These
are original long-form pages — they give the site substantial unique value
beyond the interactive tools, and cross-link to the relevant tests.

Usage:  python3 build/gen-guides.py     # regenerate the hub + every guide
Run from the repo root.
"""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://speedlab.lol"
VER = "202609152020"   # bumped by build/stamp.py after generation
PUBLISHED = "2026-09-23"
MODIFIED = "2026-09-23"

def esc(s): return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, separators=(",", ":")) + '\n</script>'

# --------------------------------------------------------------------------- #
HEAD_CHROME = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#1A1030">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2418545459143038" crossorigin="anonymous"></script>

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="SpeedLab">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{domain}/assets/img/og/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{domain}/assets/img/og/{og_image}">

<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/base.css?v={ver}">
<link rel="stylesheet" href="/assets/css/arcade.css?v={ver}">

{ld}
</head>
<body>
<script>try{{if(!sessionStorage.getItem('sl_intro')&&!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)){{document.documentElement.classList.add('intro-on');}}}}catch(e){{}}</script>
<div id="intro" aria-hidden="true"><div id="introMark"><span class="brand">speedlab<span class="lab">.lol</span></span></div></div>
<a class="skip-link" href="#main">Skip to content</a>

<!-- Consent Management Platform (CMP) mount point.
     A Google-certified CMP is required for EEA, UK and Switzerland traffic once
     AdSense is enabled. Uncomment and insert the certified CMP snippet here.
<div id="cmp-consent" aria-live="polite"></div>
-->

<header class="site-header">
  <div class="bar">
    <a class="brand" href="/">speedlab<span class="lab">.lol</span></a>
    <nav aria-label="Primary">
      <a href="/all-tests/">All Tests</a>
      <a href="/guides/">Guides</a>
      <button class="sound-toggle" id="soundToggle" type="button" aria-pressed="false">
        <span aria-hidden="true">&#128266;</span><span data-sound-label>Sound: Off</span>
      </button>
    </nav>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <h3>SpeedLab</h3>
        <p style="max-width:34ch;color:var(--c-ink-dim)">Short, sharp speed and reflex tests. Your scores are saved on your device &mdash; nowhere else.</p>
      </div>
      <div>
        <h3>Explore</h3>
        <nav aria-label="Footer">
          <a href="/all-tests/">All Tests</a>
          <a href="/guides/">Guides</a>
          <a href="/updates/">What's New</a>
          <a href="/cps-test/">CPS Test</a>
          <a href="/reaction-time-test/">Reaction Time</a>
        </nav>
      </div>
      <div>
        <h3>Site</h3>
        <nav aria-label="Legal">
          <a href="/about/">About</a>
          <a href="/privacy/">Privacy</a>
          <a href="/terms/">Terms</a>
          <a href="/disclaimer/">Disclaimer</a>
          <a href="/contact/">Contact</a>
        </nav>
      </div>
    </div>
    <p class="fine">&copy; 2026 SpeedLab &middot; No accounts, no tracking, no cookies. Scores stay in your browser.</p>
  </div>
</footer>

<script src="/assets/js/intro.js?v={ver}" defer></script>
<script src="/assets/js/engine.js?v={ver}" defer></script>
</body>
</html>
"""

def tiles(items):
    out = []
    for r in items:
        out.append(
            f'        <a class="tile" href="/{r["slug"]}/"><span class="t-kbd">{esc(r["kbd"])}</span>'
            f'<span class="t-name">{esc(r["name"])}</span><span class="t-desc">{esc(r["desc"])}</span></a>')
    return "\n".join(out)

def faq_html(faq):
    rows = "\n".join(
        f'        <details>\n          <summary>{esc(q)}</summary>\n'
        f'          <p>{esc(a)}</p>\n        </details>' for q, a in faq)
    return f'      <div class="faq">\n{rows}\n      </div>'

def faq_ld(faq):
    ents = [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]
    return jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents})

def breadcrumb_ld(trail):
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p}
             for i, (n, p) in enumerate(trail)]
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

def crumbs_html(trail, current):
    lis = [f'<li><a href="{p}">{esc(n)}</a></li>' for n, p in trail]
    lis.append(f'<li aria-current="page">{esc(current)}</li>')
    return "\n        ".join(lis)

# --------------------------------------------------------------------------- #
OG_MAP = {
    "what-is-a-good-cps": "guide-cps.png",
    "how-to-improve-reaction-time": "guide-reaction.png",
    "average-typing-speed": "guide-typing.png",
    "do-brain-training-games-work": "guide-brain.png",
    "what-is-a-good-reaction-time": "guide-rt-good.png",
    "how-to-click-faster": "guide-click-faster.png",
    "how-to-type-faster": "guide-type-faster.png",
    "reaction-time-in-gaming": "guide-gaming-rt.png",
    "how-to-improve-hand-eye-coordination": "guide-hand-eye.png",
    "can-you-train-your-reflexes": "guide-reflexes.png",
    "how-to-improve-working-memory": "guide-memory.png",
    "gaming-warm-up-routine": "guide-warmup.png",
    "what-is-a-good-tapping-speed": "guide-tapping.png",
}

def render_guide(g):
    trail = [("Home", "/"), ("Guides", "/guides/")]
    og_image = OG_MAP.get(g["slug"], "default.png")
    article_ld = jsonld({
        "@context": "https://schema.org", "@type": "Article",
        "headline": g["h1"], "description": g["ld_desc"],
        "datePublished": PUBLISHED, "dateModified": MODIFIED,
        "author": {"@type": "Organization", "name": "SpeedLab"},
        "publisher": {"@type": "Organization", "name": "SpeedLab"},
        "mainEntityOfPage": f'{DOMAIN}/guides/{g["slug"]}/',
        "image": f"{DOMAIN}/assets/img/og/{og_image}",
    })
    ld = article_ld + "\n" + breadcrumb_ld(trail + [(g["crumb"], f'/guides/{g["slug"]}/')])
    if g.get("faq"):
        ld += "\n" + faq_ld(g["faq"])

    head = HEAD_CHROME.format(
        title=esc(g["title"]), desc=esc(g["desc"]), canonical=f'{DOMAIN}/guides/{g["slug"]}/',
        og_type="article", og_title=esc(g["og_title"]), og_desc=esc(g["og_desc"]),
        og_image=OG_MAP.get(g["slug"], "default.png"),
        domain=DOMAIN, ver=VER, ld=ld)

    faq_block = ""
    if g.get("faq"):
        faq_block = "\n      <h2>Frequently asked questions</h2>\n" + faq_html(g["faq"]) + "\n"

    body = f"""
<main class="wrap layout" id="main">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb">
      <ol>
        {crumbs_html(trail, g["crumb"])}
      </ol>
    </nav>

    <article>
    <h1>{esc(g["h1"])}</h1>
    <p class="lead">{esc(g["lead"])}</p>
    <p class="byline" style="color:var(--c-ink-dim);font-size:.9rem;margin-top:-.4rem">By SpeedLab &middot; Updated {MODIFIED}</p>

    <div class="ad-slot" data-slot="content-top" aria-hidden="true"><!-- AdSense: paste unit here --></div>

    <div class="content">
{g["body"]}
{faq_block}    </div>
    </article>

    <div class="ad-slot" data-slot="content-bottom" aria-hidden="true"><!-- AdSense: paste unit here --></div>

    <section class="related" aria-label="Try these tests">
      <h2>Try these tests</h2>
      <div class="tile-grid">
{tiles(g["related_tests"])}
      </div>
    </section>

    <section class="related" aria-label="More guides">
      <h2>More guides</h2>
      <div class="tile-grid">
{tiles(g["related_guides"])}
      </div>
    </section>

    <div class="ad-slot" data-slot="footer" aria-hidden="true"><!-- AdSense: paste unit here --></div>
  </div>

  <aside class="sidebar-rail" aria-label="Advertisement">
    <div class="ad-slot" data-slot="sidebar" aria-hidden="true"><!-- AdSense: paste unit here --></div>
  </aside>
</main>

"""
    return head + body + FOOTER.format(ver=VER)


def render_hub(guides):
    trail = [("Home", "/")]
    ld = breadcrumb_ld([("Home", "/"), ("Guides", "/guides/")]) + "\n" + jsonld({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "SpeedLab Guides", "url": f"{DOMAIN}/guides/",
        "description": "Guides explaining the metrics behind SpeedLab's speed and reflex tests.",
    })
    head = HEAD_CHROME.format(
        title="Guides — Click Speed, Reaction Time & Typing Explained | SpeedLab",
        desc="Plain-English guides to the metrics behind our tests: what a good CPS is, how to improve your reaction time, average typing speed, and whether brain games work.",
        canonical=f"{DOMAIN}/guides/", og_type="website",
        og_title="SpeedLab Guides", og_desc="Guides to click speed, reaction time, typing speed and memory.",
        og_image="guides.png", domain=DOMAIN, ver=VER, ld=ld)

    cards = []
    for g in guides:
        cards.append(
            f'      <a class="tile" href="/guides/{g["slug"]}/">'
            f'<span class="t-kbd">Guide</span>'
            f'<span class="t-name">{esc(g["card_title"])}</span>'
            f'<span class="t-desc">{esc(g["card_desc"])}</span></a>')
    cards_html = "\n".join(cards)

    body = f"""
<main class="wrap" id="main">
  <nav class="crumbs" aria-label="Breadcrumb">
    <ol><li><a href="/">Home</a></li><li aria-current="page">Guides</li></ol>
  </nav>

  <h1>SpeedLab guides</h1>
  <p class="lead">Short, honest explainers on the numbers behind the tests &mdash; what counts as a good score, how each metric is measured, and practical ways to get faster. No fluff, no sign-up.</p>

  <div class="ad-slot" data-slot="content-top" aria-hidden="true"><!-- AdSense: paste unit here --></div>

  <div class="tile-grid">
{cards_html}
  </div>

  <div class="content">
    <h2>Why these guides exist</h2>
    <p>Every test on SpeedLab spits out a number, but a number only means something once you know the range it sits in. These guides give you that context: the average click speed, what a typical reaction time actually is, how words-per-minute is calculated, and what the memory tests are really measuring. Each one links back to the test it describes so you can try it the moment you're curious.</p>
    <p>New guides get added as the site grows. Browse <a href="/all-tests/">all tests</a> if you'd rather just start playing.</p>
  </div>

  <div class="ad-slot" data-slot="footer" aria-hidden="true"><!-- AdSense: paste unit here --></div>
</main>

"""
    return head + body + FOOTER.format(ver=VER)


# =========================================================================== #
# Guides
# =========================================================================== #
TESTS = {
    "cps": {"slug": "cps-test", "kbd": "Mouse", "name": "CPS Test", "desc": "Clicks per second — the classic."},
    "spacebar": {"slug": "spacebar-clicker", "kbd": "Keyboard", "name": "Spacebar Clicker", "desc": "How fast can you hit space?"},
    "tap": {"slug": "tap-speed-test", "kbd": "Mobile", "name": "Tap Speed Test", "desc": "The phone version of CPS."},
    "reaction": {"slug": "reaction-time-test", "kbd": "Reaction", "name": "Reaction Time Test", "desc": "Green means go."},
    "audio": {"slug": "audio-reaction-test", "kbd": "Reaction", "name": "Audio Reaction Test", "desc": "React to the beep."},
    "aim": {"slug": "aim-trainer", "kbd": "Reaction", "name": "Aim Trainer", "desc": "Hit 30 targets fast."},
    "gonogo": {"slug": "go-no-go", "kbd": "Reaction", "name": "Go / No-Go", "desc": "Tap green, hold on red."},
    "typing": {"slug": "typing-speed-test", "kbd": "Keyboard", "name": "Typing Speed Test", "desc": "Words per minute."},
    "keypress": {"slug": "key-press-test", "kbd": "Keyboard", "name": "Key Press Test", "desc": "Raw finger speed."},
    "numbermem": {"slug": "number-memory", "kbd": "Memory", "name": "Number Memory", "desc": "Remember the number."},
    "seqmem": {"slug": "sequence-memory", "kbd": "Memory", "name": "Sequence Memory", "desc": "Repeat the pattern."},
    "vismem": {"slug": "visual-memory", "kbd": "Memory", "name": "Visual Memory", "desc": "Remember the tiles."},
    "chimp": {"slug": "chimp-test", "kbd": "Memory", "name": "Chimp Test", "desc": "Numbers in order."},
    "match": {"slug": "memory-match", "kbd": "Memory", "name": "Memory Match", "desc": "Find the pairs."},
}

def g_ref(key, over=None):
    d = dict(TESTS[key])
    if over: d.update(over)
    return d


GUIDES = [
{
    "slug": "what-is-a-good-cps",
    "crumb": "What is a good CPS?",
    "card_title": "What is a good CPS?",
    "card_desc": "Average click speed, what's good, and how to click faster.",
    "title": "What Is a Good CPS? Average Click Speed Explained | SpeedLab",
    "desc": "What counts as a good CPS (clicks per second)? The average is 6–7 CPS. Learn what's fast, how test length changes the number, and practical ways to click faster.",
    "ld_desc": "The average click speed is about 6–7 clicks per second; this guide explains what's good and how to improve.",
    "og_title": "What Is a Good CPS? Average Click Speed Explained",
    "og_desc": "The average is 6–7 CPS. Here's what's fast and how to get there.",
    "h1": "What is a good CPS?",
    "lead": "CPS means clicks per second — the number a click speed test gives you. Most people land around 6 to 7. Here's what the ranges actually mean and how to push yours higher.",
    "body": """      <p>If you've just taken a <a href="/cps-test/">CPS test</a> and got a number, the obvious next question is: is that any good? Short answer — the <strong>average click speed is roughly 6 to 7 clicks per second</strong>. Below is what the full range looks like, why the same hand can score differently on different tests, and the techniques that actually move the needle.</p>

      <h2>Average CPS, and what counts as fast</h2>
      <p>On a standard 5-second test with a normal clicking style, here's a fair rule of thumb:</p>
      <ul>
        <li><strong>Under 4 CPS</strong> — relaxed, casual clicking.</li>
        <li><strong>5–7 CPS</strong> — average; where most people land.</li>
        <li><strong>7–9 CPS</strong> — fast; noticeably quicker than average.</li>
        <li><strong>10+ CPS</strong> — very fast for a normal click, and the point where special techniques usually take over.</li>
      </ul>
      <p>These bands are for ordinary clicking — one finger, pressing the button normally. People who post much higher numbers are typically using techniques like jitter clicking (tensing the arm to vibrate the finger) or butterfly clicking (alternating two fingers on one button). Those can push scores past 10–15 CPS, but they're a different skill and can be hard on your hand, so they're not the baseline most people should measure against.</p>

      <h2>Why the test length changes your score</h2>
      <p>A big reason two "CPS scores" aren't always comparable is <strong>duration</strong>. Your peak burst speed is much higher than the rate you can hold for a full minute:</p>
      <ul>
        <li><strong>Short tests (1–2 seconds)</strong> reward a single explosive burst, so they read high.</li>
        <li><strong>The 5-second test</strong> is the fairest all-round measure and the most commonly quoted.</li>
        <li><strong>Long tests (30–100 seconds)</strong> pull your number down toward the rate you can genuinely sustain, because no one holds a peak burst that long.</li>
      </ul>
      <p>So a "9 CPS" on a 1-second burst and a "6 CPS" over a minute can both come from the same hand. When you compare with a friend, make sure you're on the same length.</p>

      <h2>How to click faster</h2>
      <p>You can gain a click or two per second with a few tweaks, no exotic technique required:</p>
      <ul>
        <li><strong>Rest your forearm</strong> on the desk and let your finger, not your whole arm, do the work.</li>
        <li><strong>Use a light mouse button.</strong> A stiff switch caps how fast you can physically cycle it.</li>
        <li><strong>Stay loose.</strong> Tension slows you down and tires you out fast, especially past 10 seconds.</li>
        <li><strong>Match effort to the clock.</strong> Go all-out on short tests; settle into a steady rhythm on long ones.</li>
        <li><strong>Warm up.</strong> A few short runs before your "real" attempt genuinely helps.</li>
      </ul>

      <h2>Measure it properly</h2>
      <p>Take the standard <a href="/cps-test/">5-second CPS test</a> a few times and keep your best. If you play a lot on a phone or tablet, the <a href="/tap-speed-test/">tap speed test</a> measures the same thing with your finger, and the <a href="/spacebar-clicker/">spacebar clicker</a> is the keyboard equivalent. Your personal best for each is saved right in your browser, so you can chase it over time.</p>""",
    "faq": [
        ("What is the average CPS?", "About 6 to 7 clicks per second on a standard 5-second test with a normal clicking style. Under 4 is casual, 7 to 9 is fast, and 10 or more usually means a special technique."),
        ("Is 10 CPS good?", "Yes — 10 CPS is fast for ordinary clicking. Scores well above that usually come from jitter or butterfly clicking rather than a normal single-finger click."),
        ("Why is my CPS higher on shorter tests?", "Short tests capture your peak burst, which is much faster than the rate you can hold. Longer tests average out toward your sustainable speed, so they read lower."),
        ("How can I improve my CPS?", "Rest your forearm, use a light mouse button, stay relaxed, warm up first, and match your effort to the test length — burst on short tests, pace the long ones."),
    ],
    "related_tests": [g_ref("cps"), g_ref("spacebar"), g_ref("tap"), g_ref("keypress"), g_ref("aim"),
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed test."}],
    "related_guides": ["how-to-improve-reaction-time", "average-typing-speed"],
},
{
    "slug": "how-to-improve-reaction-time",
    "crumb": "How to improve reaction time",
    "card_title": "How to improve your reaction time",
    "card_desc": "The average is ~250 ms. What affects it and how to train it.",
    "title": "How to Improve Your Reaction Time (and What's Average) | SpeedLab",
    "desc": "The average human reaction time to a visual signal is about 200–250 ms. Learn what affects your reaction time and practical, evidence-based ways to improve it.",
    "ld_desc": "Average visual reaction time is 200–250 ms; this guide explains what affects it and how to improve.",
    "og_title": "How to Improve Your Reaction Time",
    "og_desc": "The average is ~250 ms. Here's what affects it and how to train it.",
    "h1": "How to improve your reaction time",
    "lead": "A typical reaction to something you see is around 200 to 250 milliseconds. Some of that is fixed biology, but a real chunk is trainable. Here's what's going on and what actually helps.",
    "body": """      <p>When you take a <a href="/reaction-time-test/">reaction time test</a>, you're measuring the gap between a signal appearing and your body responding. For a visual cue like a colour change, <strong>the average is roughly 200–250 milliseconds</strong> — about a quarter of a second. Under 200 ms is fast, and anything under about 150 ms is exceptional (and worth double-checking you didn't guess early).</p>

      <h2>What your reaction time is made of</h2>
      <p>That quarter-second isn't one thing — it's a chain: your eye detects the change, the signal travels to your brain, your brain decides to act, and the command travels to your hand. You can't shorten nerve conduction, but you <em>can</em> improve the detection and decision links, which is why practice helps.</p>
      <p>A few facts worth knowing:</p>
      <ul>
        <li><strong>Sound beats sight.</strong> People react faster to a beep than a flash — audio reaction times are often 30–50 ms quicker. Try the <a href="/audio-reaction-test/">audio reaction test</a> and compare.</li>
        <li><strong>Simple beats complex.</strong> Reacting to one signal is fast; having to choose between "act" and "don't act" adds time. That extra decision cost is exactly what the <a href="/go-no-go/">Go / No-Go test</a> measures.</li>
        <li><strong>It drifts over a session.</strong> Your times get worse when you're tired and better once you're warmed up.</li>
      </ul>

      <h2>What actually affects your score</h2>
      <ul>
        <li><strong>Sleep</strong> — probably the single biggest lever. Being under-slept slows reactions as much as mild alcohol.</li>
        <li><strong>Alertness and caffeine</strong> — a moderate amount can sharpen reactions; too much makes you jumpy and prone to false starts.</li>
        <li><strong>Age</strong> — reaction time is quickest in your late teens to twenties and gradually lengthens after, though training still helps at any age.</li>
        <li><strong>Anticipation</strong> — if you can predict roughly when the signal is coming, you respond faster. Good tests randomise the delay to stop you cheating this.</li>
        <li><strong>Screen and input lag</strong> — a slow monitor or wireless lag adds milliseconds that aren't really "you." A wired mouse and a fast screen give cleaner numbers.</li>
      </ul>

      <h2>How to train it</h2>
      <p>Reaction time responds to practice, but the gains are modest and specific — you get better at the thing you practise. Sensible approach:</p>
      <ul>
        <li><strong>Practise the exact task</strong> you care about, in short frequent sessions rather than one long grind.</li>
        <li><strong>Warm up</strong> with a handful of attempts before you judge your "real" score.</li>
        <li><strong>Wait, don't guess.</strong> Anticipating the signal lowers your average but wrecks your accuracy — and on a Go/No-Go task it costs you points. Learn to fire on the signal, not before it.</li>
        <li><strong>Fix the basics first:</strong> sleep, a bit of caffeination if that's your thing, good lighting, low input lag.</li>
        <li><strong>Mix in aim work.</strong> The <a href="/aim-trainer/">aim trainer</a> trains reaction plus targeting together, which is closer to how reactions get used in games and sport.</li>
      </ul>

      <h2>Test yourself the right way</h2>
      <p>Take the <a href="/reaction-time-test/">reaction time test</a> five times and use the average, not your single best fluke. Then compare it against the <a href="/audio-reaction-test/">audio</a> version and the <a href="/go-no-go/">Go / No-Go</a> test to see how much a sound cue and an added decision each change your number. Those differences tell you more about your reflexes than any one score.</p>""",
    "faq": [
        ("What is the average reaction time?", "For a visual signal, about 200 to 250 milliseconds. Under 200 ms is fast and under roughly 150 ms is exceptional. Reactions to sound are typically a little quicker than to sight."),
        ("Can you actually improve reaction time?", "Yes, but modestly and specifically — you improve at the task you practise. Sleep, alertness, warming up, and low input lag make a bigger day-to-day difference than raw training."),
        ("Why is my reaction time slower some days?", "Mostly sleep and alertness. Being tired can slow reactions substantially, while being warmed up and rested speeds them back up. Screen and mouse lag also add milliseconds."),
        ("Is a sound or a visual signal faster to react to?", "Sound. People generally react 30 to 50 milliseconds faster to a beep than to a visual change, because the auditory path to your brain is shorter."),
    ],
    "related_tests": [g_ref("reaction"), g_ref("audio"), g_ref("gonogo"), g_ref("aim"),
                      {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Timing precision."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["what-is-a-good-cps", "average-typing-speed"],
},
{
    "slug": "average-typing-speed",
    "crumb": "Average typing speed",
    "card_title": "What is a good typing speed?",
    "card_desc": "Average WPM, how it's measured, and how to type faster.",
    "title": "Average Typing Speed: What Is a Good WPM? | SpeedLab",
    "desc": "The average typing speed is about 40 WPM; touch typists hit 60–80 and pros exceed 100. Learn how WPM is measured and practical ways to type faster and more accurately.",
    "ld_desc": "Average typing speed is around 40 WPM; this guide explains a good WPM and how to improve.",
    "og_title": "Average Typing Speed: What Is a Good WPM?",
    "og_desc": "40 WPM is average, 60–80 is a good touch typist, 100+ is pro.",
    "h1": "What is a good typing speed?",
    "lead": "The average typist manages around 40 words per minute. Comfortable touch typists sit at 60–80, and professionals push past 100. Here's how WPM is measured and how to move up a tier.",
    "body": """      <p>Typing speed is measured in <strong>words per minute (WPM)</strong>, and the honest benchmark is simpler than most people expect. On a <a href="/typing-speed-test/">typing speed test</a>, here's where the tiers fall:</p>
      <ul>
        <li><strong>Around 40 WPM</strong> — the average, typical of someone who doesn't touch-type.</li>
        <li><strong>60–80 WPM</strong> — a comfortable touch typist who doesn't look at the keys.</li>
        <li><strong>80–100 WPM</strong> — fast; the range of people who type for a living.</li>
        <li><strong>100+ WPM</strong> — professional-grade speed.</li>
      </ul>

      <h2>How WPM is actually calculated</h2>
      <p>"A word" isn't a real word — it's standardised as <strong>five characters</strong>, spaces included. So your gross WPM is (characters typed ÷ 5) ÷ (minutes elapsed). The important part is what happens to mistakes: <strong>net WPM</strong> subtracts your errors, which is why accuracy matters as much as raw speed. Hammering keys at 90 WPM with 15% errors can net out slower than a steady 70 WPM at 99%.</p>
      <p>Test length matters too. A 15-second test lets you ride a good streak and reads a little high; a one-minute or longer test settles closer to your true sustained speed. When you compare scores, compare the same duration.</p>

      <h2>How to type faster</h2>
      <p>Speed follows technique — chasing raw pace first usually just builds fast bad habits. In order of impact:</p>
      <ul>
        <li><strong>Touch type.</strong> Learning the home row and never looking down is the single biggest jump most people can make. It feels slow for a week, then overtakes your old speed.</li>
        <li><strong>Prioritise accuracy.</strong> Aim for 97%+ before you push pace. Errors and corrections cost more time than they feel like they do.</li>
        <li><strong>Use all ten fingers</strong> and let each one own its keys, so your hands barely move.</li>
        <li><strong>Look ahead.</strong> Read a word or two beyond what you're typing so your fingers always have a queue.</li>
        <li><strong>Practise little and often.</strong> Short daily sessions beat occasional marathons for building muscle memory.</li>
      </ul>

      <h2>Beyond words: raw finger speed</h2>
      <p>WPM blends thinking, reading, and finger movement. If you want to isolate pure finger speed, the <a href="/key-press-test/">key press test</a> measures how fast you can hit a single key, and the <a href="/spacebar-clicker/">spacebar clicker</a> does the same for one big key. They're a fun contrast to a full typing test — you'll see how much of typing is actually reading and decision-making rather than finger movement.</p>

      <h2>Test yourself</h2>
      <p>Run the <a href="/typing-speed-test/">typing speed test</a> at a length that suits you and keep your best. Try the <a href="/alphabet-typing-test/">alphabet</a> and <a href="/number-typing-test/">number</a> sprints too — they strip typing down to sequences you already know, so they're a clean way to feel your ceiling.</p>""",
    "faq": [
        ("What is the average typing speed?", "About 40 words per minute. Comfortable touch typists reach 60 to 80 WPM, fast typists 80 to 100, and professionals exceed 100."),
        ("How is WPM calculated?", "A 'word' is standardised as five characters including spaces. Your speed is characters typed divided by five, per minute — and net WPM subtracts errors, so accuracy counts."),
        ("Is 60 WPM good?", "Yes. 60 WPM is a solid touch-typing speed, well above the ~40 WPM average. Getting to 80+ mostly comes from higher accuracy rather than faster finger movement."),
        ("Does test length change my WPM?", "Yes. Short tests let you ride a hot streak and read a bit higher; one-minute-plus tests settle closer to your true sustained speed. Compare like with like."),
    ],
    "related_tests": [g_ref("typing"), g_ref("keypress"),
                      {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z fast."},
                      {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race 1 to 100."},
                      g_ref("spacebar"),
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed test."}],
    "related_guides": ["what-is-a-good-cps", "do-brain-training-games-work"],
},
{
    "slug": "do-brain-training-games-work",
    "crumb": "Do brain games work?",
    "card_title": "Do brain-training games work?",
    "card_desc": "What memory tests really measure — and how to actually improve.",
    "title": "Do Brain-Training Games Work? What Memory Tests Measure | SpeedLab",
    "desc": "Do brain games actually make you smarter? Here's the honest evidence, what memory and attention tests really measure, and habits that genuinely help your focus and recall.",
    "ld_desc": "An honest look at whether brain-training games work and what memory tests actually measure.",
    "og_title": "Do Brain-Training Games Work?",
    "og_desc": "The honest answer, and what memory tests really measure.",
    "h1": "Do brain-training games work?",
    "lead": "Memory and attention games are fun and oddly addictive — but do they actually make you sharper? Here's the honest picture, and what our memory tests are really measuring.",
    "body": """      <p>It's tempting to think that grinding a <a href="/number-memory/">number memory</a> or <a href="/visual-memory/">visual memory</a> test will make your everyday memory better across the board. The honest, evidence-based answer is more modest: <strong>you reliably get better at the specific task you practise, but that improvement rarely transfers</strong> to unrelated skills. Getting great at recalling digit strings makes you great at recalling digit strings — it won't obviously make you better at remembering names or where you left your keys.</p>
      <p>That's not a reason to skip them. It just reframes what they're good for: they're an enjoyable way to test and track a specific ability, a decent warm-up, and a fun benchmark against yourself over time — not a magic upgrade to your brain.</p>

      <h2>What each memory test actually measures</h2>
      <ul>
        <li><strong><a href="/number-memory/">Number Memory</a></strong> — your digit span, i.e. how many numbers you can hold in short-term memory at once. Most people manage around 7.</li>
        <li><strong><a href="/sequence-memory/">Sequence Memory</a></strong> — spatial working memory: reproducing a growing pattern in order.</li>
        <li><strong><a href="/visual-memory/">Visual Memory</a></strong> — how many positions on a grid you can hold at once.</li>
        <li><strong><a href="/chimp-test/">Chimp Test</a></strong> — a famous task where chimpanzees often beat humans; it tests rapid spatial memory under time pressure.</li>
        <li><strong><a href="/memory-match/">Memory Match</a></strong> — classic concentration: building and updating a mental map of hidden pairs.</li>
      </ul>

      <h2>What genuinely helps your memory and focus</h2>
      <p>The boring stuff has the strongest evidence behind it:</p>
      <ul>
        <li><strong>Sleep.</strong> Memories consolidate while you sleep; short-changing it hits recall and attention hard.</li>
        <li><strong>Exercise.</strong> Regular aerobic activity is one of the best-supported things for long-term brain health.</li>
        <li><strong>Attention, not tricks.</strong> Most "bad memory" is actually never having paid attention in the first place. Removing distraction beats any technique.</li>
        <li><strong>Active recall.</strong> Testing yourself on something (rather than re-reading it) is far more effective for remembering it — the reason these tests feel like work.</li>
        <li><strong>Chunking.</strong> Grouping information — a phone number as three chunks, not ten digits — is how people push past the usual limits, and it's a skill you can practise.</li>
      </ul>

      <h2>Use them as benchmarks, not miracles</h2>
      <p>The most useful way to treat these games is as a personal benchmark: take one occasionally, keep your best, and watch it move with your sleep and stress. If you want a genuine short workout, string a few together — <a href="/number-memory/">number memory</a> for digit span, <a href="/visual-memory/">visual memory</a> for spatial recall, and <a href="/chimp-test/">chimp test</a> for speed under pressure. Just go in knowing what they can and can't do.</p>""",
    "faq": [
        ("Do brain-training games make you smarter?", "Mostly no, in the broad sense. You reliably improve at the specific task you practise, but that gain rarely transfers to unrelated abilities or general intelligence. They're better treated as benchmarks and warm-ups than upgrades."),
        ("What does the number memory test measure?", "Your digit span — how many numbers you can hold in short-term memory at once. Most people manage around seven, which is why phone numbers are the length they are."),
        ("What actually improves memory and focus?", "Sleep, regular exercise, removing distractions, active recall (testing yourself), and chunking information into groups. These have far stronger evidence than any single brain game."),
        ("Why do chimpanzees beat humans at the chimp test?", "Chimps appear to excel at rapidly memorising the positions of briefly shown numbers — a form of fast spatial memory where they often outperform adult humans."),
    ],
    "related_tests": [g_ref("numbermem"), g_ref("seqmem"), g_ref("vismem"), g_ref("chimp"), g_ref("match"),
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every brain test."}],
    "related_guides": ["how-to-improve-reaction-time", "average-typing-speed"],
},
{
    "slug": "what-is-a-good-reaction-time",
    "crumb": "What is a good reaction time?",
    "card_title": "What is a good reaction time?",
    "card_desc": "The millisecond ranges, how you compare, and what shifts them.",
    "title": "What Is a Good Reaction Time? Average Times by Age | SpeedLab",
    "desc": "The average human reaction time to a visual signal is about 200-250 ms. See the full millisecond ranges, how reaction time changes with age, and where your score lands.",
    "ld_desc": "A good visual reaction time is under about 250 ms; this guide breaks down the ranges and how age affects them.",
    "og_title": "What Is a Good Reaction Time?",
    "og_desc": "Average is ~250 ms. Here's where your score lands.",
    "og_image": "guide-rt-good.png",
    "h1": "What is a good reaction time?",
    "lead": "Take a reaction test, get a number in milliseconds, and the question is instant: is that fast? Here's the honest breakdown of the ranges, how age moves them, and what a single score does and doesn't tell you.",
    "body": """      <p>When you tap on green in a <a href="/reaction-time-test/">reaction time test</a>, you're measuring the gap between a signal appearing and your finger moving. For a visual cue, the <strong>average adult lands around 200-250 milliseconds</strong> &mdash; about a quarter of a second. That number is the baseline everything else is measured against.</p>

      <h2>The ranges, in plain milliseconds</h2>
      <ul>
        <li><strong>Over 300 ms</strong> &mdash; slower than average; often tiredness, a laggy screen, or not being warmed up.</li>
        <li><strong>250-300 ms</strong> &mdash; a typical, relaxed response.</li>
        <li><strong>200-250 ms</strong> &mdash; the average-to-good band most people sit in once warmed up.</li>
        <li><strong>150-200 ms</strong> &mdash; fast; the range competitive gamers aim for.</li>
        <li><strong>Under 150 ms</strong> &mdash; exceptional, and worth double-checking you didn't anticipate the signal rather than react to it.</li>
      </ul>
      <p>Anything under roughly 100 ms on a visual test is almost certainly a <em>jump</em> &mdash; you pressed before you actually processed the green. A good test randomises the delay specifically to catch that.</p>

      <h2>How age changes the number</h2>
      <p>Reaction time follows a predictable arc across a lifetime. It sharpens quickly through childhood, peaks in the late teens to late twenties, holds fairly steady through the thirties, then lengthens gradually from middle age onward. The change is real but smaller than people assume &mdash; a well-rested, warmed-up fifty-year-old routinely beats a tired twenty-year-old. Age sets a soft ceiling; your state on the day decides where under it you land.</p>

      <h2>Why one score means little</h2>
      <p>A single attempt is noisy. The right way to read your reaction time is the <strong>average of five or more tries</strong>, ignoring the obvious misfires. That is exactly why our test runs five rounds and averages them. Look at the spread too: five times of 240, 245, 238, 250, 242 is a more reliable 243 than 210, 300, 190, 280, 235, even though the second set has a lower single best.</p>

      <h2>Simple vs choice reaction time</h2>
      <p>The 250 ms figure is for <em>simple</em> reaction time: one signal, one response. The moment a decision is added &mdash; act on this, but not on that &mdash; the clock stretches by 50-150 ms, because your brain has to classify the signal before it moves. That extra cost is what the <a href="/go-no-go/">Go / No-Go test</a> isolates, and it's closer to what real driving or gaming demands than a bare reaction test.</p>

      <h2>Measure yours properly</h2>
      <p>Warm up with a few throwaway attempts, then take the <a href="/reaction-time-test/">reaction time test</a> for your visual baseline. Compare it against the <a href="/audio-reaction-test/">audio reaction test</a> &mdash; most people are 30-50 ms faster to a beep &mdash; and the <a href="/go-no-go/">Go / No-Go</a> for your reaction-under-decision. Those three numbers together describe your reflexes far better than any single score. If you want to actually lower them, see our guide on <a href="/guides/how-to-improve-reaction-time/">how to improve your reaction time</a>.</p>""",
    "faq": [
        ("What is the average reaction time in milliseconds?", "About 200 to 250 ms for a visual signal. Under 200 ms is fast, under 150 ms is exceptional, and under about 100 ms usually means you anticipated the signal rather than reacting to it."),
        ("Is a 200 ms reaction time good?", "Yes. 200 ms sits at the fast end of the normal range and is roughly what warmed-up competitive gamers aim for. Most people average a little above it."),
        ("Does reaction time get worse with age?", "Gradually, yes, after peaking in your late teens to twenties. But sleep, alertness and being warmed up affect your score far more than age does day to day."),
        ("How many tries should I average?", "At least five, ignoring obvious misfires. A single attempt is too noisy to mean anything, which is why our test averages five rounds."),
    ],
    "related_tests": [g_ref("reaction"), g_ref("audio"), g_ref("gonogo"), g_ref("aim"),
                      {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Timing precision."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["how-to-improve-reaction-time", "reaction-time-in-gaming"],
},
{
    "slug": "how-to-click-faster",
    "crumb": "How to click faster",
    "card_title": "How to click faster",
    "card_desc": "Normal, jitter, butterfly and drag clicking — and the risks.",
    "title": "How to Click Faster: Jitter, Butterfly & Drag Clicking | SpeedLab",
    "desc": "Want a higher CPS? Here's how to click faster with normal technique, plus how jitter, butterfly and drag clicking work, what they score, and the real risks to your hand.",
    "ld_desc": "A guide to clicking faster, covering normal technique plus jitter, butterfly and drag clicking and their trade-offs.",
    "og_title": "How to Click Faster",
    "og_desc": "Normal, jitter, butterfly and drag clicking explained.",
    "og_image": "guide-click-faster.png",
    "h1": "How to click faster",
    "lead": "Most people can add two or three clicks per second with a few tweaks, no exotic technique required. Here's how to raise your CPS safely first, then what the advanced techniques actually involve.",
    "body": """      <p>Clicking speed is part technique, part equipment, and part knowing which method suits the job. Before chasing the techniques that push past 10 CPS, it's worth maxing out a normal click &mdash; it's where the safe, repeatable gains are. Test your starting point on the <a href="/cps-test/">CPS test</a>, then work through this.</p>

      <h2>Get the basics right first</h2>
      <ul>
        <li><strong>Rest your forearm</strong> on the desk and click from the finger, not the whole arm. A moving arm wastes energy and tires fast.</li>
        <li><strong>Use a light mouse button.</strong> A stiff switch physically caps how fast you can cycle it; a light, tactile one lets your finger rebound quicker.</li>
        <li><strong>Stay loose.</strong> Tension is the enemy of speed and the fastest route to a sore hand. A relaxed hand clicks faster for longer.</li>
        <li><strong>Warm up.</strong> A couple of short runs before your real attempt reliably adds a click or two per second.</li>
        <li><strong>Match effort to the clock.</strong> Burst flat-out on a 1 or 2-second test; pace yourself on 10 seconds or more. See <a href="/guides/what-is-a-good-cps/">what a good CPS is</a> for the ranges.</li>
      </ul>
      <p>A focused normal click tops out around 7-10 CPS for most people. That's a genuinely good score and it's gentle on your hand. Everything below goes further but trades comfort for numbers.</p>

      <h2>Jitter clicking</h2>
      <p>Jitter clicking means tensing your forearm and wrist so the muscles vibrate, letting the finger buzz the button many times a second. Skilled jitter clickers reach 10-14 CPS. It's effective but hard to aim while doing it, and the deliberate muscle tension is the technique most associated with strain &mdash; it is not something to hold for long sessions.</p>

      <h2>Butterfly clicking</h2>
      <p>Butterfly clicking alternates <strong>two fingers</strong> on a single mouse button, so each downstroke registers a separate click. It can push 12-16 CPS and is easier to sustain than jittering. The catch: some mice register the rapid alternation as double-clicks unevenly, so results vary by hardware, and a few games or servers treat it as off-limits.</p>

      <h2>Drag clicking</h2>
      <p>Drag clicking drags a fingertip across the button so friction triggers a burst of rapid clicks &mdash; it can spike enormous numbers, but it depends heavily on the mouse surface and is the least controllable for anything but a raw score.</p>

      <h2>A word on your hands</h2>
      <p>The techniques that post the biggest numbers rely on sustained tension and repetitive strain is real. If clicking ever hurts, stop. For everyday use and most games, a relaxed normal click in the 7-10 range is the sweet spot: fast, accurate, and something you can do for hours. Chase the big numbers on the <a href="/cps-test/">CPS test</a> for fun, not as a daily habit. On a phone, the same ideas apply to the <a href="/tap-speed-test/">tap speed test</a> &mdash; two thumbs alternating is the butterfly equivalent.</p>""",
    "faq": [
        ("What is the fastest way to click?", "For a raw score, butterfly and drag clicking post the highest numbers. For everyday use, a relaxed normal click with a rested forearm and a light mouse button is fastest and safest at around 7-10 CPS."),
        ("Is jitter clicking bad for your hand?", "It can be. Jitter clicking relies on sustained muscle tension, which is the technique most linked to strain. Use it briefly for scores, not for long sessions, and stop if it hurts."),
        ("Why is butterfly clicking faster?", "Because two fingers alternate on one button, each registering its own click, so you roughly double the clicks a single finger could manage."),
        ("Does my mouse affect clicking speed?", "A lot. A light, responsive button lets you click faster and is needed for techniques like drag clicking, which depends on the button surface."),
    ],
    "related_tests": [g_ref("cps"), g_ref("tap"), g_ref("spacebar"), g_ref("keypress"),
                      {"slug": "right-click-test", "kbd": "Mouse", "name": "Right Click Test", "desc": "How fast can you right click?"},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed test."}],
    "related_guides": ["what-is-a-good-cps", "gaming-warm-up-routine"],
},
{
    "slug": "how-to-type-faster",
    "crumb": "How to type faster",
    "card_title": "How to type faster",
    "card_desc": "Touch typing, technique, and a realistic practice plan.",
    "title": "How to Type Faster: A Touch Typing Guide | SpeedLab",
    "desc": "Learn how to type faster with touch typing: the home row, proper technique, why accuracy beats raw speed, and a realistic four-week practice plan to raise your WPM.",
    "ld_desc": "A practical guide to typing faster through touch typing, technique and a four-week practice plan.",
    "og_title": "How to Type Faster",
    "og_desc": "Touch typing, technique, and a practice plan.",
    "og_image": "guide-type-faster.png",
    "h1": "How to type faster",
    "lead": "Faster typing is a skill, not a talent, and almost everyone can double their speed. The route is the same for everyone: learn to touch type, protect your accuracy, then build speed on top. Here's how.",
    "body": """      <p>If you're hunting and pecking, you're probably typing around 25-35 words per minute. A comfortable touch typist does 60-80, and it's a learnable gap. Check where you're starting with the <a href="/typing-speed-test/">typing speed test</a>, then follow the steps below. For context on the numbers, see <a href="/guides/average-typing-speed/">what a good typing speed is</a>.</p>

      <h2>Step 1: Learn the home row</h2>
      <p>Touch typing starts with your fingers resting on the home row &mdash; left hand on A, S, D, F and right hand on J, K, L and the semicolon. The small bumps on F and J let you find that position without looking. Every other key is reached from there and your fingers return home after each press. This one habit &mdash; never looking at the keyboard &mdash; is the single biggest jump most people ever make. It feels painfully slow for about a week, then it overtakes your old hunt-and-peck speed and keeps climbing.</p>

      <h2>Step 2: Protect accuracy before speed</h2>
      <p>This is the step people skip, and it's why they plateau. Every mistake costs you the time to notice it, backspace, and retype &mdash; far more than the keystroke saved by rushing. Aim for <strong>97% accuracy or better</strong> before you push the pace. On our test, WPM is net of errors precisely because accuracy is what actually makes you fast. Slow down until you're clean, and speed arrives on its own.</p>

      <h2>Step 3: Use all ten fingers and look ahead</h2>
      <p>Let each finger own its columns so your hands barely move. Then train your eyes to read a word or two <em>ahead</em> of what you're typing, so your fingers always have a queue to work through. Fluent typists are never reading the letter they're currently pressing &mdash; they're already two words down the line.</p>

      <h2>A realistic four-week plan</h2>
      <ul>
        <li><strong>Week 1:</strong> home row only, eyes off the keys. Accuracy over everything. 10 minutes a day.</li>
        <li><strong>Week 2:</strong> add the top and bottom rows and numbers. Still accuracy-first, still 10 minutes daily.</li>
        <li><strong>Week 3:</strong> type real sentences and paragraphs; start timing yourself but don't chase the clock.</li>
        <li><strong>Week 4:</strong> short daily speed runs on the <a href="/typing-speed-test/">typing speed test</a>, keeping accuracy above 97%.</li>
      </ul>
      <p>Short daily practice beats occasional marathons every time &mdash; muscle memory is built by repetition, not duration.</p>

      <h2>Warm up your fingers, too</h2>
      <p>Pure finger speed is a separate ingredient from typing. Loosen up with the <a href="/key-press-test/">key press test</a> (how fast you can hit one key), the <a href="/alphabet-typing-test/">alphabet sprint</a>, or the <a href="/word-spammer/">Word Spammer</a> &mdash; typing one word on repeat is a great way to feel your hands' true top speed before a real run.</p>""",
    "faq": [
        ("How long does it take to learn touch typing?", "Most people are comfortable within three to four weeks of short daily practice. It feels slower than hunt-and-peck for the first week, then overtakes it and keeps improving."),
        ("Why does accuracy matter more than speed?", "Because every error costs the time to notice, delete and retype it, which is more than you save by rushing. Net WPM subtracts mistakes, so clean typing is literally faster."),
        ("What is a realistic typing speed goal?", "Around 60-80 WPM is a solid touch-typing target and well above the ~40 WPM average. Getting there is mostly about accuracy, not faster fingers."),
        ("Does practising a few minutes a day really work?", "Yes, and it beats long infrequent sessions. Typing is muscle memory, which is built by frequent repetition rather than duration."),
    ],
    "related_tests": [g_ref("typing"), g_ref("keypress"),
                      {"slug": "alphabet-typing-test", "kbd": "Keyboard", "name": "Alphabet Typing Test", "desc": "Type A to Z fast."},
                      {"slug": "number-typing-test", "kbd": "Keyboard", "name": "Number Typing Test", "desc": "Race 1 to 100."},
                      {"slug": "word-spammer", "kbd": "Keyboard", "name": "Word Spammer", "desc": "Type one word, fast."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed test."}],
    "related_guides": ["average-typing-speed", "what-is-a-good-cps"],
},
{
    "slug": "reaction-time-in-gaming",
    "crumb": "Reaction time in gaming",
    "card_title": "Reaction time in gaming",
    "card_desc": "Why milliseconds win matches, and how to train them.",
    "title": "Reaction Time in Gaming: Why Milliseconds Matter | SpeedLab",
    "desc": "How much does reaction time matter in gaming? A look at pro benchmarks, how input lag quietly steals milliseconds, and a practical routine to train faster reactions.",
    "ld_desc": "How reaction time affects gaming performance, what pros hit, and how to train and protect your milliseconds.",
    "og_title": "Reaction Time in Gaming",
    "og_desc": "Why milliseconds win matches, and how to train them.",
    "og_image": "guide-gaming-rt.png",
    "h1": "Reaction time in gaming",
    "lead": "In fast shooters and fighting games, matches are decided in the gap between seeing something and doing something about it. Here's how much reaction time really matters, what the top players hit, and how to train and protect yours.",
    "body": """      <p>Reaction time is one of the few athletic traits that transfers directly to gaming: the player who processes a flick of movement 40 ms sooner shoots first. But raw reaction is only part of the picture, and it's easy to lose milliseconds you never knew you had. Start by measuring your baseline on the <a href="/reaction-time-test/">reaction time test</a>.</p>

      <h2>What counts as a gaming-grade reaction</h2>
      <p>The <a href="/guides/what-is-a-good-reaction-time/">average reaction time</a> is 200-250 ms. Serious competitive players tend to sit in the <strong>150-200 ms</strong> band on a clean test, warmed up. Below 150 ms is rare and often reflects partial anticipation rather than pure reaction. The difference between average and elite is real but modest &mdash; which is exactly why the surrounding factors matter so much.</p>

      <h2>Reaction is only half of it</h2>
      <p>Pure reaction &mdash; respond to one surprise signal &mdash; is what the basic test measures. Games rarely ask that. They ask you to <em>choose</em>: is that an enemy or a teammate, do I shoot or hold. Adding a decision costs 50-150 ms, which is why trained players lean on <strong>prediction</strong> &mdash; reading angles, timings and tendencies so they're already moving before the signal fully arrives. The <a href="/go-no-go/">Go / No-Go test</a> trains exactly this act-or-withhold judgement, and <a href="/aim-trainer/">aim training</a> pairs reaction with the targeting that follows it.</p>

      <h2>The milliseconds you're leaking</h2>
      <p>Your measured reaction is only the human part. Between your decision and the game responding sit several silent delays:</p>
      <ul>
        <li><strong>Display lag:</strong> a 60 Hz screen can add 30-50 ms versus a 144 Hz+ monitor.</li>
        <li><strong>Input lag:</strong> wireless peripherals and high-latency USB polling add a few ms each.</li>
        <li><strong>Network ping:</strong> in online play, your shot still has to reach the server.</li>
      </ul>
      <p>Fixing the setup often buys more real-world speed than months of training. A faster screen and a wired mouse are the cheapest reaction-time upgrades there are.</p>

      <h2>A training routine that works</h2>
      <p>Reaction gains are modest and specific, so train the exact skills and keep sessions short:</p>
      <ul>
        <li><strong>Warm up</strong> for a few minutes before you play &mdash; cold reactions are slow reactions. Our <a href="/guides/gaming-warm-up-routine/">warm-up routine</a> lays out a 5-minute version.</li>
        <li><strong>Train the pieces:</strong> <a href="/reaction-time-test/">reaction</a> for raw speed, <a href="/go-no-go/">Go / No-Go</a> for decisions, <a href="/aim-trainer/">aim trainer</a> for react-and-target.</li>
        <li><strong>Sleep.</strong> Under-slept reactions are measurably slower; it's the highest-leverage thing on this list.</li>
      </ul>
      <p>Want the fundamentals? See <a href="/guides/how-to-improve-reaction-time/">how to improve your reaction time</a> and <a href="/guides/can-you-train-your-reflexes/">whether reflexes are trainable</a>.</p>""",
    "faq": [
        ("What reaction time do pro gamers have?", "Most competitive players sit around 150-200 ms on a clean, warmed-up visual test. Below 150 ms is rare and often involves anticipation rather than pure reaction."),
        ("Does a better monitor improve reaction time?", "It improves your effective reaction. A 144 Hz+ screen can shave 30-50 ms of display lag versus 60 Hz, which is often more than you'd gain from training."),
        ("Can I actually train gaming reactions?", "Yes, modestly and specifically. Practising reaction, decision (Go/No-Go) and aim tasks helps, but sleep, warming up and low input lag make a bigger day-to-day difference."),
        ("Is reaction time or prediction more important?", "Both. Elite players rely heavily on prediction to effectively beat their own reaction time, because reading what's about to happen means they're already moving."),
    ],
    "related_tests": [g_ref("reaction"), g_ref("aim"), g_ref("gonogo"), g_ref("audio"),
                      {"slug": "dino-game", "kbd": "Reaction", "name": "Dino Dash", "desc": "Jump and duck, faster each second."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["how-to-improve-reaction-time", "gaming-warm-up-routine"],
},
{
    "slug": "how-to-improve-hand-eye-coordination",
    "crumb": "Hand-eye coordination",
    "card_title": "How to improve hand-eye coordination",
    "card_desc": "What it is, drills that help, and how to track progress.",
    "title": "How to Improve Hand-Eye Coordination | SpeedLab",
    "desc": "Hand-eye coordination is trainable at any age. Here's what it actually is, drills and activities that genuinely help, and simple ways to track your progress over time.",
    "ld_desc": "A practical guide to improving hand-eye coordination with drills, activities and progress tracking.",
    "og_title": "How to Improve Hand-Eye Coordination",
    "og_desc": "What it is, drills that help, and how to track it.",
    "og_image": "guide-hand-eye.png",
    "h1": "How to improve hand-eye coordination",
    "lead": "Hand-eye coordination is the link between what your eyes see and what your hands do about it. It's not fixed &mdash; it responds to practice at any age. Here's what it is and how to build it.",
    "body": """      <p>Hand-eye coordination is your visual system and your motor system working as a team: your eyes locate a target, your brain plots the movement, and your hand executes it &mdash; continuously, with corrections mid-flight. It underlies everything from catching a ball to landing a flick shot to simply using a mouse smoothly. The good news is it behaves like any trainable skill: specific, improvable, and measurable.</p>

      <h2>What actually drives it</h2>
      <p>Three things combine into what we loosely call coordination: how quickly you <strong>spot</strong> the target, how accurately you <strong>plan</strong> the movement, and how well you <strong>correct</strong> it as you go. Training works by tightening that loop &mdash; shrinking the gap between seeing and doing, and reducing the overshoot when you move fast. That's why pure reaction training alone isn't enough; you need the targeting part too.</p>

      <h2>Drills that genuinely help</h2>
      <ul>
        <li><strong>Target practice under time pressure.</strong> The <a href="/aim-trainer/">aim trainer</a> is built for this: spot a target, move to it, click, repeat &mdash; the core coordination loop on a timer.</li>
        <li><strong>Catch and juggle.</strong> Old-fashioned but excellent. Bouncing a ball off a wall and catching it, or learning to juggle, trains prediction and timing better than most screens can.</li>
        <li><strong>Whack-style reaction games.</strong> <a href="/whack-a-mole/">Whack-a-Mole</a> forces you to locate a target that appears somewhere unpredictable and hit it fast.</li>
        <li><strong>Precision timing.</strong> <a href="/stop-the-clock/">Stop the Clock</a> trains the anticipation half of coordination &mdash; acting at an exact moment rather than merely reacting.</li>
        <li><strong>Rhythm and music.</strong> Drumming, an instrument, or rhythm games build the timing and bilateral control coordination depends on.</li>
      </ul>

      <h2>How to practise so it sticks</h2>
      <p>Short, frequent, focused sessions beat long grinds &mdash; ten focused minutes a day will do more than an occasional hour. Push slightly past comfortable: practise at a speed where you miss <em>sometimes</em>, because that's where adaptation happens. And vary the drills; coordination built on one narrow task transfers poorly, so mix targeting, catching and timing.</p>

      <h2>Track it so you know it's working</h2>
      <p>Pick one or two tests as your yardstick and revisit them weekly. Your <a href="/aim-trainer/">aim trainer</a> average and your <a href="/reaction-time-test/">reaction time</a> are good anchors; both save your best on this device so you can watch the trend. Progress is gradual &mdash; think weeks, not days &mdash; but it's real, and seeing the number move is the best motivation there is. For the reflex side of the equation, see <a href="/guides/can-you-train-your-reflexes/">can you train your reflexes</a>.</p>""",
    "faq": [
        ("Can adults improve hand-eye coordination?", "Yes. It responds to practice at any age. The gains are gradual and specific to what you train, but they're real whether you're 15 or 55."),
        ("What games improve hand-eye coordination?", "Target-and-timing games help most: aim trainers, whack-a-mole style reaction games, and precision-timing tasks. Off-screen, catching and juggling are excellent."),
        ("How long until I see improvement?", "Think weeks of short daily practice rather than days. Tracking one test weekly is the clearest way to confirm the trend is moving."),
        ("Is hand-eye coordination the same as reaction time?", "Related but not identical. Reaction time is how fast you respond to a signal; coordination adds accurately moving your hand to a target and correcting as you go."),
    ],
    "related_tests": [g_ref("aim"), g_ref("reaction"),
                      {"slug": "whack-a-mole", "kbd": "Reaction", "name": "Whack-a-Mole", "desc": "Bop the moles."},
                      {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Stop the timer on target."},
                      {"slug": "emoji-hunt", "kbd": "Reaction", "name": "Emoji Hunt", "desc": "Find the odd one out."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["can-you-train-your-reflexes", "reaction-time-in-gaming"],
},
{
    "slug": "can-you-train-your-reflexes",
    "crumb": "Can you train reflexes?",
    "card_title": "Can you train your reflexes?",
    "card_desc": "What the science says about what's trainable and what isn't.",
    "title": "Can You Train Your Reflexes? What Actually Works | SpeedLab",
    "desc": "Are reflexes trainable or fixed? An honest look at what practice can and can't change about your reaction speed, and the habits that make the biggest real difference.",
    "ld_desc": "An honest look at whether reflexes can be trained and which habits make the biggest difference.",
    "og_title": "Can You Train Your Reflexes?",
    "og_desc": "What the science really says about trainable reflexes.",
    "og_image": "guide-reflexes.png",
    "h1": "Can you train your reflexes?",
    "lead": "The honest answer is: partly, and less dramatically than most ads promise &mdash; but the parts you can change are worth changing. Here's what practice actually moves, and what it doesn't.",
    "body": """      <p>First, a definition. A true <em>reflex</em> &mdash; like your knee jerking &mdash; is an automatic spinal response you can't really speed up. What people mean by training reflexes is lowering their <strong>reaction time</strong>: the voluntary response to something you see or hear. That one is partly trainable, and understanding the split keeps your expectations honest.</p>

      <h2>What you can change</h2>
      <ul>
        <li><strong>Task-specific speed.</strong> Practise a particular reaction and you get faster at <em>that</em> reaction. A clicker gets faster at clicking; a shooter gets faster at reacting to a flick. This is reliable and measurable.</li>
        <li><strong>Consistency.</strong> Even when your average barely moves, practice tightens your spread &mdash; fewer slow misfires. More reliable is often more useful than a lower best.</li>
        <li><strong>Prediction.</strong> The biggest real gains come from learning to anticipate, so you're already moving before the signal fully lands. It feels like faster reflexes even though your raw reaction is unchanged.</li>
        <li><strong>Your daily state.</strong> Sleep, alertness, caffeine and warming up swing your reaction time more than weeks of drills &mdash; and you control them every single day.</li>
      </ul>

      <h2>What you can't change much</h2>
      <p>The hard floor is biology: nerve signals travel at a fixed speed, and the raw conduction time from eye to brain to hand can't be trained away. That's why nobody reliably reacts to a visual signal in 50 ms &mdash; the wiring won't allow it. Your genetics and age set a soft ceiling on your best possible time; training moves you toward that ceiling, not past it. The &quot;transfer&quot; promise is also oversold: getting great at one reaction task does little for unrelated ones.</p>

      <h2>So what should you actually do?</h2>
      <ol>
        <li><strong>Fix your state first.</strong> Sleep well, warm up before it matters, cut input lag. Highest leverage, lowest effort.</li>
        <li><strong>Train the exact task you care about</strong>, in short frequent sessions rather than long grinds.</li>
        <li><strong>Practise prediction,</strong> not just raw reaction &mdash; read patterns and timings.</li>
        <li><strong>Track one benchmark</strong> so you can tell real progress from a good day.</li>
      </ol>

      <h2>Put it to the test</h2>
      <p>Use the <a href="/reaction-time-test/">reaction time test</a> as your benchmark, the <a href="/go-no-go/">Go / No-Go test</a> to train decisions, and the <a href="/aim-trainer/">aim trainer</a> to combine reaction with targeting. Take a baseline today, apply the habits above, and re-test in a few weeks &mdash; the honest way to see what's trainable for you. For the fundamentals, read <a href="/guides/how-to-improve-reaction-time/">how to improve your reaction time</a>.</p>""",
    "faq": [
        ("Are reflexes genetic or trained?", "Both. Genetics and age set a soft ceiling on your fastest possible reaction, but training, prediction and your daily state decide how close to that ceiling you get."),
        ("Can you really get faster reflexes?", "You can lower your reaction time for specific tasks and become more consistent, and you can gain a lot from prediction. You can't train away the fixed nerve-conduction time."),
        ("What improves reflexes the most?", "Day to day, sleep and warming up beat drills. Over time, task-specific practice and learning to anticipate make the biggest lasting difference."),
        ("Do reflex gains transfer between tasks?", "Not much. Improvement is largely specific to what you practise, so train the reaction that matters to you rather than expecting broad carryover."),
    ],
    "related_tests": [g_ref("reaction"), g_ref("gonogo"), g_ref("aim"), g_ref("audio"),
                      {"slug": "stop-the-clock", "kbd": "Reaction", "name": "Stop the Clock", "desc": "Timing precision."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["how-to-improve-reaction-time", "how-to-improve-hand-eye-coordination"],
},
{
    "slug": "how-to-improve-working-memory",
    "crumb": "Improve working memory",
    "card_title": "How to improve working memory",
    "card_desc": "Chunking, habits, and techniques that actually stick.",
    "title": "How to Improve Working Memory: Techniques That Work | SpeedLab",
    "desc": "Working memory is how much you can hold in mind at once. Learn what it is, the honest limits of brain games, and chunking and lifestyle techniques that genuinely help.",
    "ld_desc": "A practical guide to working memory: what it is, its limits, and techniques like chunking that genuinely help.",
    "og_title": "How to Improve Working Memory",
    "og_desc": "Chunking, habits, and techniques that stick.",
    "og_image": "guide-memory.png",
    "h1": "How to improve working memory",
    "lead": "Working memory is the mental sticky-note where you hold a phone number, a mental sum, or the start of a sentence you're still finishing. It's limited for everyone &mdash; but you can use it far more effectively. Here's how.",
    "body": """      <p>Working memory is how much information you can actively hold and manipulate at once. The classic finding is that most people juggle around <strong>four to seven items</strong> before things start dropping &mdash; which is why phone numbers are the length they are. You can measure your own span on the <a href="/number-memory/">number memory test</a>. The honest headline: you can't dramatically expand the raw capacity, but you can get much more out of it.</p>

      <h2>The one technique that really works: chunking</h2>
      <p>Chunking groups individual items into larger meaningful units, so each &quot;slot&quot; holds more. The string 1 9 4 5 2 0 2 6 is eight items; read as 1945 and 2026 it's two. Phone numbers, card numbers and sort codes are all chunked for this reason. It's the single most powerful memory technique because it sidesteps the capacity limit instead of fighting it &mdash; and it's a skill that sharpens with practice. Try deliberately chunking the digits on <a href="/number-memory/">number memory</a> and watch your span jump.</p>

      <h2>Be honest about brain games</h2>
      <p>Memory games are a genuinely good way to <em>measure</em> and warm up working memory, and chunking practice on them transfers to real chunking. What they don't do is broadly raise your intelligence &mdash; the evidence for that kind of transfer is weak, as we cover in <a href="/guides/do-brain-training-games-work/">do brain-training games work</a>. Treat them as a benchmark and a workout, not a magic upgrade.</p>

      <h2>The habits that move the needle</h2>
      <ul>
        <li><strong>Sleep.</strong> Working memory is one of the first things to suffer when you're short on sleep, and one of the first to recover. Nothing on this list beats it.</li>
        <li><strong>Remove distraction.</strong> Most &quot;bad memory&quot; is divided attention &mdash; you never encoded the thing because you were half-focused. Single-tasking is a memory technique.</li>
        <li><strong>Exercise.</strong> Regular aerobic activity is among the best-supported things for overall cognitive function.</li>
        <li><strong>Offload deliberately.</strong> Write things down so your working memory is free for thinking, not storage. Using it for the right job matters as much as its size.</li>
      </ul>

      <h2>Train and track it</h2>
      <p>Use a couple of tests as your benchmark and revisit them: <a href="/number-memory/">number memory</a> for digit span, <a href="/sequence-memory/">sequence memory</a> for spatial working memory, and the <a href="/chimp-test/">chimp test</a> for holding positions under time pressure. Practise chunking on them deliberately, keep your sleep in check, and you'll get measurably more out of the memory you already have.</p>""",
    "faq": [
        ("How many things can working memory hold?", "Usually about four to seven items at once for most people. You can't expand that raw limit much, but chunking lets each item carry far more information."),
        ("What is chunking?", "Grouping individual items into larger meaningful units, like reading 1945 as one chunk instead of four digits. It's the most effective way to work around working-memory limits."),
        ("Do memory games improve working memory?", "They're good for measuring and warming it up, and chunking practice transfers. They don't broadly raise intelligence, so treat them as a benchmark and workout."),
        ("What helps memory the most day to day?", "Sleep and undivided attention. Most forgetting is really never having encoded the thing because you were distracted when it happened."),
    ],
    "related_tests": [g_ref("numbermem"), g_ref("seqmem"), g_ref("vismem"), g_ref("chimp"), g_ref("match"),
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every brain test."}],
    "related_guides": ["do-brain-training-games-work", "how-to-improve-hand-eye-coordination"],
},
{
    "slug": "gaming-warm-up-routine",
    "crumb": "Gaming warm-up routine",
    "card_title": "A 5-minute gaming warm-up",
    "card_desc": "Prime your reactions and aim before you queue up.",
    "title": "The 5-Minute Gaming Warm-Up Routine | SpeedLab",
    "desc": "Cold reactions are slow reactions. Here's a simple five-minute warm-up routine to prime your reaction time, aim and hands before you play, using quick free browser tests.",
    "ld_desc": "A five-minute gaming warm-up routine to prime reaction time, aim and hands before you play.",
    "og_title": "The 5-Minute Gaming Warm-Up",
    "og_desc": "Prime your reactions and aim before you queue up.",
    "og_image": "guide-warmup.png",
    "h1": "The 5-minute gaming warm-up routine",
    "lead": "Your first match is usually your worst, and it isn't bad luck &mdash; it's a cold start. A few focused minutes beforehand measurably sharpens your reactions, aim and hands. Here's a routine that fits in five.",
    "body": """      <p>Reaction time, aim and finger speed all start the session dull and sharpen once you're warmed up &mdash; the same way sprinters don't open with their fastest run. Warming up on purpose means you bring your match-two self to match one. This routine uses quick browser tests so you can do it in the thirty seconds before a queue pops, no download required.</p>

      <h2>The routine, minute by minute</h2>
      <ol>
        <li><strong>Minute 1 &mdash; wake up your reactions.</strong> Five rounds of the <a href="/reaction-time-test/">reaction time test</a>. Don't chase a record; just get your hand firing on the signal and shake off the lag.</li>
        <li><strong>Minute 2 &mdash; add a decision.</strong> One run of the <a href="/go-no-go/">Go / No-Go test</a>. Tapping on green and holding on red primes the act-or-wait judgement real games live on.</li>
        <li><strong>Minutes 3-4 &mdash; react and aim.</strong> A couple of rounds of the <a href="/aim-trainer/">aim trainer</a>. This is the closest thing to in-game flicking: spot, move, click, repeat.</li>
        <li><strong>Minute 5 &mdash; loosen the hands.</strong> A short burst on the <a href="/cps-test/">CPS test</a> or <a href="/key-press-test/">key press test</a> to get blood in your fingers, then a few deliberate stretches.</li>
      </ol>

      <h2>Why it works</h2>
      <p>Warming up doesn't make you permanently faster &mdash; it removes the cold-start penalty that costs you the opening minutes of a session. Your reactions, your targeting and your finger speed all have a &quot;ready&quot; state that takes a few minutes of activity to reach. Doing a little of each means none of them is the weak link when it counts.</p>

      <h2>Don't skip the basics</h2>
      <ul>
        <li><strong>Sleep and hydration</strong> set the ceiling the warm-up reaches for &mdash; no routine rescues a bad night.</li>
        <li><strong>Check your setup:</strong> a wired mouse and a high-refresh screen quietly save you more milliseconds than any drill. See <a href="/guides/reaction-time-in-gaming/">reaction time in gaming</a> for the details.</li>
        <li><strong>Stretch your wrists</strong> gently; warm hands cramp less and move faster over a long session.</li>
      </ol>

      <h2>Make it a habit</h2>
      <p>The routine only works if it's automatic, so keep the tabs bookmarked and run it every session until it's muscle memory. Track one number &mdash; your <a href="/reaction-time-test/">reaction time</a> average &mdash; so you can see yourself arrive warm. For the bigger picture, read <a href="/guides/can-you-train-your-reflexes/">can you train your reflexes</a> and <a href="/guides/how-to-improve-hand-eye-coordination/">how to improve hand-eye coordination</a>.</p>""",
    "faq": [
        ("Does warming up before gaming actually help?", "Yes. Reactions, aim and finger speed all start a session dull and sharpen with a few minutes of activity. Warming up removes that cold-start penalty so you don't waste your first match."),
        ("How long should a gaming warm-up be?", "About five minutes is plenty: a minute of reaction work, a decision drill, a couple of minutes of aim, and a short burst to loosen the hands."),
        ("What should I warm up with?", "Quick tasks that mirror the game: reaction, a Go/No-Go decision drill, aim training, and a short clicking or key-press burst for the hands."),
        ("Does warming up make me permanently faster?", "No. It removes the cold-start penalty for that session. Lasting gains come from sleep, setup and consistent practice over time."),
    ],
    "related_tests": [g_ref("reaction"), g_ref("gonogo"), g_ref("aim"), g_ref("cps"),
                      {"slug": "dino-game", "kbd": "Reaction", "name": "Dino Dash", "desc": "Reflex runner that speeds up."},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every reflex test."}],
    "related_guides": ["reaction-time-in-gaming", "how-to-improve-reaction-time"],
},
{
    "slug": "what-is-a-good-tapping-speed",
    "crumb": "What is a good tapping speed?",
    "card_title": "What is a good tapping speed?",
    "card_desc": "Average taps per second, and how to tap faster.",
    "title": "What Is a Good Tapping Speed? Average Taps Per Second | SpeedLab",
    "desc": "What's a good tapping speed? The average is about 6-7 taps per second with one finger. See the full ranges, how two-finger tapping compares, and how to tap faster.",
    "ld_desc": "The average tapping speed is around 6-7 taps per second; this guide explains the ranges and how to improve.",
    "og_title": "What Is a Good Tapping Speed?",
    "og_desc": "Average is 6-7 taps per second. Here's what's fast.",
    "og_image": "guide-tapping.png",
    "h1": "What is a good tapping speed?",
    "lead": "You took a tap speed test, got a taps-per-second number, and want to know if it's any good. Short answer: the average is around 6-7 with one finger. Here's the full picture and how to go faster.",
    "body": """      <p>If you've just hammered the <a href="/tap-speed-test/">tap speed test</a> and want to know where your number lands, here's the honest breakdown. Tapping speed is measured in <strong>taps per second (TPS)</strong>, and for most people it sits close to mouse-clicking speed &mdash; because it's the same motion on a touchscreen.</p>

      <h2>Average taps per second</h2>
      <p>On a standard test with one finger, here's a fair rule of thumb:</p>
      <ul>
        <li><strong>Under 4 TPS</strong> &mdash; a relaxed, everyday tap.</li>
        <li><strong>6 to 7.5 TPS</strong> &mdash; right around average; where most people land.</li>
        <li><strong>8 to 11 TPS</strong> &mdash; fast; you've clearly practised.</li>
        <li><strong>11+ TPS</strong> &mdash; very fast, and almost always two fingers rather than one.</li>
      </ul>
      <p>So if you're tapping 7 per second, you're bang on average. Cross 8 and you're quick; hold double digits and you're among the fastest.</p>

      <h2>One finger vs two</h2>
      <p>The single biggest jump in tapping speed isn't practice &mdash; it's technique. A single finger tops out around 7-8 TPS for most people because the muscle has to lift and drop in one rhythm. <strong>Two fingers (or two thumbs) alternating</strong>, like a tiny drum roll, lets one land while the other lifts, which can push you well past 10 TPS. It's the touchscreen version of butterfly clicking, and it's the fastest legitimate method for a raw score.</p>

      <h2>How the test length changes your score</h2>
      <p>Your peak burst is always faster than the pace you can hold. A short 5-second test rewards one explosive flurry and reads high; a 30 or 60-second run drags your average down toward the rate you can genuinely sustain. When you compare with a friend, make sure you're on the same length &mdash; a 9 TPS burst and a 6 TPS minute can come from the same thumbs.</p>

      <h2>How to tap faster</h2>
      <ul>
        <li><strong>Use two fingers or two thumbs,</strong> alternating them steadily rather than mashing.</li>
        <li><strong>Rest your device on a table</strong> so your hand is free to move instead of gripping.</li>
        <li><strong>Keep taps light and quick.</strong> Hard, tense taps are slower and tire you out fast.</li>
        <li><strong>Match effort to the clock</strong> &mdash; burst on short runs, settle into a rhythm on long ones.</li>
        <li><strong>Warm up.</strong> A couple of practice runs reliably adds a tap or two per second.</li>
      </ul>

      <h2>Tapping speed vs CPS</h2>
      <p>Tapping speed and clicks-per-second are the same measurement with different input: a finger on glass versus a mouse button. The numbers land in a similar range, so your tap TPS and your <a href="/guides/what-is-a-good-cps/">CPS</a> are usually close. If you play on a computer, the <a href="/cps-test/">CPS test</a> is the mouse equivalent and the <a href="/spacebar-clicker/">spacebar clicker</a> the keyboard one.</p>

      <h2>Test yourself</h2>
      <p>Take the <a href="/tap-speed-test/">tap speed test</a> a few times, try one finger then two, and keep your best &mdash; each length saves its own personal best on your device. Then see how your clicking compares with the <a href="/guides/how-to-click-faster/">how to click faster</a> guide.</p>""",
    "faq": [
        ("What is a good tapping speed?", "Around 6 to 7 taps per second with one finger is average. Above 8 is fast, and holding over 10 taps per second usually means using two fingers."),
        ("What is the average taps per second?", "About 6 to 7 taps per second for a single finger on a tap speed test. Two fingers alternating can reach well past 10."),
        ("How can I tap faster?", "Alternate two fingers or thumbs like a drum roll, rest your device on a surface, keep taps light and quick, and warm up first."),
        ("Is tapping speed the same as CPS?", "Essentially yes. It's the same measurement, just on a touchscreen instead of a mouse, so your taps-per-second and clicks-per-second are usually close."),
    ],
    "related_tests": [g_ref("tap"), g_ref("cps"), g_ref("spacebar"), g_ref("keypress"),
                      {"slug": "swipe-speed-test", "kbd": "Mobile", "name": "Swipe Speed Test", "desc": "How fast can you swipe?"},
                      {"slug": "all-tests", "kbd": "Browse", "name": "All Tests", "desc": "Every speed test."}],
    "related_guides": ["what-is-a-good-cps", "how-to-click-faster"],
},
]

# Resolve related_guides slugs -> tiles
_BY_SLUG = {g["slug"]: g for g in GUIDES}
def guide_tiles(slugs):
    out = []
    for s in slugs:
        g = _BY_SLUG[s]
        out.append({"slug": "guides/" + s, "kbd": "Guide", "name": g["card_title"], "desc": g["card_desc"]})
    return out


def main():
    # hub
    hubdir = os.path.join(ROOT, "guides")
    os.makedirs(hubdir, exist_ok=True)
    with open(os.path.join(hubdir, "index.html"), "w") as f:
        f.write(render_hub(GUIDES))
    print("wrote guides/index.html")
    # articles
    for g in GUIDES:
        gg = dict(g)
        gg["related_guides"] = guide_tiles(g["related_guides"])
        outdir = os.path.join(ROOT, "guides", g["slug"])
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w") as f:
            f.write(render_guide(gg))
        print("wrote guides/%s/index.html" % g["slug"])
    print("done (%d guides + hub)" % len(GUIDES))


if __name__ == "__main__":
    main()
