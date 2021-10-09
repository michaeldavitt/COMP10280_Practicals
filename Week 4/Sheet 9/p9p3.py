"""
Pseudocode:

prompt user for a positive integer
read the number

initialise a total variable = 1

for each number in the range 1 to user number:
    multiply the current total by the number

print the factorial
terminate the program
"""

user_num = int(input("Please enter a positive integer: "))
print("You entered:", user_num)

total = 1

for i in range(1, user_num + 1):
    total *= i

print("The factorial of", user_num, "is", total)
print("Finished")