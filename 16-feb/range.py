#Task1:      Using Range function  print multiples of 5 from 0 to 75
#Using Range function  print multiples of 8 from 0 to 72

#Using Range function  print multiples of 5 from 75 to 0
#Using Range function  print multiples of 8 from 96 to 72



for i in range(0,75):
    if i % 5 == 0:
        print(f'{i}: multiple of 5')
        
for i in range(0,72):
    if i%8==0:
        print(f'{i}: multiple of 8')
for i in range(75,0,-1):
    if i %5==0:
        print(f'{i}: multiple of 5')
for i in range(96,72,-1):
    if i %8==0:
        print(f'{i}: multiple of 8')

output:

0: multiple of 5
5: multiple of 5
10: multiple of 5
15: multiple of 5
20: multiple of 5
25: multiple of 5
30: multiple of 5
35: multiple of 5
40: multiple of 5
45: multiple of 5
50: multiple of 5
55: multiple of 5
60: multiple of 5
65: multiple of 5
70: multiple of 5
0: multiple of 8
8: multiple of 8
16: multiple of 8
24: multiple of 8
32: multiple of 8
40: multiple of 8
48: multiple of 8
56: multiple of 8
64: multiple of 8
75: multiple of 5
70: multiple of 5
65: multiple of 5
60: multiple of 5
55: multiple of 5
50: multiple of 5
45: multiple of 5
40: multiple of 5
35: multiple of 5
30: multiple of 5
25: multiple of 5
20: multiple of 5
15: multiple of 5
10: multiple of 5
5: multiple of 5
96: multiple of 8
88: multiple of 8
80: multiple of 8

#Task2:   Get a dynamic list from user
n=int(input("enter number"))
print(n)
li=[]
for i in range(n):
    if i<n:
        li.append(input(li))
print(li)

output:

enter number5
5
[]3
['3']6
['3', '6']8
['3', '6', '8']0
['3', '6', '8', '0']1
['3', '6', '8', '0', '1']




#Task4:Get two integers from user  & print multiples of 8 between them
a=int(input())
b=int(input())
for i in range(a,b):
    if i %8==0:
        print(f'{i}: multiple of 8')


output:

    10
100
16: multiple of 8
24: multiple of 8
32: multiple of 8
40: multiple of 8
48: multiple of 8
56: multiple of 8
64: multiple of 8
72: multiple of 8
80: multiple of 8
88: multiple of 8
96: multiple of 8


#Task5:    Input:Li1 = [3,4,5,2,7,8,9,10]
# Output:   Li_odd = [3,5,7,9]     Li_even = [4,2,8,10]

Li1 = [3,4,5,2,7,8,9,10]
Li2=[]
Li3=[]
for i in Li1:
     if i %2==0:
        Li2.append(i)
     else:
        Li3.append(i)
print("even numbers: ",Li2)
print("odd numbers:",Li3)

output:

even numbers:  [4, 2, 8, 10]
odd numbers: [3, 5, 7, 9]

#Task6: Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
#Output:  neg_LI = [-1,-7,-3]   pos_LI = []   Zeros = []
#Numeber of postivie ele: 7
#Number nega: 3
#Number of zeros: 2

l1=[-1, -7,8,10,20,21,17,28,-3,0,0,]
l2=[]
l3=[]
l4=[]
for i in l1:
    if i>0:
        l2.append(i)
    elif i<0:
        l3.append(i)
    else:
        l4.append(i)
print("number of positive values are :",len(l2),"those are: ",l2)
print("number of negative values are :",len(l3),"those are:l",l3)
print("number of zeros are:",len(l4), "those are :", l4)

output:

number of positive values are : 6 those are:  [8, 10, 20, 21, 17, 28]
number of negative values are : 3 those are: [-1, -7, -3]
number of zeros are: 2 those are : [0, 0]
  
#Task7:  Study range function and for loop properly


print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))

output:

[0, 1, 2, 3, 4]
[1, 2, 3, 4]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[-5, -2, 1, 4]
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[10, 8, 6, 4, 2]







