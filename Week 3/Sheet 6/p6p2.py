# p6p2 - Program gets the largest odd number of a group of 3

"""
Pseudocode:

Prompt user for the first number
Prompt user for the second number
Prompt user for the third number

If all numbers are even:
    print "None of these numbers are odd"

Else:
    create a variable that keeps track of the largest odd number
    set this variable to 0

    if the first number is odd:
        largest odd number variable becomes the first number
    
    if the second number is odd and bigger than the largest odd number variable value:
        largest odd number variable becomes the second number

    if the third number is odd and bigger than the largest odd number variable value:
        largest odd number variable becomes the third number
    
    print the largest number variable


"""

num_1 = int(input("Please type an integer: "))
num_2 = int(input("Please type an integer: "))
num_3 = int(input("Please type an integer: "))

if num_1 % 2 == 0 and num_2 % 2 == 0 and num_3 % 2 == 0:
    print("None of the three numbers are odd")

else:
    max_odd = 0

    if num_1 % 2 != 0:
        max_odd = num_1

    if num_2 % 2 != 0 and (num_2 > max_odd or max_odd == 0):
        max_odd = num_2

    if num_3 % 2 != 0 and (num_3 > max_odd or max_odd == 0):
        max_odd = num_3

    print(max_odd, "is the largest odd number")

print("Finished")