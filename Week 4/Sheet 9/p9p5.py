"""
Pseudocode:

prompt the user for 2 numbers, n and k
read the numbers

initialise three total variables for the n, k and n-k factorials = 1

for each number in the range 1 to n:
    multiply the n total by the number

do two more for loops like this, replacing n with k and n-k respectively

calculate the combinations using n! / ( k! * (n-k)! )
print out the combinations

terminate the program
"""

n = int(input("Please enter the number of possible toppings: "))
k = int(input("Please enter the number of toppings offered on a standard pizza: "))

n_total, k_total, n_less_k_total = 1, 1, 1

for i in range(1, n + 1):
    n_total *= i

for j in range(1, k + 1):
    k_total *= j

for k in range(1, n - k + 1):
    n_less_k_total *= k

combinations = n_total / (k_total * n_less_k_total)

print("The total number of different combinations of toppings is", combinations)
print("Finished")
