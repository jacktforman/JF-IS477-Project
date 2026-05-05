"""
acquire.py
----------
Acquisition and integrity verification script for the Blade vs. Mallet project.

This project uses two manually curated datasets rather than live-scraped data,
because the original web sources (ESPN, GolfWRX) are JavaScript-rendered and
not reliably machine-readable. The raw CSVs included in this repository were
built from publicly available journalism sources documented in each file's
'source' column.

This script:
  1. Verifies that all expected raw data files are present
  2. Computes and records SHA-256 checksums for each file
  3. Compares against known-good checksums to confirm file integrity
  4. Logs results to logs/acquisition_log.txt

Known-good checksums (recorded at time of data collection, April 2026):
  pga_tour_sgputt_2025_raw.csv    f42a0b4911bb31ee61af092ab963d171fbcf94a4c3c1242fc2f9acee3610c34c
  masters_2026_leaderboard_raw.csv eca7d1e34abd5cdcfda709b90e2549716cefa525eb4232583e567d95d67b5cfd

Usage:
  python scripts/acquire.py
"""

import hashlib
import os
from datetime import datetime

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

EXPECTED = {
    "pga_tour_sgputt_2025_raw.csv": "f42a0b4911bb31ee61af092ab963d171fbcf94a4c3c1242fc2f9acee3610c34c",
    "masters_2026_leaderboard_raw.csv": "eca7d1e34abd5cdcfda709b90e2549716cefa525eb4232583e567d95d67b5cfd",
}

SOURCES = {
    "pga_tour_sgputt_2025_raw.csv": (
        "PGA Tour official statistics (2025 season) compiled via Eden Steak analysis. "
        "Source: https://edensteak.com/?p=33 / https://www.pgatour.com/stats/putting. "
        "Collected: April 2026. License: Publicly available; educational use."
    ),
    "masters_2026_leaderboard_raw.csv": (
        "2026 Masters Tournament leaderboard and equipment data compiled from multiple "
        "journalism sources (Golf Monthly, EssentiallySports, Sky Sports, MyGolfSpy, Wikipedia). "
        "Collected: April 13-14, 2026. License: Publicly available journalism; educational use."
    ),
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    lines = []
    lines.append(f"Acquisition log -- {datetime.utcnow().isoformat()} UTC")
    lines.append("=" * 60)
    lines.append("Project: Blade vs. Mallet -- PGA Tour Putting Performance")
    lines.append("Author: Jack Forman | IS477 SP26")
    lines.append("")

    all_passed = True

    for filename, expected_hash in EXPECTED.items():
        path = os.path.join(RAW_DIR, filename)
        lines.append(f"File: {filename}")
        lines.append(f"  Source: {SOURCES[filename]}")

        if not os.path.exists(path):
            msg = f"  MISSING -- file not found at {path}"
            lines.append(msg)
            print(msg)
            all_passed = False
            continue

        actual_hash = sha256_file(path)
        lines.append(f"  Expected SHA-256: {expected_hash}")
        lines.append(f"  Actual SHA-256:   {actual_hash}")

        if actual_hash == expected_hash:
            lines.append("  Integrity check: PASSED")
            print(f"  {filename}: PASSED")
        else:
            lines.append("  Integrity check: FAILED -- file may have been modified")
            print(f"  {filename}: FAILED")
            all_passed = False

        size_kb = os.path.getsize(path) / 1024
        lines.append(f"  File size: {size_kb:.1f} KB")
        lines.append("")

    lines.append("=" * 60)
    lines.append(f"Overall result: {'ALL CHECKS PASSED' if all_passed else 'ONE OR MORE CHECKS FAILED'}")

    log_path = os.path.join(LOG_DIR, "acquisition_log.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\nLog written to {log_path}")


if __name__ == "__main__":
    main()
