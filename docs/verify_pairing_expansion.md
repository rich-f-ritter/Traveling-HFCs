# Wave-1 QA: Pairing & Expansion Audit (Dallas / Tarrant / Bexar)

*Adversarial QA pass, 2026-07-11. Free / public-record sources only (CAD portals, apartment
listing sites, trade press). Inputs audited: `census/county_{dallas,tarrant,bexar}.json` + `.md`,
`data/seed_properties.json`, `data/sponsors.json`, `docs/phase1_verdict.md`.*

## Bottom line (return metrics)

- **Pairings improved vs. unresolvable:** of **84** low-confidence (`single-source`) seed→account
  pairings (Dallas 64, Bexar 20; Tarrant's 53 matched seed rows are all deed-date cross-validated
  and were *not* in scope), **11 improved/resolved with evidence** (incl. 1 bucket where the
  pairing is demonstrably scrambled), **~40 improvable-but-unverified** (a distinguishing partner
  clue exists but was not confirmed this pass), and **37 unresolvable from free sources — keep
  flagged**.
- **Expansions confirmed vs. suspect:** of **65** `TX-NEW-*` expansions checked (Dallas 54,
  Tarrant 5, Bexar 6), **0 are ownership false positives** (every one is owner-of-record under a
  verified sponsor). But only **~34 are genuinely-distinct new multifamily complexes**; **~30 are
  real sponsor parcels that are *not* distinct new properties** (extra CAD accounts of a complex
  already represented by a seed row or another expansion), and **1 is vacant land** (not yet
  multifamily). The "54 net-new Dallas properties / $716M" framing overstates the *property count*
  ~2×; the aggregate dollar value is not double-counted (distinct parcels).
- **Misclassifications:** **0** tier/species/traveling errors vs. the sponsor roster (a genuine
  strength). But **3 systemic classification problems**: (1) an inter-agent `kill_date` convention
  split (Dallas vs. Tarrant record the *identical* fact pattern differently, 119 vs. 33 records);
  (2) ~3 DCAD parcel-description artifacts carried as property names, one implying a non-residential
  use ("LBJ Station **Parking Garage**"); (3) stale §13(e) capital-event dates for the
  Ashland Greene/Pecos cluster (a May-2026 Blackstone foreclosure not reflected).
- **Overall confidence in wave-1 data:** **HIGH** on the entity/ownership/value/tier layer;
  **MODERATE-to-LOW** on the specific `census_id`↔building pairings inside Dallas & Bexar
  multi-property buckets; the distinct-property counts are inflated by parcel fragmentation. The
  core thesis (these 13 sponsors hold a large traveling footprint facing the 2027 cliff) holds up.

---

## Task 1 — Pairing audit

### The universe of uncertainty
The pairing problem is real **only inside same-sponsor + same-city buckets that hold more than one
account.** A `single-source` flag on a record that is the *sole* account in its bucket does **not**
mean the pairing is uncertain — there is only one candidate, so the assignment is forced.

| Category | # records | Meaning |
|---|---:|---|
| **Forced / effectively certain** | 3 | Sole account in its sponsor+city bucket — flag overstates uncertainty |
| **Improvable (distinguishing partner clue)** | 44 | Bucket partner is unique to the row; a partner→building web/deed check *could* verify. Census actually paired by **descending appraised value**, not by clue — so these are best-effort, not verified |
| **Unresolvable from free sources — keep flagged** | 37 | Every row in the bucket shares one partner **and** an identical generic ground-lease comment; nothing free disambiguates which building is which |
| **Total single-source seed pairings** | **84** | Dallas 64 + Bexar 20 (Tarrant's 53 are deed-date cross-validated) |

### Corrections list

**A. RESOLVED / IMPROVED (evidence-backed)**

| census_id | Was (census) | Correction | Evidence / confidence |
|---|---|---|---|
| **TX-43-592** | "LBJ STATION PARKING GARAGE", partner **ZG Companies**, acct `008408000C0090000` | (i) **Rename** → *LBJ Station Apartments* (249-unit community, **not** a parking garage). (ii) **Re-pair**: account is ShainRealty's, not ZG's — see swap below | LBJ Station is a 249-unit apt community (units match); **ShainRealty Capital bought it for $51M and rebranded "Infinity on the Point."** *[REBusinessOnline; Zumper]*. **HIGH** on the multifamily/name fix |
| **TX-37-7585** ↔ **TX-43-592** | ShainRealty→*Tides on Park Lane* (343u); ZG→*LBJ Station* | **Swap the account assignment**: ShainRealty row → **LBJ Station** (249u); ZG row → **Tides on Park Lane** (343u) | ShainRealty is the confirmed operator of LBJ Station; **ZG Companies operates a ~350-unit market/affordable complex** ≈ Tides on Park Lane (343u). *[REBusinessOnline; apartments.com; zgcompanies.com]*. **MODERATE** — the bucket's seed_id↔account pairing is demonstrably scrambled; this is the internally-consistent re-pairing |
| **TX-37-772** | *Infinity on the Oaks* (208u), ShainRealty | **Keep** — consistent | Real 208-unit community, 9236 Church Rd 75231 (units match); ShainRealty's "Infinity"-brand naming fits. *[apartments.com; Yardi Matrix]*. **MEDIUM-HIGH** |
| **TX-37-939198** | "ESTERA LEASING OFFICE" (100u, $18.7M), JPI, acct `00000815847130000` | **Rename** → *Estara*; this is the leasing-office parcel of the **Estara** complex. Note **TX-NEW-DALLAS-35 "ESTARA"** (`00000815847050000`, adjacent account) is the **same complex**, not a distinct property | Adjacent DCAD accounts, same `0000081584 70…` block; a "leasing office" parcel would not carry 100u/$18.7M — those are the complex's. **HIGH** it's one complex |
| **TX-43-1225449** | *Springs at Grand Prairie* (276u), Cityview | **Add aka** → *The Bradbury Apartments* (pairing itself is fine — sole Cityview row, units match) | Seed `sale_comment`: "Cityview leased the **276 unit The Bradbury Apartments** from the Pleasanton HFC." **HIGH** |
| **TX-61-1707** | *Dalian 151* (360u), Dalian Development | **Upgrade** to cross-validated | Partner name = property brand; sister property *Dalian Monterrey Village* confirmed as a Dalian-brand SA community offering "Essential Housing." *[dalianmonterreyvillage.com; apartments.com]*. **HIGH** |
| **TX-43-1153801** (Jefferson Vine, Grand Prairie) · **TX-43-3479** (The Abigail, DeSoto) · **TX-37-1358481** (Presidium Valley View, Farmers Branch) | flagged `single-source` | **Upgrade** — pairing forced (sole account in bucket) | Only one sponsor account in each city bucket; nothing to mispair against. **HIGH** |
| **TX-37-3376** | "DEDICATED CONSERVATION EASEMET/ESCARPMENT" (196u), Ashland Greene/Pecos | **Flag name as a DCAD land-description artifact.** Account/ownership valid; true marketing name **not** resolvable free (Ashland Greene brand candidates) | Ashland Greene's DFW portfolio is Pecos-ground-leased. *[The Real Deal, 4/30/2026]*. Name unresolved — **keep flagged** on the name only |

**B. IMPROVABLE but NOT verified this pass (~36 records).** Each is the only bearer of its partner
inside its bucket, so a partner-name search or a county-clerk grantor/grantee pull *would* pin it —
but the census assigned by appraised-value order, so the specific building is a disclosed
assumption. Examples: Pecos/Irving (Casa Valley=Ashland Greene+Fortress, Avalon 8801=Ashland Greene,
Rancho Mirage=S2, Wythe=Sahara, Jefferson Promenade II=TruAmerica — 5 distinct partners, 5
buildings, but paired by value); Pecos/Dallas single-partner rows (Kendrick=Citadel, The
Marion=Knightvest, Greens of Hickory Trail=NorthMarq, Mariposa=Vino Patel, Casa Bella=Abundance,
Holbrook=AIC); Bexar Pecos (Melia=Austin Capital, Seville=DiversyFund, Vistas Two 52=REEP) and
Pleasanton (Oasis=DB Capital, Trailside=Palladius, Summit=Cottonwood, Durrington Ridge=Leuven).
**Recommendation:** these are the highest-yield targets for a Method-3 deed-index pass.

**C. UNRESOLVABLE FROM FREE SOURCES — KEEP FLAGGED (37 records).** Whole bucket shares one partner
and an identical generic 99-yr ground-lease comment; no free signal disambiguates the buildings:

| Bucket | # | census_ids |
|---|---:|---|
| La Villa / Dallas — **Electra America** | 7 | TX-37-563, -564, -567, -568, -570, TX-43-496, -498, -1340126 |
| Pecos / Dallas — **WindMass Capital** | 5 | TX-37-1092, -1094, -1112 (**two rows both named "The Everly"**), TX-43-1043, -1071 |
| Pleasanton / Dallas — **Polaris Real Estate** | 4 | TX-37-750, -1104, -1153, TX-43-3712 |
| TEHPFC / Dallas — **Nitya Capital** | 4 | TX-43-518, -554, -616, -1018 |
| Pecos / Dallas — **Ashland Greene** | 3 | TX-37-1089, -3376, TX-43-1005 |
| Pecos / Dallas — **Sahara Equity** / **S2 Capital** | 2 / 2 | TX-37-680+TX-43-613 ; TX-37-803+TX-37-1111 |
| Maverick / Dallas — **BLDG Partners** | 2 | TX-43-3448, -3798 |
| Bexar Pecos — **Texsun** ; Bexar Pleasanton — **Ascendant** | 2 / 2 | TX-61-384+TX-61-1321 ; TX-61-1709+TX-61-1175498 |
| Cameron / Dallas — **ShainRealty** (the 2 ShainRealty rows, post-swap) | 2 | TX-37-772, TX-37-7585 |

> Note: mis-pairing inside these buckets corrupts only the *partner / ground-lease metadata* on a
> record, **not** the load-bearing facts (the building exists, is sponsor-owned, and its exemption
> status is read straight off the account). The tier/kill analysis is unaffected.

---

## Task 2 — Expansion audit (`TX-NEW-*`, 65 records)

Tested against the four criteria: (a) multifamily, (b) owned by one of the 13 verified sponsors,
(c) exempt/recently-exempt, (d) not a duplicate of a seed row under a different id.

**(b) Sponsor ownership — SOLID for all 65.** Every expansion was pulled from a CAD owner-name
search that resolves to a verified sponsor entity; the internal consistency check found **0**
off-roster sponsors. Same-name-local-entity risk is low (these are unusual names), and the one real
collision — Garland HFC's own in-City-of-Garland parcels — was **correctly excluded**. Spot-checks
confirmed sponsor ownership: **Sphinx @ Fiji Lofts** (Cameron County HFC + Berkshire Hathaway
Affordable Housing, 301 S. Corinth, Dallas) *[Connect CRE; The Real Deal]*; **Dalian Monterrey
Village** (essential-housing structure) *[apartments.com]*.

**(a) Multifamily — 64/65.** One **SUSPECT**: **TX-NEW-TARRANT-2 "Lofts at Grand Prairie (vacant
land)"** ($288K) — confirmed a **pre-development land-banking parcel** (a future 676-unit ground-up
by WB Property Group at 931 N Day Miar Rd) *[UMoveFree]*. Not yet a multifamily property; the
Tarrant agent already self-flagged it. (Analogous seed-row cases exist but are not expansions:
TX-38-856 "0 Blue Mound Rd vacant land.")

**(c) Exempt/recently-exempt — systemically WEAK, not expansion-specific.** Most Dallas expansions
show no TY2026 exemption (same as the seed rows — 119/132 Dallas records are taxable on the current
roll). Cameron's Sphinx parcels and all TEHPFC expansions do show the exemption. Not treated as
disqualifying because ownership is confirmed and the status is read from the roll.

**(d) Distinctness — the real weakness.** Of the 54 Dallas expansions, **29 are additional CAD
accounts/parcels of a complex already represented**, not new properties:

- **18 share a complex with a SEED row:** Landmark at Lake Village East → seed **TX-43-3702**
  (`TX-NEW-DALLAS-16,17,18,19,20,22,23`); Republic West Apartments → seed **TX-37-1415**
  (`-41,43,44,45,46,47`); Devon on Northgate Ph 2 → seed **TX-43-1510** (`-24`); Greentree Ph II →
  seed **TX-37-1314** (`-26`); Spanish Pueblo → seed **TX-37-567** (`-29`); Chase Place → seed
  **TX-37-568** (`-30`); (+ Landmark at Lake Village **North** `-48`, borderline).
- **11 are intra-expansion duplicates:** **Sphinx @ Fiji Lofts** = ONE 204-unit complex spread
  across 9 records (`-2,3,4,5,7,8,9,10,11`; note `-7` "Sphinx at **Fuji** Lofts" typo, and its
  312u/$3.4M is a unit-count-vs-value artifact); AVA (`-15` dup of `-12/13/14`); Courtney Place
  (`-28` dup of `-27`); Fawn Ridge Village East (`-33` dup of `-32`).
- **+ Estara** (`TX-NEW-DALLAS-35`) = same complex as seed **TX-37-939198** (see Task 1).

So Dallas's 54 collapse to **~24–25 distinct new complexes**. Tarrant's genuinely-new set is 4
(Oak Park, infinity on the landing, The Sydney, Chapparal) + 1 vacant land; Bexar's 6 are all
distinct (Residences at Medical, Highland Ridge, Dalian Monterrey Village, 5 Fifty, Alaro, 410
Probandt). **Verdict: ~34 solid distinct-new / ~30 non-distinct (real but over-counted) / 1 vacant
land / 0 ownership false positives.**

> Data-quality flag: **TX-NEW-BEXAR-2 "Highland Ridge"** is listed at **736 units** — the free
> listing sources describe a mid-size garden community at 1700 Jackson Keller Rd; the 736 figure is
> unverified and likely a bed-count or error. Ownership (Cameron County HFC, per BCAD) stands.

---

## Task 3 — Internal-consistency / misclassification findings

1. **Inter-agent `kill_date` convention split (material).** The identical fact pattern — *sponsor
   owns the parcel; no ad-valorem exemption on the current certified roll* — is recorded two
   different ways: **Dallas** → `kill_date = 2027-01-01` with a gap note (119 records); **Tarrant**
   → `kill_date = "already (pre-2027)"` (33 records). Bexar uses a third convention
   (`first_exempt_tax_year` per account). The Tarrant "already" is a stronger claim than the Dallas
   data supports for the same situation (Dallas itself notes the cause "cannot be determined from
   the roll alone"). **Harmonize** before the counts are aggregated across counties — the
   "already dead" headline is convention-dependent.

2. **Parcel-description artifacts carried as property names** (mislead on use/identity):
   - **TX-43-592** "LBJ STATION **PARKING GARAGE**" → a 249-unit apartment community.
   - **TX-37-3376** "DEDICATED CONSERVATION EASEMET/ESCARPMENT" → a 196-unit Pecos/Ashland Greene apt.
   - **TX-37-939198** "ESTERA **LEASING OFFICE**" → the Estara complex.
   These read as non-residential/ancillary and should be relabeled with the marketing name.

3. **Stale §13(e) capital-event dates (Ashland Greene / Pecos cluster).** Blackstone moved to
   foreclose on Ashland Greene's ~$177M DFW portfolio (**Mateo, Birch, Hawk, Knowlton** — Birch,
   Hawk, Knowlton are **Pecos-ground-leased**), auction ~May 2026 *[The Real Deal 4/30/2026;
   Hoodline]*. The Dallas agent caught **Knowlton** (deed 2026-06-03) but **Birch and Hawk are not
   in the census at all**, and other Ashland Greene/Pecos records (Emerson, Innova, Escarpment)
   still carry `2027-01-01` despite a live 2026 capital event in the same portfolio. Kill dates on
   this cluster are likely early; recommend a deed-date sweep of all Ashland Greene/Pecos parcels.

**Checked and found CONSISTENT (not misclassifications):**
- **Garland HFC "traveling = yes" for Carrollton / Addison / Dallas parcels** (TX-37-1314,
  TX-NEW-DALLAS-25, -26). A county-only test flags these, but the project keys "traveling" on the
  **city** boundary (HB21 §13). Garland HFC sits in the City of Garland; these parcels are outside
  it, and the in-Garland parcels were correctly excluded. **Correctly classified.**
- **Tarrant "already"-killed Tier-1 records** — consistent with that county's headline finding that
  TAD stripped exemptions on post-Feb-2025 deeds; the flag itself is fine (see #1 for the
  cross-county *convention* issue).
- **No record's tier/species/statute disagrees with `data/sponsors.json`** across all 223 records.

---

## Confidence summary

| Layer | Confidence | Basis |
|---|---|---|
| Sponsor / owner-of-record | **HIGH** | 0 off-roster; expansions all sponsor-owned; spot-checks confirm |
| Property existence + appraised value | **HIGH** | CAD accounts real; units/values check out on spot-checks |
| Tier / species / statute | **HIGH** | Internally consistent with Phase-1 roster |
| Traveling flag | **HIGH** | City-boundary test applied correctly |
| `census_id` ↔ specific building (Tarrant) | **HIGH** | Deed-date cross-validated per account |
| `census_id` ↔ specific building (Dallas/Bexar multi-property buckets) | **LOW–MODERATE** | 84 single-source pairings; 37 unresolvable free; ≥1 bucket demonstrably scrambled |
| Distinct-property **counts** (expansions) | **OVERSTATED** | ~30 of 65 expansions are non-distinct parcels |
| Kill-date timing / conventions | **MODERATE** | Cross-county convention split; stale §13(e) dates |

*Sources cited inline: dallascad.org / tad.org / bexar.trueautomation.com (CAD rolls);
REBusinessOnline, The Real Deal, Connect CRE, Hoodline, Multi-Housing News (trade press);
apartments.com, Zumper, Yardi Matrix, UMoveFree, dalianmonterreyvillage.com, zgcompanies.com
(listings/owner sites). All free / public-record.*
