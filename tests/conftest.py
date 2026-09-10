import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore in-memory activities state so tests don't leak into each other."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
