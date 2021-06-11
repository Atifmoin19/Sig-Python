print("Atif moin")
print("1900300100051")
print("Q4: Write a Python program to multiply all the items in a dictionary.")

n=int(input("Enter the no of element u want to enter : "))

list1=[]
for i in range (0,n):
    b=int(input('Enter number : '))
    list1.append(b)
d={}
a=0
for i in range(0,len(list1)):
    d[a]=list1[i]
    a=a+1
print('Elements in dictionary are:',d)
mul=1
for j in d:
    mul = mul*d[j]

print('multiplication of every element in dictionary is :',mul)