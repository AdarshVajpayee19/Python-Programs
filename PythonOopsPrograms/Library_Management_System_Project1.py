# Create a library class
# display book
# lend book
# return book

# adarshLibrary = Library(listofbooks,library_name)
# Dictionary (books-nameofperson)

# Create main function and run an infinite loop asking users for their input

class Library:
    def __init__(self, list, name):
        self.name = name
        self.bookslist = list
        self.lendDict = {}

    def display_book(self):
        print(f"We have following books in our library:  {self.name}")
        for book in self.bookslist:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book DataBase has been updated. you can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def add_book(self, book):
        self.bookslist.append(book)
        print("Books has been added to the book list")

    def return_book(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    adarsh = Library(['python', 'Rich daddy poor daddy', 'Harry potter', 'C++ basics', 'Algorithms by ClR'], "AdarshVajpayee")

    while True:
        print(f"Welcome to the {adarsh.name} library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            adarsh.display_book()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name : ")
            adarsh.lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            adarsh.add_book(book)

        elif user_choice == 4:
            book = input("Enter the name of the bok u want to return: ")
            adarsh.return_book(book)

        else:
            print("Not a Valid Option!!!")

        print("Press Q to quit and C to continue")
        user_choice2 = " "
        while user_choice2 != "Q" and user_choice2 !="C":
            user_choice2 = input()
            if user_choice2 == 'Q':
                exit()
            elif user_choice2 == 'C':
                continue
            else:
                print("Please Enter Valid Option!!")

