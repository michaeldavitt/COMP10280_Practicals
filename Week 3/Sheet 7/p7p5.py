# p7p5 - Sums integers in the range 1 - 10000 that are divisible by 3 or 5

"""
Pseudocode:

create a variable for the limit
set limit to 10000

create a variable to keep track of the sum total
set the total to 0

create a variable to count the number of iterations of the while loop
set the counter to 1

while counter is less than or equal to the limit:
    if counter is divisible by 3 or is divisible by 5:
        add counter to total

    increment counter

print total
"""

lim = 5000
total = 0
counter = 1

while counter <= lim:
    if counter % 3 == 0 or counter % 5 == 0:
        total += counter

    counter += 1

print(total)
