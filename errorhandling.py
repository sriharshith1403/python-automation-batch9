try:
    # Read length of the list
    n = input()
    
    # Check if n is numeric
    if not n.isdigit():
        print("Error: You must enter a numeric value.")
        exit()

    n = int(n)

    # Check if n is positive
    if n < 0:
        print("Error: The length of the list must be a non-negative integer.")
        exit()

    numbers = []

    # Read list elements
    for _ in range(n):
        value = input()
        
        # Check if element is numeric (handles negative integers too)
        if not value.lstrip('-').isdigit():
            print("Error: You must enter a numeric value.")
            exit()
        
        numbers.append(int(value))

    # Calculate average
    if n == 0:
        average = 0.00
    else:
        average = sum(numbers) / n

    # Print result
    print(f"{average:.2f}")

except Exception:
    print("Error: You must enter a numeric value.")




