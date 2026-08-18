#!/usr/bin/env python3
"""
ONE TIME migration: splits the old single homepage into

    /                      company level introduction + choose an arm
    /talent-acquisition/   the full recruitment site that used to live at /

Run once, check the output, then this file can be deleted. Kept in the repo so
the change is auditable rather than appearing as an unexplained rewrite.

    python3 _split_home.py
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = open(os.path.join(ROOT, "index.html")).read()

# --- pull the body sections out of the old homepage -------------------------
def section(html_id):
    """Return the <section ...id="X"> ... </section> block, comment included."""
    m = re.search(r'(<!-- =+ [A-Z ]+=+ -->\n)?(<section[^>]*id="%s".*?\n</section>)' % html_id,
                  SRC, re.S)
    if not m:
        raise SystemExit("could not find section id=%s" % html_id)
    return m.group(2)

HERO = re.search(r'<section class="hero">.*?\n</section>', SRC, re.S).group(0)
ABOUT      = section("about")
SERVICES   = section("services")
AI         = section("ai")
INDUSTRIES = section("industries")
APPROACH   = section("approach")
PROCESS    = section("process")
CONTACT    = section("contact")

HEADER = open(os.path.join(ROOT, "_tpl_header.html")).read()
FOOTER = open(os.path.join(ROOT, "_tpl_footer.html")).read()

FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' "
           "viewBox='0 0 54 40'><rect width='54' height='40' rx='7' fill='%23141824'/>"
           "<circle cx='19' cy='20' r='14' fill='none' stroke='%23dfb78e' stroke-width='3'/>"
           "<circle cx='35' cy='20' r='14' fill='none' stroke='%239d94e0' stroke-width='3'/></svg>\">")

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

def page(title, desc, url, schema, body, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://animustech.in{url}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://animustech.in{url}">
<meta property="og:image" content="https://animustech.in/og-image.png">

{FAVICON}

{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{extra_css}
{schema}
</head>
<body>

<div class="progress" aria-hidden="true"><div class="progress__bar" id="progressBar"></div></div>

{HEADER}

<main id="top">
{body}
</main>

{FOOTER}

<script src="/assets/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# 1. /talent-acquisition/  : everything the old homepage had, minus the chooser
# ---------------------------------------------------------------------------
TA_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://animustech.in/talent-acquisition/#service",
  "serviceType": "Talent acquisition and recruitment",
  "name": "AI enabled talent acquisition and recruitment",
  "description": "AI enabled recruitment and talent acquisition for software, manufacturing and D2C companies across India. AI powered sourcing, screening and assessment, with human judgement on culture fit.",
  "provider": { "@id": "https://animustech.in/#organization" },
  "areaServed": [
    { "@type": "City", "name": "Pune" },
    { "@type": "Country", "name": "India" }
  ],
  "url": "https://animustech.in/talent-acquisition/"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://animustech.in/" },
    { "@type": "ListItem", "position": 2, "name": "Talent acquisition" }
  ]
}
</script>"""

TA_BACKLINK = """
<div class="wrap" style="padding-top:118px">
  <nav class="crumbs" aria-label="Breadcrumb">
    <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Talent acquisition</span>
  </nav>
</div>
"""

TA_CROSSLINK = """
<!-- ============ CROSS LINK ============ -->
<section class="section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">The other half</span>
      <h2 class="section-title">Need software, not hiring?</h2>
      <p class="section-lead">
        We also build custom software for manufacturing and operations led businesses:
        project tracking, finance and invoicing, lead management and internal tools.
      </p>
      <p style="margin-top:26px">
        <a href="/software/" class="btn btn--primary">Go to software development
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
    </div>
  </div>
</section>
"""

# the old hero used bare "#contact" style anchors, which still resolve correctly
# on this page because all the target sections live here too.
ta_body = "\n".join([TA_BACKLINK, HERO, ABOUT, SERVICES, AI, INDUSTRIES,
                     APPROACH, PROCESS, CONTACT, TA_CROSSLINK])

os.makedirs(os.path.join(ROOT, "talent-acquisition"), exist_ok=True)
open(os.path.join(ROOT, "talent-acquisition", "index.html"), "w").write(
    page("AI Recruitment &amp; Talent Acquisition | Animus Tech",
         "AI enabled recruitment and talent acquisition for software, manufacturing and D2C companies across India.",
         "/talent-acquisition/", TA_SCHEMA, ta_body))
print("wrote /talent-acquisition/index.html")

# ---------------------------------------------------------------------------
# 2. /  : company level introduction, then choose an arm
# ---------------------------------------------------------------------------
# The organisation block is defined once, here, because every other page on the
# site references it by @id. It has to live on the canonical org URL.
import json as _json
from _build import org_schema

HOME_SCHEMA = ('<script type="application/ld+json">\n'
               + _json.dumps(org_schema(), indent=2, ensure_ascii=False)
               + '\n</script>\n' + """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://animustech.in/#website",
  "url": "https://animustech.in/",
  "name": "Animus Tech",
  "publisher": { "@id": "https://animustech.in/#organization" },
  "inLanguage": "en-IN"
}
</script>""")

HOME_BODY = """
<section class="hero">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="glow glow--b" aria-hidden="true"></div>

  <div class="wrap hero__inner">
    <span class="eyebrow">Pune, India</span>
    <h1>Understand the job first.<br><span class="accent-text">Then hire, or build.</span></h1>
    <h2 class="hero__kicker">Animus Tech runs two arms: AI enabled talent acquisition, and custom software for operations led businesses</h2>
    <p class="hero__lead">
      A bad hire and a bad system fail for the same reason. Somebody committed before
      anybody understood the work properly. Both halves of this company are built on
      refusing to do that, which is why we publish our own numbers rather than adjectives.
    </p>
    <div class="hero__cta">
      <a href="#choose" class="btn btn--primary">Choose where to start
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="#who-we-are" class="btn btn--ghost">Who we are</a>
    </div>
    <ul class="hero__meta">
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> We publish our own search data</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> A person signs off on every decision</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> We say no when it is not a fit</li>
    </ul>
  </div>
</section>

<!-- ============ CHOOSE ============ -->
<section class="section" id="choose">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Two things we do</span>
      <h2 class="section-title">What brought you here?</h2>
      <p class="section-lead">
        Pick the one you need. Each opens the full picture of how that side of the
        business works, including what we commit to and what we need from you.
      </p>
    </div>

    <div class="arms">
      <a class="arm reveal" href="/talent-acquisition/">
        <div class="arm__ico" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <h3>I am hiring</h3>
        <p>
          AI enabled recruitment and talent acquisition for software, manufacturing and
          D2C companies across India. Our AI sources and screens at a scale no manual team
          can match, then our recruiters judge the fit software still cannot.
        </p>
        <ul class="card__list">
          <li>Permanent, executive and volume hiring</li>
          <li>Short reasoned shortlists, not a stack of CVs</li>
          <li>Published submittal ratios and timelines</li>
        </ul>
        <span class="arm__cta">Go to talent acquisition
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </a>

      <a class="arm reveal" href="/software/">
        <div class="arm__ico" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>
        </div>
        <h3>I need software built</h3>
        <p>
          Custom software for manufacturing, small enterprises and other operations led
          businesses. The systems that usually live in a spreadsheet until the spreadsheet
          breaks, built around the process you already run.
        </p>
        <ul class="card__list">
          <li>Project and job tracking, multiple users</li>
          <li>Finance, invoicing and internal tools</li>
          <li>You own the code and the data</li>
        </ul>
        <span class="arm__cta">Go to software development
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </span>
      </a>
    </div>
  </div>
</section>

<!-- ============ WHO WE ARE ============ -->
<section class="section section--alt" id="who-we-are">
  <div class="wrap">
    <div class="reveal about__lead">
      <span class="eyebrow">About us</span>
      <h2 class="section-title">One company, two disciplines.</h2>
      <p>
        Animus Tech is based in Pune and works with companies across India. We started in
        talent acquisition, hiring for software, manufacturing and consumer businesses.
        Along the way we built the internal tools we needed to run our own operations, and
        found the same gaps sitting unaddressed in the businesses we were hiring for.
      </p>
      <p>
        So the company does two things now, and it does them the same way. We spend the
        time to understand how the work actually happens before we commit to a shortlist
        or a specification. That sounds obvious. It is also the step almost everybody skips,
        and it is where both bad hires and bad systems come from.
      </p>
      <p>
        <strong>What that looks like in practice:</strong> we publish our real search
        numbers, including the searches that ran long and why. We show two working software
        tools rather than a wall of logos. And we tell you early when something is not going
        to work, which is a cheaper conversation in week one than in month four.
      </p>
    </div>

    <div class="benefits">
      <div class="benefit reveal">
        <h3>We show the numbers</h3>
        <p>
          Submittal ratios, timelines, the searches that went long. Anyone can claim
          quality. Very few will show you the arithmetic behind the claim.
        </p>
      </div>
      <div class="benefit reveal">
        <h3>A person decides</h3>
        <p>
          Software narrows the field on both sides of the business. A person signs off
          before anything reaches you, and nobody is rejected by software alone.
        </p>
      </div>
      <div class="benefit reveal">
        <h3>We tell you early</h3>
        <p>
          If the compensation band will not clear the market, or the build is the wrong
          answer to your problem, you hear it in week one rather than week six.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ============ WHERE NEXT ============ -->
<section class="section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Where next</span>
      <h2 class="section-title">Still deciding?</h2>
      <p class="section-lead">
        These read well regardless of which side of the business you came for.
      </p>
      <p class="linkrow" style="margin-top:22px">
        <a href="/how-we-work/">How we work, and the numbers behind it</a> ·
        <a href="/blog/">Blog</a> ·
        <a href="/jobs/">Open roles</a> ·
        <a href="/tools/cost-of-a-bad-hire-calculator/">Cost of a bad hire calculator</a>
      </p>
    </div>
  </div>
</section>
"""

open(os.path.join(ROOT, "index.html"), "w").write(
    page("Animus Tech | Talent Acquisition &amp; Software Development, Pune",
         "Animus Tech runs two arms from Pune: AI enabled talent acquisition, and custom software for manufacturing and small enterprises.",
         "/", HOME_SCHEMA, HOME_BODY))
print("wrote /index.html")
