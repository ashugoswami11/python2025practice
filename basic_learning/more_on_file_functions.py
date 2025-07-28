f = open("demo.txt")

print(f.readline())
print(f.tell())   # f.tell()  is to know at which character currently our file pointer f is at

f.seek(0)  # f.seek() reset the position of the f pointer anywhere we want  "parameter is must to pass"
print(f.tell())

f.close()

""" use of with block """
#with block is simply an alternative of the f = open("file.txt")
#using with block we don't need to close the file manually

with open("file.txt") as fp:
    print(fp.readline())




