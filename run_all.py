"""
Blade vs. Mallet -- End-to-End Pipeline
Author: Jack Forman | IS477 SP26

Steps
-----
1. acquire.py                -- SHA-256 integrity check on raw data files
2. clean_and_integrate.ipynb -- clean and merge the two datasets
3. quality_assesment.ipynb   -- run quality checks, write report
4. analysis.py               -- summary statistics and figures

Usage:  python run_all.py

Outputs
-------
  data/cleaned/    cleaned CSVs
  data/integrated/ merged dataset
  logs/            acquisition log, quality report, analysis stats
  results/         fig1 -- fig4
"""

import os
import subprocess
import sys

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE    = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(BASE, "scripts")
PY      = sys.executable

# ── Pipeline steps ─────────────────────────────────────────────────────────────
STEPS = [
    ("Step 1  Integrity check",        [PY, os.path.join(SCRIPTS, "acquire.py")]),
    ("Step 2  Clean & integrate",      [PY, "-m", "jupyter", "nbconvert",
                                            "--to", "notebook", "--execute", "--inplace",
                                            os.path.join(BASE, "clean_and_integrate.ipynb")]),
    ("Step 3  Quality assessment",     [PY, "-m", "jupyter", "nbconvert",
                                            "--to", "notebook", "--execute", "--inplace",
                                            os.path.join(BASE, "quality_assesment.ipynb")]),
    ("Step 4  Analysis & figures",     [PY, os.path.join(SCRIPTS, "analysis.py")]),
]

# ── Runner ─────────────────────────────────────────────────────────────────────
def run(label, cmd):
    print(f"\n  [ {label} ]")
    print("  " + "-" * 45)
    result = subprocess.run(cmd, cwd=BASE)
    if result.returncode != 0:
        print(f"\n  FAILED -- exit code {result.returncode}")
        print("  Fix the error above and re-run.")
        sys.exit(result.returncode)
    print(f"  done.")


# ── Main ───────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Blade vs. Mallet -- End-to-End Workflow")
print("  Author: Jack Forman | IS477 SP26")
print("=" * 55)

for label, cmd in STEPS:
    run(label, cmd)

print("\n" + "=" * 55)
print("  Pipeline complete.")
print()
print("  data/cleaned/     cleaned datasets")
print("  data/integrated/  merged dataset")
print("  logs/             acquisition, quality, analysis logs")
print("  results/          figures 1 - 4")
print("=" * 55 + "\n")
