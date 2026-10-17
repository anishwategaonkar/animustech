#!/usr/bin/env python3
"""
Injects the theme boot script into the <head> of every page.

This has to run before first paint, otherwise a visitor who chose the dark
theme gets a white flash on every navigation. It is deliberately tiny and
inline for that reason: an external file would be fetched too late.

Light is the default. Dark only applies if the visitor asked for it.

Idempotent. Run via _build_all.py, which handles the ordering.

    python3 _build_theme_boot.py
"""
import os, pathlib

ROOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
MARKER = "at-theme"

SNIPPET = """<script>
(function(){try{
  if(localStorage.getItem('at-theme')==='dark')
    document.documentElement.setAttribute('data-theme','dark');
}catch(e){}})();
</script>"""


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
    print(f"theme boot: injected into {added} pages, {skipped} already had it")


if __name__ == "__main__":
    main()
