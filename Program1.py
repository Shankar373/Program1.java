class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero error"
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
operation = input("Enter operation (ADD, SUBTRACT, MULTIPLY, DIVIDE): ").lower()  
calc = Calculator(a, b)
if operation == 'add':
    print(calc.add())
elif operation == 'subtract':
    print(calc.subtract())
elif operation == 'multiply':
    print(calc.multiply())
elif operation == 'divide':
    print(calc.divide())
else:
    print("Invalid operation")
