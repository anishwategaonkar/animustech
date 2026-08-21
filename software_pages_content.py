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
             "have. Small first version, in real use fast, and you own the code and the data."),
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
         "it. We scope a small first version deliberately, so the first cost is a fraction of a "
         "full build and you find out whether the thing works before committing further."),
        ("How long does a first version take?",
         "Weeks, not quarters. We agree the smallest version that is genuinely useful, put it in "
         "front of real users on real data, and extend from there. A build that runs six months "
         "before anyone touches it is the most expensive mistake in this category, and it is the "
         "one we design against."),
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
            "Small first, then real",
            "The most expensive software mistake is building the whole thing before anyone has "
            "used any of it.",
            prose([
                "<strong>Understand the process.</strong> We sit with the people who do the work "
                "and map how it actually happens, including the workarounds nobody documented. "
                "That is usually where the real requirement is hiding.",
                "<strong>Scope the first version small.</strong> We agree the smallest thing that "
                "would genuinely be useful, and write down what is deliberately left out, so "
                "nobody discovers the gap in month three.",
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
                ("Small first, then real",
                 "A working first version in weeks, extended from what people reach for. Not a "
                 "six month build that ships the wrong thing."),
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
