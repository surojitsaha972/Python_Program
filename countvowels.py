str1=input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
bspaces=0
for i in str1:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1
    else:
        bspaces+=1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of blank spaces:", bspaces)