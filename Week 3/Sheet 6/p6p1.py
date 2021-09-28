# p6p1 - Program that checks if the sum of 2 numbers > 100

"""
Pseudocode:

Ask user for first number
Read first number
Ask user for second number
Read second number

Get sum of two numbers

If the sum is greater than 100:
    print "This is a big number"

Print "Finished"
"""

num_1 = int(input("Please enter a number: "))
print("You have entered", num_1)
num_2 = int(input("Please enter another number: "))
print("You have entered", num_2)

num_sum = num_1 + num_2

if num_sum > 100:
    print("That is a big number!")

print("Finished")
