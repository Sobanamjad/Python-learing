class Student:
    college_name = "ABC College"
    def __init__(self, fullname, marks):
        self.name = fullname
        self.totalmarks = marks
        print("Adding new student in Database....")

    # Method
    def welcome(self):
        print("Welcome Student", self.name)
    # Method
    def get_marks(self):
        return(self.totalmarks)


s1 = Student("Ahmad", 800)
s1.welcome()
print(s1.get_marks())


# s2 = Student("Ali", 900)
# print(s2.name)
# print(s2.totalmarks)
# # We can save also with Class name
# print(Student.college_name)

