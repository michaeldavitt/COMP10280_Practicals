"""
Pseudocode:

prompt the user for a positive integer
read the integer

initialise a counter variable = 0
initialise a total variable = 0

while the counter is less than or equal to the user number:
    add counter to total
    increment counter

print the total
terminate the program
"""

user_num = int(input("Please enter a positive integer: "))
print("You have entered:", user_num)

count = 0
total = 0

while count <= user_num:
    total += count
    count += 1

print("The sum of the integers up to and including", user_num, "is", total)
print("Finished")