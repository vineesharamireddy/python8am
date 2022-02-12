#Sets      #Create two empty sets

#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2



s={}
print(s)
s1=set()
print(s1)
s2={7,8,9,1,2,3,4,5,0}
s3={4,5,6,0}
print(s2)
print(s3)
print(s2.issubset(s3))
print(s2.intersection(s3))
s3.discard(0)
s2.discard(0)
print(s2)
s2.remove(8)
print(s2.union(s3))

output:


{}
set()
{0, 1, 2, 3, 4, 5, 7, 8, 9}
{0, 4, 5, 6}
False
{0, 4, 5}
{1, 2, 3, 4, 5, 7, 8, 9}
{1, 2, 3, 4, 5, 6, 7, 9}
