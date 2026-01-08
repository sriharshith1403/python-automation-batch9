import pytest

@pytest.fixture
def valid_api_data():
    return [
        {"id": 1, "name": "Alice", "email": "a@test.com"},
        {"id": 2, "name": "Bob", "email": "b@test.com"},
        {"id": 3, "name": "", "email": "c@test.com"},  # invalid
    ]
