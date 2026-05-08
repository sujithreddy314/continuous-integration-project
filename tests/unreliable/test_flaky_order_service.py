import random
import time
import pytest

from fastapi.testclient import TestClient

from services.order_service.main import app

client = TestClient(app)


@pytest.mark.flaky(reruns=2)
def test_flaky_order_creation():
    should_fail = random.choice([True, False])

    if should_fail:
        pytest.fail("Simulated flaky order service failure")

    response = client.post(
        "/orders?user_id=1&item_name=Mouse&quantity=1&total_price=25.50"
    )

    assert response.status_code == 200


def test_random_order_delay():
    delay = random.uniform(0.1, 3.0)
    time.sleep(delay)

    response = client.get("/health")
    assert response.status_code == 200