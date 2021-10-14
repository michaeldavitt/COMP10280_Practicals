"""
Pseudocode:
Factorial Rules: Factorial = 1 if N=0, Factorial = N * Factorial(N-1) if N > 0

Define the function factorial taking one formal parameter x, which is assumed to be non-negative:
    Initialise factorial = 1
    If x = 0 or X = 1 then:
        return factorial
    Else:
        initialise a position variable = 2
        while position is less than or equal to x:
            multiply factorial by position and set this equal to the new value of factorial
            increment position

        return factorial



Prompt the user for an integer
Read the integer

If the user integer is less than 0 then:
    print an error message
Else:
    Call the factorial function defined above and print the result returned by the function. Use the user number as the actual argument for the factorial function

Terminate the program
"""
import time

def factorial(x):
    fact = 1
    if (x==0) or (x==1):
        return fact

    else:
        pos = 2
        while pos <= x:
            fact *= pos
            pos += 1

        return fact


user_num = int(input("Please enter an integer greater than or equal to 0: "))
print("You have entered:", user_num)

if user_num < 0:
    print("Error, number must be greater than or equal to 0")

else:
    start_time = time.time()
    print("The factorial of", user_num, "is", factorial(user_num))
    print("Time taken:", time.time() - start_time)

print("Finished!")