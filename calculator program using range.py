def calculator(a, b, choice):
    # Using range to map choices
    if choice in range(1, 2):        # choice = 1
        return a + b                 # Addition

    elif choice in range(2, 3):      # choice = 2
        return a - b                 # Subtraction

    else:
        return "Invalid choice"
