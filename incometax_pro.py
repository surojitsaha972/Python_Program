name=input("Enter the name of the person:-")
income=int(input("Enter the income of the person:-"))
age=int(input("Enter the age of the perosn:-"))
if age<60:
    if income<=25000:
        # print("Nill")
        print(income)
    elif income>25000 or income<=50000:
        income=income+(income*0.1)
        print(income)
    elif income>50000 or income<=100000:
        income=income+(income*0.2)+3400
        print(income)
    elif income>100000:
        income=income+(income*0.3)+9400
        print(income)
else:
    print("Wrong Catagory.")
