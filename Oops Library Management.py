from datetime import datetime, timedelta
import random

# Library class to manage overall library attributes and methods
class Library:

  total_books = 0
  total_members = 0
  books = []
  members = []

  # Method to print borrowing limit
  def max_books(self):
   print("A person can borrow only 3 books")

  # Method to track and print library inventory and members
  def track(self):
   print(f"Total books: {Library.total_books}, Total members: {Library.total_members}")
   if Library.total_books > 0:
     print("Books:", self.books)
   if Library.total_members > 0:
     print("Members:", self.members)

  # Method to calculate and print book return due date
  def due_date(self):
   c_date=input("Enter date on which you borrowed the book in the format YYYY-MM-DD : ")
   b_date=datetime.strptime(c_date,"%Y-%m-%d").date()
   due_date=b_date+timedelta(days=15)
   print("Return the book by", due_date)

# Book class to represent individual books
class Book:

  def __init__(self, title, author_name):
   self.title = title
   self.author_name = author_name
   self.available = True
   Library.total_books+=1
   Library.books.append(self.title)

  # Method to check and update book availability
  def return_book(self, book):
   if self.borrowed_books > 0:
    self.borrowed_books -= 1
    book.available = True
    print(f"{self.name} returned {book.title}")

  #Availability of book
  def check_availability(self):
    if self.available:
      print(f"{self.title} is available")
    else:
      print(f"{self.title} is not available")

#Author class to implement individual Author
class Author :

    def __init__ (self,author_name,title) :
        self.author_name = author_name
        self.title = title
        self.author_id=random.randint(1000,10000)
        self.add_book(author_name,title)

    #add_book method is used to add a book into the library
    def add_book (self,author_name,title) :
        print(self.title,"written by",self.author_name,"is added")
        Library.books.append(self.title)
        Library.total_books+=1
        print(self.author_id,"is the author id")

#Member class is used to implement individual member of a library       
class Member :
    
    max_borrowed_books = 3

    def __init__ (self,name) :
        self.name = name
        Library.total_members += 1
        Library.members.append(self.name)
        self.mem_id=random.randint(1000,10000)

    #Method is used to implement borrowing system in library
    def borrow_book (self,book) :
        if Member.max_borrowed_books <= 0 :
            print(self.name,"had already borrowed 3 books. So can't borrow ",book)
        else:
            print(self.name,"borrowed",book)
            Member.max_borrowed_books -= 1
            borrow_date = datetime.now()
            self.due_date = borrow_date + timedelta(days=15)
            print("Return book by ", self.due_date.strftime("%Y-%m-%d"))


    #Implements returning of a book
    def return_book (self,book) :
      if self.due_date > datetime.now():
          print(self.name,"has returned the book",book, " with no penality")
      else:
          print(self.name,"has returned the book",book, " with penality of Rs.1000")
      Member.max_borrowed_books += 1
        

# Sample usage to demonstrate library operations
#Book class
book1 = Book("Book1", "Author1")
book1.check_availability()
#Author class
author = Author("Author2", "Book2")
author.add_book("Author3","Book3")
#Member class
member1=Member("Akhila")
member1.borrow_book("Book1")
member1.borrow_book("Book2")
member1.borrow_book("Book3")
member1.borrow_book("Book4")
member1.return_book("Book2")
#Library class
library = Library()
library.max_books()
Library.total_books
Library.total_members
library.track()
library.due_date()