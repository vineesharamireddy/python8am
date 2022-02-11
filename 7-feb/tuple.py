#Tuple    #Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)

tup1=(1,4,5,6,7,8)
tup2=(5,6,7,8,9)
print(tup1)
print(tup2)

output:

(1, 4, 5, 6, 7, 8)
(5, 6, 7, 8, 9)

#Find the common elements between two tuples

#print(tup1.intersection(tup2))


#Concatenate both tuples and remove duplicates from tuple

tup3=tup1+tup2
print(tup3)

output:

(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)


#Find the index value of 9 (after concatenation)

print(tup3.index(9))

output:

10

#multiply above elements 3 times

print(tup3*3)

output:

(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)



