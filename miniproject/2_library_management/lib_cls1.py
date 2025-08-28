class Library:
    book_list = []
    lib_name = None
    dict1 = {}

    def __init__(self, book_list, lib_name):
        self.book_list = book_list
        self.lib_name = lib_name

    def display(self):
        return self.book_list

    def lend(self, borrower_name):
        print("which book do you want to borrow") #who owns the book if not available
        book = input()
        if book in self.book_list:
            pop_book = self.book_list.pop(self.book_list.index(book))
            self.dict1[borrower_name] = pop_book
            print(f"borrowing successful book name: '{book}' to borrower: {borrower_name}")
        else:
            for key, value in self.dict1.items():
                if value == book:
                    print(f" this book {value} is landed to {key}")
                else:
                    print("check spelling.!! book is nowhere")


    def add_book(self, book1):
        self.book_list.append(book1)


    def return_book(self, borrower_name):
        for key, value in list(self.dict1.items()):
            if key == borrower_name:
                popped_item = self.dict1.pop(key)
                self.book_list.append(popped_item)

    def disp_name(self):
        return self.lib_name

    def print_dict(self):
        for key, value in self.dict1.items():
            print(f"{key}: {value}")

list1 = ["harry potter", "eat the frog", "alchemist", "richest man in babylon", "rich dad poor dad"]
Ashu_library =   Library(list1, "Ashu_library")

if __name__ == "__main__":
    name = Ashu_library.disp_name()
    print(f"welcome to the {name}")

    print("tell me your name")
    user_name = input()

    while True:
        print(" tell me your choices what you want to do\n")
        print(" press 1 to display all the books available \n" ,
              "press 2 to borrow a book \n" ,
              "press 3 to donate a book to the library\n" ,
              "press 4 to return if you are borrowing a book\n" ,
              "press 6 to print who own which books\n" ,
              "press 5 to exit \n")

        ch1 = int(input())

        if ch1 == 1:
            list2 = Ashu_library.display()
            print("all the books available in the library are: ")
            for i in list2:
                print(i)
            print()

        elif ch1 == 2:
            Ashu_library.lend(user_name)

        elif ch1 == 3:
            print("what is the name of the book you want to donate")
            donation = input()
            Ashu_library.add_book(donation)
            print(f"thank you for donating a book to the {name}")

        elif ch1 == 4:
            Ashu_library.return_book(user_name)
            print("book return is successful")

        elif ch1 == 5:
            print(f"see you next time '{user_name}'\n Greetings: {name}")
            break

        elif ch1 == 6:
            Ashu_library.print_dict()

        else:
            print("please enter a valid choice")

