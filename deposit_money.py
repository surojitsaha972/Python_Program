money=int(input("Enter the amount of money:-"))
days=int(input("Enter the days of scheme:-"))
if days<=180:
    money=money+(money*0.055)
    print(money)
elif days>180 or days<=364:
    money=money+(money*0.075)
    print(money)
elif days==365:
    money=money+(money*0.090)
    print(money)
elif days>365:
    money=money+(money*0.085)
    print(money)
else:
    print("Defaulf scheme.")