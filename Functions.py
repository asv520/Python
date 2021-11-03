# A function is of two types:
# a. Built in functions
# b. User defined functions

# To create a user defined function, make use of the 'def' keyword

def add(number1, number2):
    sum = number1 + number2
    return sum

# Inputs are string by default. Explicit conversion needs to be done
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(add(number1, number2))

# White spaces are extremely necessary, so take care of those
