print("Q2: Create a Student class and initialize it with name and roll number. Make methods to:\n")


class Student:
    def details(age,marks):
        default=input("Do you want to enter detials Y/N (if no then default info will show)")
        if(default=='N' or default =='n'):
            name= 'Atif'
            rollnum = '1900300100051'
        else:
            name= input("Enter the name : ")
            rollnum = input("Enter the roll number")
        print("Name = ",name)
        print("Roll number = ",rollnum)
        print("Age  = ",age)
        print("Marks = ",marks)


marks='Not given'
age=18
choice= int(input("1. Display - It should display all information of the student.\n2. setAge - It should assign age to student\n3. setMarks - It should assign marks to the student\n4.> Exit\nEnter your choice : "))
if (choice==1):
        print(Student.details(age,marks))
elif (choice==2):
        age=int(input("Enter your age : "))
        print(Student.details(age,marks))
elif (choice==3):
        marks=int(input("Enter Marks : "))
        print(Student.details(age,marks))
