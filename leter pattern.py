# A
# for i in range(6):
#     for j in range(5):
#         if((j==0 or j==4) and (i!=0)) or (i==0 or i==3) and (j>0 and j<4):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# B
# for i in range(7):
#     for j in range(4):
#         if(j==0 or (j==3 and i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<3)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# C
# for i in range(5):
#     for j in range(4):
#         # if (j==0 and i!=0 and i!=4) or (i==0 or i==4):
#         if(j==0 or (i==0 or i==4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# D
# for i in range(4):
#     for j in range(3):
#         if(j==0 or (j==2 and i!=0 and i!=3)) or ((i==0 or i==3)):
#             print("*",end=" ")
#         else:
#             print(end="   ")
#     print()

# E
# for i in range(5):
#     for j in range(4):
#         if((j==0 or i==0 or i==4 or i==2)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# F
# for i in range(5):
#     for j in range(4):
#         if(j==0 or i==0 or (i==2 and j<3)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()

# G not complete
# for i in range(7):
#     for j in range(6):
#         if((j==0 and i!=0 and i!=6) or (j==4 and i!=0 and i!=2 and i!=3 and i!=6) or (i==0 or i==6) and (j>0 and j<4)) or (i==4) and (j==2 or j==3 or j==5):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# H
# for i in range(5):
#     for j in range(4):
#         if(j==0 or j==3 or i==2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# I
# for i in range(5):
#     for j in range(5):
#         if(j==2 or i==0 or i==4):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# J
# for i in range(5):
#     for j in range(5):
#         if(j==3 or (j==0 and i!=1 and i!=2) or i==0 or (i==4 and j<3)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# K
# iv=0
# jv=3
# for i in range(5):
#     for j in range(4):
#         if(j==0 or i==j+1):
#             print("*",end=" ")
#         elif i==iv and j==jv:
#             print("*",end=" ")
#             iv=iv+1
#             jv=jv-1
#         else:
#             print(end="  ")
#     print()

# L
# for i in range(5):
#     for j in range(4):
#         if(j==0 or i==4):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# M
# for i in range(7):
#     for j in range(7):
#         if (j==0 or j==6 or ((i==j) and (j>0 and j<4)) or ((i==1 and j==5) or (i==2 and j==4))):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# N
# for i in range(6):
#     for j in range(6):
#         if (j==0 or j==5 or ((i==j) and (j>0 and j<5))):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# O
# for i in range(5):
#     for j in range(4):
#         if(j==0 and i!=0 and i!=4) or (j==3 and i!=0 and i!=4) or (i==0 or i==4) and (j>0 and j<3):
#              print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# P
# for i in range(7):
#     for j in range(5):
#         if(j==0 or j==4 and i!=0 and i!=3 and i!=4 and i!=5 and i!=6) or (i==0 or i==3) and (j<4):
#              print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# Q
# for i in range(6):
#     for j in range(5):
#         if(j==0 and i!=0 and i!=4 and i!=5) or (j==3 and i!=0 and i!=5) or (i==0 or i==4) and (j>0 and j<3) or (i==5 and j==4):
#              print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# R
# for i in range(6):
#     for j in range(5):
#         if(j==0 or j==4 and i!=0 and i!=3) or (i==0 or i==3) and (j<4):
#              print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# S
# for i in range(7):
#     for j in range(6):
#         if(j==0 and i!=0 and i!=3 and i!=4 and i!=6) or (j==5 and i!=0 and i!=2 and i!=3 and i!=6) or (i==0 or i==3 or i==6) and (j>0 and j<5):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# T
# for i in range(5):
#     for j in range(5):
#         if(j==2 or i==0):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# U
# for i in range(6):
#     for j in range(5):
#         if(j==0 and i!=5) or (j==4 and i!=5) or i==5 and (j>0 and j<4):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# V
# iv=0
# jv=6
# for i in range(4):
#     for j in range(7):
#         if(i==j):
#             print("*",end=" ")
#         elif i==iv and j==jv:
#             print("*",end=" ")  
#             iv=iv+1
#             jv=jv-1          
#         else:
#             print(end="  ")
#     print()

# W
# for i in range(7):
#     for j in range(7):
#         if (j==0 or j==6 or ((i==j) and (j>2 and j<6)) or (i==4 and j==2) or (i==5 and j==1)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# X
# iv=0
# jv=4
# for i in range(5):
#     for j in range(5):         
#         if (i==iv and j==jv):
#             print("*",end=" ")
#             iv+=1
#             jv-=1
#         elif(i==j):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# Y
# iv=0
# jv=4
# for i in range(5):
#     for j in range(5):
#         if(i==j and j<3 or (j==2 and i!=0 and i!=1)):
#             print("*",end=" ")         
#         elif (i==iv and j==jv):
#             print("*",end=" ")
#             iv+=1
#             jv-=1
#         else:
#             print(end="  ")
#     print()

# Z
# iv=0
# jv=4
# for i in range(5):
#     for j in range(5):
#         if (i==iv and j==jv):
#             print("*",end=" ")
#             iv+=1
#             jv-=1
#         elif(i==0 or i==4):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
