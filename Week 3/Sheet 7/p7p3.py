# p7p3 - Program that prints the square of first 50 integers

"""
Pseudocode:

create a variable for the limit
set limit to 50

create a variable to count the number of iterations of the while loop
set the counter to 1

while the counter is less than or equal to the limit:
    print(counter)
    print(counter squared)
    increment counter

"""

lim = 50
counter = 1

while counter <= lim:
    print(counter)
    print(counter ** 2)
    counter += 1

