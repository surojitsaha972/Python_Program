def sum():
    a=10
    b=20
    c=a+b
    print("No return ttype without parameter.",c)
sum()

def sum(a,b):
    print("No return type with parameter",a+b)
a=10
b=20
sum(a,b)

def sum(a,b):
    return a+b
print("Return type with parameter.",sum(10,20))

def sum():
   a=10
   b=20
   return a+b
print("No return type without parameter",a+b)

def sum(a,b=5):
    c=a+b
    print(c)
sum(5)
sum(5,2)

def sum(a,b):
    c=a+b
    print(c)
sum(5,b=8)
sum(b=6,a=3)

a=7
def show():
    a=5
    print(a)
print(a)
show()
print(a)

a=7
def show():
    global a
    a=5
    print(a)
print(a)
show()
print(a)

def sum(*arg):
    print(arg[0])
    print(arg[1])
    print(arg[2])
sum(5,6,7)

def sum(**args):
    print(args['a'],args['b'])
sum(a=5,b=6)

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(1,10):
    x=fibo(i)
    print(x)

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return (b,a%b)
x=gcd(48,32)
print(x)