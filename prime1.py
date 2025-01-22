n=int(input("Enter any number: "))
# if n==1:
#     print("not prime")
# elif n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

count=0
for i in range(2,n):
    if n%i==0:
        count=1
        break
if count==0:
    print("Number is prime.")
else:
    print("Not prime")