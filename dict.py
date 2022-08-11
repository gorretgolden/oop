
dict = {'name': 'Gorret', 'age': 45, "loc": "konge"}

for key, value in dict.items():
    print(key, value)

dict.update({'course': ["Python", "Android", "Web"], 'age': 21})
print(dict)

dict.pop('age') #  method removes the item with the specified key name:
print(dict)

dict.popitem() #method removes the last inserted item
print(dict)

del dict['loc'] #del keyword removes the item with the specified key name:
print(dict)

#The clear() method empties the dictionary:
