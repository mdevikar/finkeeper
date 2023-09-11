import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/api/v1/users/register")
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"
    