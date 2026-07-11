# Fort Bend County -- Traveling HFC/PFC/HA Census (Phase 3)

**Scope:** 9 Matrix-seed rows for Fort Bend County across 4 verified sponsors (Houston Housing
Authority, Maverick County HFC, Pleasanton HFC, Rosenberg Housing Authority) + 5 expansion
properties discovered via a Fort Bend CAD (fbcad.org) free owner-name sweep. 6/9 seed rows carry
an FBCAD-confirmed account; 3 (2 Houston HA, 1 Rosenberg HA/Stafford) could not be isolated to a
specific parcel from free public data.

**Total appraised value captured (11 properties, 12 real-property FBCAD accounts): $402,521,002**
(plus $1,153,140 across 3 small linked personal-property/FF&E accounts, not included in the
headline total). **6 of 11 properties are currently exempt on the TY2026 certified roll; 5 remain
fully taxable** despite sponsor-of-record ownership.

## Headline findings

1. **The Missouri City v. Maverick County HFC suit is about a DIFFERENT property than the one
   most easily found by name.** The lawsuit (Fort Bend 268th Dist. Ct., filed 1/24/2025) concerns
   **The Ranch at Sienna** (8811 Sienna Springs Blvd, Missouri City) — not the similarly-named
   **Ravella at Sienna** (5330 Sienna Pkwy), which was a separate, *abandoned* 2024 deal by a
   different entity ("Fort Bend County Housing Finance Corporation," per Houston Public Media).
   FBCAD's TY2023-2026 rolls show **neither property was ever transferred to any HFC**: Ranch at
   Sienna has been owned by "Ranch@Sienna Equity Partners Property LLC" continuously, and Ravella
   at Sienna by "Orion Ravella Property De LLC" continuously. This is strong corroborating evidence
   that the City's TRO blocked the Ranch at Sienna closing before it could record, and that the
   Ravella deal never proceeded past the drop announced in mid-2024. **No property record was
   created for either** — there is no CAD ownership evidence to support one, consistent with this
   project's "never guess" rule. Maverick County HFC's *only* confirmed Fort Bend holding is a
   separate, under-construction Rosenberg property ("Vero Sade," TX-63-1358163).
2. **Most Rosenberg-sponsored Fort Bend deals are DIRECT Housing Authority ownership, not routed
   through the affiliated PFC.** Phase 1 assumed "Rosenberg HA deals ride on affiliated PFCs
   (HB2071 regime)." FBCAD's owner-name sweep found 8 Rosenberg-sponsored properties in Fort Bend:
   **6 are titled directly to "Housing Authority Of The City Of Rosenberg" (Ch.392, §392.005, no
   statutory cliff at all)**, and only **2 are titled to the Rosenberg Housing Authority Public
   Facility Corporation** (Ch.303, HB2071 grandfather regime, §303.021(d) boundary risk on its
   2025 acquisitions). This matters because it changes the kill regime analysis per property —
   see the table.
3. **Exemption status is mixed, not automatic.** 6 of 11 FBCAD-matched properties are exempt
   (Real Exempt) on the TY2026 roll; the other 5 — including the Maverick HFC property under
   construction, the RHAPFC's two 2025 acquisitions, the Waterview (Rosenberg HA, closed
   2/26/2026), and Royal Sienna Plantation (Pleasanton HFC, in Missouri City) — remain **fully
   taxable** (Real Apartment/Real Land class, no exemption code) despite sponsor-of-record
   ownership. Royal Sienna Plantation's persistent taxable status, specifically inside Missouri
   City, lines up with Phase 1's note that Missouri City is one of the jurisdictions where an
   injunction against Pleasanton HFC's appeals "already STANDS."
4. **One property (Willow Park Apartments, Houston HA) doesn't fit the traveling-shell pattern at
   all.** It has been 100%-HHA-owned and tax-exempt continuously since at least TY2018 — years
   before the 2021-25 vintage of ground-lease "fee-flip" deals this census otherwise tracks, and
   with no private LLC ever in its FBCAD title chain. It reads as an authentic, older HHA
   affordable-housing asset. Flagged `in_target_set: false`.

## Table: all 14 records (9 seed + 5 expansion)

| census_id | sponsor | tier | property | city | FBCAD account(s) | units | appraised value | TY26 exempt? | first exempt yr | kill date |
|---|---|---|---|---|---|---|---|---|---|---|
| TX-63-1358163 | Maverick County HFC | 1 | Vero Sade | Rosenberg | R540253 | 310 | $24,000,000 | N | — | 2027-01-01 |
| TX-63-3158 | Pleasanton HFC | 1 | Villas at River Park West | Richmond | R331334 | 252 | $35,725,441 | Y | 2026 | 2027-01-01 |
| TX-NEW-FORTBEND-1 | Pleasanton HFC | 1 | Royal Sienna Plantation | Missouri City | R489540 | 330 | $56,475,767 | N | — | 2027-01-01 |
| TX-63-3263 | Rosenberg HA (direct) | 3 | The Addison at Sugar Land | Sugar Land | R302075 | 280 | $49,186,268 | Y | 2026 | — (no cliff) |
| TX-63-334 | Rosenberg HA | 3 | *(unresolved — Stafford)* | Stafford | — | — | — | ? | — | — (no cliff) |
| TX-63-8200 | Rosenberg HA (direct) | 3 | The Waterview | Richmond | R484621 | 295 | $45,164,643 | N | — | — (no cliff) |
| TX-63-4944 | Rosenberg HA (direct) | 3 | The Retreat @ Riverstone | Sugar Land | R418163 | 249 | $51,627,706 | Y | 2024 | — (no cliff) |
| TX-63-939655 | Rosenberg HA (direct) | 3 | Haven at Bellaire | Richmond | R487824 | 297 | $37,365,861 | Y | 2026 | — (no cliff) |
| TX-NEW-FORTBEND-2 | Rosenberg HA (direct) | 3 | The Trestle | Missouri City | R111856 | — | $21,724,017 | Y | 2024 | — (no cliff) |
| TX-NEW-FORTBEND-3 | Rosenberg HA PFC (RHAPFC) | 3 | *(unnamed)* | Richmond | R538097 / R538098 | — | $20,501,832 | N | — | — (no cliff, §303.021(d) risk) |
| TX-NEW-FORTBEND-4 | Rosenberg HA PFC (RHAPFC) | 3 | Hanover Lakemont | Richmond | R313610 | 360 | $42,316,919 | N | — | — (no cliff, §303.021(d) risk) |
| TX-63-1274045 | Houston HA | 3 | *(unresolved)* | Richmond | — | — | — | ? | — | — (no cliff) |
| TX-63-1418663 | Houston HA | 3 | *(unresolved)* | Richmond | — | — | — | ? | — | — (no cliff) |
| TX-NEW-FORTBEND-5 | Houston HA | 3 | Willow Park Apartments | Missouri City (unincorp.) | R302037 | 260 | $18,432,548 | Y | 2018 | — (no cliff; not in target set) |

*TY26 exempt column: Y = FBCAD "Real Exempt" property-type class in effect for tax year 2026; N =
"Real Apartment"/"Real Land" class (fully taxable) despite sponsor-of-record ownership; ? =
ownership/exemption status not resolved to a specific parcel.*

## By sponsor

| Sponsor | Species/statute | Records (seed+new) | With FBCAD account | Appraised value | Currently exempt (TY26) |
|---|---|---|---|---|---|
| Rosenberg Housing Authority (direct) | HA / Ch.392 | 6 | 5 | $205,068,495 | 4 of 5 |
| Rosenberg Housing Authority Public Facility Corporation | PFC / Ch.303 | 2 | 2 | $62,818,751 | 0 of 2 |
| Pleasanton Housing Finance Corporation | HFC / Ch.394 | 2 | 2 | $92,201,208 | 1 of 2 |
| Maverick County Housing Finance Corporation | HFC / Ch.394 | 1 | 1 | $24,000,000 | 0 of 1 |
| Houston Housing Authority | HA / Ch.392 | 3 | 1 | $18,432,548 | 1 of 1 |

## Method

1. **Seed**: filtered `data/seed_properties.json` to `property_county == "Fort Bend"` -> 9 rows
   across 4 verified sponsors (Houston HA, Maverick County HFC, Pleasanton HFC, Rosenberg HA).
2. **FBCAD owner search**: Fort Bend CAD's public search front-end (`esearch.fbcad.org`) is a
   BIS-Consulting/TrueAutomation platform (same family as Bexar/Dallas's TrueAutomation, different
   vendor skin). It has no advertised bulk-roll download; free access is via its keyword
   owner/address/DBA search, which resolves to a JSON API
   (`/Search/SearchResults?keywords=<term>&isArb=false`) once the UI's request pattern is
   reverse-engineered from its client-side JS. Queried each of the 4 verified sponsor names, plus
   broad sweeps on `HOUSING FINANCE CORPORATION` and `PUBLIC FACILITY CORPORATION`, plus the other
   9 sponsors in `data/sponsors.json` (Cameron County HFC/HA, La Villa HFC, Edcouch HFC, Garland
   HFC, Pecos HFC, Texas Essential Housing PFC, Plano HA, San Benito HA) — **none of the other 9
   sponsors hold any Fort Bend County property** per this sweep (all returned 0 results).
3. **Per-account history**: for every FBCAD account found, pulled the TY2018-2026 year-toggle
   (`/Property/View/{accountId}?year=YYYY`) to get owner-of-record, FBCAD's property-type class
   (`Real Exempt` vs. `Real Apartment`/`Real Land`/`Real Commercial`, which doubles as a reliable
   exemption-status proxy — no separate exemption-code field is exposed on this platform), and
   appraised value for each year — the first year the class flips to `Real Exempt` is recorded as
   `exemption.first_exempt_tax_year`.
4. **Seed-row pairing**: matched by exact property name + unit count in the seed's own
   `sale_comment` text (Waterview, Haven at Bellaire), by independently-confirmed partner-name news
   coverage (Hilltop Residential/Villas at River Park West via Hilltop's own blog; Catalyst Equity
   Partners/Addison at Sugar Land via REBusinessOnline; Vero Sade/Maverick HFC via the DBA field
   itself), and by process-of-elimination for the one remaining Sugar Land Rosenberg-HA row
   (Retreat @ Riverstone) — flagged single-source, no independent partner-name corroboration.
5. **Litigation cross-check**: web-searched the Missouri City v. Maverick County HFC suit (Houston
   Public Media, Eagle Pass Business Journal) and confirmed via FBCAD's own multi-year roll that
   neither Ranch at Sienna nor Ravella at Sienna ever recorded to any HFC.
6. **Bulk downloads**: none were used — FBCAD's public GIS/Open Data Hub
   (`fbcad-open-data-hub-fortbend.hub.arcgis.com`) offers parcel/spatial layers but no owner-level
   bulk roll export comparable to Dallas/Bexar's `DataProducts.aspx` ZIP files, so this county was
   worked entirely through the free live-search API (no bulk file was downloaded, so there was
   nothing to delete per the disk-conservation constraint).

## Top gaps / blockers

1. **3 of 9 seed rows have no FBCAD match at all**: the Stafford Rosenberg-HA row (partner "Madera
   Companies" does not appear anywhere on the FBCAD roll, and no Stafford apartment complex is
   HA/PFC-owned), and both Houston HA rows (only one HHA-owned Fort Bend account exists anywhere —
   Willow Park Apartments — and its TY2018 exemption start date and 100%-outright-ownership profile
   don't match either row's ~2022-origination 99-yr/75-yr ground-lease structure). All three would
   need a Fort Bend County Clerk grantor/grantee search (Method 3) or a TPIA to the respective
   sponsor to resolve.
2. **Exemption is absent on 5 of 11 matched properties** despite sponsor ownership — consistent
   with the pattern Dallas/Bexar also found (pending applications, non-filed §394.9027/§303.0426
   TDHCA audits, or active litigation). Not resolvable from the roll alone; TDHCA's compliance
   monitoring pages were still "TBD" as of 7/11/2026 per `docs/phase1_verdict.md`.
3. **`annual_exemption_value_est` is null on every record** — would require FBCAD's per-jurisdiction
   TY2026 tax rates (not pulled this pass) applied to each appraised value.
4. **2 properties have no confirmed unit count** (The Trestle; the unnamed RHAPFC Andado Lane
   property) — FBCAD does not publish a units field on this platform (unlike Dallas's bulk
   COM_DETAIL export), so unit counts throughout this file are sourced from public
   apartment-listing sites or news coverage, not FBCAD itself; flagged per-record.
5. **The Missouri City v. Maverick County HFC docket** (Fort Bend 268th Dist. Ct., filed
   1/24/2025) was not pulled directly — case number and current status (TRO vs. permanent
   injunction vs. dismissal) inferred only from press coverage plus the FBCAD ownership-history
   proxy. A Fort Bend District Clerk docket search would firm this up.
6. **`instrument_extractions`, `structure_dates` (MOU/SWD/ground-lease recording refs), `covenant`
   (set-aside %/AMI band)** — not pursued this pass; all `swd_to_sponsor_date` values are inferred
   from year-over-year CAD ownership snapshots (which bracket a tax year, not an exact recording
   date) rather than from an actual recorded instrument.
7. **`loan`/CMBS-CLO surveillance** — only the Vero Sade construction lender (IBC Bank, per trade
   press) was found; no DBRS/Trepp/CRED iQ pull performed for the other 10 accounts.
