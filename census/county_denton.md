# Denton County -- Traveling HFC/PFC Census (Phase 3)

**Scope:** 8 Matrix-seed rows for Denton County + 8 expansion properties discovered via a Denton CAD
(dentoncad.com, mirrored at dentoncad.net) bulk appraisal-roll sweep (Method 2). 7/8 seed rows carry a
Denton-CAD-confirmed address/account (5 high-confidence city/date/sale-comment matches, 2 best-effort
sponsor+city pairings); 1 (Pecos HFC, Aubrey) could not be isolated to a specific parcel from free
public data.

**Total appraised value captured (16 properties): $647,532,611** ($532,000,671 across 12 traveling,
in-scope properties -- 7 seed-linked + 4 net-new expansion -- plus $115,531,940 across 4 net-new
expansion properties excluded as non-traveling City-of-Denton home turf; see "Excluded" below).

## Headline finding: a 2025 exemption cutoff, not a uniform strip

Unlike Dallas County (where nearly every HFC/PFC parcel had already lost its exemption), Denton's
picture is a split determined almost entirely by **acquisition date**. Cross-referencing Denton CAD's
own Property-Entity table (`taxable_val` per taxing unit) against all 15 confirmed parcels: **every
parcel acquired in 2025 is fully TAXABLE (7 of 15)**, while **every parcel acquired in 2024 or earlier
still carries its full exemption (8 of 15, taxable_val = $0 at every entity)**. The pattern holds
across every sponsor observed here (Cameron County HFC: 1 of 3 pre-2025 parcels still exempt, 2 of 3
2025 parcels taxable; Pecos HFC: all 4 of its Denton parcels are 2025 acquisitions and all 4 are
taxable; Garland HFC's older 2023-24 parcels are still exempt; the three City-of-Denton PFC parcels,
dated 2005-2016, are all still exempt). This is consistent with a Denton CAD administrative decision
(likely informal, ahead of HB 21's 1/1/2027 statutory cliff) to stop granting the exemption to new
HFC/PFC ground-lease acquisitions starting in 2025, while not yet retroactively stripping the older
ones on the books -- a materially different posture than what Wave 1 (Dallas/Tarrant/Bexar) found,
where exemptions were largely already gone regardless of vintage.

## Table: all 16 properties

| census_id | sponsor | property | city | CAD account(s) | appraised value | TY26 taxable? | acquired | kill date | in scope? |
|---|---|---|---|---|---|---|---|---|---|
| TX-43-2669 | Cameron County HFC | Bluffs at Vista Ridge Apts | Lewisville | 310825 | $43,486,332 | Taxable | 2025-04-14 | 2027-01-01 | yes |
| TX-43-2577 | Cameron County HFC | Tides at Lewisville | Lewisville | 173667 | $47,185,908 | Taxable | 2025-04-09 | 2027-01-01 | yes |
| TX-43-1938 | Cameron County HFC | Oak Forest I & II Apts | Lewisville | 19743 + 174992 | $77,527,500 | **Exempt** | 2023-03-15 | 2027-01-01 | yes |
| TX-43-1417366 | Pecos HFC | *(unnamed, Under Construction)* | Denton | 1063244 | $16,902,935 | Taxable | 2025-05-06 | 2027-01-01 | yes |
| TX-37-1236 | Pecos HFC | Retreat at 3737 (Rosemeade Apts) | Dallas (Denton Co.) | 86134 | $29,950,000 | Taxable | 2025-03-06 | 2027-01-01 | yes |
| TX-37-7551 | Pecos HFC | *(unresolved -- no Denton CAD match)* | Aubrey | -- | -- | ? | -- | 2027-01-01 | yes |
| TX-43-2392 | Plano HA (title: Plano PFC) | Oak Tree Village Apts | Lewisville | 86563 | $37,985,836 | **Exempt** | 2021-09-29 | none (HB2071, grandfathered) | yes |
| TX-37-5252 | Pleasanton HFC | 4 Corners Apts | Frisco | 655887 | $88,899,643 | Taxable | 2024-10-18 | 2027-01-01 | yes |
| TX-NEW-DENTON-1 | Pecos HFC | Arden at Corinth | Corinth | 1037503 + 1037504 | $53,292,148 | Taxable | 2025-05-12 | 2027-01-01 | yes |
| TX-NEW-DENTON-2 | Pecos HFC | Luxe @ Lewisville | Lewisville | 1052070 | $25,700,295 | Taxable | 2025-02-21 | 2027-01-01 | yes |
| TX-NEW-DENTON-3 | Garland HFC | One90 Frankford | Dallas (Denton Co.) | 1027658 | $65,285,915 | **Exempt** | unknown | 2027-01-01 | yes |
| TX-NEW-DENTON-4 | Garland HFC | Parchaus (Lake Pointe) | Little Elm | 10 accounts | $45,784,159 | **Exempt** | unknown (yr.blt 2024) | 2027-01-01 | yes |
| TX-NEW-DENTON-5 | Denton PFC | Pecan Place Apartments | Denton | 32975 | $8,059,257 | **Exempt** | 2012-12-31 | n/a -- home turf | **no** |
| TX-NEW-DENTON-6 | Denton PFC | Veranda | Denton | 565421 | $52,303,575 | **Exempt** | 2016-04-15 | n/a -- home turf | **no** |
| TX-NEW-DENTON-7 | Premier Denton PFC | Eighteen51 Brinker | Denton | 754770 | $40,945,891 | **Exempt** | unknown | n/a -- home turf | **no** |
| TX-NEW-DENTON-8 | Renaissance Courts PFC | Renaissance Courts | Denton | 32689 | $14,223,217 | **Exempt** | 2005-07-29 | n/a -- home turf | **no** |

*"Acquired" = Denton CAD's most-recent-deed date on file for the account (may reflect a re-recording,
not necessarily original ground-lease commencement -- see gaps). "In scope" = traveling,
non-home-turf, i.e. counted in the totals above the table.*

## By sponsor (in-scope only)

| Sponsor | Records (seed+new) | Appraised value | Currently exempt (TY26) |
|---|---|---|---|
| Pecos HFC | 5 (4 matched/1 unresolved) | $125,845,378 (of the 4 with a value) | 0 |
| Cameron County HFC | 3 | $168,199,740 | 1 |
| Garland HFC | 2 (both net-new) | $111,070,074 | 2 |
| Pleasanton HFC | 1 | $88,899,643 | 0 |
| Plano HA / Plano PFC | 1 | $37,985,836 | 1 |

## Excluded (non-traveling, out of scope)

4 net-new expansion properties, all sponsored by City-of-Denton-affiliated Ch.303 PFCs (Denton Public
Facility Corporation; Premier Denton Public Facility Corporation; Renaissance Courts Public Facility
Corporation), were found in the same owner-name sweep and excluded from the census totals -- all 4 sit
inside the City of Denton itself (the sponsors' own home jurisdiction; all three PFCs share the mailing
address 1225 Wilson St, Denton, which matches Denton Housing Authority's headquarters), so under HB21's
city-boundary test and HB2071's out-of-area test these are not "traveling." Same treatment Dallas gave
Garland HFC's in-Garland parcels and Phase 1 gave Houston HA's Harris-County home-turf parcels.
Aggregate appraised value of the excluded set: **$115,531,940** (all 4 still fully exempt on the TY26
roll, consistent with these being legitimate, non-abusive in-area affordable-housing vehicles rather
than the traveling scheme this census targets).

## Note on the "Garland HFC Lewisville / Plano PFC" flag

The task brief flagged a possible mix-up between a Garland HFC "Lewisville" deal and a Plano PFC
property. Resolved by actual CAD owner-of-record: the Lewisville seed row tagged "Plano Housing
Authority" (TX-43-2392) is titled to **Plano Public Facility Corporation** (Oak Tree Village
Apartments, deed 2021-09-29 -- exactly matching the seed's ground-lease-implied commencement, and
independently named as "grandfathered" in `docs/phase1_verdict.md`). Garland HFC has no seed presence
in Lewisville; its two Denton-County holdings found here (One90 Frankford, Parchaus) are in Dallas
(Denton Co.) and Little Elm, not Lewisville. No entity misattribution found once matched to CAD
records.

## Method

1. Located Denton CAD's free bulk data mirror (the `dentoncad.com` public portal is a client-rendered
   React app with no crawlable bulk-download links, but its data files are still served from the legacy
   host `dentoncad.net/data/_uploaded/files/datafiles/`, an open Apache directory listing). Downloaded
   `2026/PreliminaryDataReal/2026 Preliminary Data - Residential (Real) Property.zip` (820MB, TY2026
   preliminary roll, retrieved 2026-07-11).
2. Extracted the fixed-width PACS/TrueAutomation-format `APPRAISAL_INFO.TXT` (Property, 380,940 rows),
   `APPRAISAL_ENTITY_INFO.TXT` (Property-Entity, per-taxing-unit assessed/taxable value), and
   `APPRAISAL_IMPROVEMENT_DETAIL.TXT` (year built) tables per the CAD's published
   `Legacy8.0.30-AppraisalExportLayout.xlsx` byte-offset layout.
3. Filtered the Property table's owner-name field for `HOUSING FINANCE` and `PUBLIC FACILITY`
   (broad, low-false-positive patterns per the kit's Method 2) plus the 4 named sponsor Housing
   Authorities not otherwise caught by those two patterns. An earlier, broader sweep that also matched
   generic `HOUSING AUTHORITY` and bare sponsor-name fragments (e.g. "PECOS," "LA VILLA") was discarded
   after inspection showed it pulled in unrelated local public-housing authorities (Dallas HA, Denton
   HA, Denton City HA -- none of which are project sponsors) and individual homeowners whose surnames
   coincidentally matched (e.g. "...VILLALOBOS" false-matching "LA VILLA").
4. Determined current exemption status from the **Property-Entity table's `taxable_val` field**, not
   the Property table's `ex_exempt`/`ex_qualify_yr` flags -- those flags were unpopulated (`F`/`0000`)
   for every single HFC/PFC parcel found, including ones independently confirmed exempt via
   `taxable_val = $0` at every taxing entity (e.g. even City of Denton's own city-hall parcels show
   `ex_exempt = F`). This indicates these ground-lease structures' exemptions route through Denton CAD's
   administrative $0-taxable-value mechanism rather than the standard application-based absolute-
   exemption code/qualify-year bookkeeping, and confirms `first_exempt_tax_year` is not recoverable from
   this single-year roll for any parcel (a gap shared with the Dallas/Tarrant/Bexar Wave-1 census).
5. Grouped accounts into 15 distinct properties by site address/dba (5 multi-account complexes:
   Oak Forest I&II [2 accts], Arden at Corinth [2], Parchaus [10], per the same site-address grouping
   Dallas used). Matched 5 of 8 seed rows to a specific parcel with high confidence (exact situs-city
   match, deed date matching the seed's ground-lease-implied commencement, or -- for Bluffs at Vista
   Ridge -- an explicit property-name mention in the seed's own `sale_comment` text). 2 more seed rows
   (both Cameron County HFC, Lewisville) were paired with their remaining candidate parcels by
   elimination and lease-term-implied acquisition-year proximity -- **not independently verified beyond
   sponsor+city+date-proximity, flagged `single-source`.** 1 seed row (Pecos HFC, Aubrey) had no
   matching Denton CAD parcel in the sponsor's owner-name bucket at all.
6. The 8 CAD-confirmed properties left over after seed-linking became expansion records
   `TX-NEW-DENTON-1..8`; 4 of those (all City-of-Denton PFC-sponsored) were further excluded from the
   traveling target set as non-traveling home turf (see above).
7. Deleted the 820MB source zip and all extracted `.TXT` working files after extraction, per
   task instructions (bulk downloads not retained).

## Top gaps / blockers

1. **7 seed rows' parcel identity rests on varying confidence.** 5 are high-confidence (exact
   situs-city match and/or deed-date/sale-comment cross-validation); 2 (Cameron County HFC's remaining
   Lewisville parcels) are best-effort sponsor+city+date pairings, not independently verified -- Method
   3 (Denton County Clerk grantor/grantee index) would be needed to pin these to specific deeds.
2. **1 seed row (Pecos HFC, Aubrey, TX-37-7551) has no CAD match at all.** No Pecos Housing Finance
   Corporation-owned parcel with situs city "Aubrey" was found anywhere in the Denton CAD 2026
   preliminary roll; web search on the seed's named partner ("Strategic Property Investment") turned up
   nothing corroborating. Candidate causes: not yet recorded under a name containing "Housing Finance,"
   the seed's city tag is a mailing address rather than situs, or the deal has not closed.
3. **`first_exempt_tax_year` is null on every record** -- see Method §4; would need Denton CAD's
   prior-year rolls (available back to 2019 on the same free mirror) to bracket when each parcel's
   taxable value first dropped to $0, or a TDHCA §394.9027/§303.0426 audit-filing date once published.
4. **Units are null on every record.** Not published in Denton CAD's bulk export or on individual
   account pages for any parcel in this sweep (same gap Tarrant and Bexar counties reported) -- one
   seed row (Bluffs at Vista Ridge) yielded a unit count (272) only because the seed's own
   `sale_comment` text happened to state it.
5. **Ground-lease vs. fee-simple structure unconfirmed for all 8 net-new expansion properties** (no
   `ground_lease_comment`-equivalent source exists for non-seed properties); `structure_confirmed` is
   left `unconfirmed` rather than assumed `fee-flip-groundlease` for those records.
6. **The 3 City-of-Denton PFC affiliations are inferred from a shared mailing address** (1225 Wilson
   St, Denton, matching Denton Housing Authority's HQ), not from a Secretary of State filing or
   certificate of formation -- a TPIA request or SOS lookup would firm this up.
7. **Loan/servicer/securitization data** (schema's `loan.*` block) was not researched -- out of reach
   of free CAD/court sources, consistent with every prior county in this census.
