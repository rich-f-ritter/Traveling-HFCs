# Bexar County — Traveling HFC/PFC Census

*Prepared 2026-07-11. Source: Bexar Central Appraisal District (BCAD) free public owner-name search
(`bexar.trueautomation.com/clientdb`, cid=110) and its per-account tax-year history (TY2022–TY2026),
cross-checked against `data/seed_properties.json` and public litigation/news coverage. See
`docs/phase1_verdict.md` and `data/sponsors.json` for sponsor tiering; `schema/property_record.schema.json`
for the per-record data model. Full records: `census/county_bexar.json`.*

## Headline

- **31 records**: all **25** Bexar seed rows accounted for (24 matched to a specific BCAD account, 1
  unresolved — see Gaps), plus **6 expansion properties** (`TX-NEW-BEXAR-1..6`) found by sweeping BCAD
  for our verified sponsor names beyond what the seed captured.
- **30 of 31** records carry a confirmed BCAD account number. Combined **TY2026 appraised value:
  $891,318,135** across those 30 accounts.
- **20 of 31** properties sit under a sponsor (Cameron County, Edcouch Community, La Villa, Maverick
  County, or Pleasanton HFC) that Bexar's chief appraiser **Rogelio Sandoval** has publicly named as a
  defendant/target in the appraisal district's suit over **~27 Bexar apartment complexes / $26M+** in
  contested exemptions. BCAD's own owner-search for those 5 sponsors' names turns up only **19** distinct
  Bexar accounts (+1 more from the seed with no BCAD match = 20 potential candidates) — **8 short of the
  reported 27**, and the suit's actual per-property exhibit list is not published anywhere free. Every
  property under those 5 sponsors is flagged `litigation_flags` as a likely/possible member of that set,
  not a confirmed one.
- **Pecos HFC** (6 properties, all Tier 1) and **Texas Essential Housing PFC** (5 properties, Tier 2) are
  **not** named in the Bexar suit's press coverage — Pecos carries its own separate litigation load
  (Haltom City, Tarrant ARB, Hays Co., TWHC challenge); TEHPFC is a Ch.303 PFC, outside HB21's reach
  entirely.
- **Notable compliance anomaly**: 5 of the 30 BCAD-confirmed properties (Edcouch's Maxwell Townhomes and
  Tara, and Pecos's Mission Villas and Brixton Apartments) show **no exemption ever granted** through
  TY2026 despite sponsor ownership of record — fully taxable every year on file. A 5th (Edcouch's Acadia
  on the Lake) has a partial-exemption year (TY2025) but its TY2026 value is blank/"N/A" on the portal
  (likely an active ARB protest). These are flagged for TDHCA §394.9027 audit-status follow-up.

## Sponsor breakdown

| Sponsor | Tier | Bexar properties (this file) | Combined TY2026 appraised value | Kill regime |
|---|---|---|---|---|
| Cameron County HFC | 1 | 6 | $207,200,000 | HB21 §13(i), 2027-01-01 |
| Edcouch Community HFC | 1 | 4 (+1 seed row unresolved) | $49,512,040 (Acadia's TY2026 value is N/A) | HB21 §13(i), 2027-01-01 |
| La Villa HFC | 1 | 2 | $35,500,000 | HB21 §13(i), 2027-01-01 |
| Maverick County HFC | 1 | 2 | $72,889,210 | HB21 §13(i), 2027-01-01 |
| Pecos HFC | 1 | 6 | $127,990,050 | HB21 §13(i), 2027-01-01 |
| Pleasanton HFC | 1 | 6 | $230,211,110 | HB21 §13(i), 2027-01-01 |
| Texas Essential Housing PFC | 2 | 5 | $168,015,725 | HB2071/Ch.303 grandfather — no fixed cliff |
| **Total** | | **31** | **$891,318,135** | |

All Tier-1 (HFC) properties are captured by **HB21 §13(i)** — exemption dies **2027-01-01** as
out-of-jurisdiction HFC-owned property, subject to the earlier **§13(e)** death trigger on any sale,
refinancing, or majority-ownership transfer (several properties here already show a recorded 2023–2025
recapitalization in the seed data; see `kill_analysis.recent_capital_event` per record). Texas Essential
Housing PFC (Ch.303) is **not** reached by HB21 — its 5 Bexar properties unwind only on a capital event,
99-year ground-lease term, a §303.0426 audit failure, or a successful CAD/AG challenge (cf. TEHPFC v.
Williamson CAD; AG opinion request KP-0437).

## Property table

| Property | City | BCAD account(s) | Units | TY2026 appraised value | In BAD suit? | Kill date | census_id |
|---|---|---|---:|---:|---|---|---|
| **Cameron County Housing Finance Corporation** | | | | | | | |
| Dalian 151 | San Antonio | 1248651 | 360 | $54,500,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1707 |
| Dalian Monterrey Village | San Antonio | 1207284 | 360 | $51,500,000 | Yes (sponsor named) | 2027-01-01 | TX-NEW-BEXAR-3 |
| Highland Ridge | San Antonio | 489629 | 736 | $42,500,000 | Yes (sponsor named) | 2027-01-01 | TX-NEW-BEXAR-2 |
| Residences at Medical | San Antonio | 487392 | 276 | $23,500,000 | Yes (sponsor named) | 2027-01-01 | TX-NEW-BEXAR-1 |
| Solara | San Antonio | 609239 | 285 | $26,000,000 | Yes (sponsor named) | 2027-01-01 | TX-61-614 |
| Willow Bend | San Antonio | 1129457, 1039279 | 250 | $9,200,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1675 |
| **Edcouch Community Housing Finance Corporation** | | | | | | | |
| Acadia on the Lake | San Antonio | 642630 | 304 | — (N/A on portal, TY2026) | Yes (sponsor named) | 2027-01-01 | TX-61-1757 |
| Maxwell Townhomes | San Antonio | 641263 | 314 | $40,500,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1237 |
| Tara | San Antonio | 1446279 | 234 | $9,012,040 | Yes (sponsor named) | 2027-01-01 | TX-61-1653 |
| *(unidentified — no BCAD match found)* | San Antonio | — | — | — | Yes (sponsor named) | 2027-01-01 | TX-61-531 |
| **La Villa Housing Finance Corporation** | | | | | | | |
| 5 Fifty | San Antonio | 646352 | 204 | $18,500,000 | Yes (sponsor named) | 2027-01-01 | TX-NEW-BEXAR-4 |
| Elevate at Huebner Grove | San Antonio | 565843 | 210 | $17,000,000 | Yes (sponsor named) | 2027-01-01 | TX-61-250 |
| **Maverick County Housing Finance Corporation** | | | | | | | |
| Alamo Residences at Spurs Lane | San Antonio | 1395697 | 120 | $15,889,210 | Yes (sponsor named) | 2027-01-01 | TX-61-1394163 |
| Sterling at Oak Hills | San Antonio | 1254484 | 330 | $57,000,000 | Yes (sponsor named) | 2027-01-01 | TX-61-2718 |
| **Pecos Housing Finance Corporation** | | | | | | | |
| Brixton Apartments | San Antonio | 500195, 1444659 | 384 | $23,500,000 | No (not in BAD press list) | 2027-01-01 | TX-61-1321 |
| Melia | San Antonio | 522684, 522690 | 300 | $14,057,700 | No | 2027-01-01 | TX-61-2092 |
| Mission Villas | San Antonio | 1444640 | 176 | $932,350 | No | 2027-01-01 | TX-61-384 |
| Seville | San Antonio | 639271 | 200 | $22,000,000 | No | 2027-01-01 | TX-61-1487 |
| Timberhill Commons | **Leon Valley** | 1300448, 1444456 | — | $40,500,000 | No | 2027-01-01 | TX-61-557312 |
| Vistas Two 52 | San Antonio | 595581 | 252 | $27,000,000 | No | 2027-01-01 | TX-61-1746 |
| **Pleasanton Housing Finance Corporation** | | | | | | | |
| Durrington Ridge | San Antonio | 1352388 | 398 | $69,000,000 | Yes (sponsor named) | 2027-01-01 | TX-61-387177 |
| Med West | San Antonio | 1284640 | 131 | $19,900,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1175498 |
| Nova Apartments | San Antonio | 1117284 | 412 | $53,500,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1709 |
| Oasis | San Antonio | 1193224 | 260 (+694 beds noted by BCAD) | $42,500,000 | Yes (sponsor named) | 2027-01-01 | TX-61-659 |
| Summit at Henderson Pass | San Antonio | 606514 | 228 | $21,791,110 | Yes (sponsor named) | 2027-01-01 | TX-61-533 |
| Trailside | San Antonio | 685075 | 240 | $23,520,000 | Yes (sponsor named) | 2027-01-01 | TX-61-1955 |
| **Texas Essential Housing Public Facility Corporation** (Tier 2 — no cliff) | | | | | | | |
| 410 Probandt | San Antonio | 1399472 | — | $5,517,690 | No (Ch.303, different regime) | event-driven | TX-NEW-BEXAR-6 |
| Abacus Alamo Ranch | San Antonio | 1304106 | 320 | $61,095,110 | No | event-driven | TX-61-374106 |
| Alaro | San Antonio | 1390520 | 248 | $54,461,070 | No | event-driven | TX-NEW-BEXAR-5 |
| Atlee | San Antonio / Olmos Park | 369472, 369485, 369492 | 144 | $11,441,855 | No | event-driven | TX-61-1521 |
| Copper Mill | San Antonio | 617253 | 342 | $35,500,000 | No | event-driven | TX-61-457 |

*"In BAD suit?" flags **sponsor-level** membership in the publicly reported Sandoval suit (Maverick,
Cameron, Pleasanton, La Villa, Edcouch named; Pecos and TEHPFC not named) — no property-level exhibit
list was found in free sources, so this is not a confirmed per-property flag. See Gaps.*

## Method

1. **Seed**: filtered `data/seed_properties.json` to `property_county == "Bexar"` → 25 rows across 7
   verified sponsors (6 Tier-1 HFCs + Texas Essential Housing PFC).
2. **BCAD owner search**: queried `bexar.trueautomation.com/clientdb` (BCAD's free property-search
   backend) by each sponsor's verified name, plus broad sweeps on `HOUSING FINANCE CORPORATION` and
   `PUBLIC FACILITY CORPORATION` (paginated) to catch anything outside the 7 known sponsors.
3. **Per-account history**: for every distinct BCAD account found, pulled the TY2022–TY2026 tax-year
   toggle (`Property.aspx`) to get appraised value, exemption code, and "Taxes w/Current Exemptions" vs.
   "Taxes w/o Exemptions" for each year — the first year those two converge to ~$0 is recorded as
   `exemption.first_exempt_tax_year`.
4. **Seed-row pairing**: matched seed rows to specific BCAD accounts using city (Leon Valley is a unique
   fingerprint for one Pecos property), partner-name web searches (LoanCore Capital/Solara, Brixton
   Capital/Atlee, Lynd Management/Copper Mill all independently confirmed), and — where no independent
   signal existed — aggregate count reconciliation with an explicit low-confidence flag. See each
   record's `gaps` array for exactly which pairings are unconfirmed.
5. **BAD suit cross-check**: web-searched San Antonio Express-News/News4SanAntonio coverage of Chief
   Appraiser Rogelio Sandoval's suit; found sponsor names (Maverick, Cameron, Pleasanton, La Villa,
   Edcouch) and the $26M/27-complex headline figures, but **no property-level list** — the actual
   petition/exhibit was not located in a free source (Bexar County District Clerk's online portal does
   not appear to offer free full-text search for this case; case number not found).

## Local (non-traveling) sponsors excluded from this file

The `%HOUSING FINANCE CORP%` / `%PUBLIC FACILITY CORP%` sweep also surfaced several Bexar/San-Antonio
**home-turf** sponsors whose properties are *not* traveling (sponsor jurisdiction = parcel jurisdiction),
so they fall outside this project's scope and are not itemized here:

- **San Antonio Housing Trust Public Facility Corporation** — ~20 San Antonio properties (Lucero, Maya,
  Oak Valley, Trove Southtown, Upton at Longhorn Quarry, Baldwin at St. Paul Square, etc.)
- **San Antonio Housing Finance Corporation** — several small San Antonio parcels
- **ACCD Public Facility Corporation** (Alamo Community College District) — Lofts on Main, Tobin Lofts
  (student housing)
- **Bexar County Public Facility Corporation** — Weston Urban/South Laredo
- **Las Varas Public Facility Corporation** — affiliated with Opportunity Home San Antonio (formerly San
  Antonio Housing Authority); Riverbreeze/Palo Alto/Wurzbach Manor bond deals

## Gaps

1. **TX-61-531 (Edcouch, partner Pennybacker Capital)** — no matching BCAD account found. BCAD's
   `EDCOUCH` owner search returns exactly 3 distinct Edcouch-owned Bexar accounts, all already paired to
   the other 3 Edcouch seed rows; this 4th seed row is unresolved (possibly divested, or recorded under
   an unindexed name variant).
2. **Individual seed-row-to-BCAD-account pairings are unconfirmed** for most Cameron County, Edcouch, La
   Villa, Maverick, Pecos, and Pleasanton properties beyond the 5 independently confirmed via web search
   (Solara/LoanCore Capital, Timberhill Commons/Leon Valley, Atlee/Brixton Capital, Copper
   Mill/Lynd Management, and by process-of-elimination Abacus Alamo Ranch/Ascendant Capital Partners).
   Where a sponsor's BCAD account count matches its seed-row count, the aggregate match is solid but
   which specific seed partner maps to which specific address is a best-effort guess flagged
   `single-source` confidence — see each record's `gaps`.
3. **5 properties show no confirmed exemption**: Maxwell Townhomes, Tara (Edcouch); Mission Villas,
   Brixton Apartments (Pecos) are fully taxable on BCAD's own record through TY2026 despite sponsor
   ownership; Acadia on the Lake (Edcouch) has a partial-exemption TY2025 but blank TY2026 value
   (likely ARB protest). None of these has been cross-checked against TDHCA's §394.9027 audit-filing
   status (that dataset was still "TBD" per `docs/phase1_verdict.md` as of 7/11/2026).
4. **Bexar Appraisal District suit's per-property list not found** — Chief Appraiser Sandoval's ~27
   complex/$26M+ figure is well-documented in press, but the actual petition/exhibit naming the 27
   properties was not located via free search (no case number, no Bexar County District Clerk online
   docket found). All properties under the 5 named sponsors (20 of 31 records) are flagged as
   possible/likely members, not confirmed.
5. **Units unknown** for 3 properties (Timberhill Commons, 410 Probandt, and the unresolved TX-61-531) —
   not published on BCAD's DBA field or on free apartment-listing sites checked.
6. **`instrument_extractions`, `structure_dates` (MOU/SWD/ground-lease recording refs), `covenant`
   (set-aside %/AMI band)** — not pursued this pass; would require county-clerk grantor/grantee search
   (Method 3, `kit/02_identification-playbook.md`) or TPIA requests to sponsors, out of scope for a
   free-CAD-portal pass.
7. **`loan`/CMBS-CLO surveillance** — only populated for Solara (LoanCore Capital, confirmed distressed
   2024 foreclosure via The Real Deal); no DBRS/Trepp/CRED iQ pull performed for the other 29 accounts.
