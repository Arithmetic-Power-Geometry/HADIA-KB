# HADIA-KB Data Dictionary

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Core tables

- `sources.csv`: one row per indexed source.
- `claims.csv`: one row per source-linked, paraphrased evidence claim.
- `plants.csv`: plant/lichen records explicitly reported in starter-culture literature.
- `microorganisms.csv`: microbial findings with identification method and source.
- `measurements.csv`: quantitative findings with units, sample context, geography and source.
- `names.csv`: canonical entities and source-reported terminology.
- `locations.csv`: display geography; coordinates are approximate visualization points, not research geocodes.
- `relations.csv`: machine-readable graph edges carrying a source identifier.
- `contradictions.csv`: disagreements or apparent conflicts preserved with contextual adjudication.
- `gaps.csv`: gaps in the **current documented corpus**, never assertions that real-world knowledge is absent.

## Missing-data policy
Use `NR` for not reported, `NA` for not applicable, and `ND` for not detected. Empty strings in legacy seed records should be interpreted as unavailable rather than as zero.
