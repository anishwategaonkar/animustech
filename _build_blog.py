#!/usr/bin/env python3
"""
Builds /blog/ and every post underneath it.

    python3 _build_blog.py

Add a post by appending to POSTS. Keep `body` as HTML. Every factual claim must
trace to experience-bank.md.
"""
import os, json, html

ROOT   = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE   = "https://animustech.in"
AUTHOR = "Anish Wategaonkar"

# ------------------------------------------------------------------ posts ---
POSTS = [
{
 "slug": "recruitment-agency-fees-india",
 "date": "2026-08-13",
 "tag": "Hiring costs",
 "title": "Recruitment Agency Fees in India | Animus Tech",
 "h1": "What recruitment agencies actually charge in India",
 "desc": "Contingency, retained and volume pricing explained, what drives the number up or down, and the questions to ask before you sign.",
 "lead": ("Almost nobody in Indian recruitment publishes their pricing, which leaves buyers "
          "guessing at a number that varies by a factor of two. Here is how the money actually "
          "works, what moves the price, and what you are really paying for."),
 "body": """
<h2>The three pricing models</h2>
<p>Nearly every recruitment engagement in India runs on one of three structures. Knowing which
one you are in tells you most of what you need to know about how the agency will behave.</p>

<h3>Contingency</h3>
<p>You pay only when a candidate joins. Fees commonly sit between <strong>8.33% and 16.67% of
the candidate's annual CTC</strong>, with a replacement guarantee of 60 to 90 days. The lower
end of that range tends to appear on volume roles and the upper end on specialist ones.</p>
<p>The attraction is obvious: no hire, no invoice. The cost is less obvious, and it is
structural. An agency paid only on placement carries all the risk, so the rational response is
to spread that risk across many clients and send volume, hoping something lands. That is why
you receive twenty CVs and end up doing the screening yourself. You are not being badly served
by a bad agency. You are being served exactly as the pricing model rewards.</p>

<h3>Retained</h3>
<p>You pay in stages, typically a third at engagement, a third at shortlist and a third on
joining. Used for leadership, confidential and genuinely scarce roles. Total cost is usually
higher, often 20% to 33% of CTC.</p>
<p>What you are buying is exclusivity and attention. A retained recruiter is not hedging across
six other clients with the same brief, which means they can afford to spend time on market
mapping and on the candidates who are not looking.</p>

<h3>Volume or per-hire</h3>
<p>For drives where you need many people in one window, pricing usually moves to a flat fee per
hire rather than a percentage. Rates fall as numbers rise. Sensible for plant ramp-ups, new
shifts and seasonal peaks.</p>

<h2>What actually moves the number</h2>
<p>Fee quotes vary far more by role than by agency. The things that push a price up:</p>
<ul>
<li><strong>Scarcity.</strong> How many people in the country can genuinely do this job, and
how many of them are reachable.</li>
<li><strong>Seniority.</strong> Senior searches take longer, involve more stakeholders and
carry a higher cost of failure.</li>
<li><strong>Confidentiality.</strong> Replacing someone still in post cannot be run as an open
search.</li>
<li><strong>Location.</strong> A plant role an hour outside the city has a smaller willing pool
than the same role in the city, regardless of salary.</li>
<li><strong>How well the role is defined.</strong> The most underrated factor, and the one
entirely within your control. More on this below.</li>
</ul>

<h2>The line item nobody quotes you</h2>
<p>Fee is the visible cost. It is rarely the largest one.</p>
<p>Run a realistic set of numbers through our
<a href="/tools/cost-of-a-bad-hire-calculator/">cost of a bad hire calculator</a> and the
recruitment fee typically lands somewhere between a tenth and a fifth of the total cost of a
hire that does not work out. The expensive lines are the ones nobody invoices you for: salary
paid to someone who was never going to succeed, the months the seat sat empty, and the
management hours spent on a problem that a better-defined role would have prevented.</p>
<p>Which is why choosing an agency on fee alone is usually the expensive decision. A two
percent difference in fee is noise against the cost of one wrong hire.</p>

<h2>What a badly defined role costs</h2>
<p>We can put a number on this, because we have run the same method against a brief that held
still and a brief that did not.</p>
<p>On a sales role where the mandate stayed fixed, we screened more than forty profiles, shared
eight in two batches of four, and the client hired from the second batch. Twenty-five days from
intake to the person starting.</p>
<p>On a factory manager search where the mandate changed mid-way, we screened over a hundred
profiles and shared twenty to twenty-five. Roughly forty-five days to joining.</p>
<p>Same recruiter, same process, roughly three times the submittals and nearly twice the
timeline. Nobody behaved badly. The role definition moved, and every profile screened against
the old definition stopped counting. If you want a search to be cheap, the highest-leverage
thing you can do is spend an hour getting the brief right before anyone starts sourcing.</p>

<h2>Questions worth asking before you sign</h2>
<ul>
<li>What is the fee, and what exactly triggers it?</li>
<li>What is the replacement guarantee, and what voids it?</li>
<li>How many other clients are you running this same brief for right now?</li>
<li>How many profiles will I see, and how many will you have screened to get there?</li>
<li>What happens if you decide the compensation band will not clear the market?</li>
<li>Who actually does the screening, and will I speak to them?</li>
</ul>
<p>The third and fourth questions are the revealing ones. An agency running your brief across
several clients simultaneously is optimising for their portfolio, not your role. And an agency
that cannot tell you its submittal-to-hire ratio has probably never measured it.</p>

<h2>How we price</h2>
<p>We scope fees to the role rather than applying a flat percentage, and we confirm them in
writing at intake before any sourcing begins. There are no upfront fees. If we think the
compensation band will not clear the market, we say so in week one rather than week six, which
is a harder conversation early and a much cheaper one.</p>
<p>More on what we commit to, and what we need from you, on
<a href="/how-we-work/">how we work</a>.</p>
""",
 "related": [("How we work, and the numbers behind it", "/how-we-work/"),
             ("Cost of a bad hire calculator", "/tools/cost-of-a-bad-hire-calculator/")],
},

{
 "slug": "how-to-choose-a-recruitment-agency",
 "date": "2026-08-13",
 "tag": "Choosing a partner",
 "title": "How to Choose a Recruitment Agency | Animus Tech",
 "h1": "How to choose a recruitment agency: 9 questions to ask first",
 "desc": "Most agencies sound identical in a pitch. These nine questions separate the ones who will do the work from the ones who will forward CVs.",
 "lead": ("Every recruitment agency promises quality and speed. The pitch is not where the "
          "difference shows. These are the questions that surface it, and what a good answer "
          "sounds like."),
 "body": """
<p>Recruitment is unusual as a purchase: the thing you are buying is judgement, and judgement is
invisible until after you have paid for it. Reputation and referrals help, but if you are
evaluating an agency cold, these nine questions do most of the work.</p>

<h2>1. How many profiles will I see, and how many will you screen to get there?</h2>
<p>This is the single most revealing question, because it exposes whether the agency does the
filtering or outsources it to you. Ten to twenty submittals per hire is common in the industry.
Some send considerably more.</p>
<p>A good answer is a specific ratio, with the top of the funnel included. "We screened forty
and sent you eight" describes work. "We'll send you plenty of options" describes forwarding.</p>

<h2>2. How many other clients are you running this brief for right now?</h2>
<p>Under contingency pricing, an agency is paid only on placement, so hedging across many
clients with similar roles is rational. It is also the reason your search may be receiving a
fraction of anyone's attention. Ask directly. The answer tells you where you sit in their
portfolio.</p>

<h2>3. Who does the screening, and will I speak to them?</h2>
<p>In many firms the person who sells the engagement is not the person who runs it. That is not
inherently wrong, but you should know before signing, and you should meet whoever will actually
read the CVs.</p>

<h2>4. What will you tell me if the compensation band will not clear the market?</h2>
<p>Listen for whether they will tell you at all, and when. An agency that discovers this in
week six has cost you six weeks. An agency that says it at intake is giving up the easy sale in
exchange for being useful, which is exactly the behaviour you want.</p>

<h2>5. What happens if you think the role is wrong?</h2>
<p>Most failed hires trace back to a role that was never properly defined rather than a
candidate who was badly sourced. An agency that will push back on your job description before
sourcing is worth more than one that simply executes it. You are paying for judgement, not
agreement.</p>

<h2>6. How will you screen for the things the CV does not show?</h2>
<p>Ask for the actual method, not the reassurance. For a factory manager role, for instance,
nearly every applicant is a production manager who describes themselves as having run the
factory, and both CVs use identical language. The way to tell them apart is to probe the
interfaces between functions, dispatch scheduling and how they traded off production targets
against despatch commitments. A production person goes thin there.</p>
<p>Whatever your role, a credible agency can describe a specific technique. A weak one talks
about "getting to know candidates".</p>

<h2>7. What is your replacement guarantee, and what voids it?</h2>
<p>Sixty to ninety days is standard. The exclusions matter more than the headline: redundancy,
role change, and resignation for reasons unrelated to fit are commonly excluded, and reasonably
so. Read them before you need them.</p>

<h2>8. How will you keep me informed, including when there is nothing to report?</h2>
<p>Silence in recruitment usually means bad news being postponed. A weekly written update
regardless of progress is a low bar, and a surprising number of agencies will not commit to
it.</p>

<h2>9. Tell me about a search that went badly.</h2>
<p>The best question on the list, and the one most likely to be dodged. Every recruiter has
searches that went long. Someone who can describe one honestly, name what caused it and say
what they changed is telling you how they will behave when yours goes sideways. Someone whose
every search has gone perfectly is either new or not being straight with you.</p>

<h2>What we would answer</h2>
<p>On a recent sales role: forty-plus profiles screened, eight shared in two batches of four,
hired from the second batch, twenty-five days from intake to joining. On a factory manager
search where the brief changed mid-way: a hundred-plus screened, twenty to twenty-five shared,
about forty-five days. The second number is worse, and the reason is the point.</p>
<p>Our answers to the rest are on <a href="/how-we-work/">how we work</a>, including what we
commit to in writing and what we need from you for any of it to hold.</p>
""",
 "related": [("How we work, and what we commit to", "/how-we-work/"),
             ("What recruitment agencies charge in India", "/blog/recruitment-agency-fees-india/")],
},

{
 "slug": "why-your-search-went-long",
 "date": "2026-08-13",
 "tag": "Hiring process",
 "title": "Why Your Search Went Long | Animus Tech",
 "h1": "Why your search went long, and where the time actually goes",
 "desc": "Most recruitment delay is not sourcing. It is the brief moving, feedback arriving late, and requirements surfacing at final round. With real numbers.",
 "lead": ("When a search runs over, the assumption is that the recruiter could not find people. "
          "Usually that is not what happened. Here is where the time really goes, with numbers "
          "from two of our own searches, including the one that went long."),
 "body": """
<h2>Two searches, same method, very different outcomes</h2>
<p>We ran both of these. The comparison is more useful than any general advice we could give.</p>

<table class="cmp">
<thead><tr><th></th><th>Sales role</th><th>Factory manager</th></tr></thead>
<tbody>
<tr><td>Brief</td><td>held steady</td><td>changed mid-search</td></tr>
<tr><td>Profiles screened</td><td>40+</td><td>100+</td></tr>
<tr><td>Shared with client</td><td>8</td><td>20–25</td></tr>
<tr><td>Intake to joining</td><td>25 days</td><td>~45 days</td></tr>
</tbody>
</table>

<p>Same recruiter. Same screening method. Roughly three times the submittals and nearly twice
the timeline. The variable was not effort, skill or market conditions. It was whether the
definition of the role stayed still.</p>

<h2>Why a moving brief is so expensive</h2>
<p>It is not that the change itself takes time. It is that every profile screened against the
old definition stops counting. Work already done is discarded, and the funnel widens again from
the top. A change in week three does not cost you a week, it costs you three.</p>
<p>This is rarely anyone behaving badly. Roles genuinely evolve, particularly when a hiring
manager starts meeting candidates and discovers what they actually want. But it should be named
when it happens, because the alternative is a recruiter quietly absorbing the cost and the
client wondering why the search is slow.</p>

<h2>The other four places time disappears</h2>

<h3>Feedback latency</h3>
<p>A batch goes out. Feedback takes eleven days. By then two of the four have accepted something
else. This is the most common and most fixable delay in recruitment, and it is entirely on the
client side. Three working days is a reasonable commitment and it changes outcomes materially.</p>

<h3>Requirements that surface at final round</h3>
<p>A shift pattern, a travel expectation, a reporting line, a non-negotiable nobody thought to
mention at intake. It surfaces at final interview and invalidates half the pipeline. Everything
in this category is preventable with a proper intake conversation.</p>

<h3>The compensation band that was never going to clear</h3>
<p>A search priced below the market does not fail slowly, it fails invisibly. Candidates decline
at offer, or never engage. The honest version of this conversation belongs in week one, on the
basis of screening data rather than opinion.</p>
<p>On one search for a consumer brand we screened more than thirty profiles looking for someone
strong in both e-commerce and quick commerce, and found nobody with both at that budget. Rather
than keep sending near-misses, we took the screening data back to the client and asked for a
revised budget and requirement. The role closed about two weeks later.</p>

<h3>Notice periods</h3>
<p>Thirty to ninety days in India, and no agency can compress them. Worth separating from the
rest when you assess whether a search was slow: on our sales role, ten of the twenty-five days
were the search and fifteen were notice. Judge the part that was actually in anyone's control.</p>

<h2>What this means for how you buy</h2>
<p>Be sceptical of any agency that promises a fixed number of days. Roughly half of what
determines the timeline sits on your side of the table: how well the role is defined, how fast
feedback comes back, whether the band is realistic, and whether the brief holds.</p>
<p>What an agency can honestly commit to is process. A written update every week whether or not
there is progress. An honest read on compensation at intake. Naming a slip when it happens,
including when the cause is on their own side. That is the part they control completely, and it
is the part worth holding them to.</p>
<p>Ours is written down on <a href="/how-we-work/">how we work</a>, including what we need from
you.</p>
""",
 "related": [("How we work, and what we commit to", "/how-we-work/"),
             ("Manufacturing recruitment in Pune", "/industries/manufacturing-recruitment-pune/")],
},
]

# --------------------------------------------------------------- rendering ---
EXTRA_CSS = """
<style>
.post{max-width:760px;margin:0 auto}
.post h2{font-size:clamp(1.4rem,2.6vw,1.85rem);letter-spacing:-.02em;margin:48px 0 14px;color:var(--text)}
.post h3{font-size:1.1rem;margin:30px 0 10px;color:var(--accent-2)}
.post p{color:var(--text-2);line-height:1.78;margin:0 0 17px;font-size:1.04rem}
.post ul{color:var(--text-2);line-height:1.85;margin:0 0 18px;padding-left:22px}
.post li{margin-bottom:8px}
.post a{color:var(--accent)}
.post strong{color:var(--text)}
.cmp{width:100%;border-collapse:collapse;margin:26px 0;font-size:.95rem}
.cmp th,.cmp td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--border)}
.cmp thead th{color:var(--text-3);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}
.cmp td:first-child{color:var(--text-2)}
.cmp td:not(:first-child){color:var(--text);font-weight:600;font-variant-numeric:tabular-nums}
.postmeta{display:flex;gap:14px;align-items:center;flex-wrap:wrap;color:var(--text-3);font-size:.86rem;margin-bottom:8px}
.tagchip{background:var(--accent-dim);border:1px solid var(--accent-line);color:var(--accent);
  padding:4px 11px;border-radius:999px;font-size:.76rem;letter-spacing:.02em}
.postlist{display:grid;gap:18px;margin-top:36px}
.postcard{background:var(--surface);border:1px solid var(--border);border-radius:15px;
  padding:26px 28px;transition:border-color .2s,transform .2s;display:block;text-decoration:none}
.postcard:hover{border-color:var(--border-lit);transform:translateY(-2px)}
.postcard h2{margin:10px 0 8px;font-size:1.22rem;color:var(--text);letter-spacing:-.01em}
.postcard p{margin:0;color:var(--text-2);font-size:.96rem;line-height:1.65}
</style>
"""

def head(title, desc, url, schema_blocks):
    schema = "\n".join('<script type="application/ld+json">\n%s\n</script>'
                       % json.dumps(s, indent=2, ensure_ascii=False) for s in schema_blocks)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(html.unescape(title), quote=True)}</title>
<meta name="description" content="{html.escape(html.unescape(desc), quote=True)}">
<link rel="canonical" href="{SITE}{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(html.unescape(title), quote=True)}">
<meta property="og:description" content="{html.escape(html.unescape(desc), quote=True)}">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 54 40'><rect width='54' height='40' rx='7' fill='%23141824'/><circle cx='19' cy='20' r='14' fill='none' stroke='%23dfb78e' stroke-width='3'/><circle cx='35' cy='20' r='14' fill='none' stroke='%239d94e0' stroke-width='3'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{EXTRA_CSS}
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

def org_ref():
    return {"@id": SITE + "/#organization"}

def build_post(p):
    url = f"/blog/{p['slug']}/"
    schema = [
      {"@context":"https://schema.org","@type":"BlogPosting",
       "headline": html.unescape(p["h1"]),
       "description": html.unescape(p["desc"]),
       "datePublished": p["date"], "dateModified": p["date"],
       "author": {"@type":"Person","name":AUTHOR},
       "publisher": org_ref(),
       "mainEntityOfPage": {"@type":"WebPage","@id": SITE+url},
       "image": SITE+"/og-image.png", "inLanguage":"en-IN"},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Blog","item":SITE+"/blog/"},
        {"@type":"ListItem","position":3,"name":html.unescape(p["h1"])}]},
    ]
    rel = " · ".join(f'<a href="{u}">{t}</a>' for t, u in p["related"])
    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><a href="/blog/">Blog</a><span class="crumbs__sep">/</span><span aria-current="page">{p['tag']}</span>
    </nav>
    <p class="postmeta"><span class="tagchip">{p['tag']}</span><span>{p['date']}</span><span>{AUTHOR}</span></p>
    <h1>{p['h1']}</h1>
    <p class="hero__lead">{p['lead']}</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <article class="post reveal">
      {p['body']}
      <p class="linkrow" style="margin-top:40px">Read next: {rel}</p>
    </article>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Get in touch</span>
      <h2 class="section-title">Hiring for something specific?</h2>
      <p class="section-lead">Tell us what the role is. You will get an honest read on the market, a realistic timeline, and a straight answer on whether we are the right firm for it, within one working day.</p>
      <p style="margin-top:26px"><a href="/#contact" class="btn btn--primary">Talk to us
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></p>
    </div>
  </div>
</section>
"""
    out = os.path.join(ROOT, "blog", p["slug"])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head(p["title"], p["desc"], url, schema) + body + TAIL)
    return url

def build_index():
    url = "/blog/"
    schema = [
      {"@context":"https://schema.org","@type":"Blog","@id":SITE+url,
       "name":"Animus Tech blog","url":SITE+url,"publisher":org_ref(),"inLanguage":"en-IN",
       "blogPost":[{"@type":"BlogPosting","headline":html.unescape(p["h1"]),
                    "url":f"{SITE}/blog/{p['slug']}/","datePublished":p["date"],
                    "author":{"@type":"Person","name":AUTHOR}} for p in POSTS]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Blog"}]},
    ]
    cards = "".join(f"""
      <a class="postcard reveal" href="/blog/{p['slug']}/">
        <p class="postmeta"><span class="tagchip">{p['tag']}</span><span>{p['date']}</span></p>
        <h2>{p['h1']}</h2>
        <p>{p['desc']}</p>
      </a>""" for p in POSTS)
    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Blog</span>
    </nav>
    <span class="eyebrow">Writing</span>
    <h1>Notes on hiring</h1>
    <p class="hero__lead">
      What we have learned running searches for software, manufacturing and consumer companies.
      Real numbers from our own work, including the searches that went long. Written for the
      person doing the hiring, not for other recruiters.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="postlist">{cards}</div>
  </div>
</section>
"""
    out = os.path.join(ROOT, "blog")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head("Notes on Hiring | Animus Tech",
             "Real numbers from our own searches, written for people doing the hiring. Agency fees, choosing a partner, and where recruitment time actually goes.",
             url, schema) + body + TAIL)
    return url

if __name__ == "__main__":
    for p in POSTS:
        print("wrote", build_post(p))
    print("wrote", build_index())
    print(f"\n{len(POSTS)} posts + index built.")
