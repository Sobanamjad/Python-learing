class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    # This is abstraction means (Unnecessary Things)
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Start....")
c1 = Car()
c1.start()

# Bank Application
class Account:

    def __init__(self, bal, accno):
        self.balance = bal
        self.account_no = accno

    # Debited
    def debite(self, amount):
        self.balance -= amount
        print("Rs", amount, "is debited")
        print("Total Balance:", self.get_balance())

    # Credited
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited")
        print("Total Balance:", self.get_balance())

    # Balance
    def get_balance(self):
       return self.balance

acc1 = Account(10000, 12345)
acc1.debite(9000)
acc1.credit(5000)
        