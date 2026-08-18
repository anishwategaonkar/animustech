#!/usr/bin/env python3
"""
Builds /jobs/ and a page per role, with JobPosting schema for Google for Jobs.

    python3 _build_jobs.py

Edit jobs_data.py, not this file.

Also refreshes sitemap-jobs entries so expired roles drop out cleanly.
"""
import os, json, html, datetime, re, shutil

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
ORG_ID = SITE + "/#organization"

from jobs_data import JOBS

# City -> state, for the JobPosting addressRegion. Add a city here when you post
# in a new one, or set "region" directly on the job in jobs_data.py.
CITY_REGION = {
    "pune": "Maharashtra",
    "mumbai": "Maharashtra",
    "nashik": "Maharashtra",
    "nagpur": "Maharashtra",
    "aurangabad": "Maharashtra",
    "chakan": "Maharashtra",
    "hinjewadi": "Maharashtra",
    "bengaluru": "Karnataka",
    "bangalore": "Karnataka",
    "hyderabad": "Telangana",
    "chennai": "Tamil Nadu",
    "coimbatore": "Tamil Nadu",
    "hosur": "Tamil Nadu",
    "new delhi": "Delhi",
    "delhi": "Delhi",
    "gurugram": "Haryana",
    "gurgaon": "Haryana",
    "faridabad": "Haryana",
    "noida": "Uttar Pradesh",
    "ghaziabad": "Uttar Pradesh",
    "ahmedabad": "Gujarat",
    "surat": "Gujarat",
    "vadodara": "Gujarat",
    "jaipur": "Rajasthan",
    "indore": "Madhya Pradesh",
    "kolkata": "West Bengal",
    "kochi": "Kerala",
    "chandigarh": "Chandigarh",
}

TODAY = datetime.date.today().isoformat()

EXTRA_CSS = """
<style>
.jobcard{background:var(--surface);border:1px solid var(--border);border-radius:15px;
  padding:26px 28px;display:block;text-decoration:none;transition:border-color .2s,transform .2s}
.jobcard:hover{border-color:var(--border-lit);transform:translateY(-2px)}
.jobcard h2{margin:12px 0 8px;font-size:1.2rem;color:var(--text);letter-spacing:-.01em}
.jobcard p{margin:0;color:var(--text-2);font-size:.95rem;line-height:1.65}
.joblist{display:grid;gap:18px;margin-top:36px}
.jobmeta{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin:0 0 4px}
.chip{background:var(--accent-dim);border:1px solid var(--accent-line);color:var(--accent);
  padding:4px 11px;border-radius:999px;font-size:.75rem;letter-spacing:.02em}
.chip--muted{background:transparent;border-color:var(--border);color:var(--text-3)}
.jobfacts{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin:32px 0}
.jobfacts div{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px 18px}
.jobfacts dt{font-size:.74rem;text-transform:uppercase;letter-spacing:.06em;color:var(--text-3);margin:0 0 5px}
.jobfacts dd{margin:0;color:var(--text);font-weight:600;font-size:.98rem}
.jobbody{max-width:760px}
.jobbody h2{font-size:1.35rem;margin:38px 0 14px;color:var(--text);letter-spacing:-.01em}
.jobbody p{color:var(--text-2);line-height:1.78;margin:0 0 16px}
.jobbody ul{color:var(--text-2);line-height:1.85;padding-left:22px;margin:0 0 18px}
.jobbody li{margin-bottom:7px}
.emptybox{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:38px 34px;margin-top:36px;max-width:760px}
.emptybox h2{margin:0 0 12px;font-size:1.25rem;color:var(--text)}
.emptybox p{color:var(--text-2);line-height:1.75;margin:0 0 15px}
.applyform{max-width:640px}
.thankbox{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:44px 38px;margin-top:36px;max-width:640px;text-align:center}
.thankbox h1{margin:0 0 14px}
.thankbox p{color:var(--text-2);line-height:1.75;margin:0 0 22px}
</style>
"""

def head(title, desc, url, schema_blocks, extra=""):
    schema = "\n".join('<script type="application/ld+json">\n%s\n</script>'
                       % json.dumps(s, indent=2, ensure_ascii=False) for s in schema_blocks)
    t = html.escape(html.unescape(title), quote=True)
    d = html.escape(html.unescape(desc), quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 54 40'><rect width='54' height='40' rx='7' fill='%23141824'/><circle cx='19' cy='20' r='14' fill='none' stroke='%23dfb78e' stroke-width='3'/><circle cx='35' cy='20' r='14' fill='none' stroke='%239d94e0' stroke-width='3'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{EXTRA_CSS}{extra}
{schema}
</head>
<body>
<div class="progress" aria-hidden="true"><div class="progress__bar" id="progressBar"></div></div>
{HEADER}
<main id="top">
"""

TAIL = f"""
</main>
{FOOTER}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

def money(n):
    if n is None: return None
    if n >= 10000000: return f"{n/10000000:.2f} Cr"
    return f"{n/100000:.1f} L".replace(".0 L", " L")

def salary_line(j):
    if not j.get("salary_min"): return "Not disclosed"
    lo, hi = money(j["salary_min"]), money(j.get("salary_max") or j["salary_min"])
    return f"₹{lo} to ₹{hi}" if hi != lo else f"₹{lo}"

def job_description_html(j):
    """Google wants the full description as HTML inside the schema."""
    parts = [f"<p>{j['summary']}</p>"]
    if j.get("responsibilities"):
        parts.append("<p><strong>Responsibilities</strong></p><ul>"
                     + "".join(f"<li>{r}</li>" for r in j["responsibilities"]) + "</ul>")
    if j.get("requirements"):
        parts.append("<p><strong>Requirements</strong></p><ul>"
                     + "".join(f"<li>{r}</li>" for r in j["requirements"]) + "</ul>")
    if j.get("nice_to_have"):
        parts.append("<p><strong>Nice to have</strong></p><ul>"
                     + "".join(f"<li>{r}</li>" for r in j["nice_to_have"]) + "</ul>")
    return "".join(parts)

def job_schema(j):
    s = {
      "@context": "https://schema.org",
      "@type": "JobPosting",
      "title": j["title"],
      "description": job_description_html(j),
      "identifier": {"@type": "PropertyValue", "name": "Animus Tech", "value": j["slug"]},
      "datePosted": j["posted"],
      "validThrough": j["valid_through"] + "T23:59:59+05:30",
      "employmentType": j["employment"],
      "hiringOrganization": {"@id": ORG_ID},
      "directApply": True,
      "url": f"{SITE}/jobs/{j['slug']}/",
    }
    if j.get("remote"):
        s["jobLocationType"] = "TELECOMMUTE"
        s["applicantLocationRequirements"] = {"@type": "Country", "name": "India"}
    else:
        # Google matches the listing to a place using locality + region. A wrong
        # region sends the job to the wrong city's search results, so map it from
        # the city rather than assuming every role is in Maharashtra.
        city = j["location"].split(",")[0].strip()
        region = j.get("region") or CITY_REGION.get(city.lower())
        addr = {"@type": "PostalAddress", "addressLocality": city,
                "addressCountry": "IN"}
        if region:
            addr["addressRegion"] = region
        s["jobLocation"] = {"@type": "Place", "address": addr}
    if j.get("salary_min"):
        s["baseSalary"] = {"@type": "MonetaryAmount", "currency": "INR",
          "value": {"@type": "QuantitativeValue",
                    "minValue": j["salary_min"],
                    "maxValue": j.get("salary_max") or j["salary_min"],
                    "unitText": "YEAR"}}
    if j.get("experience"):
        s["experienceRequirements"] = {"@type": "OccupationalExperienceRequirements",
                                       "description": j["experience"]}
    return s

def build_job(j):
    url = f"/jobs/{j['slug']}/"
    schema = [job_schema(j), {
      "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Jobs","item":SITE+"/jobs/"},
        {"@type":"ListItem","position":3,"name":j["title"]}]}]

    def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    loc = "Remote, India" if j.get("remote") else j["location"]
    apply_url = f"/jobs/{j['slug']}/apply/"

    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><a href="/jobs/">Jobs</a><span class="crumbs__sep">/</span><span aria-current="page">{j['title']}</span>
    </nav>
    <p class="jobmeta"><span class="chip">{j['industry']}</span><span class="chip chip--muted">{loc}</span></p>
    <h1>{j['title']}</h1>
    <p class="hero__lead">{j['summary']}</p>
    <div class="hero__cta">
      <a href="{apply_url}" class="btn btn--primary">Apply for this role
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <dl class="jobfacts reveal">
      <div><dt>Location</dt><dd>{loc}</dd></div>
      <div><dt>Experience</dt><dd>{j.get('experience','Not specified')}</dd></div>
      <div><dt>Salary</dt><dd>{salary_line(j)}</dd></div>
      <div><dt>Type</dt><dd>{j['employment'].replace('_',' ').title()}</dd></div>
    </dl>

    <article class="jobbody reveal">
      <h2>About the employer</h2>
      <p>{j['client_note']}</p>

      <h2>What you will own</h2>
      {ul(j['responsibilities'])}

      <h2>What we are looking for</h2>
      {ul(j['requirements'])}
      {'<h2>Nice to have</h2>' + ul(j['nice_to_have']) if j.get('nice_to_have') else ''}

      <h2>How we will assess you</h2>
      <p>
        Every application is read against a scorecard agreed with the hiring manager, not
        filtered on keywords. If your experience fits the role but your CV does not use the
        expected words, we would still rather see it. A recruiter reviews every shortlist, and
        no candidate is ever rejected by software alone.
      </p>
      <p>
        You will hear back either way. If you are not right for this role we will tell you,
        rather than leaving you wondering.
      </p>

      <p style="margin-top:32px">
        <a href="{apply_url}" class="btn btn--primary">Apply for this role</a>
      </p>
      <p class="linkrow">Posted {j['posted']} · Open until {j['valid_through']}</p>
    </article>
  </div>
</section>
"""
    out = os.path.join(ROOT, "jobs", j["slug"])
    os.makedirs(out, exist_ok=True)
    desc = f"{j['title']} in {loc}. {j['summary'][:110]}"
    open(os.path.join(out, "index.html"), "w").write(
        head(f"{j['title']} in {loc.split(',')[0]} | Animus Tech", desc, url, schema) + body + TAIL)
    build_apply(j, loc)
    return url

def build_apply(j, loc):
    """The questionnaire a candidate fills in after clicking Apply. Delivered by
    FormSubmit to admin@animustech.in, same mechanism as the homepage contact form."""
    url = f"/jobs/{j['slug']}/apply/"
    subject = f"Application: {j['title']} ({j['slug']})"
    thanks_url = f"{SITE}/jobs/{j['slug']}/apply/thank-you/"

    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><a href="/jobs/">Jobs</a><span class="crumbs__sep">/</span><a href="/jobs/{j['slug']}/">{j['title']}</a><span class="crumbs__sep">/</span><span aria-current="page">Apply</span>
    </nav>
    <span class="eyebrow">{j['title']} · {loc}</span>
    <h1>Apply for this role</h1>
    <p class="hero__lead">
      Six short questions, no account needed. A recruiter reads every application and you
      will hear back either way.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <form action="https://formsubmit.co/admin@animustech.in" method="POST" class="applyform reveal" enctype="multipart/form-data">
      <input type="hidden" name="_subject" value="{subject}">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="{thanks_url}">
      <input type="hidden" name="Role applied for" value="{j['title']} ({j['slug']})">
      <p class="hp"><label>Don't fill this out: <input name="_honey"></label></p>

      <div class="field">
        <label for="full_name">Full name *</label>
        <input type="text" id="full_name" name="Full name" required placeholder="Your full name">
      </div>

      <div class="field-row">
        <div class="field">
          <label for="email">Email *</label>
          <input type="email" id="email" name="Email" required placeholder="you@example.com">
        </div>
        <div class="field">
          <label for="phone">Phone *</label>
          <input type="tel" id="phone" name="Phone" required placeholder="+91">
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="experience">Years of experience *</label>
          <input type="text" id="experience" name="Years of experience" required placeholder="e.g. 5 years">
        </div>
        <div class="field">
          <label for="notice">Notice period *</label>
          <select id="notice" name="Notice period" required>
            <option value="">Select one</option>
            <option>Immediate / serving no notice</option>
            <option>15 days or less</option>
            <option>30 days</option>
            <option>60 days</option>
            <option>90 days</option>
            <option>Other</option>
          </select>
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="current_ctc">Current CTC *</label>
          <input type="text" id="current_ctc" name="Current CTC" required placeholder="e.g. 8 LPA">
        </div>
        <div class="field">
          <label for="expected_ctc">Expected CTC *</label>
          <input type="text" id="expected_ctc" name="Expected CTC" required placeholder="e.g. 10 LPA">
        </div>
      </div>

      <div class="field">
        <label for="fit">Why do you think you are fit for this role? *</label>
        <textarea id="fit" name="Why they are a fit" required placeholder="A few sentences on relevant experience and why this role makes sense for you."></textarea>
      </div>

      <div class="field">
        <label for="resume">Resume (PDF or Word) *</label>
        <input type="file" id="resume" name="Resume" accept=".pdf,.doc,.docx" required>
      </div>

      <button type="submit" class="btn btn--primary">
        Submit application
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </button>
      <p class="form-note">Goes straight to a recruiter. Your details are used only to assess you for this role.</p>
    </form>
  </div>
</section>
"""
    out = os.path.join(ROOT, "jobs", j["slug"], "apply")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head(f"Apply: {j['title']} | Animus Tech",
             f"Application form for {j['title']} in {loc}.", url,
             [], extra='<meta name="robots" content="noindex,follow">') + body + TAIL)
    build_apply_thanks(j)

def build_apply_thanks(j):
    url = f"/jobs/{j['slug']}/apply/thank-you/"
    body = f"""
<section class="section" style="padding-top:120px">
  <div class="wrap">
    <div class="thankbox reveal">
      <h1>Application received</h1>
      <p>
        Thanks for applying for {j['title']}. A recruiter will read it against the scorecard
        for this role and come back to you either way, not just if it is a yes.
      </p>
      <a href="/jobs/" class="btn btn--primary">See other open roles</a>
    </div>
  </div>
</section>
"""
    out = os.path.join(ROOT, "jobs", j["slug"], "apply", "thank-you")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head("Application Received | Animus Tech",
             "Your application has been received.", url,
             [], extra='<meta name="robots" content="noindex,follow">') + body + TAIL)

def build_index(live):
    url = "/jobs/"
    schema = [{
      "@context":"https://schema.org","@type":"CollectionPage","@id":SITE+url,
      "name":"Open roles at Animus Tech","url":SITE+url,
      "publisher":{"@id":ORG_ID},"inLanguage":"en-IN"},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Jobs"}]}]

    if live:
        cards = "".join(f"""
      <a class="jobcard reveal" href="/jobs/{j['slug']}/">
        <p class="jobmeta"><span class="chip">{j['industry']}</span><span class="chip chip--muted">{'Remote, India' if j.get('remote') else j['location']}</span><span class="chip chip--muted">{salary_line(j)}</span></p>
        <h2>{j['title']}</h2>
        <p>{j['summary']}</p>
      </a>""" for j in live)
        listing = f'<div class="joblist">{cards}</div>'
        lead = ("Roles we are actively recruiting for right now. Every one of these is a live "
                "mandate with a real client, and every application is read by a person.")
    else:
        listing = """
      <div class="emptybox reveal">
        <h2>No open roles listed at the moment</h2>
        <p>
          We only list roles we are actively recruiting for, so this page is sometimes empty.
          We would rather show you nothing than a stale list of positions that closed months ago.
        </p>
        <p>
          If you work in software, manufacturing or consumer brands, send us your CV anyway. We
          keep profiles on file against the mandates we take on, and we will come back to you
          when something fits rather than when we need to fill a quota.
        </p>
        <p style="margin-top:24px">
          <a href="mailto:admin@animustech.in?subject=Speculative%20application" class="btn btn--primary">Send us your CV</a>
        </p>
      </div>"""
        lead = ("We only list roles we are actively recruiting for. If the list is empty, it means "
                "we have nothing open right now rather than that we stopped updating the page.")

    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Jobs</span>
    </nav>
    <span class="eyebrow">Open roles</span>
    <h1>Jobs we are hiring for</h1>
    <p class="hero__lead">{lead}</p>
  </div>
</section>

<section class="section">
  <div class="wrap">{listing}</div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">For candidates</span>
      <h2 class="section-title">What applying here is like</h2>
      <p class="section-lead">Short version: a person reads it, and you get an answer.</p>
    </div>
    <div class="benefits">
      <div class="benefit reveal"><h3>Read against a scorecard</h3><p>Not filtered on keywords. If your experience fits but your CV does not use the expected words, we would still rather see it.</p></div>
      <div class="benefit reveal"><h3>A human decides</h3><p>Software narrows the field. A recruiter reviews every shortlist, and nobody is rejected by software alone.</p></div>
      <div class="benefit reveal"><h3>You hear back</h3><p>Including when the answer is no. Silence is the standard in this industry and it should not be.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Hiring, not looking</span>
      <h2 class="section-title">Need to fill a role?</h2>
      <p class="section-lead">We work with software, manufacturing and D2C companies across India. Tell us what you are hiring for.</p>
      <p style="margin-top:26px"><a href="/talent-acquisition/#contact" class="btn btn--primary">Talk to us about hiring</a></p>
      <p class="linkrow">See also: <a href="/how-we-work/">How we work</a> · <a href="/recruitment-agency-pune/">Recruitment agency in Pune</a></p>
    </div>
  </div>
</section>
"""
    out = os.path.join(ROOT, "jobs")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head("Open Roles &amp; Jobs | Animus Tech",
             "Live roles we are actively recruiting for across software, manufacturing and consumer companies in India. Every application read by a person.",
             url, schema) + body + TAIL)
    return url

def sync_sitemap(live):
    p = os.path.join(ROOT, "sitemap.xml")
    s = open(p).read()
    # strip every existing /jobs/ entry, then re-add
    s = re.sub(r'\s*<url>\s*<loc>https://animustech\.in/jobs/[^<]*</loc>.*?</url>', '', s, flags=re.S)
    add = f"""  <url>
    <loc>{SITE}/jobs/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>

"""
    for j in live:
        add += f"""  <url>
    <loc>{SITE}/jobs/{j['slug']}/</loc>
    <lastmod>{j['posted']}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>

"""
    open(p, "w").write(s.replace("</urlset>", add + "</urlset>"))

if __name__ == "__main__":
    live, expired = [], []
    for j in JOBS:
        (expired if j["valid_through"] < TODAY else live).append(j)

    # remove pages for jobs no longer in the file or expired
    jobs_dir = os.path.join(ROOT, "jobs")
    keep = {j["slug"] for j in live}
    if os.path.isdir(jobs_dir):
        for d in os.listdir(jobs_dir):
            full = os.path.join(jobs_dir, d)
            if os.path.isdir(full) and d not in keep:
                shutil.rmtree(full)
                print("removed expired/withdrawn:", d)

    for j in live:
        print("wrote", build_job(j))
    print("wrote", build_index(live))
    sync_sitemap(live)

    if expired:
        print(f"\n{len(expired)} job(s) past valid_through and skipped:",
              ", ".join(j["slug"] for j in expired))
        print("Delete them from jobs_data.py.")
    print(f"\n{len(live)} live job(s). Sitemap synced.")
