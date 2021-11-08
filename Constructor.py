# __init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor.
# The __init__ method can be called when an object is created from the class, and
# access is required to initialize the attributes of the class.

# Create a class named Person, use the __init__() function to assign values for name. age and position

class Person:
    def __init__(self, name, age, position):
        # self refers to the current instance of the class. It is similar to 'this' keyword in Java
        self.name = name
        self.age = age
        self.position = position


p1 = Person("Gordon Freeman", 27, "Scientist")
print(p1.name+" is "+str(p1.age)+" years old and works as a "+p1.position)
