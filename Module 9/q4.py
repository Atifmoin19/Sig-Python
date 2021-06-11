print("Atif moin")
print("1900300100051")
print('Q4:Write a Python program to write a list to a file.')

f=open('list.txt','w')
list1=[]
n=int(input('Enter number of element in list : '))
for j in range(n):
    s=input("Enter elements : ")
    list1.append(s+'\n')

for i in list1:
    f.write(i)

f.close()