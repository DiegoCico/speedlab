#!/usr/bin/env python3
"""
SpeedLab cache-bust stamper (standalone dev tool — NOT part of the served site).

Rewrites the ?v=... token on every CSS/JS asset reference to a fresh value,
across every HTML page and the generator's shell. Run this before each deploy
whenever CSS or JS changed, so returning visitors always fetch the new files
instead of a stale cached copy.

Usage:  python3 build/stamp.py
"""
import re, glob, os, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = time.strftime("%Y%m%d%H%M")   # e.g. 202609132150

def bump(path):
    with open(path) as f:
        s = f.read()
    if "?v=" not in s:
        return False
    s2 = re.sub(r'\?v=[0-9A-Za-z]+', "?v=" + VER, s)
    if s2 != s:
        with open(path, "w") as f:
            f.write(s2)
        return True
    return False

def main():
    n = 0
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        if os.sep + "build" + os.sep in f:
            continue
        if bump(f):
            n += 1
    for tool in ("gen.py", "gen-guides.py"):
        bump(os.path.join(ROOT, "build", tool))
    print("stamped %d HTML files + generators to ?v=%s" % (n, VER))

if __name__ == "__main__":
    main()
