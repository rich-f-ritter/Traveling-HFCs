# Texas Traveling HFC/PFC Census — Project Plan

**Mission:** identify every Texas multifamily property held in a *traveling* public-corporation
tax-exemption structure, classified by which legal regime kills its exemption and when — with
enough per-property detail to underwrite the coming unwinds.

**Method backbone:** the `kit/` statewide starter kit (legal framework, 4-method identification
playbook, source directory, request templates, Sarah case study). Read `kit/README.md` first.

## Agreed scope (set 2026-07-11)

- **Entities:** ALL traveling public-corporation deals, classified and tiered by kill-date —
  nothing dropped. Priority ranks by regime.
- **Depth:** two-tier — a public-record census on every in-scope property, then Sarah-level deep
  dossiers on a prioritized top slice.
- **Sources:** **public-record only.** No paid county-clerk downloads, no TPIA-and-wait, no
  subscription loan data. Per-deal artifacts that only those channels can supply (unrecorded
  ground leases, live loan/special-servicing status) are recorded as explicit `gaps`, not chased.

## The three tiers (why the seed list is not one thing)

The Yardi Matrix seed (`data/seed_properties.*`, 335 rows, 13 sponsors) blends three legal species.
Only Tier 1 dies by statute in 2027.

| Tier | Species | Seed count | Kill mechanism |
|---|---|---|---|
| **1 — priority** | HFC (Ch. 394) | 150 | **HB 21 §13(i): exemption ends 1/1/2027** if HFC-owned out-of-jurisdiction on 9/1/2025 with no host resolutions; **§13(e)** early death on sale/refi/majority transfer |
| **2** | PFC (Ch. 303) | 29 | HB 2071 **grandfathered** pre-2023 deals — NOT a 2027 cliff; audit-vulnerable; dies on own contract terms |
| **3** | Housing Authority (Ch. 392) | 156 | Separate regime (Pecos HA alone = 126); HB 21/2071 do not directly apply — Phase 1 determines the actual exemption theory and any kill date |

Tier-1 sponsors: Pleasanton HFC (58), Cameron County HFC (30), La Villa HFC (22), Edcouch HFC (18),
Maverick County HFC (18), Garland HFC (4).

## Phases

- **Phase 0 — Scaffolding (done).** Seed → `data/seed_properties.{csv,json}`; sponsor roster →
  `data/sponsors.json`; per-property model → `schema/property_record.schema.json`; derived
  traveling flag + tier. 149/150 HFC rows flag traveling on the seed home-county map.
- **Phase 1 — Sponsor triage (in progress).** One research pass per sponsor (grouped): confirm
  species / statute / home jurisdiction / area of operation / formation / genuine-traveling /
  kill-regime / litigation. Output → `sponsors/<slug>.md` + updated `data/sponsors.json`.
  **Resolves the scope/reliability question definitively.**
- **Phase 2 — State-registrar track.** Pull the two TDHCA compliance-monitoring lists (populating
  now — first audits due 6/1/2026, findings within 60 days); harvest litigation rosters (HB 21
  constitutional challenge, Pleasanton 15th-COA appeals 15-25-00110/-00111-CV, Fort Worth COA
  02-25-00474-CV, AG RQ-0566-KP) for named properties. Independent list to cross-validate Matrix;
  non-filers = highest distress.
- **Phase 3 — Per-property enrichment (fan-out, pipeline enrich→verify, batched by county).**
  Address, geocode, CAD account, units, appraised/exempt value, first-exempt year, recording
  fingerprint, covenant, HB 21 classification, kill date(s), loan/servicer if public, source/field.
- **Phase 4 — Prioritization & underwriting overlay.** Rank by exemption $/yr, capital-event
  triggers (§13(e)), and public distress signals.
- **Phase 5 — Deep dossiers.** Sarah-level reconstruction on the prioritized top slice.

## Repo layout

```
data/raw/        original Matrix xlsx (immutable)
data/            seed_properties.{csv,json}, sponsors.json  (+ census outputs)
schema/          property_record.schema.json  (the per-property data model)
sponsors/        Phase 1 per-sponsor profiles
census/          Phase 3 per-property records (one json per census_id)
kit/             the statewide starter kit (methodology; do not edit — reference)
scripts/         build/enrichment tooling
docs/            working notes, memos
```

## Provenance discipline

Every substantive field carries a source. Confidence ladder: `seed` → `single-source` →
`cross-validated` → `deep-dive`. Traps to respect (from the kit): entity name + statute chapter
beat the deal nickname; recording-stamp dates beat notary dates; executed ≠ recorded; assessed
value ≠ trade value (non-disclosure state).
