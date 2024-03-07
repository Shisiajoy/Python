class Book:
    def __init__(self,title,author,isbn):
            #initialize book attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = True #initialy set to true to indicate book is checked out
           
    def check_out(self):   #method to check out the book
        if self.checked_out :
            print(f"{self.title} is already checked out.")

        else:
            self.checked_out = True
            print (f"{self.title}, has been checked out")
    
    def return_book(self):  #method to return the book
        if not self.checked_out:
            print(f"{self.title} is already returned")
        else:
            self.checked_out = False
            print (f"{self.title} has been returned")

class Library:
    def __init__ (self):
        self.book = [] #initialing a library withan empty list to store books

    def add_book(self,book):  #a method to add a book to the  library
        self.book.append(book)


my_Library = Library()  #creat a library instance

#creat book instance
book1 = Book("bible","several authors","2456789401")
book2 = Book("mummys cook book","mummy","9876543210")


#add books to the library
my_Library.add_book(book1)
my_Library.add_book(book2)

book1.check_out()
book2.return_book()


 