class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.totalmarks = marks
        print("Adding new student in Database....")
s1 = Student("Ahmad", 800)
print(s1.name)
print(s1.totalmarks)

s2 = Student("Ali", 900)
print(s2.name)
print(s2.totalmarks)
