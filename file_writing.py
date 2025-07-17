# f = open("file.txt", "a")
#
# written_characters = f.write("coding is awesome\n")
# print(written_characters)
#
# f.close()

# for the read and write operation simultaneously on a file

f = open("file.txt", "r+")

print("write something")
f.write(input())
# f.write("do something productive")
print(f.read())

f.close()

