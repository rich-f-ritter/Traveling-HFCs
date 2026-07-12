#!/usr/bin/env python3
"""Build a self-contained interactive Leaflet map of the filtered target set:
Tier-1 (faces the 1/1/2027 cliff), year built > 1990, units > 200.
Output: data/traveling_hfc_map.html  (open in any browser)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = json.loads((ROOT / "data/geocode_cache.json").read_text())


def as_int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


SPONSOR_COLORS = {
    "Pecos Housing Finance Corporation": "#e6194B",
    "Pleasanton Housing Finance Corporation": "#4363d8",
    "Cameron County Housing Finance Corporation": "#3cb44b",
    "La Villa Housing Finance Corporation": "#911eb4",
    "Edcouch Community Housing Finance Corporation": "#f58231",
    "Maverick County Housing Finance Corporation": "#800000",
    "Garland Housing Finance Corporation": "#009999",
}
DEFAULT_COLOR = "#666666"


def short_sponsor(s):
    return (s or "").replace(" Housing Finance Corporation", " HFC").replace(
        " Community HFC", " HFC")


def main():
    d = json.loads((ROOT / "data/census_master.json").read_text())
    pts = []
    for r in d:
        yb, u = as_int(r.get("year_built")), as_int(r.get("units"))
        if not (r.get("tier") == 1 and yb and yb > 1990 and u and u > 200 and r.get("address")):
            continue
        gc = CACHE.get(r["census_id"])
        if not gc or not gc.get("lat"):
            continue
        av = r.get("appraised_value")
        pts.append({
            "id": r["census_id"],
            "name": (r.get("name") or "(unnamed)").title() if (r.get("name") or "").isupper() else (r.get("name") or "(unnamed)"),
            "addr": r.get("address"),
            "city": r.get("city"),
            "county": r.get("county"),
            "yb": yb, "units": u,
            "owner": r.get("owner_group") or "—",
            "sponsor": short_sponsor(r.get("sponsor")),
            "sponsor_full": r.get("sponsor"),
            "kill": r.get("kill_date") or "1/1/2027",
            "exempt": r.get("exemption_status") or "—",
            "av": round(av) if isinstance(av, (int, float)) else None,
            "lat": gc["lat"], "lon": gc["lon"],
            "color": SPONSOR_COLORS.get(r.get("sponsor"), DEFAULT_COLOR),
            "approx": gc.get("source") == "city-centroid",
        })
    pts.sort(key=lambda p: -(p["av"] or 0))

    # legend entries (only sponsors present)
    present = {}
    for p in pts:
        present[p["sponsor_full"]] = p["color"]
    legend_rows = "".join(
        f'<div class="lg"><span class="dot" style="background:{c}"></span>{short_sponsor(s)}</div>'
        for s, c in sorted(present.items(), key=lambda kv: short_sponsor(kv[0])))

    data_js = json.dumps(pts)
    total_av = sum(p["av"] or 0 for p in pts)
    html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Traveling HFC Target Map</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  html,body{{margin:0;height:100%;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
  #map{{position:absolute;top:0;bottom:0;left:0;right:0}}
  .banner{{position:absolute;top:10px;left:50px;z-index:1000;background:rgba(20,28,45,.92);color:#fff;
    padding:8px 14px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.3);max-width:60%}}
  .banner h1{{margin:0;font-size:15px}}
  .banner p{{margin:2px 0 0;font-size:11.5px;opacity:.85}}
  .legend{{position:absolute;bottom:22px;right:12px;z-index:1000;background:rgba(255,255,255,.95);
    padding:8px 10px;border-radius:8px;font-size:12px;box-shadow:0 2px 8px rgba(0,0,0,.3);max-height:45%;overflow:auto}}
  .legend b{{display:block;margin-bottom:4px;font-size:11px;text-transform:uppercase;letter-spacing:.03em;color:#333}}
  .lg{{display:flex;align-items:center;margin:2px 0;color:#222}}
  .dot{{width:11px;height:11px;border-radius:50%;display:inline-block;margin-right:6px;border:1px solid #333}}
  .leaflet-popup-content{{font-size:12.5px;line-height:1.45;margin:10px 12px}}
  .leaflet-popup-content .pn{{font-weight:700;font-size:14px}}
  .leaflet-popup-content table{{margin-top:5px;border-collapse:collapse}}
  .leaflet-popup-content td{{padding:1px 6px 1px 0;vertical-align:top}}
  .leaflet-popup-content td.k{{color:#666;white-space:nowrap}}
  .appx{{color:#b26a00;font-size:11px}}
</style></head><body>
<div id="map"></div>
<div class="banner"><h1>Traveling HFC deals — 2027 cliff, built &gt;1990, &gt;200 units</h1>
<p>{len(pts)} properties · ${total_av/1e9:.2f}B appraised · colored by sponsoring HFC · click a marker for details</p></div>
<div class="legend"><b>Sponsoring HFC</b>{legend_rows}</div>
<script>
var pts = {data_js};
var imagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}',{{maxZoom:19,attribution:'Imagery &copy; Esri'}});
var labels = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{{z}}/{{y}}/{{x}}',{{maxZoom:19}});
var roads = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{{z}}/{{y}}/{{x}}',{{maxZoom:19}});
var satellite = L.layerGroup([imagery, roads, labels]);
var streets = L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png',{{maxZoom:20,attribution:'&copy; OpenStreetMap, &copy; CARTO'}});
var map = L.map('map',{{layers:[satellite]}});
L.control.layers({{'Satellite':satellite,'Streets':streets}}).addTo(map);
function money(v){{return v==null?'—':'$'+v.toLocaleString();}}
var group=[];
pts.forEach(function(p){{
  var m=L.circleMarker([p.lat,p.lon],{{radius:7,color:'#111',weight:1,fillColor:p.color,fillOpacity:.9}});
  var html='<div class="pn">'+p.name+'</div>'+
    '<div>'+(p.addr||'')+(p.city?', '+p.city:'')+' '+(p.county?'('+p.county+' Co.)':'')+'</div>'+
    (p.approx?'<div class="appx">⚠ location approximate (city centroid)</div>':'')+
    '<table>'+
    '<tr><td class="k">Year built</td><td>'+p.yb+'</td></tr>'+
    '<tr><td class="k">Units</td><td>'+p.units+'</td></tr>'+
    '<tr><td class="k">Private partner — owner</td><td>'+p.owner+'</td></tr>'+
    '<tr><td class="k">Sponsor (HFC)</td><td>'+p.sponsor+'</td></tr>'+
    '<tr><td class="k">Kill date</td><td>'+p.kill+'</td></tr>'+
    '<tr><td class="k">Exemption status</td><td>'+p.exempt+'</td></tr>'+
    '<tr><td class="k">Appraised value</td><td>'+money(p.av)+'</td></tr>'+
    '<tr><td class="k">Census ID</td><td>'+p.id+'</td></tr>'+
    '</table>';
  m.bindPopup(html,{{maxWidth:320}});
  m.bindTooltip(p.name,{{direction:'top'}});
  m.addTo(map); group.push(m);
}});
map.fitBounds(L.featureGroup(group).getBounds().pad(0.08));
</script></body></html>"""
    out = ROOT / "data/traveling_hfc_map.html"
    out.write_text(html)
    print(f"wrote {out} — {len(pts)} points, ${total_av/1e9:.2f}B appraised")


if __name__ == "__main__":
    main()
