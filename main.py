class Students:
    def __init__(self,name,age,dob,id) :
        self.name = name
        self.age = age
        self.dob = dob
        self.id = id
        
    def student(id):
        return f'Student ID: {id}'    
 
           
student_one = Students('Gorret',21,2000,1)  
# student_one.student(1)

print(student_one.name,student_one.age,student_one.id)      


class Defaulters(Students):
    def __init__(self, name, age, dob, id):
        Students.__init__(self, name, age, dob, id)
        super().__init__(name, age, dob, id)  
        self.fees =200
m = Defaulters('gorret',45,2000,3,200)            