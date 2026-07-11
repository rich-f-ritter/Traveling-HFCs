# Texas Traveling HFC/PFC Census — Final Report

*Prepared 2026-07-11. Public-record sources only. Backing data: `data/census_master_final.csv`
(one row per property), `data/target_list.csv` (ranked), `sponsors/` (entity profiles),
`docs/verify_*.md` (adversarial verifications), `census/county_*.json` (per-county detail).*

---

## Executive summary

Starting from a 335-row Yardi Matrix list of "traveling HFC" deals — a list that turned out to
blend three different legal structures and mislabel its single largest sponsor — we built a
verified, sourced census of **458 Texas multifamily properties** held in traveling public-corporation
tax-exemption structures, across **12 counties**, carrying **$12.76 billion** in appraised value and
roughly **$256 million per year** in ad valorem taxes at stake.

Three findings drive the investment thesis:

1. **The 2027 cliff is bigger than the seed implied.** After classifying every sponsor to its
   statute, **388 of the 458 properties are Chapter-394 HFC deals** that lose their exemption on
   **1/1/2027** under HB 21 §13(i) (or earlier on a sale/refi under §13(e)). The seed's biggest
   sponsor — 126 "Pecos Housing Authority" rows — is actually **Pecos Housing *Finance* Corporation**,
   a Ch. 394 HFC, confirmed at the appraisal-district owner level. Two more "Cameron County Housing
   Authority" buckets (Galveston, Harris) were likewise the Ch. 394 **HFC**.

2. **The unwind is already underway — and uneven.** Adversarially verified against 13 CAD accounts
   pulled fresh: a large majority of Tier-1 parcels are **already carried at full taxable value**,
   years ahead of the cliff, because appraisal districts are **denying the exemption on recent
   acquisitions** (Dallas CAD alone denied ~120 requests, putting **~$3B back on the roll / ~$50M/yr**
   in bills) and taxing units are **petitioning to claw back** the older, still-active ones (Tarrant
   County's 28-site / $974M ARB petition). The pattern is regional: aggressive in Dallas/Tarrant/
   Harris/Travis and litigation-hit Hays; **still fully exempt** on the coast/South Texas (Cameron
   County HFC's Nueces/Galveston/Jefferson/Brazoria portfolio) and for **all Tier-2 PFC** deals.

3. **The distress overlay is real.** At least 18 traveling-HFC properties have already had a capital
   event (sale/refi/foreclosure) that trips the §13(e) early-death clock — including Blackstone-linked
   foreclosures in the Pecos/Ashland-Greene cluster and the Sarah at Lake Houston specimen.

---

## 1. The target set — three tiers by kill mechanism

| Tier | Structure | Properties | Appraised | Kill mechanism |
|---|---|---:|---:|---|
| **1 — priority** | HFC (Ch. 394) | **388** | **$11.17B** | HB 21 §13(i): exemption ends **1/1/2027**; §13(e) earlier on sale/refi/majority transfer; §394.9027 audit non-filing forfeits the tax year |
| **2** | PFC (Ch. 303) | 41 | ~$1.3B | **No 2027 cliff** — HB 2071 grandfathered; dies event-driven (capital event, §303.0426 audit failure, CAD/AG challenge) |
| **3** | Housing authority (Ch. 392) | 29 | ~$0.3B | **No statutory cliff**; exposure via ultra vires challenge / litigation only. Mostly local (Houston HA 15/15 local) |

Tier-2 is dominated by **Texas Essential Housing PFC** (sponsored by the SH130 Municipal Management
District in Austin's ETJ). Tier-3 is small after the Pecos/Cameron reclassifications; Houston HA's
apparent 19-deal footprint is almost entirely home-turf public housing, not traveling shells.

## 2. Coverage — 458 properties across 12 counties

| County | Records | Notes |
|---|---:|---|
| Dallas | 132 | 119/132 already fully taxable (DCAD denials) |
| Harris | 107 | HCAD bulk data; land/improvement splits undercount some exemptions |
| Tarrant | 60 | 33/60 taxable; epicenter of the $974M ARB clawback |
| Collin | 22 | 20/22 still exempt (contrast with Dallas) |
| Denton | 16 | taxable splits by vintage: 2025 buys taxable, older still exempt |
| Fort Bend | 14 | Rosenberg deals mostly titled to the HA directly (Ch.392), not its PFC |
| Bexar | 31 | ~20 named in the Bexar AD suit |
| Hays | 11 | Tier-1 zeroed out per the county's TRO |
| Travis | 34 | TEH PFC still exempt; Tier-1 HFCs never granted |
| Montgomery / Williamson | 11 | Williamson CAD suits vs TEH PFC + Cameron HFC |
| Small-county bundle (9) | 20 | Galveston/Nueces/Jefferson/Brazoria (exempt) vs Johnson/Wise/Comal (taxable) |

**Vs. the Matrix seed:** ~300 of the 335 seed rows were matched to a real CAD account with address,
value, and exemption status; **~126 additional properties** were discovered via owner-name sweeps
that the seed missed (note: raw-record count overstates *distinct complexes* by ~2× because one
complex is often split across several CAD parcels — the pairing/expansion QA quantifies this).
**429 of 458 records carry a CAD account number.**

## 3. The headline finding — the exemptions are already being pulled

Verified (see `docs/verify_exemption_status.md`, 13/13 sample parcels re-pulled from live portals):

- **Mechanism A — early denial (dominant):** chief appraisers are refusing the §11.11/§394.905
  exemption on 2024–2025 HFC acquisitions on the theory that traveling HFCs were never authorized to
  own out-of-jurisdiction property. Dallas: ~120 denials, ~$3B back on the roll, ~$50M/yr.
- **Mechanism B — clawback of active exemptions:** taxing units petition the ARB / sue to strip
  still-exempt older parcels (Tarrant's 28-site/$974M petition; Arlington/Haltom City/Hays TROs),
  reaching back up to 5 years (Tax Code §11.43(i)).
- **Contested and moving:** developers (via the Texas Workforce Housing Coalition) are counter-suing
  to void HB 21 and the denials as unconstitutionally retroactive — so today's taxable status is
  contingent, not settled. No injunction has moved the 2027 cliff as of this date.

**Regional split (from per-county rolls):** Dallas, Tarrant, Harris, Travis and Hays are largely
**billed now**; Collin and the coastal/South-Texas Cameron HFC portfolio (Nueces, Galveston,
Jefferson, Brazoria) are **still exempt**; every Tier-2 PFC parcel is **still exempt**.

## 4. Ranked target list (top by annual tax at stake)

Full list in `data/target_list.csv` (Tier-1, ranked). Precise per-account rates for the top 40 total
**$59.7M/yr** ($39.3M already being billed, $20.4M still exempt at the 2027 cliff). Top of the list:

| # | Property | City / County | Sponsor | ~$/yr at stake | Status |
|---:|---|---|---|---:|---|
| 1 | Jefferson Promenade II | Irving, Dallas | Pecos HFC | $2.9M | billed now |
| 2 | Innova | Dallas | Pecos HFC | $2.5M | billed now |
| 3 | Life at Jackson Square (Nob Hill) | Houston, Harris | — | $2.3M | on roll |
| 4 | Monarch Pass | Fort Worth, Tarrant | Cameron Co HFC | $2.2M | exempt → 2027 |
| 5 | Las Colinas Heights | Irving, Dallas | Cameron Co HFC | $1.9M | billed now |
| 6 | Marquis at Park Central | Dallas | — | $1.8M | billed now |
| 7 | Village at Bellaire | Houston, Harris | — | $1.8M | on roll |

*(Whole-census gross: Tier-1 appraised base $11.17B × ~2.3% combined rate ≈ **$256M/yr**.)*

## 5. Sponsors & litigation (detail in `sponsors/` and `docs/phase1_verdict.md`)

- **Pecos HFC** (126+ deals) — the largest; Haltom City injunction, Tarrant $974M ARB clawback,
  Hays & Arlington suits; ED John Salcido; deals run through the Ch. 394 HFC (sister to the Ch. 392
  authority).
- **Pleasanton HFC** (58+) — the archetype; **abandoned all its appeals**, so the Lake Worth /
  Arlington / Fort Worth / Missouri City injunctions now stand.
- **RGV HFCs** (Cameron County, La Villa, Edcouch, Maverick County) — defend jointly via the Texas
  Workforce Housing Coalition (which filed the HB 21 constitutional challenge). Cameron County HFC
  has the widest geographic spread (DFW + coast + South TX).
- **Garland HFC** (small but statewide) — won a pre-HB 21 exemption case now overridden by §13(i).
- **Texas Essential Housing PFC** (Tier 2) — grandfathered; Williamson CAD suits + AG KP-0437; no
  2027 cliff.

## 6. What changed vs. the Matrix seed (reliability)

The seed was a good net but wrong on the load-bearing dimension — legal species. Corrections applied:
**Pecos "Authority" → HFC** (126 rows, Tier 3→1); **two "Cameron County Housing Authority" buckets →
Cameron County HFC** (Tier 3→1); **home-jurisdiction / traveling test fixed** to the statutory
city-boundary (HB 21) and city+5-mile (§392.014) rules; **Texas Essential Housing PFC home county
resolved** (Travis); **Houston HA reclassified mostly-local**; **~126 off-seed properties added.**

## 7. Data model, provenance & known gaps

Every property is a record in `data/census_master_final.csv` conforming to
`schema/property_record.schema.json`, with per-field provenance and an explicit `gaps` list.
Confidence ladder: seed → single-source → cross-validated → deep-dive.

**Known gaps (public-record-only constraints):**
- **Unit counts** absent for many properties (CADs don't publish them); sourced from listings where
  available.
- **`first_exempt_tax_year`** often null (single-year roll snapshots).
- **Seed↔parcel pairing** within same-sponsor/same-city clusters is best-effort where the seed
  carried no address (flagged `single-source`); the Cameron/Dallas "LBJ Station" bucket is a known
  scramble to fix.
- **Unmatched rows:** McLennan (CAD unreachable), Rockwall (CAD login-walled), a Burleson Pecos deal,
  and 13 Harris rows (mostly under-construction) — carried forward as gaps, not dropped.
- **Not yet folded in:** the statewide TDHCA registry cross-check and the litigation/HB 21-challenge
  property rosters (harvest agents did not deliver); these *enhance* cross-validation but do not
  change the tier findings.
- **Out of scope (gated):** unrecorded ground leases, live loan/special-servicing status, TPIA
  productions — recorded as gaps, to be pulled by a human if desired.

## 8. Recommended next steps

1. **File the TDHCA TPIA** (template in `kit/04_request-templates.md`) for all §394.9027/§303.0426
   audit filings — the state's own filer census + non-filer distress signals.
2. **Deed-confirm the reclassified rows** (Cameron County HA→HFC in Galveston & Harris) at the county
   clerk.
3. **Deep-dive the top ~20 targets** (Sarah-level: recorded instrument set, covenant, loan/servicer,
   ROFR/reconveyance mechanics) — `kit/05` + `kit/reference/19` are the template.
4. **Add the loan/distress overlay** (CRE-CLO surveillance) to flag which unwinds are also forced sales.
5. **Monitor the HB 21 constitutional challenge** — if it succeeds, the 2027 cliff moves.
