# Williamson County — Traveling HFC/PFC Census (Phase 3)

**Scope:** 4 Matrix-seed rows for Williamson County (all Texas Essential Housing PFC) + 1
expansion property (Cameron County HFC) discovered via a WCAD Open Data owner-name sweep.
3/4 seed rows carry a confirmed CAD account/address; 1 could not be isolated to a specific
parcel from free public data.

**Total appraised value captured (5 properties): $203,750,000** (4 confirmed properties;
1 seed row — TX-36-2231, TEH PFC/Austin — remains unmatched and contributes $0 to this total).

## Headline finding: all 4 confirmed properties are fully taxable — none carry an exemption

Every one of the 4 confirmed Williamson accounts (3 Texas Essential Housing PFC + 1 Cameron
County HFC) shows **assessed value equal to full market value** on the certified 2025 roll,
and a targeted query of WCAD's own "Exemptions" open-data table returned **zero active
exemption records** for any of the four `propertyid`s. Despite sponsor-of-record ownership by
a Ch.303 PFC or Ch.394 HFC, none of Williamson's traveling properties are currently sheltering
any value from ad valorem tax — consistent with, and probably not unrelated to, the active
Williamson CAD litigation described below.

## Litigation — directly confirmed against specific properties

The task flagged two ongoing Williamson County disputes; both were confirmed and pinned to
specific properties in this pass:

- **Texas Essential Housing PFC v. Williamson CAD** (395th Judicial District Court): Cause No.
  **24-1698-C395** is styled *"Texas Essential Housing Public Facility Corporation Enclave La
  Frontera vs. Williamson Central Appraisal District"* — naming **Enclave at La Frontera**
  (2800 La Frontera Blvd, Round Rock; `TX-36-1968`) directly. Cause No. **24-0022-C395** is the
  companion/broader TEH PFC exemption dispute (Judge Ryan D. Larson; counsel Blake Wilson
  Stribling for TEHPFC, Eric J.R. Nichols for WCAD) — not independently confirmed from free
  sources which specific property(ies) it covers beyond TEHPFC generally, so it is flagged as
  possible/unconfirmed on Lakeside at La Frontera (`TX-36-2017`), the other Round Rock TEH PFC
  property in the same La Frontera master-planned area.
- **Williamson County v. Cameron County Housing Finance Corporation** (TRO, ~early March
  2025): per contemporaneous reporting (Texas Standard, 2025-03-11), the county sued to halt
  Cameron County HFC's acquisition of **two** Round Rock apartment complexes — **Siena Round
  Rock** and **The Sommery** — alleging exploitation of the out-of-jurisdiction HFC exemption
  loophole; County Judge Bill Gravell called it "one of the most egregious acts" he'd seen.
  WCAD's current roll confirms **Siena Round Rock** (6531 County Road 110; new expansion
  record `TX-NEW-WILLIAMSON-1`) as 100%-owned by Cameron County HFC. **The Sommery** (5540
  Sofia Pl, Round Rock), however, is currently owned by **"SOMMERY LOT 2 LP"** on WCAD's roll —
  not Cameron County HFC — indicating that leg of the acquisition did not close (plausibly
  halted by the March-2025 TRO). Not included as a census record; flagged here per the task's
  instruction to track this litigation.

## New find: Cameron County HFC's Siena Round Rock (Tier 1, faces the 2027 cliff)

Not present in the 4 TEH PFC-only Williamson seed rows. Found via a full-county WCAD
owner-name sweep. Unlike Williamson's TEH PFC properties (Tier 2, no 2027 cliff), Siena Round
Rock is Ch.394 HFC-owned and therefore subject to HB21 §13(i) — but its more immediate unwind
risk is the active county lawsuit above, which could force divestiture well before 2027.

## Method

1. **WCAD's own property-search portal (search.wcad.org) was not needed** — Williamson CAD
   publishes a genuinely free, no-login **Socrata open-data catalog** at `data.wcad.org`
   (50+ datasets: Owner, Property-Certified, Exemptions, Final Values, Sales, Improvements,
   etc.), queryable via a documented REST API (`data.wcad.org/resource/<id>.json` with
   Socrata `$where`/`$select`/`$group` query params). No bulk file download was required —
   this is a live query API, so there is nothing to delete for this county.
2. Queried the **Owner** dataset (`bbia-wsxs`) county-wide for
   `fullname LIKE '%HOUSING FINANCE%' OR '%PUBLIC FACILITY%' OR '%HOUSING AUTHORITY%' OR '%HFC%'
   OR '%PFC%'`, hand-filtered out false positives (Austin Housing Finance Corporation — not one
   of the 13 verified sponsors; Georgetown/Round Rock/Taylor/Granger local housing authorities;
   "HFC Investments Ltd" and "IHFC Texas LLC" — private companies, substring collisions).
   Followed up with explicit prefix searches for each of the 13 verified sponsor names
   individually to confirm completeness.
3. Joined matches against the **Property - Certified** dataset (`ai3c-c9pf`) for address,
   legal description, land/improvement/total market value, and against **Exemptions**
   (`nbn7-h4pp`) to confirm exemption status (all four properties: zero active-exemption rows).
4. Cross-referenced hits against the 4 Williamson seed rows by sponsor + city; used public
   apartment-listing sites (Lynd Management Group's own property pages, Apartments.com,
   ApartmentFinder) only to corroborate property names/unit counts, never as the ownership
   source of record. Confirmed the litigation-named properties via Trellis.law court-docket
   pages and a Texas Standard news article.

## Table: all 5 properties

| census_id | sponsor | property | city | CAD account | units | appraised value | exempt? | kill date |
|---|---|---|---|---|---|---|---|---|
| TX-36-2088 | Texas Essential Housing PFC | Legends Lake Creek | Austin | R392272 | 170 | $40,750,000 | No | none (Ch.303) |
| TX-36-2231 | Texas Essential Housing PFC | *(unresolved — no Williamson match)* | Austin | — | — | — | ? | none (Ch.303) |
| TX-36-1968 | Texas Essential Housing PFC | Enclave at La Frontera | Round Rock | R401785 | 411 | $68,000,000 | No | none (Ch.303) — under active litigation |
| TX-36-2017 | Texas Essential Housing PFC | Lakeside at La Frontera | Round Rock | R417224 | 366 | $64,000,000 | No | none (Ch.303) |
| TX-NEW-WILLIAMSON-1 | Cameron County HFC | Siena Round Rock | Round Rock | R599112 | 198 | $31,000,000 | No | 2027-01-01 — under active litigation (TRO) |

*"Exempt?" reflects WCAD's Exemptions dataset + assessed-vs-market-value check on the certified 2025 roll.*

## By sponsor

| Sponsor | Records (seed+new) | Appraised value | Currently exempt |
|---|---|---|---|
| Texas Essential Housing PFC | 4 (3 matched) | $172,750,000 | 0 |
| Cameron County HFC | 1 (new) | $31,000,000 | 0 |

No Pecos HFC, Pleasanton HFC, La Villa HFC, Edcouch Community HFC, Maverick County HFC,
Garland HFC, Houston Housing Authority, Rosenberg HA, Plano HA, San Benito HA, or Cameron
County HA properties were found in Williamson County (explicit prefix searches on all 13
verified sponsor names against the WCAD Owner dataset returned zero matches beyond the 2
sponsors above).

## Top gaps / blockers

1. **TX-36-2231 (TEH PFC, Austin) has no confirmed match.** WCAD's full-county owner sweep for
   "TEXAS ESSENTIAL HOUSING PUBLIC FACILITY CORPORATION" returned exactly 3 properties, all
   claimed by the other 3 Williamson seed rows. No 4th TEH PFC-owned property exists on the
   current WCAD roll. Possible explanations (unconfirmed): duplicate/second internal ID for
   the same physical property, an unclosed deal, or a since-transferred parcel. Would need
   Method 3 (Williamson Co. Clerk deed index) or a TDHCA PFC filing cross-check to resolve.
2. **Seed-row pairing of TX-36-1968/TX-36-2017 to Enclave vs. Lakeside at La Frontera is a
   best-effort match**, not independently verified beyond city+sponsor — Enclave was assigned
   by its direct name-match in the 24-1698-C395 docket; Lakeside by elimination.
3. **Whether Lakeside at La Frontera (TX-36-2017) is itself a named party to case 24-0022-C395**
   (vs. only Enclave to 24-1698-C395) was not confirmed — the full docket text was not fetched
   from a free source this pass; flagged as possible/unconfirmed litigation on that record.
4. **The Sommery's current disposition is a documented negative result, not a gap in coverage**
   — WCAD confirms a private LP (not Cameron County HFC) as owner of record, but *why* the
   deal didn't close (TRO-blocked vs. abandoned vs. still pending under a different structure)
   is not determinable from free sources.
5. **Unit counts are not published by WCAD's open data** (no dataset carries a bedroom/unit
   count field) — all `units` values are sourced from third-party listing sites, disclosed
   per-record.
6. **Loan/servicer/securitization data was not researched** — out of reach of the free sources
   used this pass.
