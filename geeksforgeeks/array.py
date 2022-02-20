===============array===============
#1) Python Program to find sum of array

arr=[2,3,4,5,6,8]
print(sum(arr))

output:

28

#2) Python Program to find largest element in an array

print(max(arr))

output:

8

#3)  Python Program for array rotation

#4Python Program to Split the array and add the first part to the end


def rot_arr(arr,p,n):
    arr[:]=arr[p:n]+arr[0:p]
    return arr
arr=[2,3,4,5,6,8]

print(arr)
print(rot_arr(arr,3,len(arr)))

output:

[2, 3, 4, 5, 6, 8]
[5, 6, 8, 2, 3, 4]

#5) Python Program for Find reminder of array multiplication divided by n

arr=[3,2,5,8,6,1,4]
arr1=[]
a=1
n=4

for i in range(0,len(arr)):
    a=a*arr[i]
    arr1.append(a)
print(arr)
print(arr1)
print(arr1[-1]%n)

output:

[3, 2, 5, 8, 6, 1, 4]
[3, 6, 30, 240, 1440, 1440, 5760]
0





















