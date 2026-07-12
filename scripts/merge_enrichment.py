#!/usr/bin/env python3
"""Fold the 46-batch partner/lender/year-built enrichment back into the master.

Reads census/enrich/pl_batch_*.json (one array per batch), keys by census_id, and:
  - adds private_partner_spe/parent, lender(+amount), year_built to data/census_master.json
  - writes data/partner_lender_yearbuilt.csv  (the focused deliverable)
  - writes docs/enrichment_summary.md          (coverage + gap stats)
Re-runnable; safe to run before all batches land (reports coverage so far).
"""
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def val(d, *keys):
    for k in keys:
        v = d.get(k)
        if v not in (None, "", "null", "N/A", "unknown", "Unknown"):
            return v
    return None


def main():
    enrich = {}
    files = sorted(glob.glob(str(ROOT / "census/enrich/pl_batch_*.json")))
    bad = []
    for f in files:
        try:
            recs = json.loads(Path(f).read_text())
        except Exception as e:
            bad.append((f, str(e)))
            continue
        for r in recs:
            cid = r.get("census_id")
            if cid:
                enrich[cid] = r

    master = json.loads((ROOT / "data/census_master.json").read_text())

    n_partner_parent = n_partner_spe = n_lender = n_year = 0
    for m in master:
        e = enrich.get(m.get("census_id"))
        if not e:
            continue
        spe = val(e, "private_partner_spe")
        parent = val(e, "private_partner_parent")
        lender = val(e, "lender")
        amt = val(e, "lender_loan_amount")
        yb = val(e, "year_built")
        m["private_partner_spe"] = spe
        m["private_partner_parent"] = parent
        m["private_partner_source"] = val(e, "private_partner_source")
        m["lender"] = lender
        m["lender_loan_amount"] = amt
        m["lender_source"] = val(e, "lender_source")
        m["lender_gap"] = e.get("lender_gap")
        if yb:
            m["year_built"] = yb
        m["year_built_source"] = val(e, "year_built_source")
        if spe:
            n_partner_spe += 1
        if parent:
            n_partner_parent += 1
        if lender:
            n_lender += 1
        if yb:
            n_year += 1

    (ROOT / "data/census_master.json").write_text(json.dumps(master, indent=2))

    cols = ["census_id", "name", "address", "city", "county", "sponsor", "tier",
            "private_partner_parent", "private_partner_spe", "private_partner_source",
            "lender", "lender_loan_amount", "lender_source", "lender_gap",
            "year_built", "year_built_source"]
    with open(ROOT / "data/partner_lender_yearbuilt.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for m in master:
            w.writerow([m.get(c) for c in cols])

    total = len(master)
    matched = sum(1 for m in master if m.get("census_id") in enrich)
    lines = [
        "# Partner / Lender / Year-Built Enrichment — Coverage\n",
        f"- Batches loaded: {len(files)} / 46" + (f"  (parse-failed: {len(bad)})" if bad else ""),
        f"- Master records: {total}; enriched (matched to a batch result): {matched}",
        f"- **Private partner (parent group) found:** {n_partner_parent}/{total} ({100*n_partner_parent//max(total,1)}%)",
        f"- **Private partner (seller SPE) found:** {n_partner_spe}/{total}",
        f"- **Lender found:** {n_lender}/{total} ({100*n_lender//max(total,1)}%)  — gaps expected (public-record only)",
        f"- **Year built (filled/verified):** {n_year}/{total}",
    ]
    if bad:
        lines.append("\n## Parse-failed batch files\n")
        for f, e in bad:
            lines.append(f"- {Path(f).name}: {e}")
    (ROOT / "docs/enrichment_summary.md").write_text("\n".join(lines) + "\n")

    print(f"batches={len(files)} matched={matched}/{total} "
          f"partner_parent={n_partner_parent} lender={n_lender} year={n_year}")
    if bad:
        print("PARSE-FAILED:", bad)


if __name__ == "__main__":
    main()
