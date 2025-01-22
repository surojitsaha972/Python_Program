n=int(input("Enter the number:"))
first,second=0,1
print("fibonaci series are:")
for i in range(0,n):
    if(i<=1):
        result=i
    else:
        result=first+second
        first=second
        second=result
        print(result)
    # print(result)
