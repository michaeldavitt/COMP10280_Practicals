"""
Pseudocode:

prompt the user for a number

while user number is not equal to 0:
    read the number

    initialise a cube root variable = 0

    while cube root to the power of 3 is less than the absolute value of the user number:
        increment cube root

    if cube root to the power of 3 is equal to the absolute value of the user number:
        if the number is less than 0:
            multiply the cube root by -1

        print "The cube root of user number is cube root"

    else:
        print "User number is not a perfect cube"

    prompt the user for a number
"""

user_num = int(input("Please enter a number (enter 0 to exit): "))

while user_num != 0:
    print("You entered:", user_num)

    cube_root = 0

    while cube_root ** 3 < abs(user_num):
        cube_root += 1

    if cube_root ** 3 == abs(user_num):
        if user_num < 0:
            cube_root = -cube_root

        print("The cube root of", user_num, "is", cube_root)

    else:
        print(user_num, "is not a perfect cube")

    user_num = int(input("Please enter a number (enter 0 to exit): "))

print("Finished")