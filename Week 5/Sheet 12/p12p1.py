# Note: The use of the time module is to answer PS14 Q1

"""
Pseudocode:
Factorial Rules: 
Factorial = 1 if N=0 
Factorial = N * Factorial(N-1) if N > 0

Define the function factorial taking one formal parameter x, which is assumed to be non-negative:
    Initialise a factorial variable = 1
    Initialise a position variable = 2

    while position is less than or equal to x (loop will be skipped when x < 2) do the following:
        multiply factorial by position and set this equal to the new value of factorial
        increment position

    return factorial



Prompt the user for an integer
Read the integer

If the user integer is less than 0 then:
    Print an error message

Else:
    Call the factorial function defined above and print the result returned by the function. Actual parameter = user integer.

Terminate the program
"""
import time

def factorial(x):
    """Calculates the factorial of an argument x
    
    The argument x is assumed to be non-negative
    """
    fact = 1
    pos = 2
    while pos <= x:
        fact *= pos
        pos += 1

    return fact


user_num = int(input("Please enter an integer greater than or equal to 0: "))
print("You have entered:", user_num)

if user_num < 0:
    print("Error, the integer must be greater than or equal to 0")

else:
    start_time = time.time()
    print("The factorial of", user_num, "is", factorial(user_num))
    print("Time taken:", time.time() - start_time)

print("Finished!")