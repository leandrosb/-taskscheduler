import pytest
from taskscheduler import create_app


@pytest.fixture
def client():
    app = create_app()
    return app


def test_healthz(client):
    response = client.get("/healthz")
    if response.status_code != 200:
        raise AssertionError
