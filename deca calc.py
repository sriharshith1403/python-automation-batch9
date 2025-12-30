#Defines a decorator function named calculator
# It takes another function as input (func)
def calculator(func):
#Defines an inner function
# This function will replace the original function
    def wrapper(a, b, op):
#Calls the original function (calculate)
# Passes the values a, b, and op
        return func(a, b, op)
    return wrapper


@calculator
def calculate(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b if b != 0 else "Division by zero error"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (add / sub / mul / div): ").lower()

print(calculate(a, b, op))