class Student():

    def __init__(self, name):
        self.name = name
s1 = Student("Ali")
print(s1.name)

del(s1.name)
# print(s1.name)


class Account():
    
    def __init__(self, acc_num, acc_pass):
        self.acc_num = acc_num
        # Private object access in class not in out of class ( and __ can make attribute private)
        self.__acc_pass = acc_pass

    def reset_password(self):
        print(self.__acc_pass)

acc1 = Account("12345", "pass123")

print(acc1.acc_num)
print(acc1.reset_password())

        
