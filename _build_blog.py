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
AUTHOR = "Animus Tech"

# ------------------------------------------------------------------ posts ---
POSTS = [
{
 "slug": "recruitment-agency-fees-india",
 "date": "2026-07-28",
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
 "slug": "why-choose-animus-tech",
 "date": "2026-08-05",
 "tag": "Why us",
 "title": "Why Choose Animus Tech | Recruitment Agency India",
 "h1": "Why choose us, answered with numbers instead of adjectives",
 "desc": "Every agency claims quality and speed. Here are our actual submittal ratios, timelines and the searches that ran long, so you can judge for yourself.",
 "lead": ("Every recruitment agency promises quality and speed. Almost none will show you "
          "what those words mean in their own numbers. Here are ours, including the search "
          "that took nearly twice as long as it should have."),
 "body": """
<p>Choosing a recruitment partner is an unusual purchase, because the thing you are buying is
judgement, and judgement is invisible until after you have paid for it. Pitches all sound the
same for exactly that reason.</p>
<p>So rather than describe ourselves, here is the evidence.</p>

<h2>You see a shortlist, not a stack</h2>
<p>On a sales role for a manufacturing client we screened more than forty profiles. The client
saw eight, sent in two deliberate batches of four. They hired from the second batch.</p>
<p>The number that matters there is not the eight. It is the thirty two you never had to open.
Screening is the work, and if we pass that work back to you by forwarding everything that
loosely matches, you are doing our job while paying us to do it.</p>
<p>On a marketing role for a SaaS startup the shape was the same: twenty to thirty screened,
six shared after the first batch of four was rejected, one hired. On a D2C brand search,
thirty plus screened, five shared, one hired.</p>

<h2>Speed, where the role allows it</h2>
<p>That same sales search closed in ten days across three interview rounds, the last one at
board level. The candidate joined fifteen days later, which was their notice period. Twenty
five days from intake to someone sitting at the desk.</p>
<p>The marketing search ran twelve days to offer, then fifteen days of notice. Roughly
twenty seven days intake to joining.</p>
<p>We quote those with the notice period broken out on purpose. An agency that tells you
twenty five days without saying that fifteen of them were the candidate's notice is
managing your impression rather than your search.</p>

<h2>The search we did not do well, and why we publish it</h2>
<p>A factory manager search took over a hundred profiles screened and twenty to twenty five
shared. Around forty five days to joining. Three times the submittals of the sales role and
nearly twice the timeline.</p>
<p>Same recruiter, same method. What changed was that the mandate moved mid search, so every
profile screened against the original definition stopped counting.</p>
<p>We publish that one because it is the honest counterweight to the numbers above, and
because it is the single most useful thing we know about hiring cost. If you want a search to
be fast and cheap, the highest leverage hour you will spend is the one before sourcing starts,
getting the brief right. More on that in
<a href="/blog/why-your-search-went-long/">why your search went long</a>.</p>

<h2>Software narrows. A person decides.</h2>
<p>Our AI sources, screens and assesses at a scale and speed no manual team matches. On a
developer search it ran eighty plus profiles down through an AI interview stage to ten
candidates, one of whom was hired.</p>
<p>But nobody is rejected by software alone. A recruiter reviews every shortlist before it
reaches you, because the questions that actually predict success are not keyword questions.
On that developer search the useful ones were simple: is the project live, did you personally
own this part, and what problem were you solving. Those separate the people who built
something from the people who were nearby when it was built.</p>

<h2>We tell you the uncomfortable thing early</h2>
<p>If we think the compensation band will not clear the market, you hear it in week one rather
than week six. If we think the role as written will not attract the person you actually want,
we say so before sourcing rather than after four rejected batches.</p>
<p>That is a harder first conversation and a much cheaper overall one. It is also the main
reason our submittal counts stay low: we spend the disagreement upfront instead of spreading
it across weeks of wasted screening.</p>

<h2>What you can hold us to</h2>
<ul>
<li>A shortlist with written reasoning against a scorecard agreed at intake, not a forwarded pile.</li>
<li>An update every Friday, including the weeks when the update is that nothing moved.</li>
<li>An honest read on compensation, early, even when it is not what you want to hear.</li>
<li>Reservations included with candidates we recommend, not just the flattering parts.</li>
<li>No upfront fees, with terms confirmed in writing before any sourcing begins.</li>
</ul>

<h2>Fair questions to ask us, or anyone else</h2>
<p>If you are comparing agencies, these four surface more than any pitch will:</p>
<ul>
<li>How many other clients are you running this same brief for right now?</li>
<li>How many profiles will I see, and how many will you have screened to get there?</li>
<li>What is your submittal to hire ratio, and can you show me a search that went badly?</li>
<li>What happens if you decide the compensation band will not clear the market?</li>
</ul>
<p>The last two are the revealing ones. An agency that cannot tell you its ratio has never
measured it, and an agency with no failed search to describe is either very new or not being
straight with you.</p>
<p>Our full answers, including what we need from you for any of this to hold, are on
<a href="/how-we-work/">how we work</a>. What we charge and why is in
<a href="/blog/recruitment-agency-fees-india/">what recruitment agencies actually charge in India</a>.</p>
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
<tr><td>Shared with client</td><td>8</td><td>20 to 25</td></tr>
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
{
 "slug": "what-drives-the-cost-of-custom-software",
 "date": "2026-08-21",
 "tag": "Software costs",
 "arm": "software",
 "title": "What Drives the Cost of Custom Software | Animus Tech",
 "h1": "What actually drives the cost of custom software",
 "desc": "Nobody quotes a number at the first conversation, and anyone who does is guessing. Here is what genuinely moves the price of a build, and how to keep it down.",
 "lead": ("The first question every business owner asks is what it will cost. The honest answer "
          "at that point is a range, because the number is decided by things nobody has "
          "established yet. This is what those things are, so you can work out roughly where "
          "your project sits before anyone quotes you."),
 "body": """
<p>If a development firm gives you a firm price in the first meeting, they are doing one of two
things. Either they have a template they intend to bend your business around, or they have
padded the number enough to survive whatever they discover later. Neither is good for you.</p>

<p>What follows is what actually moves the cost. None of it is mysterious, and you can estimate
most of it yourself before you speak to anybody.</p>

<h2>1. How many workflows the system has to carry</h2>

<p>This is the single biggest driver, and it is the one most people underestimate. A tool that
tracks jobs through five stages is a different size of problem to one that tracks jobs, raises
invoices against them, manages materials, and reports on profitability per job.</p>

<p>Each additional workflow is not just more screens. It is more states things can be in, more
rules about what is allowed when, and more ways the data can end up inconsistent. Cost tends to
rise faster than the count of features suggests.</p>

<p>The practical implication: a system covering one process end to end costs considerably less
than one covering three processes partly, and it is usually more useful on day one.</p>

<h2>2. Whether it has to talk to something you already run</h2>

<p>A standalone tool is straightforward. A tool that has to exchange data with your accounting
software, or read from a machine on the floor, or push into a portal a customer insists on, is
a different matter.</p>

<p>Integrations are where estimates go wrong, because the difficulty depends entirely on what
the other system allows. Some expose clean, documented interfaces. Others expect a human with a
login and offer nothing else. You cannot tell which you are dealing with until someone checks,
which is why an honest quote depends on that check happening first.</p>

<p>If cost matters more than convenience, a clean export that your accountant imports is
usually a fraction of the price of a live two way integration, and for many businesses it is
genuinely enough.</p>

<h2>3. How many people use it, and how different they are</h2>

<p>Ten people doing the same job need one interface. Ten people across four roles, where the
supervisor sees things the operator must not, need permissions, and permissions need thinking
about. Roles multiply the design work more than headcount does.</p>

<p>Where people use it matters too. A tool used at a desk is simpler than one used on a shop
floor on a shared tablet with wet hands, which has real consequences for how much can be on a
screen and how much typing you can reasonably ask for.</p>

<h2>4. How clear the process already is</h2>

<p>This is the driver nobody expects, and it is the one you have most control over.</p>

<p>If the way work moves through your business is well understood and consistent, building
software for it is mostly execution. If different people do the same job differently, or the
rules live in one person's memory and turn out to have exceptions nobody mentioned, then part
of the project becomes deciding what the process actually is.</p>

<p>That decision has to be made by somebody. It is cheaper and better when you make it, not when
a developer guesses. Before you get quotes, it is worth writing down how the work moves,
including the exceptions. You will find disagreements, and finding them then is much cheaper
than finding them in testing.</p>

<h2>5. Data you already have</h2>

<p>Years of history in a spreadsheet has to go somewhere. If it is clean and consistent, moving
it is routine. If the same customer appears four ways, dates are typed in three formats, and
some rows have notes in the amount column, then cleaning it is a project of its own.</p>

<p>You can reduce this cost yourself, and you are better placed to do it than anyone else,
because you know which of the four spellings is the real customer.</p>

<h2>What does not drive cost as much as people think</h2>

<p>Visual design, for most operational tools. These are systems people use every day at work,
where clarity and speed matter far more than distinctiveness. A plain interface that is obvious
beats a striking one that needs explaining.</p>

<p>The technology choice, within reason. Arguments about frameworks matter much less to your
outcome than whether the person building it understood your process.</p>

<h2>How to get a realistic number</h2>

<p>Come to the conversation with the process written down, the exceptions listed, a clear view
of who will use it and where, and honesty about what state your existing data is in. Ask for the
cost of one workflow built completely rather than everything at once. You will get a tighter
number, a shorter timeline, and something in real use sooner.</p>

<p>And ask what is deliberately excluded from the quote. That answer tells you more about
whether a firm has understood your problem than the price does.</p>
""",
 "related": [("Custom software development in Pune", "/software/custom-software-development-pune/"),
             ("Manufacturing software", "/software/manufacturing-software/")],
},

{
 "slug": "how-ai-screening-actually-works",
 "date": "2026-08-25",
 "tag": "AI & screening",
 "title": "How AI Screening Actually Works | Animus Tech",
 "h1": "How AI screening actually works, and what it still can't judge",
 "desc": "What our AI interview stage actually filters, with real funnel numbers, and the three questions no algorithm can ask instead of a person.",
 "lead": ("Every agency now says AI-powered somewhere on its homepage. Almost none say what the "
          "AI actually does, where it stops, or what still needs a person. Here is ours, with "
          "the real numbers from one search."),
 "body": """
<h2>Where AI actually sits in the process</h2>
<p>On a backend developer search this year, the funnel ran like this: 80 plus resumes screened,
20 taken through an AI interview stage, 10 shared with the client, 1 hired. Ten submittals for
one hire, and a stage in the middle that most agencies do not have at all.</p>
<p>Most recruitment still runs CV screen straight to submittal. That is exactly why clients end
up with candidates who read well on paper and interview badly. Adding a stage in between, an AI
interview before a human ever reviews the shortlist, is what let half of the 20 who cleared the
resume screen get filtered out before anyone's time was spent on them.</p>

<h2>The developer search: what the AI interview stage filtered</h2>
<p>That halving is the actual story. The AI interview did not replace judgement. It asked every
one of those 20 people the same questions, in the same order, scored against the same rubric,
with no fatigue and no drift over a long day of screening. What survived went to a recruiter,
not straight to the client.</p>
<p>Ten of the twenty did not clear that stage. The point of publishing that number is not to
show the AI being clever. It is to show that the filtering happened before a human's time got
spent on it, and that a person still reviewed everyone who came through the other side.</p>

<h2>What AI can judge, and what it cannot</h2>
<p>An AI interview is good at consistency. Every candidate gets the same questions in the same
order, scored against the same rubric, with no favouritism toward whoever interviewed last and
no drop in attention on the fifteenth call of the day. That is a genuine advantage over a human
doing back to back screens.</p>
<p>What it cannot do reliably is tell a fluent talker from someone who actually did the work.
That distinction matters most in technical hiring, where the vocabulary sounds identical whether
or not the person shipped anything.</p>

<h2>The three-question method for the part AI cannot reach</h2>
<p>Lokesh, who runs the search side of Animus Tech, is not from an engineering background and
closes backend and frontend roles anyway. He took recruitment-tech courses to learn which
skills actually matter per role, then built a verification method that does not require writing
code himself. It checks three things, in order.</p>
<ul>
<li><strong>Live project, or not.</strong> Was this shipped and used, or a college assignment, or
a team product where this candidate's own piece is unclear? Someone who cannot draw that
distinction himself is a flag on its own.</li>
<li><strong>What was actually owned.</strong> Not what the team delivered around them. What this
person was personally accountable for.</li>
<li><strong>The problem statement.</strong> What problem was the project solving? Someone who
owned the work states it in a sentence. Someone who was adjacent to it describes the technology
instead.</li>
</ul>
<p>That last question is the cheapest, highest-signal filter available, and it is very hard to
fake convincingly across a real conversation. It is also something any hiring manager can ask
themselves in thirty seconds, AI tooling or not.</p>

<h2>The keyword problem AI alone does not solve</h2>
<p>On an unrelated search, a candidate surfaced whose CV was, in Lokesh's words, not a resume
but a page consisting of education, company name and internship name. No responsibilities
listed, no achievements, nothing for a keyword match to grab onto. A pure keyword system, human
or automated, would have skipped that CV entirely, regardless of who the person actually was.</p>
<p>An AI interview stage does not fix this by itself. It only gets a chance to evaluate someone
once that person has already been pulled into the funnel. Sourcing that goes wider than keyword
matching, and a recruiter willing to look past a thin CV, still has to happen upstream of any AI
stage. Tooling narrows a pool that already exists. It does not go looking for the pool.</p>

<h2>What we actually commit to</h2>
<p>Our AI sources, screens and interviews at a scale no manual team matches. But nobody is
rejected by software alone. A recruiter reviews every shortlist before it reaches you, because
the questions that predict success on the job, like the problem-statement question above, are
not the kind an algorithm asks well on its own.</p>
<p>That is the honest version of AI-powered: tooling narrows the field fast and consistently,
and a person makes the calls that require judgement. If an agency tells you AI does the whole
job, ask to see the funnel. If they cannot show you one, they probably do not have a real stage,
just a label.</p>
<p>More on how we structure a search end to end is on <a href="/how-we-work/">how we work</a>,
and what we look for role by role is on our
<a href="/talent-acquisition/">talent acquisition</a> page. For software roles specifically, see
<a href="/industries/it-software-recruitment-pune/">IT and software recruitment in Pune</a>.</p>
""",
 "related": [("How we work, and what we commit to", "/how-we-work/"),
             ("IT and software recruitment in Pune", "/industries/it-software-recruitment-pune/")],
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
       "author": {"@type":"Organization","name":AUTHOR},
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
      <p style="margin-top:26px"><a href="/talent-acquisition/#contact" class="btn btn--primary">Talk to us
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
                    "author":{"@type":"Organization","name":AUTHOR}} for p in POSTS]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Blog"}]},
    ]
    def cards_for(arm):
        return "".join(f"""
      <a class="postcard reveal" href="/blog/{p['slug']}/">
        <p class="postmeta"><span class="tagchip">{p['tag']}</span><span>{p['date']}</span></p>
        <h3>{p['h1']}</h3>
        <p>{p['desc']}</p>
      </a>""" for p in POSTS if p.get("arm", "hiring") == arm)

    def group(arm, title, blurb):
        inner = cards_for(arm)
        if not inner:
            return ""
        return f"""
    <div class="reveal" style="margin-bottom:22px">
      <h2 class="section-title" style="font-size:clamp(1.3rem,2.2vw,1.7rem)">{title}</h2>
      <p class="section-lead">{blurb}</p>
    </div>
    <div class="postlist" style="margin-bottom:54px">{inner}</div>"""

    cards = (group("hiring", "On hiring",
                   "Recruitment, assessment and what searches actually cost in time and money.")
             + group("software", "On building software",
                     "Custom systems for operations led businesses, and what makes them "
                     "succeed or quietly fail."))
    body = f"""
<section class="hero hero--sub">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="glow glow--a" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a><span class="crumbs__sep">/</span><span aria-current="page">Blog</span>
    </nav>
    <span class="eyebrow">Writing</span>
    <h1>Notes on hiring and building</h1>
    <p class="hero__lead">
      What we have learned running searches, and building the systems businesses run on.
      Real numbers from our own work, including the searches that went long and the builds
      that taught us something. Written for the person doing the work, not for other agencies.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
{cards}
  </div>
</section>
"""
    out = os.path.join(ROOT, "blog")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(
        head("Notes on Hiring and Building Software | Animus Tech",
             "Real numbers from our own searches and builds. Agency fees, choosing a hiring partner, where recruitment time goes, and what drives the cost of custom software.",
             url, schema) + body + TAIL)
    return url

if __name__ == "__main__":
    for p in POSTS:
        print("wrote", build_post(p))
    print("wrote", build_index())
    print(f"\n{len(POSTS)} posts + index built.")
