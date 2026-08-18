#!/usr/bin/env python3
"""
Builds the interactive tool pages (they need inline JS, so they don't fit the
standard _build.py template). Re-runnable.

    python3 _build_tool.py
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_tpl_header.html')).read()
FOOTER = open(os.path.join(ROOT, '_tpl_footer.html')).read()
SITE = "https://animustech.in"

URL   = "/tools/cost-of-a-bad-hire-calculator/"
TITLE = "Cost of a Bad Hire Calculator (India) | Animus Tech"
DESC  = "Work out what a failed hire actually cost you. Salary, recruitment spend, ramp-up loss and management time, with every assumption editable."
H1    = "Cost of a Bad Hire Calculator"

schema = [
  {
    "@context": "https://schema.org", "@type": "WebApplication",
    "name": "Cost of a Bad Hire Calculator",
    "url": SITE + URL,
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Any",
    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
    "description": DESC,
    "publisher": {"@id": SITE + "/#organization"},
  },
  {
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
      {"@type": "ListItem", "position": 2, "name": "Tools", "item": SITE + "/tools/"},
      {"@type": "ListItem", "position": 3, "name": "Cost of a bad hire calculator"},
    ],
  },
  {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [
      {"@type": "Question", "name": "How much does a bad hire cost in India?",
       "acceptedAnswer": {"@type": "Answer", "text": "There is no single number, which is why this calculator asks for your figures rather than quoting a statistic. The cost is made up of salary paid to someone who did not work out, the cost of recruiting them, the productivity lost while they ramped up and then disengaged, the management and interview time spent, and the cost of doing it all again. For a mid-level role on 12 lakh CTC who leaves at month six, the total commonly lands between one and two times annual CTC once every component is counted."}},
      {"@type": "Question", "name": "What is the biggest hidden cost of a failed hire?",
       "acceptedAnswer": {"@type": "Answer", "text": "The vacancy period, both before and after. A role sitting open is work not being done, and it is rarely counted because no invoice is raised for it. The second largest is management time: the meetings, the performance conversations, the re-interviewing, none of which appear in a recruitment budget."}},
      {"@type": "Question", "name": "How do you reduce the risk of a bad hire?",
       "acceptedAnswer": {"@type": "Answer", "text": "Most failed hires trace back to a role that was never properly defined rather than a candidate who was badly sourced. Writing a scorecard with the hiring manager before sourcing begins, interviewing culture fit as behavioural history rather than hypotheticals, and staying engaged through the notice period all reduce it materially."}},
    ],
  },
]

schema_html = "\n".join(
    '<script type="application/ld+json">\n%s\n</script>' % json.dumps(s, indent=2, ensure_ascii=False)
    for s in schema)

CALC_CSS = """
<style>
.calc{display:grid;grid-template-columns:1fr 1fr;gap:34px;margin-top:36px;align-items:start}
@media(max-width:900px){.calc{grid-template-columns:1fr}}
.calc__panel{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px}
.calc__panel h3{margin:0 0 4px;font-size:1.05rem;color:var(--text)}
.calc__hint{margin:0 0 22px;color:var(--text-3);font-size:.88rem;line-height:1.6}
.f{margin-bottom:20px}
.f label{display:block;font-size:.9rem;color:var(--text-2);margin-bottom:7px;font-weight:500}
.f .sub{display:block;font-size:.78rem;color:var(--text-3);font-weight:400;margin-top:3px;line-height:1.5}
.f input[type=number]{width:100%;background:var(--bg-2);border:1px solid var(--border);
  border-radius:9px;padding:11px 13px;color:var(--text);font:inherit;font-size:.98rem}
.f input[type=number]:focus{outline:none;border-color:var(--accent)}
.f input[type=range]{width:100%;accent-color:var(--accent);margin-top:6px}
.rangeval{float:right;color:var(--accent);font-weight:600;font-size:.9rem}
.total{background:linear-gradient(160deg,rgba(157,148,224,.16),rgba(223,183,142,.08));
  border:1px solid var(--accent-line);border-radius:14px;padding:24px;margin-bottom:22px}
.total__label{margin:0;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase;color:var(--text-3)}
.total__n{margin:8px 0 4px;font-size:clamp(2rem,5vw,2.9rem);font-weight:800;color:var(--text);letter-spacing:-.02em}
.total__x{margin:0;font-size:.9rem;color:var(--accent-2)}
.brk{list-style:none;margin:0;padding:0}
.brk li{display:flex;justify-content:space-between;gap:14px;padding:11px 0;
  border-bottom:1px solid var(--border);font-size:.93rem}
.brk li:last-child{border-bottom:0}
.brk span:first-child{color:var(--text-2)}
.brk span:last-child{color:var(--text);font-weight:600;font-variant-numeric:tabular-nums}
.brk small{display:block;color:var(--text-3);font-size:.78rem;font-weight:400;margin-top:2px}
.note{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);
  color:var(--text-3);font-size:.84rem;line-height:1.7}
</style>
"""

CALC_JS = """
<script>
(function(){
  var f=['ctc','months','recruit','rampMonths','vacancy','mgmtHours','mgmtCtc'];
  function v(id){var e=document.getElementById(id);return parseFloat(e.value)||0;}
  function fmt(n){
    n=Math.round(n);
    if(n>=10000000) return '₹'+(n/10000000).toFixed(2)+' Cr';
    if(n>=100000)   return '₹'+(n/100000).toFixed(2)+' L';
    return '₹'+n.toLocaleString('en-IN');
  }
  function calc(){
    var ctc=v('ctc')*100000, months=v('months'), recruit=v('recruit')/100,
        ramp=v('rampMonths'), vac=v('vacancy'), mh=v('mgmtHours'), mctc=v('mgmtCtc')*100000;

    var monthly=ctc/12;
    var salary=monthly*months;
    var hireCost=ctc*recruit;
    // during ramp the person produces progressively; count half of ramp salary as lost output
    var rampLoss=monthly*Math.min(ramp,months)*0.5;
    var vacancyLoss=monthly*vac;
    var mgmtCost=(mctc/(12*22*8))*mh;
    var redo=hireCost;   // you pay to recruit the replacement too

    var total=salary+hireCost+rampLoss+vacancyLoss+mgmtCost+redo;

    document.getElementById('oTotal').textContent=fmt(total);
    document.getElementById('oX').textContent=ctc?('That is '+(total/ctc).toFixed(1)+'x the role\\u2019s annual CTC'):'';
    document.getElementById('oSalary').textContent=fmt(salary);
    document.getElementById('oHire').textContent=fmt(hireCost);
    document.getElementById('oRamp').textContent=fmt(rampLoss);
    document.getElementById('oVac').textContent=fmt(vacancyLoss);
    document.getElementById('oMgmt').textContent=fmt(mgmtCost);
    document.getElementById('oRedo').textContent=fmt(redo);

    document.getElementById('vMonths').textContent=months+(months===1?' month':' months');
    document.getElementById('vRecruit').textContent=v('recruit')+'%';
    document.getElementById('vRamp').textContent=v('rampMonths')+' mo';
    document.getElementById('vVac').textContent=v('vacancy')+' mo';
  }
  f.forEach(function(id){
    var e=document.getElementById(id);
    if(e){e.addEventListener('input',calc);e.addEventListener('change',calc);}
  });
  calc();
})();
</script>
"""

BODY = """
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Cost of a bad hire calculator</span>
    </nav>
    <span class="eyebrow">Free tool</span>
    <h1>Cost of a Bad Hire Calculator</h1>
    <p class="hero__lead">
      Most hiring budgets only count the agency fee. That is usually the smallest line.
      Put your own numbers in and see what a hire that did not work out actually cost,
      with every assumption visible and editable. Nothing is sent anywhere.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="calc">

      <div class="calc__panel reveal">
        <h3>Your numbers</h3>
        <p class="calc__hint">Defaults are a mid-level Indian role. Change anything that does not match your situation.</p>

        <div class="f">
          <label for="ctc">Annual CTC of the role (₹ lakh)</label>
          <input type="number" id="ctc" value="12" min="1" step="0.5">
        </div>

        <div class="f">
          <label for="months">Months they stayed <span class="rangeval" id="vMonths">6 months</span></label>
          <input type="range" id="months" value="6" min="1" max="24" step="1">
        </div>

        <div class="f">
          <label for="recruit">Recruitment cost, as % of CTC <span class="rangeval" id="vRecruit">12%</span>
            <span class="sub">Agency fee, job board spend, or your own team's time if hiring in house.</span></label>
          <input type="range" id="recruit" value="12" min="0" max="30" step="0.5">
        </div>

        <div class="f">
          <label for="rampMonths">Ramp-up period <span class="rangeval" id="vRamp">3 mo</span>
            <span class="sub">Months before someone in this role is fully productive.</span></label>
          <input type="range" id="rampMonths" value="3" min="0" max="12" step="1">
        </div>

        <div class="f">
          <label for="vacancy">Total months the seat sat empty <span class="rangeval" id="vVac">3 mo</span>
            <span class="sub">Before they joined, plus after they left, before the replacement started.</span></label>
          <input type="range" id="vacancy" value="3" min="0" max="12" step="1">
        </div>

        <div class="f">
          <label for="mgmtHours">Management &amp; interview hours spent</label>
          <input type="number" id="mgmtHours" value="60" min="0" step="5">
        </div>

        <div class="f">
          <label for="mgmtCtc">Average CTC of those managers (₹ lakh)</label>
          <input type="number" id="mgmtCtc" value="25" min="1" step="1">
        </div>
      </div>

      <div class="calc__panel reveal">
        <div class="total">
          <p class="total__label">Estimated total cost</p>
          <p class="total__n" id="oTotal">-</p>
          <p class="total__x" id="oX"></p>
        </div>

        <ul class="brk">
          <li><span>Salary paid<small>To someone who did not work out</small></span><span id="oSalary">-</span></li>
          <li><span>Cost to recruit them<small>Fee, ads, or internal time</small></span><span id="oHire">-</span></li>
          <li><span>Lost output during ramp-up<small>Counted at half productivity</small></span><span id="oRamp">-</span></li>
          <li><span>Vacancy cost<small>Work not being done at all</small></span><span id="oVac">-</span></li>
          <li><span>Management &amp; interview time<small>Costed at the managers' own rate</small></span><span id="oMgmt">-</span></li>
          <li><span>Cost to recruit again<small>You pay for the replacement too</small></span><span id="oRedo">-</span></li>
        </ul>

        <p class="note">
          <strong>How this is calculated.</strong> Salary is monthly CTC times months served.
          Ramp-up loss counts the ramp period at half productivity, which is deliberately
          conservative. Vacancy cost values an empty seat at the role's own monthly cost.
          Management time is costed at the managers' actual hourly rate, assuming 22 working
          days and 8 hour days. Recruitment cost is counted twice, because you pay to fill the
          seat and then pay again to refill it.
          <br><br>
          There is no industry multiplier baked in and no study being quoted at you. Every
          input is yours and every assumption is stated. Treat the output as an order of
          magnitude, not an invoice.
        </p>
      </div>

    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">What the number means</span>
      <h2 class="section-title">The agency fee is the cheapest part</h2>
      <p class="section-lead">Which is exactly why choosing on fee alone is expensive.</p>
    </div>
    <div class="prose reveal">
      <p>
        Run the calculator with a realistic set of numbers and the recruitment fee usually
        lands somewhere between a tenth and a fifth of the total. The expensive lines are the
        ones nobody invoices you for: the salary paid to someone who was never going to work
        out, the months the seat sat empty, and the management hours spent on a problem that a
        better-defined role would have prevented.
      </p>
      <p>
        That is the case for spending more time before the search, not less. Most failed hires
        trace back to a role that was never properly defined rather than a candidate who was
        badly sourced. A scorecard written with the hiring manager before sourcing starts costs
        an hour. The alternative is on the screen above.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Questions</span>
      <h2 class="section-title">Frequently asked</h2>
    </div>
    <div class="faq reveal">
      <details><summary>How much does a bad hire cost in India?</summary>
        <p>There is no single number, which is why this calculator asks for your figures rather than quoting a statistic. The cost is made up of salary paid to someone who did not work out, the cost of recruiting them, the productivity lost while they ramped up and then disengaged, the management and interview time spent, and the cost of doing it all again. For a mid-level role on 12 lakh CTC who leaves at month six, the total commonly lands between one and two times annual CTC once every component is counted.</p></details>
      <details><summary>What is the biggest hidden cost of a failed hire?</summary>
        <p>The vacancy period, both before and after. A role sitting open is work not being done, and it is rarely counted because no invoice is raised for it. The second largest is management time: the meetings, the performance conversations, the re-interviewing, none of which appear in a recruitment budget.</p></details>
      <details><summary>How do you reduce the risk of a bad hire?</summary>
        <p>Most failed hires trace back to a role that was never properly defined rather than a candidate who was badly sourced. Writing a scorecard with the hiring manager before sourcing begins, interviewing culture fit as behavioural history rather than hypotheticals, and staying engaged through the notice period all reduce it materially.</p></details>
      <details><summary>Is this calculator storing my numbers?</summary>
        <p>No. Everything runs in your browser. Nothing is sent to a server, nothing is logged, and there is no form to fill in before you see the result.</p></details>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Get in touch</span>
      <h2 class="section-title">Rather not run this calculator again</h2>
      <p class="section-lead">
        We define the role before we source it, screen every candidate against a scorecard
        agreed with your hiring manager, and stay engaged through the notice period. Tell us
        what you are hiring for.
      </p>
      <p style="margin-top:26px">
        <a href="/talent-acquisition/#contact" class="btn btn--primary">Start hiring with us
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </p>
      <p class="linkrow reveal">See also:
        <a href="/recruitment-agency-pune/">Recruitment agency in Pune</a> ·
        <a href="/services/hiring-advisory/">Hiring advisory</a> ·
        <a href="/talent-acquisition-firm-pune/">Talent acquisition firm in Pune</a>
      </p>
    </div>
  </div>
</section>
"""

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}{URL}">

<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE}{URL}">
<meta property="og:image" content="{SITE}/og-image.png">

<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 54 40'><rect width='54' height='40' rx='7' fill='%23141824'/><circle cx='19' cy='20' r='14' fill='none' stroke='%23dfb78e' stroke-width='3'/><circle cx='35' cy='20' r='14' fill='none' stroke='%239d94e0' stroke-width='3'/></svg>">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{CALC_CSS}
{schema_html}
</head>
<body>

<div class="progress" aria-hidden="true"><div class="progress__bar" id="progressBar"></div></div>

{HEADER}

<main id="top">
{BODY}
</main>

{FOOTER}

<script src="/assets/site.js" defer></script>
{CALC_JS}
</body>
</html>
"""

out = os.path.join(ROOT, "tools", "cost-of-a-bad-hire-calculator")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "index.html"), "w") as fh:
    fh.write(PAGE)
print("wrote", URL + "index.html")
