
print("Atif moin")
print("1900300100051")
print("Q2: Write one line of Python code that takes a list and makes a new list that has only the even elements.")

n=int(input("Enter the no of element u want to enter : "))

list1=[]
for i in range (0,n):
    b=int(input('Enter number : '))
    list1.append(b)

print('List items before are :',list1)

output_list=[var for var in list1 if var%2==0]
print(output_list)