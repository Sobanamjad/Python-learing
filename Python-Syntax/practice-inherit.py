class Student():
    
    def __init__( self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem
        # self.percentage = str(( phy + math + chem) / 3) + "%"
    
    # Property Decorators
    @property
    def calcPercentage(self):
        return str(( self.phy + self.math + self.chem) / 3) + "%"

s1 = Student(87,90,88)
print(s1.calcPercentage)

# after change numebr 
s1.phy = 95
print(s1.phy)
print(s1.calcPercentage)
