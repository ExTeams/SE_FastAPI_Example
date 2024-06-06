from fastapi.testclient import TestClient
from main import app  # replace with the actual module name


client = TestClient(app)

def test_root():
    _response = client.get("/")
    print(_response)
    assert _response.status_code == 200
    assert _response.text == '"FastApi service started!"'

def test_favicon():
    _response = client.get("/favicon.ico")
    assert _response.status_code == 200
    assert _response.headers["Content-Disposition"] == "attachment; filename=favicon.ico"

def test_predict_positive():
    _response = client.post("/predict/", json={"text": "This is a positive review!"})
    assert _response.status_code == 200
    assert _response.json()[0]["label"] == "POSITIVE"

def test_predict_negative():
    _response = client.post("/predict/", json={"text": "This is a negative review!"})
    assert _response.status_code == 200
    assert _response.json()[0]["label"] == "NEGATIVE"

def test_predict_invalid_input():
    _response = client.post("/predict/", json={"abc": "This is a positive review!"})
    assert _response.status_code == 422

def test_batch_predict():
    _response = client.post("/batch_predict/", json={"items": ["This is a positive review!", "This is a negative review"]})
    assert _response.status_code == 200
    assert len(_response.json()) == 2
    assert _response.json()[0][0]["label"] == "POSITIVE"
    assert _response.json()[1][0]["label"] == "NEGATIVE"

def test_batch_predict_invalid_input():
    response = client.post("/batch_predict/", json={"abc": ["This is a positive review!", "This is a negative review"]})
    assert response.status_code == 422
