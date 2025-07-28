# dict1 = {"ashu":"student", "goswami":"cast", "ankit":"dixit"} #dictionary is made up with curly brackets
# print(dict1["ashu"])  #key value pairs so if we type key we'll get it's value
#
# #we can make dictionary inside a dictionary
# dict1 = {"ashu":"student", "goswami":"cast", "ankit":{"a":"for apple", "b":"for ball"}}
# print(dict1["ankit"]["a"])
#
# #adding items in the dictionary
# dict1["pooja"] ="chauhan"  #just by adding a key and value will add another key and value pair
# print(dict1)

person={"ashu":"student", "age":24}

new_person = person.copy()  #here i might think it just copy dictionary item into another dictionary but actually both are just pointers pointing towards the same dictionary
new_person["age"] = 56 #here inactual person's value is manipulated instead of new dict new_person

person.update({"jhonny":"sins"}) #to add a key value in the dictionary

print(person.items())
# print(new_person)

