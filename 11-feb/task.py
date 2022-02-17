#Task1:    Nested DataStructure

Li1 =[2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]

print(Li1[3])                 #5
print(Li1[4][1])               #56
print(Li1[4][4][1])            #222
print(Li1[4][4][3][2][1])      #50000
print(Li1[4][4][3][2][3][3:6])  #put
print(Li1[4][4][3][0])            #5555
print(Li1[4][4][3][4])             #7777
print(Li1[4][4][6])                  #666
print(Li1[4][5])                   #89
print(Li1[4][4][3][2][2][4:])       #on
print(Li1[4][4][2])                #333
print(Li1[4][4][3][1])            #3333

output:

5
56
222
50000
put
5555
7777
666
89
on
333
3333
​


#Task2

a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

print(a[4][3][9:])         #science
print(a[4][3][:8])     #computer

output:

science
Computer



# Task3

a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]

print(a[4][4])       #666
print(a[4][3][0])     #201
print(a[4][1])        #102
print(a[4][3][2][0])     #999
print(a[4][5])           #777

output:

666
201
102
999
777

#Task4:

Li1 = [2,3,"python","hello",4,5,0]  

print(Li1[3][2:4])       #ll
print(Li1[2][2:])       #thon

output:

ll
thon


# Task5

Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

print(Li1[5][0]) #11
print(Li1[5][6])#6666
print(Li1[5][-2])#6666
print(Li1[5][7])#7777
print(Li1[6])#7777
print(Li1[5][5][1])#222
print(Li1[-2][-1])#7777
print(Li1[-2][2:4])#33 44

output:

11
6666
6666
7777
7777
222
7777
[33, 44]
​
#Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

print(a[1][3][0:2])   #py
print(a[2][10][1:])   #ello
print(a[2][40][3:5])    #en
print(a[40][1][0:3])    #zoo
print(a[40][2][0:3])    #Bot
print(a)


output:

py
ello
en
zoo
Bot
{1: [1, 2, 3, 'python'], 2: {10: 'hello', 20: 'welcome', 40: 'science'}, 99: {3, 4, 5, 6}, 40: {1: 'zoology', 2: 'Botany'}}





#Task7:       Covert below two lists in to a dictionary
#[1,2,3,4,5]
#["python","cpp","c","java","php"]
     
li1=[1,2,3,4,5]
li2=["python","cpp","c","java","php"]
print(dict(zip(li1,li2)))

output:

{1: 'python', 2: 'cpp', 3: 'c', 4: 'java', 5: 'php'}


#Task8:     Covert below set in to a list
#{5,4,3,6,2,7,1}

s1={5,4,3,6,2,7,1}
print(list(s1))

output:

[1, 2, 3, 4, 5, 6, 7]

#Task9:    Remove duplicates from below list
#[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]

l1=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(l1)
l2=set(l1)
print(l2)

output:

[5, 4, 3, 6, 2, 7, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 5]
{1, 2, 3, 4, 5, 6, 7}


#Task10:    Convert below one to tuple
#[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]

li1=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(tuple(li1))

output:

(5, 4, 3, 6, 2, 7, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 5)













