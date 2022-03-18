class Library:
    def __init__(self, ListOfBooks):
        self.ListOfBooks = ListOfBooks

    def DisplayAvaialableBooks(self):
        print("The Books available in the library are: ")
        for book in self.ListOfBooks:
            print(book)

    def IssueBook(self, bookname):
        if bookname in self.ListOfBooks:
            print("You have been issued a book", bookname,
                  "Please take care of it and return it within 30 days.")
            self.ListOfBooks.remove(bookname)
            return True
        else:
            print("Sorry currently we don't have this Book Or it Has been issued")
            return False

    def ReturnBook(self, bookname):
        self.ListOfBooks.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a Great day ahead!")

    def AddBook(self, bookname):
        if(bookname in self.ListOfBooks):
            print("We already Have this Book!\nCome again with another book")
        else:
            self.ListOfBooks.append(bookname)
            print("Thanks for donating the book:",
                  bookname, "We are Grateful☺")


class Student:
    def IssueBook(self):
        self.book = input("Enter the name of the book you want to issue: ")
        return self.book

    def ReturnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    def AddBook(self):
        a = (input("Enter the name of the book you would like to donate:"))
        return a


if __name__ == "__main__":
    centralLibrary = Library(
        ["Data Structures", "Algorithms", "Java", "C", "C++", "Python", "Machine Learning"])
    student = Student()
    # centralLibrary.DisplayAvaialableBooks()
    while(True):
        print('''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Issue a book
        3. Return a book
        4. Add a book to the library
        5. Exit the Library
        ''')
        a = int(input("Enter Your choice: "))
        if (a == 1):
            centralLibrary.DisplayAvaialableBooks()
        elif (a == 2):
            centralLibrary.IssueBook(student.IssueBook())
        elif (a == 3):
            centralLibrary.ReturnBook(student.ReturnBook())
        elif (a == 4):
            centralLibrary.AddBook(student.AddBook())
        elif (a == 5):
            print("Thanks for visiting the library. Have a great day ahead!✌")
            exit()
        else:
            print("Invalid character")
