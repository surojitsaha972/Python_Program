n=str(input("Enter any roman number: "))
n.upper()
i=0
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
if(n==I):
    print("1")
elif(n==V):
    print("5")
elif(n==X):
    print("10")
elif(n==L):
    print("50")
elif(n==C):
    print("100")
elif(n==D):
    print("500")
elif(n==M):
    print("1000")
while i<len(n):
    s1=value()