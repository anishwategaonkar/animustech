#!/usr/bin/env python3
"""
Generates the SEO landing pages for animustech.in.

Reads the shared header/footer extracted from index.html so every generated
page is visually identical to the homepage. Re-runnable: safe to edit the
PAGES dict below and run again.

    python3 _build.py
"""
import os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()

SITE = "https://animustech.in"

# ---------------------------------------------------------------- schema ----
ORG_ID = f"{SITE}/#organization"

def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": "EmploymentAgency",
        "@id": ORG_ID,
        "name": "Animus Tech",
        "alternateName": "Animus Tech Talent Acquisition",
        "description": ("AI enabled recruitment agency and talent acquisition firm in Pune. "
                        "AI powered sourcing, screening and assessment, combined with human "
                        "judgement on culture fit. Hiring for software, manufacturing and D2C companies."),
        "url": SITE + "/",
        "logo": f"{SITE}/logo-dark.svg",
        "image": f"{SITE}/og-image.png",
        "email": "animus@animustech.in",
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Pune",
            "addressRegion": "Maharashtra",
            "addressCountry": "IN",
        },
        "areaServed": [
            {"@type": "City", "name": "Pune"},
            {"@type": "City", "name": "Pimpri-Chinchwad"},
            {"@type": "Place", "name": "Chakan Industrial Area"},
            {"@type": "Place", "name": "Hinjewadi"},
            {"@type": "Place", "name": "Talegaon"},
            {"@type": "Place", "name": "Ranjangaon"},
            {"@type": "Country", "name": "India"},
        ],
        "knowsAbout": [
            "Recruitment", "Talent acquisition", "AI resume screening",
            "Executive search", "Volume hiring", "Manufacturing recruitment",
            "IT recruitment", "D2C recruitment", "Candidate assessment",
            "Culture fit interviewing",
        ],
        "sameAs": [
            "https://www.linkedin.com/company/animustechnologies",
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Recruitment services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n,
                 "url": f"{SITE}{u}"}}
                for n, u in [
                    ("Permanent recruitment", "/services/permanent-recruitment/"),
                    ("Leadership and executive search", "/services/executive-search/"),
                    ("Volume and project hiring", "/services/bulk-hiring/"),
                    ("AI candidate assessment", "/services/ai-candidate-assessment/"),
                    ("Hiring advisory", "/services/hiring-advisory/"),
                ]
            ],
        },
    }

def breadcrumbs(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            ({"@type": "ListItem", "position": i, "name": n, "item": SITE + u}
             if u else {"@type": "ListItem", "position": i, "name": n})
            for i, (n, u) in enumerate(crumbs, 1)
        ],
    }

def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }

def service_schema(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "name": name,
        "description": desc,
        "provider": {"@id": ORG_ID},
        "areaServed": {"@type": "City", "name": "Pune"},
        "url": SITE + url,
    }

# ------------------------------------------------------------- rendering ----
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
      <a href="/#contact" class="btn btn--primary">Tell us what you're hiring for
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="/#ai" class="btn btn--ghost">See how our AI works</a>
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
        <a href="/#contact" class="btn btn--primary">Start hiring with us
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

def crumb_html(crumbs):
    out = []
    for name, url in crumbs:
        if url:
            out.append(f'<a href="{url}">{name}</a>')
        else:
            out.append(f'<span aria-current="page">{name}</span>')
    return '<span class="crumbs__sep">/</span>'.join(out)

def render(p):
    schemas = [org_schema(), breadcrumbs(p["crumbs"])]
    if p.get("faq"):
        schemas.append(faq_schema(p["faq"]))
    if p.get("service"):
        schemas.append(service_schema(p["service"], p["desc"], p["url"]))
    schema_html = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>' % json.dumps(s, indent=2, ensure_ascii=False)
        for s in schemas
    )
    return PAGE.format(
        site=SITE, header=HEADER, footer=FOOTER, schema=schema_html,
        crumb_html=crumb_html(p["crumbs"]),
        title=html.escape(p["title"], quote=True),
        desc=html.escape(p["desc"], quote=True),
        url=p["url"], eyebrow=p["eyebrow"], h1=p["h1"], lead=p["lead"],
        body=p["body"],
        cta_title=p.get("cta_title", "Let's talk about the role"),
        cta_lead=p.get("cta_lead",
            "Tell us what you are hiring for and we will come back within one working day "
            "with a view on the market, a realistic timeline, and whether we are the right firm for it."),
    )

# ------------------------------------------------------------------ build ---
if __name__ == "__main__":
    from pages_content import PAGES
    for p in PAGES:
        out_dir = os.path.join(ROOT, p["url"].strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "index.html")
        with open(path, "w") as f:
            f.write(render(p))
        print("wrote", p["url"] + "index.html" if p["url"].endswith("/") else p["url"])
    print(f"\n{len(PAGES)} pages built.")
