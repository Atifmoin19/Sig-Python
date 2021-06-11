print("Atif Moin")
print("19003000100051")

list1=[]
list2=[]
n=int(input('Enter Number of element in list : '))
for i in range(0,n):
    ele=str(input('Enter element : '))
    list1.append(ele)

print("Orignal List is : ",list1)

list2=list1[:]

print("copied  List is : ",list2)