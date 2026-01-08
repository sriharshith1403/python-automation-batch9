import pytest
from app.validator import validate_response
from app.file_handler import save_to_json, save_to_csv

class FakeResponse:
    def __init__(self, status, data, content_type="application/json"):
        self.status_code = status
        self._data = data
        self.headers = {"Content-Type": content_type}

    def json(self):
        return self._data

# ---------- Parameterized Tests ----------
@pytest.mark.parametrize("status,data,expected", [
    (200, [{"id":1,"name":"A","email":"a@test.com"}], 1),
    (200, [{"id":1,"name":"","email":"a@test.com"}], 0),
])
def test_api_success(status, data, expected):
    response = FakeResponse(status, data)
    result = validate_response(response)
    assert len(result) == expected

# ---------- Invalid API Response ----------
def test_api_invalid_response():
    response = FakeResponse(404, [])
    with pytest.raises(ValueError):
        validate_response(response)

# ---------- File Write Test ----------
def test_file_write(valid_api_data, tmp_path):
    file_json = tmp_path / "test.json"
    file_csv = tmp_path / "test.csv"

    save_to_json(file_json, valid_api_data)
    save_to_csv(file_csv, valid_api_data)

    assert file_json.exists()
    assert file_csv.exists()

# ---------- Exception Handling ----------
def test_invalid_content_type():
    response = FakeResponse(200, [], "text/html")
    with pytest.raises(ValueError):
        validate_response(response)

# ---------- Marker Example ----------
@pytest.mark.xfail(reason="Future enhancement")
def test_future_feature():
    assert False
