n=int(input("Enter the number:-"))
s=0
a=n
while n!=0:
    d=n%10
    n=n//10
    s=s*10+d
if a==s:
    print("palindome")
else:
    print("NOt palindrome")