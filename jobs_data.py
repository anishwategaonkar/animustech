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
]
