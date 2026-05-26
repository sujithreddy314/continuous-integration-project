import random
import time
import pytest

from fastapi.testclient import TestClient

from services.user_service.main import app

client = TestClient(app)

@pytest.mark.flaky(reruns=2)
def test_random_flaky_failure():
    result = random.choice([True, False])
    assert result


def test_random_delay():
    delay = random.uniform(0.1, 2.5)
    time.sleep(delay)

    response = client.get("/health")
    assert response.status_code == 200 what do i need to remove