=================list===========================
list=[2,4,6,3,57,9,1]

#1) Python | Reversing a List
print(list[::-1])

#2) Python program to find sum of elements in list
print(sum(list))

#3) Python program to find smallest number in a list
print(min(list))

#4) Python program to find largest number in a list
print(max(list))

output:

[1, 9, 57, 3, 6, 4, 2]
82
1
57

#5)Python program to print even numbers and odd numbers in a list

li=[2,4,6,3,9,5]
li_even=[]
li_odd=[]

for i in li:
    if i%2 == 0:
        li_even.append(i)
        print("even number list is:" ,li_even)
    elif i%2==1:
        li_odd.append(i)
        print("odd number list is:",li_odd)

output:

even number list is: [2]
even number list is: [2, 4]
even number list is: [2, 4, 6]
odd number list is: [3]
odd number list is: [3, 9]
odd number list is: [3, 9, 5]

#6,7) Python program to print all even numbers and odd numbers in a range

a=int(input())
b=int(input())
l1=[]
l2=[]
for i in range(a,b):
    if i %2==0:
        l1.append(i)
        
    else:
        l2.append(i)
print("even number list:",l1)
print("odd nuber list:",l2)

output:

10
30
even number list: [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
odd nuber list: [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        
#8,9) Python program to print positive numbers and negative numbers in a range

m=int(input())
n=int(input())
for i in range(m,n):
    if i>0:
        print(i,":is positive number")
    elif i<0:
        print(i,":is negative number")
    else:
        print(i," :is invalid number")
output:

-2
3
-2 :is negative number
-1 :is negative number
0  :is invalid number
1 :is positive number
2 :is positive number

#10,11) Python program to print positive numbers and negative numbers in a list

l=[-2,-4,0,6,9,4,-9]
for i in l:
    if i>0:
        print(i,":is positive number")
    elif i<0:
        print(i,":is negative number")
    else:
        print(i," :is invalid number")

output:

-2 :is negative number
-4 :is negative number
0  :is invalid number
6 :is positive number
9 :is positive number
4 :is positive number
-9 :is negative number

#12) Remove multiple elements from a list in Python

li=[2,4,6,3,9,5,-6]
li.pop(4)
print(li)
li.remove(2)
print(li)
del li[1:4]
print(li)

output:

[2, 4, 6, 3, 5, -6]
[4, 6, 3, 5, -6]
[4, -6]

#13) python program to find Cumulative sum of a list

li=[3,2,5,8,6,1,4]
l1=[]
a=0

for i in range(0,len(li)):
    a=a+li[i]
    l1.append(a)
print(li)
print(l1)

output:

[3, 2, 5, 8, 6, 1, 4]
[3, 5, 10, 18, 24, 25, 29]

#14) Python | Multiply all numbers in the list

l1=[2,4,3,6,4,7,9]
a=1
for i in l1:
    a=a*i
    print(a)

output:

2
8
24
144
576
4032
36288

#15) Python program to find second largest number in a list

li=[23,45,32,76,54,92,84]
l1=li.sort()
print(li)
print(li[-2])

output:

[23, 32, 45, 54, 76, 84, 92]
84

#16) Python program to find N largest elements from a list

n=int(input())
li=[23,45,32,76,54,92,84]
l1=li.sort()
print(li)
print(li[-n:])

output:

4
[23, 32, 45, 54, 76, 84, 92]
[54, 76, 84, 92]

#17) Python | Sort the values of first list using second list

li=[23,45,32,76,54,92,84]
l1=[]
for i in range(0,len(li)):
    l1.append(min(li))
    li.remove(min(li))
print(l1)

output:

[23, 32, 45, 54, 76, 84, 92]

#18)  Python program to interchange first and last elements in a list

def interchange_list(list):
    temp=0
    temp=list[0]
    list[0]=list[-1]
    list[-1]=temp
    

list=[12,45,67,89,92]

interchange_list(list)
print(list)

output:

[92, 45, 67, 89, 12]

#19) Python program to swap two elements in a list

def s_list(list,p1,p2):
      list[3],list[4]=list[4],list[3]
        
list=[23,12,32,54,65,76,89]

s_list(list,1,2)
print(list)

output:

[23, 12, 32, 65, 54, 76, 89]






















    








   

