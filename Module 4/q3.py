print("ATIF MOIN")
print("1900300100051")

x=int(input('Enter 1st number : '))
y=int(input('Enter 2nd number : '))
z=int(input('Enter 3rd number : '))

if (x>y and x<z) or (x>z and x<y):
    med=x
elif (y>z and y<x) or (y<z and y>x):
    med=y
else :
    med = z

print("Meadian is : ",med) 