# Phase 1 Verdict — Sponsor Classification & Seed Reliability

*All 13 sponsors profiled (7 agents, public-record sources, 2026-07-11). Profiles in `sponsors/`;
verified roster in `data/sponsors.json`; re-tiered properties in `data/seed_properties.{csv,json}`.*

## Headline: the seed's premise was backwards

Going in, the concern was that ~half the Matrix list (the housing-authority rows, dominated by
Pecos's 126) might **not** be "going away in 2027." The classification found the opposite. **Pecos
is the mislabel that flips the thesis:** the 126 rows tagged "Pecos Housing Authority" are actually
**Pecos Housing *Finance* Corporation** — a Chapter 394 **HFC**, confirmed at the appraisal-district
owner level and in every lawsuit against it. The Housing Authority (Ch. 392) and the HFC (Ch. 394)
are sister entities sharing a board and executive director, but the exemption is claimed under
§394.905, so **HB 21 governs and the 1/1/2027 cliff applies.**

Result: Tier 1 nearly doubles, and **82% of the list is in the 2027-cliff set**, not ~45%.

| | Before (seed guess) | **After (verified)** |
|---|---|---|
| **Tier 1 — HFC, dies 1/1/2027** | 150 | **276** |
| **Tier 2 — PFC, grandfathered (no cliff)** | 29 | **29** |
| **Tier 3 — Housing Authority (no statutory cliff)** | 156 | **30** |
| Faces the 2027 cliff | — | **276 of 335 (82%)** |
| Traveling (out-of-jurisdiction) | 285 | **320 of 335** |

## Tier 1 — the 2027-cliff HFCs (276 properties, all traveling)

Every HFC sponsor confirmed as Chapter 394, genuinely traveling, and captured by HB 21 §13(i)
(1/1/2027) with §13(e) early death on any sale/refi/majority transfer.

| Entity | Props | Home | Notes |
|---|---|---|---|
| **Pecos Housing Finance Corp** | 126 | Reeves (Pecos) | *Reclassified from "Authority."* Haltom City injunction; Tarrant ARB 5-yr back-assessment ($974M/28 sites); Hays & Arlington suits |
| **Pleasanton HFC** | 58 | Atascosa | Archetype; **abandoned all its appeals → every injunction now stands**; ~68+ reported (seed undercounts) |
| **Cameron County HFC** | 30 | Cameron | Williamson Co. TRO; Bexar AD suit. *Distinct from Cameron County Housing Authority* |
| **La Villa HFC** | 22 | Hidalgo | City of ~1,300; developer-driven |
| **Edcouch Community HFC** | 18 | Hidalgo | Also runs in-town LIHTC rehabs (out of scope) |
| **Maverick County HFC** | 18 | Maverick | Chartered 6/24/2024 — some deals may be post-5/28/2025 (barred outright, not just cliffed) |
| **Garland HFC** | 4 | Dallas (city) | Won a pre-HB21 exemption case; HB21 now overrides. Seed count is a floor |

Shared infrastructure: the RGV HFCs (and Pleasanton/Pecos) defend jointly through the **Texas
Workforce Housing Coalition** (counsel Blake Stribling / Gibson Dunn), which also filed the **HB 21
constitutional challenge** — the case that, if it wins, could move the 2027 cliff.

## Tier 2 — grandfathered PFC (29 properties, no 2027 cliff)

**Texas Essential Housing PFC** (Ch. 303), sponsored by the **SH130 Municipal Management District
No. 1** (a special district in Austin's ETJ; home county Travis — resolves the seed's blank). All 29
travel statewide. HB 21 does **not** reach PFCs, so no cliff — these unwind on capital events, 99-yr
term, §303.0426 audit failure, or CAD/AG challenge. Two Williamson CAD suits and AG KP-0437 are
already testing them; ~12 post-6/18/2023 deals carry boundary/grandfather risk under §303.021(d).

## Tier 3 — housing authorities (30 properties, no statutory cliff)

The Ch. 392 §392.005 exemption has **no geographic self-destruct**, and neither HB 21 nor HB 2071
reaches it — analysts call it "the least regulated" tool, a structure that may *grow* as HFC deals
die. These unwind only via ultra vires challenges, §392.005(c) affordability conditions, or
litigation — event-driven, no clean date.

- **Houston HA (19)** — *mostly local*: ~15 are Harris-County home-turf and drop out of the traveling
  census; only ~4 (Fort Bend/Montgomery) genuinely travel. Runs a Ch. 303 PFC; halted new deals in 2025.
- **Rosenberg HA (5)** & **Plano HA (1)** — deals ride on affiliated **PFCs** (HB 2071 regime). Plano's
  unwind vector is active litigation (Collin Co. 219-03003-2024).
- **Cameron County HA (4)** — **entity-identity gap:** all 4 travel, but deed-level confirmation is
  needed whether each is held by the Authority (Ch. 392, no cliff) or the Cameron County **HFC**
  sibling (Ch. 394, 2027 cliff). Resolves tier per property.
- **San Benito HA (1)** — McAllen deal is "Prospective"; may never have closed. Confirm existence.

## How reliable was the Matrix seed?

- **Good as a net:** it caught the right entities and 320/335 are genuinely traveling. As a starting
  roster it holds up.
- **Wrong on legal species / tier** — the load-bearing error. It flattened three statutes into one
  "PHA" column and mislabeled the single largest sponsor (Pecos HFC as an Authority), which alone
  moved 126 properties across the tier line.
- **Undercounts scale:** Pleasanton (58 vs ~68 reported) and Garland (4, described as a top-2
  statewide HFC) are floors — Phase 2/3 will find more via TDHCA and appraisal-roll sweeps.
- **Traveling flag needed a statute fix:** the seed compared *counties*; HB 21 keys on the sponsor's
  *city* boundary and §392.014 on *city + 5 miles*. Recomputed accordingly (first-order; Phase-3
  geocode refines the +5mi edge cases).

## Verification gaps carried into Phase 3 (per-property)

1. **Cameron County HA (4)** — HA vs HFC per deed. 2. **Maverick (18)** — date each acquisition vs
5/28/2025 (§13(i) cliff vs §394.031 outright bar). 3. **Host resolutions** — any adopted (removes a
property from the cliff)? 4. **§394.9027 audits** — filed by 6/1/2026? Non-filing forfeits TY2026,
*earlier* than the cliff. 5. **Per-property title-holder** confirmation for all 276 Tier-1 (spot-checks
only so far). 6. **San Benito** — did the deal close at all?
