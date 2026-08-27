# 🌾 HADIA
## The Digital Knowledge Home of Jharkhand's Handia

**HADIA-KB v1.0.0 · Public Evidence Release**  
**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

HADIA is an open research infrastructure that transforms scattered public documentation about **Handia / Hadia / Hadiya / Handiya / Haria**—traditional rice-based fermented beverages often described as rice beer—into a source-linked dataset, searchable research portal, machine-readable knowledge graph, and reproducible API.

**Jharkhand, India, is the primary geographic focus.** Comparative evidence from other regions is retained with its original geographic context rather than being automatically generalized to Jharkhand.

> **Research boundary:** HADIA-KB maps publicly documented and retrievable evidence. It does not claim that all oral, community-held, unpublished, or undocumented knowledge exists on the internet, and it never treats an unstudied place as a place without knowledge.

---

## 🌐 Explore HADIA

**Interactive Research Portal**  
https://hadia-kb.streamlit.app/

**Permanent Zenodo Archive**  
https://doi.org/10.5281/zenodo.22132285

**GitHub Repository**  
https://github.com/Arithmetic-Power-Geometry/HADIA-KB

---

## 🔬 What is HADIA-KB?

Knowledge concerning Handia/Hadia/Haria is distributed across ethnobotanical studies, fermentation research, microbiology, food chemistry, nutrition, cultural studies, government documents, legal materials, policy records, and regional accounts.

HADIA-KB provides a structured framework for bringing this documented evidence together while preserving its provenance.

The knowledge base covers:

- Handia/Hadia/Haria terminology and reported names
- Traditional starter cultures such as **Ranu**
- Plants and plant parts reported in starter preparation
- Preparation and fermentation evidence
- Microorganisms reported in scientific studies
- Chemical and nutritional measurements
- Geographic context
- Communities as reported by sources
- Cultural practices
- Government and policy evidence
- Legal and regulatory material
- Source-linked scientific claims
- Evidence relationships
- Documented differences and uncertainties
- Research gaps in the currently documented corpus

---

## 🧭 Evidence with Provenance

HADIA-KB follows a simple principle:

> **A research record should remain connected to where it came from.**

Records therefore preserve, wherever available:

- source identifier
- source title
- authors or institutional owner
- publication year
- source URL or persistent identifier
- terminology used by the source
- geographic scope
- community context
- evidence category
- quantitative units and sample context
- methodological information
- cautions and interpretation boundaries

Evidence from Jharkhand, West Bengal, Odisha, or other regions is not silently merged into a single universal preparation.

Traditional knowledge claims, laboratory observations, chemical measurements, cultural documentation, and policy evidence are also kept conceptually distinguishable.

---

## 📊 HADIA-KB v1.0.0

The frozen public evidence release currently contains:

| Evidence component | Records |
|---|---:|
| Sources | **29** |
| Claim-level evidence records | **34** |
| Plant/lichen records | **16** |
| Microorganism records | **12** |
| Quantitative measurements | **18** |
| Evidence-linked graph relations | **192** |

Additional structured tables cover terminology, locations, communities, policy/legal evidence, documented differences, and research gaps.

These counts describe **version 1.0.0** and should not be interpreted as the total amount of knowledge that exists about Handia/Hadia/Haria.

---

## 🖥️ Interactive Research Portal

The HADIA portal provides:

- Research dashboard
- Evidence Explorer
- Filtered evidence search
- Jharkhand evidence atlas
- Ranu and plant explorer
- Microorganism explorer
- Quantitative science explorer
- Culture, policy, and legal evidence
- Claim-level **Handia Evidence Passport**
- Interactive evidence knowledge graph
- Research-gap dashboard
- Searchable source library
- Research data downloads
- Filtered CSV and JSON exports

Explore the live platform:

**https://hadia-kb.streamlit.app/**

---

## 📥 Research Data

Researchers can access individual machine-readable tables directly from the repository and through the interactive portal.

The release provides or supports:

- CSV
- XLSX
- JSON
- JSON-LD
- GraphML
- RDF/Turtle
- PostgreSQL-compatible schema
- API-based access

CSV files remain visible individually so researchers can inspect, download, analyze, and reproduce results without requiring the web interface.

The Excel workbook provides a convenient multi-table version of the research dataset.

---

## 🪪 Handia Evidence Passport

Claim-level records are designed to function as evidence passports.

An evidence passport can connect a reported finding with information such as:

- claim identifier
- evidence category
- reported finding
- geographic context
- terminology as reported
- source
- evidence quality
- related entities
- interpretation caution

This allows users to move from a statement displayed in the portal back to its documented evidence context.

---

## 🕸️ Knowledge Graph

HADIA-KB represents relationships among evidence entities including:

**sources → claims → locations → communities → plants → starter cultures → microorganisms → measurements → cultural evidence → policy/legal evidence**

The graph is intended to support both human exploration and computational research.

---

## 🚀 Run HADIA Locally

Install the Streamlit dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run streamlit_app.py
```

No database credentials or external secrets are required for the standard public-data Streamlit deployment.

---

## ☁️ Streamlit Community Cloud

For deployment through Streamlit Community Cloud:

1. Fork or upload this repository to GitHub.
2. Select the repository in Streamlit Community Cloud.
3. Select the `main` branch.
4. Set the main file path to:

```text
streamlit_app.py
```

5. Deploy.

The official public instance is available at:

**https://hadia-kb.streamlit.app/**

---

## 🔌 API

Install API dependencies:

```bash
pip install -r requirements.txt -r requirements-api.txt
```

Run the API:

```bash
uvicorn backend.main:app --reload
```

Example endpoints include:

```text
GET /api/v1/claims
GET /api/v1/plants
GET /api/v1/microorganisms
GET /api/v1/measurements
GET /api/v1/sources.csv?q=Ranu
```

The API is intended to support computational reuse and integration with external research workflows.

---

## ♻️ Reproducibility

The repository includes automated validation intended to detect problems such as:

- duplicate primary identifiers
- orphan source references
- relational-integrity failures
- malformed source URLs
- Python compilation errors
- automated test failures
- Streamlit startup failures

Versioned releases are frozen so that analyses performed using an earlier release can remain reproducible even as HADIA-KB continues to grow.

---

## 🏷️ Versioning

HADIA-KB follows versioned public releases.

The current release is:

**HADIA-KB v1.0.0**

Future evidence additions, corrections, and structural improvements should appear in subsequent versions rather than silently changing the archived v1.0.0 research record.

---

## 📦 Permanent Archive and DOI

HADIA-KB v1.0.0 is archived through Zenodo.

**DOI:**  
https://doi.org/10.5281/zenodo.22132285

**Zenodo record:**  
https://zenodo.org/records/22132285

The DOI provides a persistent identifier for citation and long-term scholarly reference to this release.

---

## 📖 Citation

If you use **HADIA-KB, the HADIA software, its evidence structure, dataset, or research portal** in research, please cite:

> **Akhtar, M. A. K. (2026). _HADIA-KB: An Evidence-Linked Knowledge Base and Interactive Research Platform for Handia/Hadia/Haria_ (Version 1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.22132285**

Machine-readable citation metadata are provided in:

```text
CITATION.cff
```

---

## ⚖️ Licensing

HADIA uses a dual-licensing structure appropriate to its software and research-data components.

### Software

**Apache License 2.0**

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

### Original HADIA-KB data compilation

The original HADIA-KB compilation, annotations, structured research data, schema, and associated documentation are made available under **Creative Commons Attribution 4.0 International (CC BY 4.0)** where indicated.

### Third-party material

Third-party publications, articles, source text, linked resources, traditional/community knowledge, and externally produced materials remain subject to their respective copyrights, licenses, and other applicable rights.

HADIA-KB provides source metadata and appropriately structured or paraphrased evidence; inclusion of a citation or link does not transfer ownership of the underlying third-party work.

See:

```text
LICENSE
LICENSE-DATA.md
NOTICE
```

---

## 🤝 Contributing

HADIA-KB welcomes contributions that expand, verify, or correct documented knowledge about Handia/Hadia/Haria.

All new factual information should be supported by verifiable evidence. Contributions should provide, where applicable:

- a reliable source or persistent identifier such as a DOI
- exact geographic context
- terminology used in the original source
- concise description of the supported evidence
- relevant methodological or interpretation information

Corrections to existing records are equally welcome when supported by appropriate evidence.

Please do not submit copyrighted full-text publications. Provide bibliographic information, persistent identifiers, source links, and appropriately paraphrased evidence instead.

Contributions should be reviewed for source quality, accuracy, provenance, geographic context, duplication, and consistency before incorporation into a versioned HADIA-KB release.

Previously archived releases remain unchanged to preserve reproducibility.

> **Every record should be traceable, verifiable, and reusable.**

---

## 🌱 Research Scope and Future Growth

HADIA-KB is designed to grow.

Future releases may incorporate additional documented evidence from:

- scientific publications
- theses and dissertations
- government archives
- biodiversity documentation
- food and fermentation research
- ethnobotanical literature
- cultural and anthropological studies
- legal and regulatory sources
- responsibly documented community knowledge
- newly published analytical studies

Absence of evidence in the database must not be interpreted as evidence of absence in a community or geographic region.

---

## 🌾 HADIA

**The Digital Knowledge Home of Jharkhand's Handia**

From Jharkhand's living tradition to an evidence-linked knowledge resource for the world.

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

