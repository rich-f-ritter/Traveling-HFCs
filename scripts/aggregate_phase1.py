#!/usr/bin/env python3
"""Phase 1 aggregation — fold the 7 verified sponsor profiles back into the data.

- Rewrites data/sponsors.json with VERIFIED classifications (species, statute, tier,
  kill-regime, affiliated PFC, litigation, confidence).
- Re-tiers every property (the big change: Pecos 'Housing Authority' rows are actually
  Pecos Housing Finance Corporation, Ch.394 HFC -> Tier 1).
- Recomputes a first-order `traveling` flag using the correct jurisdictional test
  (city boundary for city sponsors, county for county sponsors) instead of the naive
  county-equality heuristic. Flags where a Phase-3 geocode (city+5mi, Sec.392.014) is needed.
"""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Verified sponsor classifications, keyed by the seed's PHA-owner name.
# level: 'city' | 'county' | 'district' -> chooses the traveling test.
CORRECTED = {
    "Pleasanton Housing Finance Corporation": dict(
        entity="Pleasanton Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Pleasanton", home_county="Atascosa", level="city", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i) 1/1/2027 + §13(e) capital-event; multiple injunctions already STAND (Lake Worth, Arlington, Fort Worth, Missouri City — appeals abandoned); Hays CAD TRO",
        litigation=["15-25-00110/-00111-CV (appeals abandoned; TIs stand)", "Hays Co. 25-1185-DCB TRO", "AG RQ-0566-KP pending"],
        note="Archetype traveling HFC; ~68+ properties reported (seed 58 is a floor)."),
    "Cameron County Housing Finance Corporation, The": dict(
        entity="Cameron County Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Harlingen", home_county="Cameron", level="county", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i)/§13(e)",
        litigation=["Williamson County v. Cameron County HFC (TRO)", "Bexar AD suit (27 complexes/$26M)", "TWHC HB21 constitutional challenge (Cameron Co., 9/9/2025)"],
        note="FIX: seed listed home city 'San Benito' — that is the Housing AUTHORITY's town. Distinct from Cameron County Housing Authority (Ch.392)."),
    "La Villa Housing Finance Corporation": dict(
        entity="La Villa Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="La Villa", home_county="Hidalgo", level="city", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i)/§13(e)",
        litigation=["Fort Worth temporary-order effort (13 props/$3.2M)", "Bexar AD suit", "TWHC coalition"],
        note="City of ~1,300; developer-driven; shared TWHC/Chasnoff-Stribling defense."),
    "Edcouch Community Housing Finance Corporation": dict(
        entity="Edcouch Community Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Edcouch", home_county="Hidalgo", level="city", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i)/§13(e)",
        litigation=["Bexar AD suit", "TWHC coalition"],
        note="Mixed actor — also runs in-Edcouch LIHTC rehabs (out of scope); only traveling deals in scope."),
    "Maverick County Housing Finance Corporation": dict(
        entity="Maverick County Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Eagle Pass", home_county="Maverick", level="county", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i)/§13(e); post-5/28/2025 acquisitions BARRED outright by §394.031(c)-(d)",
        litigation=["Missouri City v. Maverick County HFC (Fort Bend 268th, TRO)", "Fort Worth effort", "Bexar AD suit", "TWHC coalition"],
        note="Chartered 6/24/2024 — deals straddle the 5/28/2025 line; date each for §13(i) vs outright bar."),
    "Garland Housing Finance Corporation": dict(
        entity="Garland Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Garland", home_county="Dallas", level="city", tier=1, faces_2027_cliff=True,
        affiliated_pfc=None, confidence="high",
        kill_regime="HB21 §13(i)/§13(e)",
        litigation=["Collin CAD v. GHFC 05-19-01417-CV (GHFC won pre-HB21; now overridden by §13(i))"],
        note="Long-standing municipal HFC; all 4 seed properties out-of-city (incl. Carrollton). Seed count is a floor."),
    "Pecos Housing Authority": dict(
        entity="Pecos Housing Finance Corporation", species="HFC", statute="Ch.394",
        home_city="Pecos", home_county="Reeves", level="city", tier=1, faces_2027_cliff=True,
        affiliated_pfc="Sister entity: Pecos Housing Authority (Ch.392) — shares board + ED John Salcido; deals run through the Ch.394 HFC",
        confidence="high",
        kill_regime="HB21 §13(i) 1/1/2027 + §13(e); Haltom City injunction (6/3/2025); Arlington TRO; Tarrant ARB 5-yr back-assessment ($974M/28 sites); AG RQ-0566/0587-KP retroactive theory",
        litigation=["Haltom City v. Pecos HFC (injunction 6/3/2025)", "Arlington 15-25-00111-CV", "Hays Co. (~$230M)", "Tarrant ARB $974M/28 sites", "TWHC HB21 challenge"],
        note="RECLASSIFIED: seed label 'Pecos Housing Authority' is a MISLABEL — appraisal-district owner records show Pecos Housing FINANCE Corporation (Ch.394 HFC). Moves 126 properties Tier 3 -> Tier 1."),
    "Texas Essential Housing Public Facility Corporation": dict(
        entity="Texas Essential Housing Public Facility Corporation", species="PFC", statute="Ch.303",
        home_city="Austin (SH130 corridor)", home_county="Travis", level="district", tier=2, faces_2027_cliff=False,
        affiliated_pfc="Is itself the PFC; sponsored by SH130 Municipal Management District No.1",
        confidence="high",
        kill_regime="NO 2027 cliff (HB21 is HFC-only). Event-driven: contract/99-yr term, capital event, §303.0426 audit failure, CAD/AG challenge (KP-0437). ~12 post-6/18/2023 deals carry boundary/grandfather risk (§303.021(d))",
        litigation=["TEHPFC v. Williamson CAD 24-0022-C395 & 24-1698-C395", "AG KP-0437", "SB 2434 (dissolution) died 88R"],
        note="Sponsor is a special district in Austin's ETJ; all 29 travel statewide. Separate non-cliff tier."),
    "Houston Housing Authority": dict(
        entity="Houston Housing Authority", species="HA", statute="Ch.392",
        home_city="Houston", home_county="Harris", level="county", tier=3, faces_2027_cliff=False,
        affiliated_pfc="HHA-sponsored Ch.303 PFC exists; but seed rows show HHA as direct fee/ground-lessor (§392.005)",
        confidence="med",
        kill_regime="NO statutory cliff — HB21/HB2071 don't reach Ch.392 §392.005 (no geographic self-destruct). Exposure: ultra vires challenge (+5-yr back-assessment §11.43(i)); §392.005(c) affordability condition (6/18/2023); voluntary halt of new deals",
        litigation=["No tax-structure litigation found (political/journalistic pressure drove 2025 halt)"],
        note="MOSTLY LOCAL: ~15 of 19 are Harris-County home-turf (drop out); ~4 traveling (Fort Bend/Montgomery). Analysts flag Ch.392 as 'least regulated' — a growing structure."),
    "Cameron County Housing Authority": dict(
        entity="Cameron County Housing Authority", species="HA", statute="Ch.392",
        home_city="San Benito/Brownsville", home_county="Cameron", level="county", tier=3, faces_2027_cliff=False,
        affiliated_pfc=None, confidence="low",
        kill_regime="If genuinely HA (Ch.392): no cliff, but strongest ultra vires posture (300+ mi out-of-area). If any row is actually the Ch.394 Cameron County HFC sibling: HB21 §13(i) 2027 cliff (Tier 1)",
        litigation=["Distinguish from Williamson County v. Cameron County HFC (that's the HFC sibling)"],
        note="ENTITY-IDENTITY GAP: all 4 rows traveling, but deed-level confirmation needed — HA (Ch.392) vs Cameron County HFC (Ch.394). Decides tier + cliff. Priority Phase-3 verification."),
    "Rosenberg Housing Authority": dict(
        entity="Rosenberg Housing Authority", species="HA", statute="Ch.392",
        home_city="Rosenberg", home_county="Fort Bend", level="city", tier=3, faces_2027_cliff=False,
        affiliated_pfc="Rosenberg Housing Authority Public Facility Corporation (RHAPFC, Ch.303, created 5/2021)",
        confidence="med",
        kill_regime="HB2071 (Ch.303 via RHAPFC); no 2027 cliff. Pre-2023 deals grandfathered but out-of-area; 2025-26 acquisitions post-HB2071 -> §303.021(d) may bar out-of-area PFC ownership -> exemption arguably invalid from inception (back-assessable)",
        litigation=["Fort Bend PFC deals criticized in local press; statewide PFC/AG scrutiny"],
        note="Municipal area of operation = city+5mi (§392.014); Sugar Land/Stafford deals are out-of-area."),
    "San Benito Housing Authority": dict(
        entity="San Benito Housing Authority", species="HA", statute="Ch.392",
        home_city="San Benito", home_county="Cameron", level="city", tier=3, faces_2027_cliff=False,
        affiliated_pfc=None, confidence="low",
        kill_regime="No cliff (not an HFC). Seed deal in McAllen (Hidalgo, ~40mi/1 county out); if via PFC -> HB2071 §303.021(d) bar; if direct HA -> needs McAllen+Hidalgo cooperation resolutions. Legally dubious either way",
        litigation=[],
        note="Seed property is 'Prospective' — confirm whether it closed at all; no recorded deal/exemption found. Distinguish from Cameron County HA/HFC."),
    "Plano Housing Authority": dict(
        entity="Plano Housing Authority", species="HA", statute="Ch.392",
        home_city="Plano", home_county="Collin", level="city", tier=3, faces_2027_cliff=False,
        affiliated_pfc="Plano Public Facility Corporation (Ch.303)",
        confidence="high",
        kill_regime="HB2071 (Ch.303 via Plano PFC); no 2027 cliff. Oak Tree Village grandfathered (pre-2023). Real early-unwind vector is active litigation, not a statutory cliff",
        litigation=["City of Plano + Plano ISD v. Plano HA & its PFCs (Collin Co. 219-03003-2024) — constitutional PFC ad valorem challenge"],
        note="Seed's single property (Lewisville) is the lone traveling deal of Plano PFC's ~14 (rest Plano-local)."),
}

# Houston HA is a municipal authority but its home county Harris is the practical
# area-of-operation proxy, so it uses the county test (Harris = local).


def is_traveling(sponsor_meta, prop_city, prop_county):
    level = sponsor_meta["level"]
    if level == "district":
        return "yes"  # tiny special district; all statewide
    if level == "county":
        hc = sponsor_meta["home_county"]
        if hc and prop_county:
            return "yes" if hc.lower() != prop_county.lower() else "no"
        return "unknown"
    # city-level sponsor: test property city vs home city (first-order proxy for
    # city / city+5mi jurisdiction). Phase-3 geocode refines the +5mi boundary.
    hcity = sponsor_meta["home_city"]
    if hcity and prop_city:
        # split on '/' for multi-name home cities
        homes = [h.strip().lower() for h in hcity.replace("(", "/").split("/")]
        return "no" if prop_city.strip().lower() in homes else "yes"
    return "unknown"


def main():
    records = json.loads((ROOT / "data/seed_properties.json").read_text())

    for rec in records:
        m = CORRECTED[rec["sponsor"]]
        rec["sponsor_entity_verified"] = m["entity"]
        rec["sponsor_species"] = m["species"]
        rec["sponsor_statute"] = m["statute"]
        rec["tier"] = m["tier"]
        rec["faces_2027_cliff"] = m["faces_2027_cliff"]
        rec["sponsor_home_county"] = m["home_county"]
        rec["sponsor_home_city"] = m["home_city"]
        rec["traveling"] = is_traveling(m, rec.get("property_city"), rec.get("property_county"))
        rec["classification_confidence"] = m["confidence"]

    (ROOT / "data/seed_properties.json").write_text(json.dumps(records, indent=2))

    # sponsors.json (verified)
    counts = Counter(r["sponsor"] for r in records)
    trav = Counter(r["sponsor"] for r in records if r["traveling"] == "yes")
    sponsors_out = []
    for name, m in CORRECTED.items():
        sponsors_out.append({
            "seed_name": name, "verified_entity": m["entity"], "species": m["species"],
            "statute": m["statute"], "tier": m["tier"], "faces_2027_cliff": m["faces_2027_cliff"],
            "home_city": m["home_city"], "home_county": m["home_county"], "level": m["level"],
            "affiliated_pfc": m["affiliated_pfc"], "kill_regime": m["kill_regime"],
            "litigation": m["litigation"], "confidence": m["confidence"], "note": m["note"],
            "property_count": counts.get(name, 0), "traveling_count": trav.get(name, 0),
            "classification_status": "PHASE1_VERIFIED",
        })
    (ROOT / "data/sponsors.json").write_text(json.dumps(sponsors_out, indent=2))

    # CSV refresh
    csv_cols = ["census_id", "sponsor", "sponsor_entity_verified", "sponsor_species",
                "sponsor_statute", "tier", "faces_2027_cliff", "traveling", "role",
                "sponsor_home_city", "sponsor_home_county", "property_city", "property_county",
                "status", "affordable", "classification_confidence", "sale_date"]
    with open(ROOT / "data/seed_properties.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(csv_cols)
        for rec in records:
            w.writerow([rec.get(c) for c in csv_cols])

    # ---- summary ----
    print("=== REVISED TIERS ===")
    print("by tier:", dict(sorted(Counter(r["tier"] for r in records).items())))
    print("by species:", dict(Counter(r["sponsor_species"] for r in records)))
    print("faces 2027 cliff:", dict(Counter(r["faces_2027_cliff"] for r in records)))
    print("traveling:", dict(Counter(r["traveling"] for r in records)))
    print()
    print("=== Tier 1 (HFC, 2027 cliff) traveling & cliff ===")
    t1 = [r for r in records if r["tier"] == 1]
    print(f"  Tier1 total={len(t1)}, traveling={sum(1 for r in t1 if r['traveling']=='yes')}")
    print()
    print("=== Per-sponsor (tier | cliff | count | traveling) ===")
    for s in sponsors_out:
        print(f"  T{s['tier']} cliff={str(s['faces_2027_cliff']):5} {s['property_count']:3d} trav={s['traveling_count']:3d}  {s['verified_entity']}")


if __name__ == "__main__":
    main()
