# Phase 4 — Top-40 Tier-1 HFC Properties Ranked by Annual Tax at Stake

*Enrichment overlay for `census/enrich_foregone_tax.json`. Compiled 2026-07-11. Scope: the 40 highest Tier-1 (Ch. 394 HFC) properties by `exemption.appraised_value` across the three completed counties (Dallas, Tarrant, Bexar). Ranks by **annual foregone tax at stake**, not appraised value.*

## Method

`annual_foregone_tax_est = exemption.appraised_value (TY2026 certified) × the property's combined TY2025 local ad valorem rate` (most recent fully-adopted/certified combined rate; TY2026 rates are not set until Aug–Oct 2026). Each property's exact taxing-jurisdiction combination (county + city + the specific ISD + college/hospital/special districts) was resolved per-account from the appraisal district's own jurisdiction table, because Dallas, Irving, Grand Prairie and Fort Worth each straddle multiple ISDs. Rates are public-record (DCAD / Dallas County Tax Office; TAD / Tarrant County; BCAD / Bexar Tax Assessor-Collector). No rate is guessed — see `sources[]` per record in the JSON.

## Headline numbers

| Metric | Value |
|---|---|
| Properties ranked | 40 |
| With a foregone-tax estimate | 40 / 40 |
| With a unit count | 34 / 40 (6 Tarrant lack a free-source unit count) |
| **Total annual tax at stake across the top 40** | **$59,671,515** |
| — of which **currently BILLED** (exemption already stripped) | $39,318,296 |
| — of which **still exempt** (at risk at the 1/1/2027 HB21 cliff) | $20,353,218 |

**Key distinction (per the brief):** many of these are *not* prospectively exempt — the exemption has already been stripped and the property is on the roll at full taxable value **today**. For those (`currently_exempt = no`), the figure is the tax **now being billed**; the "foregone" framing applies to the jurisdiction only if the HFC wins it back in litigation. For `currently_exempt = yes`, the figure is the tax that returns to the rolls at the 2027 cliff (or on an earlier §13(e) capital event). All 23 Dallas top-40 properties are already fully taxable on the TY2026 DCAD roll; Tarrant is split; the 5 Bexar top-40 remain exempt (first exempt TY2025).

## Ranked table — by annual tax at stake

| # | Property | City | County | Sponsor | Units | Appraised value | Combined TY2025 rate | **Annual tax at stake** | Currently exempt? | First exempt yr |
|---|---|---|---|---|---:|---:|---:|---:|:--:|:--:|
| 1 | JEFFERSON PROMENADE II | Irving | Dallas | Pecos | 433 | $101,520,700 | 2.8391% | **$2,882,254** | no | — |
| 2 | INNOVA | Dallas | Dallas | Pecos | 430 | $113,950,000 | 2.2267% | **$2,537,336** | no | — |
| 3 | Monarch Pass Apartment Homes | Fort Worth | Tarrant | Cameron | — | $96,000,000 | 2.3123% | **$2,219,789** | yes | 2023 |
| 4 | LAS COLINAS HEIGHTS | Irving | Dallas | Cameron | 513 | $87,210,000 | 2.1391% | **$1,865,492** | no | — |
| 5 | MARQUIS AT PARK CENTRAL | Dallas | Dallas | Pleasanton | 308 | $76,010,140 | 2.3381% | **$1,777,178** | no | — |
| 6 | JEFFERSON VINE | Grand Prairie | Dallas | Pecos | 380 | $76,000,000 | 2.2568% | **$1,715,138** | no | — |
| 7 | Oak Park | Euless | Tarrant | Cameron | 608 | $81,900,000 | 2.0497% | **$1,678,680** | yes | 2024 |
| 8 | Jefferson Fossil Creek | Haltom City | Tarrant | Pecos | — | $73,200,000 | 2.2927% | **$1,678,234** | yes | 2025 |
| 9 | ARBORSTONE II   CORAL CREEK APTS | Dallas | Dallas | Pecos | 536 | $75,000,000 | 2.2267% | **$1,670,032** | no | — |
| 10 | The Sydney | Mansfield | Tarrant | Pleasanton | 354 | $70,900,000 | 2.3290% | **$1,651,247** | yes | 2025 |
| 11 | TEAK APTS | Dallas | Dallas | La Villa | 316 | $73,000,000 | 2.2267% | **$1,625,498** | no | — |
| 12 | KENDRICK | Dallas | Dallas | Pecos | 405 | $68,850,000 | 2.3381% | **$1,609,768** | no | — |
| 13 | THE LOFT APARTMENT OF ADDISON | Addison | Dallas | Garland | 353 | $75,044,080 | 2.1360% | **$1,602,949** | no | — |
| 14 | Durrington Ridge | San Antonio | Bexar | Pleasanton | 398 | $69,000,000 | 2.2675% | **$1,564,557** | yes | 2025 |
| 15 | Stillwater Crystal Springs Apts | Fort Worth | Tarrant | Pecos | 387 | $67,300,000 | 2.3123% | **$1,556,164** | no | — |
| 16 | Cortland Riverside | Fort Worth | Tarrant | Pleasanton | 374 | $65,400,000 | 2.3792% | **$1,555,984** | no | — |
| 17 | EQUINOX ON THE PARK | Garland | Dallas | Pleasanton | 338 | $64,000,000 | 2.3947% | **$1,532,621** | no | — |
| 18 | The Dawnson at Berksire | Fort Worth | Tarrant | Pleasanton | — | $66,500,000 | 2.2176% | **$1,474,691** | yes | 2026 |
| 19 | JEFFERSON AT MONTFORT APT | Dallas | Dallas | La Villa | 336 | $66,082,800 | 2.2267% | **$1,471,472** | no | — |
| 20 | JEFFERSON AT MONTFORT II | Dallas | Dallas | La Villa | 326 | $64,116,050 | 2.2267% | **$1,427,678** | no | — |
| 21 | KADE | Dallas | Dallas | Pecos | 348 | $64,000,000 | 2.2267% | **$1,425,094** | no | — |
| 22 | Jefferson North Collins | Arlington | Tarrant | Pecos | 344 | $68,000,000 | 2.0328% | **$1,382,338** | yes | 2025 |
| 23 | The Sovereign | Fort Worth | Tarrant | Maverick | — | $60,500,000 | 2.2804% | **$1,379,630** | yes | 2025 |
| 24 | RANCHO MIRAGE | Irving | Dallas | Pecos | 310 | $65,086,730 | 2.0713% | **$1,348,128** | no | — |
| 25 | THE EMERSON | Dallas | Dallas | Pecos | 486 | $56,303,680 | 2.3381% | **$1,316,425** | no | — |
| 26 | Sterling at Oak Hills | San Antonio | Bexar | Maverick | 330 | $57,000,000 | 2.2902% | **$1,305,399** | yes | 2025 |
| 27 | LA COSTA VILLA | Dallas | Dallas | Maverick | 260 | $53,840,380 | 2.3381% | **$1,258,831** | no | — |
| 28 | Dalian 151 | San Antonio | Bexar | Cameron | 360 | $54,500,000 | 2.2902% | **$1,248,145** | yes | 2025 |
| 29 | SPRINGS AT GRAND PRAIRIE | Grand Prairie | Dallas | Pleasanton | 276 | $54,898,400 | 2.2568% | **$1,238,925** | no | — |
| 30 | Rocklyn Apartments | Fort Worth | Tarrant | Pleasanton | 272 | $53,400,000 | 2.3123% | **$1,234,758** | yes | 2026 |
| 31 | Nova Apartments | San Antonio | Bexar | Pleasanton | 412 | $53,500,000 | 2.2902% | **$1,225,243** | yes | 2025 |
| 32 | Neuhaus Lake Worth Apts | Lake Worth | Tarrant | Pleasanton | — | $54,700,000 | 2.2165% | **$1,212,436** | no | — |
| 33 | REPUBLIC WEST APARTMENTS | Garland | Dallas | Pecos | 410 | $50,090,050 | 2.3947% | **$1,199,516** | no | — |
| 34 | THE EVERLY | Dallas | Dallas | Pecos | 420 | $51,234,870 | 2.3381% | **$1,197,912** | no | — |
| 35 | THE ABBOTT | Dallas | Dallas | Pecos | 332 | $53,500,000 | 2.2267% | **$1,191,290** | no | — |
| 36 | Dalian Monterrey Village | San Antonio | Bexar | Cameron | 360 | $51,500,000 | 2.2902% | **$1,179,440** | yes | 2025 |
| 37 | Northpoint Villas | Fort Worth | Tarrant | Pleasanton | — | $49,600,000 | 2.2804% | **$1,131,068** | yes | 2025 |
| 38 | LIVE OAKS AT THE BRANCH | Dallas | Dallas | La Villa | 196 | $49,500,000 | 2.2267% | **$1,102,221** | no | — |
| 39 | MONTORO APARTMENTS | Irving | Dallas | Cameron | 324 | $48,600,000 | 2.1391% | **$1,039,593** | no | — |
| 40 | BRIARCREST APTS | Carrollton | Dallas | Pecos | 238 | $47,450,990 | 2.0197% | **$958,358** | no | — |

*Sponsor column abbreviates "Housing Finance Corporation." "Currently exempt = no" means the exemption is already off the roll and the tax is being billed now.*

## Top 5 by dollars at stake

1. **JEFFERSON PROMENADE II** (Irving, Dallas) — $2,882,254/yr on $101,520,700 at 2.8391% — *already billed (exemption stripped)*.
2. **INNOVA** (Dallas, Dallas) — $2,537,336/yr on $113,950,000 at 2.2267% — *already billed (exemption stripped)*.
3. **Monarch Pass Apartment Homes** (Fort Worth, Tarrant) — $2,219,789/yr on $96,000,000 at 2.3123% — *still exempt — returns to roll at 2027 cliff*.
4. **LAS COLINAS HEIGHTS** (Irving, Dallas) — $1,865,492/yr on $87,210,000 at 2.1391% — *already billed (exemption stripped)*.
5. **MARQUIS AT PARK CENTRAL** (Dallas, Dallas) — $1,777,178/yr on $76,010,140 at 2.3381% — *already billed (exemption stripped)*.

## Notable rate findings

- **Jefferson Promenade II** (Irving, #1) carries the extra **Dallas County Utility & Reclamation District (DCURD)** at 0.70/$100 — the Las Colinas/Valley Ranch reclamation district — pushing its combined rate to 2.8391%, far above peers and making it the single largest annual bill despite ranking only #2 by appraised value.
- Five North Dallas / Lake Highlands HFC properties (Marquis at Park Central, Kendrick, The Emerson, La Costa Villa, The Everly) sit in **Richardson ISD**, not Dallas ISD — a materially higher ISD rate (1.1052 vs 0.9938).
- **Fort Worth** combined rates below are core (County + College + JPS + City + ISD) and omit the Tarrant Regional Water District (~0.026/$100) that TAD lists as a 6th/7th unit — so those seven estimates are ~1% conservative.
- **Bexar**: the four Northside-ISD properties share 2.2902%; Durrington Ridge (North East ISD) is 2.2675%. Note BCAD's figures apply the TY2025 rate to the TY2026 value; where the appraised value moved year-over-year the true TY2025 bill differs (e.g. Nova Apartments was ~$120k higher in TY2025).

## Gaps

- **Units missing (6, all Tarrant/Fort Worth):** Monarch Pass, Jefferson Fossil Creek, The Dawson at Berkshire, The Sovereign, Neuhaus Lake Worth, Northpoint Villas — TAD publishes no unit count and no free listing gave a reliable total. **Oak Park (Euless)** unit count (608, Apartment Finder) conflicts across sources and is low-confidence.
- **first_exempt_tax_year** could not be recovered for the 23 Dallas properties: DCAD's roll shows them carried at full taxable value with no prior-year exempt value posted, so the year the exemption first attached is not reconstructable from the free roll alone.
- **Fort Worth rates** exclude the ~0.026/$100 TRWD (and one further district on Cortland Riverside), a known ~1% understatement.
- **Northwest ISD** rate (The Dawson at Berkshire) reflects a Nov-2025 VATRE; treated as the adopted TY2025 rate but carries slightly lower confidence than the consolidated-table entries.
