#List
#Create an empty list (two ways)

li=[]
print(li)
l=list()
print(l)

output:

[]
[]

#Concatenate with [5,6,7,8]

li1=[5,6,7,8]
li2=li+li1
li3=[8,9,1,5,6,7,8]
print(li2)
print(li3)


output:

[5, 6, 7, 8]
[8, 9, 1, 5, 6, 7, 8]

#add 1 elements to that list

li3.append(1)
print(li3)

output:

[8, 9, 1, 5, 6, 7, 8, 1]

#Find frequency of 8 (count)

print(li3.count(8))
output:

2

#find the mean of the list

print("mean of li1 is",(sum(li3))/len(li3))

output:
mean of li3 is 5.5


#find sum (List) + min + Max 

print(min(li3))
print(sum(li3))
print(max(li3))
print(len(li3))

output:

1
45
9
8



#Find median of the list

li3.sort()
a=int((len(li3)/2))
print(a)
print((li3[a]+li3[a+1])/2)

output:

[9, 1, 4, 8, 8]
2
8.0

#remove duplicates from list and give output in the format of tuple

print(set(tuple(li3)))

output:

{8, 1, 4, 9}
