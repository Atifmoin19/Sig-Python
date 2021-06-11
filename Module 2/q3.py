print("Atif moin\n")
print("1900300100051\n")
print("Q.3=>WAP to find GCD of two numbers.\n")


print("Enter Two numbers : ")
n1 = int(input("x: "))
n2 = int(input("y: "))

while(n1!=n2):
    if n1>n2:
        n1=n1-n2
    else:
        n2=n2-n1

print("CGD = ",n1)