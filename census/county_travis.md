# Travis County - Traveling HFC/PFC Census (Phase 3)

*Per-property enrichment for TRAVIS County. Source: **Travis CAD 2026 Preliminary Special Export (JSON)**, noticed 2026-03-27, downloaded from traviscad.org/publicinformation on 2026-07-11. Method: full-county owner-name sweep of the appraisal roll (30 GB JSON, streamed from the zip) for the Phase-1 VERIFIED sponsor names plus `%HOUSING FINANCE CORP%` / `%PUBLIC FACILITY CORP%`. Classification per docs/phase1_verdict.md + data/sponsors.json.*

> **Method note:** TCAD's interactive owner-search API (propaccess.traviscad.org / esearch) is blocked by this session's egress proxy (502 on CONNECT), so the targeted-API path used by other county agents was unavailable here. The static full-roll export from traviscad.org was the working substitute and yields the same fields (owner, situs, appraised/taxable value, exemption codes, deeds) with complete county coverage.

## Headline findings

- **34 census-grade property records**: **27** matched to the 27 Travis seed rows + **7** expansions found in the roll sweep (`TX-NEW-TRAVIS-1..7`).
- **Total appraised value: $1,191,300,803** (~$1.19 billion) across the 34 properties.
- **Tier split (Travis):** Tier 1 (HFC, 2027 cliff) = **26 properties / $923,246,084**; Tier 2 (TEH PFC, no cliff) = **8 properties / $268,054,719**.
- **PRIMARY-SOURCE FINDING - the exemption line splits exactly on tier.** On the 2026 preliminary roll every **Tier-2 Texas Essential Housing PFC** property carries the **EX-XV** public-property exemption (**taxable value $0**), while **every Tier-1 traveling-HFC** property (Pecos, Pleasanton, Cameron, La Villa, Edcouch) sits on the roll at **full taxable value with NO exemption granted.** TCAD is *not* exempting the traveling-HFC deals - consistent with the statewide CAD crackdown (Tarrant/Bexar/Hays). The grandfathered Ch. 303 PFC keeps its exemption; the Ch. 394 HFCs do not.
- **Kill implication:** for the Tier-1 set the HB21 sec.13(i) 1/1/2027 cliff is nearly moot in Travis - if the exemption is never granted there is nothing to lose in 2027; the deals are already fully taxable (and each carries a 2024-2025 special-warranty deed to the HFC = a sec.13(e) capital event on record). Tier-2 TEH PFC has **no 2027 cliff** (HB2071 grandfathered); its risk is event-driven (audit / capital event / Williamson-CAD-style challenge), with per-deal vintage risk for any post-6/18/2023 board approval.

## By sponsor

| Sponsor | Tier | Props | Appraised value | Exemption status (2026 prelim) |
|---|:--:|--:|--:|---|
| Texas Essential Housing Public Facility Corporation | 2 | 8 | $268,054,719 | EXEMPT (EX-XV, $0 taxable) |
| Pleasanton Housing Finance Corporation | 1 | 10 | $438,305,428 | NOT exempt (full taxable value) |
| Pecos Housing Finance Corporation | 1 | 8 | $195,565,447 | NOT exempt (full taxable value) |
| Cameron County Housing Finance Corporation | 1 | 3 | $107,752,480 | NOT exempt (full taxable value) |
| La Villa Housing Finance Corporation | 1 | 2 | $97,768,600 | NOT exempt (full taxable value) |
| Edcouch Community Housing Finance Corporation | 1 | 3 | $83,854,129 | NOT exempt (full taxable value) |
| **Total** | | **34** | **$1,191,300,803** | |

## Property table

| census_id | Address (Travis) | City | TCAD acct | Appraised | Tier | Exempt? | Kill basis |
|---|---|---|---|--:|:--:|:--:|---|
| TX-36-375983 | 9111 RESEARCH BLVD | Austin | 252833 | $96,626,183 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-927014 | 7655 N FM 620 | Austin | 497787 | $92,960,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-568 | 12101 N LAMAR BLVD | Austin | 864982 | $71,490,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1526 | 9127 RESEARCH BLVD | Austin | 252834 | $70,610,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1838 | 11600 SPIRIT DR | Austin | 974493+100159.. | $67,080,619 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1345319 | 404 & 705 E OLYMPIC DR | Austin | 953959+974441 | $66,522,813 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1155680 | 15835 FOOTHILL FARMS LOOP | Austin | 481431+277030.. | $59,499,999 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-528 | 12113 METRIC BLVD | Austin | 262009 | $54,710,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1508 | 2101 BURTON DR | Austin | 287604 | $49,080,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1194 | 2405 MONTOPOLIS DR | Austin | 920583 | $44,650,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1357295 | 10700 GENOME DR | Manor | 938136 | $43,340,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-377618 | 2302 E WILLIAM CANNON DR | Austin | 336592 | $37,000,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1466 | 8527 N CAPITAL OF TEXAS HWY | Austin | 497709 | $35,270,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1604 | 1500 REAGAN HILL DR | Austin | 228220 | $17,990,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-370218 | 3506 & 3622 MENCHACA RD | Austin | 305344+306014 | $17,772,480 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1179 | 7227 E US HWY 290 | Austin | 852233 | $17,398,449 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1875 | 9024 NORTHGATE BLVD | Austin | 248790 | $17,294,194 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1228395 | 1305 E WELLS BRANCH PKWY | Pflugerville | 944112 | $16,802,944 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-NEW-TRAVIS-7 | 1600 S PLEASANT VALLEY RD | Austin | 285506 | $11,000,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1417384 | 9013 UNITED DR | Austin | 1004086 | $8,556,152 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1549620 | 1005 W STASSNEY LN | Austin | 319611 | $7,880,000 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-1403 | 12704 HARRIS BRANCH PKWY | Austin | 247934 | $6,925,604 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-NEW-TRAVIS-5 | 1801 WELLS BRANCH PKWY | Austin | 272667 | $5,227,200 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-NEW-TRAVIS-4 | 827 W 12TH ST | Austin | 196630 | $4,808,600 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-NEW-TRAVIS-6 | 3101 SHORELINE DR | Austin | 379417 | $2,222,475 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-NEW-TRAVIS-3 | 5301 DECKER LN | Austin | 881289 | $528,372 | 1 | no | HB21 sec.13(i) 1/1/2027 + sec.13(e); already fully taxable on roll |
| TX-36-535 | 9617 GREAT HILLS TRL | Austin | 154607 | $61,054,267 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-36-1314832 | 8300 & 8216 N INTERSTATE HWY 35 | Austin | 238208+238211 | $40,110,000 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-36-1395069 | 614 S 1ST ST | Austin | 101697 | $38,250,000 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-36-1510489 | 1125 SHADY LN | Austin | 192591 | $35,795,394 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-36-1527161 | 7100 & 7200 GILBERT RD | Manor | 994526+994523 | $34,165,058 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-36-1527165 | 824 CAMINO LA COSTA | Austin | 845440 | $25,660,000 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-NEW-TRAVIS-1 | 9220 N INTERSTATE HWY 35 | Austin | 243367 | $17,250,000 | 2 | YES | HB2071 grandfathered - no 2027 cliff |
| TX-NEW-TRAVIS-2 | 7928 GESSNER DR | Austin | 236544 | $15,770,000 | 2 | YES | HB2071 grandfathered - no 2027 cliff |

## Expansions beyond the seed (TX-NEW-TRAVIS-n)

- **TX-NEW-TRAVIS-1** - Texas Essential Housing Public Facility Corporation - 9220 N INTERSTATE HWY 35, Austin 78753 (acct 243367) - $17,250,000 - Tier 2.
- **TX-NEW-TRAVIS-2** - Texas Essential Housing Public Facility Corporation - 7928 GESSNER DR, Austin 78753 (acct 236544) - $15,770,000 - Tier 2.
- **TX-NEW-TRAVIS-3** - Edcouch Community Housing Finance Corporation - 5301 DECKER LN, Austin 78724 (acct 881289) - $528,372 - Tier 1.
- **TX-NEW-TRAVIS-4** - La Villa Housing Finance Corporation - 827 W 12TH ST, Austin 78701 (acct 196630) - $4,808,600 - Tier 1.
- **TX-NEW-TRAVIS-5** - Pecos Housing Finance Corporation - 1801 WELLS BRANCH PKWY, Austin 78728 (acct 272667) - $5,227,200 - Tier 1.
- **TX-NEW-TRAVIS-6** - Pleasanton Housing Finance Corporation - 3101 SHORELINE DR, Austin 78728 (acct 379417) - $2,222,475 - Tier 1.
- **TX-NEW-TRAVIS-7** - Pleasanton Housing Finance Corporation - 1600 S PLEASANT VALLEY RD, Austin 78741 (acct 285506) - $11,000,000 - Tier 1.

## Top gaps

1. **Property (marketing) names** - TCAD `dba` field not captured in this sweep pass; addresses used as identifiers. Retrievable from the roll's dba field or propaccess detail pages (proxy-blocked here).
2. **Unit counts** - the special export exposes improvement *area*, not unit counts; propaccess detail page is proxy-blocked. Units are null for all 34 (the seed also lacked them).
3. **Seed-row <-> parcel 1:1 mapping is SET-LEVEL** inside the Pecos (7 rows / 8 complexes), Pleasanton (8 rows), and TEH (6 rows / 8 complexes) clusters. Matched on sponsor + city + count + deed date; the TCAD export omits the ground-lessee/operating partner, so which physical parcel is which Yardi row is not individually confirmed. Cameron / Edcouch / La Villa matches are higher-confidence (deed dates + city + partner cues).
4. **2025-certified exemption status** - only the 2026 preliminary roll was pulled. Whether TCAD granted the HFC exemptions in 2025 and then denied vs. never granted is unresolved (both are consistent with the taxable-on-roll finding).
5. **First exempt tax year for TEH PFC** estimated at 2023 from deed dates; exact CAD first-exempt year per parcel unconfirmed.
6. **TEH per-deal grandfather vintage** - HB2071 sec.303.021(d) turns on board-approval date, not the (2023) deed date; per-property board-approval dates are the controlling test and are a recording/minutes gap.

## Also surfaced in the sweep (LOCAL / out of scope - not censused)

The owner-name sweep also returned large **Austin home-jurisdiction** public-corporation exempt multifamily that is **not traveling** and therefore outside this census: **Austin Housing Finance Corp** (~82 accts), **Austin Affordable Housing Corp** (~49), **Texas State Affordable Housing Corp / TSAHC** (~10), **Capital Area Housing Finance Corp**, **Strategic Housing Finance Corp** (~7), **AISD Public Facility Corp** (3), **South Congress PFC** (2), and Dominium `%LEASED HOUSING%` LIHTC entities. These are home-county (Travis) deals - local, not traveling - logged here only to document sweep coverage. **Strategic HFC / Capital Area HFC** are not on our verified roster and their home jurisdiction is unverified (flag if a later pass needs them). The **SH130 Municipal Management District** (TEH's sponsor) also holds one small EX-XV-exempt A1 parcel (8101 N FM 973, $1.08M) - the district's own land, not a multifamily deal.
