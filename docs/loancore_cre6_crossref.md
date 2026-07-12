# LoanCore 2021-CRE6 — CLO Collateral × Census Cross-Reference

*Source: Morningstar DBRS Surveillance Performance Update, LoanCore 2021-CRE6 Issuer Ltd.,
April 22, 2026 (March 2026 remittance). Cross-referenced against the 458-property HFC/PFC census
(`data/census_master.json`) + the partner/lender enrichment (`census/enrich/`).*

## Question

The Sarah at Lake Houston (Pleasanton HFC, Humble) is financed by a LoanCore loan in this CLO.
**Are any other properties in the CRE6 pool on our traveling-HFC/PFC list?**

## Answer: no — only The Sarah

The pool is winding down to **12 remaining loans** (office concentration now >50%). Four are
**Texas multifamily**, and only one is a traveling-HFC deal:

| CRE6 loan | City | Trust balance | T-12 DSCR | Maturity | On our list? | What it is |
|---|---|---|---|---|---|---|
| **The Sarah at Lake Houston** | Humble, TX | $45.0M | **1.06** | 7/9/2026 | ✅ **Yes** — Pleasanton HFC (Ch. 394), Harris Co., 2027 cliff | The one HFC fee-flip |
| Santa Fe Ranch | Irving, TX | $67.3M | 0.51 | 9/9/2026 | ❌ No | Tides Equities value-add, rebranded "Tides o Ranchview" (8203 Ranchview Dr; 357 units; on servicer watchlist). Conventional, no exemption |
| Trails of Towne Lake | Irving, TX | $47.3M | 0.87 | 10/9/2027 | ❌ No | Lion Real Estate Group, rebranded "Trinity" (1147 Esters Rd; 496 units). Conventional |
| Alister & Emerson | Austin, TX | $39.1M | 0.72 | 11/9/2027 | ❌ No | Two East Riverside communities (1845 & 1919 Burton Dr). Conventional |

Non-TX collateral: 433 North Camden (office, Beverly Hills), 110 Atrium (office, Bellevue WA),
Stonesthrow Apartments (MF, Greensboro NC), 1755 Blake Street (office, Denver), 250 East 200 South
(office, SLC), Winds at Poplar Creek (MF, Schaumburg IL), 735 Montgomery Street, Hotel Theodore,
Tower 250 (office, SLC).

### Confidence on the three "no"s
- **Santa Fe Ranch / Trails of Towne Lake — high.** Our Dallas pass swept the full DCAD bulk export for
  every HFC/PFC sponsor owner-name and surfaced 132 Dallas-county HFC parcels; neither of these appeared.
  Both are independently confirmed as privately owned (Tides; Lion RE).
- **Alister & Emerson — medium-high.** Our Travis CAD coverage was the thinnest of any county, so this is
  the one residual gap, but no free source ties it to an HFC/PFC or a tax exemption.

Note the performance inversion: **The Sarah (the HFC deal) is the best-performing TX multifamily loan in
the pool** (1.06 DSCR) vs. 0.51–0.87 on the conventional value-add deals. The exemption structure isn't
what caused the CLO distress here — a 2021–22 floating-rate value-add wave did.

## The broader finding: LoanCore's HFC exposure runs deeper — outside CRE6

The census already flags **three other Cameron County HFC deals financed by LoanCore**, none of which is
in the CRE6 pool (so they sit in other LoanCore securitizations or on balance sheet):

| Property (census_id) | City | Sponsor | LoanCore loan |
|---|---|---|---|
| Madison at Walnut Creek, fka Park at Walnut Creek (TX-36-528) | Austin | Cameron County HFC | $72M |
| Capital Hills, fka Falls on Bull Creek (TX-36-1466) | Austin | Cameron County HFC | $52M |
| Solara (TX-61-614) | San Antonio | Cameron County HFC | $56.3M |
| Oaks of North Dallas (TX-37, Collin) | McKinney area | Cameron County HFC | "C/O LoanCore" mailing-address lead only (not confirmed) |

**Different pattern than The Sarah.** These trace: Nitya Capital → **GVA (Alan Stalcup)** buys 2021 on
LoanCore debt → GVA defaults (~$125M combined, Dec 2023) → **LoanCore forecloses and takes REO** (2024) →
**Cameron County HFC** comes in as operating partner (2024–25). So LoanCore's entanglement with the
traveling-HFC world is real and broader than The Sarah, but via **distressed/REO** channels rather than a
clean developer-to-HFC fee-flip.

## Next step (open)

Run the same collateral-vs-census cross-reference against the other LoanCore CLOs (2021-CRE5, 2022-CRE7,
etc.) and Cameron County HFC's LoanCore assets to pin down which trust holds each of the three loans above
— yielding LoanCore's full exposure map to the 2027 unwind. Requires the other DBRS/EDGAR reports.

## Sources
- Morningstar DBRS, LoanCore 2021-CRE6 Surveillance Update, 4/22/2026 (collateral tables, Top-10 summary).
- apartments.com — Santa Fe Ranch / "Tides o Ranchview," 8203 Ranchview Dr, Irving.
- MultifamilyBiz — Lion Real Estate Group acquires 496-unit Trails of Towne Lake (now "Trinity").
- The Real Deal — "GVA Defaults on $125M in Austin Multifamily Loans," 12/6/2023.
