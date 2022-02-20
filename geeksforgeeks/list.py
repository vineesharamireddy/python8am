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

#5,6)Python program to print even numbers and odd numbers in a list

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

#7,8) Python program to print all even numbers and odd numbers in a range

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
        
#10,9) Python program to print positive numbers and negative numbers in a range

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

#12,11) Python program to print positive numbers and negative numbers in a list

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

#13) Remove multiple elements from a list in Python

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

#14) python program to find Cumulative sum of a list

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

#15) Python | Multiply all numbers in the list

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

#16) Python program to find second largest number in a list

li=[23,45,32,76,54,92,84]
l1=li.sort()
print(li)
print(li[-2])

output:

[23, 32, 45, 54, 76, 84, 92]
84

#17) Python program to find N largest elements from a list

n=int(input())
li=[23,45,32,76,54,92,84]
l1=li.sort()
print(li)
print(li[-n:])

output:

4
[23, 32, 45, 54, 76, 84, 92]
[54, 76, 84, 92]

#18) Python | Sort the values of first list using second list

li=[23,45,32,76,54,92,84]
l1=[]
for i in range(0,len(li)):
    l1.append(min(li))
    li.remove(min(li))
print(l1)

output:

[23, 32, 45, 54, 76, 84, 92]

#19)  Python program to interchange first and last elements in a list

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

#20) Python program to swap two elements in a list

def s_list(list,p1,p2):
      list[3],list[4]=list[4],list[3]
        
list=[23,12,32,54,65,76,89]

s_list(list,1,2)
print(list)

output:

[23, 12, 32, 65, 54, 76, 89]
========================================
l1=[3,5,8,4,0,2,5,7]

#21)Python | Ways to find length of list

a=len(l1)
print(a)

output:

8

#22)  Python | Ways to check if element exists in list

print(l1.index(5))

output:

1

#23)Different ways to clear a list in Python

l1.clear()
print(l1)

output:

[]

#24)Python – Remove empty List from List
l2=[2,4,[],6,[],5,9,[],7,4,1,4,6]
print("The original list is : " + str(l2))
res = [ele for ele in l2 if ele != []]
print ("List after empty list removal : " + str(res))

output:

The original list is : [2, 4, [], 6, [], 5, 9, [], 7, 4, 1, 4, 6]
List after empty list removal : [2, 4, 6, 5, 9, 7, 4, 1, 4, 6]


#25)Python | Count occurrences of an element in a list
print(l2.count(4))

output:

3

#26)Python | Cloning or Copying a list

def cpy_list(l1):
    l2=l1.copy()
    return l2
l1=[2,5,3,9,6]
print(cpy_list(l1))

output:

[2,5,3,9,6]

# 27)Python | Remove empty tuples from a list

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

output:

[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]

#28)Python | Program to print duplicates from a list of integers

list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
new = []  
for a in list: 
    n = list.count(a) 
    if n > 1:        
 
        if new.count(a) == 0:  # condition to check
 
            new.append(a)
 
print(new)

output:

[1, 2, 5, 9]

#29)Python | Sum of number digits in List

test_list = [12, 67, 98, 34]
print("The original list is : " + str(test_list))
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
print ("List Integer Summation : " + str(res))

output:

The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]

#30)Break a list into chunks of size N in Python

l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
n = 4
x = [l[i:i + n] for i in range(0, len(l), n)] 
print(x)

output:

[[1, 2, 3, 4], [5, 6, 7, 8], [9]]


















    








   

