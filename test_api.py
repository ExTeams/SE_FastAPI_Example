from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_translate_endpoint():
    response = client.post("/predict/", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert response.json() == [{'label': 'POSITIVE', 'score': 0.9997164607048035}]
