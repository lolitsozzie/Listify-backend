import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    client.default_format = 'json'
    return client


@pytest.fixture(autouse=True)
def disable_network_access(monkeypatch):
    """Prevent any un-mocked network requests from executing in tests"""

    def fail(*args, **kwargs):
        pytest.fail('Called network method in test')

    monkeypatch.setattr('socket.socket', fail)
