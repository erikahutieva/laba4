import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user(test_user):
    response = client.post("/auth/register/", json=test_user)
    assert response.status_code == 200
    assert response.json()["msg"] == "User registered successfully"

def test_login_user(test_user):
    response = client.post("/auth/login/", data={"username": test_user["username"], "password": test_user["password"]})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_user_invalid_credentials():
    response = client.post("/auth/login/", data={"username": "testuser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"



def test_get_exchange_rate_invalid_amount():
    response = client.get("/currency/exchange/?amount=-100&from_currency=USD&to_currency=EUR")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_exchange_rate_missing_parameters():
    response = client.get("/currency/exchange/?amount=100&from_currency=USD")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_exchange_rate_zero_amount():
    response = client.get("/currency/exchange/?amount=0&from_currency=USD&to_currency=EUR")
    assert response.status_code == 422
    assert "detail" in response.json()

