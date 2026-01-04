from database import create_table
from crud import add_student, view_students, update_student, delete_student

def menu():
    print("\n***** Student Management System *****")
    print("press 1: To ADD student")
    print("press 2: To VIEW students")
    print("press 3: To UPDATE student")
    print("press 4: To DELETE student")
    print("press 5: To exit ")
  
def main():
    create_table()
    
    while True:
        menu()
        choice = input("Enter Your Choice:")
        
        if choice == '1':
            name = input("Enter Student Name: ")
            age = int(input("Enter Student's Age: "))
            course = input("Enter Student's Course: ")
            
            add_student(name, age, course)
            print("Student Added Successfully!")
            
        elif choice == '2':
            students = view_students()
            for s in students:
                print(s)
                    
        elif choice == '3':
            student_id = int(input("Enter Student ID to Update: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            course = input("Enter New Course:") 
            update_student(student_id, name, age, course)
            print("student updated successfully!")
            
        elif choice == '4':
            student_id = int(input("Enter Student ID to Delete: "))
            delete_student(student_id)      
            print("Student Deleted Successfully!")
            
        elif choice == '5':
            print("Exiting the program. goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")
            
            
if __name__ == "__main__":
    main()