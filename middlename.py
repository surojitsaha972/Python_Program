name = input("Enter your name:- ")
name_words = name.split()
if len(name_words) == 2:
    print("This person does not have a middle name.")
elif len(name_words) == 3:
    print("This person has a middle name.")
else:
    print("This person's name is not in the correct format.")