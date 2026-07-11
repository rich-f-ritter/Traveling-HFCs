# Texas Traveling HFC/PFC Census — Starter Kit

**Mission:** build a list of every multifamily property in Texas held in a *traveling*
HFC/PFC tax-exemption structure — the deals whose exemptions are going away — with enough
per-property detail to underwrite the coming unwinds.

This kit is the distilled, verified knowledge from a completed deep-dive on one such deal
(The Sarah at Lake Houston, Humble TX — Pleasanton HFC), where we reconstructed the entire
structure from public records, verified the law against enrolled bill text, and confirmed
every retrieval channel by actually using it. Dates herein are as of **July 11, 2026**.

## Contents

| File | What it is |
|---|---|
| `01_legal-framework.md` | The statutes and kill dates that define the target set — read first; it defines project scope |
| `02_identification-playbook.md` | How to actually FIND these properties: the recording fingerprint, the appraisal-roll method, the TDHCA census shortcut, name-sweep strategy |
| `03_source-directory.md` | Every verified portal, contact, cost, and procedure |
| `04_request-templates.md` | Ready-to-file TPIA request language (HFC, TDHCA, appraisal district) |
| `05_case-study_sarah-at-lake-houston.md` | One complete specimen, end to end — what a fully-documented entry looks like |
| `data/example_instrument_extraction_sarah.json` | The structured-extraction schema we used on recorded instruments (use it as the census's per-property data model) |
| `reference/` | The three underlying research memos (full citations, verification votes, caveats) |

## The single most important thing in this kit

**The State of Texas is about to publish most of this census for you.** HB 21 (2025) and
HB 2071 (2023) force every HFC and PFC claiming the multifamily exemption to file annual
independent compliance audits with TDHCA, which must publish findings summaries within 60
days. First HFC audits were due **June 1, 2026** — the publication window is open now
(TDHCA's lists still showed "TBD" on 7/11/2026). One TPIA request to TDHCA for *all §394.9027
and §303.0426 audit filings received* is the highest-leverage single action available to
this project: it yields, in one document set, the property list, the sponsor HFC/PFC for
each, and the compliance posture of each. Everything else in this kit is for (a) properties
whose sponsors didn't file (themselves a high-value distress signal — non-filing forfeits
the exemption for the tax year), (b) per-property deep dives, and (c) cross-validation.

## Scope warning (defines "the ones going away")

- **HFC out-of-jurisdiction deals (Ch. 394):** these die by statute. Owned out-of-area on
  9/1/2025 + no host resolutions by 12/31/2026 → exemption terminates after **1/1/2027**
  (HB 21 §13(i)). Grandfather also dies early on any sale/refi/majority transfer (§13(e)).
  **This is the core target set.**
- **PFC traveling deals (Ch. 303) closed before HB 2071 (June 2023):** these were
  **grandfathered and do NOT automatically die** — do not assume a 2027 cliff for them.
  They are audit-vulnerable (TDHCA regime) and die on their own contract terms, but listing
  them as "going away" without checking each deal's facts would be wrong. Track them as a
  separate tier.
- LIHTC deals are carved out of the new HFC conditions — exclude properties whose
  affordability comes from tax credits rather than the HFC/PFC fee-ownership structure.

## Known starting points (documented, not exhaustive)

- **Pleasanton HFC** — the archetype; local reporting documents a **~68-property portfolio**
  statewide; enjoined in Lake Worth and Arlington (15th COA Nos. 15-25-00110-CV,
  -00111-CV); named specifically in AG opinion request RQ-0566-KP (10/2/2024).
- The **HB 21 constitutional challenge** (Texas Workforce Housing Coalition + Cameron
  County, filed Sept. 2025, attacking the retroactive tax provisions) — its plaintiff/amici
  lists are a roster of affected sponsors and deals; pull the petition.
- Senate sponsor Bettencourt's press materials and **Texas Housers**' HB 21 coverage cite
  statewide counts and name deals — good seed lists, verify each against records.

## Provenance & confidence

Everything here was adversarially verified (3-vote process) against primary sources —
enrolled bill text, live portal fetches, recorded instruments — in two deep-research runs
(101 and 105 agents) plus direct document reads. Where something was REFUTED in
verification it is flagged in the files (there are two such traps: HB 2071 PFC set-aside
specifics, and a supposed "underwriting assessment on the HFC's website" route). The
`reference/` memos carry the full citation trail.
