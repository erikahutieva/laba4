import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_user():
    return {"username": "testuser", "password": "testpass"}
