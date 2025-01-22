class Student:
    def eligibility(self,percentage):
        if percentage >= 60:
            print("You are eligible for getting addmission in BCA")
        else:
            print("You are not eligible for getting addmission in BCA")

Student1 = Student()
Student1.eligibility("Surojit",75)

