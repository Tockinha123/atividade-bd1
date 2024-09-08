import pytest
from fastapi.testclient import TestClient

from user_registry.app import app


@pytest.fixture
def client():
    return TestClient(app)
