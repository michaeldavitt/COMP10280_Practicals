"""
Pseudocode:
Define the function approx_sqrt taking the formal parameters x (a non-negative number) and epsilon:
    Initialise a root variable = 0
    Initialise a step variable = epsilon squared
    
    while the absolute value of x minus root squared is less than epsilon and root squared is less than or equal to x do the following:
        Increment root by step

    if the absolute value of x minus root squared is less than epsilon then:
        return root
    
    else:
        return "Failed to find a square root"


Prompt the user for a non-negative floating point number
Read the number

if the number is less than 0 then:
    print an error message

else:
    print the result of the approx_square function. Actual arguments: x = user floating point and epsilon = 0.01

Terminate the program
"""

def approx_sqrt(x, epsilon):
    """Calculates the approximate square root of the argument x using a tolerance of epsilon
    
    The difference between x and root squared must be less than epsilon in order for root to be considered an approximate square root
    Assumes that the argument x is non-negative
    Uses exhaustive enumeration
    """
    root = 0
    step = epsilon ** 2

    while abs(x - root ** 2) >= epsilon and root ** 2 <= x:
        root += step

    if abs(x - root ** 2) < epsilon:
        return root

    else:
        return "Failed to find a square root"


user_num = float(input("Please enter a floating point number greater than or equal to 0: "))
print("You have entered:", user_num)

if user_num < 0:
    print("Error: The number must be greater than or equal to 0")

else:
    print("The approximate square root of", user_num, "is:", approx_sqrt(user_num, 0.01))

print("Finished!")