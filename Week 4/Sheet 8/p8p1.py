"""
Pseudocode:
Prompt user for a number

while the number is non-negative:
    Read number
    
    If the number is divisible by 2, 3, 5 or 7:
        if number is divisible by 2:
            print("number is divisible by 2)

        do the same test for 3, 5 and 7

    else:
        print "the number is not divisible by 2, 3, 5 or 7

    prompt the user for a number

Terminate the program
"""

user_num = int(input("Please enter a number (enter a negative number to exit): "))

while user_num >= 0:
    print("You entered:", user_num)

    if (user_num % 2 == 0) or (user_num % 3 == 0) or (user_num % 5 == 0) or (user_num % 7 == 0):
        if user_num % 2 == 0:
            print(user_num, "is divisible by 2")

        if user_num % 3 == 0:
            print(user_num, "is divisible by 3")

        if user_num % 5 == 0:
            print(user_num, "is divisible by 5")

        if user_num % 7 == 0:
            print(user_num, "is divisible by 7")

    else:
        print(user_num, "is not divisible by 2, 3, 5 or 7")

    user_num = int(input("Please enter a number (enter a negative number to exit): "))

print("Finished")