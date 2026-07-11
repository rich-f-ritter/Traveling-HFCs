# Harris County — Traveling HFC/PFC Census (Phase 3)

**Scope:** 88 Matrix-seed rows for Harris County + 19 expansion properties discovered via an HCAD
(hcad.org) bulk Property Data Export (Pdata) sweep (Method 2). 75/88 seed rows carry an
HCAD-confirmed account/address; 13 could not be isolated to a specific parcel from free public
data (mostly Under-Construction deals or a bucket where seed count exceeded HCAD candidates).

**Total appraised value captured (107 properties): $2,001,448,045** ($1,829,335,020 across the 75
seed-linked records with a value + $172,113,025 across the 19 net-new expansion records).

## Headline finding #1: a second Pecos-style mislabel, this time on Cameron County

The two Harris seed rows tagged sponsor **"Cameron County Housing Authority"** (Ch.392, Tier 3, no
cliff) — TX-63-3735 (Houston) and TX-63-403 (Stafford) — matched to HCAD accounts whose registered
mailing address is **"1327 E Washington Ave PMB 110, Harlingen, TX"**, identical to the address used
by more than a dozen confirmed **"Cameron County Housing Finance Corporation"** (Ch.394, Tier 1)
accounts elsewhere in this same sweep. No account anywhere on the Harris roll spells the owner name
out in full as "Cameron County Housing Authority" (San Benito/Brownsville) — the two matches are
truncated ("CAMERON COUNTY HOUSING" / "THE CAMERON COUNTY HOUSING") in HCAD's owner field. This is
the same pattern Phase 1 already found and resolved for Pecos (HA-labeled-but-actually-HFC), and it
directly answers Phase 1's flagged "Cameron County HA entity-identity gap" for Harris's 2 rows. Both
records are carried in this census as **Tier 1 / HFC / 2027-01-01 cliff** on this evidence, with a
`gaps` note recommending formal deed-level confirmation (Method 3) as the final word.

## Headline finding #2: HCAD's roll lags the actual exemption action — even on the reference specimen

The Sarah at Lake Houston (kit's own validation case, HCAD acct 1416560010001/-0002, Pleasanton HFC,
partner **ZaneCRE** — matched via the seed's `partners` field, confirming the method) exposes a
structural quirk: HCAD splits these ground-leased deals into a **land account** (mailto = the
sponsor, e.g. "PLEASANTON HOUSING FINANCE CORP") and a companion **improvement account**
(mailto = the *prior* borrower LLC, cross-referenced via "LAND\*"/"IMPS\*" tags in the legal
description). On both the 2025 certified and 2026 preliminary HCAD extracts, Sarah's land account
(1416560010001) still shows full **taxable** value ($58,104,208, state class B1), and its
improvement account (1416560010002) is classified exempt (X1) but carries **no posted value**
("All Values Pending") — despite the case study's own documentation of a $1,020,960 October-2025
retroactive exemption credit. HCAD's account-level roll processing lags the tax office's actual
billing/exemption action by at least one cycle. **This means owner-name sweeps like this one likely
undercount total appraised value** on properties where the improvement account hasn't yet been
reassigned to the sponsor's name — flagged as a systemic gap on every matched record.

## Headline finding #3: most Harris parcels are STILL not showing an exemption on the 2025 roll

Of the 94 matched HCAD accounts/groups with a determinable exemption status, only **28 show TY2025
taxable value = $0** (fully exempt); **66 are carried at full taxable value** despite
sponsor-of-record ownership. This matches the pattern the Dallas and other county passes found:
non-filing of the §394.9027 TDHCA compliance audit, pending applications on 2025 acquisitions, or
active litigation are all candidate causes, none confirmable from the roll alone.

## Table: sponsors captured

| Sponsor | Records (seed+new) | Appraised value captured | Currently exempt (of determinable) |
|---|---|---|---|
| Pecos Housing Finance Corporation | 34 | $781,549,503 | low |
| Pleasanton Housing Finance Corporation | 22 | $369,415,605 | low |
| Houston Housing Authority (local, traveling=no) | 15 | $53,708,106 | mixed |
| La Villa Housing Finance Corporation | 9 | $207,815,206 | low |
| Texas Essential Housing Public Facility Corporation | 8 | $141,503,109 | high |
| Maverick County Housing Finance Corporation | 7 | $193,290,576 | low |
| Cameron County Housing Finance Corporation (incl. 2 reclassified) | 6 | $107,298,473 | low |
| Edcouch Community Housing Finance Corporation | 6 | $146,867,467 | low |

Tier split: **Tier 1 (HFC, 2027-01-01 cliff) = 84 records**, **Tier 2 (TEHPFC, grandfathered
PFC, no cliff) = 8 records**, **Tier 3 (Houston HA, no statutory cliff) = 15 records**.

## Houston Housing Authority: local vs. traveling

All **15 of 15** Harris-seed Houston HA rows are flagged **traveling = no** (carried forward from
the seed's own classification, consistent with Phase 1's "~15 of 19 are Harris-County home-turf").
The HCAD owner-name sweep independently found **288 total Houston HA-owned Harris accounts** — 250
in the City of Houston itself, 22 with a blank postal city, and only 16 outside Houston (Humble 5,
Spring 4, Katy 3, Baytown 2, Missouri City 1, Friendswood 1) — all still inside Harris County and
therefore still "home turf" under Phase 1's characterization. Per the task's scope instruction,
**none of Houston HA's non-seed local portfolio was added as `TX-NEW-HARRIS` expansion** — those
deals are excluded as in-jurisdiction, same treatment the Dallas census gave Garland HFC's
home-city parcels. One seed row (TX-63-1155169, "Alexis Apartments," Spring — 102-unit leasehold to
Heritage Investments) matched by exact name/unit-count cross-reference to the seed's own
`sale_comment` text, validating the bucket-pairing method.

## Method

1. Located HCAD's Craft-CMS-backed Property Data Export API
   (`hcad.org/actions/hcad-pdata/default/get-property-downloads`) behind the public "Download
   Property Data" page — free, no Cloudflare gate (unlike search.hcad.org) — and pulled the **2025
   certified** roll: `Real_acct_owner.zip` (real_acct.txt, owners.txt, deeds.txt) and
   `Real_jur_exempt.zip` (jur_value.txt, jur_exempt.txt). Cross-checked the 2026 preliminary vintage
   for the Sarah specimen to confirm the roll-lag finding above.
2. Filtered `owners.txt`'s `name` field for our 8 Harris-relevant verified sponsors and their HCAD
   spelling variants/scrivener errors (e.g., "PECOS HOUSING FINAN CE CORPORATION", "MAVERICK COUNTY
   HOUSING FINANCE CORPORAT" [truncated]) — 376 matched accounts, of which 288 are Houston HA.
   Explicitly excluded look-alike LOCAL Harris entities that are not among our 13 sponsors:
   "HCHFC \*" (Harris County HFC's own landowner-LLC portfolio), "HOUSTON HOUSING FINANCE CORP"
   (the City of Houston's own HFC, distinct from Houston Housing **Authority**), "HARRIS COUNTY
   HOUSING AUTHORITY", "ALDINE/HOUSTON ISD PUBLIC FACILITY CORP", "WINROCK NORTH/SOUTH PFC",
   "LAKESIDE PLACE PFC" — all are Harris-local structures unrelated to the 13-sponsor roster.
3. Joined matched accounts to `real_acct.txt` (address, state class, values, `new_own_dt`,
   `yr_impr`), and to `jur_value.txt`/`jur_exempt.txt` for the Harris County taxing district (code
   `040`) to get true pre-exemption appraised value and exempt/taxable status (HCAD zeroes
   `tot_appr_val` on X1/X2-exempt accounts in `real_acct.txt`; the district-level `jur_value.txt`
   table carries the real appraised figure).
4. Grouped raw accounts into 96 distinct properties (84 non-HHA + 12 HHA-non-Houston) by common
   site address, parsing unit counts from HCAD's convention of appending the total-unit count as a
   trailing number on `site_addr_1` (validated against Sarah's known 350 units and Alexis's known
   102 units).
5. Matched seed rows to HCAD property groups: pinned 5 rows with independent corroboration (name,
   unit count, or mailing-address match — Sarah, Alexis, the merged Sterling Point/Milagro pair, and
   the 2 reclassified Cameron rows), then bucket-paired the remainder within
   (sponsor, property_city), sorted by descending appraised value — same disclosed-assumption method
   the Dallas census used. Leftover HCAD groups beyond seed count became `TX-NEW-HARRIS-1..19`.
6. **Deleted all downloaded HCAD bulk files** (~1.9 GB of zips/txt) after extraction to conserve
   session disk, per instructions.

## Top gaps / blockers

1. **HCAD's owner-of-record field lags the actual exemption/deed action** on ground-leased deals
   (land vs. improvement account split) — see Sarah finding above. Total appraised value for some
   properties in this census is likely an undercount (land-only) where the improvement account
   hadn't yet been reassigned to the sponsor as of the 2025/2026 extracts pulled.
2. **13 of 88 seed rows have no HCAD match** — concentrated in Edcouch+Houston (3 short), Houston
   HA+Spring (3 short) and +Katy (1 short) and +Cypress (1, zero HCAD candidates), La Villa+Kingwood
   (1, zero candidates), Pleasanton+La Porte (1, zero candidates), and TEHPFC+Houston (3 short).
   Some are Under-Construction deals not yet on the roll; others may sit under a prior-owner LLC
   name per finding #2.
3. **Cameron County HA reclassification (2 records) rests on a mailing-address match, not a deed.**
   Flagged high-priority for Method-3 (grantor/grantee index) confirmation, same as Phase 1 asked.
4. **Sterling Point / Milagro merger**: seed row TX-63-7604 describes two legacy properties (921-unit
   Sterling Point + 258-unit Milagro) merged under Pecos HFC; both HCAD accounts still carry separate
   parcels/names ("STERLING POINT" and "STERLING POINTII"). The larger is pinned to the seed row; the
   smaller is not separately broken out as an expansion (documented as a companion parcel instead).
5. **`first_exempt_tax_year` and `annual_exemption_value_est` are null on every record** — same gap
   as the Dallas pass; would require differencing against HCAD's free prior-year rolls and applying
   each taxing unit's adopted rate.
6. **66 of 94 status-determinable HCAD accounts show NO exemption in effect for TY2025** despite
   sponsor-of-record ownership — cause not determinable from the roll alone (Method 1's TDHCA
   audit-filing cross-check is the next step, same as every other county pass).
7. **Loan/servicer/securitization data** (schema's `loan.*` block) not researched — out of reach of
   free HCAD/court sources for this pass.
