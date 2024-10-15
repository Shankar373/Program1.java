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
```

### Program 2: Odd Number Series Generator (Java)
This program generates a series of odd numbers based on user input.

**File**: `program2.java`


```java
import java.util.Scanner;

public class Program2 {
    public static void generateOddSeries(int a) {
        for (int i = 0; i < a; i++) {
            System.out.print((2 * i + 1) + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer:");
        int a = sc.nextInt();
        generateOddSeries(a);
    }
}

```

### Program 3: Modified Odd Number Series Generator (Java)
This program generates a modified series of odd numbers based on user input.


**File**: `program3.java`

```java
import java.util.Scanner;

public class Program3 {
    public static void generateModifiedOddSeries(int a) {
        for (int i = 0; i < (a + 1) / 2; i++) {
            System.out.print((2 * i + 1) + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer:");
        int a = sc.nextInt();
        generateModifiedOddSeries(a);
    }
}
```
### Program 4: Count Multiples (Python)
This program counts how many numbers in the input list are multiples of each number from 1 to 9.

**File**: `program4.py`

```python

def count_multiples(arr):
    multiples_count = {i: 0 for i in range(1, 10)}
    for num in arr:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    return multiples_count

user_input = input("Enter numbers separated by commas: ")
arr = [int(num.strip()) for num in user_input.split(',')]
result = count_multiples(arr)
print(result)
```

## Usage

Clone this repository:


```
git clone https://github.com/Shankar373/Tandemloop.git
```

Navigate to the project directory:

cd ```Tandemloop```

# Run the desired program:


For Python programs, use:
```
python program1.py
python program4.py
```
For Java programs, compile and run:
```
javac Program2.java
java Program2
```

```
javac Program3.java
java Program3
```
## Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Instructions to Use:
- Replace `Shankar373` with your actual GitHub username in the clone command.
- Feel free to modify any sections as needed to better suit your project specifics or add any other relevant information. 
- Ensure you create a `LICENSE` file if you include the licensing section. You can choose an appro
