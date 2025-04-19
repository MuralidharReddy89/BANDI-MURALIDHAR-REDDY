class Calculator:
    def __init__(self,a,b,operation): 
        self.a=float(a)
        self.b=float(b)
        self.operation=operation.lower()


    def calculate(self):
        if self.operation == 'addition':
            # Return the sum of a and b
            return self.a + self.b
        elif self.operation == 'subtraction':
            # Return the difference of a and b
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero!"
        else:
            return "Invalid operation!"

a=input()

b=input()
operation=input()
cal =Calculator(a,b,operation) 
print(cal.calculate())

