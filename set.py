s1={}
print(s1)
s2=set()
print(s2)
s3={1,2,3,5,7,9,8,0}
s3.add(24)
s2.add(4)
s2.add(5)
s2.add(6)
s2.add(2)
s2.add(3)
print(s2)
print(s3)
print(s2.issubset(s3))
print(s2.isdisjoint(s3))
print(s2.intersection(s3))
print(s2)
s2.discard(5)
print(s2)
print(s2.union(s3))



output:

{}
set()
{2, 3, 4, 5, 6}
{0, 1, 2, 3, 5, 7, 8, 9, 24}
False
False
{2, 3, 5}
{2, 3, 4, 5, 6}
{2, 3, 4, 6}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 24}    
