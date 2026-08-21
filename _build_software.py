#!/usr/bin/env python3
"""
Builds /software/ , the software development arm of the site.

    python3 _build_software.py

Shares the header, footer, stylesheet and contact mechanism with the talent
acquisition side, so both arms look and behave like one company.

HONESTY RULE, same as everywhere else on this site: only describe software that
actually exists and works. The two tools below are real and running. Do not add
a case study for anything that is still a proposal or a pitch.
"""
import os, json, html

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
ORG_ID = SITE + "/#organization"
URL    = "/software/"

TITLE = "Software Development for Manufacturing India | Animus Tech"
DESC  = ("Custom software for manufacturing and small enterprises across India. "
         "Project tracking, finance and invoicing, lead management and internal tools.")

# ------------------------------------------------------------------ schema ---
SCHEMAS = [
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": SITE + URL + "#service",
  "serviceType": "Custom software development",
  "name": "Custom software development for manufacturing",
  "description": ("Custom software for manufacturing, small enterprises and operations led businesses: project "
                  "tracking with multiple users, finance and invoicing systems, lead "
                  "management and internal operational tools."),
  "provider": {"@id": ORG_ID},
  "areaServed": [
      {"@type": "Country", "name": "India"},
      {"@type": "City", "name": "Pune"},
      {"@type": "City", "name": "Mumbai"},
      {"@type": "City", "name": "Bengaluru"},
  ],
  "url": SITE + URL,
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Software development services",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
      for n in [
        "Project and job tracking systems",
        "Finance, invoicing and billing tools",
        "Lead management and CRM",
        "Internal operations tools",
        "Reporting and dashboards",
      ]
    ],
  },
},
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Software development"},
  ],
},
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": q,
     "acceptedAnswer": {"@type": "Answer", "text": a}}
    for q, a in [
      ("Do you build software for manufacturing companies?",
       "Yes. We build custom software for manufacturing, small enterprises and operations led businesses, "
       "including project and job tracking, finance and invoicing systems, lead management "
       "and internal operational tools. We work with companies across India."),
      ("Can the software handle multiple users with different access levels?",
       "Yes. Most operational tools need this. A supervisor, an accounts person and a plant "
       "head each need a different view of the same data, and we build role based access in "
       "from the start rather than adding it later."),
      ("Do we own the software you build for us?",
       "Yes. You own the code and the data. We agree this in writing before any work starts, "
       "so there is no ambiguity about it later."),
      ("Why does a recruitment firm build software?",
       "Because we built ours first. We needed tools to run our own operations, built them, "
       "and found the same gaps sitting unaddressed in the businesses we hire for. The two "
       "arms share one thing: we spend the time to understand how the work actually happens "
       "before we build or hire for it."),
      ("How long does a project take?",
       "It depends entirely on scope, and we will not quote a timeline before we understand "
       "yours. What we will do is scope the first working version deliberately small, so you "
       "have something in real use in weeks rather than waiting months to see anything."),
    ]
  ],
},
]

EXTRA_CSS = """
<style>
.arm-note{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-bottom:26px}
.arm-note a{font-size:.9rem;color:var(--text-3);border-bottom:1px solid var(--border);
  padding-bottom:2px;transition:color .2s,border-color .2s}
.arm-note a:hover{color:var(--accent);border-color:var(--accent-line)}
.builtbox{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:30px 32px;margin-top:22px}
.builtbox h3{font-size:1.12rem;margin-bottom:10px;color:var(--text)}
.builtbox p{color:var(--text-2);font-size:.97rem;line-height:1.75;margin-bottom:14px}
.builtbox p:last-child{margin-bottom:0}
.builtbox .tag{margin-bottom:14px}
.builtgrid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:44px}
@media(max-width:860px){.builtgrid{grid-template-columns:1fr}}
</style>
"""

# -------------------------------------------------------------------- body ---
BODY = """
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="glow glow--b" aria-hidden="true"></div>

  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Software development</span>
    </nav>
    <p class="arm-note"><a href="/talent-acquisition/">Looking for hiring instead? Go to talent acquisition</a></p>
    <h1>Software built around <span class="accent-text">how the work actually happens.</span></h1>
    <h2 class="hero__kicker">Custom software for manufacturing, small enterprises and operations led businesses across India</h2>
    <p class="hero__lead">
      Most operational software fails for the same reason most hires fail: nobody spent
      enough time understanding the job before committing to a solution. We build tools that
      fit the process you already run, rather than asking your team to work the way the
      software prefers.
    </p>
    <div class="hero__cta">
      <a href="#software-contact" class="btn btn--primary">Tell us what you need built
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="#what-we-built" class="btn btn--ghost">See what we have built</a>
    </div>
    <ul class="hero__meta">
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> You own the code and the data</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> A complete working system, in real use fast</li>
      <li><svg class="tick" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> Built by the people who run it</li>
    </ul>
  </div>
</section>

<!-- ============ WHAT WE BUILT ============ -->
<section class="section" id="what-we-built">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Working software</span>
      <h2 class="section-title">What we have built and run</h2>
      <p class="section-lead">
        Two systems in real use, carrying real data every working day. Not prototypes,
        and not slideware.
      </p>
    </div>

    <div class="builtgrid">
      <div class="builtbox reveal">
        <span class="tag">Lead management</span>
        <h3>Lead generation tracker</h3>
        <p>
          In daily use at a digital marketing agency. It runs their pipeline end to end:
          capturing leads, tracking every touch against them, and showing what is actually
          moving rather than what somebody remembered to update.
        </p>
        <p>
          The useful part was never the database. It was deciding what counts as a stage
          change, and making the tool refuse to let a record sit in limbo without a next
          action against it.
        </p>
      </div>

      <div class="builtbox reveal">
        <span class="tag">Finance and invoicing</span>
        <h3>Finance tracker</h3>
        <p>
          Customised for small and medium enterprises that work job by job. It raises
          invoices and holds the complete financial history against each job, so the money
          side of a job and the job itself stay attached to each other.
        </p>
        <p>
          Anyone who has run an operation like this knows why it matters. The moment
          invoicing lives in one place and job history lives in another, reconciliation
          becomes somebody's whole week.
        </p>
      </div>

    </div>
  </div>
</section>

<!-- ============ HOW WE WORK ============ -->
<section class="section" id="software-approach">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">How we work</span>
      <h2 class="section-title">One workflow, complete, then the next</h2>
      <p class="section-lead">
        The most expensive software mistake is building everything at once, before anyone
        has used any of it. We build one process properly, start to end, and put it to work.
      </p>
    </div>

    <div class="steps">
      <div class="step reveal">
        <h3>Understand the process</h3>
        <p>
          We sit with the people who do the work and map how it actually happens, including
          the workarounds nobody documented. That is usually where the real requirement is
          hiding.
        </p>
      </div>
      <div class="step reveal">
        <h3>Take one process, whole</h3>
        <p>
          We agree the workflow that is costing you most and build the whole of it, start to
          end, rather than a piece of several. We also write down what is deliberately not in
          scope yet. Both halves of that matter.
        </p>
      </div>
      <div class="step reveal">
        <h3>Build it and put it in use</h3>
        <p>
          A working version your team uses on real data, not a demo environment. Real use
          surfaces problems that no amount of specification review will.
        </p>
      </div>
      <div class="step reveal">
        <h3>Extend from evidence</h3>
        <p>
          We add what people actually reach for and drop what they do not. Every extension
          is argued from use, not from the original wish list.
        </p>
      </div>
    </div>

    <div class="human-note reveal" style="margin-top:44px">
      <div class="human-note__ico" aria-hidden="true">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 11l3 3L22 4M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>
      </div>
      <div>
        <h3>What we commit to in writing</h3>
        <p>
          You own the code and the data. We tell you when something you have asked for is a
          bad idea, and why, rather than quietly building it and invoicing for it. And if a
          deadline is going to slip, you hear it when we know, not when it slips.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ============ WHY US ============ -->
<section class="section section--alt">
  <div class="wrap">
    <div class="reveal about__lead">
      <span class="eyebrow">Why us</span>
      <h2 class="section-title">We are the users, not just the builders</h2>
      <p>
        Most software firms hand over a system and move on. We run operational software
        ourselves, every day, which changes what you build and what you refuse to build.
        You stop adding features nobody opens and start fixing the three screens people
        actually live in.
      </p>
      <p>
        The other half of Animus Tech is talent acquisition, and that is not a coincidence.
        Both jobs come down to the same discipline: understand how the work actually
        happens before committing to anything. Skip that step and you get a bad hire, or
        a system your team quietly works around.
      </p>
      <p>
        <strong>Which is why this page shows you two working tools rather than a wall of
        logos.</strong> You can judge software by what it does. Adjectives are cheap.
      </p>
    </div>

    <div class="benefits">
      <div class="benefit reveal">
        <h3>We use what we build</h3>
        <p>
          Both systems on this page run our own operations. Software you depend on daily
          gets built differently from software you hand over and forget.
        </p>
      </div>
      <div class="benefit reveal">
        <h3>We know operational businesses</h3>
        <p>
          We recruit for manufacturing companies across India, so shift patterns,
          dispatch pressure and plant floor reality are not new information to us.
        </p>
      </div>
      <div class="benefit reveal">
        <h3>We say no</h3>
        <p>
          If a project is not a fit, or the budget will not produce something worth having,
          we say so early. That is a cheaper conversation in week one than in month four.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ============ CONTACT ============ -->
<section class="section" id="software-contact">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Get in touch</span>
      <h2 class="section-title">Tell us what you need built</h2>
      <p class="section-lead">
        Describe the problem rather than the solution and we will come back within one
        working day with an honest view, including whether we are the right people for it.
      </p>
    </div>

    <div class="contact__grid" style="margin-top:52px">
      <div class="reveal">
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
              <div class="contact-item__val"><a href="https://www.linkedin.com/company/animus_tech" target="_blank" rel="noopener">linkedin.com/company/animus_tech</a></div>
            </div>
          </div>
        </div>
      </div>

      <form action="https://formsubmit.co/admin@animustech.in" method="POST" class="reveal reveal--right">
        <input type="hidden" name="_subject" value="New software enquiry from animustech.in">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://animustech.in/contact/thank-you/?src=software">
        <input type="hidden" name="Enquiry type" value="Software development">
        <p class="hp"><label>Don't fill this out: <input name="_honey"></label></p>

        <div class="field-row">
          <div class="field">
            <label for="sw-name">Your name *</label>
            <input type="text" id="sw-name" name="name" required placeholder="Full name">
          </div>
          <div class="field">
            <label for="sw-company">Company *</label>
            <input type="text" id="sw-company" name="company" required placeholder="Company name">
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="sw-email">Work email *</label>
            <input type="email" id="sw-email" name="email" required placeholder="you@company.com">
          </div>
          <div class="field">
            <label for="sw-phone">Phone</label>
            <input type="tel" id="sw-phone" name="phone" placeholder="+91">
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="sw-industry">Industry</label>
            <select id="sw-industry" name="industry">
              <option value="">Select one</option>
              <option>Manufacturing &amp; engineering</option>
              <option>Automotive &amp; auto components</option>
              <option>Service &amp; maintenance</option>
              <option>Software &amp; technology</option>
              <option>D2C &amp; consumer</option>
              <option>Other</option>
            </select>
          </div>
          <div class="field">
            <label for="sw-need">What do you need?</label>
            <select id="sw-need" name="need">
              <option value="">Select one</option>
              <option>Project or job tracking system</option>
              <option>Finance, invoicing or billing tool</option>
              <option>Lead management or CRM</option>
              <option>Internal operations tool</option>
              <option>Reporting and dashboards</option>
              <option>Not sure yet, want to discuss</option>
            </select>
          </div>
        </div>

        <div class="field">
          <label for="sw-message">What are you trying to solve? *</label>
          <textarea id="sw-message" name="message" required placeholder="The process that is painful today, roughly how many people would use the tool, and any deadline you are working to."></textarea>
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

<!-- ============ CROSS LINK ============ -->
<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">The other half</span>
      <h2 class="section-title">Hiring, not building?</h2>
      <p class="section-lead">
        Animus Tech is also an AI enabled talent acquisition firm working with software,
        manufacturing and D2C companies across India.
      </p>
      <p style="margin-top:26px">
        <a href="/talent-acquisition/" class="btn btn--primary">Go to talent acquisition
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
      <p class="linkrow">See also: <a href="/software/custom-software-development-pune/">Custom software development in Pune</a> · <a href="/software/manufacturing-software/">Manufacturing software</a> · <a href="/software/ai-solutions/">Custom AI</a> · <a href="/software/internal-tools/">Internal tools</a> · <a href="/how-we-work/">How we work</a></p>
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------------- build ---
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

    out_dir = os.path.join(ROOT, "software")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(PAGE.format(
            title=html.escape(html.unescape(TITLE), quote=True),
            desc=html.escape(html.unescape(DESC), quote=True),
            site=SITE, url=URL, extra_css=EXTRA_CSS, schema=schema_html,
            header=HEADER, footer=FOOTER, body=BODY))
    print("wrote", URL + "index.html")
