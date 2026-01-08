import csv
import json

def is_valid_employee(record):
    try:
        emp_id = int(record["EmployeeID"])
        salary = int(record["Salary"])
        name = record["Name"].strip()
        department = record["Department"].strip()

        if emp_id <= 0 or salary <= 0:
            return False
        if not name or not department:
            return False
        return True
    except (ValueError, KeyError):
        return False

def read_and_validate_csv(file_path):
    valid_employees = []
    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if is_valid_employee(row):
                    valid_employees.append({
                        "EmployeeID": int(row["EmployeeID"]),
                        "Name": row["Name"],
                        "Department": row["Department"],
                        "Salary": int(row["Salary"])
                    })
    except FileNotFoundError:
        print("CSV file not found")
    return valid_employees

def write_to_json(data, output_file):
    try:
        with open(output_file, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)
    except IOError:
        print("Error writing JSON file")

def calculate_statistics(employees):
    total = len(employees)
    if total == 0:
        return 0, 0
    avg_salary = sum(emp["Salary"] for emp in employees) // total
    return total, avg_salary

def process_employee_data(input_csv, output_json):
    valid_employees = read_and_validate_csv(input_csv)
    write_to_json(valid_employees, output_json)
    total, average = calculate_statistics(valid_employees)

    print(f"Valid employees processed: {total}")
    print(f"Average salary: {average}")
    print(f"Output written to {output_json}")

if __name__ == "__main__":
    process_employee_data("employee_data.csv", "valid_employees.json")
