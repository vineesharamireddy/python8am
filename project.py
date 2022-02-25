print("welcome to data structure calculater")
def create_list():
    list1=[]
    no_of_ele=int(input("enter number of elements:"))
    for i in range(0,no_of_ele):
        ele=int(input())
        list1.append(ele)
    print("created list is :",list1)
    return list1
def list_append(list2):
    add_elements=int(input("enter elements to add to list"))
    list1.append(add_elements)
    return list1
def list_pop(list2):
    print("list is: ",list2)
    pop_elements=int(input("enter elements to pop from list"))
    list1.pop(pop_elements)
    return list1
def list_sum(list3):
    print("sum of all elements of list is:",sum(list1))
    return sum(list1)
def list_max(list4):
    print("the maximum number in elements of list is:",max(list1))
    return  max(list1)
def list_min(list5):
    print("the minimum number in elements of list is:",min(list1))
    return min(list1)
def list_len(list6):
    d=len(list1)
    print("the length of the list is:",d)
    return d
def list_mean(list7):
    p=list_sum(list1)
    q=list_len(list1)
    r=p/q
    print("the mean of the list is:",r)
    return r


user_selection=int(input("user selecting one data structure ::: 1.list 2.tuple 3.set 4.dictionary ::: "))
if user_selection==1:
    print("selected data structure is list")
    list1=create_list()
    while True:
        print("1.append","\n2.pop","\n3.sum","\n4.max","\n5.min","\n6.len", "\n7.mean","\n8.exit")
        list_opr=int(input("user selected option in lists is:"))
        if list_opr==1:
            list1=list_append(list1)
            print("list after adding elements is:",list1)
        elif list_opr==2:
            list1=list_pop(list1)
            print("list after poping elements is:",list1)
        elif list_opr==3:
            list3=list_sum(list1)
        elif list_opr==4:
            list4=list_max(list1)
        elif list_opr==5:
            list5=list_min(list1)
        elif list_opr==6:
            list6=list_len(list1)
        elif list_opr==7:
            list7=list_mean(list1)
        elif list_opr==8:
            break
        
