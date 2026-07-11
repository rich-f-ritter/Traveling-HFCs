# 03 — Source Directory: verified portals, contacts, costs, procedures

Status legend: **[V]** = fetched live and adversarially verified 7/11/2026; **[S]** =
standard source from earlier research, confirm on first use.

## State

| Source | URL / contact | What it yields | Cost / notes |
|---|---|---|---|
| **[V]** TDHCA HFC monitoring | tdhca.texas.gov/housing-finance-corporation-compliance-monitoring · hfc@tdhca.texas.gov | §394.9027 audit filings + published findings (the HFC census) | free; lists "TBD" as of 7/11/26 — repull ~Aug 2026 |
| **[V]** TDHCA PFC monitoring | tdhca.texas.gov/public-facilities-corporation-compliance-monitoring | §303.0426 PFC filings | free |
| **[V]** Ch. 394 statute (static text) | tdhca.texas.gov/sites/default/files/pmcdocs/Ch394-LGC.pdf | certified statute PDF (capitol site serves a JS shell to scripts) | free |
| **[V]** HB 21 enrolled | capitol.texas.gov/tlodocs/89R/billtext/html/HB00021F.htm | the operative reform text incl. §13 transition rules | free |
| **[S]** HB 2071 enrolled | capitol.texas.gov/tlodocs/88R/billtext/html/HB02071F.htm | PFC-side reform | free |
| **[V]** AG opinion files | texasattorneygeneral.gov (request files; RQ-0566-KP PDF verified live) | opinion requests/opinions on HFC legality | free |
| **[S]** Comptroller taxable-entity search | mycpa.cpa.state.tx.us/coa/ | entity status, registered agents — free alternative to SOS | free |
| **[S]** SOSDirect | sos.state.tx.us | formation docs, filing history, **UCC search** | ~$1/search |

## Courts

| Source | URL | What it yields |
|---|---|---|
| **[S]** Appellate dockets/briefs | search.txcourts.gov | 15th COA 15-25-00110-CV & -00111-CV (Pleasanton injunction appeals); Ft Worth COA 02-25-00474-CV; free PDFs of orders/briefs |
| **[S]** Trial courts | re:SearchTX (research.txcourts.gov) | district-court filings; sweep sponsor + property names |

## Counties (pattern; Harris verified as the model)

| Source | URL / contact | Notes |
|---|---|---|
| **[V]** Harris Co. Clerk real property | cclerk.hctx.net/applications/websearch/**RP.aspx** | file-number, grantor/grantee, film-code, instrument-type search; free account → free watermarked viewing (post-2000); $1/page plain, $5+$1/page certified; plats $10/page; cart+email delivery |
| **[V]** Harris Co. Tax Office | hctax.net/Property/ViewStatementReceipts | statements + payment receipts by account, free; data lags print date |
| **[V]** HCAD search | search.hcad.org (browser-only; Cloudflare-gated) | record card, exemption status, value history |
| **[V]** HCAD open records | hcad.org/hcad-help/open-records-request | TPIA route to exemption applications (Tax Code §11.48 partial confidentiality — expect redactions/AG ruling ~45d) |
| **[V]** HCAD ARB history | hcad.org/hcad-online-services/protest-hearings-database | protest history by account (200-result cap) |
| **[S]** Other big CADs | dcad.org, tad.org, bcad.org, traviscad.org, etc. | most offer bulk roll exports for Method-2 sweeps |
| **[S]** Multi-county clerk aggregators | TexasFile, CourthouseDirect | one-name-many-counties sweeps, ~$1–3/doc |

## The Pleasanton/PHFC channel (the archetype sponsor)

| Item | Detail |
|---|---|
| **[V]** TPIA portal | **cityofpleasantontx.nextrequest.com** — the designated channel (§552.234: use it, not arbitrary email). Browse `/requests` and `/documents` first — prior productions are public and may already contain what you need |
| **[V]** Custodian | City Secretary **Andres Aguirre**, aaguirre@pleasantontx.gov, 830-569-3867 x216, 108 Second St, Pleasanton TX 78064 |
| **[V]** PHFC facts | created by Pleasanton City Council 3/14/2023; registered agents: City Mgr Johnny Huizar; atty Carey Troell (Cantu Harden Montoya LLP) |
| **[V]** TPIA clock | §552.221: production "promptly"; 10 business days = written-certification deadline, not absolute; calendar day-10 follow-up |

## Loan/distress overlay

| Source | Detail |
|---|---|
| **[S]** Morningstar DBRS | dbrs.morningstar.com — issuer pages for CRE CLOs (e.g., LoanCore 2021-CRE6, issuer 27765); surveillance reports free with registration |
| **[S]** Computershare ctslink | ctslink.com — monthly remittance reports; register as prospective investor (144A certification) |
| **[S]** Trepp / CRED iQ | subscription loan-level: special-servicing transfers, maturity/extension status, servicer commentary; CRED iQ blog names distressed CRE-CLO loans free |

## Known refuted routes (do NOT use)

- ~~"Underwriting assessment published on the HFC's own website + comptroller-form
  exemption application to TDHCA/CAD"~~ — refuted 0-3; the route is TPIA (§394.0045) and
  the §394.9027 audit via TDHCA.
- ~~HB 2071 "$40/unit audit fee, retroactive to all pre-existing PFC deals" and the
  specific 12% very-low-income tier formula~~ — refuted 0-3; re-verify PFC specifics
  against the enrolled text before publishing.
