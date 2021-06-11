print("Atif moin")
print("1900300100051")
print("Q3: Write a Python program to remove item(s) from set.")

n=int(input("Enter the no of element u want to enter : "))

list1=[]
for i in range (0,n):
    b=int(input('Enter number : '))
    list1.append(b)

set2=set(list1)
print('Lset before deletion is :',set2)

d=int(input("enter the number u want to delete : "))

set2.discard(d)

print("after deletion : ",set2)