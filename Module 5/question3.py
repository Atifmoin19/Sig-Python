print("Atif Moin")
print("19003000100051")

list1=[]
n=int(input('Enter Number of element in list : '))
for i in range(0,n):
    ele=str(input('Enter element : '))
    list1.append(ele)

print("List name is : ",list1)

for i in range(0,n):
    if (i%2==0):
        list1[i]="#"
  

print("changed name is : ",list1)

