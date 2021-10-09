"""
Pseudocode:

prompt the user for a positive integer

while the user number is non-negative:
    read the number

    initialise a counter variable = 1
    initialise a total variable = 1

    while counter is less than or equal to the user number:
        multiply total by counter
        increment counter

    print the total

    prompt the user for a positive integer

terminate the program
"""

user_num = int(input("Please enter a positive integer (enter a negative number to exit): "))

while user_num >= 0:
    print("You entered:", user_num)

    count = 1
    total = 1

    while count <= user_num:
        total *= count
        count += 1

    print("the factorial of", user_num, "is", total)

    user_num = int(input("Please enter a positive integer (enter a negative number to exit): "))

print("Finished")