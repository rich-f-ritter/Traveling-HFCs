#!/usr/bin/env python3
"""Build a single clean IC-style slide (Milestone deck format):
Top-30 private owners of HFC deals (table) + metro geography + institutional-target funnel.
Output: data/ownership_geography_slide.html  (1280x960, print-ready)
Target set = HFC (Ch.394) property built >=1990 AND >=200 units.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
d = json.loads((ROOT / "data/census_master.json").read_text())


def i(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


METRO = {}
for c in ["Dallas", "Tarrant", "Collin", "Denton", "Rockwall", "Johnson", "Wise"]:
    METRO[c] = "DFW"
for c in ["Harris", "Fort Bend", "Montgomery", "Galveston", "Brazoria"]:
    METRO[c] = "Houston"
for c in ["Travis", "Williamson", "Hays"]:
    METRO[c] = "Austin"
for c in ["Bexar", "Comal"]:
    METRO[c] = "San Antonio"

t1 = [r for r in d if r.get("tier") == 1]  # HFC / Ch.394


def is90(r):
    return (i(r.get("year_built")) or 0) >= 1990


def is200(r):
    return (i(r.get("units")) or 0) >= 200


def tgt(r):
    return is90(r) and is200(r)


def short(n):
    return (n.replace(" Corporation", "").replace(" Companies", "")
             .replace(" Real Estate Partners", " RE Partners")
             .replace(" Investment Group", " Investment Grp")
             .replace(" Capital Management", " Capital Mgmt"))


# ---- owners ----
own_tot = Counter(r.get("owner_group") for r in t1 if r.get("owner_group"))
own_tgt = Counter(r.get("owner_group") for r in t1 if r.get("owner_group") and tgt(r))
TOPN = 30
owners = [(short(n), c, own_tgt.get(n, 0)) for n, c in own_tot.most_common(TOPN)]
identified = sum(own_tot.values())
unidentified = sum(1 for r in t1 if not r.get("owner_group"))
top_sum = sum(c for _, c, _ in owners)

# ---- metros ----
order = ["DFW", "Houston", "Austin", "San Antonio", "Other"]
m = defaultdict(lambda: [0, 0, 0])   # all, >=1990, target
for r in t1:
    mm = METRO.get(r.get("county"), "Other")
    m[mm][0] += 1
    if is90(r):
        m[mm][1] += 1
    if tgt(r):
        m[mm][2] += 1

# ---- funnel ----
F_ALL = len(t1)
F_90 = sum(1 for r in t1 if is90(r))
F_TGT = sum(1 for r in t1 if tgt(r))

# ---- takeaways ----
dfwhou_tgt = m["DFW"][2] + m["Houston"][2]
top4 = sum(c for _, c, _ in owners[:4])
s2c, tds = own_tot.get("S2 Capital", 0), own_tot.get("Tides Equities", 0)
s2t, tdt = own_tgt.get("S2 Capital", 0), own_tgt.get("Tides Equities", 0)

# ---- owner table split into two side-by-side columns ----
half = (TOPN + 1) // 2
left_owners, right_owners = owners[:half], owners[half:]


def orow(rank, name, tot, tg):
    tgc = f'<td class="num gold">{tg}</td>' if tg else '<td class="num zero">&mdash;</td>'
    return (f'<tr><td class="rk">{rank}</td><td class="own">{name}</td>'
            f'<td class="num">{tot}</td>{tgc}</tr>')


def otable(rows, start):
    body = "".join(orow(start + j + 1, n, t, g) for j, (n, t, g) in enumerate(rows))
    return ('<table class="t"><colgroup><col style="width:24px"><col><col style="width:40px">'
            '<col style="width:46px"></colgroup>'
            '<thead><tr><th></th><th>Owner</th><th class="num">HFC</th>'
            '<th class="num">Tgt*</th></tr></thead><tbody>' + body + '</tbody></table>')


owner_block = (f'<div class="ocol">{otable(left_owners, 0)}</div>'
               f'<div class="ocol">{otable(right_owners, half)}</div>')

# ---- metro table ----
metro_body = ""
for mm in order:
    a, nine, t = m[mm]
    metro_body += (f'<tr><td class="own">{mm}</td><td class="num">{a}</td>'
                   f'<td class="num">{nine}</td><td class="num gold">{t}</td></tr>')
metro_body += (f'<tr class="tot"><td class="own">All metros</td><td class="num">{F_ALL}</td>'
               f'<td class="num">{F_90}</td><td class="num gold">{F_TGT}</td></tr>')

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Traveling-HFC Census — Ownership &amp; Geography</title>
<style>*{{box-sizing:border-box}}html,body{{margin:0;padding:0}}
:root{{--navy:#074070;--navy-ink:#1A2B3C;--blue:#589BD5;--gold:#B49955;--gray:#6F6F70;
--body:#404040;--panel:#EEF1F6;--divider:#D9D9D9;--pale:#C7D6E6;
--serif:Cambria,Georgia,"Times New Roman",serif;--sans:Calibri,Carlito,"Segoe UI",Arial,sans-serif;
--mono:Consolas,"Cascadia Code",Menlo,monospace;}}
body{{background:#cfd6dd;color:var(--body);font-family:var(--sans);-webkit-font-smoothing:antialiased;}}
.deck{{display:flex;flex-direction:column;align-items:center;padding:26px 12px;}}
.page{{width:1280px;height:960px;background:#fff;border:1px solid #b9c2cb;
box-shadow:0 2px 6px rgba(20,40,60,.12),0 14px 40px -18px rgba(20,40,60,.35);
padding:30px 44px 16px;display:flex;flex-direction:column;overflow:hidden;}}
@media print{{body{{background:#fff}}.deck{{padding:0}}.page{{border:none;box-shadow:none}}
@page{{size:1280px 960px}}*{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
.topbar{{display:flex;justify-content:space-between;align-items:baseline;}}
.kicker{{font-size:12.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--blue);font-weight:600;}}
.pageno{{font-size:11.5px;letter-spacing:.22em;color:var(--gray);text-transform:uppercase;}}
h1{{font-family:var(--serif);font-weight:700;font-size:26px;line-height:1.12;color:var(--navy-ink);margin:9px 0 0;letter-spacing:-.005em;}}
.bar{{width:130px;height:4px;background:var(--navy);margin:8px 0 8px;}}
.insight{{font-size:14.5px;line-height:1.48;color:var(--body);max-width:1192px;margin:0;}}
.insight b{{color:var(--navy);}}
.cols{{display:flex;gap:30px;flex:1;min-height:0;margin-top:14px;}}
.sec{{font-size:13.5px;font-weight:700;color:var(--navy);letter-spacing:.02em;margin:0 0 8px;
padding-bottom:5px;border-bottom:1.5px solid var(--divider);}}
table.t{{width:100%;border-collapse:collapse;font-size:11.8px;table-layout:fixed;color:var(--body);}}
table.t th{{font-size:9.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--navy);
text-align:left;padding:6px 8px;border-bottom:2px solid var(--navy);background:#DCE6F1;font-weight:700;}}
table.t td{{padding:9.5px 8px;border-bottom:1px solid #EAEDF1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
table.t tbody tr:nth-child(even) td{{background:#F6F8FB;}}
table.t td.rk{{color:var(--gray);font-family:var(--mono);font-size:10px;text-align:right;padding-right:3px;}}
table.t td.own{{font-weight:600;color:var(--navy-ink);}}
table.t .num{{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums;font-weight:700;color:var(--navy-ink);}}
table.t td.gold{{color:var(--gold);}}
table.t td.zero{{color:#C9CDD3;font-weight:400;}}
table.t tr.tot td{{background:#DCE6F1!important;border-top:2px solid var(--navy);font-weight:700;color:var(--navy);}}
.ocols{{display:flex;gap:22px;}}
.ocol{{flex:1;min-width:0;}}
.onote{{font-size:10px;color:var(--gray);font-style:italic;margin:9px 0 0;line-height:1.4;}}
.funnel{{background:var(--panel);border:1px solid var(--divider);border-left:4px solid var(--navy);
padding:11px 14px;margin-top:16px;}}
.funnel .ft{{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:6px;}}
.frow{{display:flex;align-items:center;margin:9px 0;}}
.ftrk{{flex:1;display:flex;align-items:center;}}
.fbar{{height:22px;border-radius:0 3px 3px 0;}}
.fbar.pale{{background:var(--pale);}}.fbar.blue{{background:var(--blue);}}.fbar.gold{{background:var(--gold);}}
.fnum{{width:70px;text-align:right;font-family:var(--mono);font-size:17px;font-weight:700;color:var(--navy-ink);padding:0 9px;}}
.fnum .fpct{{display:block;font-size:9.5px;color:var(--gray);font-weight:400;}}
.flab{{width:150px;font-size:11.5px;color:var(--body);}}
.take{{margin-top:16px;}}
.take .ft{{font-size:13px;font-weight:700;color:var(--navy);border-bottom:1.5px solid var(--divider);padding-bottom:5px;margin-bottom:6px;}}
.take ul{{margin:0;padding-left:16px;}}
.take li{{font-size:12.2px;line-height:1.5;color:var(--body);margin:5px 0;}}
.take li b{{color:var(--navy);}}
.foot{{border-top:1px solid var(--divider);margin-top:auto;padding-top:8px;display:flex;
justify-content:space-between;gap:14px;font-size:10px;color:var(--gray);align-items:baseline;}}
.foot .src{{font-style:italic;}}.foot .brand{{white-space:nowrap;letter-spacing:.06em;}}
.foot .brand b{{color:#595959;font-weight:700;}}
.rnote{{font-size:10px;color:var(--gray);font-style:italic;margin:10px 0 0;line-height:1.4;}}
</style></head><body><div class="deck"><section class="page">
<div class="topbar"><div class="kicker">Traveling-HFC Census &nbsp;·&nbsp; Ownership &amp; Geography &nbsp;·&nbsp; 388 HFC-held properties (Ch. 394)</div>
<div class="pageno">Exhibit</div></div>
<h1>Who Holds the Traveling-HFC Portfolio — and Where the Institutional Targets Cluster</h1>
<div class="bar"></div>
<p class="insight">Ownership is a familiar bench of value-add sponsors and the geography is lopsided. Of <b>388 HFC-held
properties</b>, only <b>~1 in 4 (107)</b> are institutional-quality — <b>built 1990+ and 200+ units</b> — and they
concentrate in <b>DFW (53)</b> and <b>Houston (32)</b>; Austin holds just 13. Tellingly, volume and quality diverge:
<b>Presidium (5 of 7)</b> and <b>JPI (5 of 6)</b> skew new-and-large, while <b>S2 Capital's 35</b> and <b>Tides' 19</b> are mostly older or sub-200-unit stock.</p>
<div class="cols">
  <div style="flex:0 0 660px;min-width:0;display:flex;flex-direction:column;">
    <div class="sec">Top 30 private owners — number of HFC-held properties</div>
    <div class="ocols">{owner_block}</div>
    <p class="onote">Owner = the private group that conveyed the property into the HFC (normalized). Top 30 = {top_sum} of {identified} identified-owner properties; a further {unidentified} HFC properties have no owner identifiable from free records. &nbsp;*Tgt = target (built 1990+ &amp; 200+ units).</p>
  </div>
  <div style="flex:1;min-width:0;display:flex;flex-direction:column;">
    <div class="sec">By metro — and how many clear the quality bar</div>
    <table class="t"><colgroup><col><col style="width:56px"><col style="width:64px"><col style="width:60px"></colgroup>
      <thead><tr><th>Metro</th><th class="num">HFC</th><th class="num">1990+</th><th class="num">Target</th></tr></thead>
      <tbody>{metro_body}</tbody></table>
    <div class="funnel"><div class="ft">The quality funnel</div>
      <div class="frow"><div class="ftrk"><span class="fbar pale" style="width:100%"></span></div><div class="fnum">{F_ALL}<span class="fpct">100%</span></div><div class="flab">All HFC-held</div></div>
      <div class="frow"><div class="ftrk"><span class="fbar blue" style="width:{F_90/F_ALL*100:.0f}%"></span></div><div class="fnum">{F_90}<span class="fpct">{F_90/F_ALL*100:.0f}%</span></div><div class="flab">Built 1990 or newer</div></div>
      <div class="frow"><div class="ftrk"><span class="fbar gold" style="width:{F_TGT/F_ALL*100:.0f}%"></span></div><div class="fnum">{F_TGT}<span class="fpct">{F_TGT/F_ALL*100:.0f}%</span></div><div class="flab">Target — 1990+ &amp; 200+ u</div></div>
    </div>
    <div class="take"><div class="ft">The read</div>
      <ul><li><b>DFW + Houston</b> hold <b>{dfwhou_tgt} of the {F_TGT} targets</b> ({dfwhou_tgt/F_TGT*100:.0f}%) — the actionable set is a two-market story.</li>
      <li>The four biggest owners (S2, Tides, Post, Sphinx) hold <b>{top4}</b> HFC deals, but volume ≠ quality: of <b>S2's {s2c}</b> and <b>Tides' {tds}</b>, only <b>{s2t + tdt}</b> clear the bar.</li>
      <li>The newest-and-largest stock sits with <b>Presidium</b> and <b>JPI</b> — small holders, but nearly all target-grade.</li></ul></div>
    <p class="rnote">"Target" = HFC-held, built 1990 or newer, 200+ units — the institutional-scale subset most likely to trade at the 2027 unwind. Metros: DFW, Houston, Austin, San Antonio; "Other" = Beaumont, Corpus, Waco.</p>
  </div>
</div>
<div class="foot"><span class="src">Source: Traveling HFC/PFC census (458 properties; 388 HFC / Ch. 394 shown) — CAD rolls, county deed indexes, TDHCA, listing sites; owners normalized from recorded grantors &amp; press. As of 2026-07-12.</span>
<span class="brand"><b>The MILESTONE Group</b> &nbsp;|&nbsp; CONFIDENTIAL &amp; PROPRIETARY</span></div>
</section></div></body></html>"""

out = ROOT / "data/ownership_geography_slide.html"
out.write_text(html)
print(f"wrote {out} | top{TOPN} owners, top_sum={top_sum}/{identified} identified, {unidentified} unid | funnel {F_ALL}->{F_90}->{F_TGT}")
