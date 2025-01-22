x=int(input("Enter 1st no.: "))
y=int(input("Enter 2nd no.: "))
z=int(input("Enter 3rd no.: "))
if(x>y and x>z):
    print(x," is the large no.")
elif(y>x and y>z):
    print(y," is the large no.")
else:
    print(z," is the large no.")
