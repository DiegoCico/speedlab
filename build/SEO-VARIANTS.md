# SEO Variant-Page Plan

Some tests are searched by a **specific duration or mode** ("cps test 5 second",
"1 minute typing test", "spacebar counter 1 minute"). Google ranks *pages*, not
in-page buttons, so each high-demand variant gets its **own URL, `<title>`, `<h1>`,
meta description, and self-referencing canonical**, all cross-linked into a small
cluster. This is the same "one keyword = one page" rule the whole site follows.

Variants are stamped from a template by `build/gen-variants.py` (standalone dev
tool, not a build dependency) so they are never hand-maintained.

## Rules for every variant page

- URL: `/<test>/<duration>/` — lowercase, hyphenated, trailing slash, never changes.
- Unique `<title>` (≤ 60 chars) built around the exact phrase, e.g.
  `CPS Test — 10 Second Click Speed Test`.
- Unique meta description (150–160 chars) written for the click.
- Exactly one `<h1>` containing the phrase, e.g. `10 Second CPS Test`.
- Self canonical (`https://speedlab.lol/<test>/<duration>/`).
- 4-level `BreadcrumbList`: Home › All Tests › <Test> › <Duration>.
- `SoftwareApplication` + `FAQPage` JSON-LD.
- The test loads **locked to that duration** (no click needed).
- Duration selector rendered as **crawlable `<a>` links** to sibling variants,
  active one marked — this is the internal-linking cluster.
- A **differentiated intro paragraph** per duration (what that length is good for,
  a good score for *that* length) so pages are not thin duplicates.
- Added to `sitemap.xml` and reachable from the hub page + `/all-tests/`.

## Rollout by priority (search demand)

### 1. CPS Test — BUILD FIRST (done in this pass)
Hub `/cps-test/` stays the general page (defaults 5s). Variants:
`/cps-test/{1,2,5,10,15,20,30,60,100}-second/` (9 pages).
Highest-demand: 5-second, 10-second, 1-second, 100-second.

### 2. Typing Speed Test — HIGH VALUE
Phrasing is minutes, not seconds ("1 minute typing test" is the big one).
Plan: `/typing-speed-test/{1-minute,3-minute,5-minute,30-second,15-second}/`.
Requires extending the typing module's duration list to include 60/180/300s.

### 3. Spacebar Clicker — MEDIUM-HIGH
`/spacebar-clicker/{5,10,30,60,100}-second/` plus a `/1-minute/` alias page for 60s
(people search "spacebar counter 1 minute"). Reuses the same clicker module.

### 4. Tap Speed Test — LOW-MEDIUM (optional)
`/tap-speed-test/{5,10}-second/`.

## Not getting variants (no per-duration/mode search demand)
Reaction Time, Audio Reaction, Aim Trainer, Whack-a-Mole, Color Match, Key Press,
Alphabet/Number typing, the memory suite, Scroll/Swipe/Emoji. These already target
their single best keyword; extra URLs would only dilute them.

## "1 minute" vs "60 second"
Both are searched. Pick ONE canonical slug per test to avoid duplicates:
- CPS: `60-second` (the CPS community phrasing).
- Typing / Spacebar: `1-minute` (natural phrasing, higher volume there).
Do not create both `/60-second/` and `/1-minute/` for the same test.
