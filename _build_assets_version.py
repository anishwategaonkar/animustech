#!/usr/bin/env python3
"""
Stamps a content hash onto the stylesheet and script URLs in every page.

GitHub Pages serves assets with `cache-control: max-age=600`, so for ten
minutes after a deploy a returning visitor can be handed fresh HTML against a
stale site.css or site.js. That mismatch is worse than either file being old on
its own: new markup styled by old CSS, or new classes with no script to drive
them. It has caught us out several times, always looking like a bug in the
change rather than a caching artefact.

Appending ?v=<hash of the file> makes the URL change whenever the file changes,
so the browser is forced to refetch, and stays cached when it has not.

Idempotent: an existing ?v= is stripped before the new one goes on, so running
this twice does not stack query strings.

Run via _build_all.py, which handles the ordering. It has to come after every
page is written and before nothing in particular.

    python3 _build_assets_version.py
"""
import hashlib
import os
import pathlib
import re

ROOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
ASSETS = ["assets/site.css", "assets/site.js"]


def short_hash(path):
    return hashlib.md5(path.read_bytes()).hexdigest()[:8]


def main():
    versions = {}
    for rel in ASSETS:
        p = ROOT / rel
        if not p.exists():
            print("  ! missing, skipped:", rel)
            continue
        versions["/" + rel] = short_hash(p)

    if not versions:
        print("assets version: nothing to stamp")
        return

    # matches /assets/site.css or /assets/site.js plus any ?v= already there
    pattern = re.compile(
        r'(/assets/site\.(?:css|js))(\?v=[0-9a-f]+)?'
    )

    def swap(m):
        base = m.group(1)
        v = versions.get(base)
        return base + ("?v=" + v if v else "")

    touched = 0
    for p in sorted(ROOT.rglob("index.html")):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        html = p.read_text(encoding="utf-8")
        new = pattern.sub(swap, html)
        if new != html:
            p.write_text(new, encoding="utf-8")
            touched += 1

    print("assets version: stamped {} page(s) with {}".format(
        touched, ", ".join(k.rsplit("/", 1)[-1] + "=" + v
                           for k, v in sorted(versions.items()))))


if __name__ == "__main__":
    main()
