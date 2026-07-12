#!/usr/bin/env python3
"""Fold the Travis/Tarrant unit-backfill results into data/census_master.json.
Fills `units` where it was null; also backfills `name` for previously-unnamed rows.
Re-runnable. Run after the units_batch_*.json land, then re-run export_csvs / build_excel / build_map.
"""
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
master = json.loads((ROOT / "data/census_master.json").read_text())
idx = {r["census_id"]: r for r in master}

BAD = {"none", "null", "unknown", "n/a", "", "(unnamed)"}
u_filled = n_filled = 0
for f in sorted(glob.glob(str(ROOT / "census/enrich/units_batch_*.json"))):
    try:
        recs = json.loads(Path(f).read_text())
    except Exception as e:
        print(f"SKIP {f}: {e}")
        continue
    for e in recs:
        r = idx.get(e.get("census_id"))
        if not r:
            continue
        units = e.get("units")
        if units and not r.get("units"):
            try:
                r["units"] = int(float(units))
                u_filled += 1
            except (TypeError, ValueError):
                pass
        rn = e.get("resolved_name")
        if rn and str(rn).strip().lower() not in BAD and (not r.get("name") or str(r.get("name")).strip().lower() in BAD):
            r["name"] = rn
            n_filled += 1

(ROOT / "data/census_master.json").write_text(json.dumps(master, indent=2))
print(f"units filled: {u_filled} | names backfilled: {n_filled}")
