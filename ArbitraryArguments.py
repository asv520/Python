# If you do not know how many arguments that will be passed into your function,
# add a '*' before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly

def my_function(*names):
    print("The name of the protagonist of Splinter Cell: " + names[0])


my_function("Sam Fisher", "Adam Jensen", "Gordon Freeman")
