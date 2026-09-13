# SpeedLab

Short, addictive speed & reflex tests — click speed, reaction time, memory, typing.
Live at **https://speedlab.lol**.

## Principles

- **Vanilla HTML/CSS/JS only.** No framework, no build step, no npm, no bundler.
- **No backend, no database, no external requests.** Everything runs client-side and works offline after first load. Fonts are self-hosted.
- **No tracking.** Scores and settings are stored in `localStorage`. No accounts, no forms, no analytics, no cookies.
- **One test = one page = one URL = one keyword.** Each test is playable above the fold with zero clicks to start.

## Hosting (GitHub Pages)

Served from the `main` branch root at the custom domain `speedlab.lol`.

- `.nojekyll` — stops Jekyll from touching the site.
- `CNAME` — the custom domain (`speedlab.lol`, apex, no www).
- All internal links and asset paths are **root-relative** (`/cps-test/`, `/assets/css/base.css`).
- Canonicals, OpenGraph URLs, and `sitemap.xml` all use `https://speedlab.lol`.
- Turn on **Enforce HTTPS** in repo settings once DNS resolves.
- Cache-bust CSS/JS with a query string (`base.css?v=2`) when shipping changes.

## Structure

```
/.nojekyll  /CNAME  /robots.txt  /sitemap.xml  /404.html
/cps-test/index.html            ← flagship test
/about/  /privacy/  /terms/  /contact/
/assets/css/base.css            ← tokens, layout, content, ad slots
/assets/css/arcade.css          ← cabinet, CRT screen, segmented display, motion
/assets/js/engine.js            ← config, storage, ranks, percentiles, sound, counter-test harness, results
/assets/js/share-card.js        ← canvas result image
/assets/js/site.js              ← shared header wiring (non-test pages)
/assets/js/tests/cps.js         ← CPS test config
/assets/fonts/                  ← Archivo (OFL) + DSEG7 (OFL), self-hosted
/assets/img/                    ← favicon + OG social images
```

## Adding a test

Most "count events in a time window" tests (CPS, spacebar, tap, jitter, butterfly,
kohi, key-press) are a small config passed to `SPEEDLAB.counterTest(...)`. Add a
percentile/rank entry in `SPEEDLAB.config` (engine.js), write a page from the
CPS template, and link it from `/all-tests/` and related-tests blocks.

## Local preview

```
python3 -m http.server 8000
# open http://localhost:8000/cps-test/
```

## Fonts

- **Archivo** — UI/headings/body. SIL OFL. See `assets/fonts/Archivo-OFL.txt`.
- **DSEG7 Classic** — the seven-segment live readout only. SIL OFL. See `assets/fonts/DSEG-LICENSE.txt`.
