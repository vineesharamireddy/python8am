#List
#Create an empty list (two ways)

li1=[]
print(li1)
li2=list()
print(li2)

output:

[]
[]

#Concatenate with [5,6,7,8]

li3=[5,6,7,8]
li4=[8,9,1,5,6,7,8]
print(li3)
print(li4)


output:

[5, 6, 7, 8]
[8, 9, 1, 5, 6, 7, 8]

#add 1 elements to that list

li4.append(1)
print(li4)

output:

[8, 9, 1, 5, 6, 7, 8, 1]

#Find frequency of 8 (count)

print(li4.count(1))
output:

2

#find the mean of the list
#find sum (List) + min + Max 

print(min(li4))
print(sum(li4))
print(max(li4))
print(len(li4))

output:

1
45
9
8



#Find median of the list

#remove duplicates from list and give output in the format of tuple


