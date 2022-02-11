
#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

d1={}   #empty dict

d2={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

print(d2[3][0][::2])
print(d2[3][2][6:-6:-1])

print(tuple(d2.keys()))


a=print(sum(d2[2]))
b=print(len(d2[2]))



output:


bobtn
arbeg
(1, 2, 3)
60
3
