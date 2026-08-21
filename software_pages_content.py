# -*- coding: utf-8 -*-
"""
Content for the software arm's child pages.

Rendered by _build_software_pages.py. Reuses the shared section helpers from
pages_content so the markup stays identical to the rest of the site.

Naming rule, from the dual-business strategy: every page here must carry a
build word in its title and H1 (development, custom software, build, systems).
Never a bare "software company" phrase, which would compete with the
recruitment side's IT and software hiring page.
"""
from pages_content import sec, cards, rolegrid, prose, faq_html, links

PAGES = []

# ============================================ /software/custom-software-development-pune/
PAGES.append({
    "url": "/software/custom-software-development-pune/",
    "title": "Custom Software Development Company in Pune | Animus Tech",
    "desc": ("Custom software development in Pune for manufacturing and small businesses. "
             "Job tracking, invoicing and internal tools. You own the code and the data."),
    "crumbs": [("Home", "/"), ("Software", "/software/"),
               ("Custom software development in Pune", None)],
    "eyebrow": "Custom software development, Pune",
    "h1": "Custom software development company in Pune",
    "lead": ("We build the operational software small businesses actually run on. Job tracking, "
             "invoicing, lead management and internal tools, fitted to the process you already "
             "have. A complete working system, in real use fast, and you own the code and "
             "the data."),
    "service": "Custom software development",
    "cta_title": "Tell us what needs building",
    "cta_lead": ("Describe the problem rather than the solution. We will come back within one "
                 "working day with an honest view, including whether we are the right people "
                 "for it."),
    "faq": [
        ("How much does custom software cost in Pune?",
         "It depends almost entirely on scope, and the honest answer at first contact is a range "
         "rather than a number. What moves the figure is how many distinct workflows the tool has "
         "to carry, whether it needs to talk to systems you already run, and how many people use "
         "it. We start with one workflow built completely rather than several built partly, so "
         "the first cost is a fraction of an everything-at-once build and you have a working "
         "system before you commit to the next piece."),
        ("How long does the first system take?",
         "Weeks, not quarters. We take the process that is costing you most, build the whole of "
         "it start to end, and put it in front of real users on real data. A build that runs six "
         "months before anyone touches it is the most expensive mistake in this category, and it "
         "is the one we design against."),
        ("Do we own the software you build?",
         "Yes. You own the code and the data, and we commit to that in writing before any work "
         "starts. There is no lock-in and no dependency on us to keep it running. If you later "
         "want to take it in house or to another developer, you can."),
        ("Do you work with businesses outside Pune?",
         "Yes. We are based in Pune and know the industrial belt around it well, which is why a "
         "lot of our work sits there, but we build for small and mid-size businesses across "
         "India. Most of the work is remote either way, with on-site time where understanding "
         "the process needs it."),
        ("Why not just use off the shelf software?",
         "Often you should, and we will say so. Standard tools are cheaper and better supported "
         "where your process is standard. Custom is worth it when the way you work is genuinely "
         "specific and bending it to fit a template costs more than building the thing properly. "
         "We would rather tell you that at the first conversation than after an invoice."),
    ],
    "body": (
        sec("Why businesses call us",
            "The spreadsheet finally broke",
            "Almost every tool we have built started the same way.",
            prose([
                "Two people editing the same sheet at once. A lead that went cold because nobody "
                "owned the next step. An invoice raised with no link back to the job it belonged "
                "to. A new hire who cannot be shown how the system works, because there is no "
                "system, only a set of habits held in somebody's head.",
                "None of that is really a spreadsheet problem. It is a problem of nobody having "
                "written down how the work actually happens. It stays invisible until it costs "
                "you a client, or a week of reconciliation.",
                "Usually the process itself is sound. What is holding it together is a workaround: "
                "a sheet only one person truly understands, tabs that have to be updated in a "
                "particular order, a colour code that means something to whoever invented it. It "
                "works, in the sense that the business runs. But it is slow, it is hard to hand "
                "over, there is no history worth the name, and nobody can see the real position "
                "without asking someone. That is the point at which a proper system pays for "
                "itself, and it is exactly what we build: the whole process, start to end, "
                "not another patch on top of the last one.",
                "Pune has a very large number of businesses in exactly that position. Engineering "
                "firms, job shops, service and maintenance operations, agencies, distributors. "
                "Big enough that the informal system is straining, not big enough to want an "
                "enterprise ERP priced and scoped for someone else entirely.",
            ])),
        sec("What we build",
            "Software for how the work actually happens",
            "Fitted to your process, rather than a template you have to bend around.",
            rolegrid([
                ("Job and project tracking",
                 ["Jobs, stages and ownership", "What is moving and what is stuck",
                  "History against each job", "Nothing sitting without a next action"]),
                ("Invoicing and finance",
                 ["Invoices raised against jobs", "Financial history stays attached",
                  "Reconciliation stops being a week", "Exports for your accountant"]),
                ("Lead and enquiry management",
                 ["Capture from every channel", "Every touch recorded",
                  "Stage changes that mean something", "Follow-up that does not get forgotten"]),
                ("Internal operations tools",
                 ["The thing only you need", "Replacing the shared sheet",
                  "Dashboards people actually open", "Access control that fits your team"]),
            ]), alt=True),
        sec("Proof",
            "Two systems in daily use, not slideware",
            "We would rather show you working software than a wall of client logos.",
            cards([
                ("Lead generation tracker",
                 "In daily use at a digital marketing agency, running their pipeline end to end. "
                 "The useful part was never the database. It was deciding what counts as a stage "
                 "change, and making the tool refuse to let a record sit in limbo without a next "
                 "action against it."),
                ("Finance tracker",
                 "Built for a small enterprise that works job by job. It raises invoices and "
                 "holds the complete financial history against each job, so the money side and "
                 "the work side stay attached. Anyone who has run an operation like this knows "
                 "why that matters."),
                ("We are the users, not just the builders",
                 "We run our own operations on tools we built. That changes what gets made. You "
                 "stop adding features nobody opens and start fixing the three screens people "
                 "actually live in."),
            ])),
        sec("How we work",
            "One workflow, complete, then the next",
            "The most expensive software mistake is building everything at once, before anyone "
            "has used any of it.",
            prose([
                "<strong>Understand the process.</strong> We sit with the people who do the work "
                "and map how it actually happens, including the workarounds nobody documented. "
                "That is usually where the real requirement is hiding.",
                "<strong>Take one process, whole.</strong> We agree the workflow costing you most "
                "and build the whole of it, start to end, rather than a piece of several. We also "
                "write down what is deliberately not in scope yet, so nobody discovers the gap in "
                "month three.",
                "<strong>Put it in real use.</strong> On real data, with the people who will live "
                "in it. Real use surfaces problems no amount of specification review will.",
                "<strong>Extend from evidence.</strong> We add what people actually reach for and "
                "drop what they do not. Every extension is argued from use, not from the original "
                "wish list.",
            ]), alt=True),
        sec("What we commit to",
            "Written down before anything is built",
            "",
            cards([
                ("You own the code and the data",
                 "No lock-in, and no dependency on us to keep it running."),
                ("We say when something is a bad idea",
                 "And why, rather than quietly building it and invoicing for it."),
                ("You hear about a slip when we know",
                 "Not when the deadline arrives."),
            ])),
        links("See also:", [
            ("Software for manufacturing", "/software/manufacturing-software/"),
            ("What we have built", "/software/#what-we-built"),
            ("Hiring rather than building?", "/talent-acquisition/"),
        ]),
    ),
})


# ======================================================= /software/manufacturing-software/
MFG_FAQ = [
    ("Is this an ERP?",
     "No, and for most small manufacturers that is the point. Full ERP is scoped and priced for a "
     "much larger business, takes months to implement, and brings modules you will never open. We "
     "build the two or three things that are actually costing you time, in a tool your team will "
     "use, and leave the rest alone."),
    ("What does manufacturing software usually replace?",
     "Usually a set of spreadsheets and a WhatsApp group. Job status in one sheet, dispatch in "
     "another, invoicing in the accountant's software, and the real state of things held in one "
     "person's head. The cost is rarely a dramatic failure. It is small, constant reconciliation "
     "and the jobs that quietly slip."),
    ("Can it work alongside Tally or our accounting software?",
     "Generally yes. We do not try to replace your accounting system. The useful thing is keeping "
     "job history and the money attached to each other, and exporting cleanly into whatever your "
     "accountant already uses."),
    ("Will people on the shop floor actually use it?",
     "That is the real test, and it is why we put a small version into real use early rather than "
     "specifying everything upfront. Tools fail on the floor when they add data entry without "
     "giving anything back. If a screen does not save someone time, it should not exist."),
    ("Do you build for a single plant or multiple sites?",
     "Both, though we would usually start with one site and one workflow, prove it, then extend. "
     "Building multi-site complexity before the single-site version has earned its place is how "
     "these projects get expensive."),
]

PAGES.append({
    "url": "/software/manufacturing-software/",
    "title": "Manufacturing Software for Small Businesses | Animus Tech",
    "desc": ("Custom manufacturing software for small and mid-size businesses in India. Job "
             "tracking, production visibility and invoicing tied to each job, without ERP scope."),
    "crumbs": [("Home", "/"), ("Software", "/software/"),
               ("Manufacturing software", None)],
    "eyebrow": "Manufacturing and operations",
    "h1": "Custom manufacturing software, without the ERP",
    "lead": ("Job tracking, production visibility and invoicing that stays attached to the work it "
             "came from. Built for small and mid-size manufacturers who have outgrown spreadsheets "
             "but do not need an enterprise system, and would not use one if they had it."),
    "service": "Manufacturing software development",
    "cta_title": "Tell us what needs building",
    "cta_lead": ("Describe what is costing you time. We will come back within one working day with "
                 "an honest view, including whether custom software is the right answer at all."),
    "faq": MFG_FAQ,
    "body": (
        sec("The problem",
            "Between a spreadsheet and an ERP, there is nothing",
            "Which is where most small manufacturers actually sit.",
            prose([
                "The spreadsheet stops working somewhere around the point where more than two "
                "people need to touch it, or where the history of a job matters as much as its "
                "current state. That is a real threshold and most owners can name the week they "
                "crossed it.",
                "What is on offer above that line does not fit either. Full ERP assumes a scale of "
                "operation, a budget and an implementation appetite that a fifty person plant does "
                "not have. Buy it anyway and you get a long rollout, a lot of unused modules, and "
                "a team that keeps using the spreadsheet because it is faster.",
                "So the gap stays open. Jobs tracked in one place, dispatch in another, invoicing "
                "in the accountant's software, and the actual state of the plant living in one "
                "person's memory. Nothing collapses. It just costs a few hours every week and the "
                "occasional job that slips through.",
            ])),
        sec("What we build",
            "The two or three things costing you time",
            "Not a system of record for everything. The parts that are actually leaking.",
            rolegrid([
                ("Job and work order tracking",
                 ["Every job with a stage and an owner", "What is stuck and for how long",
                  "Complete history against each job", "Visible without asking anyone"]),
                ("Production and dispatch",
                 ["Status that reflects the floor", "Materials and readiness",
                  "Dispatch and delivery record", "Simple enough to keep updated"]),
                ("Invoicing tied to the job",
                 ["Invoice raised from the work", "Financial history stays attached",
                  "Payment status visible", "Clean export to accounts"]),
                ("Reporting that gets opened",
                 ["A handful of numbers that matter", "Job level profitability",
                  "Where time is actually going", "No dashboard nobody reads"]),
            ]), alt=True),
        sec("Proof",
            "A finance tracker already doing this",
            "Working software, in daily use, carrying real data.",
            prose([
                "We built a finance tracker for a small enterprise that works job by job. It "
                "raises invoices and holds the complete financial history against each job, so "
                "the money side of a job and the job itself stay attached to each other.",
                "Anyone who has run an operation like this knows why that matters. The moment "
                "invoicing lives in one place and job history lives in another, reconciliation "
                "becomes somebody's whole week, every month, forever.",
                "We also run our own operations on tools we built, which is a different discipline "
                "from handing something over and moving to the next client. You learn quickly "
                "which screens people live in and which ones were built to look thorough.",
            ])),
        sec("Why us",
            "We know your floor from the other side",
            "",
            cards([
                ("We recruit for plants across India",
                 "Production, quality, maintenance, supply chain. We have spent a lot of time "
                 "inside manufacturing operations understanding how they actually run, which is "
                 "the same understanding a useful tool depends on."),
                ("One workflow, complete",
                 "The whole of one process, working start to end, in weeks. Then extended from "
                 "what people actually reach for. Not a six month build that ships the wrong "
                 "thing."),
                ("You own the code and the data",
                 "Committed in writing before anything is built. No lock-in."),
            ]), alt=True),
        sec("Common questions",
            "Questions we get asked",
            "",
            faq_html(MFG_FAQ)),
        links("See also:", [
            ("Custom software development in Pune", "/software/custom-software-development-pune/"),
            ("What we have built", "/software/#what-we-built"),
            ("Manufacturing recruitment", "/industries/manufacturing-recruitment-pune/"),
        ]),
    ),
})


# ================================================================ /software/ai-solutions/
AI_FAQ = [
    ("Is this real AI or a wrapper around ChatGPT?",
     "Both descriptions miss the point. Most useful business AI does involve a language model, "
     "ours included. What decides whether it works is everything around the model: what you feed "
     "it, how you constrain it, what happens when it is unsure, and whether a person checks the "
     "output before it matters. That is the engineering, and it is what we have spent our own "
     "time on."),
    ("What if the AI gets something wrong?",
     "It will, and any firm telling you otherwise has not run one in production. The question is "
     "what happens next. In our own system nothing is rejected by software alone, every score "
     "carries written reasoning a person can argue with, and disagreements between the AI and "
     "the human are surfaced rather than hidden. We build client systems the same way. AI that "
     "cannot show its working is not usable for decisions that matter."),
    ("Do we need a lot of data to start?",
     "Usually less than people assume. Reading documents, extracting fields, classifying and "
     "routing work do not require you to have a large historical dataset. Where you would need "
     "real volume is training something bespoke on your own patterns, and for most small and "
     "mid-size businesses that is not the useful starting point."),
    ("Where does AI genuinely not help?",
     "Where the rules are already clear and consistent. If a decision can be written as a rule, "
     "write it as a rule. It will be cheaper, faster, and it will never surprise you. AI earns "
     "its place on messy inputs and judgement heavy work, not on arithmetic."),
    ("Can it run on our own systems?",
     "Depends what the work is and how sensitive the data is. Some of it can run against your "
     "own infrastructure, some depends on external model providers. We will tell you plainly "
     "which parts sit where before you commit, because for some businesses that answer is the "
     "deciding factor."),
]

PAGES.append({
    "url": "/software/ai-solutions/",
    "title": "Custom AI Development for Business | Animus Tech",
    "desc": ("Custom AI for document screening, workflow automation and internal assistants. "
             "Built by a team running its own AI system in production every working day."),
    "crumbs": [("Home", "/"), ("Software", "/software/"), ("AI solutions", None)],
    "eyebrow": "Custom AI development",
    "h1": "Custom AI that does a real job",
    "lead": ("Most AI pitches are demos. Ours is a system we run our own business on: sourcing, "
             "screening and assessing candidates every working day, at a volume no manual team "
             "could match. We build the same kind of thing for other businesses."),
    "service": "Custom AI development",
    "cta_title": "Tell us what needs deciding, sorted or read",
    "cta_lead": ("Describe the work that is eating people's time. We will come back within one "
                 "working day with an honest view, including whether AI is the right tool for "
                 "it at all."),
    "faq": AI_FAQ,
    "body": (
        sec("Proof first",
            "We run AI in production, on our own P&L",
            "Not a pilot, not a demo built for a pitch.",
            prose([
                "Our recruitment arm runs on AI we built. It reads every profile that comes in "
                "rather than the first fifty, scores each one against the criteria agreed at "
                "intake, and writes out its reasoning including the gaps worth asking about. It "
                "searches on meaning rather than keywords, so it surfaces people whose "
                "experience fits even when their CV never uses the client's terminology.",
                "Around that sit the smaller pieces that make it usable day to day: job "
                "descriptions drafted from a scorecard, structured interview support, candidate "
                "fitment evaluation against how a specific team actually operates, search across "
                "LinkedIn and Naukri, and a Chrome extension that screens a CV in the browser "
                "where a recruiter is already working.",
                "None of that is a case study we commissioned. It is the operational software of "
                "a business with revenue attached, which means we have had to live with every "
                "decision in it. That is a materially different experience from shipping an AI "
                "project and moving on.",
            ])),
        sec("What we build",
            "Four things AI is genuinely good at",
            "We would rather be specific about where it works than sell you a category.",
            rolegrid([
                ("Reading documents",
                 ["CVs, invoices, forms, reports", "Extracting fields reliably",
                  "Scoring against your criteria", "Written reasoning, not just a number"]),
                ("Automating workflow steps",
                 ["Classifying and routing work", "Drafting from a template and context",
                  "Flagging exceptions for a human", "Removing the copy and paste"]),
                ("Internal assistants",
                 ["Questions answered from your own documents", "Grounded in your data, not the web",
                  "Access controlled by role", "Answers that cite where they came from"]),
                ("Browser and workflow extensions",
                 ["Working where your team already works", "No new system to log into",
                  "Screening and summarising in place", "Adopted because it saves time"]),
            ]), alt=True),
        sec("How we think about it",
            "The model is the easy part",
            "",
            prose([
                "Getting a language model to produce something plausible takes an afternoon. "
                "Getting a system you can run a business on takes considerably longer, and almost "
                "none of the difficulty is in the model itself.",
                "It is in deciding what the thing is actually allowed to conclude. What happens "
                "when it is unsure. Whether a person sees the output before it matters, and "
                "whether that person is given enough reasoning to disagree usefully. Whether the "
                "output is consistent enough that two similar inputs on different days get "
                "treated the same way.",
                "We learned that by running one. Our own system ranks and narrows, a recruiter "
                "reviews, and nobody is rejected by software alone. Where the AI and the human "
                "disagree, we surface it, because that disagreement is usually the most "
                "informative signal in the whole process. We build client systems on the same "
                "principle.",
            ])),
        sec("When to say no",
            "We will tell you when AI is the wrong answer",
            "",
            cards([
                ("If a rule would do the job",
                 "Write the rule. It is cheaper, faster, and it will never surprise you at the "
                 "worst possible moment."),
                ("If the process is not agreed",
                 "AI applied to a process nobody has settled just automates the disagreement. "
                 "Fix the process first."),
                ("If nobody will check the output",
                 "Automation nobody reviews is a risk with a schedule attached. If there is no "
                 "capacity to check it, we would rather not build it."),
            ]), alt=True),
        links("See also:", [
            ("Custom software development in Pune", "/software/custom-software-development-pune/"),
            ("Internal tools", "/software/internal-tools/"),
            ("What we have built", "/software/#what-we-built"),
        ]),
    ),
})


# ============================================================== /software/internal-tools/
TOOLS_FAQ = [
    ("How is this different from Zoho, HubSpot or a template CRM?",
     "Those are excellent when your process matches what they assume. The trouble starts when it "
     "does not, and you end up using a field called something else to mean the thing you "
     "actually track, with a note in the description explaining the workaround. If you recognise "
     "that, a tool built around your process is worth pricing. If you do not, keep the template. "
     "We will say so."),
    ("Can it replace our spreadsheets entirely?",
     "For the process we build, yes, and that is the point. What we would not do is try to "
     "replace every spreadsheet in the business at once. Some of them are genuinely fine, and a "
     "spreadsheet used by one person for analysis is not the problem. The ones worth replacing "
     "are the ones several people depend on and nobody fully trusts."),
    ("What happens when we need a change later?",
     "You ask, and we build it, or you take the code to someone else and they do. You own it "
     "either way. Most changes after launch are small and come from real use rather than from "
     "anyone's original plan, which is why we do not try to specify everything upfront."),
    ("Who hosts it and what does that cost?",
     "Usually a small monthly hosting cost, which for a tool used by a handful of people is "
     "modest. We will set out exactly what it will be before you commit, and it is yours to "
     "move elsewhere whenever you like."),
    ("Will our team actually use it?",
     "Only if it saves them time on day one. Tools fail when they add data entry and give "
     "nothing back, so we build for the two or three screens people genuinely live in and "
     "resist adding the rest. If a screen does not earn its place, it should not exist."),
]

PAGES.append({
    "url": "/software/internal-tools/",
    "title": "Internal Tools & Custom CRM Development | Animus Tech",
    "desc": ("Custom internal tools for operations led businesses in India. Lead management, "
             "invoicing, job tracking and reporting, built around how your team already works."),
    "crumbs": [("Home", "/"), ("Software", "/software/"), ("Internal tools", None)],
    "eyebrow": "Internal operations tools",
    "h1": "Internal tools built around your process",
    "lead": ("Lead management, invoicing, job tracking and the reporting that sits on top. The "
             "unglamorous software a business actually runs on, built to fit how your team "
             "already works rather than a template they have to bend around."),
    "service": "Internal tools development",
    "cta_title": "Tell us what needs building",
    "cta_lead": ("Describe the sheet or the process that is causing trouble. We will come back "
                 "within one working day with an honest view."),
    "faq": TOOLS_FAQ,
    "body": (
        sec("What these are",
            "The software nobody demos, and everybody depends on",
            "Internal tools are not the interesting part of a business. They are the part that "
            "quietly decides how much time it takes to run.",
            prose([
                "Nobody buys a company because its lead tracker is good. But an operations team "
                "that cannot see which jobs are stuck, or a finance function reconciling "
                "invoices against job history by hand every month, is losing hours that never "
                "appear on any report. It just feels like being busy.",
                "The tools we build are deliberately narrow. A lead system that will not let a "
                "record sit without a next action. An invoicing tool that keeps the money "
                "attached to the work it came from. A job tracker that shows what is stuck and "
                "for how long without anyone having to ask. Reporting that is a handful of "
                "numbers people actually open, rather than a dashboard built to look thorough.",
            ])),
        sec("Proof",
            "Two systems, in daily use, carrying real data",
            "These are ours and our clients', running now.",
            cards([
                ("Lead generation tracker",
                 "In daily use at a digital marketing agency, running their pipeline end to end. "
                 "The useful part was never the database. It was deciding what counts as a stage "
                 "change, and making the tool refuse to let a record sit in limbo without a next "
                 "action against it."),
                ("Finance tracker",
                 "Built for a small enterprise that works job by job. It raises invoices and "
                 "holds the complete financial history against each job, so the money side and "
                 "the work side stay attached to each other."),
                ("Our own operations",
                 "We run our recruitment business on tools we built. That is a different "
                 "discipline from handing something over and moving on. You find out fast which "
                 "screens people live in and which ones were built to look complete."),
            ]), alt=True),
        sec("What we build",
            "Where internal tools usually earn their cost",
            "",
            rolegrid([
                ("Lead and enquiry management",
                 ["Capture from every channel", "Every touch recorded against a record",
                  "Stage changes that mean something", "Nothing sitting without a next action"]),
                ("Invoicing and finance",
                 ["Invoices raised from the work", "Financial history attached to each job",
                  "Payment status visible", "Clean export to your accountant"]),
                ("Job and project tracking",
                 ["Stage and owner on every job", "What is stuck, and for how long",
                  "Full history, not just current state", "Visible without asking anyone"]),
                ("Reporting and dashboards",
                 ["A few numbers that matter", "Job or client level profitability",
                  "Where time is actually going", "No report nobody opens"]),
            ])),
        sec("The honest version",
            "Sometimes you should buy, not build",
            "",
            prose([
                "If your process is standard, a template product is cheaper, better supported "
                "and available today. We will tell you that rather than quote you for a build "
                "you did not need.",
                "Custom earns its cost when the way you work is genuinely specific, when the "
                "workarounds required to fit a template are themselves becoming the problem, or "
                "when the thing you need to track simply does not exist as a field in anything "
                "off the shelf. That is a real situation for a lot of operations led businesses, "
                "and it is the one we build for.",
            ]), alt=True),
        links("See also:", [
            ("Manufacturing software", "/software/manufacturing-software/"),
            ("Custom AI development", "/software/ai-solutions/"),
            ("Custom software development in Pune", "/software/custom-software-development-pune/"),
        ]),
    ),
})
