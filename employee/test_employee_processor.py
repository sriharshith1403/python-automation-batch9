import pytest
import csv
from employee_processor import (
    is_valid_employee,
    read_and_validate_csv,
    calculate_statistics
)

@pytest.fixture
def sample_csv(tmp_path):
    file_path = tmp_path / "employees.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["EmployeeID", "Name", "Department", "Salary"])
        writer.writerow([101, "Alice", "IT", 60000])
        writer.writerow([102, "Bob", "HR", 55000])
        writer.writerow([103, "Charlie", "Finance", 0])   # invalid
        writer.writerow([104, "", "Marketing", 50000])   # invalid
    return file_path

@pytest.mark.parametrize(
    "record, expected",
    [
        ({"EmployeeID": "1", "Name": "A", "Department": "IT", "Salary": "5000"}, True),
        ({"EmployeeID": "-1", "Name": "A", "Department": "IT", "Salary": "5000"}, False),
        ({"EmployeeID": "1", "Name": "", "Department": "IT", "Salary": "5000"}, False),
        ({"EmployeeID": "1", "Name": "A", "Department": "", "Salary": "5000"}, False),
    ],
)
def test_is_valid_employee(record, expected):
    assert is_valid_employee(record) == expected

def test_valid_records_filtered(sample_csv):
    valid_employees = read_and_validate_csv(sample_csv)
    assert len(valid_employees) == 2

def test_average_salary(sample_csv):
    employees = read_and_validate_csv(sample_csv)
    total, average = calculate_statistics(employees)
    assert total == 2
    assert average == (60000 + 55000) // 2

@pytest.mark.xfail(reason="Future validation rules not implemented")
def test_future_validation():
    assert False
