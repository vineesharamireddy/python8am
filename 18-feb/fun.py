# Write function to concatenate three strings

def cancatnt(a,b,c):
    d=a+b+c
    return d
print(cancatnt("hi"," hello"," namaste"))

output:

hi hello namaste

# Write a function multiply three different integers and return a int

def prdct(a,b,c):
    d=a*b*c
    return d
print(prdct(2,3,4))
print(prdct(4,6,2))

output:

24
48

## Write a function to return middle char of the string

def midchar(a):
    b=int(len(a)/2)
    return (a[b])
print(midchar("umberilla"))

output:

r

## write a function to return whether middle character is vowel or not 
def mid_vow(a):
    b=int(len(a)/2)
    c=a[b]
    if c in ["a","e","i","o","u"]:
        print("middle char is vowel")
    else:
        print("middle char is not vowel")
    return c
print(mid_vow("alphabets"))

output:

middle char is vowel
a

##whether the string is palindrome or not

def string(a):
    if a[::]==a[::-1]:
        print(a," :is polindrome")
    else:
        print(a,":is not polindrome")
    return a
print(string("malayalam"))
print(string("python"))

output:

malayalam  :is polindrome
malayalam
python :is not polindrome
python

#  whether the number is armstrong or not

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

False
True

##Find factorial of a number using function

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

output:

factorial of 5 is 120

5. Find factorial of a number using recursive function
## Find factorial of a number without using function

a=int(input())

if a<0:
    print("not a valid num")
elif a==0 or a==1:
    print("factorial is 1")
elif a>0:
    temp=1
    while(a>1):
        temp=temp*a
        a=a-1
print("factorial is:",temp)

output:

5
factorial is: 120



##without using while

n=int(input())

for i in range(1,n):
    if n<0:
        print("factorial is 0")
    elif n==0 or n==1:
        print("factorial is 1")
    else:
        n=i*n
print(n)

output:

5
120



















