"""
Pseudocode:

prompt the user for a number
read user number

if the number is less than 0:
    print "Number should be non-negative

else:
    initialise fact variable = 1
    initialise counter variable = 1

    while counter variable is less than or equal to user number:
        multiply fact by counter

    print the factorial variable

terminate the program
"""

user_num = int(input("Enter the number for which you want to calculate the factorial (an int >= 0): "))
print("You entered:", user_num)

if user_num < 0:
    print("Error: Number entered was less than 0")

else:
    fact = 1
    count = 1

    while count <= user_num:
        fact *= count
        count += 1

    print("Factorial of", user_num, "is", fact)

print("Finished")