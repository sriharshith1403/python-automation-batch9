import pytest

@pytest.fixture

def valid_api_data():
    return[
        {"id": 1 , "name":"Arun", "email":"a@test.com"},
        {"id": 2 , "name":"Babu", "email":"b@test.com"},
        {"id": 3 , "name":"", "email":"c@test.com"},
    ]
