import pytest
from taskscheduler import create_app


@pytest.fixture
def client():
    app = create_app()
    return app


def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
