class lib1:
    def __init__(self, ad_name, lib_name, book_list ):
        self.ad_name = ad_name
        self.lib_name = lib_name
        self.book_list = book_list

    def display_books(self):
        return self.book_list

    def display_book(self, book_name):
        pass

print("hello..!! to establish the library tell me your name")
admin_name = input()
print("which name you want to give your library")
library_name = input()


print("add some books atleast 5, and 'quit' to exit")


i = True
book_names = []
while i:
    j = input(">>> ")

    if j == "quit":
        i = False
        break
    else:
        book_names.append(j)

print(book_names)

new_lib = lib1(admin_name, library_name, book_names)
