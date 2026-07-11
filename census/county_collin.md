# Collin County -- Traveling HFC/PFC Census (Phase 3)

**Scope:** 13 Matrix-seed rows for Collin County + 9 expansion properties discovered via a Collin
Central Appraisal District (CCAD, collincad.org) owner-name sweep (Method 2). All 13 seed rows
carry a CCAD-confirmed account; 11 are HIGH-confidence name/date/partner matches and 2 rest on a
disclosed single-source assumption (see Method, below). Only 5 of our 13 verified sponsors
(Cameron County HFC, Garland HFC, La Villa HFC, Maverick County HFC, Pecos HFC) own property in
Collin County; the other 8 (Pleasanton, Edcouch, Texas Essential Housing PFC, Houston HA, Cameron
County HA, Rosenberg HA, San Benito HA) returned zero hits.

**Total appraised value captured (22 properties): $728,600,549** ($522,997,173 across the 13
seed-linked records + $205,603,376 across the 9 net-new expansion records).

## Headline finding: the opposite of Dallas -- most Collin parcels ARE currently exempt

Unlike Dallas County (Phase 3 wave 1), where only 11 of 132 traveling HFC parcels showed an active
exemption, **20 of 22 Collin properties (91%) appear on CCAD's TY2026 Absolute Exemption List**
(`apc5-s9fa`, the statutorily-required Tex. Admin. Code §9.3011 public list of 100%-exempt
accounts) as of the 2026-07-10/11 data pull. Only two properties are NOT currently benefiting from
the structure:

- **The Riley** (Garland HFC, Richardson, TX-NEW-COLLIN-3) -- acquired 2024-04-30, but has **never**
  carried an exemption code on any CCAD roll through TY2026. Two-plus years of ownership with no
  exemption ever posted; cause (no application filed, application denied, or a TDHCA §394.9027
  non-filing) cannot be determined from the appraisal roll alone.
- **Hathaway at Willow Bend** (Pecos HFC, Plano, TX-NEW-COLLIN-9) -- Pecos HFC acquired it
  2025-03-21, but CCAD's TY2026 Preliminary roll shows it **already sold** to Winston GT Holdings LP
  (deed 2026-06-24/25) -- a pre-2027 §13(e) capital-event exit, independently discovered in this
  sweep (see below). Interestingly, CCAD's Absolute Exemption List snapshot (pulled the same day as
  the current roll) had **not yet caught up** to the sale and still showed Pecos HFC as owner -- a
  useful illustration of how "current exemption status" can differ depending on which CCAD table you
  query, and a caution against treating any single extract as fully authoritative.

**Important caveat:** TY2026 is CCAD's "Preliminary" roll (`propStatus: Preliminary`), not yet
ARB-certified as of 2026-07-11 (certification typically follows in late July). Sixteen of the 20
currently-exempt properties are 2025-vintage acquisitions that show `exemptCodes=None` on the
TY2025 *certified* roll and only pick up `EX-XV` on the TY2026 preliminary extract -- i.e., the
exemption looks newly granted this year, consistent with the acquisition timing, but could still be
revised before final certification. Three properties (Savannah at Gateway Senior Apartments and
Montgomery at Watters Creek, both Garland HFC; and 380 Villas, Cameron County HFC) have
longer-standing, TY2025-certified exemptions (see `first_exempt_tax_year` below).

**Methodology note on "exempt":** CCAD's bulk roll export (`currValAssessed`) does **not** net out
this exemption for any parcel checked, including known 100%-exempt government buildings -- so the
assessed-value field cannot be used the way Dallas's DCAD `TOTAL_EXEMPTION` field was used in wave
1. This census instead uses CCAD's separately-published Absolute Exemption List (`apc5-s9fa`) as the
authoritative "currently exempt" signal.

## Independently-discovered capital event (pre-2027 exit)

- **Hathaway at Willow Bend** (2525 Preston Rd, Plano, 229 units) -- sold by **Pecos Housing Finance
  Corporation** to **Winston GT Holdings LP** (& Herrera 1031 TIC LLC & Artem Winston LLC), deed
  effective **2026-06-24** (filed 2026-06-25, CCAD instrument 2026000085487) -- roughly two weeks
  before this data pull. Treated in the JSON as a §13(e) early-death event with `kill_date_estimate`
  set to the actual deed date, analogous to the Bernard/Beckham/Blake and Knowlton Apartment Homes
  findings in `census/county_dallas.md`.

## Method

1. Queried Collin CAD's own free bulk appraisal-data exports via the Texas.gov Open Data Portal
   (Socrata API) rather than downloading the full roll file, to conserve disk: current/preliminary
   TY2026 roll (`data.texas.gov/resource/nne4-8riu.json`, dataset "Collin CAD Appraisal Data -
   Preliminary"), the TY2025 certified roll (`vffy-snc6`) and TY2020-2024 certified rolls (used to
   bracket first-exempt years), the TY2026 Absolute Exemption List (`apc5-s9fa`), and CCAD's
   published entity tax rates (`pvdc-9ym5`, "Collin CAD Value History") to estimate foregone tax.
2. Filtered each year's roll by `ownername LIKE '%<sponsor name>%'` for all 13 verified sponsor
   entities (`data/sponsors.json`) plus generic `%HOUSING FINANCE CORP%` / `%PUBLIC FACILITY CORP%`
   sweeps to catch any un-rostered HFC/PFC. The generic sweep returned exactly the same 21 parcels as
   summing the 5 relevant sponsor-name searches -- no additional/unrostered HFC owns Collin
   multifamily property. The `%PUBLIC FACILITY CORP%` sweep surfaced Plano PFC, Pecan PFC, and
   McKinney PFC (all locally-domiciled, non-traveling, and not among our 13 sponsors) -- excluded, see
   below.
3. Linked 13 seed rows to specific CCAD accounts by cross-referencing `sale_comment` text (deed
   dates, named partners, portfolio unit counts) and `ground_lease_comment` against CCAD's
   `dbaName`/`deedEffDate`/owner-name fields -- 11 rows are high-confidence exact matches (unit
   counts, partner names, or ground-lease-term/city uniquely identify the parcel); 2 rows
   (`TX-37-8327`/`TX-37-8328`, both Cameron County HFC "Dallas" rows) rest on a disclosed
   descending-value bucket pairing within a 4-parcel same-deed-batch cluster, and 1 row
   (`TX-37-3160`, Pecos HFC "Plano") was a best-effort pick between two same-city, same-era
   candidates -- flagged `single-source` with a gap note on each.
4. The 9 CCAD-confirmed parcels left over after seed-linking became expansion records
   `TX-NEW-COLLIN-1..9`, including two small ($6-99K) unnamed common-area/amenity outparcels that
   share a site address and deed batch with a matched apartment complex.
5. **Excluded as non-traveling / out of scope (not counted in the totals above):** Plano Housing
   Authority (one of our 13 sponsors, but Collin-based/home-turf -- same treatment the Dallas census
   gave Garland HFC's in-Garland parcels), Plano Public Facility Corporation, Pecan Public Facility
   Corporation, McKinney Public Facility Corporation, Housing Authority of the City of McKinney/
   Frisco/Dallas, and other local housing authorities -- none of these are among our 13 verified
   sponsors, or (for Plano HA) the holdings found were on its own home turf.

## Table: all 22 properties

| census_id | sponsor | property | city | CAD account | units | appraised value | exempt now (TY26)? | first-exempt yr | kill date |
|---|---|---|---|---|---|---|---|---|---|
| TX-37-109 | Cameron County HFC | Spring Pointe Apartments | Richardson | 1615274 | 208 | $25,558,696 | Y | 2026 | 2027-01-01 |
| TX-37-8327 | Cameron County HFC | Oaks of North Dallas Apartments (4701 Haverwood) | Dallas | 1571748 | 168 | $16,760,321 | Y | 2026 | 2027-01-01 |
| TX-37-8328 | Cameron County HFC | 4804 Haverwood Apartments | Dallas | 1708824 | 180 | $15,751,585 | Y | 2026 | 2027-01-01 |
| TX-37-8332 | Cameron County HFC | 380 Villas | McKinney | 2905902 | 220 | $48,859,852 | Y | 2024 | 2027-01-01 |
| TX-NEW-COLLIN-1 | Cameron County HFC | Oaks of North Dallas Apartments (5075 Pear Ridge) | Dallas | 1650804 | 144 | $14,002,575 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-2 | Cameron County HFC | Oaks of North Dallas Apartments (5055 Pear Ridge) | Dallas | 1650813 | 144 | $13,788,728 | Y | 2026 | 2027-01-01 |
| TX-37-1228308 | Garland HFC | Montgomery at Watters Creek | Allen | 2834129 | 370 | $87,659,189 | Y | 2023 | 2027-01-01 |
| TX-37-1480322 | Garland HFC | Savannah at Gateway Senior Apartments | Plano | 2630081 | -- | $4,654,168 | Y | ≤2020 | 2027-01-01 |
| TX-NEW-COLLIN-3 | Garland HFC | The Riley | Richardson | 2924643 | 269 | $62,918,060 | **N** | never | already taxable |
| TX-37-4164 | La Villa HFC | Twin Creeks Crossing I Apartments | Allen | 2731037 | 347 | $60,528,188 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-4 | La Villa HFC | Twin Creeks Crossing II Apartments | Allen | 2735309 | 330 | $57,575,594 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-5 | La Villa HFC | (common-area outparcel) | Allen | 2735311 | -- | $6,338 | Y | 2026 | 2027-01-01 |
| TX-37-1180 | Maverick County HFC | Palencia Apartments | Dallas | 2018449 | 281 | $32,936,817 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-6 | Maverick County HFC | (common-area outparcel) | Dallas | 2040610 | -- | $70,276 | Y | 2026 | 2027-01-01 |
| TX-37-369642 | Maverick County HFC | Alma Hub 121 Apartments | McKinney | 2820606 | 286 | $50,321,895 | Y | 2026 | 2027-01-01 |
| TX-37-3204 | Pecos HFC | Larkin | McKinney | 2057207 | 240 | $38,218,870 | Y | 2026 | 2027-01-01 |
| TX-37-3160 | Pecos HFC | The Dayton | Plano | 1627494 | 389 | $47,324,508 | Y | 2026 | 2027-01-01 |
| TX-37-4378 | Pecos HFC | Carson at Twin Creeks | Allen | 2856059 | 374 | $67,847,411 | Y | 2026 | 2027-01-01 |
| TX-37-3179 | Pecos HFC | Adriane | Wylie | 2526594 | 180 | $26,575,673 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-7 | Pecos HFC | (common-area outparcel) | Dallas | 1970815 | -- | $99,461 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-8 | Pecos HFC | The Junction at 7760 | Dallas | 1963419 | 297 | $22,642,344 | Y | 2026 | 2027-01-01 |
| TX-NEW-COLLIN-9 | Pecos HFC | Hathaway at Willow Bend | Plano | 1716655 | 229 | $34,500,000 | **SOLD 2026-06-24** | -- | 2026-06-24 (already occurred) |

*"exempt now" = appears on CCAD's TY2026 Absolute Exemption List (`apc5-s9fa`), Preliminary/
not-yet-certified. "first-exempt yr" = first tax year the account shows an exemption code across
CCAD's TY2020-2026 rolls (bracketed year-over-year); most 2025-vintage acquisitions show
`first-exempt yr = 2026`, meaning the exemption first appears on the still-preliminary current roll.*

## By sponsor

| Sponsor | Records (seed+new) | Appraised value | Currently exempt (TY26 preliminary) |
|---|---|---|---|
| Pecos HFC | 7 | $237,208,267 | 6 (7th sold out of structure 6/24/2026) |
| Garland HFC | 3 | $155,231,417 | 2 (3rd never exempt) |
| Cameron County HFC | 6 | $134,721,757 | 6 |
| La Villa HFC | 3 | $118,110,120 | 3 |
| Maverick County HFC | 3 | $83,328,988 | 3 |

## Kill analysis

All 5 sponsors present in Collin County are **Tier 1 HFCs (Ch.394)**, confirmed traveling, and
captured by **HB 21 §13(i)** -- exemption loss effective **1/1/2027**, absent a qualifying
host-jurisdiction resolution. None of the Collin seed rows' `sale_comment` text describes a sale
*out of* HFC ownership (they describe the HFC's own *entry* into each deal, mostly 2024-2025
recapitalizations/acquisitions) -- so no seed-linked record carries an independent §13(e) early-death
trigger from the seed data itself. The one confirmed §13(e) event (Hathaway at Willow Bend) was
found only through the CCAD sweep, not the seed.

- **20 of 22 (91%) are currently exempt** per CCAD's TY2026 Absolute Exemption List -- a sharp
  contrast to Dallas County (wave 1), where only 11 of 132 (8%) showed an active exemption. Collin's
  HFC deals are recent (16 of 20 exempt parcels are 2024-2025 acquisitions) and appear to have moved
  through CCAD's exemption-application process quickly.
- **The Riley** (Garland HFC, Richardson) is the one still-HFC-owned parcel with **no exemption ever
  granted** -- 2+ years of ownership, still fully taxable. Worth flagging for the TDHCA §394.9027
  audit-filing cross-check (Method 1) once that data is available.
- **Hathaway at Willow Bend** (Pecos HFC, Plano) already left the HFC structure entirely via sale on
  2026-06-24, well ahead of the 2027 cliff -- a genuine pre-2027 unwind, not a projection.

## Top gaps / blockers

1. **TY2026 is CCAD's Preliminary roll, not yet ARB-certified** as of the 2026-07-11 data pull.
   Final certification (typically late July) could still change exemption status or appraised
   values for any of the 20 currently-exempt parcels, especially the 16 whose exemption first
   appears this year.
2. **CCAD's bulk-roll `currValAssessed` field does not net out the HFC exemption** for any parcel
   checked (confirmed against known 100%-exempt government buildings) -- "currently exempt" in this
   census relies on CCAD's separately-published Absolute Exemption List instead, which is itself a
   distinct extract that can lag real-time ownership changes (see the Hathaway finding above).
3. **Two seed rows rest on a disclosed bucket-pairing, not an independent match:** `TX-37-8327` and
   `TX-37-8328` (Cameron County HFC, "Dallas") were paired to the two highest-value parcels in a
   4-parcel same-deed-batch cluster ("Oaks of North Dallas Apartments" + "4804 Haverwood
   Apartments") -- Collin County Clerk grantor/grantee index (Method 3) would be needed to confirm
   which seed row is which parcel. `TX-37-3160` (Pecos HFC, "Plano") was a best-effort pick between
   two same-city, same-era candidates (The Dayton vs. Hathaway at Willow Bend); the non-selected
   candidate is captured separately as `TX-NEW-COLLIN-9`.
4. **`first_exempt_tax_year` is a genuine bracket, not a guess, but is coarse for 16 records:**
   because the only two available roll years spanning the transition are TY2025 (certified,
   pre-exemption) and TY2026 (Preliminary, first showing the exemption code), the true first-exempt
   year for those 16 could in principle be pinned more precisely once TY2026 is certified.
5. **`annual_exemption_value_est` is a rough estimate** using TY2025 published entity tax rates
   (county + community college + school district + city; TIF-zone entities excluded) applied to the
   TY2026 appraised value -- TY2026 rates had not yet been adopted as of the data pull, and this does
   not model any prior-year proration.
6. **Loan/servicer/securitization data** (schema's `loan.*` block) was not researched -- out of
   reach of free CAD/court sources for this pass.
7. **The Riley's non-exemption cause is undetermined** -- CCAD's public data cannot distinguish "no
   application filed," "application denied," or a TDHCA §394.9027 non-filing; would need a TPIA
   request (Method 1) or CCAD open-records request to resolve.
8. **Ground-lease commencement dates** for the three ground-leased deals (380 Villas, Palencia
   Apartments, Adriane) are approximated from the seed's stated lease-expiration dates minus the
   99-year term; not independently confirmed against a recorded Memorandum of Ground Lease
   (Method 3).
