"""
Pseudo Code:

Define a recursive function with one formal parameter n:
    if n is equal to 0:
        return 13

    else if n is equal to 1:
        return 8

    else:
        return f(n - 2) plus 13 multiplied by f(n - 1)

Prompt the user for an integer

while the user integer is greater than or equal to 0:
    Read the integer

    for each number i in the range 0 to user integer - 1:
        print the result of the call to the recursive function with argument i + 1

    Prompt the user for an integer

Terminate the program
"""

def last_series_fn(n):
    """Calculates 13 if the argument n = 0, 8 if n = 1 and f(n-2) + 13 * f(n-1) if n > 1
    
    Assumes that the argument n is a non-negative integer
    Uses a recursive definition
    """
    # print("Current number:", n)
    
    if n == 0:
        return 13

    elif n == 1:
        return 8

    else:
        return last_series_fn(n - 2) + 13 * last_series_fn(n - 1)



user_num = int(input("Please enter an integer >= 0 (enter a negative number to exit): "))

while user_num >= 0:
    print("You have entered:", user_num)

    for i in range(user_num):
        print(last_series_fn(i))

    user_num = int(input("Please enter an integer >= 0 (enter a negative number to exit): "))
    
print("Finished!")