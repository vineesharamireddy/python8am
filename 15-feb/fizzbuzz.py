#Task3

#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number


a=int(input("one number from user")) 
if a%3==0: 
    print("fizz") 
elif a%5==0:
    print("buzz")
elif a%3==0 and a%5==0:
    print("fizzbuzz")
else:
    print("invalid number")

output:

one number from user100
buzz



#Task4:   Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark
#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL


a=int(input("enter mark"))
if a>=0 and a<=100:
    print("valid number")
else: 
    print("invalid number")
if a>50 and a<=100:
    print("pass")
else:
    print("fail")
if a>=90 and a<=100:
    print("grade A")
elif a>=80 and a<=89:
    print("grade B")
elif a>=70 and a<=79:
    print("grade C")
elif a>=60 and a<=69:
    print("grade D")
elif a>=50 and a<=59:
    print("grade E")
else:
    print("fail")

output:

enter mark72
valid number
pass
grade C

#Task 5:    collect three marks from user
#calculate mark1 + mark2 + mark3 / 100

#if calculate > 90 ===> Grade A
#if calculate > 75 ==> Grade B
#calculate > 50  ==> grade C
#Other wise ===> Grade D


mark1=int(input("sub1 marks"))
mark2=int(input("sub2 marks"))
mark3=int(input("sub3 marks"))
d=float(mark1+mark2+mark3)/3
print(d)
if d>=70:
 print("first class")
elif d>=50 and d<=70:
 print("second class")
elif d>=35 and d<=50:
 print("third class")
else:
 print("failure")

output:
    
sub1 marks60
sub2 marks60
sub3 marks60
60.0
second class

​
