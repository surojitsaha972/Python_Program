n=int(input("Enter the number:"))
while(n>0):
    j=n%10
    if j!=0 & j!=1:
        print("n is not binary")
        break
    n=n//10
    if n==0:
        print("n is binary")
