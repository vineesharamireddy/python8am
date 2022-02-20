================strings================
#1) Python program to check if a string is palindrome or not

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

#2)  Python program to check whether the string is Symmetrical or Palindrome












#3)  Reverse words in a given String in Python

string="welcome to python class"
l=string.split(" ")
print(l[::-1])

output:
['class', 'python', 'to', 'welcome']

#2) Python program to print even length words in a string

string="welcome to python class"
l=string.split(" ")
for word in l:
    if len(word)%2==0:
        print(word)
output:

to
python


#4) Ways to remove i’th character from string in Python

str1="mathematics"
a=len(str1)
str2=""
for i in range(a):
    if i!=3:
        str2=str2+str1[i]
print(str1)
print(str2)

output:

mathematics
matematics

#5) Find length of a string in python (4 ways)
---------method 1-------------
def l_str(a):
    c=0
    for i in a:
        c=c+1
    return c
a="hello world"
print(l_str(a))

output:

11

----------mrthod 2-----------
s="maths"
n=len(s)
print(n)

output:

5



















    
               

