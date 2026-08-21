#!/usr/bin/env python3
"""
Builds /contact/ , the one canonical contact URL for the whole company.

    python3 _build_contact.py

Exists so there is a single address to put on directory listings, the Google
Business Profile and outreach emails, rather than pointing people at an anchor
part way down another page.

Routes the three kinds of enquiry (hiring, software, candidates) from one place.
"""
import os, json, html

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
ORG_ID = SITE + "/#organization"
URL    = "/contact/"

TITLE = "Contact Animus Tech | Hiring &amp; Software Enquiries"
DESC  = ("Contact Animus Tech for recruitment or custom software. Email admin@animustech.in, "
         "call +91 94225 15047, or send an enquiry. We reply within one working day.")

SCHEMAS = [
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "@id": SITE + URL + "#contactpage",
  "url": SITE + URL,
  "name": "Contact Animus Tech",
  "description": "Contact details and enquiry form for Animus Tech.",
  "about": {"@id": ORG_ID},
  "inLanguage": "en-IN",
},
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Contact"},
  ],
},
]

EXTRA_CSS = """
<style>
.routecards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:44px 0 8px}
@media(max-width:900px){.routecards{grid-template-columns:1fr}}
.routecard{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:24px 26px}
.routecard h3{font-size:1.05rem;margin-bottom:9px;color:var(--text)}
.routecard p{color:var(--text-2);font-size:.93rem;line-height:1.7;margin-bottom:14px}
.routecard a{color:var(--accent);font-size:.9rem;font-weight:600}
</style>
"""

BODY = """
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Contact</span>
    </nav>
    <h1>Get in touch</h1>
    <p class="hero__lead">
      Tell us what you need and we will come back within one working day, including when
      the honest answer is that we are not the right firm for it.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="routecards">
      <div class="routecard reveal">
        <h3>Hiring for a role</h3>
        <p>
          Permanent, leadership or volume hiring across software, manufacturing and consumer
          companies. Tell us the role and we will give you a view on the market first.
        </p>
        <a href="#contact-form">Send a hiring enquiry</a>
      </div>
      <div class="routecard reveal">
        <h3>Need software built</h3>
        <p>
          Project and job tracking, finance and invoicing, lead management or internal
          operations tools. Describe the problem rather than the solution.
        </p>
        <a href="#contact-form">Send a software enquiry</a>
      </div>
      <div class="routecard reveal">
        <h3>Looking for a job</h3>
        <p>
          Open roles are listed with a short application form on each one. If nothing fits
          today, send a speculative CV and we will keep it against future mandates.
        </p>
        <a href="/jobs/">See open roles</a>
      </div>
    </div>

    <div class="contact__grid" style="margin-top:56px" id="contact-form">
      <div class="reveal">
        <span class="eyebrow">Details</span>
        <h2 class="section-title" style="font-size:1.5rem">Reach us directly</h2>
        <div class="contact-list">
          <div class="contact-item">
            <div class="contact-item__ico" aria-hidden="true">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4h16v16H4z"/><path d="M4 7l8 6 8-6"/></svg>
            </div>
            <div>
              <div class="contact-item__label">Email</div>
              <div class="contact-item__val"><a href="mailto:admin@animustech.in">admin@animustech.in</a></div>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-item__ico" aria-hidden="true">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.2a2 2 0 012.1-.5c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>
            </div>
            <div>
              <div class="contact-item__label">Phone</div>
              <div class="contact-item__val"><a href="tel:+919422515047">+91 94225 15047</a></div>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-item__ico" aria-hidden="true">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div>
              <div class="contact-item__label">Office</div>
              <div class="contact-item__val">Pune, Maharashtra, India</div>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-item__ico" aria-hidden="true">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5zM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05C21 8.65 22 10.9 22 14.2V21h-4v-6c0-1.6-.6-2.7-2-2.7-1.2 0-1.9.8-2.2 1.6-.1.3-.13.7-.13 1.1V21h-4z"/></svg>
            </div>
            <div>
              <div class="contact-item__label">LinkedIn</div>
              <div class="contact-item__val"><a href="https://www.linkedin.com/company/animus-technologies" target="_blank" rel="noopener">linkedin.com/company/animus-technologies</a></div>
            </div>
          </div>
        </div>
        <p class="form-note" style="text-align:left;margin-top:22px">
          We work with companies across India and reply within one working day.
        </p>
      </div>

      <form action="https://formsubmit.co/admin@animustech.in" method="POST" class="reveal reveal--right">
        <input type="hidden" name="_subject" value="New enquiry from animustech.in contact page">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://animustech.in/contact/thank-you/">
        <p class="hp"><label>Don't fill this out: <input name="_honey"></label></p>

        <div class="field">
          <label for="c-about">What is this about? *</label>
          <select id="c-about" name="Enquiry type" required>
            <option value="">Select one</option>
            <option>Hiring for a role</option>
            <option>Custom software</option>
            <option>Both hiring and software</option>
            <option>Something else</option>
          </select>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="c-name">Your name *</label>
            <input type="text" id="c-name" name="Name" required placeholder="Full name">
          </div>
          <div class="field">
            <label for="c-company">Company *</label>
            <input type="text" id="c-company" name="Company" required placeholder="Company name">
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="c-email">Work email *</label>
            <input type="email" id="c-email" name="Email" required placeholder="you@company.com">
          </div>
          <div class="field">
            <label for="c-phone">Phone</label>
            <input type="tel" id="c-phone" name="Phone" placeholder="+91">
          </div>
        </div>

        <div class="field">
          <label for="c-message">What do you need? *</label>
          <textarea id="c-message" name="Message" required placeholder="For hiring: the roles, how many, location and when you need people. For software: the process that is painful today and roughly how many people would use the tool."></textarea>
        </div>

        <button type="submit" class="btn btn--primary">
          Send enquiry
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </button>
        <p class="form-note">We reply within one working day. Your details stay confidential.</p>
      </form>
    </div>
  </div>
</section>
"""

THANKS_BODY = """
<section class="section" style="padding-top:120px">
  <div class="wrap">
    <div class="emptybox reveal" style="text-align:center;max-width:620px;margin:0 auto">
      <h1 style="font-size:1.8rem;margin-bottom:14px">Thanks, we have it</h1>
      <p>
        Your enquiry has reached us and we will come back within one working day. If it is
        urgent, call +91 94225 15047 rather than waiting on email.
      </p>
      <p style="margin-top:22px">
        <a href="/" class="btn btn--primary">Back to home</a>
      </p>
    </div>
  </div>
</section>
"""

THANKS_CSS = """
<style>
.emptybox{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:44px 38px}
.emptybox p{color:var(--text-2);line-height:1.75;margin:0 0 14px}
</style>
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
{extra_css}{robots}
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

    out = os.path.join(ROOT, "contact")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(PAGE.format(
        title=html.escape(html.unescape(TITLE), quote=True),
        desc=html.escape(html.unescape(DESC), quote=True),
        site=SITE, url=URL, extra_css=EXTRA_CSS, robots="", schema=schema_html,
        header=HEADER, footer=FOOTER, body=BODY))
    print("wrote", URL + "index.html")

    out = os.path.join(ROOT, "contact", "thank-you")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(PAGE.format(
        title="Enquiry Received | Animus Tech",
        desc="Your enquiry has been received. We reply within one working day.",
        site=SITE, url="/contact/thank-you/", extra_css=THANKS_CSS,
        robots='\n<meta name="robots" content="noindex,follow">', schema="",
        header=HEADER, footer=FOOTER, body=THANKS_BODY))
    print("wrote /contact/thank-you/index.html")
