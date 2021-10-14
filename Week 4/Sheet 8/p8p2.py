"""
Pseudocode:

prompt the user to enter a number
read the number

initialise a counter i = 1

while i is less than or equal to the user number:
    initialise a counter j = 1

    while j is less than or equal to the user number:
        print i multiplied by j, then add a tab for neatness
        increment j

    create a new line
    increment i

Terminate the program
"""

user_num = int(input("Please enter a number: "))
print("You entered", user_num)
print("Here is a multiplication table for the number", user_num, "from 1 to", user_num)
print()
print("--------------------------------------")

i = 1

while i <= user_num:
    j = 1

    while j <= user_num:
        print("|", i * j, "\t", end="")
        j += 1

    print()
    print("--------------------------------------")

    i+= 1

print("Finished")