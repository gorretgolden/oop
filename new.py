thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key,value in thisdict.items():
  print(key,value)


thisdict.update({"qty":200})
print(thisdict)

thisdict.pop('model')
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["year"]
print(thisdict)