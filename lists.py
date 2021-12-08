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