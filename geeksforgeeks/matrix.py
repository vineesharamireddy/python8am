=====================matrices=======================

#1) Python program to add two Matrices
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
c=[[0,0,0],
  [0,0,0],
  [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for r in c:
    print(r)

output:

[2, 4, 6]
[8, 10, 12]
[14, 16, 18]

##2)  Python program to multiply two matrices

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
c=[[0,0,0],
  [0,0,0],
  [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]*b[i][j]
for r in c:
    print(r)

output:

[1, 4, 9]
[16, 25, 36]
[49, 64, 81]

##3) Adding and Subtracting Matrices in Python

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b = [[5,4,3],
    [1 ,7,6],
    [8 ,2,0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]-b[i][j]
for r in c:
    print(r)

output:

[-4, -2, 0]
[3, -2, 0]
[-1, 6, 9]






























    
   
