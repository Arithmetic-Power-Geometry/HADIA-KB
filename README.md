# 🌾 HADIA
## The Digital Knowledge Home of Jharkhand's Handia

**HADIA-KB v1.0.0 · Public Evidence Release**  
**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

HADIA is an open research infrastructure that turns scattered public documentation about **Handia / Hadia / Hadiya / Handiya / Haria** into a source-linked dataset, searchable Streamlit portal, machine-readable knowledge graph and reproducible API. Jharkhand is the primary focus; comparative evidence from other regions remains explicitly labelled by geography.

> **Research boundary:** HADIA-KB maps publicly documented and retrievable evidence. It does not claim that all oral, community-held or unpublished knowledge exists on the internet, and it never treats an unstudied place as a place without knowledge.

## 🚀 Run immediately on Streamlit

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

For Streamlit Community Cloud, upload this repository to GitHub, choose `streamlit_app.py` as the entrypoint, and deploy. No secrets or database credentials are required.

## What the portal contains

- Home research dashboard
- Evidence Explorer with filtered CSV/JSON export
- Jharkhand evidence atlas
- Ranu & plant atlas
- Microbial and quantitative-science explorer
- Culture, policy and legal evidence
- Claim-level **Handia Evidence Passport**
- Interactive evidence knowledge graph
- Documented research-gap dashboard
- Searchable source library
- Complete/individual research downloads

## Frozen release

Current packaged counts: **29 sources · 34 claims · 16 plant/lichen records · 12 microorganism records · 18 measurements · 192 graph relations**.

Researchers can download CSV tables directly from the app. The repository also contains JSON-ready APIs, a PostgreSQL schema, an Excel research workbook, and an all-table ZIP release.

## API

```bash
pip install -r requirements.txt -r requirements-api.txt
uvicorn backend.main:app --reload
```

Examples:

- `GET /api/v1/claims`
- `GET /api/v1/plants`
- `GET /api/v1/microorganisms`
- `GET /api/v1/measurements`
- `GET /api/v1/sources.csv?q=Ranu`

## Licensing

- **Software:** Apache License 2.0
- **Original HADIA-KB compilation, annotations, schema and documentation:** CC BY 4.0
- **Third-party articles, source text and other linked materials:** retain their own rights/licenses

See `LICENSE`, `LICENSE-DATA.md`, and `NOTICE`.

## Citation

> Akhtar, M. A. K. (2026). *HADIA-KB: Evidence-Linked Knowledge Base of Handia/Hadia/Haria* (Version 1.0.0) [Data set].

Add the permanent DOI to `CITATION.cff` after archiving the GitHub release in a DOI-issuing repository.

## Reproducibility

Every push is checked by GitHub Actions for Python compilation, relational integrity, orphan citations, malformed source URLs, automated tests and a live Streamlit health check.
