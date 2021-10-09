"""
Pseudocode:

prompt the user for a number n

for each number i in the range 0 to n-1:

    initialise two total variables for the 2*i and i factorials = 1

    for each number in the range 1 to 2*i:
        multiply the n total by the number

    for each number in the range 1 to i:
        multiply the n total by the number

    calculate the Catalan numbers using (2i)! / ( i! ** 2 * (i-1)! )
    print out the catalan number

terminate the program
"""

n = int(input("Please enter a number: "))
print("Catalan Numbers:")

for i in range(0, n):

    two_n_total, n_total = 1, 1

    for j in range(1, 2 * i + 1):
        two_n_total *= j

    for k in range(1, i + 1):
        n_total *= k

    catalan = two_n_total / (n_total ** 2 * (i + 1))

    print(catalan)

print("Finished")