numbers = [10, 25, 3, 89, 45, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)