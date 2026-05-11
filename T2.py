#library management system

class Book:
    def __init__(self, title, author, num_pages, num_copy):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.num_copy = num_copy

class Library:
    def __init__(self):
        self.booksList = [] #empty list

    def add_book(self, title, author, num_pages, num_copy):
        book = Book(title, author, num_pages, num_copy)
        self.booksList.append(book)
        book.num_copy += 1

    def remove_book(self, title):
        for book in self.bookList:
            if book.title == title:
                self.booksList.remove(book)
                book.num_copy - 1
                print(f"{title} is removed")
                return
        print("Book was not found!")

    def check_in(self, title):
        for book in self.booksList:
            if book.title == title:
                book.num_copy += 1
                print(f"Checked in {title}: Copies in available {book.num_copy}")

    def check_out(self, title):
        for book in self.booksList:
            if book.title == title:
                if book.num_copy > 0:
                    book.num_copy -= 1
                    print(f"Checked out {title}. Copies left: {book.num_copy}")
                else:
                    print("There are no copies available.")
                return
            print("Book not found.")

    def showListBooks(self):
        for book in self.booksList:
            print(f"{book.title} : {book.author} : {book.num_pages} pages : {book.num_copy} copies")

#program:

print("------------------------")
print("-   Library program    -")
print("------------------------")

lib = Library()

while True:

    print("\n1. Show list of all books in the library:")
    print("2. Add a book")
    print("3. ")
    print("")
    print("")
    print("")



    title = input("Enter the title of the book: ")

    author = input("Enter name of author: ")

    num_pages = input("Enter number of pages: ")
    lib.add_book(title, author, num_pages)

    rmBook = input("Enter book you want to remove from library system: ")



    quit = input("Type Quit to end program")
    if quit == "Quit":
        break

#automatically print list(for testing)
lib.showListBooks()





