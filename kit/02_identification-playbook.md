# 02 — Identification Playbook: how to find every traveling HFC/PFC multifamily deal in Texas

Four independent detection methods. Run them all — each catches deals the others miss, and
properties confirmed by 2+ methods are census-grade.

## Method 1 — The TDHCA census shortcut (highest leverage; do first)

HB 21 (§394.9027) and HB 2071 (§303.0426) make TDHCA the state's involuntary registrar of
exactly the properties this project wants.

1. Watch the two monitoring pages (both live): 
   `tdhca.texas.gov/housing-finance-corporation-compliance-monitoring` and
   `tdhca.texas.gov/public-facilities-corporation-compliance-monitoring`. First HFC audits
   were due **6/1/2026**; findings summaries must publish within 60 days — the lists were
   still "TBD" on 7/11/2026, so they should populate ~Aug 2026. When they do, that IS the
   filer census (property, sponsor, compliance posture).
2. Don't wait — **TPIA TDHCA now** for: all §394.9027 and §303.0426 audits received to
   date; the list of developments registered for monitoring; all 60-day extension requests
   (extensions were available on request by 5/1/2026). Contact: hfc@tdhca.texas.gov;
   template in `04_request-templates.md`.
3. **The non-filers are the alpha.** Cross the filer list against Method 2's
   exemption-roll list: an exempt HFC-owned property with NO audit on file has already
   forfeited its exemption for the tax year (§394.9027) and its owner may not know —
   maximal distress, earliest unwind.

## Method 2 — Appraisal-roll sweep (the scalable data method)

Every one of these properties is, by construction, a **100%-exempt multifamily parcel whose
owner is a public corporation**. County appraisal districts publish downloadable rolls.

1. Pull CAD data (bulk exports where offered — HCAD has open data; big CADs: Harris,
   Dallas, Tarrant, Bexar, Travis, Collin, Denton, Fort Bend, Montgomery, Williamson,
   El Paso, Hidalgo, Galveston, Brazoria… traveling deals cluster in metros).
2. Filter: state class code = multifamily (B1/B2 etc. varies by CAD) AND total exemption
   (taxable value 0 or exemption ≈ 100% of appraised) — then match **owner name** against:
   `%HOUSING FINANCE CORP%`, `%HFC%`, `%PUBLIC FACILITY CORP%`, `%PFC%`, plus known-sponsor
   names. Also catch title-holding shells: `%LEASED HOUSING%`, `%AFFORDABLE HOUSING CORP%`.
3. Classify traveling vs local: geocode the sponsor's home jurisdiction (the corporation's
   name usually declares it — "Pleasanton HFC," "Cameron County HFC") vs the parcel county.
   Sponsor county ≠ parcel county → traveling. Ambiguous names → check the SWD grantee's
   address on the recorded deed, or the Comptroller entity record's registered agent.
4. **Date the structure**: the exemption's start year (the roll shows when taxable value
   dropped) + the recorded SWD date give you the HB 21 §13(i)/HB 2071 classification.

## Method 3 — County-clerk fingerprint search (per-deal ground truth)

These closings leave an unmistakable recording signature — at the Sarah it was **seven
instruments e-filed in one batch at 07:34 AM**:

> SWD (developer→HFC) · Regulatory Agreement · **Memorandum of Ground Lease** · Purchase
> Option/ROFA · lender-side memo · A&R leasehold Deed of Trust · A&R Assignment of Leases
> and Rents — consecutive instrument numbers, same filing timestamp, "UNOFFICIAL COPY"
> watermarks on scans.

How to sweep a county:
1. Grantor/grantee index search on each known HFC/PFC name (start list in `README.md`;
   grow it from TDHCA filings and litigation). Every hit's date-batch reveals the rest of
   that deal's instrument set via adjacent file numbers.
2. Reverse direction: search instrument type MEMO/LEASE where grantee contains
   "Housing Finance" — memoranda of ground lease are the cleanest single marker (a fee
   owner leasing TO an LLC for 99 years is not a normal apartment transaction).
3. Portal capabilities vary by county. Harris: cclerk.hctx.net websearch (free viewing
   w/ account, $1/page). Tarrant, Dallas, Bexar, Travis have equivalents; smaller counties
   may need runner services. Statewide aggregators (TexasFile, CourthouseDirect, ~$1-3/doc)
   let you run one name across many counties — worth it for the sponsor-name sweeps.
4. The regulatory agreement's recitals name the deal economics (set-aside, AMI band); the
   DoT names the lender — capture both into the data model.

## Method 4 — Names, news, and litigation (seed + verify layer)

- **Litigation dockets** (search.txcourts.gov, re:SearchTX, free): every city that sued or
  was sued over an HFC deal names properties and sponsors in its pleadings. Start:
  the two 15th COA Pleasanton appeals; the Fort Worth COA appraisal case; the HB 21
  constitutional challenge (its plaintiff coalition = a sponsor roster).
- **AG materials**: RQ-0566-KP names deals/parties; watch for the opinion and any
  successor requests.
- **Local journalism**: Pleasanton Express (documented PHFC's ~68-property portfolio and
  fee schedule); Fort Worth Report; Texas Housers' HB 21 analyses; The Real Deal Texas;
  Bettencourt's Senate press releases (statewide counts).
- **CLO/CMBS surveillance** for the distress overlay: many of these are 2021-22 vintage
  floating bridge loans in CRE CLOs. DBRS/KBRA surveillance and Trepp/CRED iQ special-
  servicing lists cross-referenced against Method 2's property list flag which unwinds are
  also forced sales — the acquisition pipeline within the census.

## Per-property data model

Use `data/example_instrument_extraction_sarah.json` as the schema seed. Minimum fields:
property (name/address/county/CAD account/units) · sponsor (HFC/PFC name, home
jurisdiction, statute chapter) · structure dates (MOU, SWD, ground-lease, recording refs)
· exemption (first exempt year, annual value) · covenant (set-aside %, AMI band) · fees ·
lender/servicer + loan status · HB 21/2071 classification (13(i)-captured? resolutions?
audit filed?) · kill date(s) · litigation flags · sources per field.

## Traps (learned the hard way)

1. Deal files and brokers say "PFC" for everything — **the entity name and statute chapter
   are the truth**, not the nickname. Misclassification changes which law and kill date apply.
2. Scanned county copies contain scrivener errors (wrong years, misdescribed entities) —
   extract dates from recording stamps, not notary blocks.
3. An executed document is not a recorded document — the Sarah's MOU carried no recording
   stamp; recital chains ("as recited in…") are how you find what ISN'T recorded.
4. Exemption timing ≠ deal timing: the Sarah's MOU was 7/2024, closing 2/2025, exemption
   effective tax year 2025, cash effect Oct 2025. Model accrual and cash separately.
5. Assessed values on these properties often far exceed distressed trade values
   (non-disclosure state) — don't equate the roll's implied tax with the buyer's pro forma.
