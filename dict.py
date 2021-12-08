
dict = {'name': 'Gorret', 'age': 45, "loc": "konge"}

for key, value in dict.items():
    print(key, value)

dict.update({'course': ["Python", "Android", "Web"], 'age': 21})
print(dict)

dict.pop('age')
print(dict)

dict.popitem()
print(dict)

del dict['loc']
print(dict)

