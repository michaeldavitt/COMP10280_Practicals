# Modified version of code from the lecture notes (lecture 16 pg 14 - 17)

"""
Pseudo Code:
function findDivisors(num)
    initialise divisors with a tuple containing 1 and num
    for i from 2 to (num/2 + 1) do
        if num1 mod i == 0 then
            add i to divisors
    return divisors

Prompt the user for a positive integer
if the number entered is not positive then
    print out an error message
else
    find the divisors using findDivisors(user_number)
    print out the divisors
"""

# Program to get the common divisors of two positive integers supplied by the user
# Demonstrates the use of tuples
def findDivisors(num):
    """Finds the divisers of a formal parameter num

    Assumes that num is a positive integer
    Returns a tuple containing the divisors of num"""
    divisors = (1, num)
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            divisors += (i,)
    return divisors


number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Number should be > 0.")
else:
    divisors = findDivisors(number)
    print("The divisors of", number, "are", divisors)

print("Finished!")