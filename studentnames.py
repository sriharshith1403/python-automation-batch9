students = [
    ("sri", "harshith"),
    ("sai", "harshith"),
    ("k", "teja"),
    ("ram", "charan"),
    ("virat", "kohli"),
    ("rohit", "sharma"),
    ("singh", "dhoni"),
    ("sachin", "tendulkar"),
    ("anil", "kumble"),
    ("zaheer", "khan")
]

# set to track unique first names
unique_first_names = set()

# list to store final students after removing duplicates
final_students = []

# logic to keep only one student per first name
# not in it is operator to check if first name is already added in a collection
for first_name, last_name in students:
    if first_name not in unique_first_names:
        #it is a set to store unique first names
        unique_first_names.add(first_name)
        #Adds one student to the list
        # Only runs when the first name is unique
        # Maintains the order of students
        final_students.append((first_name, last_name))

# output the final student names
print("Students after removing duplicate first names:\n")
for student in final_students:
    #This line prints the first name and last name of one student.
    print(student[0], student[1])
