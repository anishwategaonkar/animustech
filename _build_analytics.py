#!/usr/bin/env python3
"""
Injects the GA4 tag into the <head> of every page.

Kept out of the page templates on purpose: those templates are rendered with
str.format(), and the gtag snippet contains braces that would have to be
escaped in every one of them. This runs last instead, over the built output.

Idempotent, so it is safe to run repeatedly. Run it AFTER any other build
script, or just use _build_all.py which does the ordering for you.

    python3 _build_analytics.py
"""
import os, pathlib

ROOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
SNIPPET = (ROOT / "_tpl_analytics.html").read_text(encoding="utf-8").rstrip("\n")
MARKER = "googletagmanager.com/gtag/js"


def main():
    added = skipped = 0
    for p in sorted(ROOT.rglob("index.html")):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        html = p.read_text(encoding="utf-8")
        if MARKER in html:
            skipped += 1
            continue
        if "</head>" not in html:
            print("  ! no </head>, skipped:", p)
            continue
        p.write_text(html.replace("</head>", SNIPPET + "\n</head>", 1), encoding="utf-8")
        added += 1
    print(f"analytics: injected into {added} pages, {skipped} already had it")


if __name__ == "__main__":
    main()
