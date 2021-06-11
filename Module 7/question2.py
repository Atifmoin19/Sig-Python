print("Atif Moin")
print("1900300100051")
print(" Write a Python function to check whether a number is in a given range.")

def inrange(x,y,z):
    if z in range(x,y):
        print(z,' : is in range ')
    else :
        print(z,' : is not in range')

x=int(input('Enter lower bound : '))
y=int(input('Enter upper bound : '))
z=int(input('Enter Value : '))
inrange(x,y,z)