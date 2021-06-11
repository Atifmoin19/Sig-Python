print("Atif moin")
print("1900300100051")
print('Q3:Write a Python program to count the number of lines in a text file.')
f=open('dummy.txt','r')
count=0
text= f.read()
list1=text.split("\n")

for i in list1:
    if i:
        count += 1

print(count)


