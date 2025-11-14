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
# Create a main.py that:
# Imports the Book class.
# Creates 3 book objects.
# Prints info of each book.
# Simulates borrowing and returning books.
# Shows updated info after actions.

from library import Book

b1 = Book("ggg" , "ttt" ,2)

print(b1.book_info())

print(b1.borrow_book())

print(b1.book_info())

print(b1.return_book())

print(b1.book_info())
print("\n")
b2 = Book("sedond" , "jio" ,3)
print(b2.book_info())

print(b2.borrow_book())

print(b2.book_info())

print(b2.return_book())

print(b2.book_info())