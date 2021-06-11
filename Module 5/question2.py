print("Atif Moin")
print("19003000100051")
list1=[]
list2=[]
n=int(input('Enter Number of element in list : '))
for i in range(0,n):
    ele=str(input('Enter element : '))
    list1.append(ele)

print("List name is : ",list1)

for j in range(0,n):
    list2.append(len(list1[j]))


print("List length is : ",list2)
maximum=max(list2)
print("Length of longest element is : ",maximum)
for k in range(0,n):
    if (len(list1[k])==maximum):
        print("Longest element is : ",list1[k])
    
