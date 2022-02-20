=========================tuples============
#1) Python program to Find the size of a Tuple

tup=(2,5,3,8,6,9,1)
print("size of the tuple is:",len(tup))

#2) Python – Maximum and Minimum K elements in Tuple

print("minimum element of tuple :",min(tup))
print("maximum element of tuple :",max(tup))

output:

size of the tuple is: 7
minimum element of tuple : 1
maximum element of tuple : 9

#3) Python – Adding Tuple to List and vice – versa

tup1=(2,4,7)
li=[6,3]
li+=tup1
print(li)

output:

[6, 3, 2, 4, 7]


#4)Python – Convert Nested Tuple to Custom Key Dictionary

Li1 = (3,4,5,6,9)
Li2 = ("hello","hi","welcome","to","python")

print(dict(zip(Li1,Li2)))

output:

{3: 'hello', 4: 'hi', 5: 'welcome', 6: 'to', 9: 'python'}

#5Python – Flatten tuple of List to tuple

Li1 = (3,4,5,6,9)
Li2 = ("hello","hi","welcome","to","python")

print(list(zip(Li1,Li2)))
output:
[(3, 'hello'), (4, 'hi'), (5, 'welcome'), (6, 'to'), (9, 'python')]



























