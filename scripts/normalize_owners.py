#!/usr/bin/env python3
"""Normalize the free-text private_partner_parent field into a clean `owner_group`.

Adds `owner_group` to every record in data/census_master.json (keeps the raw
private_partner_parent for audit). Run AFTER merge_enrichment.py.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "data/census_master.json"

# Leading hedge phrases to drop.
HEDGES = ["unconfirmed, probable ", "unconfirmed but probable ", "likely ", "probable ",
          "probably ", "uncertain ", "possible ", "possibly "]

# Strings (lowercased, after programmatic canon) that mean "no named firm" -> blank.
BLANKISH = ("unconfirmed", "unidentified", "unknown", "none", "n/a", "no free source",
            "not asserted", "not identified", "see notes", "see lender")

# Alias map: canonical display name -> variants (matched on lowercased canon key).
ALIASES = {
    "The Lynd Company": ["lynd acquisitions group", "lynd group", "lynd company", "lynd living", "lynd"],
    "Knightvest Residential": ["knightvest residential", "knightvest capital", "knightvest"],
    "Post Investment Group": ["post investment group", "post real estate group"],
    "S2 Capital": ["s2 capital"],
    "Tides Equities": ["tides equities"],
    "Ashland Greene Capital": ["ashland greene capital", "ashland greene"],
    "Sphinx Development Corporation": ["sphinx development corporation", "sphinx development", "the sphinx group"],
    "Cottonwood Group": ["cottonwood group", "cottonwood management"],
    "Sahara Equity": ["sahara equity"],
    "Strategic Realty Holdings": ["strategic realty holdings"],
    "Pennybacker Capital": ["pennybacker capital"],
    "Magma Equities": ["magma equities"],
    "Nitya Capital": ["nitya capital"],
    "WindMass Capital": ["windmass capital"],
    "Cienda Partners": ["cienda partners"],
    "Polaris Real Estate Partners": ["polaris real estate partners"],
    "REEP Equity": ["reep equity"],
    "ShainRealty Capital": ["shainrealty capital"],
    "TTI Capital": ["tti capital"],
    "Presidium": ["presidium"],
    "GVA": ["gva"],
    "Dalian Development": ["dalian development", "dalian"],
    "Equity Partnership Holdings": ["equity partnership holdings", "eph"],
    "MC Companies": ["mc companies", "mc cos", "mc"],
    "Madera Companies": ["madera companies", "madera residential", "madera"],
    "Landmark Companies": ["landmark companies", "landmark cos", "landmark"],
    "Trammell Crow Residential": ["trammell crow residential", "high street residential"],
}


def _cut(s):
    """Cut at the earliest descriptor delimiter."""
    delims = [" -- ", " — ", " – ", " (", "(", ";", ",", " / ", " dba ", " in joint venture",
              " in partnership", " in a joint", " itself"]
    idx = len(s)
    for d in delims:
        i = s.find(d)
        if i != -1:
            idx = min(idx, i)
    return s[:idx]


def canon(s):
    if not s:
        return ""
    s = s.strip()
    low = s.lower()
    for h in HEDGES:
        if low.startswith(h):
            s = s[len(h):].strip()
            low = s.lower()
    if any(low.startswith(b) for b in BLANKISH):
        return ""
    s = _cut(s).strip().strip(".").strip()
    s = re.sub(r"\s+(LLC|L\.L\.C\.|Inc\.?|Corp\.?|Ltd\.?|LP|L\.P\.)$", "", s, flags=re.I).strip()
    if not s or s.lower() in BLANKISH or len(s) <= 1:
        return ""
    # alias merge
    kl = s.lower()
    for canonical, variants in ALIASES.items():
        if kl in variants:
            return canonical
    return s


def main():
    data = json.loads(MASTER.read_text())
    for r in data:
        r["owner_group"] = canon(r.get("private_partner_parent"))
    MASTER.write_text(json.dumps(data, indent=2))

    c = Counter(r["owner_group"] for r in data if r["owner_group"])
    blank = sum(1 for r in data if not r["owner_group"])
    print(f"records: {len(data)} | distinct owners: {len(c)} | with owner: {sum(c.values())} | blank/unidentified: {blank}")
    print("--- top owners ---")
    for name, n in c.most_common(40):
        print(f"{n:3d}  {name}")


if __name__ == "__main__":
    main()
