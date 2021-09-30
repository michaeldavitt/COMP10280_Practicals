# p6p1 - Program that checks if the sum of 2 numbers > 100

"""
Pseudocode:

Prompt user for first number
Read first number
Prompt user for second number
Read second number

Sum the two numbers

If the sum is greater than 100:
    print "This is a big number"

Print "Finished"
"""

num_1 = float(input("Please enter a number: "))
print("You have entered", num_1)

num_2 = float(input("Please enter another number: "))
print("You have entered", num_2)

num_sum = num_1 + num_2

if num_sum > 100:
    print("That is a big number!")

print("Finished")
