"""
Pseudo Code:
Rules: A prime number only divides by itself and 1. 
If it divides by something other than itself and 1, it's not prime.

Create a variable to check whether the test is passed or not
Initialise this variable = True

Prompt the user for a number
Read the user number

For each number in the range 2 to 19:
    For each number "i" in the range 2 to (number - 1):
        If the number divides evenly into something other than itself and 1:
            The number is not prime
            Print the number and the factor pair
            Set the pass/fail variable to false

    If the pass/fail variable is true:
        Print The number is prime

    Set the pass/fail variable to true

Terminate the program
"""

pass_fail = True

user_num = int(input("Please enter an integer: "))
print("You have entered:", user_num)

for number in range(2, user_num + 1):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            pass_fail = False
    
    if pass_fail:
        print(number, "is a prime number")

    pass_fail = True

print("Finished!")