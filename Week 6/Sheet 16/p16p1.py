"""
Pseudo code:
Rules: f(n) = 2 when n = 1, 2 * f(n-1) when n > 1

define function that takes an argument n and returns 2 if n = 1 and 2 * f(n-1) otherwise:
    if n is equal to 1 then:
        return 2

    else:
        return 2 * f(n-1)

Prompt user for a number x
Read x

while x is greater than or equal to 1:
    for each number i in the range 1 to x:
        call the function above with i as the actual argument

    Prompt the user for a number
Terminate the program
"""

def recursive_fn(n):
    """Function that returns 2 if the formal parameter n == 1, returns 2 * fn(n-1) otherwise
    
    Assumes that the formal parameter n is a positive integer
    """
    print("Current n value:", n)

    if n == 1:
        return 2

    else:
        return 2 * recursive_fn(n - 1)


user_num = int(input("Please enter a positive integer (enter a non-positive integer to exit): "))
print("You have entered:", user_num)

while user_num >= 1:
    for i in range(1, user_num+1):
        print(recursive_fn(i))

    user_num = int(input("Please enter a positive integer (enter a non-positive integer to exit): "))

print("Finished!")
