#question 1:--
"""
s1 = "9,1,6,3"
s2 = "8,2,5"

s1 = s1.split(",")
s2 = s2.split(",")
s1.extend(s2)

ls = [int(i) for i in s1 ]
ls.sort()
ls.insert(1,10)
print(ls)
"""

# #question 2:----
"""
sentence = "python is awesome and powerful"
words = sentence.split(" ")

result = []
for word in words:
    if len(word)%2 == 0:
        result.insert(0,word)
    else:
        result.append(word)

print(result)
"""

# question 3:----

"""

Never remove elements from a list while iterating on it.
Use a new list (result) and build the final data.

words = ["apple", "banana orange", "grape", "kiwi mango"]

ls = []
for i in words:
    if " " in i:
        ls.extend(i.split(" "))
    else:
        ls.append(i)

print(ls)
"""

#question 4:--
"""
given_str = "5 3 7 1 9"

ls = [int(i) for i in given_str.split(" ")]

new_ls = []
for i in ls:
    if i % 2 == 0:
        new_ls.append(i)
    else:
        new_ls.insert(0,i)

new_ls.sort(reverse=True)
print(new_ls)
"""

#question 5:----

sent = "Ashu is learning Python"

sent_as_ls = sent.split(" ")

new_sent_as_ls = []
for i in sent_as_ls:
    new_sent_as_ls.append(i)
    if len(i)<=2:
        new_sent_as_ls.append("definitely")

print(new_sent_as_ls)












