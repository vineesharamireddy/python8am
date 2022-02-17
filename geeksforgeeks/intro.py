=============Basic programs==================
#1)Python program to add two numbers
------------int addition------------
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a+b
print("sum of {0} and {1} is {2}".format(a,b,c))

output:

enter first number34
enter second number23
sum of 34 and 23 is 57

--------float addition--------------

a=input("enter first number")
b=input("enter second number")
c=float(a)+float(b)
print("sum of {0} and {1} is {2}".format(a,b,c))

output:

enter first number1.45
enter second number23.54
sum of 1.45 and 23.54 is 24.99


#2)Maximum of two numbers in Python
-----------method 1------------
a=int(input("enter first number"))
b=int(input("enter second number"))
if a>b:
    print("a is maximum")
else:
    print("b is maximum")

output:

enter first number49
enter second number65
b is maximum

--------------method 2--------------
a=4
b=9
print(max(a,b))

output:

9

#3)Python Program for factorial of a number
--------method 1-----------
n=int(input())
for i in range(1,n):
    if i>0:
         n=i*n
print(n)

output:

5
120
-------------method 2-----------
def facto(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        f=1
        while(n>1):
            f=f*n
            n=n-1
        return f
n=5
print("factorial of", n, " is", facto(n))



#4)Python Program for simple interest
--------method 1---------
p=int(input())
r=int(input())
t=int(input())
a=(p*t*r)/100
print(a)

output:

50
45
23
517.5

------------method 2-----------
def si(p,t,r):
    print('principle is:',p)
    print("time is:",t)
    print('rate of intrest:',r)
    si=(p*t*r)/100
    print('simple intrest is:',si)
    
si(3,5,7)
output:

principle is: 3
time is: 5
rate of intrest: 7
simple intrest is: 1.05

#5)Python Program for compound interest{A = P(1 + R/100) t}(Compound Interest =A – P )

def ci(p,t,r):
   
    a= p * (pow((1+r / 100), t))
    ci=a-p
    print("simple intrest is:",ci)

ci(5000,12,9)

output:

simple intrest is: 9063.323908914484




#7)Python Program for Program to find area of a circle 
pi=float(3.14)
r1=float(input("radious"))
area=pi*r1*r1
print(float(area))

output:
radious   8.6
232.2344

#14)Python Program for Sum of squares of first n natural numbers
----method 1------
n=int(input())
a=0
for i in range(1,n+1):
    if i>=1 and i<=n:
        a=a+(i*i)
print(a)

output:
4
30

------method 2------

def sqsm(n):
 
 return (n*(n+1)*(2*n+1))//6
n=4
print(sqsm(n))

output:
30

#15)Python Program for cube sum of first n natural numbers
---------method 1-----------
n=int(input())
a=0
for i in range(1,n+1):
    if i>=1 and i<=n:
        a=a+(i*i*i)
print(a)
output:

5
225
---------method 2----------------
def cubsm(n):
 a=(n*(n+1))/2
 return (a*a)
n=5
print(cubsm(n))

output:

225.0
































