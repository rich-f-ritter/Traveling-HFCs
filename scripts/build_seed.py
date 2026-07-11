#!/usr/bin/env python3
"""Phase 0 — convert the Yardi Matrix seed xlsx into the census substrate.

Outputs:
  data/seed_properties.csv    — clean tabular seed (335 rows)
  data/seed_properties.json   — structured records with derived fields + stable IDs
  data/sponsors.json          — the 13 sponsoring entities with a classification scaffold
Derived fields added: traveling flag (sponsor home county vs property county),
sponsor legal-species guess, and a stable census id per property.
"""
import csv
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/Traveling_HFC_deals_March_2026.xlsx"

# --- Sponsor reference scaffold -------------------------------------------------
# species: HFC (Ch.394, dies 1/1/2027 if traveling+no host resolutions),
#          PFC (Ch.303, HB2071 grandfathered), HA (housing authority, separate regime).
# home_county is a STARTING guess to seed the traveling flag; Phase 1 verifies it.
SPONSORS = {
    "Pleasanton Housing Finance Corporation": {
        "aka": ["Pleasanton HFC", "PHFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "Pleasanton", "home_county": "Atascosa", "tier": 1},
    "Cameron County Housing Finance Corporation, The": {
        "aka": ["Cameron County HFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "San Benito", "home_county": "Cameron", "tier": 1},
    "La Villa Housing Finance Corporation": {
        "aka": ["La Villa HFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "La Villa", "home_county": "Hidalgo", "tier": 1},
    "Edcouch Community Housing Finance Corporation": {
        "aka": ["Edcouch HFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "Edcouch", "home_county": "Hidalgo", "tier": 1},
    "Maverick County Housing Finance Corporation": {
        "aka": ["Maverick County HFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "Eagle Pass", "home_county": "Maverick", "tier": 1},
    "Garland Housing Finance Corporation": {
        "aka": ["Garland HFC"], "species": "HFC", "statute": "Ch.394",
        "home_city": "Garland", "home_county": "Dallas", "tier": 1},
    "Texas Essential Housing Public Facility Corporation": {
        "aka": ["Texas Essential Housing PFC", "TEH PFC"], "species": "PFC", "statute": "Ch.303",
        "home_city": None, "home_county": None, "tier": 2},
    "Pecos Housing Authority": {
        "aka": ["Pecos HA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "Pecos", "home_county": "Reeves", "tier": 3},
    "Houston Housing Authority": {
        "aka": ["Houston HA", "HHA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "Houston", "home_county": "Harris", "tier": 3},
    "Cameron County Housing Authority": {
        "aka": ["Cameron County HA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "San Benito", "home_county": "Cameron", "tier": 3},
    "Rosenberg Housing Authority": {
        "aka": ["Rosenberg HA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "Rosenberg", "home_county": "Fort Bend", "tier": 3},
    "San Benito Housing Authority": {
        "aka": ["San Benito HA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "San Benito", "home_county": "Cameron", "tier": 3},
    "Plano Housing Authority": {
        "aka": ["Plano HA"], "species": "HA", "statute": "HA (Ch.392)",
        "home_city": "Plano", "home_county": "Collin", "tier": 3},
}

COLS = ["Matrix SP Link", "MarketID", "PropertyID", "PHA Owner", "PHA role on property",
        "PHA Jurisdiction", "Property City", "Property County", "PropertyCityForJurisdiction",
        "Private partner 1", "Private partner 2", "Private partner 3", "Property Status",
        "Affordable Housing Status", "Ground Lease comment", "Related Sale date",
        "Related Sales Comments"]

FIELD = {
    "market_id": 1, "property_id": 2, "sponsor": 3, "role": 4, "sponsor_jurisdiction": 5,
    "property_city": 6, "property_county": 7, "partner1": 9, "partner2": 10, "partner3": 11,
    "status": 12, "affordable": 13, "ground_lease_comment": 14, "sale_date": 15, "sale_comment": 16,
}


def clean(v):
    if v is None:
        return None
    s = str(v).strip()
    return s or None


def main():
    wb = openpyxl.load_workbook(RAW, data_only=True)
    ws = wb["Traveling HFC properties"]
    rows = list(ws.iter_rows(values_only=True))[1:]  # skip header

    records = []
    for r in rows:
        rec = {k: clean(r[i]) for k, i in FIELD.items()}
        sp = SPONSORS.get(rec["sponsor"], {})
        home_county = sp.get("home_county")
        pc = rec["property_county"]
        # traveling flag: sponsor home county != property county (None home => unknown)
        if home_county and pc:
            rec["traveling"] = "yes" if home_county.lower() != pc.lower() else "no"
        else:
            rec["traveling"] = "unknown"
        rec["sponsor_species"] = sp.get("species", "UNKNOWN")
        rec["sponsor_statute"] = sp.get("statute", "UNKNOWN")
        rec["tier"] = sp.get("tier")
        rec["sponsor_home_county"] = home_county
        # stable census id: market-property
        rec["census_id"] = f"TX-{rec['market_id']}-{rec['property_id']}"
        # partners as list
        rec["partners"] = [p for p in (rec.pop("partner1"), rec.pop("partner2"), rec.pop("partner3")) if p]
        records.append(rec)

    # sale_date may be datetime -> str
    for rec in records:
        if rec.get("sale_date"):
            rec["sale_date"] = str(rec["sale_date"])[:10]

    (ROOT / "data/seed_properties.json").write_text(json.dumps(records, indent=2))

    # CSV
    csv_cols = ["census_id", "sponsor", "sponsor_species", "sponsor_statute", "tier",
                "traveling", "role", "sponsor_home_county", "sponsor_jurisdiction",
                "property_city", "property_county", "status", "affordable",
                "sale_date", "ground_lease_comment", "sale_comment"]
    with open(ROOT / "data/seed_properties.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(csv_cols)
        for rec in records:
            w.writerow([rec.get(c) for c in csv_cols])

    # sponsors.json with live counts
    counts = {}
    trav = {}
    for rec in records:
        s = rec["sponsor"]
        counts[s] = counts.get(s, 0) + 1
        if rec["traveling"] == "yes":
            trav[s] = trav.get(s, 0) + 1
    sponsors_out = []
    for name, meta in SPONSORS.items():
        sponsors_out.append({
            "name": name, **meta,
            "property_count": counts.get(name, 0),
            "traveling_count_seed": trav.get(name, 0),
            "classification_status": "SEED_GUESS_UNVERIFIED",
        })
    (ROOT / "data/sponsors.json").write_text(json.dumps(sponsors_out, indent=2))

    # summary
    print(f"records: {len(records)}")
    from collections import Counter
    print("by species:", dict(Counter(r["sponsor_species"] for r in records)))
    print("by tier:", dict(Counter(r["tier"] for r in records)))
    print("by traveling:", dict(Counter(r["traveling"] for r in records)))
    print("tier-1 (HFC) traveling:",
          sum(1 for r in records if r["tier"] == 1 and r["traveling"] == "yes"))


if __name__ == "__main__":
    main()
