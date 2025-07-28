# first step towards the file IO is opening a file by using the "open()"

f = open("demo.txt")  #open function return a file pointer, and then we can use that pointer to manipulate the file
# content = f.read()
# print(content)

for line in f:
    print(line, end="")  #used to iterate lines directly from the file pointer

f.close()   # it is mandatory to close the file too

#to ride file line by line we use print(f.readline())