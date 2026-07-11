#!/usr/bin/env python3
"""Consolidate all completed county census files into a master spreadsheet + summary.

Robust to whichever census/county_*.json files exist so far (re-run as more land).
Outputs:
  data/census_master.csv   — one flat row per property
  data/census_master.json  — merged records
  docs/census_summary.md    — running rollup + ranked Tier-1 target list
"""
import csv
import glob
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def g(d, *path, default=None):
    cur = d
    for k in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
    return cur if cur is not None else default


def flatten(r):
    lit = r.get("litigation_flags") or []
    gaps = r.get("gaps") or []
    # Flat records (small-bundle children) have no nested "property" object.
    if "property" not in r:
        return {
            "census_id": r.get("census_id"),
            "name": r.get("property_name"),
            "address": r.get("address"),
            "city": r.get("city"),
            "county": r.get("county"),
            "cad_account": r.get("cad_account"),
            "units": r.get("units"),
            "year_built": None,
            "sponsor": r.get("sponsor_verified") or r.get("owner_of_record_name"),
            "species": r.get("species"),
            "statute": {"HFC": "Ch.394", "PFC": "Ch.303", "HA": "Ch.392"}.get(r.get("species")),
            "tier": r.get("tier"),
            "traveling": r.get("traveling"),
            "in_target_set": r.get("tier") == 1,
            "appraised_value": r.get("appraised_value"),
            "first_exempt_year": r.get("first_exempt_tax_year"),
            "kill_regime": r.get("kill_regime"),
            "kill_date": r.get("kill_date_estimate"),
            "captured_9_1_2025": None,
            "recent_capital_event": None,
            "kill_basis": r.get("kill_date_basis"),
            "litigation": "; ".join(lit) if isinstance(lit, list) else str(lit),
            "confidence": "single-source" if r.get("seed_match") else "single-source",
            "gaps_n": len(gaps) if isinstance(gaps, list) else 0,
            "exemption_status": r.get("exemption_status"),
        }
    return {
        "census_id": r.get("census_id"),
        "name": g(r, "property", "name"),
        "address": g(r, "property", "address"),
        "city": g(r, "property", "city"),
        "county": g(r, "property", "county"),
        "cad_account": g(r, "property", "cad_account"),
        "units": g(r, "property", "units"),
        "year_built": g(r, "property", "year_built"),
        "sponsor": g(r, "sponsor", "name"),
        "species": g(r, "sponsor", "species"),
        "statute": g(r, "sponsor", "statute"),
        "tier": g(r, "classification", "tier"),
        "traveling": g(r, "classification", "traveling"),
        "in_target_set": g(r, "classification", "in_target_set"),
        "appraised_value": g(r, "exemption", "appraised_value"),
        "first_exempt_year": g(r, "exemption", "first_exempt_tax_year"),
        "kill_regime": g(r, "kill_analysis", "regime"),
        "kill_date": g(r, "kill_analysis", "kill_date_estimate"),
        "captured_9_1_2025": g(r, "kill_analysis", "captured_9_1_2025"),
        "recent_capital_event": g(r, "kill_analysis", "recent_capital_event"),
        "kill_basis": g(r, "kill_analysis", "kill_date_basis"),
        "litigation": "; ".join(lit) if isinstance(lit, list) else str(lit),
        "confidence": r.get("confidence"),
        "gaps_n": len(gaps) if isinstance(gaps, list) else 0,
        "exemption_status": r.get("exemption_status"),
    }


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    files = sorted(glob.glob(str(ROOT / "census/county_*.json")))
    rows = {}
    counties_loaded = []
    for f in files:
        try:
            recs = json.loads(Path(f).read_text())
        except Exception as e:
            print(f"SKIP {f}: {e}")
            continue
        counties_loaded.append(Path(f).stem.replace("county_", ""))
        for r in recs:
            fr = flatten(r)
            cid = fr["census_id"] or f"{Path(f).stem}-{len(rows)}"
            # keep the record with more non-null fields if duplicate id
            if cid in rows:
                old = sum(1 for v in rows[cid].values() if v not in (None, "", 0))
                new = sum(1 for v in fr.values() if v not in (None, "", 0))
                if new <= old:
                    continue
            rows[cid] = fr
    recs = list(rows.values())

    # master json (keep full records too)
    (ROOT / "data/census_master.json").write_text(json.dumps(recs, indent=2))

    cols = ["census_id", "name", "address", "city", "county", "cad_account", "units",
            "year_built", "sponsor", "species", "statute", "tier", "traveling",
            "in_target_set", "appraised_value", "exemption_status", "first_exempt_year",
            "kill_regime", "kill_date", "captured_9_1_2025", "recent_capital_event",
            "litigation", "confidence", "gaps_n", "kill_basis"]
    with open(ROOT / "data/census_master.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in recs:
            w.writerow([r.get(c) for c in cols])

    # ---- summary ----
    total_val = sum(fnum(r["appraised_value"]) or 0 for r in recs)
    by_county = defaultdict(lambda: [0, 0.0])
    by_tier = defaultdict(lambda: [0, 0.0])
    by_sponsor = defaultdict(lambda: [0, 0.0])
    with_acct = sum(1 for r in recs if r["cad_account"])
    expansions = sum(1 for r in recs if str(r["census_id"]).startswith("TX-NEW"))
    cap_events = [r for r in recs if r["recent_capital_event"]]
    for r in recs:
        v = fnum(r["appraised_value"]) or 0
        by_county[r["county"]][0] += 1; by_county[r["county"]][1] += v
        by_tier[r["tier"]][0] += 1; by_tier[r["tier"]][1] += v
        by_sponsor[r["sponsor"]][0] += 1; by_sponsor[r["sponsor"]][1] += v

    def money(x):
        return f"${x/1e9:.2f}B" if x >= 1e9 else f"${x/1e6:.1f}M"

    lines = []
    lines.append("# Census Master — Running Rollup (interim, unverified)\n")
    lines.append(f"*Consolidated from: {', '.join(counties_loaded)}. "
                 f"This is a live interim cut — the Opus verify pass and the remaining "
                 f"counties (incl. Harris) are not yet folded in.*\n")
    lines.append(f"- **Total property records:** {len(recs)}")
    lines.append(f"- **With a CAD account #:** {with_acct}")
    lines.append(f"- **Off-seed expansions (found beyond the Matrix list):** {expansions}")
    lines.append(f"- **Total appraised value captured:** {money(total_val)}")
    lines.append(f"- **Already-closed capital events (§13(e) early deaths):** {len(cap_events)}\n")

    lines.append("## By county\n\n| County | Records | Appraised value |\n|---|---|---|")
    for c, (n, v) in sorted(by_county.items(), key=lambda kv: -kv[1][1]):
        lines.append(f"| {c} | {n} | {money(v)} |")
    lines.append("")

    lines.append("## By tier\n\n| Tier | Records | Appraised value |\n|---|---|---|")
    tier_lbl = {1: "1 — HFC (2027 cliff)", 2: "2 — PFC (grandfathered)", 3: "3 — Housing authority"}
    for t, (n, v) in sorted(by_tier.items(), key=lambda kv: (kv[0] is None, kv[0])):
        lines.append(f"| {tier_lbl.get(t, t)} | {n} | {money(v)} |")
    lines.append("")

    lines.append("## By sponsor\n\n| Sponsor | Records | Appraised value |\n|---|---|---|")
    for s, (n, v) in sorted(by_sponsor.items(), key=lambda kv: -kv[1][1]):
        lines.append(f"| {s} | {n} | {money(v)} |")
    lines.append("")

    # ranked Tier-1 target list (top 25 by value)
    t1 = [r for r in recs if r["tier"] == 1 and fnum(r["appraised_value"])]
    t1.sort(key=lambda r: -(fnum(r["appraised_value"]) or 0))
    lines.append("## Top 25 Tier-1 targets by appraised value\n")
    lines.append("| Property | City | County | Sponsor | Appraised | Kill date | Flags |\n|---|---|---|---|---|---|---|")
    for r in t1[:25]:
        flags = []
        if r["recent_capital_event"]:
            flags.append("§13(e) sold")
        if r["litigation"]:
            flags.append("litigation")
        lines.append(f"| {r['name'] or '?'} | {r['city'] or ''} | {r['county'] or ''} | "
                     f"{(r['sponsor'] or '').replace(' Housing Finance Corporation','  HFC')} | "
                     f"{money(fnum(r['appraised_value']) or 0)} | {r['kill_date'] or ''} | {', '.join(flags)} |")
    (ROOT / "docs/census_summary.md").write_text("\n".join(lines) + "\n")

    print(f"records={len(recs)} counties={counties_loaded}")
    print(f"total_value={money(total_val)} with_acct={with_acct} expansions={expansions} cap_events={len(cap_events)}")


if __name__ == "__main__":
    main()
