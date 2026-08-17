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
]
