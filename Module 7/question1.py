print("Atif Moin")
print("1900300100051")
print("Write a Python function to multiply all the numbers in a list.")

def multiply_numbers_list(num):
     sum = 1
     for i in num:
         sum *= i
     return sum
    
lis=[]
n=int(input('enter number of input : '))
for i in range(0,n):
    num=int(input('enter numbers : '))
    lis.append(num)

print('Multiplication of numbers are : ',multiply_numbers_list(lis))