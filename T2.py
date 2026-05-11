#library management system

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

class Library:
    def __init__(self):
        self.booksList = [] #empty list

    def add_book(self, title, author, num_pages):
        book = Book(title, author, num_pages)
        self.booksList.append(book)

    def showListBooks(self):
        for book in self.booksList:
            print(f"{book.title} : {book.author} : {book.num_pages}")

#program:

print("------------------------")
print("-   Library program    -")
print("------------------------")

lib = Library()

while True:
    title = input("Enter the title of the book: ")
    author = input("Enter name of author: ")
    num_pages = input("Enter number of pages: ")
    lib.add_book(title, author, num_pages)

    quit = input("Type Quit to end program")
    if quit == "Quit":
        break

#automatically print list(for testing)
lib.showListBooks()





