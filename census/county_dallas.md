# Dallas County -- Traveling HFC/PFC Census (Phase 3)

**Scope:** 78 Matrix-seed rows for Dallas County + 54 expansion properties discovered via a DCAD (dallascad.org) bulk appraisal-roll sweep (Method 2). 76/78 seed rows carry a DCAD-confirmed address/account; 2 could not be isolated to a specific parcel from free public data.

**Total appraised value captured (132 properties): $3,885,721,680** ($3,169,464,710 across the 78 seed-linked records + $716,256,970 across the 54 net-new expansion records).

## Headline finding: most of these parcels are NOT currently exempt

Cross-referencing DCAD's own TOTAL_EXEMPTION / ACCT_EXEMPT_VALUE tables against the 123 traveling, unit-bearing parcels confirmed under our 8 Dallas-relevant sponsors' names: only **11** show a public-property ad valorem exemption in effect for **tax year 2026**; **119** are carried at full taxable value (city/county/ISD taxable value = full appraised value) despite sponsor-of-record ownership. Practically all of Pecos, Pleasanton, Edcouch, La Villa, and Maverick HFC's Dallas-County holdings are currently TAXABLE on the certified roll; only Cameron County HFC (partial), Garland HFC (mostly, on its traveling parcels), and Texas Essential Housing PFC (all) show the exemption actually posted. This cannot be fully explained from the roll alone -- candidate causes include exemption applications still pending for recently-acquired (2025) parcels, non-filing of the §394.9027 TDHCA compliance audit (which forfeits the exemption for the year), or the various city/CAD challenges catalogued in Phase 1. See `gaps` on each record.

## Independently-discovered capital events (pre-2027 exits)

The DCAD deed-transfer dates surfaced **6 parcels** (6 seed-linked) where the sponsor HFC has already been replaced as owner of record, ahead of the 1/1/2027 §13(i) cliff:

- **The Bernard / Beckham / Blake / Bentley / Baxter Apartments** (the old 1,487-unit "Brooklyn @9669" portfolio split, ~1,437 units combined) -- all five sold together on **4/7/2026** (recorded 4/8/2026, DCAD instrument INT202600073067) to **Oconee Real Estate Holdings XIX / BX5 LLC**, out of Pecos HFC ownership. DCAD's own condition field flags the Bentley and Baxter accounts 55% and 56% vacant -- consistent with a distressed/lender-driven disposition.
- **Knowlton Apartment Homes** (Mesquite, 412 units) -- sold **6/3/2026** (recorded 6/4/2026, instrument INT202600120366) to **Stonelex I 2 LLC c/o Blackstone Mortgage Trust**, a lender/special-servicer-style vehicle, out of Pecos HFC ownership.

Both are treated in the JSON as §13(e) early-death events with `kill_date_estimate` set to the actual DCAD deed date rather than 2027-01-01.

Separately, **Ash at the Branch** and **Cedar at the Branch** (part of the same La Villa HFC "at the Branch" portfolio as Teak Apts and Live Oaks at the Branch) are still recorded to **S2 Ash LP / S2 Cedar LP** on the 2026 roll, not to La Villa HFC -- independently corroborating the seed's own note that the La Villa transfer was an *"unrecorded sale."*

## Method

1. Downloaded DCAD's free bulk 2026 Current appraisal-roll export (`dallascad.org/DataProducts.aspx` > DCAD2026_CURRENT.ZIP) and filtered ACCOUNT_INFO.CSV owner fields for the 8 verified sponsor entities appearing in Dallas seed rows (Cameron County HFC, Edcouch Community HFC, Garland HFC, La Villa HFC, Maverick County HFC, Pecos HFC, Pleasanton HFC, Texas Essential Housing PFC), handling DCAD's owner-name truncation/wraparound into the address-line fields.
2. Joined matches against ACCOUNT_APPRL_YEAR (values), COM_DETAIL (property name/units/year built), TOTAL_EXEMPTION and ACCT_EXEMPT_VALUE (exemption status).
3. Grouped accounts into 134 distinct properties by site address; excluded 11 parcels located within the City of Garland itself (Garland HFC's home jurisdiction -- non-traveling, out of HB21 §13(i)'s scope, analogous to Houston HA's local portfolio in Phase 1).
4. Linked 12 seed rows to specific properties by name (sale_comment text cross-referenced against DCAD's COM_DETAIL.PROPERTY_NAME -- e.g. "Melville", "The Holden", "The Charlie", the Brooklyn @9669 split). Linked a further 64 seed rows to DCAD parcels within the same sponsor+city bucket (paired by descending appraised value where a bucket held more than one candidate) -- **these bucket pairings are NOT independently verified beyond sponsor/city/tier and are flagged `single-source` with a gap note on every such record.**
5. The 54 DCAD-confirmed properties left over after seed-linking became expansion records `TX-NEW-DALLAS-1..54`. Two seed rows (Pecos in Rowlett; Pleasanton in Dallas) had no remaining DCAD candidate in their bucket and carry no property match.

## Table: all 132 properties

| census_id | sponsor | property | city | CAD account | units | appraised value | TY26 exempt? | first-exempt yr | kill date |
|---|---|---|---|---|---|---|---|---|---|
| TX-43-592 | Cameron County HFC | LBJ STATION PARKING GARAGE | Dallas | 008408000C0090000 | 249 | $40,375,000 | N | — | 2027-01-01 |
| TX-37-7585 | Cameron County HFC | TIDES ON PARK LANE | Dallas | 00000368152000000 | 343 | $36,325,970 | N | — | 2027-01-01 |
| TX-37-772 | Cameron County HFC | INFINITY ON THE OAKS | Dallas | 00000792887000000 | 208 | $28,500,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-1 | Cameron County HFC | ESTRELLA  AT KIEST (ALL BILLS) | Dallas | 00000657048000100 | 232 | $20,533,930 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-2 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335533000000 | 32 | $6,755,030 | Y | — | 2027-01-01 |
| TX-NEW-DALLAS-3 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335536000000 | 32 | $6,741,050 | Y | — | 2027-01-01 |
| TX-NEW-DALLAS-4 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335560000000 | 30 | $6,736,940 | Y | — | 2027-01-01 |
| TX-NEW-DALLAS-5 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335548000000 | 30 | $6,726,590 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-6 | Cameron County HFC | LAKE JUNE VILLAGE | Dallas | 00000624321000000 | 100 | $3,585,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-7 | Cameron County HFC | SPHINX AT FUJI LOFTS | Dallas | 00000335581000000 | 312 | $3,388,990 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-8 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335539000000 | 16 | $3,385,300 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-9 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335578000000 | 16 | $3,378,330 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-10 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335563000000 | 16 | $3,372,160 | Y | — | 2027-01-01 |
| TX-NEW-DALLAS-11 | Cameron County HFC | SPHINX AT FIJI LOFTS | Dallas | 00000335566000000 | 16 | $3,371,880 | N | — | 2027-01-01 |
| TX-43-1496 | Cameron County HFC | LAS COLINAS HEIGHTS | Irving | 32065600000010000 | 513 | $87,210,000 | N | — | 2027-01-01 |
| TX-43-1599 | Cameron County HFC | MONTORO APARTMENTS | Irving | 32441150000000000 | 324 | $48,600,000 | N | — | 2027-01-01 |
| TX-43-3829 | Edcouch HFC | INFINITY ON YORKTOWN | Dallas | 006816000A0010000 | 226 | $38,500,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-12 | Edcouch HFC | AVA WEST I | Dallas | 00000791118050000 | 272 | $25,000,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-13 | Edcouch HFC | AVA NORTH | Dallas | 00000791118080000 | 248 | $22,000,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-14 | Edcouch HFC | AVA WEST II | Dallas | 00000791118060000 | 200 | $20,000,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-15 | Edcouch HFC | AVA APARTMENTS | Dallas | 008107000C0010000 | 160 | $18,000,000 | N | — | 2027-01-01 |
| TX-43-3702 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 60 UNITS | Garland | 26178690010030000 | 60 | $7,820,160 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-16 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 57 UNITS | Garland | 26595600010010000 | 57 | $7,302,600 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-17 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 54 UNITS | Garland | 26178690010030100 | 54 | $6,604,800 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-18 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 28 UNITS | Garland | 26178580030010100 | 28 | $3,776,670 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-19 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 28 UNITS | Garland | 26178650020010000 | 28 | $3,744,420 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-20 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 28 UNITS | Garland | 26178710030030200 | 28 | $3,744,420 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-21 | Edcouch HFC | TIDES AT LAKE VILLAGE - 32 UNITS | Garland | 26178300010030800 | 32 | $3,693,300 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-22 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 20 UNITS | Garland | 26178650010010100 | 20 | $2,577,220 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-23 | Edcouch HFC | LANDMARK AT LAKE VILLAGE EAST - 14 UNITS | Garland | 26178630020020200 | 14 | $1,841,150 | N | — | 2027-01-01 |
| TX-43-1510 | Edcouch HFC | DEVON ON NORTHGATE | Irving | 321100000A0010000 | 260 | $38,883,930 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-24 | Edcouch HFC | DEVON ON NORTHGATE PH 2 | Irving | 321100000A0010100 | 188 | $28,116,070 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-25 | Garland HFC | THE LOFT APARTMENT OF ADDISON | Addison | 104500000A0010000 | 353 | $75,044,080 | N | — | 2027-01-01 |
| TX-37-1314 | Garland HFC | GREENTREE APTS | Carrollton | 14065900000010000 | 237 | $33,439,520 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-26 | Garland HFC | GREENTREE APARTMENTS PHASE II | Carrollton | 14041070000010000 | 128 | $18,060,480 | N | — | 2027-01-01 |
| TX-37-4278 | La Villa HFC | TEAK APTS | Dallas | 005403000A0010000 | 316 | $73,000,000 | N | — | 2027-01-01 |
| TX-37-1116 | La Villa HFC | JEFFERSON AT MONTFORT APT | Dallas | 008166000B01B0000 | 336 | $66,082,800 | N | — | 2027-01-01 |
| TX-43-1340126 | La Villa HFC | JEFFERSON AT MONTFORT II | Dallas | 008166000F01B0000 | 326 | $64,116,050 | N | — | 2027-01-01 |
| TX-43-496 | La Villa HFC | LIVE OAKS AT THE BRANCH | Dallas | 005403000B0010000 | 196 | $49,500,000 | N | — | 2027-01-01 |
| TX-43-498 | La Villa HFC | SPANISH CREEK APTS-TXA19950410 | Dallas | 00000595754000000 | 302 | $33,220,000 | N | — | 2027-01-01 |
| TX-37-563 | La Villa HFC | CAROUSEL COURT/LOW HOUSING | Dallas | 005984000007A0000 | 278 | $28,877,680 | N | — | 2027-01-01 |
| TX-37-564 | La Villa HFC | THE BROOKMOORE (59% OCCUPIED) | Dallas | 00000474118000000 | 152 | $20,927,220 | N | — | 2027-01-01 |
| TX-37-567 | La Villa HFC | SPANISH PUEBLO | Dallas | 00000595780580000 | 128 | $20,041,330 | N | — | 2027-01-01 |
| TX-37-568 | La Villa HFC | CHASE PLACE | Dallas | 00000595729000000 | 125 | $19,375,000 | N | — | 2027-01-01 |
| TX-37-570 | La Villa HFC | ANDORA | Dallas | 00000595753420000 | 136 | $18,128,980 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-27 | La Villa HFC | COURTNEY PLACE (ECU) | Dallas | 00000595741000000 | 115 | $17,136,470 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-28 | La Villa HFC | COURTNEY PLACE (ECU) | Dallas | 00000595735000000 | 106 | $17,063,360 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-29 | La Villa HFC | SPANISH PUEBLO APARTMENTS | Dallas | 00000595781000000 | 96 | $15,070,980 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-30 | La Villa HFC | CHASE PLACE | Dallas | 00000595738000000 | 81 | $14,842,150 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-31 | La Villa HFC | MESA RIDGE VILLAGE EAST ((ECU 49% VACANT)) | Dallas | 00000474083000000 | 140 | $13,566,350 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-32 | La Villa HFC | FAWN RIDGE VILLAGE EAST (ECU 49% VACANT) | Dallas | 00000474154000000 | 48 | $4,736,270 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-33 | La Villa HFC | FAWN RIDGE VILLAGE EAST (ECU 49% VACANT) | Dallas | 00000474151000000 | 32 | $3,157,520 | N | — | 2027-01-01 |
| TX-37-4241 | La Villa HFC | Ash at the Branch | Dallas | 005403000B0020000 | 402 | — | N | — | 2027-01-01 |
| TX-37-4277 | La Villa HFC | Cedar at the Branch | Dallas | 005403000B0030000 | 321 | — | N | — | 2027-01-01 |
| TX-43-3448 | Maverick County HFC | LA COSTA VILLA | Dallas | 007731000A0010000 | 260 | $53,840,380 | N | — | 2027-01-01 |
| TX-43-3798 | Maverick County HFC | GABLES UPTOWN TOWER | Dallas | 000970001207A0000 | 196 | $42,343,390 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-34 | Maverick County HFC | DELAFIELD VILLAS-TXA20050340 | Dallas | 006209000A0010000 | 204 | $21,218,660 | N | — | 2027-01-01 |
| TX-37-1294 | Pecos HFC | BRIARCREST APTS | Carrollton | 14006580000000000 | 238 | $47,450,990 | N | — | 2027-01-01 |
| TX-37-1320 | Pecos HFC | THE HOLDEN | Carrollton | 14107320000010000 | 320 | $44,400,000 | N | — | 2027-01-01 |
| TX-43-1005 | Pecos HFC | INNOVA | Dallas | 002006001801D0000 | 430 | $113,950,000 | N | — | 2027-01-01 |
| TX-43-1043 | Pecos HFC | ARBORSTONE II   CORAL CREEK APTS | Dallas | 006938000A01A0000 | 536 | $75,000,000 | N | — | 2027-01-01 |
| TX-43-1065 | Pecos HFC | KENDRICK | Dallas | 008125000501D0000 | 405 | $68,850,000 | N | — | 2027-01-01 |
| TX-43-1071 | Pecos HFC | KADE | Dallas | 005703004A0010000 | 348 | $64,000,000 | N | — | 2027-01-01 |
| TX-37-1089 | Pecos HFC | THE EMERSON | Dallas | 0080690B0001A0000 | 486 | $56,303,680 | N | — | 2027-01-01 |
| TX-37-1092 | Pecos HFC | THE ABBOTT | Dallas | 007209000A0040000 | 332 | $53,500,000 | N | — | 2027-01-01 |
| TX-37-1094 | Pecos HFC | THE EVERLY | Dallas | 0080700A000010100 | 420 | $51,234,870 | N | — | 2027-01-01 |
| TX-37-1111 | Pecos HFC | PRESTON GREENS | Dallas | 00000799898000000 | 257 | $47,204,360 | N | — | 2027-01-01 |
| TX-37-1112 | Pecos HFC | THE EVERLY | Dallas | 0080700A000010000 | 354 | $43,439,470 | N | — | 2027-01-01 |
| TX-37-1315618 | Pecos HFC | The Blake Apartments | Dallas | 00842100060010000 | 309 | $40,177,090 | N | — | 2026-04-07 |
| TX-37-696 | Pecos HFC | Melville Apartments | Dallas | 00000737176000000 | 356 | $40,000,000 | N | — | 2027-01-01 |
| TX-37-1173 | Pecos HFC | VILLAGE ON THE GREEN | Dallas | 00C79640000000100 | 202 | $39,200,000 | N | — | 2027-01-01 |
| TX-43-1324461 | Pecos HFC | MARIPOSA VILLA APTS HOMES | Dallas | 00767100130010000 | 216 | $39,000,000 | N | — | 2027-01-01 |
| TX-37-1315617 | Pecos HFC | The Beckham Apartments | Dallas | 00842100060070000 | 260 | $38,923,350 | N | — | 2026-04-07 |
| TX-37-1315615 | Pecos HFC | The Bernard Apartments | Dallas | 00842100060020000 | 314 | $38,342,570 | N | — | 2026-04-07 |
| TX-37-3376 | Pecos HFC | DEDICATED CONSERVATION EASEMET/ESCARPMENT | Dallas | 00000818285800000 | 196 | $37,129,080 | N | — | 2027-01-01 |
| TX-37-1315619 | Pecos HFC | The Bentley Apartments | Dallas | 00842100060060200 | 284 | $35,269,050 | N | — | 2026-04-07 |
| TX-37-3624 | Pecos HFC | GREENS OF HICKORY TRAIL | Dallas | 007553000A0080000 | 250 | $35,000,000 | N | — | 2027-01-01 |
| TX-37-1315620 | Pecos HFC | The Baxter Apartments | Dallas | 00842100060030000 | 270 | $29,537,650 | N | — | 2026-04-07 |
| TX-37-4271 | Pecos HFC | THE MARION | Dallas | 00000791059100000 | 326 | $29,446,970 | N | — | 2027-01-01 |
| TX-43-613 | Pecos HFC | TIDES OF LAWLER EAST | Dallas | 008432000C0010000 | 220 | $27,000,000 | N | — | 2027-01-01 |
| TX-37-680 | Pecos HFC | HOLBROOK | Dallas | 00675500020010000 | 232 | $26,295,380 | N | — | 2027-01-01 |
| TX-43-712 | Pecos HFC | HOLBROOK | Dallas | 00675500020020000 | 232 | $26,295,160 | N | — | 2027-01-01 |
| TX-37-803 | Pecos HFC | WESTWOOD APTS | Dallas | 00000660352500000 | 187 | $25,071,420 | N | — | 2027-01-01 |
| TX-37-826 | Pecos HFC | CASA BELLA (2019 RENO) | Dallas | 00000725357000000 | 176 | $25,000,000 | N | — | 2027-01-01 |
| TX-37-1155 | Pecos HFC | THE CHARLIE | Dallas | 0086780A000020000 | 314 | $24,500,000 | N | — | 2027-01-01 |
| TX-37-939198 | Pecos HFC | ESTERA LEASING OFFICE | Dallas | 00000815847130000 | 100 | $18,720,440 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-35 | Pecos HFC | ESTARA | Dallas | 00000815847050000 | 116 | $17,073,560 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-36 | Pecos HFC | WYNDHAM ON THE CREEK | Dallas | 00815000140010000 | 151 | $15,600,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-37 | Pecos HFC | ADIRA APARTMENTS | Dallas | 00000750862900000 | 164 | $14,500,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-38 | Pecos HFC | TIDES ON MCCALLUM NORTH | Dallas | 008199002212A0100 | 68 | $7,685,200 | N | — | 2027-01-01 |
| TX-43-3479 | Pecos HFC | THE ABIGAIL | Desoto | 200547500A0020000 | 198 | $38,000,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-39 | Pecos HFC | VISTA RIDGE ORIGINALLY RIDGLEA HILLS | Duncanville | 22059500010010000 | 158 | $14,500,000 | N | — | 2027-01-01 |
| TX-37-1415 | Pecos HFC | REPUBLIC WEST APARTMENTS | Garland | 26178370010010000 | 410 | $50,090,050 | N | — | 2027-01-01 |
| TX-37-1438 | Pecos HFC | THE HUXLEY | Garland | 26578520010010000 | 236 | $30,000,000 | N | — | 2027-01-01 |
| TX-37-4261 | Pecos HFC | BARRETT APARTMENT HOMES | Garland | 26381700010010000 | 200 | $28,500,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-40 | Pecos HFC | THE ABRAM | Garland | 26511800010010000 | 144 | $25,500,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-41 | Pecos HFC | REPUBLIC WEST APARTMENTS (114 UNITS) | Garland | 26178420010010300 | 114 | $14,160,290 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-42 | Pecos HFC | LAKEWAY PLACE | Garland | 26178410010010000 | 148 | $13,565,710 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-43 | Pecos HFC | REPUBLIC WEST APARTMENTS (32 UNITS) | Garland | 26178370010010800 | 32 | $3,976,950 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-44 | Pecos HFC | REPUBLIC WEST APARTMENTS (30 UNITS) | Garland | 26178420010011400 | 30 | $3,818,300 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-45 | Pecos HFC | REPUBLIC WEST APARTMENTS (30 UNITS) | Garland | 26178420010010600 | 30 | $3,765,030 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-46 | Pecos HFC | REPUBLIC WEST APARTMENTS (30 UNITS) | Garland | 26178420010010500 | 31 | $3,729,500 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-47 | Pecos HFC | REPUBLIC WEST APARTMENTS (18 UNITS) | Garland | 26178370010011100 | 18 | $2,300,900 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-48 | Pecos HFC | LANDMARK AT LAKE VILLAGE NORTH (24 UNITS) | Garland | 26178380010010200 | 24 | $2,156,220 | N | — | 2027-01-01 |
| TX-43-1153801 | Pecos HFC | JEFFERSON VINE | Grand Prairie | 28103730010020000 | 380 | $76,000,000 | N | — | 2027-01-01 |
| TX-43-1479 | Pecos HFC | JEFFERSON PROMENADE II | Irving | 322422200A0020000 | 433 | $101,520,700 | N | — | 2027-01-01 |
| TX-43-1495 | Pecos HFC | RANCHO MIRAGE | Irving | 32023410000020000 | 310 | $65,086,730 | N | — | 2027-01-01 |
| TX-43-1523 | Pecos HFC | AVALON 8801 | Irving | 325597700A0010000 | 212 | $47,000,000 | N | — | 2027-01-01 |
| TX-43-1614 | Pecos HFC | CASA VALLEY APTS | Irving | 320558000A0010000 | 151 | $30,652,500 | N | — | 2027-01-01 |
| TX-43-1625 | Pecos HFC | WYTHE APTS (2018 RENO) | Irving | 325355400A0010000 | 248 | $29,850,000 | N | — | 2027-01-01 |
| TX-37-1473208 | Pecos HFC | Knowlton Apartment Homes | Mesquite | 382165600001D0000 | 412 | $46,500,000 | N | — | 2026-06-03 |
| TX-43-1702 | Pecos HFC | THE RALEIGH | Mesquite | 382160000A03A0000 | 264 | $40,680,000 | N | — | 2027-01-01 |
| TX-37-1153309 | Pecos HFC | *(unresolved)* | Rowlett | — | — | — | ? | — | 2027-01-01 |
| TX-37-1104 | Pleasanton HFC | MARQUIS AT PARK CENTRAL | Dallas | 007731000A0020000 | 308 | $76,010,140 | N | — | 2027-01-01 |
| TX-37-1153 | Pleasanton HFC | WINDHDAM CREST | Dallas | 008097000A01B0000 | 196 | $25,082,420 | N | — | 2027-01-01 |
| TX-43-3712 | Pleasanton HFC | FOREST HILLS APTS | Dallas | 008421000702A0000 | 216 | $21,500,000 | N | — | 2027-01-01 |
| TX-37-750 | Pleasanton HFC | RIVIERIA | Dallas | 00000787230000000 | 247 | $20,750,000 | N | — | 2027-01-01 |
| TX-37-881 | Pleasanton HFC | *(unresolved)* | Dallas | — | — | — | ? | — | 2027-01-01 |
| TX-37-1358481 | Pleasanton HFC | PRESIDIUM VALLEY VIEW | Farmers Branch | 241475800A0010000 | 338 | $43,500,000 | N | — | 2027-01-01 |
| TX-37-1385 | Pleasanton HFC | EQUINOX ON THE PARK | Garland | 26174700010010000 | 338 | $64,000,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-49 | Pleasanton HFC | FIREWHEEL TOWN VILLAGE SENIOR LIVING | Garland | 261792400101R0000 | 154 | $26,200,000 | N | — | 2027-01-01 |
| TX-43-1225449 | Pleasanton HFC | SPRINGS AT GRAND PRAIRIE | Grand Prairie | 220334900A0010000 | 276 | $54,898,400 | N | — | 2027-01-01 |
| TX-43-1468 | Pleasanton HFC | BELMONT | Grand Prairie | 282175200A0010000 | 260 | $44,720,000 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-50 | Pleasanton HFC | ANTHEM | Mesquite | 38003430010020000 | 241 | $35,358,560 | N | — | 2027-01-01 |
| TX-NEW-DALLAS-51 | Pleasanton HFC | ROWLETT STATION APTS BLDG 1 & 2 | Rowlett | 446820000201R0000 | 224 | $45,615,890 | N | — | 2027-01-01 |
| TX-43-1018 | Texas Essential Housing PFC | THE MUSE | Dallas | 00000513763000000 | 804 | $78,801,260 | Y | — | — |
| TX-43-518 | Texas Essential Housing PFC | BELLA VIDA | Dallas | 00000557891000000 | 256 | $26,400,000 | Y | — | — |
| TX-43-554 | Texas Essential Housing PFC | HIGHLAND ROAD VILLAGE | Dallas | 00000660886500000 | 172 | $21,451,950 | Y | — | — |
| TX-43-616 | Texas Essential Housing PFC | WESTERN PARK | Dallas | 00000660886000000 | 160 | $19,121,620 | Y | — | — |
| TX-NEW-DALLAS-52 | Texas Essential Housing PFC | THE INTERLACE APTS (ECU) | Dallas | 00693200080040000 | 204 | $18,128,690 | Y | — | — |
| TX-NEW-DALLAS-53 | Texas Essential Housing PFC | TRADEWIND APTS PH 1 | Mesquite | 38208500090010000 | 200 | $22,377,850 | Y | — | — |
| TX-NEW-DALLAS-54 | Texas Essential Housing PFC | TRADEWINDS APTS PH II | Mesquite | 65146263510330100 | 107 | $11,972,150 | Y | — | — |

*TY26 exempt column: Y = DCAD TOTAL_EXEMPTION in effect for tax year 2026; N = fully taxable on the 2026 roll despite sponsor ownership; ? = ownership/exemption status not resolved to a specific parcel.*

## By sponsor

| Sponsor | Records (seed+new) | Appraised value | Currently exempt (TY26) |
|---|---|---|---|
| Pecos HFC | 56 | $1,966,453,170 | 0 |
| La Villa HFC | 19 | $478,842,160 | 0 |
| Pleasanton HFC | 12 | $457,635,410 | 0 |
| Cameron County HFC | 16 | $308,986,170 | 4 |
| Edcouch HFC | 16 | $231,604,740 | 0 |
| Texas Essential Housing PFC | 7 | $198,253,520 | 7 |
| Garland HFC | 3 | $126,544,080 | 0 |
| Maverick County HFC | 3 | $117,402,430 | 0 |

## Excluded (non-traveling, out of scope)

11 Garland HFC-owned multifamily parcels located within the City of Garland itself were found in the same DCAD sweep and excluded from this census -- Garland is Garland HFC's home jurisdiction, so under HB 21's city-boundary test these are not "traveling" and fall outside HB21 §13(i)'s reach (same treatment Phase 1 gave Houston HA's ~15 Harris-County home-turf properties). Aggregate appraised value of the excluded set: $409,064,990 (from the raw DCAD sweep), not included in the totals above.

## Top gaps / blockers

1. **Exemption status is largely negative on the current roll.** 119 of 132 records show NO ad valorem exemption in effect for TY2026 despite sponsor-of-record ownership -- the cause (pending application, non-filing of the §394.9027 TDHCA audit, denial, or active litigation) cannot be determined from the appraisal roll alone; TDHCA's compliance-monitoring page (Method 1) and/or a TPIA request are the next step.
2. **Seed-row-to-parcel identity for 64 of 78 seed rows rests on a sponsor+city bucket pairing, not an independent match.** Where a city held more seed rows than one obvious distinguishing clue (most Pecos "Additional owner" rows in the City of Dallas), the specific building assigned to a given census_id is a best-effort, disclosed assumption -- Method 3 (Dallas County Clerk grantor/grantee index) would be needed to pin these down to individual deeds.
3. **`first_exempt_tax_year` and `annual_exemption_value_est` are null on every record.** A single current-year roll snapshot cannot date when an exemption began; DCAD publishes prior-year rolls back to 2021 (free) that would let a future pass bracket the first exempt year, and DCAD's TaxRates.aspx has the per-jurisdiction rates needed to convert appraised value into an annual foregone-tax estimate.
4. Two seed rows (`TX-37-1153309`, Pecos/Rowlett; `TX-37-881`, Pleasanton/Dallas) have no remaining DCAD candidate in their sponsor+city bucket and carry no property match at all.
5. Loan/servicer/securitization data (schema's `loan.*` block) was not researched -- out of reach of free CAD/court sources; the Oconee/BX5 and Stonelex/Blackstone Mortgage Trust namings are suggestive of distressed CRE-CLO workouts but unconfirmed.
