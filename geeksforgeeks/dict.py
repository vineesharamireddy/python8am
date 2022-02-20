================dictionary==============
#1)  Python – Extract Unique values dictionary values

a={'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
print(a.values())
print(a.items())

output:

dict_values([[5, 6, 7, 8], [6, 12, 10, 8], [10, 11, 7, 5], [1, 2, 5]])
dict_items([('gfg', [5, 6, 7, 8]), ('best', [6, 12, 10, 8]), ('is', [10, 11, 7, 5]), ('for', [1, 2, 5])])

#2)Python program to find the sum of all items in a dictionary

d={'a': 100, 'b':200, 'c':300}
a=d.values()
n=0
for i in d.values():
    n=n+i
print(n)

output:

600

#3) #Python | Merging two Dictionaries

d={'a': 100, 'b':200, 'c':300}
a={'d':25, 'e':50}
d.update(a)
print(d)

output:

{'a': 100, 'b': 200, 'c': 300, 'd': 25, 'e': 50}

#4)Python | Ways to remove a key from dictionary

a={3: 'hello', 4: 'hi', 5: 'welcome', 6: 'to', 9: 'python'}
print(a.keys())
a.pop(4)
print(a)

output:

dict_keys([3, 4, 5, 6, 9])
{3: 'hello', 5: 'welcome', 6: 'to', 9: 'python'}

#5)Python – Convert key-values list to flat dictionary

a = {'wk' : [1, 2, 3,4],
             'name' : ['sun', 'mon', 'tues','wedns']}
res = dict(zip(a['wk'], a['name']))
print(res)

output:

{1: 'sun', 2: 'mon', 3: 'tues', 4: 'wedns'}

























