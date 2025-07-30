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
sentence = sentence.split(" ")

ls = [i for i in sentence if len(i)%2 == 0]
ls2 = [i for i in sentence if len(i)%2 != 0]

ls.extend(ls2)
print(ls)
"""

# question 3:----
"""
words = ["apple", "banana orange", "grape", "kiwi mango"]

ls = []
for i in words:
    if i.count(" ") > 0:
        ls.append(i)
        words.remove(i)

new_ls = " ".join(ls)
new_ls = new_ls.split(" ")

words.extend(new_ls)
print(words)

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
    if len(i)<=2:
        ind = sent_as_ls.index(i)
        new_sent_as_ls.append(i)
        new_sent_as_ls.insert(ind+1,"definitely") #index+1 make sure insertion of definitely must be after the word which lenth is <=2
    else:
        new_sent_as_ls.append(i)


print(new_sent_as_ls)












