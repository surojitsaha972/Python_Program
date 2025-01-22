# 1
# a=5
# b=6
# print("The sum of two numbers is : ",a+b)

# 2
# n=6
# if(n%2==0):
#     print("divided by 2.")
# else:
#     print("Not divided")

# 3
# a=35
# b=80
# if(a>b):
#     print("A is greater")
# else:
#     print("B is greater.")

# 4
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print("Average of two number is:",(a+b)/2)

# 5
# a=int(input("Enter a number:"))
# print(a**2)

# 6
# n=str(input("Enter your name:"))
# print("Good Afternoon",n)

# 7
# name="Surojit Saha"
# date="06/01/2025"
# print("Dear",name,"Your are selected!\n",date)

# 8
# print("Dear Surojit,\n\tHello this is my python folder\nCheck it!")

# 9
# list1=[]
# list1.append(input("Enter any name:"))
# print(list1)

# 10
# n=[1,2,3,4]
# sum=0
# for i in n:
#     sum+=i
# print(sum)

# 11
# n=(1,0,2,0,1,0,2,0,3)
# c=n.count(0)
# print(c)

# 12
# trs={
#     "sakti":"power",
#     "din":"Day",
#     "rat":"Night"
# }
# trs.update({"biporit":"opposite"})
# print(trs)

# 13
# s=set()
# s.add(20)
# s.add(19.5)
# s.add("20")
# print(len(s))

# 14
# s=set()
# print(type(s))

# 15
# dist={}
# dist.update({"Suro":"Math","Arpan":"History","Sunny":"Bengali","Rup":"Python"})
# print(dist.keys())
# print(dist.get("Suro"))
# print(dist)

# 16
# dist={}
# dist.update({"Suro":"Math","Arpan":"History","Sunny":"Bengali","Suro":"Python"})
# print(dist.get("Suro"))

# 17
# a=int(input("Enter 1st num: "))
# b=int(input("Enter 2nd num: "))
# c=int(input("Enter 3rd num: "))
# d=int(input("Enter 4th num: "))
# if(a>b and a>c and a>d):
#     print("Greater number is:",a)
# elif(b>a and b>c and b>d):
#     print("Greater number is:",b)
# elif(c>a and c>b and c>d):
#     print("Greater number is:",c)
# else:
#     print("Greater number is:",d)

# 18
# ben=int(input("Enter marks: "))
# eng=int(input("Enter marks: "))
# math=int(input("Enter marks: "))
# avg=(ben+eng+math)/3
# if(avg>=40):
#     if(ben>=33 and eng>=33 and math>=33):
#         print("Pass")
#     else:
#         print("fail")
# else:
#         print("fail")

# 19
# a="subscribe this"
# b=input("Enter a cmt:")
# if(b==a):
#     print("Spam Comment")
# else:
#     print("Not spam massage")

# 20
# s=input("Enter your name:")
# if(len(s)>10):
#     print("your name is greater than 10 characters")
# else:
#     print("your name is less than 10 characters")

# 21
# n=5
# for i in range(1,11):
#     print(f"{n}*{i}=",n*i)

# 22
# l1=["Rup","Surojit","Sunny","Arpan"]
# for i in l1:
#     if i.lower().startswith('s'):
#         print(f"Hello {i}")

# 23
# n=12
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count=1
#         break
# if count==0:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

# 24
# n=5
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print(s)

# 25
# n=5
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)

# 26
# n=3
# for i in range(0,n):
#     for j in range(i+1):
#         print("*",end='')
#     print()

# 27
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

# 28
# for i in range(3):
#     for j in range(3):
#         if((j==0) or (i==0 or i==2)):
#             print(" *",end=" ")
#     print()

# 29
# n=6
# for i in range(10,0,-1):
#     print(f"{n}*{i}=",n*i)

# 30
# def gb():
#     print("Good Bye")
# gb()

# 31
# def g(n):
#     gr="Hello "+n
#     return gr
# a=g("suro")
# print(a)

# 32
# def greater(a,b,c):
#     if(a>b and a>c):
#         print("Greater number is: ",a)
#     elif(b>a and b>c):
#         print("Greater number is: ",b)
#     elif(c>b and c>a):
#         print("Greater number is: ",c)
#     else:
#         print("default")
# greater(5,7,6)

# 33
# # def convert(c):
# def convert(f):
#     # f=(c*1.8)+32
#     c=(f-32)/1.8
#     print(c)
# convert(90)

# 34
# def sum(n):
#     s=0
#     for i in range(n+1):
#         s=s+i
#     print(s)
# sum(5)

# 35
# def p(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end=" ")
#         print()
# p(3)

# 36
# def convert(i):
#     c=i*2.54
#     print(c)
# convert(90)

# 37
# def mul():
#     n=int(input("Enter a number:"))
#     for i in range(1,11):
#         print(f"{n}*{i}:",n*i)
# mul()

# 38
