# Note: The use of the time module is to answer PS14 Q1

"""
Pseudo Code:
Define factorial function taking one formal parameter x, assumed to be a non-negative integer:

    print "Current value of x:" followed by the current value of x

    if x = 0 then:
        return 1

    else:
        return x multiplied by the result of the function call of the factorial function with actual argument = x - 1
        for a value N > 1, this will result in N times fact(N-1), which will be N times (N-1) times fact(N-2) etc until we reach N = 0 (satisfying the recursive definition of a factorial)
        

Prompt the user for an integer
Read the integer

if user number is less than 0 then:
    print an error message

else:
    call the function factorial with actual argument = user number and print the result

Terminate the program
"""


import time

def factorial(x):
    """Function that returns the factorial of its argument
    
    Assumes that its argument is a non-negative integer
    Uses a recursive definition
    """

    print("Current value of x:", x)

    if x == 0:
        return 1

    else:
        return x * factorial(x-1)


user_num = int(input("Please enter an integer greater than or equal to 0: "))
print("You have entered:", user_num)

if user_num < 0:
    print("Error: number must be greater than or equal to 0")

else:
    start_time = time.time()
    print("Factorial of", user_num, "is", factorial(user_num))
    print("Time taken:", time.time() - start_time)

print("Finished")