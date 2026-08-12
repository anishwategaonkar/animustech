# -*- coding: utf-8 -*-
"""Content for the generated SEO landing pages. Edit here, then run _build.py."""

def sec(eyebrow, title, lead, body="", alt=False):
    cls = "section section--alt" if alt else "section"
    lead_html = f'<p class="section-lead">{lead}</p>' if lead else ""
    return f'''
<section class="{cls}">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2 class="section-title">{title}</h2>
      {lead_html}
    </div>
    {body}
  </div>
</section>'''

def cards(items):
    inner = "".join(
        f'<div class="benefit reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in items
    )
    return f'<div class="benefits">{inner}</div>'

def rolegrid(groups):
    inner = ""
    for title, roles in groups:
        lis = "".join(f"<li>{r}</li>" for r in roles)
        inner += f'<div class="reveal"><h3>{title}</h3><ul>{lis}</ul></div>'
    return f'<div class="rolegrid">{inner}</div>'

def prose(paras):
    return '<div class="prose reveal">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"

def faq_html(pairs):
    inner = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs
    )
    return f'<div class="faq reveal">{inner}</div>'

def links(label, pairs):
    ls = " · ".join(f'<a href="{u}">{t}</a>' for t, u in pairs)
    return f'<p class="linkrow reveal">{label} {ls}</p>'


# ============================================================== FAQ content ==
RAP_FAQ = [
    ("What does a recruitment agency in Pune charge?",
     "Most Pune recruitment agencies charge a contingency fee of 8.33% to 16.67% of the candidate's annual CTC, "
     "payable on joining, with a replacement guarantee of 60 to 90 days. Leadership and executive search is usually "
     "retained, billed in stages. Volume hiring is typically priced per hire at a lower rate. We scope fees to the "
     "role rather than applying a flat rate, and confirm them in writing at intake."),
    ("How long does it take to fill a role in Pune?",
     "A first shortlist typically reaches you within 5 to 7 working days. Time to offer depends on the role: "
     "mid-level software and manufacturing roles usually close in 3 to 5 weeks, leadership and niche searches in "
     "6 to 10 weeks. Notice periods in India then add 30 to 90 days before joining, which is why joining ratio "
     "matters more than offer count."),
    ("Which industries does Animus Tech recruit for?",
     "Software and technology, manufacturing and engineering, and D2C and consumer brands. We stay narrow "
     "deliberately, because knowing what a good hire looks like in a specific sector is most of the value a "
     "recruiter adds, and it is what our screening criteria are trained on."),
    ("How is AI used in your recruitment process?",
     "In three places. Sourcing uses semantic matching to find candidates whose actual experience fits the role, "
     "including people whose CV never uses your exact terminology. Screening reads every profile against the "
     "scorecard agreed at intake and writes out the reasoning for each ranking. Assessment runs role specific "
     "skill tests scored on the same rubric for every candidate. A recruiter reviews every shortlist before it "
     "reaches you, and no candidate is ever rejected by software alone."),
    ("Do you hire for manufacturing plants around Pune?",
     "Yes. We recruit across the Pune industrial corridor including Chakan, Talegaon, Ranjangaon, Bhosari and "
     "Pimpri-Chinchwad, covering design and R&D, production, quality, maintenance, supply chain and plant "
     "leadership. Plant hiring has its own rules around shift realities, commute distance and joining ratios, "
     "and we screen for those explicitly rather than treating it as generic hiring."),
    ("What is the difference between a recruitment agency and a talent acquisition firm?",
     "In practice the terms overlap, but the distinction that matters is scope. A recruitment agency typically "
     "fills a defined vacancy you hand over. A talent acquisition firm engages earlier: defining the role, "
     "building the scorecard, mapping the market, and advising on compensation and interview design. We work the "
     "second way, because most failed hires trace back to a badly defined role rather than a badly sourced candidate."),
]


# ==================================================================== PAGES ==
PAGES = [

# ---------------------------------------------------- 1. MONEY PAGE ---------
{
 "url": "/recruitment-agency-pune/",
 "title": "Recruitment Agency in Pune | Animus Tech",
 "desc": "AI enabled recruitment agency in Pune for software, manufacturing and D2C hiring. Shortlists in 5 to 7 days, screened for skills and culture fit.",
 "crumbs": [("Home", "/"), ("Recruitment agency in Pune", None)],
 "eyebrow": "Pune · Maharashtra",
 "h1": "Recruitment Agency in Pune for Software, Manufacturing &amp; D2C",
 "lead": ("Animus Tech is an AI enabled recruitment agency in Pune. Our AI sources, screens and assesses "
          "candidates at a scale no manual team can match. Our recruiters then do the part software still "
          "cannot: judging whether a person will genuinely work well inside your team. What reaches your "
          "inbox is a short list, not a stack of resumes."),
 "faq": RAP_FAQ,
 "body":
   sec("Why us", "Why companies in Pune work with us",
       "Most recruitment agencies in Pune compete on volume. We compete on what reaches your inbox.",
       prose([
         "Most agencies forward whatever the job board returns and let you do the filtering. That model has a "
         "hard ceiling, because one recruiter can only read so many profiles in a day, and the ones they read "
         "first are not necessarily the best ones.",
         "We work backwards from the shortlist. At intake we build a scorecard with your hiring manager, "
         "describing what good actually looks like for this role, in your team, at your stage. Every candidate "
         "is then screened against that scorecard rather than a generic template, assessed on role specific "
         "skills, and interviewed for culture fit by a recruiter. You see the few who cleared the bar, with "
         "the reasoning written out.",
       ]) +
       cards([
         ("Faster hiring", "You interview candidates who have already cleared the bar, not a pile of maybes. First shortlists land in 5 to 7 working days."),
         ("Better fit", "Skills and culture checked upfront, not discovered three months in when the person quietly disengages."),
         ("Less noise", "Fewer resumes, higher signal. Less scrolling, less second guessing, fewer interview slots wasted."),
       ]), alt=True) +

   sec("Proof", "How a recent search actually ran",
       "One real search, start to finish, with the actual numbers.",
       cards([
         ("40+ screened, 8 sent",
          "We read more than forty profiles. The client saw eight, in two batches of four. The work happens before your inbox, not in it."),
         ("10 days",
          "From intake to a signed offer, across three interview rounds, the last of them with the board."),
         ("25 days",
          "Intake to the person actually starting. The other 15 days were their notice period, which no agency can compress."),
       ]) +
       prose([
         "The role was a sales associate with an electronics background and industrial sales exposure. "
         "More than forty profiles were screened to produce a shortlist of eight, and the person who "
         "joined came from the second batch of four. That ratio is the whole argument: eight submittals "
         "per hire, against an industry norm where ten to twenty is common and some agencies send far "
         "more. Batching four at a time meant the client reviewed a small set, gave feedback, and we "
         "adjusted before the second batch rather than burying them in profiles and hoping something landed.",
         "One of those candidates is worth describing. Their CV was a single page listing education, a "
         "company name and an internship name. No responsibilities, no achievements, nothing a keyword "
         "search could match against. A recruiter filtering on terms would never have seen them, because "
         "keyword search scores the document rather than the person. Semantic screening surfaced them "
         "anyway, and a recruiter then made the call on whether they were right for the role.",
       ]) +
       links("Read more:", [("How our AI screening works", "/#ai"),
                            ("AI assessment as a service", "/services/ai-candidate-assessment/")])) +

   sec("What we do", "Recruitment services we offer in Pune", "",
       cards([
         ('<a href="/services/permanent-recruitment/">Permanent recruitment</a>',
          "End to end hiring for full time roles, from role definition through to offer acceptance and joining."),
         ('<a href="/services/executive-search/">Leadership &amp; niche search</a>',
          "Confidential search for senior and specialist roles where the pool is small and mostly not looking."),
         ('<a href="/services/bulk-hiring/">Volume &amp; project hiring</a>',
          "Structured drives when you need many people in one window: a new plant, a new shift, festive season or a funding led scale up."),
         ('<a href="/services/ai-candidate-assessment/">AI assessment as a service</a>',
          "Already have a pipeline? Send us your candidates and we return a scored report on each."),
         ('<a href="/services/hiring-advisory/">Hiring advisory</a>',
          "Job descriptions that attract the right people, interview loops that actually discriminate, and honest salary benchmarks for the Pune market."),
       ])) +

   sec("Where we specialise", "Industries we recruit for",
       "We stay narrow on purpose. Knowing what a good hire looks like in your sector is most of the value a "
       "recruiter adds, and it is also what we train our screening criteria on. A generalist agency is guessing.",
       cards([
         ('<a href="/industries/it-software-recruitment-pune/">Software &amp; technology</a>',
          "Engineering, data, product, design, QA, DevOps and SRE across Hinjewadi, Kharadi, Magarpatta and Baner, for product companies, SaaS teams, GCCs and services firms."),
         ('<a href="/industries/manufacturing-recruitment-pune/">Manufacturing &amp; engineering</a>',
          "Design, R&amp;D and NPD through production, quality, maintenance and plant leadership, across the Chakan, Talegaon, Ranjangaon and Pimpri-Chinchwad belt."),
         ('<a href="/industries/d2c-consumer-recruitment/">D2C &amp; consumer brands</a>',
          "Growth, performance marketing, category and brand, supply chain and founder's office roles for fast moving consumer brands."),
       ]), alt=True) +

   sec("Coverage", "Areas we cover around Pune", "",
       prose([
         "We recruit across Pune city and the surrounding industrial and technology corridors, including "
         "Hinjewadi, Kharadi, Magarpatta, Baner, Viman Nagar, Pimpri-Chinchwad, Bhosari, Chakan, Talegaon and "
         "Ranjangaon. For leadership and niche roles we search nationally and relocate candidates into Pune "
         "where the local pool is genuinely thin, which for some specialisms it is.",
       ])) +

   sec("Questions", "Frequently asked questions", "", faq_html(RAP_FAQ), alt=True),
},

# ------------------------------------------- 2. TALENT ACQUISITION FIRM -----
{
 "url": "/talent-acquisition-firm-pune/",
 "title": "Talent Acquisition Firm in Pune | Animus Tech",
 "desc": "Talent acquisition firm in Pune working from role definition through to joining. Market mapping, scorecard design, AI screening and culture fit assessment.",
 "crumbs": [("Home", "/"), ("Talent acquisition firm in Pune", None)],
 "eyebrow": "Pune · Maharashtra",
 "h1": "Talent Acquisition Firm in Pune",
 "lead": ("Most failed hires trace back to a badly defined role, not a badly sourced candidate. We engage "
          "before the search starts, building the scorecard and mapping the market, then run AI powered "
          "sourcing and screening against it with human judgement on culture fit."),
 "body":
   sec("The distinction", "Recruitment agency, or talent acquisition partner?",
       "The terms overlap in everyday use. The difference that actually matters is where the engagement starts.",
       prose([
         "A recruitment agency typically receives a vacancy that has already been defined and fills it. The job "
         "description arrives, candidates go out, the role closes or it does not. It is a transaction, and for "
         "straightforward roles it works.",
         "A talent acquisition firm engages a step earlier. Before anyone is sourced, we work out what the role "
         "actually needs to accomplish in its first year, what the team it joins is genuinely like to work "
         "inside, what the market will bear on compensation, and how the interview loop should be built to "
         "discriminate between candidates rather than simply tire them out.",
         "That earlier engagement is where most of the leverage sits. A search executed flawlessly against a "
         "vague scorecard still produces the wrong hire, and by the time that becomes visible you have lost "
         "six months and a salary.",
       ]), alt=True) +

   sec("Where hiring breaks", "Four failure points we design around", "",
       cards([
         ("The role was never properly defined", "Everyone agreed on the title and nobody agreed on the outcome. We write the scorecard with your hiring manager before sourcing begins."),
         ("Culture fit was assumed", "Technical evaluation is close to solved. How someone handles disagreement, ambiguity or a slipped deadline goes unmeasured, and that is where hires quietly fail."),
         ("The market was never mapped", "Compensation set from an outdated benchmark produces a search that cannot close. We tell you at intake if the band will not clear."),
         ("The process lost the candidate", "Slow feedback, an unstructured loop and a counter-offer at notice. We manage the close, not just the shortlist."),
       ])) +

   sec("How we engage", "What you get at each stage", "",
       rolegrid([
         ("Intake &amp; scorecard", ["Hiring manager working session", "Success criteria for year one", "Written scorecard the AI screens against", "Honest read on the compensation band"]),
         ("Market map", ["Where the talent actually sits", "Realistic pool size", "Competitor and comparator companies", "Timeline you can plan around"]),
         ("Search &amp; assess", ["Semantic AI sourcing", "Every profile screened, not the first fifty", "Role specific skill assessment", "Structured culture fit interview"]),
         ("Close &amp; joining", ["Scheduling and feedback loops", "Offer negotiation support", "Notice period engagement", "Contact through onboarding"]),
       ]), alt=True) +

   sec("Who we work with", "Three industries, three different games",
       "We stay narrow because sector knowledge is what our screening criteria are built on.",
       cards([
         ('<a href="/industries/it-software-recruitment-pune/">Software &amp; technology</a>', "Product companies, SaaS teams, GCCs and services firms across the Pune tech corridor."),
         ('<a href="/industries/manufacturing-recruitment-pune/">Manufacturing &amp; engineering</a>', "Automotive, capital equipment, precision engineering and EV across the Pune industrial belt."),
         ('<a href="/industries/d2c-consumer-recruitment/">D2C &amp; consumer</a>', "Fast moving brands who need people that can own a number without a playbook."),
       ]) +
       links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                           ("Hiring advisory", "/services/hiring-advisory/")])),
},

# ------------------------------------------- 2b. HOW WE WORK ---------------
{
 "url": "/how-we-work/",
 "title": "How We Work | Animus Tech",
 "desc": "Our process, our numbers, and what we commit to in writing. 40+ screened, 8 shared, 1 hired. A written update every Friday, progress or not.",
 "crumbs": [("Home", "/"), ("How we work", None)],
 "eyebrow": "Process &amp; commitments",
 "h1": "How We Work",
 "lead": ("Every recruitment agency says quality and speed. Almost none of them show you a "
          "number. This page is our process, the numbers from our work so far, and what we "
          "commit to in writing, including what we need from you for any of it to hold."),
 "body":
   sec("The numbers", "What a shortlist actually means here",
       "Fewer resumes only means rigour if you can see what was filtered out. So here is the whole funnel.",
       cards([
         ("40+", "Profiles screened against the scorecard agreed at intake. Every one read, not just the first fifty returned by a search."),
         ("8", "Shared with the client, in two deliberate batches of four."),
         ("1", "Hired, from the second batch. Eight submittals per hire."),
       ]) +
       prose([
         "Eight submittals to one hire. The common industry range is ten to twenty per hire, and "
         "plenty of agencies send considerably more, because when you are paid only on placement "
         "the rational move is to flood several clients and see what sticks. The cost of that "
         "model is not paid by the agency. It is paid by the hiring manager reading forty CVs on "
         "a Sunday.",
         "We batch instead. Four profiles, then a real conversation about what was right and wrong "
         "about them, then four more shaped by that feedback. It is slower to start and faster to "
         "finish, and it means the second batch is genuinely better than the first rather than "
         "just longer.",
         "<strong>On sample size:</strong> this is one completed search. We are a new firm and we "
         "would rather show you one real funnel than quote an industry statistic we did not "
         "measure. These numbers will be updated as more searches close, including the ones that "
         "go badly.",
       ]), alt=True) +

   sec("Our commitments", "What we commit to, in writing", "",
       cards([
         ("A written update every Friday",
          "Progress or no progress. A week with nothing to report is itself information, and you should not have to chase us for it."),
         ("An honest read at intake",
          "If we think the compensation band will not clear the market, we tell you in week one, not week six. It is a harder conversation early and a much cheaper one."),
         ("We will tell you if the role is wrong",
          "If the job description will not attract who you actually need, we say so before sourcing starts. You are paying us for judgement, not agreement."),
         ("Reservations included",
          "Every shortlist carries a written view on each candidate, with the concerns stated. A shortlist where everyone looks perfect is a shortlist that has not been thought about."),
       ])) +

   sec("The honest part", "Where hiring actually slows down",
       "Most delay in recruitment is not sourcing. It is the two sides not staying in step.",
       prose([
         "Search timelines slip for reasons that have very little to do with finding people. The "
         "mandate changes halfway through. The scorecard agreed at intake quietly becomes a "
         "different role. Feedback on a batch takes eleven days, by which point two of the four "
         "have accepted something else. An input nobody thought to mention at intake, a shift "
         "pattern, a travel expectation, a reporting line, surfaces at final interview and "
         "invalidates half the pipeline.",
         "None of that is anyone behaving badly. Hiring managers are busy and roles genuinely "
         "evolve. But it is why we will not promise you a fixed number of days and pretend the "
         "outcome rests entirely on us. What we will promise is that when something slips, you "
         "hear about it on Friday with the cause named plainly, whether the cause is on our side "
         "or yours, and with a proposed fix attached.",
         "That is the part we control completely, and it is the part we hold ourselves to. A "
         "process followed honestly survives a mandate change. A promise of speed does not.",
       ]), alt=True) +

   sec("What we need from you", "The other half of the process", "",
       rolegrid([
         ("At intake", ["45 minutes with the actual hiring manager, not a forwarded JD",
                        "What success looks like in year one",
                        "The real compensation band, including flexibility",
                        "Any non-negotiable: shift, location, travel, reporting line"]),
         ("During the search", ["Feedback on a batch within 3 working days",
                                "A named decision maker who can say yes",
                                "Interview slots held in advance, not found later",
                                "Early warning if the mandate changes"]),
         ("At offer", ["A decision within the agreed window",
                       "Offer released promptly once verbally agreed",
                       "Someone from the team in contact during notice",
                       "A joining day that is actually ready"]),
       ]) +
       prose([
         "None of this is unusual. It is written down because writing it down is what stops a "
         "search quietly drifting, and because a client who cannot commit to three-day feedback "
         "is better off knowing that at intake than at week eight.",
       ]) +
       links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                           ("Cost of a bad hire calculator", "/tools/cost-of-a-bad-hire-calculator/"),
                           ("Hiring advisory", "/services/hiring-advisory/")])),
 "cta_title": "Want this run on your role?",
 "cta_lead": ("Tell us what you are hiring for. You will get an honest read on the market, a "
              "realistic timeline, and a straight answer on whether we are the right firm for it, "
              "within one working day."),
},

# ------------------------------------------------- 3. MANUFACTURING ---------
{
 "url": "/industries/manufacturing-recruitment-pune/",
 "title": "Manufacturing Recruitment Agency in Pune | Animus Tech",
 "desc": "Manufacturing recruitment across Pune, Chakan, Talegaon and Ranjangaon. Production, quality, maintenance and plant leadership, screened for joining ratio.",
 "crumbs": [("Home", "/"), ("Recruitment agency in Pune", "/recruitment-agency-pune/"), ("Manufacturing recruitment", None)],
 "eyebrow": "Chakan · Talegaon · Ranjangaon · Pimpri-Chinchwad",
 "h1": "Manufacturing &amp; Engineering Recruitment in Pune",
 "lead": ("Pune sits in one of India's densest industrial corridors. Plant hiring here has its own rules, and "
          "most recruitment agencies apply software hiring logic to it and wonder why the offer acceptance "
          "rate is poor. We screen for the things that actually decide whether someone joins and stays."),
 "body":
   sec("The real problem", "Why plant hiring breaks generic recruitment",
       "A CV tells you whether someone can do the job. In manufacturing, that is rarely the thing that goes wrong.",
       prose([
         "What goes wrong is the offer declined three days before joining, or the maintenance engineer who "
         "leaves in month four because the commute from Wakad to Ranjangaon turned out to be ninety minutes "
         "each way in monsoon. Four factors decide manufacturing hires, and none of them are visible on a resume.",
       ]) +
       cards([
         ("Commute reality", "Plant locations in Chakan, Talegaon and Ranjangaon are an hour or more from most residential Pune. Company transport routes, shift timings and where the candidate actually lives decide whether an offer sticks. We check this at screening, not after the offer."),
         ("Shift tolerance", "Rotational shifts, night shifts and six day weeks are ordinary in production and maintenance. A candidate who has only worked general shift will often accept and then reconsider. We ask directly and verify against their history."),
         ("Counter-offer exposure", "Notice periods of 60 to 90 days give the current employer a long window. We track engagement through the notice period rather than closing the file at offer acceptance."),
         ("Process discipline", "An engineer from an unstructured shop floor moving into a tier-1 supplier with audited processes is a real transition. It is screenable, and it is usually not screened."),
       ]), alt=True) +

   sec("Roles", "Roles we hire for", "",
       rolegrid([
         ("Design, R&amp;D &amp; NPD", ["Design engineers — CAD, CAE, GD&amp;T", "NPD and product development", "Simulation and validation", "Tooling and fixture design"]),
         ("Production &amp; operations", ["Production engineers, shift in-charge", "Industrial engineering, lean, TPM", "Assembly and machine shop leadership", "Plant and manufacturing managers"]),
         ("Quality &amp; maintenance", ["QA, QC and supplier quality", "Customer quality and warranty", "Mechanical, electrical, instrumentation", "Reliability and preventive maintenance"]),
         ("Supply chain &amp; sourcing", ["Strategic sourcing, vendor development", "Production planning and materials", "Logistics and warehousing", "Costing and should-costing"]),
       ])) +

   sec("Sectors", "Sectors within manufacturing", "",
       prose([
         "Automotive and auto components, industrial and capital equipment, electrical and electronics, "
         "precision engineering and machining, EV and battery systems, packaging, and process industries. "
         "The Pune belt is dense in tier-1 and tier-2 auto suppliers, and hiring patterns there differ "
         "meaningfully from capital equipment or process plants. We scope the search accordingly.",
       ]), alt=True) +

   sec("Our AI", "How AI helps in manufacturing hiring specifically", "",
       prose([
         "Manufacturing CVs are harder to read than software CVs. Job titles are inconsistent across companies, "
         "the same responsibility appears under five different names, and capability is often buried in a line "
         "about a project rather than stated as a skill. Keyword search fails badly here.",
         "Our AI reads for meaning rather than terminology. A candidate who ran a line balancing exercise and "
         "cut cycle time surfaces for an industrial engineering role even if their CV never contains the phrase. "
         "Every profile is scored against the scorecard we built with your plant head, with the reasoning "
         "written out, and a recruiter reviews the shortlist before it reaches you.",
       ])) +

   sec("Coverage", "Locations we cover", "",
       prose([
         "Chakan MIDC, Talegaon MIDC, Ranjangaon MIDC, Bhosari MIDC, Pimpri-Chinchwad, Hinjewadi, Shirwal, "
         "Baramati and the wider Pune–Nashik and Pune–Mumbai industrial corridors. For plant leadership and "
         "specialist roles we search nationally, since the local pool for some specialisms is genuinely thin.",
       ]) +
       links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                           ("Volume &amp; project hiring", "/services/bulk-hiring/"),
                           ("IT &amp; software recruitment", "/industries/it-software-recruitment-pune/")]),
       alt=True),
 "cta_title": "Hiring for a plant in the Pune belt?",
 "cta_lead": ("Tell us the role, the location and the shift pattern. We will come back within one working day "
              "with a view on the local pool, a realistic timeline, and an honest read on whether the "
              "compensation band will clear."),
},

# ---------------------------------------------------- 4. IT / SOFTWARE ------
{
 "url": "/industries/it-software-recruitment-pune/",
 "title": "IT Recruitment Consultancy in Pune | Animus Tech",
 "desc": "IT and software recruitment in Pune. Backend, frontend, data, ML, cloud, DevOps and engineering leadership for product companies, SaaS teams and GCCs.",
 "crumbs": [("Home", "/"), ("Recruitment agency in Pune", "/recruitment-agency-pune/"), ("IT &amp; software recruitment", None)],
 "eyebrow": "Hinjewadi · Kharadi · Magarpatta · Baner",
 "h1": "IT &amp; Software Recruitment in Pune",
 "lead": ("Engineering, data, product, design, QA, DevOps and SRE for product companies, SaaS teams, GCCs and "
          "services firms. We read a stack seriously and do not confuse keyword matches with capability."),
 "body":
   sec("The core problem", "Why keyword matching fails on engineering CVs",
       "The best candidate for your role often does not use your vocabulary.",
       prose([
         "An engineer who spent three years building an event driven order pipeline may never write the word "
         "Kafka on their CV, because at their company the internal system had a different name. A keyword "
         "search returns zero. A hiring manager reading the same CV would flag them in thirty seconds.",
         "That gap is the single largest source of waste in technical recruitment, and it gets worse as you go "
         "senior, because senior engineers describe outcomes rather than tools. Our AI reads a role the way a "
         "hiring manager would and matches on demonstrated capability, then writes out why each candidate "
         "ranked where they did, including the gaps worth asking about in interview.",
       ]), alt=True) +

   sec("Roles", "Roles we hire for", "",
       rolegrid([
         ("Engineering", ["Backend, frontend, full stack", "Mobile — iOS, Android, React Native", "Architects and principal engineers", "Engineering managers and directors"]),
         ("Data &amp; AI", ["Data engineering and platforms", "Machine learning and MLOps", "Analytics and business intelligence", "Data science"]),
         ("Infrastructure", ["Cloud — AWS, Azure, GCP", "DevOps, SRE and platform engineering", "Security and application security", "Database and reliability"]),
         ("Product &amp; quality", ["Product management", "Product design and UX", "QA and automation", "Technical program management"]),
       ])) +

   sec("Who we hire for", "Product companies, SaaS, GCCs and services firms",
       "The same title means different things across these four, and screening should reflect that.",
       cards([
         ("Product companies &amp; SaaS", "Smaller teams where individual ownership is high and a mis-hire is felt immediately. We screen hard for autonomy and for people who have shipped rather than maintained."),
         ("Global capability centres", "Pune has one of India's largest GCC concentrations. Hiring here turns on whether a candidate can operate across time zones with a distant parent org, which is a distinct skill from working in a colocated team."),
         ("Services &amp; consulting firms", "Client facing delivery under commercial pressure. Breadth, ramp-up speed and communication carry more weight than depth in any single stack."),
       ]), alt=True) +

   sec("Coverage", "Pune technology locations", "",
       prose([
         "Hinjewadi Phases 1, 2 and 3, Kharadi and EON, Magarpatta and Hadapsar, Baner and Balewadi, Viman "
         "Nagar, Yerwada and the Pune city centre. We also place remote and hybrid roles nationally where the "
         "team is distributed, which for engineering it increasingly is.",
       ]) +
       links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                           ("Leadership &amp; executive search", "/services/executive-search/"),
                           ("AI candidate assessment", "/services/ai-candidate-assessment/")])),
},

# ------------------------------------------------------------- 5. D2C -------
{
 "url": "/industries/d2c-consumer-recruitment/",
 "title": "D2C &amp; Consumer Brand Recruitment | Animus Tech",
 "desc": "Hiring for D2C and consumer brands across India. Growth, performance marketing, category, supply chain and founder's office roles, screened for ownership.",
 "crumbs": [("Home", "/"), ("Recruitment agency in Pune", "/recruitment-agency-pune/"), ("D2C &amp; consumer", None)],
 "eyebrow": "India wide",
 "h1": "D2C &amp; Consumer Brand Recruitment",
 "lead": ("Fast moving brands need people who can own a number without a playbook. We look for ownership and "
          "comfort with ambiguity, not just a familiar logo on the CV."),
 "body":
   sec("The core problem", "Why brand-name pedigree misleads in D2C",
       "The same job title describes two completely different people.",
       prose([
         "Someone who ran paid social at a large consumer company had a large budget, an agency executing, a "
         "brand that people already searched for, and a analytics team answering questions. Someone who ran "
         "paid social at a young D2C brand had a small budget, built the creative themselves, and found out "
         "within a week whether it worked because the money was visibly gone.",
         "Both CVs say performance marketing. Only one of them has done the job you are hiring for. We screen "
         "for what someone owned and what happened when it went wrong, rather than where they did it.",
       ]), alt=True) +

   sec("Roles", "Roles we hire for", "",
       rolegrid([
         ("Growth &amp; marketing", ["Performance marketing and paid media", "Growth and retention", "CRM and lifecycle", "Content, social and influencer"]),
         ("Category &amp; brand", ["Category management", "Brand management", "Product and merchandising", "Pricing and revenue"]),
         ("Operations &amp; supply chain", ["Supply chain and planning", "Warehousing and fulfilment", "Procurement and vendor management", "Quality and sourcing"]),
         ("Leadership", ["Founder's office and chief of staff", "Business unit and P&amp;L leadership", "Head of growth, head of brand", "Operations leadership"]),
       ])) +

   sec("How we assess", "Screening for ambiguity tolerance", "",
       prose([
         "Comfort with ambiguity is treated as a personality trait and interviewed for with hypotheticals, "
         "which candidates learn to answer. We interview it as history instead: a specific time the plan was "
         "wrong, what they did in the first week after realising, and what they would do differently. The "
         "answers separate people quickly, and they are hard to rehearse.",
         "Every shortlist includes a written view on fit with reservations included. You get an honest read, "
         "not a sales pitch.",
       ]) +
       links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                           ("Talent acquisition firm in Pune", "/talent-acquisition-firm-pune/")]),
       alt=True),
},

]


# ================================================== SERVICE PAGES (compact) ==
def service_page(url, title, desc, h1, eyebrow, lead, what, when, get, service_name):
    return {
        "url": url, "title": title, "desc": desc, "h1": h1, "eyebrow": eyebrow, "lead": lead,
        "service": service_name,
        "crumbs": [("Home", "/"), ("Recruitment agency in Pune", "/recruitment-agency-pune/"), (h1, None)],
        "body":
            sec("What it is", "What this covers", "", prose(what), alt=True) +
            sec("When you need it", "When companies come to us for this", "", cards(when)) +
            sec("What you get", "What you get", "", rolegrid(get) +
                links("See also:", [("Recruitment agency in Pune", "/recruitment-agency-pune/"),
                                    ("Talent acquisition firm in Pune", "/talent-acquisition-firm-pune/")]),
                alt=True),
    }


PAGES += [

service_page(
 "/services/permanent-recruitment/",
 "Permanent Recruitment Agency in Pune | Animus Tech",
 "End to end permanent recruitment in Pune. AI sourcing, ranked shortlists with written rationale, and support through offer, notice period and joining.",
 "Permanent Recruitment", "Service",
 "End to end hiring for full time roles, from role definition through to offer acceptance and joining.",
 ["Our core engagement. We take a role from an initial conversation with the hiring manager through to the "
  "candidate walking in on day one, and we stay involved through the notice period, which in India is where "
  "a surprising number of searches quietly fail.",
  "Every candidate is sourced with semantic AI search, screened against the scorecard we agreed at intake, "
  "assessed on role specific skills, and interviewed for culture fit by a recruiter. Nobody is rejected by "
  "software alone, and every shortlist carries a written rationale you can argue with."],
 [("You have tried and the pipeline is thin", "The role has been open for weeks, applicants are not matching, and the internal team does not have the hours to source actively."),
  ("The role is hard to define", "Everyone agrees the hire is needed and nobody agrees what good looks like. We write the scorecard before sourcing starts."),
  ("You cannot afford a mis-hire", "Small team, senior seat, or a role with real commercial consequences attached to it.")],
 [("At intake", ["Hiring manager session", "Written scorecard", "Compensation reality check", "Realistic timeline"]),
  ("During search", ["Semantic AI sourcing", "Every profile screened", "Skill assessment", "Culture fit interview"]),
  ("On shortlist", ["Ranked candidates", "Written rationale for each", "Flagged gaps and questions", "Assessment scores"]),
  ("Through close", ["Scheduling and feedback", "Offer negotiation", "Notice period engagement", "Onboarding contact"])],
 "Permanent recruitment"),

service_page(
 "/services/executive-search/",
 "Executive Search Firm in Pune | Animus Tech",
 "Confidential executive search in Pune for senior and specialist roles. AI mapped talent landscape, discreet human led approach, deep reference checks.",
 "Leadership &amp; Executive Search", "Service",
 "Confidential search for senior and specialist roles where the pool is small and mostly not looking.",
 ["Senior search is a different exercise from filling a vacancy. The people you want are employed, performing, "
  "not browsing job boards, and will only engage in a conversation that is discreet and worth their time.",
  "We map the landscape first: who is doing this job well, where, and what would move them. Approach is human "
  "led and confidential throughout. Reference checking goes deeper than the two names a candidate offers, "
  "because at this level the difference between a good hire and an expensive one is rarely visible in interview."],
 [("The pool is small and passive", "A handful of people in the country can do this job and none of them applied to anything this year."),
  ("The search must stay confidential", "The incumbent is still in seat, or the mandate itself is market sensitive."),
  ("A previous search failed", "The role has been open a long time, or a first hire did not work out and the second attempt cannot.")],
 [("Market map", ["Who is doing this well and where", "Realistic pool size", "Compensation reality", "Comparator companies"]),
  ("Approach", ["Discreet, human led outreach", "Confidential positioning", "Candidate motivation assessment", "No mass mailing"]),
  ("Assessment", ["Structured leadership interview", "Culture fit against your actual norms", "Deep reference checks", "Written view with reservations"]),
  ("Close", ["Offer structuring support", "Counter-offer management", "Notice period engagement", "Onboarding through month three"])],
 "Executive search"),

service_page(
 "/services/bulk-hiring/",
 "Bulk Hiring &amp; Volume Recruitment in Pune | Animus Tech",
 "Volume and project hiring in Pune. AI screening at scale, campus and walk-in drives, weekly pipeline reporting. For new plants, new shifts and rapid scale ups.",
 "Volume &amp; Project Hiring", "Service",
 "Structured drives when you need many people in one window, whether that is a new plant, a new shift, festive season or a funding led scale up.",
 ["Volume hiring fails on logistics more often than on sourcing. Getting three hundred applicants is not hard. "
  "Screening them consistently, scheduling them without losing half, and keeping the ones who accepted engaged "
  "until they actually join is where drives fall apart.",
  "AI screening removes the bottleneck at the top of the funnel, applying the same criteria to candidate one "
  "and candidate three hundred. We run campus and walk-in drives on the ground, and report pipeline weekly so "
  "you always know whether the number is going to land."],
 [("A new plant or new shift", "You need a defined headcount in place by a date that is not moving."),
  ("Seasonal or festive peaks", "Predictable annual surges where the hiring window is short and the volume is large."),
  ("A funding led scale up", "Headcount has been approved and the plan assumes people start in this quarter, not next.")],
 [("Planning", ["Headcount and role mapping", "Timeline working backwards from your date", "Sourcing channel mix", "Drive logistics"]),
  ("At scale", ["AI screening on consistent criteria", "Campus and walk-in drives", "Assessment batteries", "High volume scheduling"]),
  ("Reporting", ["Weekly pipeline numbers", "Funnel conversion at each stage", "Offer and acceptance tracking", "Early warning on shortfalls"]),
  ("Joining", ["Offer to joining engagement", "Drop-off risk flagging", "Backup pipeline maintained", "Joining day support"])],
 "Volume hiring"),

service_page(
 "/services/ai-candidate-assessment/",
 "AI Candidate Assessment Service | Animus Tech",
 "Send us your existing pipeline and we return a scored report on each candidate. Role specific skill assessments plus a structured culture fit interview.",
 "AI Assessment as a Service", "Service",
 "Already have a pipeline? Send us your candidates and we will run them through our AI assessment and culture fit process, then return a scored report on each.",
 ["Some companies do not need sourcing. They have applicants, an internal recruiter, and a referral network "
  "that works. What they do not have is a consistent way to compare thirty candidates without panel fatigue "
  "and first impression bias deciding it.",
  "This is that, unbundled. You send the pipeline, we run role specific skill assessments and a structured "
  "culture fit interview, scored on the same rubric for every candidate, and return a written report per "
  "person. No difference between the candidate interviewed on Monday and the one on Friday."],
 [("You have applicants but no bandwidth", "The pipeline is full and nobody has the hours to assess it properly."),
  ("Panel decisions keep splitting", "Different interviewers reach different conclusions and there is no shared standard to resolve it."),
  ("You need to defend the decision", "Comparable scores across the pool, documented, for internal review or for a regulated process.")],
 [("Skill assessment", ["Role specific, not generic", "Technical and functional", "Same rubric across the pool", "Scored and comparable"]),
  ("Culture fit", ["Structured interview", "Interviewed against your actual norms", "Behavioural history, not hypotheticals", "Reservations documented"]),
  ("Report", ["Written report per candidate", "Score with reasoning", "Flagged gaps and risks", "Recommended interview questions"]),
  ("Turnaround", ["Typically 3 to 5 working days", "Scales to large pipelines", "No sourcing engagement required", "Priced per candidate"])],
 "AI candidate assessment"),

service_page(
 "/services/hiring-advisory/",
 "Hiring Advisory &amp; Salary Benchmarking | Animus Tech",
 "Job description and scorecard design, interview loop design, and honest compensation benchmarks for the Pune market.",
 "Hiring Advisory", "Service",
 "Job descriptions that attract the right people, interview loops that actually discriminate, and honest salary benchmarks for your market.",
 ["Most hiring problems are design problems. A job description written to sound impressive attracts a hundred "
  "people who cannot do the job. An interview loop with five rounds of unstructured conversation tires "
  "candidates without distinguishing between them. A compensation band set from a two year old benchmark "
  "produces a search that was never going to close.",
  "This engagement fixes those before you spend money on sourcing. It is also the cheapest thing we do, and "
  "for teams hiring steadily it is often the highest return."],
 [("You are hiring repeatedly for a role", "Fixing the JD and the loop once pays off across every subsequent hire."),
  ("Offers keep getting declined", "Usually a compensation or a process problem, and it is worth knowing which before hiring again."),
  ("You are building an in-house function", "Setting the standard your internal recruiters will work to.")],
 [("JD &amp; scorecard", ["Written to filter, not to flatter", "Success criteria for year one", "Must-have vs nice-to-have split", "Scorecard interviewers can use"]),
  ("Interview design", ["Loop that discriminates", "Structured questions per competency", "Interviewer briefing", "Decision framework"]),
  ("Compensation", ["Pune market benchmarks", "Band recommendation by level", "Honest read on whether it will clear", "Equity and variable structuring"]),
  ("Process", ["Funnel diagnosis", "Drop-off analysis", "Candidate experience review", "Offer to joining protection"])],
 "Hiring advisory"),

]
