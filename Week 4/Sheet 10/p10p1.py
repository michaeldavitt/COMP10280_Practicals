"""
Pseudocode:

prompt the user for a number

while the user number is non-negative:
    read the number

    initialise a square root variable = 0

    while the square root variable to the power of two is less than the user number:
        increment square root variable

    if the square root variable to the power of two is equal to the user number:
        print "The square root of user number is square root number"

    else:
        print "user number is not a perfect square"

    prompt the user for a number

terminate the program
"""

user_num = int(input("Please enter an integer (enter a negative number to exit): "))

while user_num >= 0:
    print("You entered:", user_num)
    sq_root = 0

    while sq_root ** 2 < user_num:
        sq_root += 1

    if sq_root ** 2 == user_num:
        print("The square root of", user_num, "is", sq_root)

    else:
        print(user_num, "is not a perfect square")

    user_num = int(input("Please enter an integer (enter a negative number to exit): "))

print("Finished")