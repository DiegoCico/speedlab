#!/usr/bin/env python3
"""
SpeedLab OG social-card generator (standalone dev tool — NOT part of the site).

Draws 1200x630 Open Graph cards in the arcade style: pink SPEEDLAB pill, big
title, subtitle, and an amber 7-segment value on a dark screen panel. It reads
the site's own self-hosted fonts (assets/fonts/*.woff2) and converts them to TTF
at runtime with fontTools, so it needs no external font downloads — just Pillow,
fontTools and brotli in the Python environment.

Usage:  python build/make-og.py            # regenerate the cards defined below
Output: assets/img/og/<name>.png
"""
import os, tempfile
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "og")
os.makedirs(OUT, exist_ok=True)

C = dict(bg="#1A1030", dot="#241640", screen="#0B0716", scan="#15112b",
         ink="#F6F1FF", dim="#A99FC7", amber="#FFC531", line="#000000", p1="#FF3D7F")

# --- fonts: convert the repo's woff2 to ttf so Pillow can use them ---------- #
_tmp = tempfile.mkdtemp(prefix="speedlab-og-")
def _woff2ttf(rel):
    src = os.path.join(ROOT, rel)
    out = os.path.join(_tmp, os.path.basename(rel).replace(".woff2", ".ttf"))
    f = TTFont(src); f.flavor = None; f.save(out); return out
ARCHIVO = _woff2ttf("assets/fonts/archivo-var.woff2")
DSEG = _woff2ttf("assets/fonts/dseg7-bold.woff2")

def archivo(size, weight=900):
    f = ImageFont.truetype(ARCHIVO, size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f
def dseg(size): return ImageFont.truetype(DSEG, size)

def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f); return b[2] - b[0], b[3] - b[1], b

def rounded(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

# --------------------------------------------------------------------------- #
def make(name, title, subtitle, value, label=""):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), C["bg"])
    d = ImageDraw.Draw(img)

    # dot texture
    for y in range(0, H, 40):
        for x in range(0, W, 40):
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=C["dot"])
    # outer frame
    d.rectangle([16, 16, W - 17, H - 17], outline=C["line"], width=12)

    # marquee pill
    wm = archivo(52, 900)
    tW, tH, tb = tw(d, "SPEEDLAB", wm)
    px0, py0 = 60, 54
    pill = [px0, py0, px0 + tW + 52, py0 + tH + 34]
    rounded(d, [pill[0] - 6, pill[1] - 6, pill[2] + 6, pill[3] + 6], 18, fill=C["line"])
    rounded(d, pill, 14, fill=C["p1"])
    d.text((pill[0] + 26 - tb[0], pill[1] + 17 - tb[1]), "SPEEDLAB", font=wm, fill=C["line"])

    # screen panel (right)
    sx0, sy0, sx1, sy1 = 712, 170, 1150, 482
    rounded(d, [sx0 - 6, sy0 - 6, sx1 + 6, sy1 + 6], 26, fill=C["line"])
    rounded(d, [sx0, sy0, sx1, sy1], 20, fill=C["screen"])
    scan = Image.new("RGB", (sx1 - sx0 - 8, sy1 - sy0 - 8), C["screen"])
    sd = ImageDraw.Draw(scan)
    for yy in range(0, scan.height, 6):
        sd.line([(0, yy), (scan.width, yy)], fill=C["scan"], width=2)
    img.paste(scan, (sx0 + 4, sy0 + 4))
    d = ImageDraw.Draw(img)

    # value (auto-fit to the panel)
    inner_w, inner_h = (sx1 - sx0) - 80, (sy1 - sy0) - (110 if label else 70)
    size = 210
    while size > 40:
        vf = dseg(size); vW, vH, vb = tw(d, value, vf)
        if vW <= inner_w and vH <= inner_h: break
        size -= 6
    vf = dseg(size); vW, vH, vb = tw(d, value, vf)
    cx = (sx0 + sx1) / 2
    vy = (sy0 + sy1) / 2 - vH / 2 - vb[1] - (18 if label else 0)
    d.text((cx - vW / 2 - vb[0], vy), value, font=vf, fill=C["amber"])
    if label:
        lf = archivo(30, 800); lW, lH, lb = tw(d, label, lf)
        d.text((cx - lW / 2 - lb[0], sy1 - 66), label, font=lf, fill=C["dim"])

    # title (1-2 lines, auto-shrink to the left column)
    maxw = sx0 - 80 - 40
    ty = 200 if len(title) == 1 else 188
    base = 118 if len(title) == 1 else 96
    for line in title:
        size = base
        while size > 44:
            f = archivo(size, 900)
            if tw(d, line, f)[0] <= maxw: break
            size -= 4
        f = archivo(size, 900); _, _, b = tw(d, line, f)
        d.text((80 - b[0], ty), line, font=f, fill=C["ink"])
        ty += (130 if len(title) == 1 else 104)

    # subtitle
    sf = archivo(34, 800)
    _, _, sb = tw(d, subtitle, sf)
    d.text((80 - sb[0], ty + 6), subtitle, font=sf, fill=C["dim"])

    # footer wordmark
    ff = archivo(44, 900)
    fx, fy = 80, H - 96
    _, _, wb = tw(d, "speedlab", ff)
    d.text((fx - wb[0], fy), "speedlab", font=ff, fill=C["ink"])
    ww = tw(d, "speedlab", ff)[0]
    _, _, lb2 = tw(d, ".lol", ff)
    d.text((fx + ww + 2 - lb2[0], fy), ".lol", font=ff, fill=C["amber"])

    path = os.path.join(OUT, name)
    img.save(path)
    print("wrote", path, os.path.getsize(path), "bytes")

# --------------------------------------------------------------------------- #
CARDS = [
    ("2048.png", ["2048"], "Slide, merge, reach 2048", "2048", ""),
    ("clusters.png", ["CLUSTERS"], "Sort 16 words into 4 groups", "16", ""),
    ("word-spammer.png", ["WORD", "SPAMMER"], "Type your word as fast as you can", "150", "WPM"),
]

def main():
    for c in CARDS:
        make(*c)
    print("done (%d cards)" % len(CARDS))

if __name__ == "__main__":
    main()
