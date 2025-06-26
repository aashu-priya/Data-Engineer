# tests/test_api.py

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_sample_data():
    response = client.get("/data/sample?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5
