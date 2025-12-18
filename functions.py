"""""
a=-90
print(abs(a))
def cal_speed(distance, time):
    return distance / time
#user-defined
def cal_velocity(displacement, time):
    return displacement / time
#inbuilt
d =dict(a=1, b=2, c=3)
"""
"""""
def get_overall_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "F"


subjects = {} #dictionary
failed_subjects = []#list
total_marks = 0

n = int(input("Enter number of subjects: "))
max_marks = n * 100   # each subject out of 100

for i in range(n):
    name = input(f"\nEnter subject {i+1} name: ")
    mark = int(input(f"Enter marks for {name}: "))

    subjects[name] = mark
    total_marks += mark
#store the subject marks and add them to the total marks.
    if mark < 35:
        failed_subjects.append(name)

percentage = (total_marks / max_marks) * 100

print("\n--- RESULT ---")
for subject, mark in subjects.items():
    print(subject, ":", mark)

print("\nTotal Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%") # it will round to 2 decimal places
print("Overall Grade:", get_overall_grade(percentage))

if failed_subjects:
    print("\nFAILED in subject(s):")
    for sub in failed_subjects:
        print(sub)
else:
    print("\nPASSED in all subjects")

"""


def calculator(a, b, choice):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid choice"


print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = int(input("Enter your choice (1-4): "))

result = calculator(num1, num2, choice)
print("Result:", result)

