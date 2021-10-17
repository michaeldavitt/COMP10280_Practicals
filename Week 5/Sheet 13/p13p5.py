# Taken verbatum from the notes (Lecture 15 page 12)

"""
Pseudo Code:
Define a function f taking a formal parameter x:
    Print "In function x"
    Increment x by 1
    Set y = 1
    Set b = a + 3

    print the values of x, y, z, a and b

    return x

Set 5, 10, 15, 20 and 25 to be the values of x, y, z, a and b respectively

Print "Before funtion f:"
Print the values of x, y, z, a and b

Set z = function call of f with x as the actual argument
Set a = function call of f with y as the actual argument

Print "After function f:"
Print the values of x, y, z, a and b

"""

def f(x):
    """Function that adds 1 to its argument x
    
    Also sets y = 1, b = a + 3 and prints out all values x, y, z, a and b
    """

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