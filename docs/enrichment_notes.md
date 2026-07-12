# Partner / Lender / Year-Built Enrichment — Notes & Caveats

Deliverable: **`data/partner_lender_yearbuilt.csv`** (458 rows). Fields also folded into
`data/census_master.json`. Produced by 46 agents (~10 properties each), free public-record sources only.

## Coverage (final, 46/46 batches)

| Field | Found | Rate |
|---|---|---|
| Year built (verified/filled) | 422/458 | 92% |
| Private partner — parent group | 361/458 | 78% |
| Private partner — seller SPE (deed grantor) | 310/458 | 68% |
| Lender | 99/458 | 21% |

## Why lender is only 21% (the honest ceiling under free-only)

Lender is recorded in the **Deed of Trust**, which lives in the county clerk's records, not the CAD.
- Where the clerk's deed index is scriptable, coverage is excellent: **Harris County's cclerk.hctx.net
  (RP.aspx) yielded 9–10/10 lenders** in batches 17 and 22. Most other batches near 0.
- Most county clerk portals (Dallas, Tarrant, Bexar, Travis, Collin, Denton, Montgomery) are
  JS/Cloudflare SPAs that return only an app shell to free tools.
- The reliable free fallback is **SEC EDGAR full-text search** for CMBS/CLO loans — which is why the
  lenders we *did* find cluster on securitized, distressed, or press-covered deals.
- **Structural point:** after the fee-flip, private debt often rides the operator's *leasehold*, so it
  never appears on the CAD's fee record even when the portal is open.
→ To lift lender coverage materially would require paid county-clerk deed-of-trust pulls (out of scope
  per the public-record-only decision).

## Why seller-SPE coverage varies by county

The grantor SPE comes from the CAD's deed/ownership-history page. Present and scriptable in **Dallas
(DCAD), Tarrant (TAD), Galveston, Williamson, Fort Bend, Nueces, Jefferson** → good SPE coverage.
Absent or auth-gated in **Bexar, Travis (Prodigy/Auth0), Denton (Prodigy/Auth0), Collin (Cloudflare),
Montgomery (private API)** → SPE gaps there; parent group still recovered via news/firm pages.

## This pass corrected the Matrix seed's partner column

The seed's "private partner" hints frequently did **not** corroborate against deeds/press and were
corrected or nulled rather than repeated. Confirmed examples: The Establishment → **Nitya** (not
CityStreet); Cypresswood → **Civitas** (not Aspen Oak); Enclave on Louetta → **Streamline** (not
Civitas); Providence at Champions → **Nitya** (not Frankforter); Seville → **REEP** (not the row it was
paired to); plus multiple Tarrant/Harris bucket-pairing fixes. Treat the enriched `private_partner_*`
fields as higher-confidence than the seed hints.

## Sponsor-mislabel flags surfaced (for follow-up)

- A **Burleson (Johnson Co.)** row tagged *Pleasanton HFC*, but Johnson County's top-taxpayer report
  shows **Pecos HFC** as the holder.
- **Denton PFC**'s own city webpage says it currently owns no properties, yet Pecan Place & Veranda are
  tagged to it.
- Three Nitya-partnered **Houston** deals are filed with TDHCA under **"Texas Workforce Housing
  Foundation,"** not "Texas Essential Housing PFC" as tagged.

## Structural / thesis notes

- **Developer concentration:** Presidium developed 5 of 7 Pleasanton HFC deals in Travis County — these
  programs cluster around a handful of repeat developers per sponsor.
- The deals with the **best-documented lenders are the distressed/CMBS ones** — exactly the unwinds the
  census targets (e.g., Waterford Grove, $62.5M in a 2025 CMBS trust, already in special servicing after
  losing its HFC exemption; the Pecos LoanCore CRE-CLO assets; Langdon/Walnut Park).

## Residual gaps

~10 seed rows carry no name/address/CAD account and could not be resolved from any free source (upstream
Matrix data gaps); a handful of ground-up/LIHTC deals have no grantor SPE because the sponsor held the
land through construction rather than acquiring from a private seller. All flagged per-row in `notes`.
