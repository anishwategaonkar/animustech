# -*- coding: utf-8 -*-
"""
Live job listings. Edit this file, then run:  python3 _build_jobs.py

=============================================================================
RULES. These are not style preferences, they protect you.
=============================================================================

1. ONLY POST ROLES YOU ARE GENUINELY RECRUITING FOR.
   Google removes sites from Google for Jobs for posting roles that are not
   real or not open. It is also unfair to candidates who apply.

2. EVERY JOB NEEDS AN INTERNAL `valid_through` DATE.
   It is not shown publicly. Once that date passes, the listing stops showing.
   Delete closed roles from this file and rebuild.

3. NEVER NAME THE CLIENT unless they have agreed in writing.
   Use "a tier-1 auto supplier in Chakan", "a Series A SaaS company", and so on.

4. SALARY IS OPTIONAL BUT WORTH INCLUDING.
   Listings with a salary band get materially more applications. If the client
   will not allow it, set salary_min/salary_max to None.

=============================================================================
FIELD REFERENCE
=============================================================================
slug            url-safe-id, becomes /jobs/<slug>/
title           the job title as a candidate would search it
location        "Chakan, Pune" / "Hinjewadi, Pune" / "Remote"
remote          True if fully remote, else False
employment      FULL_TIME | PART_TIME | CONTRACTOR | TEMPORARY | INTERN
experience      "5 to 8 years"
industry        "Manufacturing" | "Software" | "D2C & Consumer"
posted          "YYYY-MM-DD"
valid_through   "YYYY-MM-DD"  internal expiry, not shown publicly
salary_min      annual CTC in rupees, or None
salary_max      annual CTC in rupees, or None
client_note     one line about the employer, no names
summary         2 or 3 sentences, shown on the listing card
responsibilities  list of strings
requirements      list of strings
nice_to_have      list of strings, can be empty
=============================================================================
"""

JOBS = [
    {
     "slug": "finance-associate-bengaluru",
     "title": "Finance Associate",
     "location": "Bengaluru",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "2 to 5 years",
     "industry": "Manufacturing",
     "posted": "2026-09-28",
     "valid_through": "2026-11-27",
     "salary_min": None,
     "salary_max": None,
     "client_note": "A growing specialty chemicals company hiring for its Bengaluru office.",
     "summary": ("Join a core finance team focused on accounting operations, financial controls, "
                 "statutory compliance and maintaining strong finance processes in a fast paced environment."),
     "responsibilities": [
         "Manage day to day accounting and finance operations",
         "Maintain accurate books in the ERP and ensure financial hygiene",
         "Handle domestic and international payments and bank reconciliations",
         "Manage vendor invoices, customer invoicing and ledger reconciliations",
         "Ensure timely statutory compliance and support monthly closures",
         "Maintain audit ready books and coordinate with auditors and consultants",
     ],
     "requirements": [
         "2 to 5 years of experience in accounting or finance operations",
         "Strong accounting knowledge with hands on ERP experience",
         "Experience with bank entries, payment entries, journal entries and bill booking",
         "Good understanding of accounts payable, accounts receivable, reconciliations, invoicing and ledger scrutiny",
         "Working knowledge of GST, TDS, PF, ESIC, PTAX and related statutory compliances",
         "High ownership mindset and ability to work independently",
     ],
     "nice_to_have": [
         "Experience with Microsoft Dynamics ERP",
         "Exposure to import, export or cross border transactions",
     ],
    },
    {
     "slug": "rd-team-leader-api-synthesis-bengaluru",
     "title": "R&D Team Leader, API and Active Ingredient Synthesis",
     "location": "Bengaluru",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "3 to 15 years, depending on qualification",
     "industry": "Manufacturing",
     "posted": "2026-09-28",
     "valid_through": "2026-11-27",
     "salary_min": None,
     "salary_max": None,
     "client_note": "A growing specialty chemicals company hiring for its Bengaluru R&D team.",
     "summary": ("Lead process research and development projects for agrochemical active ingredients, "
                 "manage and mentor scientists, and remain hands on from laboratory development through pilot scale up."),
     "responsibilities": [
         "Lead and mentor a team of scientists while remaining hands on in laboratory work and project execution",
         "Drive process development, optimization, validation and scale up from laboratory to pilot plant",
         "Lead technology transfer and development of cost effective, scalable and commercially viable manufacturing processes",
         "Investigate reaction mechanisms, process impurities and impurity profiles, and guide purification strategies",
         "Interpret analytical data from NMR, mass spectrometry, HPLC and GC, and use literature search tools",
         "Own technical documentation, cost analysis, route of synthesis evaluation and development reports",
         "Work with manufacturing, analytical, procurement, EHS and other teams to deliver projects",
         "Maintain laboratory safety, IP confidentiality and organizational quality standards",
     ],
     "requirements": [
         "PhD in Organic Chemistry with 3 to 5 years of relevant experience, or MSc in Chemistry with 12 to 15 years of relevant experience",
         "Relevant experience in agrochemical R&D, API synthesis or process development",
         "Strong experience in chemical process development, optimization, validation and scale up from laboratory to pilot plant",
         "Experience in the agrochemical or pharmaceutical API industry, including technology transfer and commercialization",
         "Demonstrated ability to develop cost effective, scalable and commercially viable processes",
         "Strong understanding of purification methods including distillation, crystallization and chromatography",
     ],
     "nice_to_have": [
         "Experience using SciFinder and Reaxys",
         "Experience developing commercially viable, non infringing manufacturing processes",
     ],
    },
    {
     "slug": "associate-manager-supply-chain-planning-bengaluru",
     "title": "Associate Manager - Supply Chain Planning (EXIM Operations)",
     "location": "Bengaluru",
     "region": "Karnataka",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "1 to 4 years",
     "industry": "Manufacturing",
     "reports_to": "A member of the founding team",
     "posted": "2026-11-03",
     "valid_through": "2027-01-02",
     "salary_min": None,
     "salary_max": None,
     "client_note": "A well funded, early stage specialty chemicals company in Bengaluru, founded by IIT and IIM alumni, building an asset light, R&D driven, contract manufacturing brand across agrochemicals, surfactants, flavours and fragrances, and pharmaceuticals.",
     "summary": ("Own every import and export shipment, start to finish. This is not a coordination "
                 "seat, it is an ownership seat: plan shipments before they turn urgent, fix them fast "
                 "when they go sideways, and be the one person who always knows where things stand, "
                 "pulling Demand, Supply, Logistics and Finance together to get it done."),
     "responsibilities": [
         "Build forward shipment plans from confirmed and expected orders, aligning supplier readiness, documentation, payment terms and logistics slots before they become bottlenecks",
         "Re plan quickly when a vessel is delayed, a document is missing or a supplier slips, finding the next best route or workaround and keeping the customer informed",
         "Maintain a live view of every shipment, including status, timelines, risks and next actions",
         "Own exports end to end, from order closure to dispatch and customs clearance, meeting each customer's shipment level requirements",
         "Own imports end to end, coordinating with overseas suppliers and tracking inbound shipments through to clearance and receipt",
         "Act as the link between Demand, Supply, Logistics, Fulfilment and Finance so every shipment moves as planned",
         "Be the single point of contact for EXIM status across all teams, covering order closure, supplier fulfilment, payments, advances and receivables",
         "Spot the few things that will make or break a shipment, whether it is a document, payment, supplier or booking, and raise them early",
         "Ensure import, export and hazardous cargo documentation is complete and ready for customs clearance",
         "Build the checklists, trackers and SOPs that make EXIM predictable as the company scales, and turn recurring problems into lasting process fixes",
     ],
     "requirements": [
         "1 to 4 years of experience in supply chain, operations, program management or a similar role; EXIM experience is a plus, not a must",
         "Understanding of import and export processes and payment terms is helpful; if new to EXIM, a strong willingness to learn it quickly",
         "Strong stakeholder management across Demand, Supply, Logistics, Finance, suppliers and freight partners, with the ability to push timelines firmly while keeping relationships intact",
         "High attention to detail, able to catch incorrect documents, missed payment terms and customer specific requirements before they cause delays",
         "A genuine sense of ownership, comfortable being accountable for a shipment's outcome from order closure to delivery",
         "Comfortable planning ahead and reacting fast when something breaks",
         "Calm under pressure, with clear communication when things go wrong",
     ],
     "nice_to_have": [
         "Prior experience specifically in EXIM or international logistics",
         "Experience in a fast growing, early stage company where processes are still being built",
         "Exposure to specialty chemicals, agrochemicals or related manufacturing sectors",
     ],
    },
    {
     "slug": "qc-analytical-chemist-agro-formulations-bengaluru",
     "title": "QC Analytical Chemist",
     "location": "Bengaluru",
     "region": "Karnataka",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "5 to 10 years",
     "industry": "Manufacturing",
     "posted": "2026-11-03",
     "valid_through": "2027-01-02",
     "salary_min": None,
     "salary_max": None,
     "salary_note": "Up to \u20b912 LPA, performance-linked",
     "client_note": "A well funded, early stage specialty chemicals company in Bengaluru, founded by IIT and IIM alumni, building an asset light, R&D driven, contract manufacturing brand across agrochemicals, surfactants, flavours and fragrances, and pharmaceuticals.",
     "summary": ("Own the analytical backbone of our agro formulations business. Characterise active "
                 "ingredients, raw materials and finished products end to end, build and validate the "
                 "methods that make our data regulator ready, and be the person R&D and manufacturing "
                 "both rely on to know exactly what's in a sample and why it matters."),
     "responsibilities": [
         "Perform analysis of agrochemical active ingredients, raw materials, intermediates and finished formulations using HPLC, UHPLC, GC, LC-MS/MS, GC-MS, IC, UV-Vis, FTIR, NMR, KF & AT and wet chemical methods",
         "Develop and validate analytical methods against requirements, and run routine and non-routine testing for assay, impurities and residual solvents",
         "Interpret analytical data and prepare the reports and documentation that go into regulatory submissions",
         "Generate the physico-chemical and storage-stability data needed to support product registration",
         "Support method transfer and quality control at in-house and toll manufacturing sites",
         "Partner with the formulation R&D team on stability studies and partial validation of methods",
         "Maintain laboratory instruments and troubleshoot issues to keep testing on schedule",
         "Maintain proper laboratory records, SOPs and audit readiness across all testing",
         "Ensure full compliance with laboratory and safety standards at every stage of testing",
         "Work flexibly across geographies where manufacturing and R&D timelines require it",
     ],
     "requirements": [
         "M.Sc. in Chemistry, with a preferred concentration in an analytical discipline",
         "5 to 10 years of experience in analytical laboratories, with agrochemical formulation analytical experience mandatory",
         "Strong hands-on knowledge of chromatography (HPLC, UHPLC, GC) and related analytical techniques",
         "Clear written and verbal communication in English",
         "Comfortable working in a team of scientists and collaborating across R&D and manufacturing",
     ],
     "nice_to_have": [
         "Experience with LC-MS/MS, GC-MS, NMR or other advanced instrumentation beyond routine QC",
         "Prior exposure to regulatory submission data (physico-chemical, storage-stability) for agrochemical products",
         "Experience in a fast growing, early stage company where processes are still being built",
     ],
    },

    {
     "slug": "business-development-manager-chandigarh",
     "title": "Business Development Manager",
     "location": "Chandigarh",
     "region": "Chandigarh",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "3 to 6 years",
     "industry": "Marketing & SaaS",
     "posted": "2026-11-04",
     "valid_through": "2027-01-03",
     "salary_min": 800000,
     "salary_max": 1200000,
     "client_note": "A technical marketing company based in Sector 17, Chandigarh, working with SaaS, AI and cloud product companies on cloud marketplace listings, AI-driven discovery and demand generation.",
     "summary": ("Own the full sales cycle for a marketing partner that gets SaaS, AI and cloud products "
                 "listed and selling across the major cloud marketplaces. You will find the technology "
                 "companies that need that visibility, build the relationship, shape the proposal with the "
                 "content and SDR teams, and close it. This suits someone who can hold a credible "
                 "conversation about cloud marketplaces and AI discovery, not just run a pipeline."),
     "responsibilities": [
         "Identify and qualify new business opportunities with SaaS, AI and cloud technology companies",
         "Own the end to end sales cycle, from prospecting and discovery through negotiation and close",
         "Run market research and competitive analysis to sharpen targeting and positioning",
         "Present marketplace listing, AI visibility and content services to technical and marketing decision makers",
         "Build and nurture client relationships that grow into larger, longer term accounts",
         "Work with the internal marketing, content and SDR teams to tailor proposals and presentations",
         "Manage client onboarding and stay involved through to account growth",
         "Maintain a healthy pipeline in the CRM and report on sales performance metrics",
         "Contribute to local business development strategy across the Chandigarh region",
     ],
     "requirements": [
         "3 to 6 years in business development, B2B sales or account management within technology or SaaS",
         "Proven track record in lead generation and pipeline management, with hands on CRM discipline",
         "Strong relationship building, negotiation and stakeholder communication skills, with the ability to influence decision makers",
         "Comfortable with market research, competitive analysis and GTM strategy for cloud and AI solutions",
         "Able to present complex technical and marketing services clearly, with basic familiarity with cloud marketplaces and AI platforms",
         "Bachelor's degree in Business, Marketing, Technology or a related field, or equivalent practical experience",
         "Able to work on site in Chandigarh, with strong organisational skills, self motivation and a results oriented approach",
     ],
     "nice_to_have": [
         "Direct experience selling SaaS, cloud or AI products",
         "Hands on exposure to cloud marketplaces such as AWS, Azure, GCP, Salesforce, Databricks, Snowflake, Oracle or SAP",
         "Familiarity with AI discovery platforms and how brands surface in tools like ChatGPT, Gemini, Claude and Perplexity",
         "Experience collaborating closely with technical and content teams on proposals",
     ],
    },

    {
     "slug": "marketing-manager-chandigarh",
     "title": "Marketing Manager",
     "location": "Chandigarh",
     "region": "Chandigarh",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "3 to 6 years",
     "industry": "Marketing & SaaS",
     "posted": "2026-11-04",
     "valid_through": "2027-01-03",
     "salary_min": 800000,
     "salary_max": 1200000,
     "client_note": "A B2B growth and AWS partnership acceleration company based in Sector 17, Chandigarh, helping technology and cloud businesses strengthen their AWS presence, build go to market strategies and generate qualified pipeline.",
     "summary": ("A hybrid marketing and sales development role. You will pick the accounts worth winning, "
                 "work out who inside them matters, and run the outreach that turns that research into booked "
                 "meetings. Expect to split your time between campaign work and hands on prospecting, with "
                 "performance measured on qualified leads and discovery calls as much as on campaign reach. "
                 "A strong fit if you want real exposure to ABM, outbound and AWS focused go to market in one seat."),
     "responsibilities": [
         "Research and activate high value target accounts that match the ideal customer profile",
         "Map decision makers across founders, CEOs, sales, alliance, cloud and AWS, and marketing leadership",
         "Build and run multi touch ABM campaigns across LinkedIn, email, content and direct outreach",
         "Prospect and generate qualified B2B leads through LinkedIn, email, calls, databases and events",
         "Write personalised outreach messages and run structured follow up until a prospect qualifies or closes",
         "Qualify prospects on fit, authority, requirement and opportunity, and book discovery calls for the business development team",
         "Re engage dormant leads and previously contacted accounts",
         "Support outbound campaigns targeting AWS Partners, cloud companies, SaaS companies, ISVs, MSPs and technology service providers",
         "Help plan and execute demand generation campaigns across email, LinkedIn, webinars, events and partner marketing",
         "Coordinate marketing collateral such as one pagers, case studies, blogs, eBooks and presentations",
         "Build, clean and segment prospect databases, and keep CRM records accurate and current",
         "Track outreach activity, response rates, meetings booked and campaign performance, and report weekly and monthly",
     ],
     "requirements": [
         "3 to 6 years in B2B marketing, lead generation, sales development or account based marketing",
         "Strong written and verbal communication, with the ability to write personalised outreach and marketing copy",
         "Able to research companies and identify the right decision makers inside them",
         "Hands on experience with LinkedIn prospecting and email outreach",
         "Solid understanding of lead qualification and B2B sales funnels",
         "Good working knowledge of Excel or Google Sheets, and of CRM and database management",
         "Able to run multiple campaigns and target accounts at the same time",
         "Analytical mindset, and comfortable being measured on pipeline and campaign metrics",
         "Currently based in Chandigarh, as this role is open to local candidates only",
     ],
     "nice_to_have": [
         "Experience working with IT services, SaaS, cloud or AWS technology companies",
         "Familiarity with the AWS Partner ecosystem and cloud services",
         "Experience with LinkedIn Sales Navigator and other prospecting or data intelligence tools",
         "Familiarity with CRM and marketing automation platforms",
         "A track record executing ABM or targeted outbound campaigns",
     ],
    },

    {
     "slug": "hr-manager-chandigarh",
     "title": "HR Executive / Manager",
     "location": "Chandigarh",
     "region": "Chandigarh",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "2 to 5 years",
     "industry": "Marketing & SaaS",
     "posted": "2026-11-04",
     "valid_through": "2027-01-03",
     "salary_min": None,
     "salary_max": None,
     "client_note": "A specialist technical marketing company based in Sector 17, Chandigarh, working with SaaS, AI and cloud brands on cloud marketplace listings, AI driven discovery and demand generation, with a team growing across marketing, content and sales development.",
     "summary": ("Own the HR function for a growing technical marketing team. This is a standalone, hands on "
                 "role covering the full employee lifecycle, from hiring and onboarding through performance, "
                 "engagement and compliance. A good fit if you want the scope to build HR processes rather "
                 "than inherit them, and the visibility that comes with working directly alongside leadership."),
     "responsibilities": [
         "Own end to end HR operations for a growing technical marketing team",
         "Run recruitment and onboarding, from identifying talent needs with leadership through to a new joiner's first weeks",
         "Design and implement HR policies, and keep HR documentation accurate and audit ready",
         "Manage performance review cycles and support career progression frameworks aligned to business goals",
         "Handle employee relations, resolving workplace issues fairly and in confidence",
         "Coordinate payroll with the finance team and administer employee benefits",
         "Support workforce planning alongside the leadership team",
         "Coordinate training and development initiatives that build skills and engagement",
         "Organise employee engagement programmes and help build an inclusive culture",
         "Maintain compliance with local labour laws and regulations",
         "Report on HR metrics and use them to inform decisions",
     ],
     "requirements": [
         "2 to 5 years across core HR functions including recruitment, onboarding, performance management and employee relations",
         "Experience developing HR policy and maintaining HR documentation",
         "Working knowledge of local labour laws and compliance requirements",
         "Able to coordinate payroll and administer benefits",
         "Strong communication, interpersonal and conflict resolution skills, with the ability to build trust across teams",
         "Experience coordinating training, learning and development, and employee engagement initiatives",
         "Proficiency with HRIS or similar HR software tools",
         "Bachelor's degree in Human Resources, Business Administration or a related field",
         "Able to work independently, handle sensitive information discreetly and make data informed decisions",
         "Comfortable in a fast paced, high growth setting supporting cross functional teams",
         "Based in Chandigarh, as this is a full time on site role",
     ],
     "nice_to_have": [
         "HR certifications",
         "Prior experience managing HR in a technology, marketing or professional services company",
         "Experience building HR processes from scratch in a growing team",
         "Familiarity with HR analytics and reporting tools",
     ],
    },

]

# Previous postings are retained for reference but are not published.
LEGACY_JOBS = [
    # ---------------------------------------------------------------------
    # EXAMPLE, KEPT COMMENTED SO THE BOARD STARTS EMPTY AND HONEST.
    # Copy this block, fill it in with a real open role, uncomment, rebuild.
    # ---------------------------------------------------------------------
    # {
    #  "slug": "production-manager-chakan",
    #  "title": "Production Manager",
    #  "location": "Chakan, Pune",
    #  "remote": False,
    #  "employment": "FULL_TIME",
    #  "experience": "8 to 12 years",
    #  "industry": "Manufacturing",
    #  "posted": "2026-08-14",
    #  "valid_through": "2026-10-14",
    #  "salary_min": 1200000,
    #  "salary_max": 1800000,
    #  "client_note": "A tier-1 automotive component supplier in the Chakan belt.",
    #  "summary": ("Own the production floor end to end: output, quality, manpower and "
    #              "the interface with dispatch. Reporting to the plant head."),
    #  "responsibilities": [
    #      "Daily production planning against despatch commitments",
    #      "Manpower deployment across shifts",
    #      "Quality and rejection control at line level",
    #      "Lean and TPM initiatives on the shop floor",
    #  ],
    #  "requirements": [
    #      "8+ years in automotive or precision manufacturing",
    #      "Owned production targets, not just supervised a line",
    #      "Comfortable with rotational shifts",
    #      "BE Mechanical or Production, or equivalent",
    #  ],
    #  "nice_to_have": [
    #      "Experience of a plant ramp-up",
    #      "Exposure to dispatch and supply chain planning",
    #  ],
    # },
    {
     "slug": "marketing-manager-pune",
     "title": "Marketing Manager",
     "location": "Pune",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "4 to 7 years",
     "industry": "Software",
     "posted": "2026-08-17",
     "valid_through": "2026-10-16",
     "salary_min": 1000000,
     "salary_max": 1000000,
     "client_note": "An Enterprise SaaS company transitioning into the DeepTech space, Pune.",
     "summary": ("Own the brand narrative for a company moving from Enterprise SaaS into "
                 "DeepTech. Blend brand storytelling, data driven digital strategy and "
                 "on ground event execution, working from office in Pune."),
     "responsibilities": [
         "Own and evolve the brand identity across all customer touchpoints",
         "Develop brand guidelines and lead positioning strategy as the company expands into DeepTech",
         "Drive thought leadership content and PR initiatives",
         "Build annual and quarterly marketing plans aligned with business growth objectives",
         "Conduct competitive analysis and define go to market strategies for new offerings",
         "Manage and grow presence across LinkedIn, Twitter/X and other relevant platforms",
         "Plan and execute performance marketing campaigns across SEO, SEM and paid social",
         "Track digital KPIs and manage the content calendar and website content strategy",
         "Plan and execute industry events, product launches, webinars and trade show participation",
         "Coordinate ATL campaigns and BTL activations, and manage event budgets and vendor relationships",
     ],
     "requirements": [
         "4 to 7 years of marketing experience, ideally in B2B SaaS or technology companies",
         "Proven track record in brand building and strategic marketing",
         "Strong understanding of digital marketing platforms, tools and analytics",
         "Experience managing events end to end, both ATL and BTL",
         "Excellent written and verbal communication skills",
     ],
     "nice_to_have": [
         "Exposure to DeepTech, AI or emerging technology domains",
         "MBA in Marketing or equivalent qualification",
     ],
    },
    {
     "slug": "senior-ai-engineer-new-delhi",
     "title": "Senior AI Engineer",
     "location": "New Delhi",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "2 to 5 years",
     "industry": "Software",
     "posted": "2026-08-17",
     "valid_through": "2026-10-16",
     "salary_min": 800000,
     "salary_max": 800000,
     "client_note": "A GenAI and LLM solutions company serving CPG, retail and finance clients.",
     "summary": ("Hands on role building agentic AI systems, RAG pipelines and vector "
                 "database architectures for enterprise clients, working alongside "
                 "experienced AI engineers and data scientists."),
     "responsibilities": [
         "Design and implement multi LLM agentic systems using LangGraph, LangChain or custom orchestration",
         "Build and optimize RAG pipelines with vector databases such as Pinecone, Qdrant, OpenSearch, Weaviate or FAISS",
         "Engineer context injection and retrieval infrastructure for domain specific GenAI solutions",
         "Collaborate with data engineers on embedding stores and unstructured data ingestion pipelines",
         "Fine tune or adapt transformer based models for domain specific tasks when required",
         "Deploy solutions across cloud and on prem environments, balancing security, latency and scalability",
         "Work on client facing projects, translating business problems into technical architectures",
     ],
     "requirements": [
         "2 to 5 years of experience with strong programming in Python",
         "Hands on experience with transformer libraries such as Hugging Face, OpenAI, Anthropic or Llama",
         "Experience with LangChain, LangGraph or similar orchestration frameworks",
         "Hands on expertise with vector databases and embedding pipelines",
         "Working knowledge of RAG system design and best practices",
         "Familiarity with containerization and orchestration, Docker and Kubernetes",
         "Experience with Git",
     ],
     "nice_to_have": [
         "Prior work fine tuning transformers or domain adaptation",
         "Familiarity with observability and monitoring for LLM applications",
         "Exposure to multi agent systems and reinforcement learning concepts",
         "Experience integrating AI into enterprise workflows, CRMs or ERPs",
         "Basic understanding of AWS, Azure or Google Cloud AI services",
     ],
    },
    {
     "slug": "brand-associate-bengaluru",
     "title": "Brand Associate",
     "location": "Bengaluru",
     "remote": False,
     "employment": "FULL_TIME",
     "experience": "0 to 2 years",
     "industry": "D2C & Consumer",
     "posted": "2026-08-17",
     "valid_through": "2026-10-16",
     "salary_min": 600000,
     "salary_max": 800000,
     "client_note": "A fast growing D2C beauty and personal care brand, Bengaluru.",
     "summary": ("An early career brand role for someone who wants to build a consumer brand "
                 "rather than just market one. You will work across brand ideation, on ground "
                 "events, social media and content shoots, with real ownership from month one."),
     "responsibilities": [
         "Develop brand level creative strategies that strengthen the brand's positioning",
         "Generate campaign ideas from consumer insights and seasonal trends",
         "Identify the right timing, platforms and messaging to maximise brand impact",
         "Execute brand campaigns, product launches and promotional events end to end",
         "Coordinate with internal teams, agencies and vendors to keep delivery on track",
         "Manage event logistics, branding materials and post event reporting",
         "Grow and manage the brand's presence across Instagram, Facebook and LinkedIn",
         "Plan, schedule and publish on brand content, and track how it performs",
         "Plan and oversee photo and video shoots for campaigns and product launches",
         "Work with photographers, stylists, influencers and production partners on shoot day",
         "Run market research and competitor benchmarking to feed the next campaign",
         "Report on campaign performance and recommend what to change next time",
     ],
     "requirements": [
         "0 to 2 years of experience in e commerce, D2C or consumer brand marketing",
         "Master's degree in Business, Marketing or a related field",
         "Strong analytical skills and comfort with web analytics tools",
         "Excellent written and verbal communication, and the ability to work across teams",
         "Detail oriented and organised, able to hold several priorities at once",
     ],
     "nice_to_have": [
         "Experience in beauty, personal care or wellness categories",
         "Hands on experience running a brand's social media, not just scheduling posts",
         "Exposure to influencer led campaigns and content shoot coordination",
     ],
    },
]
