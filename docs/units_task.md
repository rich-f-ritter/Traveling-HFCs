# Unit-count backfill task (Travis / Tarrant)

You are one of several agents backfilling **unit counts** for traveling-HFC apartment
properties in Travis (Austin) and Tarrant (Fort Worth / Arlington) counties, whose CADs
didn't publish a unit count. Working dir: /home/user/Traveling-HFCs.

**Your batch:** `data/unit_batches/ub_<NN>.json` — ~12 properties, each with `census_id`,
`name` (may be null for Travis rows), `address`, `city`, `county`, `owner_group` (the
private operator/owner), `year_built`, `sponsor`.

For **EACH** property, find the **total number of apartment units** (the whole community's
unit count) from **FREE public sources only**:
- apartments.com, apartmenthomeliving.com, rentcafe, apartmentfinder, zillow/trulia listing
  pages (unit count is usually stated, e.g. "354 units").
- The operator's / developer's own site or press release (e.g. "acquired the 330-unit …").
- CAD improvement detail: Tarrant `tad.org/property?account=…` (try the r.jina.ai reader
  proxy or curl with a browser user-agent) sometimes lists "Living Units"; Travis TCAD is
  gated — use listings instead.
- Litigation / CMBS / TDHCA filings that state a unit count.

For rows with a null `name`, first identify the property by its **address + owner** (search
"<address> apartments" or "<owner> <city> apartments"), then get its unit count.

**RULES:** free sources only; cite a source URL for each unit count. If you genuinely can't
find it, set `units: null` and explain in `notes` — do NOT guess. Watch for multi-building
communities where the address is one of several parcels — report the **whole-community** unit
count and note it. Distinguish current-vacancy counts (e.g. "24 available") from total units.

**OUTPUT:** write `census/enrich/units_batch_<NN>.json` — a JSON array, one object per property:
```json
{ "census_id", "resolved_name", "units", "units_source", "notes" }
```

**RETURN** (final message, tight): # properties done; # units found vs gap; any property you
couldn't identify at all; top blockers.
