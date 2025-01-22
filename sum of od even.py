list=[1,2,3,4,5,6,7,8]
print(list)
even=0
odd=0
for i in list:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Sum of odd no:-",odd)
print("Sum of even no:-",even)
