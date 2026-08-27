-- HADIA-KB v1.0 PostgreSQL schema
-- Copyright (C) 2026 Mohammad Amir Khusru Akhtar
CREATE TABLE IF NOT EXISTS sources (
  source_id TEXT PRIMARY KEY, authors_or_owner TEXT, title TEXT NOT NULL, year INTEGER,
  venue TEXT, source_type TEXT, geographic_scope TEXT, name_as_reported TEXT,
  source_url TEXT NOT NULL, source_quality TEXT, doi TEXT, access_class TEXT, notes TEXT,
  dataset_version TEXT NOT NULL, record_status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS claims (
  claim_id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(source_id),
  claim_category TEXT NOT NULL, claim_text TEXT NOT NULL, geographic_scope TEXT NOT NULL,
  community_as_reported TEXT, name_as_reported TEXT, evidence_directness TEXT,
  verification_status TEXT, source_quality TEXT, caution TEXT, dataset_version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS measurements (
  measurement_id TEXT PRIMARY KEY, analyte TEXT NOT NULL, value TEXT, unit TEXT,
  sample_context TEXT, fermentation_stage TEXT, geographic_scope TEXT,
  source_id TEXT NOT NULL REFERENCES sources(source_id), source_title TEXT, source_year TEXT,
  source_url TEXT, dataset_version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS relations (
  relation_id TEXT PRIMARY KEY, subject_id TEXT NOT NULL, predicate TEXT NOT NULL,
  object_id TEXT NOT NULL, source_id TEXT REFERENCES sources(source_id),
  evidence_status TEXT, dataset_version TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_claims_category ON claims(claim_category);
CREATE INDEX IF NOT EXISTS idx_claims_scope ON claims(geographic_scope);
CREATE INDEX IF NOT EXISTS idx_claims_source ON claims(source_id);
CREATE INDEX IF NOT EXISTS idx_rel_subject ON relations(subject_id);
CREATE INDEX IF NOT EXISTS idx_rel_object ON relations(object_id);
