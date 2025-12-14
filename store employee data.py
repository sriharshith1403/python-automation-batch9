# Dictionary to store employee data
employee = {}

# Input employee details
name = input("Enter Employee Name: ")
base_salary = float(input("Enter Base Salary: "))
bonus = float(input("Enter Bonus: "))

# Calculate final salary
final_salary = base_salary + bonus

# Store data in dictionary
employee[name] = {
    "Base Salary": base_salary,
    "Bonus": bonus,
    "Final Salary": final_salary
}

# Print salary slip
print("\n----- Salary Slip -----")
print("Employee Name:", name)
print("Base Salary: ₹", employee[name]["Base Salary"])
print("Bonus: ₹", employee[name]["Bonus"])
print("Final Salary: ₹", employee[name]["Final Salary"])
