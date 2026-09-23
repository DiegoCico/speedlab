#!/usr/bin/env python3
"""
SpeedLab page generator (standalone dev tool — NOT part of the served site).

Stamps out test pages from a shared shell so the head, header, CMP mount, ad
slots and footer stay identical across every test. Each test supplies only the
unique bits (SEO copy, the interactive "cabinet" markup, its scripts, the
written content, FAQ and related tiles).

Usage:  python3 build/gen.py            # regenerate every page in SPECS
        python3 build/gen.py cps-test   # regenerate just one

Run from the repo root. Specs live in build/specs/*.py (one dict named SPEC).
"""
import os, sys, json, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECDIR = os.path.join(ROOT, "build", "specs")
DOMAIN = "https://speedlab.lol"

# --------------------------------------------------------------------------- #
def esc(s): return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, separators=(",", ":")) + '\n</script>'

def software_ld(spec):
    return jsonld({
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": spec["name"], "applicationCategory": "GameApplication",
        "operatingSystem": "Any (web browser)", "url": f'{DOMAIN}/{spec["slug"]}/',
        "description": spec["ld_desc"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    })

def breadcrumb_ld(spec):
    items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
        {"@type": "ListItem", "position": 2, "name": "All Tests", "item": f"{DOMAIN}/all-tests/"},
    ]
    pos = 3
    parent = spec.get("parent")   # {"name","slug"} for variant pages
    if parent:
        items.append({"@type": "ListItem", "position": pos, "name": parent["name"],
                      "item": f'{DOMAIN}/{parent["slug"]}/'})
        pos += 1
    items.append({"@type": "ListItem", "position": pos, "name": spec["crumb"],
                  "item": f'{DOMAIN}/{spec["slug"]}/'})
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

def crumbs_html(spec):
    lis = ['<li><a href="/">Home</a></li>', '<li><a href="/all-tests/">All Tests</a></li>']
    parent = spec.get("parent")
    if parent:
        lis.append(f'<li><a href="/{parent["slug"]}/">{esc(parent["name"])}</a></li>')
    lis.append(f'<li aria-current="page">{esc(spec["crumb"])}</li>')
    return "\n        ".join(lis)

def faq_ld(spec):
    ents = [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in spec["faq"]]
    return jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents})

def faq_html(spec):
    rows = "\n".join(
        f'        <details>\n          <summary>{esc(q)}</summary>\n'
        f'          <p>{esc(a)}</p>\n        </details>' for q, a in spec["faq"])
    return f'      <div class="faq">\n{rows}\n      </div>'

def related_html(spec):
    tiles = []
    for r in spec["related"]:
        if r.get("slug"):
            tiles.append(
                f'        <a class="tile" href="/{r["slug"]}/"><span class="t-kbd">{esc(r["kbd"])}</span>'
                f'<span class="t-name">{esc(r["name"])}</span><span class="t-desc">{esc(r["desc"])}</span></a>')
        else:
            tiles.append(
                f'        <div class="tile soon"><span class="t-soon">Soon</span>'
                f'<span class="t-name">{esc(r["name"])}</span><span class="t-desc">{esc(r["desc"])}</span></div>')
    return "\n".join(tiles)

def scripts_html(spec):
    tags = ['<script src="/assets/js/engine.js?v=202609231820" defer></script>',
            '<script src="/assets/js/share-card.js?v=202609231820" defer></script>']
    for s in spec["scripts"]:
        tags.append(f'<script src="{s}?v=202609231820" defer></script>')
    return "\n".join(tags)

# --------------------------------------------------------------------------- #
SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{domain}/{slug}/">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1A1030">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2418545459143038" crossorigin="anonymous"></script>

<meta property="og:type" content="website">
<meta property="og:site_name" content="SpeedLab">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{domain}/{slug}/">
<meta property="og:image" content="{domain}/assets/img/og/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{domain}/assets/img/og/{og_image}">

<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/dseg7-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/base.css?v=202609231820">
<link rel="stylesheet" href="/assets/css/arcade.css?v=202609231820">

{software_ld}
{breadcrumb_ld}
{faq_ld}
</head>
<body>
<a class="skip-link" href="#{skip_target}">Skip to the test</a>

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

<main class="wrap layout">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb">
      <ol>
        {crumbs}
      </ol>
    </nav>

    <h1>{h1}</h1>
    <p class="lead">{lead}</p>

{cabinet}

    <div class="ad-slot" data-slot="content-top" aria-hidden="true"><!-- AdSense: paste unit here --></div>

    <div class="content">
{content}

      <h2>Frequently asked questions</h2>
{faq_html}
    </div>

    <div class="ad-slot" data-slot="content-bottom" aria-hidden="true"><!-- AdSense: paste unit here --></div>

    <section class="related" aria-label="Related tests">
      <h2>Related speed tests</h2>
      <div class="tile-grid">
{related}
      </div>
    </section>

    <div class="ad-slot" data-slot="footer" aria-hidden="true"><!-- AdSense: paste unit here --></div>
  </div>

  <aside class="sidebar-rail" aria-label="Advertisement">
    <div class="ad-slot" data-slot="sidebar" aria-hidden="true"><!-- AdSense: paste unit here --></div>
  </aside>
</main>

<footer class="site-footer">
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
          <a href="/spacebar-clicker/">Spacebar Clicker</a>
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

{scripts}
</body>
</html>
"""

def cabinet_counter(spec):
    """Build the interactive cabinet for a counter-style test from small fields."""
    c = spec["counter"]
    durs = c["durations"]
    default = c["default"]
    opts = "\n".join(
        f'        <button class="opt" data-dur="{d}" type="button" aria-pressed="{"true" if d == default else "false"}">'
        f'{("No timer" if d == 0 else str(d) + "s")}</button>' for d in durs)
    key_attr = f' data-key="{c["key"]}"' if c.get("input") == "key" else ""
    btn_attr = f' data-button="{c["button"]}"' if c.get("button") else ""
    timer_start = "&#8734;" if default == 0 else str(default)
    return f"""    <section class="cabinet" id="clicker"
      data-testid="{c['testid']}" data-input="{c.get('input','pointer')}"{key_attr}{btn_attr}
      data-durations="{','.join(str(d) for d in durs)}" data-default="{default}"
      data-name="{esc(c['name'])}" aria-label="{esc(spec['crumb'])}">
      <div class="marquee">{esc(c['marquee'])}</div>

      <div class="screen" id="screen">
        <div id="play" class="play">
          <div class="readout-row">
            <div class="readout">
              <div class="seg-wrap"><span class="seg-value tnum" id="clicks">0</span></div>
              <div class="readout-label">{esc(c['count_label'])}</div>
            </div>
            <div class="readout small">
              <div class="seg-wrap"><span class="seg-value tnum" id="timer">{timer_start}</span></div>
              <div class="readout-label">Seconds left</div>
            </div>
          </div>
          <div class="play-area">
            <button class="click-pad is-armed" id="pad" type="button" aria-describedby="c-help">
              <span data-pad-title>Start</span>
              <span class="hint" data-pad-hint>{esc(c['hint'])}</span>
            </button>
          </div>
        </div>
        <div class="result" id="result"></div>
      </div>

      <div style="text-align:center;margin-top:1rem">
        <button class="arcade-btn p1" id="restart" type="button" hidden>Reset</button>
      </div>

      <div class="seg-select" role="group" aria-label="Test duration" id="c-help">
{opts}
      </div>

      <div class="pb-strip">
        <span>Personal best <span class="pb-val" data-pb>&mdash;</span></span>
        <button data-clear type="button">Clear my scores</button>
      </div>
    </section>"""

def render(spec):
    if spec.get("kind") == "counter":
        spec = dict(spec)
        spec["cabinet"] = cabinet_counter(spec)
        spec["scripts"] = ["/assets/js/tests/clicker.js"]
    return SHELL.format(
        domain=DOMAIN, slug=spec["slug"],
        robots=spec.get("robots", "index,follow,max-image-preview:large"),
        title=esc(spec["title"]), desc=esc(spec["desc"]),
        og_title=esc(spec["og_title"]), og_desc=esc(spec["og_desc"]),
        og_image=spec["og_image"],
        software_ld=software_ld(spec), breadcrumb_ld=breadcrumb_ld(spec), faq_ld=faq_ld(spec),
        skip_target=spec.get("skip_target", "pad"),
        crumbs=crumbs_html(spec), h1=esc(spec["h1"]), lead=esc(spec["lead"]),
        cabinet=spec["cabinet"].rstrip("\n"),
        content=spec["content"].rstrip("\n"),
        faq_html=faq_html(spec), related=related_html(spec), scripts=scripts_html(spec),
    )

def load_specs():
    specs = {}
    if not os.path.isdir(SPECDIR):
        return specs
    for fn in sorted(os.listdir(SPECDIR)):
        if not fn.endswith(".py") or fn.startswith("_"):
            continue
        path = os.path.join(SPECDIR, fn)
        s = importlib.util.spec_from_file_location(fn[:-3], path)
        mod = importlib.util.module_from_spec(s)
        s.loader.exec_module(mod)
        specs[mod.SPEC["slug"]] = mod.SPEC
    return specs

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    specs = load_specs()
    if not specs:
        print("No specs found in build/specs/"); return
    count = 0
    for slug, spec in specs.items():
        if only and slug != only:
            continue
        outdir = os.path.join(ROOT, slug)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w") as f:
            f.write(render(spec))
        print("wrote", f"{slug}/index.html")
        count += 1
    print(f"done ({count} page{'s' if count != 1 else ''})")

if __name__ == "__main__":
    main()
