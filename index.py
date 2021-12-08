class Students:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def name(self):
        print(self.student_name)

    def student(student_id, student_name, student_class):
        return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
    print(student('S122', 'Wilson Medina', 'VI'))


student_two = Students('Q22', 'Joy', 's.2')

print(student_two.student_name)
