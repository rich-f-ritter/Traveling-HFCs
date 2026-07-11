#!/usr/bin/env python3
"""Finalize: merge underwriting numbers into the master, compute annual tax-at-stake
for every Tier-1 property, derive billed-now vs at-2027-risk status, and emit the
ranked target list + summary stats used by the final report.

Inputs : data/census_master.json (flattened), census/enrich_foregone_tax.json
Outputs: data/census_master_final.csv, data/target_list.csv, docs/_final_stats.json
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPRESENTATIVE_RATE = 0.023  # ~2.2-2.4% TX combined rate; used only where no precise rate

recs = json.loads((ROOT / "data/census_master.json").read_text())

# --- merge precise foregone-tax enrichment by census_id ---
enrich = {}
ef = ROOT / "census/enrich_foregone_tax.json"
if ef.exists():
    for e in json.loads(ef.read_text()):
        cid = e.get("census_id")
        if cid:
            enrich[cid] = e


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def norm_key(r):
    """Rough complex key to collapse multi-parcel fragments of one property."""
    name = (r.get("name") or "").lower()
    name = re.sub(r"\b(lot|blk|block|bldg|building|phase|ph|unit|land|improvement|only|sec|section)\b.*", "", name)
    name = re.sub(r"[^a-z0-9 ]", "", name).strip()
    addr = (r.get("address") or "").lower()
    addr = re.sub(r"[^a-z0-9 ]", "", addr).strip()
    base = name[:18] or addr[:18] or (r.get("census_id") or "")
    return (r.get("county"), base)


for r in recs:
    cid = r.get("census_id")
    e = enrich.get(cid, {})
    # units: prefer enrich
    if e.get("units"):
        r["units"] = e["units"]
    av = fnum(r.get("appraised_value"))
    # annual tax at stake
    precise = fnum(e.get("annual_foregone_tax_est"))
    if precise is not None:
        r["tax_at_stake"] = round(precise)
        r["tax_basis"] = "precise (per-account rate)"
    elif r.get("tier") == 1 and av:
        r["tax_at_stake"] = round(av * REPRESENTATIVE_RATE)
        r["tax_basis"] = "estimated (2.3% representative rate)"
    else:
        r["tax_at_stake"] = None
        r["tax_basis"] = None
    # current status: billed now (taxable) vs still-exempt (2027 risk) vs unknown
    ce = e.get("currently_exempt")
    es = (r.get("exemption_status") or "").lower()
    if ce == "no" or es == "taxable":
        r["current_status"] = "billed_now"          # exemption already denied/stripped
    elif ce == "yes" or es == "exempt":
        r["current_status"] = "exempt_at_2027_risk"  # still exempt, dies at cliff
    else:
        r["current_status"] = "unknown"

# --- distinct-complex estimate (collapse parcel fragments) ---
complexes = defaultdict(list)
for r in recs:
    complexes[norm_key(r)].append(r)
distinct = len(complexes)

# --- stats ---
def s_sum(rows, f="tax_at_stake"):
    return sum(fnum(r.get(f)) or 0 for r in rows)

t1 = [r for r in recs if r.get("tier") == 1]
t2 = [r for r in recs if r.get("tier") == 2]
t3 = [r for r in recs if r.get("tier") == 3]
billed = [r for r in recs if r.get("current_status") == "billed_now"]
atrisk = [r for r in recs if r.get("current_status") == "exempt_at_2027_risk"]
expansions = [r for r in recs if str(r.get("census_id")).startswith("TX-NEW")]

stats = {
    "records": len(recs),
    "distinct_complexes_est": distinct,
    "with_cad_account": sum(1 for r in recs if r.get("cad_account")),
    "expansions_raw": len(expansions),
    "total_appraised": s_sum(recs, "appraised_value"),
    "tier1_records": len(t1), "tier2_records": len(t2), "tier3_records": len(t3),
    "tier1_appraised": s_sum(t1, "appraised_value"),
    "tier1_tax_at_stake": s_sum(t1, "tax_at_stake"),
    "billed_now_records": len(billed), "billed_now_tax": s_sum(billed, "tax_at_stake"),
    "atrisk_records": len(atrisk), "atrisk_tax": s_sum(atrisk, "tax_at_stake"),
    "total_annual_tax_at_stake": s_sum(recs, "tax_at_stake"),
}
(ROOT / "docs/_final_stats.json").write_text(json.dumps(stats, indent=2))

# --- enhanced master CSV ---
cols = ["census_id", "name", "address", "city", "county", "cad_account", "units",
        "sponsor", "species", "tier", "traveling", "current_status", "appraised_value",
        "tax_at_stake", "tax_basis", "kill_regime", "kill_date", "exemption_status",
        "litigation", "confidence", "gaps_n"]
with open(ROOT / "data/census_master_final.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(cols)
    for r in recs:
        w.writerow([r.get(c) for c in cols])
(ROOT / "data/census_master_final.json").write_text(json.dumps(recs, indent=2))

# --- ranked target list (Tier-1, by tax at stake) ---
ranked = sorted([r for r in t1 if fnum(r.get("tax_at_stake"))],
                key=lambda r: -(fnum(r.get("tax_at_stake")) or 0))
tcols = ["rank", "name", "city", "county", "sponsor", "units", "appraised_value",
         "tax_at_stake", "current_status", "kill_date"]
with open(ROOT / "data/target_list.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(tcols)
    for i, r in enumerate(ranked, 1):
        w.writerow([i, r.get("name"), r.get("city"), r.get("county"),
                    r.get("sponsor"), r.get("units"), r.get("appraised_value"),
                    r.get("tax_at_stake"), r.get("current_status"), r.get("kill_date")])

def money(x):
    return f"${x/1e9:.2f}B" if x >= 1e9 else f"${x/1e6:.1f}M"

print(f"records={stats['records']} distinct_complexes~={distinct} tier1={len(t1)} tier2={len(t2)} tier3={len(t3)}")
print(f"total_appraised={money(stats['total_appraised'])} tier1_appraised={money(stats['tier1_appraised'])}")
print(f"annual_tax_at_stake(all)={money(stats['total_annual_tax_at_stake'])}")
print(f"  billed_now: {len(billed)} recs / {money(stats['billed_now_tax'])}")
print(f"  exempt_at_2027_risk: {len(atrisk)} recs / {money(stats['atrisk_tax'])}")
print(f"  unknown status: {len(recs)-len(billed)-len(atrisk)} recs")
print("TOP 12 TARGETS by annual tax at stake:")
for i, r in enumerate(ranked[:12], 1):
    print(f"  {i:2d}. {money(fnum(r['tax_at_stake']))}  {r.get('name')} ({r.get('city')}, {r.get('county')}) [{r.get('current_status')}]")
