# Step 1: Using List to store marks
marks_list = []   # empty list to store marks

for i in range(1, 6):
    mark = int(input("Enter marks of subject %d: " % i))
    
    if mark < 0 or mark > 100:
        print("Invalid marks entered")
        exit()
    
    marks_list.append(mark)   # add marks to list

# Step 2: Using Tuple to store marks permanently (immutable)
marks_tuple = tuple(marks_list)  # convert list to tuple
print("Marks (Tuple):", marks_tuple)

# Step 3: Using Dictionary to store marks with subject names
subjects = ["Math", "Science", "English", "History", "Art"]
marks_dict = {}

for i in range(5):
    marks_dict[subjects[i]] = marks_list[i]   # key=subject, value=marks

print("Marks (Dictionary):", marks_dict)

# Step 4: Calculate total and average
total = sum(marks_list)
average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)