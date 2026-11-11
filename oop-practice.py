class Student:

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your Average is", sum/3)

s1 = Student("Ahmad Anwar", [90,87,78])
s1.get_average()