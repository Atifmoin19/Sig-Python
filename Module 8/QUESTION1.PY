print("Atif moin")
print("1900300100051")
print("Q1: Write a Python code to print the sum of all the items in a list using list comprehension.")

n=int(input("Enter the no of element u want to enter : "))

list1=[]
for i in range (0,n):
    b=int(input('Enter number : '))
    list1.append(b)

print('List items are :',list1)

output_list={sum(list1) for var in list1}
print(output_list)
