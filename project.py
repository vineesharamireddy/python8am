import random
l2=["list","set"]
print("welcome to data structure calculater")
print("selecting one data structure randomly ")
a=random.choice(l2)
li=[2,4,6,8,6,3]
s1={3,4,5,6,7,8}
if a=="list":
    print("entering into list options")
    print("1.append","\n2.pop","\n3.update","\n4.sum","\n5.min","\n6.max","\n7.concatenation","\n8.length", "\n9.mean","\n10.median","\n11.find","\n12.frequency","\n13.insertion","\n14.remove","\n15.count")
    b=(input())
    if b=="1.append":
        li.append(1)
        print("after append list is:",li)
    elif b=="2.pop":
        li.pop()
        print("after pop list is:",li)
    elif b=="3.update":
        li.update()
        print("after update list is:",li)
    elif b=="4.sum":
        print(sum(li))
    elif b=="5.min":
        print(min(li))
    elif b=="6.max":
        print(max(li))
    elif b=="7.concatenation":
        li1=[5,6,7,8]
        li2=li+li1
        li3=[8,9,1,5,6,7,8]
        print("list after concatenation is:",li3)
    elif b=="8.length":
        print(len(li))
    elif b=="9.mean":
        print("mean of li1 is",(sum(li))/len(li))
    elif b=="10.median":
        li.sort()
        a=int((len(li)/2))
        print(a)
        print((li[a]+li[a+1])/2)
        print(set(tuple(li)))
    elif b=="13.insertion":
        Li1 = [3,4,5,6,"hello"]
        Li1.insert(3,1000) #(index, value)
        print(Li1)
    elif b=="14.remove":
        Li1.remove(8) #particular element
        print(Li1)
    elif b=="15.count":
        print(Li1.count(3))
    else:
        print("no option available")
s={3,4,5,6,7,8}
s2={12,34,56,78,90}
tup1 = (4,5,6,3,2,1,9,7,2)
if a=="set":
    print("entering into set option:")
    print("1.add","\n2.clear","\n3.copy","\n4.difference","\n5.discard","\n6.intersection","\n7.union","\n8.isdisjoint","\n9.issuperset","\n10.issubset","\n11.pop","\n12.min","\n13.max","\n14.sum","\n15.update")
    s1=(input())
    if s1=="1.add":
        s.add(2)
        print("set after adding ele:",s)
    elif s1=="2.clear":
        s.clear()
        print("set after clear:",s)
    elif s1=="3.copy":
        s2=s.copy()
        print("set after copy:",s2)
    elif s1=="4.difference":
        s3=s2.difference(s)
        print("diff of s1 and s is:",s3)
    elif s1=="5.discard":
        s.discard(6)
        print("set after discard:",s)
    elif s1=="6.intersection":
        s3=s2.intersecton(s)
        print("set after intersection:",s3)
    elif s1=="7.union":
        s3=s2.union(s)
        print("set after uion")
    elif s1=="8.isdisjoint":
        print(s2.isdisjoint(s)) 
    elif s=="9.issuperset":
        print(s2.issuperset(s))
    elif s1=="10.issubset":
        print(s2.issubset(s))
    elif s1=="11.pop":
        s2.pop()
        print("set after pop:",s2)
    elif s1=="12.min":
        print(min(s2))
    elif s1=="13.max":
        print(max(s2))
    elif s1=="14.sum":
        print(sum(s2))
    elif s1=="15.update":
        s2=update(s)
        print("set after update:",s2)
    else:
        print("invalid input")
elif a=="tuple":
    print("entering into tuple options:")
    print("1.index","\n2.count","\n3.min","\n4.max","\n5.sum","\n6.len","\n7.multiplication","\n8.add")
    t=(input())
    if t=="1.index":
        t1=tup1.index(4)
        print("index of tuple is",t1)
    elif t=="2.count":
        t2=tup1.count(2)
        print("cout of tuple:",t2)
    elif t=="3.min":
        print(min(tup1))
    elif t=="4.max":
        print(max(tup1))
    elif t=="5.sum":
        print(sum(tup1))
    elif t=="6.len":
        print(len(tup1))
    elif t=="7.multiplication":
        print(tup1*3)
    elif t=="8.add":
        print(tup1(27))
    else:
        print("invalid input")
