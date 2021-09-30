# p7p3 - Program that prints the square of first 50 integers

"""
Pseudocode:

create a variable for the limit
set limit to 50

create a variable to count the number of iterations of the while loop
set the counter to 1

while the counter is less than or equal to the limit:
    print the counter and the square of the counter
    increment counter

"""

lim = 50
counter = 1

while counter <= lim:
    print("integer =", counter, "; square of integer =", counter ** 2)
    counter += 1

print("Finished")
