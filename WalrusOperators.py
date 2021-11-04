# Walrus operator := allows you to assign values to variables within an expression,
# including variables that do not exist yet

# Let's suppose we want to take an integer from the user, assign it to a variable num and output it,
# then Walrus operator can do this at once
print(num := int(input("Enter a number: ")))
