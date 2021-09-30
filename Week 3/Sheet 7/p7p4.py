# p7p4 - Summing the first 5000 integers

"""
Pseudocode:

create a variable for the limit
set limit to 5000

create a variable to keep track of the sum total
set the total to 0

create a variable to count the number of iterations of the while loop
set the counter to 1

while counter is less than or equal to the limit:
    add counter to total
    increment counter

print total
"""

lim = 5000
total = 0
counter = 1

while counter <= lim:
    total += counter
    counter += 1

print("The sum of the first 5000 integers is:", total)

print("Finished")
