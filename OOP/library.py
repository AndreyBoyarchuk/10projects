class Library:
    def __init__(self, lisfOfBooks):
        self.avaliableBooks = lisfOfBooks

    def displayAvaliableBooks(self):
        print()
        print( "Aviliable Books" )
        for book in self.avaliableBooks:
            print( book )

    def lenBook(self, requestedBook):
        if requestedBook in self.avaliableBooks:
            print( "you have now borrowed the book" )
            self.avaliableBooks.remove( requestedBook )
        else:
            print( "Soory your books is not avaliable on our list " )

    def addBook(self, returnedBook):
        self.avaliableBooks.append( returnedBook )
        print( "You have returned the book" )


class Customer:
    def requestBook(self):
        print( "Enter the name of a book you would like to borrow!" )
        self.book = input()
        return self.book

    def returnBook(self):
        print( "Enter the name of the book which you returning" )
        self.book( input )
        return self.book


library = Library( ['Think and Grow Rich', 'Who will cry whe you die', 'For one More day'] )
customer=Customer()

while True:
    print("Enter 1 to display avaliable books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoice = int(input())

    if userChoice == 1:
        library.displayAvaliableBooks()
    elif userChoice == 2:
        requestedBook=customer.requestBook()
        library.lenBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()

    



