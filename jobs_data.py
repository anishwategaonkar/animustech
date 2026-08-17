# -*- coding: utf-8 -*-
"""
Live job listings. Edit this file, then run:  python3 _build_jobs.py

=============================================================================
RULES. These are not style preferences, they protect you.
=============================================================================

1. ONLY POST ROLES YOU ARE GENUINELY RECRUITING FOR.
   Google removes sites from Google for Jobs for posting roles that are not
   real or not open. It is also unfair to candidates who apply.

2. EVERY JOB NEEDS A REAL `valid_through` DATE.
   Google requires it. Once that date passes, the listing stops showing.
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
valid_through   "YYYY-MM-DD"  (delete the job once this passes)
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
