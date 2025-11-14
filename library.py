# Task Requirement:
# Create a file library.py with a Book class that:
# Uses an __init__ method to initialize:
# title
# author
# copies (how many copies are available)
# Add a method book_info() that returns:
# "Book: Harry Potter | Author: J.K. Rowling | Copies: 3"
# Add a method borrow_book():
# If copies > 0, reduce by 1 and return "Borrowed successfully!"
# Otherwise return "Sorry, no copies available."
# Add a method return_book():
# Increase copies by 1 and return "Book returned successfully!"

class Book :

    def __init__(self, title , author , copies):
        self.title = title
        self.author = author
        self.copies = copies

    def book_info(self):
        return f"Book : {self.title} | {self.author} | {self.copies}"

    def borrow_book(self):
        if self.copies > 0 :
            self.copies-=1
            return "Borrowed successfully!"
        else:return "Sorry, no copies available."

    def return_book(self):
        self.copies += 1
        return "Book returned successfully!"



