"""agenda:-- to create a attendance formatter with custom separator

tasks:--
1. take a list of student names
2. ask the user whether they are present 'p' or absent 'A'
3. store the present and absent students in separate lists
4. join the names of present with pipe '|' and absent student with ampersand'&'
"""

student_names = ["jhon", "rekha", "amitabh", "rohan" ,"rakesh", "vinod", "salman"]

list_absent = []
list_present = []
total_present = 0
total_absent = 0
for student in student_names:
    print("enter 'A ' for absent and 'P' for present")
    print("student name is: ",student)
    while True:
        user_input = input().strip().upper()
        if user_input == "P":
            list_present.append(student)
            total_present += 1
            break
        elif user_input == "A":
            list_absent.append(student)
            total_absent += 1
            break
        else:
            print("invalid input only enter either 'A' or 'P' for student: ", student)


print("present students: ",'|'.join(list_present))
print("absent students: ",' & '.join(list_absent))
print()
print(f"total students present : {total_present}")
print(f"total students absent : {total_absent}")
if len(list_absent) == 0:
    print("congratulation :all students are present")
elif len(list_present) == 0:
    print("is any holiday today because: all students are absent")
