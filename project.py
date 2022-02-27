
def create_list():
    list1=[]
    no_of_ele=int(input("enter number of elements:"))
    for i in range(0,no_of_ele):
        ele=int(input())
        list1.append(ele)
    print("created list is :",list1)
    return list1
def list_append():
    add_elements=int(input("enter elements to add to list"))
    list1.append(add_elements)
    return list1
def list_pop():
    print("list is: ",list1)
    pop_elements=int(input("enter elements to pop from list"))
    list1.pop(pop_elements)
    return list1
def list_sum():
    print("sum of all elements of list is:",sum(list1))
    return sum(list1)
def list_max():
    print("the maximum number in elements of list is:",max(list1))
    return  max(list1)
def list_min():
    print("the minimum number in elements of list is:",min(list1))
    return min(list1)
def list_len():
    d=len(list1)
    print("the length of the list is:",d)
    return d
def list_mean():
    p=list_sum()
    q=list_len()
    r=p/q
    print("the mean of the list is:",r)
    return r
def set_create():
    set1=set()
    no_of_ele=int(input("enter number of elements:"))
    for i in range(0,no_of_ele):
        ele=int(input())
        set1.add(ele)
    print("created set is :",set1)
    return set1
def set_add():
    add_elements=int(input("enter elements to add to set"))
    set1.add(add_elements)
    return set1
def set_pop():
    pop_elements=int(input("enter elements to pop from set"))
    set1.pop()
    return set1
def set_sum():
    a=sum(set1)
    print("sum of elements is:",a)
    return a
def set_max():
    b=max(set1)
    print("maximun element in set is:",b)
    return b
def set_min():
    c=min(set1)
    print("minimum elemet in set is:",c)
    return c
def set_intersection():
    set7=set1.intersection(s)
    print("intersection set is:",set7)
    return set7
def set_union():
    set8=set1.union(s)
    print("union of two sets is:",set8)
    return set8
def tup_create():
    tup1=tuple()
    no_of_ele=int(input("enter number of elements:"))
    for i in range(0,no_of_ele):
        num_ele=int(input())
        print("created tuple is :",tup1)
    return tup1
def tup_add():
    add_elements=int(input("enter elements to add to tuple"))
    tup1=(add_elements,)
    return tup1
def tup_multiplication():
    a=int(input("number"))
    tup2=tup1*a
    print("multiplication is:",tup2)
    return tup2
def tup_sum():
    tup3=sum(tup1)
    print("sum of tuple is:",tup3)
    return tup3
def tup_max():
    tup4=max(tup1)
    print("maximum number in tuple is:",tup4)
    return tup4
def tup_min():
    tup5=min(tup1)
    print("minimum number in tuple is:", tup5)
    return tup5
def tup_count():
    a=int(input())
    b=tup1(count(a))
    print("count of tuple is:",b)
    return b
def tup_length():
    tup7=len(tup1)
    print("length of tuple is:",tup7)
    return tup7
def dict_create():
    dict1={}
    no=input("Enter the number of elements:")
    for i in range(int(no)):
        keys=int(input("enter the key value:"))
        value=(input("enter the value:"))
        dict1[keys]=value
    print("dictionary is:",dict1)
    return dict1
def dict_add():
    keys=int(input("enter the key value:"))
    value=(input("enter the value:"))
    dict1[keys]=value
    print("ater adding doctionary is:",dict1)
    return dict1
def dict_pop():
    keys=int(input("enter the key value:"))
    dict1.pop(keys)
    print("after delete dictionary is:",dict1)
    return dict1
def dict_update():
    dict3=dict_create()
    dict1.update(dict3)
    print("updates dictionary is:",dict1)
    return dict1
def dict_max():
    dict4=max(dict1)
    print("max",dict4)
    return dict4
def dict_min():
    dict5=min(dict1)
    print("min",dict5)
    return dict5

    
    
    
while True:
    user_selection=int(input("user selecting one data structure ::: 1.list 2.set 3.tuple 4.dictionary 5.exit::: "))
    if user_selection==1:
        print("selected data structure is list")
        list1=create_list()
        while True:
            print("1.append","\n2.pop","\n3.sum","\n4.max","\n5.min","\n6.len", "\n7.mean","\n8.exit")
            list_opr=int(input("user selected option in lists is:"))
            if list_opr==1:
                list1=list_append()
                print("list after adding elements is:",list1)
            elif list_opr==2:
                list1=list_pop()
                print("list after poping elements is:",list1)
            elif list_opr==3:
                list3=list_sum()
            elif list_opr==4:
                list4=list_max()
            elif list_opr==5:
                list5=list_min()
            elif list_opr==6:
                list6=list_len()
            elif list_opr==7:
                list7=list_mean()
            elif list_opr==8:
                break
    elif user_selection==2:
        print("user selected data structure is set:")
        s=set_create()
        set1=set_create()
        while True:
            print("1.add","\n2.pop","\n3.sum","\n4.max","\n5.min","\n6.intersection","\n7.union","\n8.exit")
            set_opr=int(input("user selected option in set is:"))
            if set_opr==1:
                set2=set_add()
                print("set after adding ele:",set2)
            elif set_opr==2:
                set3=set_pop()
                print("set after poping element is:",set3)
            elif set_opr==3:
                set4=set_sum()
            elif set_opr==4:
                set5=set_max()
            elif set_opr==5:
                set6=set_min()
            elif set_opr==6:
                set7=set_intersection()
            elif set_opr==7:
                set8=set_union()
            elif set_opr==8:
                break
    elif user_selection==3:
        print("user selected data structure is tuple:")
        tup1=tup_create()
        while True:
            print("1.add","\n2.multiplcation","\n3.sum","\n4.max","\n5.min","\n6.count","\n7.length","\n8.exit")
            tup_opr=int(input("user selected option in tuple is:"))
            if tup_opr==1:
                tup2=tup_add()
                print("tuple after adding ele:",tup2)
            elif tup_opr==2:
                tup3=tup_multiplication()
                print("tuple after deleting ele",tup3)
            elif tup_opr==3:
                tup3=tup_sum()
            elif tup_opr==4:
                tup4=tup_max()
            elif tup_opr==5:
                tup5=tup_min()
            elif tup_opr==6:
                tup6=tup_count()
            elif tup_opr==7:
                tup7=tup_length()
            elif tup_opr==8:
                break
    elif user_selection==4:
        print("user selected data structure is dictionaries:")
        dict1=dict_create()
        while True:
            print("1.add","\n2.pop","\n3.update","\n4.max","\n5.min","\n6.exit")
            dict_opr=int(input("user selected option is dictionaries:"))
            if dict_opr==1:
                dict_add()
            elif dict_opr==2:
                dict_pop()
            elif dict_opr==3:
                dict_update()
            elif dict_opr==4:
                dict_max()
            elif dict_opr==5:
                dict_min()
            elif dict_opr==6:
                break
    elif user_selection==5:
        break

    
    
