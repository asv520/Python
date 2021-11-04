# To handle exceptions, and to call code when an exception occurs,
# we can use a try/except statement

try:
    first_number = 5
    second_number = 0
    print(int(first_number//second_number))
except ZeroDivisionError:
    """Here ZeroDivisionError will be caught as it was encountered
    in the code above"""
    print("Division by zero")
finally:
    print("Calculation completed")

"""A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses,
to have the except block handle all of them"""

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Division by zero")
except (ValueError, TypeError):
    print("Error occurred")

"""An except statement without any exception specified will catch all errors.
 These should be used sparingly, as they can catch unexpected errors and hide programming mistakes."""