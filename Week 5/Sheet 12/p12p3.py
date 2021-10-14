"""
Pseudocode:
Define the function approx_sqrt taking the formal parameters x, a non-negative number, and epsilon:
    Initialise a root variable = 0
    Initialise a step variable = epsilon squared
    
    while the absolute value of x minus root squared is less than epsilon and root squared is less than or equal to x:
        Increment root by step

    if the absolute value of x minus root squared is less than epsilon:
        return root
    
    else:
        return "Failed to find a square root"


Prompt the user for a non-negative floating point number
Read the number

if the number is less than 0:
    print an error message

else:
    print "the approximate square root of the user number is approx_sqrt(user number, 0.01)"

Terminate the program
"""

def approx_sqrt(x, epsilon):
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
    print("The approximate square root of", user_num, "is", approx_sqrt(user_num, 0.01))

print("Finished!")