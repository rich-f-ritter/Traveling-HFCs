# Montgomery County — Traveling HFC/PFC Census (Phase 3)

**Scope:** 5 Matrix-seed rows for Montgomery County + 1 expansion property discovered via a
Montgomery CAD (MCAD) GIS sweep + Montgomery County Tax Office owner-name sweep. 4/5 seed
rows carry a confirmed CAD account/address; 1 could not be isolated to a specific parcel from
free public data.

**Total appraised value captured (6 properties): $202,800,000** (5 confirmed properties;
1 seed row — TX-62-940094, Houston HA/Spring — remains unmatched and contributes $0 to this total).

## Headline finding: none of the 5 confirmed properties are cleanly, fully exempt

Cross-referencing Montgomery County Tax Office (ACT) account detail against all 5 confirmed
accounts: **3 carry a `PRORATED-EXXV` exemption code** (Avaya Kingwood/Houston HA, Woodland
Landings/Pleasanton HFC, Porterwood Apartments/Pecos HFC — new find) meaning the exemption
began *partway through* tax year 2025 and only a portion of value is currently sheltered
(e.g. Woodland Landings: $54.2M of its $66.0M market value is exempt, but $11.75M remains
taxable and a real $185,798 levy was billed and paid for TY2025). **The other 2 — both
Maverick County HFC's Woodlands parcels — carry NO exemption at all**: Exemption Value $0.00,
full market value taxable, full levy billed and paid. This mirrors the Dallas census finding
that most HFC/PFC-owned parcels are not cleanly exempt on the current roll; here the pattern
is more granular (partial/prorated rather than binary exempt/taxable).

## New find: Pecos HFC's Montgomery footprint (Porterwood Apartments, Porter, TX)

Pecos HFC — the single largest sponsor statewide (126 seed properties) — was not represented
in Montgomery's 5 seed rows. A direct owner-name search on the Montgomery County Tax Office
turned up **Porterwood Apartments** (24270 FM 1314 Rd, Porter, TX 77365; 136 units, built
1984; account 0004250002900), a fee-flip/ground-lease structure where Pecos HFC holds the
land account (with the improvement value bundled into the same billing account, prorated-
exempt for TY2025) while MCAD's GIS layer still shows the improvement segment attributed to
"PORTERWOOD APARTMENTS LLC" — a stale ownership label relative to the Tax Office's current
billing record. New census_id: `TX-NEW-MONTGOMERY-1`.

## Method

1. **MCAD's SPA property-search portal (mcad-tx.org / esearch.mcad-tx.org) could not be used
   as a free source this pass.** It runs on a TrueProdigy backend requiring an authenticated
   session; the anonymous/guest token obtainable via the public office-lookup + auth-token
   flow (`prod-container.trueprodigyapi.com/trueprodigy/publicportal/auth/token`) carries only
   `"Create User"` and `"Prodigy Public Portal - Legal Statement"` modules and returns
   `403 User is not authorized for ['Prodigy Public Portal']` on the actual property-search
   endpoint. MCAD's "Appraisal Data Exports" page is a client-rendered page with no visible
   free/paid bulk-file disclosure reachable without the same authenticated session.
2. **Pivoted to two other free MCAD/Montgomery County sources that ARE openly queryable:**
   - **MCAD Tax Parcel View**, a public ArcGIS FeatureServer maintained by Montgomery County
     GIS from MCAD's own data (`services1.arcgis.com/PRoAPGnMSUqvTrzq/arcgis/rest/services/
     Tax_Parcel_view/FeatureServer/0`), queryable with a plain attribute `WHERE` clause — no
     auth, no bulk download needed. Fields: `ownerName`, `situs`, `exemptions`, `stateCd`,
     `imprvMainArea`, `legalDescription`, `imprvActualYearBuilt`. Ran a county-wide sweep for
     `ownerName LIKE '%HOUSING FINANCE%' / '%PUBLIC FACILITY%' / '%HOUSING AUTHORITY%' / '%HFC%'
     / '%PFC%'` plus each of the 13 verified sponsor names individually (172-row raw result set,
     hand-filtered for false positives such as "IHFC Texas LLC," "Idaho Housing & Finance
     Association," and personal surnames "Garland"/"Rosenberg"/"Maverick").
   - **Montgomery County Tax Office** (`actweb.acttax.com/act_webdev/montgomery`, run by
     Appraisal & Collection Technologies) — a free, server-rendered owner-name search
     (`showlist.jsp`, prefix match on "Last Name First") returning account number, CAD
     reference, gross/land/improvement value, exemption code, and (via the "Exemption and Tax
     Rate Information" link) a per-taxing-unit jurisdiction breakdown that exposes the
     `PRORATED-EXXV` mechanic and lets `first_exempt_tax_year` and a modeled
     `annual_exemption_value_est` be derived. Ran a prefix search for each of the 13 verified
     sponsor names.
3. Cross-referenced hits against the 5 Montgomery seed rows by sponsor + city; used public
   apartment-listing sites (Lynd/Hilltop/29th Street Capital/Apartments.com/HAR.com) only to
   corroborate property names/unit counts, never as the ownership source of record.
4. No bulk files were downloaded for Montgomery (both sources used are live query APIs), so
   there is nothing to delete for this county.

## Table: all 6 properties

| census_id | sponsor | property | city | CAD account | units | appraised value | exempt? | kill date |
|---|---|---|---|---|---|---|---|---|
| TX-62-4408 | Houston Housing Authority | Avaya Kingwood (fka Virtual Living at Kingwood) | Kingwood | 0004050100903 | — | $34,400,000 | Partial (PRORATED-EXXV) | none (Ch.392) |
| TX-62-940094 | Houston Housing Authority | *(unresolved — no Montgomery match)* | Spring | — | — | — | ? | none (Ch.392) |
| TX-63-3939 | Maverick County HFC | Grove at Sterling Ridge | The Woodlands | 0004990000129 | — | $44,000,000 | No | 2027-01-01 |
| TX-63-2255 | Maverick County HFC | Montfair at The Woodlands (now Evergreen at Sterling Ridge) | The Woodlands | 0097169900700 | 310 | $44,750,000 | No | 2027-01-01 |
| TX-63-4733 | Pleasanton HFC | Woodland Landings | Magnolia | 0005460004200 | — | $66,000,000 | Partial (PRORATED-EXXV) | 2027-01-01 |
| TX-NEW-MONTGOMERY-1 | Pecos HFC | Porterwood Apartments | Porter | 0004250002900 | 136 | $13,650,000 | Partial (PRORATED-EXXV) | 2027-01-01 |

*"Exempt?" reflects the Montgomery County Tax Office's TY2025 certified account status.*

## By sponsor

| Sponsor | Records (seed+new) | Appraised value | Currently exempt (any portion) |
|---|---|---|---|
| Maverick County HFC | 2 | $88,750,000 | 0 |
| Pleasanton HFC | 1 | $66,000,000 | 1 (partial/prorated) |
| Houston Housing Authority | 2 (1 matched) | $34,400,000 | 1 (partial/prorated) |
| Pecos HFC | 1 (new) | $13,650,000 | 1 (partial/prorated) |

No Cameron County HFC, La Villa HFC, Edcouch Community HFC, Garland HFC, Texas Essential
Housing PFC, Rosenberg HA, Plano HA, San Benito HA, or Cameron County HA properties were found
in Montgomery County via either free source (explicit prefix/substring searches on all 13
verified sponsor names against both the MCAD GIS layer and the Tax Office all returned zero
matches beyond the 4 sponsors above).

## Litigation flags

None of Montgomery's properties are individually named in the litigation the task flagged
(that litigation — Williamson CAD v. Texas Essential Housing PFC and Williamson County v.
Cameron County HFC — concerns Williamson County properties; see `county_williamson.md`).
Sponsor-wide litigation (Haltom City v. Pecos HFC, Missouri City v. Maverick County HFC, Bexar
AD suit, TWHC HB21 constitutional challenge, Hays Co. TRO) is noted on each record's
`litigation_flags` per Phase-1's sponsor profiles but is not property-specific to Montgomery.

## Top gaps / blockers

1. **MCAD's own property-search SPA is not usable as a free anonymous source.** Its
   TrueProdigy backend gates the actual property-search endpoint behind a portal-module grant
   that the public/guest auth-token flow does not carry (`403` observed). All Montgomery data
   in this file instead comes from MCAD's public ArcGIS GIS layer (which lacks appraised-value
   and unit-count fields) cross-referenced with the Montgomery County Tax Office's independent
   billing system (which has values but not units). Neither publishes apartment unit counts,
   so all `units` fields are either null or sourced from third-party listing sites, disclosed
   per-record.
2. **TX-62-940094 (Houston HA, Spring) has no confirmed match.** An owner-name prefix search
   for "HOUSTON HOUSING AUTHORITY" on the Tax Office returned exactly one account statewide
   (the Kingwood property already matched to TX-62-4408); the GIS sweep likewise found only
   that one HHA parcel. Spring, TX addresses commonly straddle the Harris/Montgomery line —
   this parcel may actually sit in Harris County despite the seed's county tag, or the deal
   may not have resulted in a Montgomery-recorded fee-title change. Unresolved from
   Montgomery-only free sources.
3. **`PRORATED-EXXV` exemption codes give a tax year (2025) but not an exact effective date**,
   and the derived `annual_exemption_value_est` figures are a modeled estimate (current
   taxable-portion levy × exempt/taxable ratio from the Tax Office's own 2025 jurisdiction
   table), not an official published foregone-tax figure.
4. **Seed-row-to-parcel pairing for both Maverick County HFC Woodlands rows (TX-63-2255,
   TX-63-3939) is a best-effort bucket assignment** by role language (Ground Leasor → Grove at
   Sterling Ridge; Additional owner → Montfair/Evergreen at Sterling Ridge), not independently
   verified against a recorded deed. A Montgomery Co. Clerk grantor/grantee search (Method 3)
   would be needed to confirm.
5. **Loan/servicer/securitization data was not researched** — out of reach of the free sources
   used this pass.
