# n=int(input("Enter the number:-"))
n=153
a=n
s=0
while n>0:
    s=s+(n%10)**3#(s%10)*(s%10)
    n=n//10
if a==s:
    print("Armstrome number")
else:
    print("Not Armstrome number")



# n=int(input("Enter any number: "))
# n=153
# sum=0
# temp=n
# while(temp>0):
#     dig=temp%10
#     cub=dig**3
#     sum+=cub
#     temp//=10
# if sum==n:
#     print("Armstrong")
# else:
#     print("not armstrong")