#!/usr/bin/env python3
"""
Generates the software arm's child pages under /software/.

Mirrors _build.py, but the calls to action point at the software enquiry form
(/software/#software-contact) rather than the hiring one, and the Service
schema is provided by the organisation as software development rather than
recruitment.

    python3 _build_software_pages.py
"""
import os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()

SITE = "https://animustech.in"
ORG_ID = f"{SITE}/#organization"

# Reuse the single source of truth for the organisation entity.
from _build import org_schema, breadcrumbs, faq_schema, crumb_html
from pages_content import sec, faq_html


def service_schema(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@type_note": None,
        "serviceType": name,
        "name": name,
        "description": desc,
        "provider": {"@id": ORG_ID},
        "areaServed": [
            {"@type": "Country", "name": "India"},
            {"@type": "City", "name": "Pune"},
        ],
        "url": SITE + url,
    }


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

{schema}
</head>
<body>

<div class="progress" aria-hidden="true"><div class="progress__bar" id="progressBar"></div></div>

{header}

<main id="top">

<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="glow glow--b" aria-hidden="true"></div>

  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="hero__lead">{lead}</p>
    <div class="hero__cta">
      <a href="/software/#software-contact" class="btn btn--primary">Tell us what you need built
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="/software/#what-we-built" class="btn btn--ghost">See what we have built</a>
    </div>
  </div>
</section>

{body}

<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Get in touch</span>
      <h2 class="section-title">{cta_title}</h2>
      <p class="section-lead">{cta_lead}</p>
      <p style="margin-top:26px">
        <a href="/software/#software-contact" class="btn btn--primary">Tell us what you need built
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
    </div>
  </div>
</section>

</main>

{footer}

<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def render(p):
    body = p["body"]
    if isinstance(body, (tuple, list)):
        body = "".join(body)
    # If the page declares FAQs but has not rendered them visibly, add the
    # section. Google requires FAQPage markup to match on-page content.
    if p.get("faq") and 'class="faq' not in body:
        body = body + sec("Common questions", "Questions we get asked", "",
                          faq_html(p["faq"]))

    schemas = [org_schema(), breadcrumbs(p["crumbs"])]
    if p.get("faq"):
        schemas.append(faq_schema(p["faq"]))
    if p.get("service"):
        s = service_schema(p["service"], p["desc"], p["url"])
        s.pop("@type_note", None)
        schemas.append(s)

    schema_html = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>' % json.dumps(s, indent=2, ensure_ascii=False)
        for s in schemas
    )
    return PAGE.format(
        site=SITE, header=HEADER, footer=FOOTER, schema=schema_html,
        crumb_html=crumb_html(p["crumbs"]),
        title=html.escape(html.unescape(p["title"]), quote=True),
        desc=html.escape(html.unescape(p["desc"]), quote=True),
        url=p["url"], eyebrow=p["eyebrow"], h1=p["h1"], lead=p["lead"],
        body=body,
        cta_title=p["cta_title"], cta_lead=p["cta_lead"],
    )


if __name__ == "__main__":
    from software_pages_content import PAGES
    for p in PAGES:
        out_dir = os.path.join(ROOT, p["url"].strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(render(p))
        print("wrote", p["url"] + "index.html")
    print(f"\n{len(PAGES)} software pages built.")
