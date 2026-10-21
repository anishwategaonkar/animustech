#!/usr/bin/env python3
"""
Builds /candidates/ , the candidate side of the site.

    python3 _build_candidates.py

HONESTY RULE, same as the rest of the site: describe only what exists.
Interview practice and mock interviews are deliberately NOT on this page. They
are not running yet. Add them when they launch, not before.
"""
import os, json, html

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
ORG_ID = SITE + "/#organization"
URL    = "/candidates/"

TITLE = "Jobs &amp; Careers | Animus Tech"
DESC  = ("Open roles across software, manufacturing and consumer companies in India. "
         "Every application is read by a person and you hear back either way.")

FAQ = [
 ("Will I actually hear back if I apply?",
  "Yes, either way. Silence is the standard in this industry and we think it should not be. "
  "If you are not right for a role we tell you, rather than leaving you wondering."),
 ("Is my application screened by software?",
  "Software narrows the field, but a recruiter reads every shortlist and no candidate is "
  "rejected by software alone. Your profile is read against a scorecard agreed with the "
  "hiring manager, not matched on keywords."),
 ("What if my CV does not use the right words?",
  "That is exactly the case the keyword approach gets wrong. If your experience fits the role "
  "but your CV does not use the expected words, we would still rather see it."),
 ("Do you charge candidates anything?",
  "No. Our fees are paid by the companies hiring. Applying, being screened and being put "
  "forward all cost you nothing."),
 ("There is nothing that fits me today. Is it worth applying?",
  "Send a speculative CV. We keep profiles against the mandates we take on and come back to "
  "you when something genuinely fits, rather than when we need to fill a quota."),
]

SCHEMAS = [
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": SITE + URL + "#webpage",
  "url": SITE + URL,
  "name": "Jobs and careers at Animus Tech",
  "description": ("Open roles across software, manufacturing and consumer companies in India, "
                  "with an application read by a person."),
  "about": {"@id": ORG_ID},
  "inLanguage": "en-IN",
},
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "For candidates"},
  ],
},
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
    for q, a in FAQ
  ],
},
]

EXTRA_CSS = """
<style>
.steps--cand{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:46px}
@media(max-width:900px){.steps--cand{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.steps--cand{grid-template-columns:1fr}}


@media(max-width:860px){


@media(max-width:760px){.promise{grid-template-columns:1fr}}
.promise div{padding-top:22px;border-top:1px solid var(--border)}
.promise h3{font-size:1.04rem;margin-bottom:8px}
.promise p{color:var(--text-2);font-size:.95rem;line-height:1.7}
.faqlist{max-width:780px;margin-top:40px}
.faqlist details{border-bottom:1px solid var(--border);padding:18px 0}
.faqlist summary{
  cursor:pointer;list-style:none;font-weight:600;color:var(--text);font-size:1.02rem;
  display:flex;justify-content:space-between;gap:20px;align-items:center;
}
.faqlist summary::-webkit-details-marker{display:none}
.faqlist summary::after{content:"+";color:var(--accent);font-weight:400;font-size:1.3rem;line-height:1}
.faqlist details[open] summary::after{content:"\\2013"}
.faqlist p{color:var(--text-2);line-height:1.75;margin-top:12px;font-size:.97rem}
</style>
"""

BODY = """
<section class="hero hero--sub hero--aud">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">For candidates</span>
    </nav>
    <span class="eyebrow">For candidates</span>
    <h1>A person reads your application. <span class="accent-text">And you hear back.</span></h1>
    <p class="hero__lead">
      We recruit for software, manufacturing and consumer companies across India. Software
      narrows the field, a recruiter decides, and you get an answer either way. That should not
      be unusual, and yet it is.
    </p>
    <div class="hero__cta">
      <a href="/jobs/" class="btn btn--primary">See open roles
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="#process" class="btn btn--ghost">How we screen</a>
    </div>
    <ul class="hero__meta">
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> Free for candidates, always</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> Never rejected by software alone</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> An answer either way</li>
    </ul>
  </div>
</section>

<!-- ============ WHAT HAPPENS ============ -->
<section class="section section--alt" id="process">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">What happens</span>
      <h2 class="section-title">Where your application actually goes</h2>
      <p class="section-lead">
        Most agencies will not tell you this part. Here is the whole of it.
      </p>
    </div>

    <div class="steps steps--cand">
      <div class="step reveal">
        <h3>You apply</h3>
        <p>
          A short form on the role itself. Name, experience, notice period, current and expected
          compensation, and why you think the role fits. Four minutes, not forty.
        </p>
      </div>
      <div class="step reveal">
        <h3>Read against a scorecard</h3>
        <p>
          The scorecard is agreed with the hiring manager before sourcing starts, so you are
          measured against the actual job rather than against a keyword list.
        </p>
      </div>
      <div class="step reveal">
        <h3>A recruiter decides</h3>
        <p>
          Software narrows the field. A person reviews every shortlist before it reaches the
          client, and nobody is rejected by software alone.
        </p>
      </div>
      <div class="step reveal">
        <h3>You get an answer</h3>
        <p>
          Shortlisted or not. If we put you forward we tell you what we said about you,
          reservations included, so you know what you are walking into.
        </p>
      </div>
    </div>

    <div class="promise">
      <div class="reveal">
        <h3>We will not waste your notice period</h3>
        <p>
          If we think the compensation band will not clear the market, or the role is not what
          the advert implies, you hear it from us before you start interviewing, not after you
          have resigned.
        </p>
      </div>
      <div class="reveal">
        <h3>Your CV does not get sprayed around</h3>
        <p>
          Your profile goes to the role you applied for. If we think another mandate fits you
          better, we ask first. It is your name on the document.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ============ OPEN ROLES ============ -->
<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Open roles</span>
      <h2 class="section-title">What we are hiring for right now</h2>
      <p class="section-lead">
        We only list roles we are actively recruiting for. If the list is short, that is because
        it is honest, not because we stopped updating it.
      </p>
      <p style="margin-top:26px">
        <a href="/jobs/" class="btn btn--primary">See open roles
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
      <p class="linkrow">
        Nothing fits today?
        <a href="mailto:anish@animustech.in?subject=Speculative%20application">Send us your CV anyway</a>
        and we will come back when something does.
      </p>
    </div>
  </div>
</section>

<!-- ============ FAQ ============ -->
<section class="section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Questions</span>
      <h2 class="section-title">The things candidates actually ask</h2>
    </div>
    <div class="faqlist reveal">
      __FAQ__
    </div>
  </div>
</section>

<!-- ============ CROSS LINK ============ -->
<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">The other side</span>
      <h2 class="section-title">Hiring, not job hunting?</h2>
      <p class="section-lead">
        We work with software, manufacturing and D2C companies across India, and we build
        custom software for operations led businesses.
      </p>
      <p style="margin-top:26px">
        <a href="/talent-acquisition/" class="btn btn--primary" data-set-aud="employer">Go to the employer side
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
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
    faq_html = "\n      ".join(
        f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>"
        for q, a in FAQ)
    schema_html = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>'
        % json.dumps(s, indent=2, ensure_ascii=False) for s in SCHEMAS)

    out = os.path.join(ROOT, "candidates")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w") as f:
        f.write(PAGE.format(
            title=html.escape(html.unescape(TITLE), quote=True),
            desc=html.escape(html.unescape(DESC), quote=True),
            site=SITE, url=URL, extra_css=EXTRA_CSS, schema=schema_html,
            header=HEADER, footer=FOOTER, body=BODY.replace("__FAQ__", faq_html)))
    print("wrote", URL + "index.html")
