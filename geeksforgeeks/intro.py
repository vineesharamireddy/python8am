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




#6)Python Program for Program to find area of a circle 
pi=float(3.14)
r1=float(input("radious"))
area=pi*r1*r1
print(float(area))

output:
radious   8.6
232.2344

#7)Python Program for Sum of squares of first n natural numbers
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

#8)Python Program for cube sum of first n natural numbers
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

#9)Program to print ASCII Value of a character
def asc(a):
    b=ord(a)
    return b
a="f"
print(asc(a))

output:

102

##10)Python Program to check Armstrong Number

def ordr(a):
    n=0
    while(a!=0):
        n=n+1
        a=a//10
    return(n)
def armstrg(a):
    n=ordr(a)
    temp=a
    sum1=0
    while(temp!=0):
        r=temp%10
        sum1=sum1+pow(r,n)
        temp=temp//10
    return(sum1==a)
a=9874
print(armstrg(a))
a=153
print(armstrg(a))

output:

True
False

#11) Python program to check whether a number is Prime or not

a=13

if a>1:
    for i in range(2,int(a/2+1)):
        if a%i==0:
            print("not prime")
            break
        else:
            print("prime")
else:
    print("not prime")

output:

13 prime
13 prime
13 prime
13 prime
13 prime

#12)Python program to print all Prime numbers in an Interval

def prime_num(a,b):
    pl=[]
    for i in range(a,b):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
                else:
                    pl.append(i)
    return pl
x=6
y=19
li=prime_num(x,y)
if li == 0:
    print("no prime numbers between range")
else:
    print("list of prime numbers are:",li)
    print(set(li))

output:


list of prime numbers are: [7, 7, 9, 11, 11, 11, 11, 13, 13, 13, 13, 13, 15, 17, 17, 17, 17, 17, 17, 17]
{7, 9, 11, 13, 15, 17}


## 13)Python Program for n-th Fibonacci number


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(7))

output:

8

##14)Python Program for How to check if a given number is Fibonacci number?

import math
def psquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return psquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
for i in range(1,11):
     if (isFibonacci(i) == True):
         print (i,"is a Fibonacci Number")
     else:
         print (i,"is a not Fibonacci Number ")

output:

1 is a Fibonacci Number
2 is a Fibonacci Number
3 is a Fibonacci Number
4 is a not Fibonacci Number 
5 is a Fibonacci Number
6 is a not Fibonacci Number 
7 is a not Fibonacci Number 
8 is a Fibonacci Number
9 is a not Fibonacci Number 
10 is a not Fibonacci Number 


## 15)Python Program for n\’th multiple of a number in Fibonacci Series















