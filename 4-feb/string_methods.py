#Task1:Get one string from user & identify the middle character of the string

a='all the best'
b=(len(a))
print(b)
c=b//2
print(a[c])

output:

12
e


#Task2:    string1: ***python***
#      string: ********java*******
#output: python  java   [using(strip,rstrip,lstrip method *)]

string1="****python********"
string="********java*******"
#print(string1.strip())
#print(string.strip())

print(string1.lstrip("*").rstrip("*"))
print(string.lstrip("*").rstrip("*"))

output:

python
java


# Task3: (name<space>float)   collect three strings from user  name<space>float

#string1: "ravi 10.30"  
#string2: "meghala 12.19"
#string3: "Gokul 20.20"     (split + indexing)

#10.30 + 12.19 + 20.20 ===> output ===> add it 42.69


a=input("enter string 1")
b=input("enter string 2")
c=input("enter string 3")

#print(a)
#print(b)
#print(c)

d=a.split(' ')
e=b.split(' ')
f=c.split(' ')

l=print(d[1])
m=print(e[1])
n=print(f[1])

l=float(d[1])
m=float(e[1])
n=float(f[1])

p=float(l+m+n)
print(p)

output:

enter string 1ravi 10.30
enter string 2meghala 12.19
enter string 3gokul 20.20
10.30
12.19
20.20
42.69

#Task4:   collect two strings from user  
#string1: java    
#String2: python    (output ===> jythonpava64hv)

#string1: science     string2: maths    (output ===> sathsmcience57te)


str1=input("string1")
str2=input("string2")

print(str1[0],str2[1:],str2[0],str1[1:])
b=len(str2)
a=len(str1)
print(b,a)
c=a//2
d=b//2
print(str2[d],str1[c])

output:

string1science
string2maths
s aths m cience
5 7
t e


#Task6:   collect one string from user:  string: computer  (output: c6r)
#string: mathematics   (output: m9s)

a=input("string ")
b=len(a)
print(a[0],b-2,a[-1])

output:

string mathematics
m 9 s

string computer
c 6 r


#Task7:    Say hello world with python

a="say hello world  "
b="with python"
c=a+ b
print(c)

output:

say hello world  with python

#Task 8: swapcase

a="WelComeTo Python PROGramming"
b=a.swapcase()
print(b)

output:

wELcOMEtO pYTHON progRAMMING

#Task9:   what's your name

a=input("wat's your name")
print(a)

output:

wat's your name vinni
 vinni

#Task11:  Arithmetic operator  & Task12:python divison

a=24
b=6
#addition
c=a+b
print(c)
#substraction
d=a-b
print(d)
#multiplication
e=a*b
print(e)
#division
f=a/b
print(f)
#floor ivision
g=a//b
print(g)
#modulus
h=a%b
print(h)
#exponent
i=a**b
print(i)

output:

30
18
144
4.0
4
0
191102976
​





