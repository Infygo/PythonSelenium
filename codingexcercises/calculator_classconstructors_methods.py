class BasicCalculator:
    # constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # addition method
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


obj = BasicCalculator(10, 5)
print('Addition:' , obj.add())
print('Subtraction:' , obj.sub())
print('Multiplication:' , obj.mult())
print('Division:', obj.div())