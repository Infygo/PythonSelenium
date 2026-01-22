# class and object instantions
# objs > no need of new keyword > just instantiate the class
# obj.methodname , obj.variable name
# constructor > no class name , just __init__(self)
# class variables >  variables in a class that doesnt change with object creation
# instance variable > variables that are different for different instances / objects
# use of self keyword in all methods in a class and use of self.variablename to use instance variable in a methods in a class

class Calculator:
    parentclass_num = 100 # class variable
    def __init__(self, a, b):
        print('Default constructor , called automatically when object is created')
        self.a = a # instance variable1 that changes for different objects
        self.b = b # instance variable2

    def getData(self): # use of self keyword parameters are mandatory for methods inside a class
        print("executing a method in a class")

    def sum(self):
        print('Sum of 2 nums:', self.a + self.b)
        return self.a + self.b + self.parentclass_num

obj1 = Calculator(1,2)
obj2 = Calculator(3,4)
print('Returns sum of class + instance variables', obj1.sum()) # 1, 2 gets passed as instance variables
print('Returns sum of class + instance variables', obj2.sum()) # 3, 4 gets passed as instance variables