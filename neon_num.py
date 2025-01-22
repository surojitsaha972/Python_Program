n=int(input("Enter the number:-"))
sum=0
sqr=n**2
while sqr>0:
    d=sqr%10
    sum=sum+d
    sqr=sqr//10
if n==sum:
    print("Neon number.")
else:
    print("Not neon number.")