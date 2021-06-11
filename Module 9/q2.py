
print("Atif moin")
print("1900300100051")
print('Q2:Write a Python program to append text to a file and display the text.')

f=open('new.txt','a')
n=input('Enter the string : ')
f.write(n+'\n')
f=open('new.txt','r')
print(f.read())
f.close()
f.close()