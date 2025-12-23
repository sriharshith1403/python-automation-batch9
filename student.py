from Person import Person

class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


# Object creation
x = Student("harsh", "sri", 2025)

# Method calls
x.printname()
x.welcome()
