#!/usr/bin/env python3
"""
Ensures every page carries the Organization entity.

Several generators (blog, jobs, contact, tools, the software hub) emit Service
or BlogPosting markup that references the organisation by @id, but never define
that organisation on the page. A reference with nothing to resolve to is a
dangling node: Google sees the service but not the business providing it.

This walks the built output and injects the org JSON-LD wherever it is missing.
Idempotent. Runs from _build_all.py, before the analytics injection.

    python3 _build_org_schema.py
"""
import json, os, pathlib

from _build import org_schema, ORG_ID

ROOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

BLOCK = ('<script type="application/ld+json">\n'
         + json.dumps(org_schema(), indent=2, ensure_ascii=False)
         + '\n</script>')


def defines_org(html):
    """True only if a page carries the full entity, not just a reference to it.

    Blog posts and job pages contain a `publisher` node named Animus Tech and a
    provider referencing the org @id, so a plain substring check reports a false
    positive on both. The entity itself is the node that has the @id AND the
    real business fields hanging off it.
    """
    import re as _re
    for block in _re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                             html, _re.S):
        try:
            data = json.loads(block)
        except Exception:
            continue
        found = []

        def walk(node):
            if isinstance(node, dict):
                if node.get("@id") == ORG_ID and "address" in node:
                    found.append(node)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(data)
        if found:
            return True
    return False


def main():
    added = skipped = 0
    for p in sorted(ROOT.rglob("index.html")):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        html = p.read_text(encoding="utf-8")
        if defines_org(html):
            skipped += 1
            continue
        if "</head>" not in html:
            print("  ! no </head>, skipped:", p)
            continue
        p.write_text(html.replace("</head>", BLOCK + "\n</head>", 1), encoding="utf-8")
        added += 1
        print("  + org schema:", "/" + str(p.parent.relative_to(ROOT)).strip("."))
    print(f"organization: added to {added} pages, {skipped} already had it")


if __name__ == "__main__":
    main()
