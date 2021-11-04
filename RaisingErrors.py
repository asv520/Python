# raise keyword can be used to raise any error

"""num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("Negative number!")"""

# raise can also be used within except block to re-raise an error

try:
    result = 5/0
    print(result)
except ZeroDivisionError:
    print("An error occurred!")
    raise
