class student:
    def grade(self,name,roll,str,perc):
        if perc>80:
            print("A")
        elif perc>60 and perc<79:
            print("B")
        elif perc>40 and perc<59:
            print("C")
        else:
            print("Fail.")
obj1=student()
obj2=student()
#name=input("Enter the student name:-")
#perc=int(input("Enter the percentage:-"))
#roll=int(input("Enter the roll number:-"))
#str=input("Enter the stream:-")
obj1.grade("abc",101,"BCA",64)
obj2.grade("xyz",102,"BBA",85)
#obj1.grade(name,perc,roll,str)