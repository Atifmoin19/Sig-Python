print("Atif moin\n")
print("1900300100051\n")
print("Q.2=>Write a Python program to check a triangle is equilateral, isosceles or scalene.\n")
s1=int(input('length of side 1 : '))
s2=int(input('length of side 2 : '))
s3=int(input('length of side 3 : '))
 
if s1==s2==s3:
      print(' This is Equiletral triangle\n')

elif(s1==s2 or s2==s3 or s3==s1):
    print("This is isosceles triangle\n")

else:
    print("This is scalene triangle\n")