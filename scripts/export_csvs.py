#!/usr/bin/env python3
"""Regenerate both CSV exports from data/census_master.json WITH the normalized
`private_partner_owner` column. Run after normalize_owners.py.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data/census_master.json").read_text())

for r in DATA:
    r["private_partner_owner"] = r.get("owner_group")

MASTER_COLS = ["census_id", "name", "address", "city", "county", "cad_account", "units",
               "year_built", "sponsor", "private_partner_owner", "species", "statute", "tier",
               "traveling", "in_target_set", "appraised_value", "exemption_status",
               "first_exempt_year", "kill_regime", "kill_date", "captured_9_1_2025",
               "recent_capital_event", "litigation", "confidence", "gaps_n", "kill_basis"]

PL_COLS = ["census_id", "name", "address", "city", "county", "sponsor", "tier",
           "private_partner_owner", "private_partner_parent", "private_partner_spe",
           "private_partner_source", "lender", "lender_loan_amount", "lender_source",
           "lender_gap", "year_built", "year_built_source"]


def write(path, cols):
    with open(ROOT / path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in DATA:
            w.writerow([r.get(c) for c in cols])
    print(f"wrote {path} ({len(DATA)} rows, {len(cols)} cols)")


write("data/census_master.csv", MASTER_COLS)
write("data/partner_lender_yearbuilt.csv", PL_COLS)
