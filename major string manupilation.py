#perform differnt string manipulation operations.
"""""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
""""
#Calculate the Bill Amount

item_names = ["Rice", "Wheat", "Chocolate", "Biscuits"]
item_prices = [999.98, 49.99, 29.99, 19.99]
item_counts = [4, 2, 3, 5]

grand_total = 0   # To store total bill amount

for i in range(len(item_names)):
    total_cost = item_prices[i] * item_counts[i]
    grand_total += total_cost
    print("You bought %d %s for a total of %.2f"
          % (item_counts[i], item_names[i], total_cost))

print("Total Bill Amount: %.2f" % grand_total)

"""
# Employee Salary Calculator

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
years_of_experience = int(input("Enter years of experience: "))

# Bonus calculation using conditional statements
if years_of_experience >= 10:
    bonus = basic_salary * 0.20
elif years_of_experience >= 5:
    bonus = basic_salary * 0.10
else:
    bonus = basic_salary * 0.05

total_salary = basic_salary + bonus

# Formatted Output
print(
    "\n----- SALARY DETAILS -----\n"
    "Employee Name     : %s\n"
    "Basic Salary      : $%.2f\n"
    "Bonus Amount      : $%.2f\n"
    "Total Salary      : $%.2f"
    % (employee_name, basic_salary, bonus, total_salary)
)

