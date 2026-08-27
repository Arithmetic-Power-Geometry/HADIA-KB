from hadia.data import load_all, metadata
from hadia.validate import validate_all

def test_metadata_version(): assert metadata()["version"] == "1.0.0"
def test_integrity(): assert validate_all(load_all()) == []
def test_minimum_corpus():
    t=load_all(); assert len(t["sources"]) >= 25; assert len(t["claims"]) >= 30
def test_every_claim_has_source():
    t=load_all(); assert set(t["claims"].source_id).issubset(set(t["sources"].source_id))
def test_geography_present(): assert (load_all()["claims"].geographic_scope.str.len()>0).all()
