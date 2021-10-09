"""
Pseudocode:

prompt the user for an integer

while user integer is greater than or equal to 0:
    initialise the variables f(n-2) and f(n-1) to be 0 and 1 respectively

    if user integer equal to 0 then:
        print "Error, integer should be greater than 0"

    elif user integer is equal to 1:
        print Fibonacci Series: 0

    else:
        print Fibonacci Series: f(n-2), f(n-1)

        for each number in the range 2 to user integer (user integer not included):
            Assign f(n-1) to the variable f(n-2) and assign f(n-1) + f(n-2) to the variable f(n-1) using multiple assignment
            print f(n-1)

    print a new line

    prompt the user for a number

terminate the program
"""

user_int = int(input("Please enter the number of terms you want to calculate (enter a negative number to exit): "))

while user_int >= 0:
    f_0, f_1 = 0, 1

    if user_int <= 0:
        print("Error: Number entered was less than or equal to 0", end="")

    elif user_int == 1:
        print("Series is:", f_0, end="")

    else:
        print("Series is: ", f_0, ", ", f_1, sep="", end="")

        for i in range(2, user_int):
            f_0, f_1 = f_1, f_0 + f_1
            print(",", f_1,  end="")

    print()

    user_int = int(input("Please enter the number of terms you want to calculate (enter a negative number to exit): "))

print("Finished")