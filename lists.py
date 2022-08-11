m = [1, 2, 3, 4, 5, 6, 7, 8]
print(m[:5])

marks = [90, 78, 88, 100, 98]
marks.append(73)
print(marks)

for x in marks:
    print(x)

marks.insert(5, 99)
print(marks)

m.remove(7)
print(m)

m.pop()
print(m)

marks.extend(m)
print(marks)

del m[0]
print(m)

marks[1] = 100

print(marks)
#Now the file has more content!#Now the file has more content!
print(type(m))

#list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#check existance of an item
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#changing values 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  

#add
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#sorting lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sort to lower
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse lists
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#copying lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)