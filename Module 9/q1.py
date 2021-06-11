print("Atif moin")
print("1900300100051")

print("Q1:Write a Python program to read first n lines of a file.")

n=int(input('enter the number of lines u want to read : '))
f=open('dummy.txt','r')
for i in range (1,n+1):
    print(f.readlines(n))


f.close()