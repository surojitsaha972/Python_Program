name1=input("Enter the 1st name of student:")
name2=input("Enter the 2nd name of student:")
name3=input("Enter the 3rd name of student:")
if name1>name2 and name1>name3:
    if name2>name3:
        print(name1,name2,name3)
    else:
        print(name1,name3,name2)
if name2>name1 and name2>name3:
    if name1>name3:
        print(name2,name1,name3)
    else:
        print(name2,name3,name1)
if name3>name2 and name3>name1:
    if name2>name1:
        print(name3,name2,name1)
    else:
        print(name3,name1,name2)