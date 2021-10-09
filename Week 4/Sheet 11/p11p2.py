"""
Pseudocode:
initialise the variables f(n-2) and f(n-1) to be 0 and 1 respectively

prompt the user for an integer

if user integer is less or equal to 0 then:
    print "Error, integer should be greater than 0"

elif user integer is equal to 1:
    print Fibonacci Series: 0

else:
    print Fibonacci Series: f(n-2), f(n-1)

    initialise position variable = 3

    while position is less than or equal to the user integer:
        Assign f(n-1) to the variable f(n-2) and assign f(n-1) + f(n-2) to the variable f(n-1) using multiple assignment
        print f(n-1)
        increment position variable

print a new line
terminate the program
"""
f_0, f_1 = 0, 1

user_int = int(input("Please enter the number of terms you want to calculate (an int > 0): "))

if user_int <= 0:
    print("Error: Number entered was less than or equal to 0", end="")

elif user_int == 1:
    print("Series is:", f_0, end="")

else:
    print("Series is: ", f_0, ", ", f_1, sep="", end="")

    pos = 3

    while pos <= user_int:
        f_0, f_1 = f_1, f_0 + f_1
        print(",", f_1,  end="")
        pos += 1

print()
print("Finished")