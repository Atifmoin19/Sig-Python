print("ATIF MOIN")
print("1900300100051")
print("Enter the number .....")
x=int(input('number='))
s=0
while (x!=0):
    n = x%10
    s=s+n
    x=int(x/10)

print(int(s))

