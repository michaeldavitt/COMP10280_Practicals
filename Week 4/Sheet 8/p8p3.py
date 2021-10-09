"""
Pseudocode:

prompt the user for a number
read the number

initialise a counter variable = 0
initialise a limit variable = 20

while counter is less than or equal to limit:
    print the counter and the counter multiplied by 6
    increment counter

Terminate the program
"""

user_num = int(input("Please enter a number: "))
print("You entered:", user_num)

count = 0
lim = 20

print("Times", user_num, "Table")

while count <= lim:
    print(count, "\t\t", count * user_num)
    count += 1

print("Finished")