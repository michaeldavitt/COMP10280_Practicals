# Taken verbatum from the notes (Lecture 15 page 12)

# Program to illustrate scoping in Python

"""
Pseudo Code:
Define a function f taking a formal parameter x:
    Print "In function x"
    Increment x by 1
    Set y = 1

    print the values of x, y and z

    return x

Set 5, 10, 15 to be the values of x, y, z respectively

Print "Before funtion f:"
Print the values of x, y and z

Set z = function call of f with x as the actual argument

Print "After function f:"
Print the values of x, y and z

"""

def f(x):
    """Function that adds 1 to its argument and prints it out"""

    print("In function f:")
    x += 1
    y = 1
    b = a + 3

    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("a is", a)
    print("b is", b)

    return x
    
x, y, z, a, b = 5, 10, 15, 20, 25

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)

z = f(x)
a = f(y)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)