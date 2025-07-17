thela = [["a",67],["b",89],["c",99],["d",34],["e",12]]

#we can typecast a list into dictionary

dict1 = dict(thela)
# print (dict1)

# for key,vall in dict1.items():      #in dictionary the key and it's associative value whole considered as an item
# print(vall)         #by default if just like list we try to fetch dictionary values. python will only fetch key but for whole key value pair we must have to use .items()

#exercise

list2 = [45,"radha", 2, "ashu", 9, 3,6,7,1, "rr", 99]

# for item in list2:
#     if type(item) == int:
#         if item >= 6:
#             print(item)

for item in list2:    #isdigit only checks for integers whereas isnumeric is more specifically check for fraction digits romans etc
    if str(item).isnumeric() and item >=6:
        print(item)
