#!/usr/bin/env python3
"""Geocode the map's filtered property set (tier 1, year>1990, units>200).
Uses the US Census geocoder (address -> lat/lon), Nominatim as fallback, and a
city-centroid last resort (flagged approximate). Caches to data/geocode_cache.json.
"""
import json
import os
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CA = "/root/.ccr/ca-bundle.crt"
VERIFY = CA if os.path.exists(CA) else True
CACHE = ROOT / "data/geocode_cache.json"


def as_int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def filtered():
    d = json.loads((ROOT / "data/census_master.json").read_text())
    out = []
    for r in d:
        yb, u = as_int(r.get("year_built")), as_int(r.get("units"))
        if r.get("tier") == 1 and yb and yb > 1990 and u and u > 200 and r.get("address"):
            out.append(r)
    return out


def census(q):
    r = requests.get("https://geocoding.geo.census.gov/geocoder/locations/onelineaddress",
                     params={"address": q, "benchmark": "Public_AR_Current", "format": "json"},
                     timeout=30, verify=VERIFY)
    m = r.json().get("result", {}).get("addressMatches", [])
    if m:
        c = m[0]["coordinates"]
        return c["y"], c["x"], m[0]["matchedAddress"]
    return None


def nominatim(q):
    r = requests.get("https://nominatim.openstreetmap.org/search",
                     params={"q": q, "format": "json", "limit": 1, "countrycodes": "us"},
                     headers={"User-Agent": "traveling-hfc-census/1.0"}, timeout=30, verify=VERIFY)
    j = r.json()
    if j:
        return float(j[0]["lat"]), float(j[0]["lon"]), j[0].get("display_name", "")
    return None


def main():
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    rows = filtered()
    print(f"geocoding {len(rows)} filtered properties")
    exact = approx = fail = 0
    for r in rows:
        cid = r["census_id"]
        if cid in cache and cache[cid].get("lat"):
            (exact if cache[cid]["source"] != "city-centroid" else approx).__int__  # no-op
            continue
        addr = f"{r['address']}, {r['city']}, TX"
        res, src = None, None
        try:
            res = census(addr); src = "census"
        except Exception:
            pass
        if not res:
            try:
                time.sleep(1); res = nominatim(addr); src = "nominatim"
            except Exception:
                pass
        if not res:  # city centroid fallback (approximate)
            try:
                res = census(f"{r['city']}, TX"); src = "city-centroid"
            except Exception:
                pass
        if res:
            cache[cid] = {"lat": res[0], "lon": res[1], "source": src, "matched": res[2]}
            if src == "city-centroid":
                approx += 1
            else:
                exact += 1
        else:
            cache[cid] = {"lat": None, "lon": None, "source": "FAILED", "matched": None}
            fail += 1
        CACHE.write_text(json.dumps(cache, indent=1))
    # recount from cache for the current filtered set
    exact = sum(1 for r in rows if cache[r["census_id"]]["source"] in ("census", "nominatim"))
    approx = sum(1 for r in rows if cache[r["census_id"]]["source"] == "city-centroid")
    fail = sum(1 for r in rows if cache[r["census_id"]]["source"] == "FAILED")
    print(f"exact: {exact} | approx (city centroid): {approx} | failed: {fail}")


if __name__ == "__main__":
    main()
