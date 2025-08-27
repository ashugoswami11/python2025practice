def member_func():
    print("hey.! member enter your name")
    username = input()
    with open("member_list.txt", "r") as f:
        items = f.readlines()
    items = [items.strip() for items in items]

    if  username in items:
        print("your name is already exist ")
    else:
        with open("member_list.txt", "a") as file:
            file.write(username + "\n")

    return username


def admin_func2(u_name):
    global popped_book
    print(f"heyy.!! {u_name} ",
          "would you like to watch list of books press 1",
          "would you borrow a book press 2",
          "do you want to return the book press 3")
    ch1 = int(input())
    if ch1 == 1:
        with open("book_list.txt", "r") as f:
            items = f.readlines()
            print(items)

    if ch1 == 2:
        print("please enter the name of the book you want to borrow")
        book_name = input()
        with open("book_list.txt", "r") as f:
            items1 = f.readlines()
            items1 = [items1.strip() for items1 in items1]
        if book_name in items1:
            popped_book = items1[items1.index(book_name)]
        with open("book_list.txt", "w") as f:
            for item in items1:
                f.write(item + "\n")

        with open("borrowers.txt", "a") as f:
            f.write(f"{u_name : popped_book},  \n")

    if ch1 == 3:
        print("enter the name of the book you want to return")
        book_name = input()
        with open("borrowers.txt", "r") as f:
            items = f.readlines()
        items = [items.strip() for items in items]


u_name = member_func()
admin_func2(u_name)