# Enrichment task — private partner + lender + year built

You are one of ~46 enrichment agents, each assigned ONE batch file. Working dir: /home/user/Traveling-HFCs.

**Your batch:** `data/batches/batch_<NN>.json` — ~10 properties, each with `census_id`, `name`, `address`,
`city`, `county`, `cad_account`, `sponsor` (the HFC/PFC that now holds title), `tier`, and `year_built`
(may be filled or null). Skim `docs/phase1_verdict.md` once for context on these fee-flip/ground-lease deals.

For **EACH** property, find these THREE fields from **PUBLIC-RECORD / FREE sources ONLY**:

1. **PRIVATE PARTNER** — the private group that owned the apartment building and conveyed it INTO the
   HFC/PFC. Capture BOTH:
   - `private_partner_spe`: the immediate seller/grantor entity — the SPE/LLC that deeded the property to
     the HFC/PFC (the grantor on the special warranty deed to the sponsor; find it in the CAD
     deed/ownership history for the account).
   - `private_partner_parent`: the recognizable PARENT developer/equity firm behind that SPE
     (e.g. S2 Capital, Post Investment Group, WindMass Capital, Ashland Greene) — from news, the firm's
     site, or PR releases.

2. **LENDER** — the mortgage lender / debt holder on the property. FREE sources only: the recorded Deed of
   Trust beneficiary where freely viewable on the county clerk portal, any CAD lien/mortgage field, and
   news/press releases (which routinely name the lender + loan amount, e.g. "LoanCore provided a $58.3M
   loan"). Name the CMBS/CLO trust if the loan was securitized and it's public. Capture lender + loan
   amount if stated. If NO free source shows it: `lender=null`, `lender_gap=true`. Do NOT guess.

3. **YEAR_BUILT** — year of construction. If the batch already has `year_built`, VERIFY against one source
   (confirm or correct). If null, find it (CAD building/structural data, apartments.com, developer press).

**RULES:** FREE public-record sources only (CAD portals, freely-viewable county deed indexes, news,
apartments.com, developer sites, CMBS/CLO surveillance blogs). Cite a source URL for EACH of the three
fields per property. NEVER guess — use null + a note where a free source can't supply it. Do NOT download
bulk appraisal rolls; use targeted per-property lookups (you already have the CAD account + address). Many
county portals block scripted fetches — try curl with a browser user-agent or the r.jina.ai reader proxy.

**OUTPUT:** write `census/enrich/pl_batch_<NN>.json` — a JSON array, one object per property:
```json
{ "census_id","property_name","address","city","county","cad_account",
  "private_partner_spe","private_partner_parent","private_partner_source",
  "lender","lender_loan_amount","lender_source","lender_gap",
  "year_built","year_built_verified","year_built_source","notes" }
```

**RETURN** (final message, tight): # properties done; # lender found vs gap; # partner-parent found;
# year_built confirmed/filled; top blockers.
