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
