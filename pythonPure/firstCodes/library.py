class Library:
    def __init__(self, listOfBooks):
        self.availablBooks =listOfBooks

    def displayAvailablBooks(self):
        print()
        print("Available Books: ")
        for book in self.availablBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availablBooks:
            print("You have now borrowed a book.")
            self.availablBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")

    def addBook(self, returnedBook):
        self.availablBooks.append(returnedBook)
        print("You have returned the book. Thank you!")


class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich', 'Who will Cry When You Die', 'For One More Day'])
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())

    if userChoice is 1:
        library.displayAvailablBooks()
    if userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice is 4:
        quit()