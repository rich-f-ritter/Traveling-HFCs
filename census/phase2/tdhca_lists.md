# Phase 2 — Method 1: TDHCA State-Registrar Shortcut (HFC/PFC compliance monitoring)

*Pulled live 2026-07-11. Public-record / free sources only. Every claim cites a source URL.*

## TL;DR

- **HFC page: STILL "TBD."** The §394.9027 HFC compliance-monitoring page — the one that
  would name our seven HFC sponsors' developments and publish the first audit findings — has
  **not populated**. The "HFC Developments" section literally renders the string **`TBD`**, and
  the "2026 HFC Monitoring Reports – Period Ending 2025" accordion is **empty**. First reports
  were due 6/1/2026; as of 7/11/2026 none are posted. **The HFC census shortcut is not yet
  available.**
- **PFC page: POPULATED (partial).** The §303.0426 PFC monitoring page publishes a
  **"PFC Properties That Have Reported"** spreadsheet (2024: 141 developments; 2025: 178
  developments) plus hundreds of per-property Monitoring Reports (MR) and Corrective Action
  Reports (CAR) as PDFs. This is the **PFC regime (HB 2071 / Ch. 303), not the HFC regime** —
  so it covers only our PFC-species and PFC-affiliated sponsors, not the seven Chapter-394 HFCs.
- **30 developments tied to our sponsors** were extracted from the PFC reported list (see
  `tdhca_developments.json`).

Source pages:
- HFC: https://www.tdhca.texas.gov/housing-finance-corporation-compliance-monitoring
- PFC: https://www.tdhca.texas.gov/public-facilities-corporation-compliance-monitoring

---

## 1. What the HFC page shows now (the one that matters for the 2027 cliff)

**Status: TBD / empty.** Verbatim from the live HTML (accordion `m-a12211`):

> `HFC Developments`
> `TBD`
>
> `2026 HFC Monitoring Reports - Period Ending 2025`  → *(content div empty — no reports listed)*

What IS posted on the HFC page (forms/infrastructure only — no census data):

| Item | URL |
|---|---|
| HFC Audit Workbook (blank dev-name template) | `/sites/default/files/pmcdocs/HFC-AR26-DevName2p.xlsx` |
| Tenant Income Certification (PDF/DOCX) | `/sites/default/files/pmcdocs/HFC-TIC.pdf` |
| Rent Reduction & Public-Benefit Test | `/sites/default/files/pmcdocs/260311-HFC-PBRR.pdf` |
| Annual Service Fee form (PDF/XLSX) | `/sites/default/files/pmcdocs/HFC-AnnualFee.xlsx` |
| Auditor's List | `/sites/default/files/pmcdocs/HFC-AuditorList_0.xlsx` |
| HB 21 (enrolled) | `/sites/default/files/pmcdocs/HB21-Enrolled.pdf` |
| Chapter 394 (LGC) | `/sites/default/files/pmcdocs/Ch394-LGC.pdf` |

Deadlines / mechanics stated on the page:
- First HFC audit reports **due 6/1/2026** (received, not postmarked); annually by 6/1 thereafter.
- Extension requests governed by **10 TAC Ch. 10, Subchapter J, §10.1203(1)(B)**; max 60 days
  beyond 6/1; TDHCA responds within 7 days.
- Reports + corrective-action docs submitted via **Serv-U account** and **hfc@tdhca.texas.gov**.
- §394.9026/§394.9027 **do not apply while a development holds a 9% LIHTC** allocation
  (Subchapter DD, Ch. 2306) — a carve-out to watch when a sponsor claims non-applicability.
- Contacts: **Wendy Quackenbush** (wendy.quackenbush@tdhca.texas.gov), **Amy Hammond**
  (amy.hammond@tdhca.texas.gov).
- "Lunch and Learn Series **Coming Soon**."

**Implication for the census:** the state-registrar shortcut for HFCs is **not yet live**. Our
seven HFC sponsors (Pecos, Pleasanton, Cameron County HFC, La Villa, Edcouch, Maverick, Garland)
cannot be confirmed as filers or flagged as non-filers from this page today. §394.9027 findings
must publish within 60 days of receipt; expect this page to populate **~Aug–Sep 2026**. Repull then.

## 2. What the PFC page shows now (the populated one)

**Status: POPULATED.** Key data file:

- **"PFC Properties That Have Reported"** — `/sites/default/files/pmcdocs/PFC-Reported-Devs_1.xlsx`
  - Sheet **"2024 Reports Received"**: 141 developments; columns = No. | PFC Sponsor | PFC User |
    Property Name | Address | City | County | Zip | Initial Audit Report Received (Year).
  - Sheet **"2025 Reports Received"**: 178 developments; same columns (PFC User/Sponsor swapped order).
- Plus per-property PDFs under `/sites/default/files/pmcdocs/Monitoring%20Reports/` —
  counted on the live page: **27** `24-CAR-*`, **5** `24-MR-*`, **56** `25-CAR-*`,
  **97** `25-MR-*`, **78** `25-PFC-*` (corrective-action / monitoring reports).
- Audit workbooks split pre- vs post-6/18/2023; Auditor's List XLSX.
- PFC monitoring covers **only developments initiated on/after 6/18/2023** and exempts those
  with ≥20% public housing, RAD, Ch. 1372 bond, or LIHTC assistance. Regime = **HB 2071 /
  §303.0421, §303.0425, §303.0426**; rules **10 TAC §10.1101–10.1107**.

This is the **PFC-side** census, so it reaches only our Tier-2 PFC and Tier-3 HA-with-PFC sponsors.

### 2a. Rule + board materials (task item 2)

The HFC monitoring **rulemaking is complete**, but it did not create any separately posted
registry of developments — the register still lives (as TBD) on the monitoring page above.

- **10 TAC Ch. 10, Subchapter J — HFC Compliance Monitoring Rule (adopted):**
  https://www.tdhca.texas.gov/sites/default/files/pmcdocs/10TAC10-HFC-CM-Rule.pdf (Dec 26, 2025)
- Proposed draft: https://www.tdhca.texas.gov/sites/default/files/pmcdocs/10TAC10-J-HFC-Proposed-DRAFT.pdf (Oct 24, 2025)
- Public-comment notice for the new HFC rule:
  https://www.tdhca.texas.gov/calendar/public-comment-new-housing-finance-corporation-hfc-rule
- **§10.1204 HFC rule reg-amendment** (Governing Board approved **4/9/2026**; published Texas
  Register **4/24/2026**):
  https://www.tdhca.texas.gov/sites/default/files/pdf/public-comment/10TAC10-1204-HFCRuleRegAmend.pdf
- TDHCA was required by HB 21 to adopt these rules by **1/1/2026** (done), funded at $228,228/yr
  + 1 FTE. No board-posted list of monitored HFC developments or audit-findings summary was found
  outside the (still-TBD) monitoring page as of 7/11/2026.

---

## 3. Per-sponsor filer / non-filer status (against data/sponsors.json)

**Cross-reference basis:** the PFC reported-developments spreadsheet (above), matched on the
"PFC Sponsor" column. HFC sponsors are marked N/A because the HFC page that would list them is
still TBD.

| # | Our sponsor | Species / Tier | On a TDHCA published list? | Signal |
|---|---|---|---|---|
| 1 | Pleasanton HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 2 | Cameron County HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 3 | La Villa HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 4 | Edcouch Community HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 5 | Maverick County HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 6 | Garland HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 7 | Pecos HFC | HFC / T1 | **N/A — HFC page TBD** | Cannot determine yet |
| 8 | **Texas Essential Housing PFC** | PFC / T2 | **YES — FILER** (2024 + 2025 sheets) | 15 developments listed |
| 9 | **Houston Housing Authority** | HA / T3 | **YES — FILER** (2025 sheet, as PFC sponsor) | 4 developments (all Harris/local) |
| 10 | Cameron County Housing Authority | HA / T3 | No | N/A (not a PFC; no monitoring obligation on this list) |
| 11 | **Rosenberg Housing Authority** | HA / T3 | **NO — absent** | **Potential non-filer (caveated)** |
| 12 | San Benito Housing Authority | HA / T3 | No | N/A (deal may never have closed; not a PFC) |
| 13 | **Plano Housing Authority** | HA / T3 | **YES — FILER** (directly + via Plano PFC) | 3 direct + 8 via Plano Public Facility Corp = 11 |

### Filers confirmed (our sponsors that appear)
- **Texas Essential Housing PFC (T2)** — 15 unique developments on the reported list. Confirms
  the PFC is actively reporting; both under "Texas Essential Housing PFC" and the full-name
  variant "Texas Essential Housing Public Facility Corporation." (Note: its sponsoring special
  district, "SH 130 Municipal Management District No. 1," also appears once as a distinct sponsor
  string in 2025 — TDHCA is not normalizing sponsor names.)
- **Houston Housing Authority (T3)** — filer in 2025 as a PFC sponsor: Allora Gosling, Caroline
  at Memorial, Birchway Perry Road, Milano Apartments (all Harris County — the local, non-traveling
  cluster consistent with Phase-1's "mostly local" finding).
- **Plano Housing Authority (T3)** — filer both as itself (Collin Creek, Latitude, Summers
  Crossing) and via **Plano Public Facility Corporation** (8 more: Avalon/Thornbury at Chase Oaks,
  Bel Air 16th, Bel Air Oaks, Enclave Gateway, Fountains at Steeplechase, Jada/Opal Legacy Central).
  All Collin County (Plano-local); the lone traveling deal (Lewisville) noted in Phase 1 is **not**
  on this PFC list — expected, since it may predate 6/18/2023 or sit in the HFC/other structure.

### Non-filer signals (our sponsors that DON'T appear)
- **Rosenberg Housing Authority / RHAPFC — ABSENT from both PFC sheets.** This is the only
  PFC-regime sponsor of ours that does not appear.
  - **Caveat before treating as a §303 forfeit:** PFC monitoring only reaches deals **initiated
    on/after 6/18/2023**; pre-2023 deals are grandfathered and exempt from this list. Phase 1
    flagged Rosenberg's Sugar Land/Stafford deals as out-of-area but did not date them. Absence is
    therefore **consistent with either** (a) legitimate exemption (all deals pre-6/18/2023) **or**
    (b) an actual reporting failure. Resolve by dating each Rosenberg acquisition, then TPIA if any
    post-6/18/2023 deal exists with no report on file.
  - Note: the **§394.905 exemption-forfeit-for-non-filing** mechanism the task highlights is an
    **HFC** mechanism (§394.9027). It does not attach to Rosenberg (a Ch. 392/303 actor). The
    sponsors most exposed to that early-death-by-non-filing are the **seven HFCs — whose filer
    status is still unknowable because the HFC page is TBD.** That is the single highest-value
    repull for August.
- **Cameron County HA, San Benito HA** — absent, but neither is a PFC, so absence carries no
  non-filing signal on this list.

### Data-quality caveats (TDHCA's own spreadsheet)
- Sponsor names are **not normalized** ("Plano Public Facility Corporation" vs "Plano Public
  Facilities Corporation" vs "Plano Housing Authority"; two Texas Essential name strings).
- At least one row is internally inconsistent: **"Latitude"** is listed once as Plano/Collin/75075
  and once as Houston/Harris/77004 for the same street ("601 Patton Blvd") and same user ("Post
  Latitude, LLC"). Treated as one Plano development in our JSON. Verify against CAD at Phase 3.
- Some property names are misspelled in the source ("Thrive Alemda Genoa," "Founmtains").

---

## 4. Template-B TPIA to file now (HFC list is still incomplete/TBD)

Because the HFC monitoring page has not populated, the register + first-year audit findings for
our seven Chapter-394 HFC sponsors are not obtainable by download. File the following to TDHCA to
force production of the HFC §394.9027 filings and the underlying register (per kit/04 Template B).

**Channel:** TDHCA public-information / open-records. Reports intake is hfc@tdhca.texas.gov;
route the formal PIA through TDHCA's designated open-records channel and cc the HFC monitoring
staff (Wendy Quackenbush, Amy Hammond). Ask for electronic copies.

> **Public Information Act Request — HFC/PFC compliance filings**
>
> Pursuant to Gov't Code ch. 552, I request: (1) all compliance audit reports received by the
> Department under Loc. Gov't Code §394.9027 (housing finance corporations) and §303.0426 (public
> facility corporations) from January 1, 2026 to the date of this request; (2) the Department's
> current list or register of multifamily developments subject to HFC or PFC compliance
> monitoring, including development name, address, county, and sponsoring corporation; (3) all
> requests for extension of the June 1, 2026 audit deadline and the Department's dispositions; and
> (4) any summary reports prepared under §394.9027(c). Per §394.9027(k) I understand
> tenant-identifying information may be redacted; I request all remaining portions electronically.
>
> If the records cannot be produced within ten business days, please provide the written
> certification required by Gov't Code §552.221(d).

**Why this is worth filing despite the page being TBD:** the audits were *due* 6/1/2026 and
findings *must* publish within 60 days — so the records **exist at the Department now** even though
the public page has not been updated. The PIA reaches them ~45 business days faster than waiting
for the webmaster, and item (3) (extension dispositions) surfaces exactly which of our seven HFC
sponsors asked for more time vs. which simply **did not file** — the §394.905 forfeiture signal.

**Targeted add-ons** (optional, to sharpen the non-filer question): amend item (2) to request the
register broken out by sponsoring corporation, and add "(5) for each of the following corporations,
all §394.9027 audit reports and any notice of non-submission: Pecos Housing Finance Corporation;
Pleasanton Housing Finance Corporation; Cameron County Housing Finance Corporation; La Villa
Housing Finance Corporation; Edcouch Community Housing Finance Corporation; Maverick County Housing
Finance Corporation; Garland Housing Finance Corporation."

---

## 5. Next actions

1. **Repull both pages ~Aug–Sep 2026** — the HFC 60-day publication window closes then.
2. **File Template B now** (§4) to obtain the HFC register + findings + extension dispositions
   ahead of the page update.
3. **Date Rosenberg's deals** vs 6/18/2023 to convert the "absent" signal into non-filer vs
   grandfathered.
4. Feed the 30 PFC developments (`tdhca_developments.json`) into the Phase-3 per-property roll.

## Sources
- HFC monitoring page (live, TBD): https://www.tdhca.texas.gov/housing-finance-corporation-compliance-monitoring
- PFC monitoring page (live, populated): https://www.tdhca.texas.gov/public-facilities-corporation-compliance-monitoring
- PFC Properties That Have Reported (XLSX): https://www.tdhca.texas.gov/sites/default/files/pmcdocs/PFC-Reported-Devs_1.xlsx
- HFC Auditor's List (XLSX): https://www.tdhca.texas.gov/sites/default/files/pmcdocs/HFC-AuditorList_0.xlsx
- HB 21 enrolled (TDHCA copy): https://www.tdhca.texas.gov/sites/default/files/pmcdocs/HB21-Enrolled.pdf
- Ch. 394 LGC (TDHCA copy): https://www.tdhca.texas.gov/sites/default/files/pmcdocs/Ch394-LGC.pdf
- HB 2071 enrolled: https://www.capitol.state.tx.us/tlodocs/88R/billtext/html/HB02071F.htm
