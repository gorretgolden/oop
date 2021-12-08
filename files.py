f = open("index.py", "r")
# print(f.read(5))
print(f.readline())

for x in f:
    print(x)

f.close()

f = open("lists.py", "a")
f.write("#Now the file has more content!")
f.close()

f = open("lists.py", "r")
print(f.read())

f = open("del.py", "w")
f.write("Woops! I have deleted the content!")
f.close()

x = open('create.py','a')
x.write('#new')
x.write('class Main:def _init(self, name)')

import os
# os.remove("create.py")

if os.path.exists("demofile.txt"):
      os.remove("demofile.txt")
else:
  print("The file does not exist")