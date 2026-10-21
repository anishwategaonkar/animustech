#!/usr/bin/env python3
"""
Builds /start/ , the second step: which of the two arms the visitor needs.

The homepage pitches the company and both verticals. This page is where a
client commits to one of them. Candidates are offered a way out here too,
because some of them will have come through the client facing homepage.

    python3 _build_start.py
"""
import os, json, html

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
ORG_ID = SITE + "/#organization"
URL    = "/start/"

TITLE = "Where to Start | Animus Tech"
DESC  = ("Talent acquisition or custom software development. Pick the arm you need "
         "and get straight into the detail.")

SCHEMAS = [
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": SITE + URL + "#webpage",
  "url": SITE + URL,
  "name": "Where to start with Animus Tech",
  "description": DESC,
  "about": {"@id": ORG_ID},
  "inLanguage": "en-IN",
},
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Where to start"},
  ],
},
]

EXTRA_CSS = ""

BODY = """
<section class="hero hero--sub hero--aud">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>

  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a> <span aria-hidden="true">/</span> <span>Where to start</span>
    </nav>
    <h1>What brought you here?</h1>
    <p class="hero__lead">
      Two arms, run to the same standard. Pick the one you need and we will get
      straight into the detail rather than the brochure.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="arms">
      <a class="arm reveal" href="/talent-acquisition/" data-set-aud="employer">
        <div class="arm__ico" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <h3>I am hiring</h3>
        <p>
          AI enabled recruitment for software, manufacturing and D2C companies across
          India. Our AI sources and screens at a scale no manual team can match, then
          our recruiters judge the fit software still cannot.
        </p>
        <ul class="card__list">
          <li>Permanent, executive and volume hiring</li>
          <li>Short reasoned shortlists, not a stack of CVs</li>
          <li>Published submittal ratios and timelines</li>
        </ul>
        <span class="arm__cta">Talent acquisition
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </a>

      <a class="arm reveal" href="/software/" data-set-aud="employer">
        <div class="arm__ico" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>
        </div>
        <h3>I want to build a system</h3>
        <p>
          Custom software for manufacturing, small enterprises and other operations led
          businesses. The systems that usually live in a spreadsheet until the
          spreadsheet breaks, built around the process you already run.
        </p>
        <ul class="card__list">
          <li>Lead management, job tracking, internal tools</li>
          <li>Built around your process, not a template</li>
          <li>You own the code and the data</li>
        </ul>
        <span class="arm__cta">Software development
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </a>
    </div>

    <div class="candidateband reveal" style="margin-top:56px">
      <div>
        <span class="eyebrow">Neither of those</span>
        <h2 class="section-title" style="font-size:1.5rem;margin-bottom:12px">You are looking for a job</h2>
        <p style="color:var(--text-2);line-height:1.75;max-width:560px">
          We list only the roles we are actively recruiting for. A recruiter reads every
          application and you hear back either way.
        </p>
      </div>
      <a href="/candidates/" class="btn btn--primary" data-set-aud="candidate">For candidates
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
    </div>
  </div>
</section>
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}{url}">
<meta property="og:image" content="{site}/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 54 40'><rect width='54' height='40' rx='7' fill='%23141824'/><circle cx='19' cy='20' r='14' fill='none' stroke='%23dfb78e' stroke-width='3'/><circle cx='35' cy='20' r='14' fill='none' stroke='%239d94e0' stroke-width='3'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra_css}
{schema}
</head>
<body>
<div class="progress" aria-hidden="true"><div class="progress__bar" id="progressBar"></div></div>
{header}
<main id="top">
{body}
</main>
{footer}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    schema_html = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>'
        % json.dumps(s, indent=2, ensure_ascii=False) for s in SCHEMAS)

    out = os.path.join(ROOT, "start")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w") as f:
        f.write(PAGE.format(
            title=html.escape(html.unescape(TITLE), quote=True),
            desc=html.escape(html.unescape(DESC), quote=True),
            site=SITE, url=URL, extra_css=EXTRA_CSS, schema=schema_html,
            header=HEADER, footer=FOOTER, body=BODY))
    print("wrote", URL + "index.html")
