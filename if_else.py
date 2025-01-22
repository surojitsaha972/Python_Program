a=int(input("Enter 1st angle:-"))
b=int(input("Enter 2nd angle:-"))
c=int(input("Enter 3rd angle:-"))
if a+b+c==180:
    print("The tringle is possible.")
    if a==90 or b==90 or c==0:
        print("The tringle is rightangle.")
    elif a<90 and b<90 and c<90:
        print("The tringle is ocute.")
    else:
        print("Tne tringle is obtuse.")
else:
    print("The tingle is not possible.")