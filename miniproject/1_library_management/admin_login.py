username = "ashu@123"
password = "12345"
def admin_func():
    while True:
        count = 0
        while True:
            print("enter your username")
            input1 = input()
            if input1 == username:
                count += 1
                break
            else:
                print("please enter correct username")

        while True:
            print("enter your password")
            input2 = input()
            if input2 == password:
                count += 1
                break
            else:
                print("please enter correct password")

        if count == 2:
            print("would you like to watch list of books press 1",
                  "would you like to see who borrow which book press 2",
                  "do you want to add a new book in the library press 3")

            ch = int(input())
            if ch == 1:
                with open("book_list.txt", "r") as f:
                    items = f.readlines()
                    print(items)

            elif ch == 2:
                with open("book_list.txt", "r") as f:
                    items = f.readlines()

            elif ch == 4:
                break


admin_func()