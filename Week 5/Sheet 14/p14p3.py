# Taken verbatum from the lecture notes (Lecture 13 Slide 16)

"""
Pseudo Code:
Rules: A prime number only divides by itself and 1. 
If it divides by something other than itself and 1, it's not prime.

Prompt the user for a number
Read the user number

For each number in the range 2 to 19:
    For each number "i" in the range 2 to (number - 1):
        If the number divides evenly into something other than itself and 1:
            Print that the number is not prime
            break out of the for loop

    Else (reaching this clause implies that the for loop has run to the end):
        print The number is prime

Terminate the program
"""


# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers
user_num = int(input("Please enter an integer: "))
print("You have entered:", user_num)

for number in range(2, user_num + 1):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            break
    else:
        # loop fell through without finding a factor
        print(number, "is a prime number")

print("Finished!")