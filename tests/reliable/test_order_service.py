import uuid

from fastapi.testclient import TestClient

from services.order_service.main import app

client = TestClient(app)


def test_order_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_order():
    item_name = f"Laptop-{uuid.uuid4()}"

    response = client.post(
        f"/orders?user_id=1&item_name={item_name}&quantity=1&total_price=999.99"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["user_id"] == 1
    assert data["item_name"] == item_name
    assert data["quantity"] == 1
    assert data["total_price"] == 999.99
    assert data["status"] == "CREATED"


def test_get_orders():
    response = client.get("/orders")

    assert response.status_code == 200
    assert isinstance(response.json(), list)