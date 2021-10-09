"""
Pseudocode:

prompt the user for a number

while the number is non-positive:
    read the number

    initialise total variable = 0
    for each number in the range 0 to user number:
        add the number to total

    print the total

    prompt the user for a number

terminate the program
"""

user_num = int(input("Please enter a positive integer (enter a non-positive integer to exit): "))

while user_num > 0:
    print("You entered:", user_num)

    total = 0
    for i in range(user_num + 1):
        total += i

    print("The sum of the integers up to and including", user_num, "is", total)

    user_num = int(input("Please enter a positive integer (enter a non-positive integer to exit): "))#

print("Finished")