# Taken verbatum from the notes (Lecture 15 page 12)

"""
Pseudo Code:
Define a function f taking a formal parameter x:
    Print "In function f:"
    Increment x by 1
    Set y = 1

    print the values of x, y and z

    return the value x

Set 5, 10, 15 to be the values of x, y, z respectively

Print "Before funtion f:"
Print the values of x, y and z

Set z = function call of f with x as the actual argument

Print "After function f:"
Print the values of x, y and z

"""

def f(x):
    """Function that adds 1 to its argument, sets y = 1 and prints out all values x, y and z"""

    print("In function f:")
    x += 1
    y = 1

    print("x is", x)
    print("y is", y)
    print("z is", z)

    return x
    
x, y, z = 5, 10, 15

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

z = f(x)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)