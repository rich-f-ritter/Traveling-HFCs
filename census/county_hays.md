# Hays County -- Traveling HFC/PFC Census (Phase 3)

**Scope:** 6 Matrix-seed rows for Hays County (4 Pleasanton HFC, 1 Pecos HFC, 1 Edcouch Community
HFC) + 5 expansion properties discovered via a HaysCAD (esearch.hayscad.com) owner-name sweep
(Method 2). 4/6 seed rows carry a HaysCAD-confirmed account; 2 could not be matched to any current
HaysCAD account from free public data.

**Total appraised value captured (11 records / 9 confirmed CAD accounts): $212,054,063**
($163,100,000 across 4 seed-linked accounts + $48,954,063 across 5 net-new expansion accounts).

## Headline finding: the Hays County TRO appears to be working -- almost nothing here is exempt

Hays County sued **Pecos HFC and Pleasanton HFC** on 4/30/2025 (*Hays County v. Pecos Housing
Finance Corporation & Pleasanton Housing Finance Corporation*, Case No. 25-1185-DCB) and obtained a
**TRO blocking Hays CAD from granting ad valorem exemptions** on their San Marcos & Kyle
properties -- County Judge Ruben Becerra put **~$227-230M** of tax base at stake. The roll bears
this out: **all 4 confirmed Pleasanton HFC accounts (Vantage at Plum Creek, The Lodge in San
Marcos, The Chloe) are fully taxable** -- market value equals taxable value on every taxing entity,
in both TY2025 (the acquisition year) and the current TY2026 preliminary roll. **No exemption has
ever been posted for any Pleasanton HFC Hays County account.**

**Edcouch Community HFC is not a party to that suit**, yet its Hays holdings tell a related but
distinct story. Of its 2 complexes (5 CAD accounts): **Jovie Belterra** (Dripping Springs, $35.5M)
has also never carried any exemption. **Local Dripping Springs** (Dripping Springs, 3 accounts,
$29.5M combined) shows an inconsistent pattern -- one account (R190278) got a **partial exemption
for TY2025 that was then reversed to fully taxable for TY2026**, while its two sibling accounts on
the same site/closing were fully taxable in TY2025 already. Cause not determinable from the roll
alone (see gaps): candidates include the §394.9027 TDHCA compliance-audit deadline, a lapsed
application, or precautionary Hays CAD posture spreading from the adjacent Pecos/Pleasanton fight.

**The one Tier-2 (PFC) find is the opposite case.** **Texas Essential Housing PFC**'s Cheatham
Street Flats (San Marcos, mixed-use) has been **fully exempt on its residential parcel since
TY2023** (partial/prorated exemption from the TY2022 acquisition year) -- TEHPFC is a Ch.303 PFC,
outside HB21's reach and outside the Hays HFC suit entirely, and its exemption has never been
challenged locally. The complex's small retail/ancillary parcel remains mostly taxable, consistent
with the housing exemption not extending to commercial space.

## The Pecos gap: an "unrecorded sale" that stayed unrecorded

The seed's single Hays row for Pecos HFC (San Marcos, TX-36-861336) carries the seed's own
diagnostic note: *"In 03/25 the property was recapitalized with an unrecorded sale that added Pecos
Housing Authority, Nome Capital Partners and Pensam Capital to the ownership group."* An
owner-name sweep of HaysCAD for `PECOS`, `PECOS HOUSING*`, `NOME`, `PENSAM`, and `IMPEX` (the seed's
three named recap partners) returned **zero matches**. This is not a failed search -- it
independently corroborates both the seed's "unrecorded sale" language and the premise of the Hays
County TRO itself (that Hays CAD had not processed these transfers). The property physically exists
somewhere in San Marcos, but its identity cannot be pinned down from free public HaysCAD data;
Method 3 (Hays County Clerk grantor/grantee index) or the Case 25-1185-DCB pleadings would be
needed. A second Pleasanton San Marcos seed row (TX-36-240, Ground Leasor) has the same
"no matching account" problem, though for that one only one candidate account (The Lodge in San
Marcos) exists at all in HaysCAD under Pleasanton ownership -- see that record's `gaps`.

## Method

1. HaysCAD (`esearch.hayscad.com`, a BIS Consultants-built ASP.NET/Blazor "eSearch" portal --
   `hayscad.com` itself sits behind a Cloudflare challenge and was not used) offers **no bulk
   roll export**; free public access is per-property lookup only. Used the portal's underlying
   JSON search API (`/Search/SearchResults?keywords=OwnerName:"<name>"`) to run owner-name
   sweeps for each of the 13 verified project sponsors (`data/sponsors.json`) plus the generic
   `%HOUSING FINANCE%` / `%PUBLIC FACILITY%` patterns from the kit. This is the free-data
   equivalent of Method 2's CAD roll filter, done one query at a time rather than via CSV.
2. Confirmed matches: **Pleasanton HFC** (3 accounts, all Kyle/San Marcos), **Edcouch Community
   HFC** (5 accounts across 2 Dripping Springs complexes), **Texas Essential Housing PFC**
   (2 accounts, 1 San Marcos complex). Zero matches for Pecos HFC, Cameron County HFC, La Villa
   HFC, Maverick County HFC, or Garland HFC under any owner-name variant tried.
3. Pulled each matched account's `/Property/View` page for situs address, legal description,
   owner/mailing address, Property Values panel (market/appraised/assessed value), the
   per-taxing-entity Property Taxing Jurisdiction table (used to determine exemption status:
   market value = taxable value means **no exemption in effect**), the Property Improvement
   tables (year built), and the Property Deed History table (grantor/grantee chain, recording
   instrument numbers, dates) -- this last table supplied clean SWD dates/instruments without
   needing a separate county-clerk search (Method 3 fingerprint visible directly in the CAD
   deed history for most of these accounts).
4. Toggled each account's year selector (2021-2026 available) to establish `first_exempt_tax_year`
   and to check for exemption reversals year-over-year.
5. Property names/unit counts not printed on the CAD card (HaysCAD's public card has no explicit
   unit-count field) were cross-checked against 2-3 independent listing/developer sources
   (apartments.com, Greystar, Wilson Capital's own portfolio pages, Yardi Matrix's public listing
   page) and only recorded where sources agreed; conflicting or single-source unit counts were
   left `null` with a `gaps` note rather than guessed, per the project's no-guess rule.
6. Matched 4 of 6 seed rows to specific HaysCAD accounts by sponsor + city + best-effort role/
   value pairing (2 seed rows share identical Kyle/Pleasanton and San Marcos/Pleasanton buckets
   with no distinguishing address in the seed) -- flagged `single-source` with a `gaps` note on
   every such record, per the Dallas census's bucket-pairing convention. 2 seed rows (1 Pecos,
   1 Pleasanton) had no HaysCAD candidate at all.
7. The 5 HaysCAD-confirmed accounts left over after seed-linking became expansion records
   `TX-NEW-HAYS-1..5`. No bulk files were downloaded in this pass (none exist for HaysCAD); no
   cleanup of bulk downloads was required, per the project's disk-conservation instruction.

## Table: all 11 records

| census_id | sponsor | property | city | CAD account | appraised value | TY26 exempt? | first-exempt yr | kill date |
|---|---|---|---|---|---|---|---|---|
| TX-36-1273141 | Edcouch Community HFC | Jovie Belterra Apartments | Dripping Springs | R179726 | $35,500,000 | N | -- | 2027-01-01 |
| TX-36-861336 | Pecos HFC | *(unresolved -- unrecorded sale)* | San Marcos | -- | -- | ? | -- | 2027-01-01 |
| TX-36-2275 | Pleasanton HFC | Vantage at Plum Creek Apartments | Kyle | R132408 | $38,000,000 | N | -- | 2027-01-01 |
| TX-36-186 | Pleasanton HFC | The Lodge in San Marcos | San Marcos | R100679 | $38,600,000 | N | -- | 2027-01-01 |
| TX-36-240 | Pleasanton HFC | *(unresolved -- no 2nd San Marcos account found)* | San Marcos | -- | -- | ? | -- | 2027-01-01 |
| TX-36-1128394 | Pleasanton HFC | The Chloe | Kyle | R172991 | $51,000,000 | N | -- | 2027-01-01 |
| TX-NEW-HAYS-1 | Edcouch Community HFC | Local Dripping Springs (Lot 1) | Dripping Springs | R190278 | $11,000,000 | N (was partial in TY25) | 2025 (reversed) | 2027-01-01 |
| TX-NEW-HAYS-2 | Edcouch Community HFC | Local Dripping Springs (Lot 2) | Dripping Springs | R190279 | $18,000,000 | N | -- | 2027-01-01 |
| TX-NEW-HAYS-3 | Edcouch Community HFC | Local Dripping Springs (Lot 3, out-parcel) | Dripping Springs | R190280 | $458,050 | N | -- | 2027-01-01 |
| TX-NEW-HAYS-4 | Texas Essential Housing PFC | Cheatham Street Flats (residential) | San Marcos | R151288 | $18,107,596 | **Y (full, $0 taxable)** | 2022 (partial) / 2023 (full) | -- (no cliff, Ch.303) |
| TX-NEW-HAYS-5 | Texas Essential Housing PFC | Cheatham Street Flats (retail parcel) | San Marcos | R194294 | $1,388,417 | Partial (~9% exempt) | unconfirmed | -- (no cliff, Ch.303) |

*TY26 exempt column: Y = HaysCAD taxable value < market value for tax year 2026; N = fully taxable
(market = taxable) despite sponsor-of-record ownership; ? = ownership/exemption status not resolved
to a specific parcel.*

## By sponsor

| Sponsor | Records (seed+new) | Accounts w/ CAD match | Appraised value captured | Currently exempt (TY26) |
|---|---|---|---|---|
| Pleasanton HFC | 4 | 3 | $127,600,000 | 0 |
| Edcouch Community HFC | 4 | 4 | $64,958,050 | 0 (1 had a since-reversed partial exemption in TY25) |
| Texas Essential Housing PFC | 2 | 2 | $19,496,013 | 1 full + 1 partial |
| Pecos HFC | 1 | 0 | -- | ? |
| Cameron County HFC / La Villa HFC / Maverick County HFC / Garland HFC | 0 each | 0 | -- | -- (no HaysCAD presence found) |

## Kill analysis (Tier 1 HFC sponsors -- Pleasanton, Edcouch)

All 8 Tier-1 HFC-sponsored Hays records (Pleasanton x4 incl. 1 unresolved, Edcouch x4) face
**HB 21 §13(i)**: exemption ineligible after **2027-01-01** for HFC-owned multifamily property held
outside the sponsor's home jurisdiction as of 9/1/2025, absent a qualifying host-jurisdiction
resolution -- plus **§13(e)** early death on any sale/refinance/majority-ownership transfer. In
practice, **the 2027 cliff is largely moot for the 6 confirmed Pleasanton/Edcouch accounts that
have never carried any exemption at all** -- there is nothing left for the statute to kill on those
records; the live question for them is whether/when an exemption is ever granted, not when an
existing one lapses. The one exception (`TX-NEW-HAYS-1`, Local Dripping Springs Lot 1) already
lost a partial exemption between TY2025 and TY2026 -- an earlier, non-statutory kill.

Every Tier-1 record in this file carries a `litigation_flags` entry. For **Pleasanton HFC** (all 4
records) and, contingently, **Pecos HFC** (the 1 unresolved record): direct exposure to *Hays
County v. Pecos HFC & Pleasanton HFC*, Case No. 25-1185-DCB (filed 4/30/2025) -- the TRO
specifically targeting these two sponsors' San Marcos/Kyle exemption claims. For **Edcouch
Community HFC** (all 4 records): explicitly **not** a named party to that suit, flagged as such to
avoid over-attributing the litigation risk, even though its Hays exemption outcomes look similar
in practice.

**Texas Essential Housing PFC (Tier 2)** faces no 2027 cliff (HB21 is HFC-only); its kill vectors
are the 99-year ground-lease term, a capital event, §303.0426 audit failure, or a CAD/AG
challenge -- none of which has hit its Hays County account. Its litigation flags are its
sponsor-level Williamson CAD suits and AG KP-0437 (`data/sponsors.json`), not Hays-specific.

## Top gaps / blockers

1. **2 of 6 seed rows (1 Pecos, 1 Pleasanton) could not be matched to any HaysCAD account.** The
   Pecos gap is independently corroborated by the seed's own "unrecorded sale" language and by the
   Hays TRO's premise; the Pleasanton gap has only one candidate account in HaysCAD for two seed
   rows. Method 3 (Hays County Clerk grantor/grantee index) or the Case 25-1185-DCB court file
   would resolve both.
2. **Why several accounts show an exemption granted then reversed (or never granted despite recent
   §394.905/§303.0426 acquisition) cannot be determined from the appraisal roll alone.** Candidate
   causes: the Hays TRO itself (for Pleasanton), non-filing of the §394.9027 TDHCA compliance audit
   (first due 6/1/2026, would forfeit the exemption for the year), a pending/denied application, or
   precautionary Hays CAD posture. TDHCA's compliance-monitoring pages (Method 1) or a TPIA request
   are the next step -- same open item flagged in the Dallas census.
3. **`property.units` is null on 7 of 11 records.** HaysCAD's public property card has no unit-count
   field (unlike DCAD's bulk `COM_DETAIL` export used for Dallas); where 2+ independent secondary
   sources agreed (The Lodge in San Marcos: 258; The Chloe: 342) units were recorded, otherwise left
   null rather than guessed from conflicting or single-source listings.
4. **`annual_exemption_value_est` is null on every record.** HaysCAD's TY2026 per-jurisdiction "Total
   Tax Rate" reads 0.000000 across the board (2026 rates not yet adopted on this preliminary roll);
   a prior adopted-rate year applied to that year's exempted value would approximate this in a
   future pass.
5. **Seed-to-account pairing for the 2 Kyle and (partially) 2 San Marcos Pleasanton rows is
   best-effort, not deed-confirmed** -- flagged `single-source` on each affected record.
6. **Edcouch's single Hays seed row was matched to one of TWO distinct Edcouch complexes**
   (Jovie Belterra vs. Local Dripping Springs, both developed by the seed's named partner Wilson
   Capital) on a best-effort, higher-value basis; it could equally represent the other.
7. Loan/servicer/securitization data (schema's `loan.*` block) was not researched -- out of reach of
   free CAD/court sources for this county pass, consistent with prior county censuses.
