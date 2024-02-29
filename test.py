from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest 
from main import app  # Импортируем ваше приложение из файла app.py

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "FastApi service started!"

def test_get_params(client):
    response = client.get("/привет я голый")
    assert response.status_code == 200
    assert 'label' in response.json()[0]
    assert 'score' in response.json()[0]



