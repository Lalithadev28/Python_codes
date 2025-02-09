class Calculator:
    def add(self, a, b=0):
        return a + b
 
# Creating an instance of Calculator
calc = Calculator()
 
# Using the add method with one argument
print(calc.add(5))  # Output: 5
 
# Using the add method with two arguments
print(calc.add(5, 3.5))  # Output: 8


class Calculator:
    def add(self, *args):
        return sum(args)
 
calc = Calculator()
 
print(calc.add(1))  # Output: 1
print(calc.add(1, 2))  # Output: 3
print(calc.add(1, 2, 3, 4))  # Output: 10