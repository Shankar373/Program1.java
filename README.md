# Tandemloop Programming Test

This repository contains solutions for a programming test, including a calculator program, series generator programs, and a multiple counter program. Each program is designed to demonstrate fundamental programming skills in Python and Java.

## Table of Contents

- [Overview](#overview)
- [Programs](#programs)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of this project is to showcase the implementation of basic algorithms and operations using different programming languages. The following functionalities are provided:

1. A calculator that performs basic arithmetic operations.
2. A program to generate an odd number series based on user input.
3. A modified program to generate a limited odd number series based on user input.
4. A function that counts the multiples of numbers from 1 to 9 in a user-provided list of integers.

## Programs

### Program 1: Calculator (Python)

This program performs addition, subtraction, multiplication, and division operations.

**File**: `program1.py`

```python
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
