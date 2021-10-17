"""
Pseudocode:
Rules of Fibonnaci: 
Series = nothing if N=0 
Series = 0 if N=1 
Series = Fib(N-1) + Fib(N-2) if N > 1

Define a function fibonacci taking one formal parameter x, which is assumed to be non-negative:
    Initialise two variables, representing fib(n-2) and fib(n-1) to be 0 and 1 respectively

    if x is equal to 0 then:
        Print "Series:"

    else if x is equal to 1 then:
        Print "Series: fib(n-2)"

    else:
        Print "Series is: fib(n-2), fib(n-1)"

        initialise position variable = 3

        while position is less than or equal to x (loop will be skipped when x < 3) do the following:
            Assign f(n-1) + f(n-2) to the variable f(n-1) and assign f(n-1) to the variable f(n-2) using multiple assignment
            Print f(n-1)
            Increment the position variable

    print a new line



Prompt the user for an integer
Read the user integer

if the user integer is less than 0:
    print an error message

else:
    call the fibonnaci function, actual parameter = user integer.

Terminate the program
"""

def fibonnaci(x):
    """For an argument x, the function calculates x number of terms of the fibonnaci sequence
    
    The argument x is assumed to be non-negative
    """
    n_2, n_1 = 0, 1

    if x == 0:
        print("Series:", end="")

    elif x == 1:
        print("Series:", n_2, end="")

    else:
        print("Series: ", n_2, ", ", n_1, sep="", end="")
        
        pos = 3

        while pos <= x:
            n_2, n_1 = n_1, n_1 + n_2
            print(",", n_1, end="")
            pos += 1

    print()



user_num = int(input("Please enter an integer greater than or equal to 0: "))
print("You have entered:", user_num)

if user_num < 0:
    print("Error: Number must be greater than or equal to 0")

else:
    fibonnaci(user_num)

print("Finished")