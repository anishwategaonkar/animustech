#!/usr/bin/env python3
"""
Runs every build script in the right order, then injects analytics.

Order matters: the generators overwrite whole files, so the analytics
injection has to come last or it gets wiped out.

    python3 _build_all.py
"""
import subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    "_build.py",                 # recruitment landing pages
    "_build_software.py",        # /software/ hub
    "_build_software_pages.py",  # /software/ children
    "_build_contact.py",         # /contact/ and thank-you
    "_build_blog.py",            # /blog/
    "_build_jobs.py",            # /jobs/ and apply flows
    "_build_tool.py",            # /tools/
    "_build_static.py",          # re-inject header/footer into hand written pages
    "_build_analytics.py",       # MUST be last
]

failed = []
for s in SCRIPTS:
    path = os.path.join(ROOT, s)
    if not os.path.exists(path):
        print(f"-- {s}: not found, skipping")
        continue
    print(f"-- {s}")
    r = subprocess.run([sys.executable, path], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        failed.append(s)
        print(r.stdout)
        print(r.stderr)
    else:
        tail = [l for l in r.stdout.strip().splitlines() if l.strip()]
        if tail:
            print("   " + tail[-1])

print()
if failed:
    print("FAILED:", ", ".join(failed))
    sys.exit(1)
print("All builds completed.")
