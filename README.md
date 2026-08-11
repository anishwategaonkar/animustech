# animustech.in

Static site, served by GitHub Pages from the repo root. Custom domain in `CNAME`.

## Layout

```
index.html                     homepage (hand-edited)
assets/site.css                all styles, shared by every page
assets/site.js                 nav, scroll reveal, progress bar
sitemap.xml  robots.txt        SEO
<slug>/index.html              generated landing pages — DO NOT EDIT BY HAND
_build.py                      page generator (template + schema)
pages_content.py               page copy — EDIT THIS
_tpl_header.html               header extracted from index.html
_tpl_footer.html               footer extracted from index.html
```

## Editing a landing page

Landing pages under `recruitment-agency-pune/`, `industries/` and `services/` are
generated. Editing them directly gets overwritten on the next build.

1. Edit the copy in `pages_content.py`
2. `python3 _build.py`
3. Commit both the source and the regenerated `index.html` files

## Adding a page

Add a dict to `PAGES` in `pages_content.py` (copy an existing one), run
`python3 _build.py`, then add the URL to `sitemap.xml`.

Only add a URL to the sitemap once the page is actually live — a sitemap
pointing at 404s damages crawl trust.

## Changing the header, footer or styles

Header and footer live in `index.html`. After changing either, refresh the
templates and rebuild, or the subpages will drift out of sync:

```bash
python3 - <<'EOF'
import re
src = open('index.html').read()
for name, pat in [('_tpl_header.html', r'(<header class="header".*?</header>)'),
                  ('_tpl_footer.html', r'(<footer class="footer">.*?</footer>)')]:
    block = re.search(pat, src, re.S).group(1)
    open(name, 'w').write(re.sub(r'href="#([a-z]+)"', r'href="/#\1"', block))
EOF
python3 _build.py
```

Styles are in `assets/site.css` and apply everywhere. Subpage-specific rules are
in the `SUBPAGE ADDITIONS` block at the bottom.

## Local preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000. Hard-refresh after CSS changes — the
stylesheet caches aggressively.

## Before this goes live

The `EmploymentAgency` schema in every page is missing a street address, phone
number and `sameAs` links. Local search ranking weights address specificity, so
fill these in `_build.py` (`org_schema`) and rebuild:

- `telephone`
- `address.streetAddress` and `postalCode`
- `sameAs` — LinkedIn company page, Google Business Profile
