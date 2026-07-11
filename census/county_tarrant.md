# Tarrant County — Traveling HFC/PFC Census

*Compiled 2026-07-11. Sources: `data/seed_properties.json` (Matrix seed, filtered to
`property_county == "Tarrant"`, 55 rows), `data/sponsors.json` + `docs/phase1_verdict.md`
(Phase 1 verified sponsor roster), and live owner-name searches of the free Tarrant
Appraisal District portal (**tad.org**, property search + per-account pages), retrieved
2026-07-11. Every property below carries per-field provenance in
`census/county_tarrant.json`; this file is the human-readable summary.*

## Headline finding: TAD has quietly stopped granting the exemption on new deals — well ahead of both the court fights and the 2027 cliff

Tarrant County property tax lien attaches Jan 1, so a deed recorded any time within the year
determines exemption eligibility for the *following* tax year. Pulling every one of the 82 TAD
accounts held by our 8 confirmed traveling HFC/PFC sponsors and reading each account's own
"Exemptions / Special Appraisal" section produced a striking, clean pattern:

- **Deeds recorded before ≈ February 2025** almost universally still carry an active
  `PUBLIC PROPERTY 11.11` exemption code in TAD's live system today (TY2026).
- **Deeds recorded from ≈ February 2025 onward** almost universally show **no exemption on
  file at all** — TAD's own account pages say *"There are no exemptions for this property."*
  These parcels are **fully taxable right now**, as reflected in TAD's public records.

This flip predates the Haltom City injunction (6/3/2025), the Tarrant County ARB petitions
(filed 5/28/2025), and is unrelated to which city sued whom — it cuts across all 8 sponsors and
every Tarrant city in the sweep. It looks like TAD tightened its own administrative practice on
new HFC exemption applications in early 2025, independent of and running ahead of both the
litigation and the 1/1/2027 HB21 statutory cliff. **33 of the 60 properties below (55%) are
already fully taxable in TAD's system today** — the "kill" has, for these properties, already
happened administratively, years before the statute forces it.

This is distinct from, and layered on top of, the two active injunctions:

- **Haltom City** (2 Pecos HFC properties in this census): Jefferson Fossil Creek (acct 43027850,
  deed 12/18/2024) still shows an **active** exemption; Emmit Luxury Apts (accts 4986261/4986288,
  deed 5/16/2025) shows **no exemption on file** — consistent with the Feb-2025 cutoff above,
  not obviously driven by the injunction itself.
- **Arlington** (8 properties across 4 sponsors): 4 still show active exemptions (older deeds,
  2023–2024), 4 show none (2025 deeds) — same pattern.

## Numbers

| Metric | Count |
|---|---|
| Seed rows (property_county = Tarrant) | 55 |
| Seed rows matched to a TAD account | 53 |
| Seed rows with **no** TAD match (gap) | 2 (Roanoke/Maverick, Burleson/Pleasanton — see Gaps) |
| New properties found via sponsor/owner-name sweep, not in seed | 5 (`TX-NEW-TARRANT-1..5`) |
| **Total census records** | **60** |
| Records with a resolved TAD account | 58 |
| Total 2026 appraised value (sum of known accounts) | **≈ $2.02 billion** |
| Properties in Haltom City / Arlington (the two litigated cities) | 2 / 8 |
| Properties already fully taxable per TAD (no §11.11 on file) | 33 |
| Properties still showing an active §11.11 exemption (targeting the 1/1/2027 cliff) | 22 |
| Properties with kill status undetermined (2 unmatched + 3 Tier-2 PFC, event-driven) | 5 |
| Underlying TAD accounts (parcels) behind the 60 properties | 82 |

Cross-check: Tarrant County's own 5/28/2025 ARB petition described **28 sites / $974M** in one
initial filing batch. This census — covering all 8 confirmed traveling sponsors, not just the
subset in that petition — finds **58 accounts across ~58 sites and ~$2.02B**, consistent with
the County's petition being a first tranche rather than the full traveling-HFC footprint in
Tarrant.

## By sponsor

| Sponsor | Tier | Properties in Tarrant | Total 2026 appraised value | Cliff |
|---|---|---|---|---|
| Pecos Housing Finance Corporation | 1 | 27 | $844,640,000 | HB21 §13(i) 1/1/2027 |
| Pleasanton Housing Finance Corporation | 1 | 12 | $477,951,037 | HB21 §13(i) 1/1/2027 |
| Cameron County Housing Finance Corporation | 1 | 6 | $231,588,117 | HB21 §13(i) 1/1/2027 |
| Maverick County Housing Finance Corporation | 1 | 5 | $181,500,000 | HB21 §13(i) 1/1/2027 |
| Edcouch Community Housing Finance Corporation | 1 | 3 | $106,700,000 | HB21 §13(i) 1/1/2027 |
| Texas Essential Housing Public Facility Corporation | 2 | 3 | $100,331,500 | No cliff (Ch.303 PFC) |
| La Villa Housing Finance Corporation | 1 | 3 | $60,800,000 | HB21 §13(i) 1/1/2027 |
| Garland Housing Finance Corporation | 1 | 1 | $19,038,359 | HB21 §13(i) 1/1/2027 |

All 8 sponsors are on the Phase 1 verified roster (`data/sponsors.json`); all are confirmed
traveling (home jurisdiction outside Tarrant County) except that all sit **in** Tarrant here —
Tarrant is a destination county for every one of them, not a home county for any.

## Full property table

| Property | City | TAD account(s) | 2026 appraised value | Exemption now? | Kill date |
|---|---|---|---|---|---|
| 5300 Village Ln Apts | Fort Worth | 4705912; 4705920; 4705939; 4705947 | $20,100,000 | Active | 2027-01-01 |
| Dylan East Fort Worth | Fort Worth | 4849264 | $15,200,000 | Active | 2027-01-01 |
| Monarch Pass Apartment Homes | Fort Worth | 4981812 | $96,000,000 | Active | 2027-01-01 |
| Sierra Gardens | Fort Worth | 2445921; 5968631; 4691865 | $18,100,000 | **None** | already |
| Oak Park *(new find)* | Euless | 2054183; 2054191; 7049498 | $81,900,000 | Active | 2027-01-01 |
| Lofts at Grand Prairie (vacant land) *(new find)* | Grand Prairie | 43255054; 43255062 | $288,117 | **None** | already |
| Elliot Windsprint Apts | Arlington | 4846710 | $34,600,000 | **None** | already |
| Meadow Ridge | Fort Worth | 41525787; 41564685 | $38,600,000 | Active | 2027-01-01 |
| infinity on the landing *(new find)* | Fort Worth | 4971493 | $33,500,000 | Active | 2027-01-01 |
| Legacy Riverside Senior Living | Fort Worth | 42717874 | $19,038,359 | Active | 2027-01-01 |
| the carmin | Arlington | 4761634 | $21,100,000 | **None** | already |
| 500 Flats (Woodridge) | Fort Worth | 4325893 | $18,400,000 | **None** | already |
| Flats on Mill | Fort Worth | 5550939 | $21,300,000 | **None** | already |
| Landmark at Crowley | Crowley | 42687789 | $45,000,000 | **None** | already |
| Lost Spurs Ranch Apts | Fort Worth | 7830262 | $37,300,000 | **None** | already |
| Mag and May Apts | Fort Worth | 42332301 | $38,700,000 | Active | 2027-01-01 |
| The Sovereign | Fort Worth | 41652207 | $60,500,000 | Active | 2027-01-01 |
| *(unresolved — see Gaps)* | Roanoke | — | — | — | — |
| Cedar Point Apts | Arlington | 1592742 | $31,900,000 | Active | 2027-01-01 |
| Jefferson North Collins | Arlington | 42642581 | $68,000,000 | Active | 2027-01-01 |
| Westley Apts | Arlington | 2930528; 2930536 | $37,800,000 | **None** | already |
| Athena | Benbrook | 640654 | $27,600,000 | **None** | already |
| Lawson | Benbrook | 4770773 | $18,200,000 | **None** | already |
| Leander Apt Homes | Benbrook | 640816 | $17,300,000 | **None** | already |
| Sagamore Apartment Homes | Benbrook | 640794; 640808 | $35,200,000 | **None** | already |
| 1505 Exchange | Fort Worth | 4402324 | $21,000,000 | **None** | already |
| Azora Ranch | Fort Worth | 42793929 | $4,180,000 | **None** | already |
| Bridge Hollow Apartments | Fort Worth | 4972759 | $24,000,000 | Active | 2027-01-01 |
| Casa Villa | Fort Worth | 4855280 | $13,300,000 | **None** | already |
| Decker Apartment Homes | Fort Worth | 4885953 | $18,100,000 | **None** | already |
| Stella | Fort Worth | 1198998 | $14,500,000 | **None** | already |
| Stillwater Crystal Springs Apts | Fort Worth | 42699604 | $67,300,000 | **None** | already |
| Taylor Commons Apts. | Fort Worth | 538744 | $20,800,000 | **None** | already |
| The Falls / The Oaks | Fort Worth | 3435024; 3435075 | $40,700,000 | Active | 2027-01-01 |
| The Ryan Apts | Fort Worth | 4972848 | $16,200,000 | Active | 2027-01-01 |
| The Woodlands | Fort Worth | 4447727; 6468071; 5654394 | $25,500,000 | **None** | already |
| Tides at Eastchase | Fort Worth | 5682045 | $25,500,000 | **None** | already |
| Western Station at Fossil Creek | Fort Worth | 7008937 | $36,200,000 | Active | 2027-01-01 |
| Vine on North Park | Grapevine | 5647622; 5647630 | $40,900,000 | **None** | already |
| Emmit Luxury Apts | Haltom City | 4986261; 4986288 | $41,860,000 | **None** | already |
| Jefferson Fossil Creek | Haltom City | 43027850 | $73,200,000 | Active | 2027-01-01 |
| Hills at Ironhorse | North Richland Hills | 4986776 | $31,600,000 | **None** | already |
| Parkwyn | North Richland Hills | 5647452 | $29,300,000 | **None** | already |
| The Hudson | North Richland Hills | 4987144 | $32,500,000 | **None** | already |
| Remi Apartments | White Settlement | 5677483; 5676002 | $32,000,000 | **None** | already |
| Cedar at River Legacy Park | Arlington | 4970594 | $32,800,000 | **None** | already |
| Tides at North Arlington | Arlington | 2146436; 2146290 | $37,100,000 | Mixed (1 of 2 accts) | already |
| *(unresolved — see Gaps)* | Burleson | — | — | — | — |
| 0 Blue Mound Rd (vacant land) | Fort Worth | 42721201 | $451,037 | Active | 2027-01-01 |
| Cortland Riverside | Fort Worth | 42220791; 42220783 | $65,400,000 | **None** | already |
| Flats at Brentwood | Fort Worth | 1184954 | $15,100,000 | Active | 2027-01-01 |
| Northpoint Villas | Fort Worth | 41410475 | $49,600,000 | Active | 2027-01-01 |
| Rocklyn Apartments | Fort Worth | 42402920; 42402938; 42402946 | $53,400,000 | Active | 2027-01-01 |
| The Dawnson at Berkshire | Fort Worth | 42729627 | $66,500,000 | Active | 2027-01-01 |
| Tides on Randol Mill Apts | Fort Worth | 5682460; 6493777 | $32,000,000 | **None** | already |
| Neuhaus Lake Worth Apts | Lake Worth | 43008758 | $54,700,000 | **None** | already |
| The Sydney *(new find)* | Mansfield | 42662484 | $70,900,000 | Active | 2027-01-01 |
| Palace of Arlington | Arlington | 1181793; 4620070 | $43,300,000 | Active | n/a (Tier 2 PFC) |
| Chapparal Apts *(new find)* | Fort Worth | 7245637 | $12,400,000 | Active | n/a (Tier 2 PFC) |
| Range West | Saginaw | 42987235; 42987243 | $44,631,500 | Active | n/a (Tier 2 PFC) |

## The 5 new (non-seed) discoveries

Found by sweeping TAD owner-name search across all 8 confirmed sponsors plus
`%HOUSING FINANCE CORP%` / `%PUBLIC FACILITY CORP%` broadly (which also turned up ~250 accounts
under Fort Worth's own local HFC, Arlington's own local HFC, Fort Worth Housing Solutions'
various single-project PFCs — Cavile, Eastwood, Hillside, Huntley, Ironwood Crossing, FW
Alliance/Bonds Ranch/Primrose/Ramble/Skyline — plus Hurst PFC, Mansfield PFC, and Grand Prairie
HFC. All of those are **local** (sponsor's home city = property's city) and were excluded as
non-traveling; not deep-dived further here):

1. **TX-NEW-TARRANT-1** — Oak Park Apts, Euless (Cameron County HFC, 3 accounts, $81.9M) —
   owner name recorded as "Cameron County Housing **Corporation**" (missing "Finance"), which is
   why it didn't surface in a strict "Housing Finance" search.
2. **TX-NEW-TARRANT-2** — Lofts at Grand Prairie, vacant land (Cameron County HFC, 2 accounts,
   $288K) — **not yet built**; a land-banking parcel, worth flagging as a leading indicator of a
   pipeline deal.
3. **TX-NEW-TARRANT-3** — infinity on the landing, Fort Worth (Edcouch Community HFC, $33.5M) —
   seed's Edcouch/Fort Worth count was 1; TAD shows 2.
4. **TX-NEW-TARRANT-4** — The Sydney, Mansfield (Pleasanton HFC, $70.9M) — seed's Pleasanton
   Tarrant footprint didn't include Mansfield.
5. **TX-NEW-TARRANT-5** — Chapparal Apts, Fort Worth (Texas Essential Housing PFC, $12.4M).

## Gaps

- **TX-38-2533** (Maverick County HFC, seed city = Roanoke): no TAD account found under any
  Maverick spelling variant, and a full TAD `PropertyCity=Roanoke` sweep found no HFC/PFC-owned
  exempt multifamily. Roanoke sits mostly in **Denton County** — the seed's `property_county =
  Tarrant` label may be wrong, or this parcel is on Denton CAD's roll instead. Recommend a Denton
  CAD check.
- **TX-38-1314388** (Pleasanton HFC, seed city = Burleson): no TAD account found; a full
  Pleasanton owner-name sweep returned 16 accounts, none in Burleson. Burleson spans Tarrant,
  Johnson, and Ellis counties — likely sitting in the Johnson CAD portion.
- **TX-38-1487** (Edcouch Community HFC): seed labels this property's city as Euless; no
  Edcouch-owned exempt multifamily exists in Euless per TAD (confirmed via a full Euless sweep,
  1,166 commercial parcels checked). Best match is Edcouch's Elliot Windsprint Apts in Arlington
  — paired here as a best-effort match, flagged as unverified against Matrix.
- **Units**: not published anywhere in TAD's bulk export or individual account pages for any of
  the 60 properties — would need CoStar/Apartments.com/site-plan cross-reference.
- **Zip codes**: not a field TAD's property search returns.
- **Annual exemption value (foregone tax $)**: not computed — would need each property's
  FY2026 combined ad valorem rate (city + Tarrant County + hospital district + college district +
  ISD, which vary by taxing-unit set — captured per property in the JSON's
  `exemption.taxing_units` count) applied to `appraised_value`.
- **Partners** (private developer/operator) are only known for seed-matched rows (from Matrix);
  all 5 new finds have no partner identified.
- **Ground-lease term/date**: only captured where the Matrix seed row carried a
  `ground_lease_comment`; new finds and several seed rows lack it.
- **TDHCA §394.9027 audit status**: unknown for all — TDHCA's compliance-monitoring lists were
  still "TBD" as of 7/11/2026 per `docs/phase1_verdict.md`.
- **Seed-to-TAD address pairing**: Matrix's seed data carries no street address. Where a
  (sponsor, city) group had the same count of seed rows as TAD sites, they were paired 1:1
  (position-arbitrary, noted per-record in `provenance`); this is high-confidence for the
  property's *existence, sponsor, and exemption facts*, but the specific census_id ↔ specific
  street address pairing within a multi-property group is not independently verified.
- **Loan/lender/CMBS data**: out of scope for public-record-only sourcing per project
  constraints; would need Trepp/DBRS/CRED iQ surveillance.

## Method note

TAD's owner-name search (`tad.org/search-results`, POST form) does OR-style token matching, so
a query like "Pecos Housing Finance Corporation" also returns unrelated matches containing any
of those words. All matches here were filtered down to accounts whose **Owner Name** field
resolves to one of the 8 verified sponsor entities (allowing for TAD's own scrivener misspellings
— "Hosuing" for "Housing", "Cameron County Housing Corporation" for "...Housing **Finance**
Corporation", "Maverick County Finance Corporation" for "...**Housing** Finance Corporation" —
all three variants were found and folded in). Bulk CSV export
(`tad.org/export/search-txt`) was used for the full-column property/value data; individual
account pages (`tad.org/property?account=<id>`) were fetched separately for deed date,
instrument number, and the current-year exemption-code list (not present in the bulk export).
