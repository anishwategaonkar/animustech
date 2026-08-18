#!/usr/bin/env python3
"""
Re-injects the shared header and footer into the two hand written pages,
/ and /talent-acquisition/, so they never drift from the generated pages.

    python3 _build_static.py

Run this whenever _tpl_header.html or _tpl_footer.html changes. Everything
else on the site is generated and picks the templates up automatically.
"""
import os, re, json

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, "_tpl_header.html")).read().rstrip("\n")
FOOTER = open(os.path.join(ROOT, "_tpl_footer.html")).read().rstrip("\n")

from _build import org_schema

PAGES = ["index.html", "talent-acquisition/index.html"]

for rel in PAGES:
    path = os.path.join(ROOT, rel)
    s = open(path).read()
    new = re.sub(r'<header class="header".*?</header>', lambda m: HEADER, s, count=1, flags=re.S)
    new = re.sub(r'<footer class="footer".*?</footer>', lambda m: FOOTER, new, count=1, flags=re.S)
    if new == s:
        print("unchanged", rel)
    else:
        open(path, "w").write(new)
        print("refreshed", rel)

# The organisation block is defined once in _build.py and lives on the homepage,
# because every other page references it by @id. Keep the copy here in sync.
path = os.path.join(ROOT, "index.html")
s = open(path).read()
block = ('<script type="application/ld+json">\n'
         + json.dumps(org_schema(), indent=2, ensure_ascii=False)
         + '\n</script>')
new = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*'
             r'"@type": "EmploymentAgency".*?</script>',
             lambda m: block, s, count=1, flags=re.S)
if new != s:
    open(path, "w").write(new)
    print("synced organisation schema on /")
else:
    print("organisation schema already current")
