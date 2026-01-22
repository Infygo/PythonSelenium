# Inheritance
# Inheriting parent class methods from child class
# child inheriting from parent class > use of parent class in brackets in child class
# always invoke parent class default constructor in the child class constructor # Call to __init__ of super class is missed
from pythonbasics.pyoops import Calculator


class ChildImpl(Calculator):
    childclass_num = 200
    def __init__(self): # need to access parent class instance variables / access parent class constructor
        # Call to __init__ of super class is missed > gives a warning already in the constructor of child class
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.childclass_num + self.parentclass_num + self.sum()

childObject = ChildImpl()
print(childObject.getCompleteData())