class Library:
    def __init__(self, library_name, location): #unique attributes
        self.library_name = library_name
        self.location = location
        self.books = []          # list to store book names

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' removed from the library.")
        else:
            print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print(f"Books available in {self.library_name} ({self.location}):")
            for book in self.books:
                print("-", book)


library = Library("Central Library", "Visakhapatnam")

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.display_books()

library.remove_book("Data Structures")
library.display_books()
