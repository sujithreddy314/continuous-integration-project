import uuid
from fastapi.testclient import TestClient

from services.user_service.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


import uuid

def test_create_user():
    unique_email = f"ashok_test_{uuid.uuid4()}@gmail.com"

    response = client.post(
        f"/users?name=ashok_test&email={unique_email}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "ashok_test"
    assert data["email"] == unique_email


def test_get_users():
    response = client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)