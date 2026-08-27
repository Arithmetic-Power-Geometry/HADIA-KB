from fastapi.testclient import TestClient
from backend.main import app
client=TestClient(app)
def test_root(): assert client.get('/api/v1').status_code==200
def test_claims():
    r=client.get('/api/v1/claims?limit=3'); assert r.status_code==200; assert len(r.json()['records'])<=3
