"""
Pseudo Code:

Define a function to evaluate the nth term in a Fibonacci sequence, taking one formal parameter n:
    if n is equal to 1 then:
        return 0

    else if n is equal to 2 then:  
        return 1

    else:
        return f(n - 1) + f(n - 2)

Prompt the user for an integer


While the user integer is greater than or equal to 1:
    Read the user integer

    for each number i in the range 0 to the user number - 1:
        print out the result of the fibonacci function with actual argument = (i + 1)

    Prompt the user for another integer
    
Terminate the program
"""

def fibonacci(n):
    """Function that returns the nth term in the fibonacci sequence
    
    Assumes that the argument n is positive
    """
    print("Current number:", n)
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

user_num = int(input("Please enter an integer >= 1 (enter a non-positive integer to exit): "))

while user_num >= 1:
    print("You have entered:", user_num)

    for i in range(user_num):
        print(fibonacci(i + 1))

    user_num = int(input("Please enter an integer >= 1 (enter a non-positive integer to exit): "))

print("Finished!")