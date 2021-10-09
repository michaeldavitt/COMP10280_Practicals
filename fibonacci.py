"""
Fibonacci Series:
Rules: f(n) = f(1) if n = 1, f(1), f(2) if n = 2, f(n-1) + f(n-2) if n > 2

Prompt the user for an integer

Initialise 2 variables, representing the first 2 numbers in the fibonacci sequence

if the integer is not positive then:
    Print The integer must be positive (greater than 0)

Else:
    If n is 1 then:
        print "sequence = f(1)"

    Else if n is 2 then:
        print "sequence = f(1), f(2)"
    
    else:
        Initialise a variable position = 3
        Initialise operand_1 = f(2) and operand_2 = f(1)

        while position is less than or equal to n:
            calculate next number in fibonacci sequence by adding operand_1 and operand_2
            print the next fibonacci number
            change operand_1 to the fibonacci number and change operand_2 to operand_1's previous value

Terminate the program
"""

n = int(input("Please enter a positive integer (a whole number > 0): "))

f_1 = 1
f_2 = 1

if n <= 0:
    print("The integer must be positive")

else:
    if n == 1:
        print("f(n=", n, "): ", f_1, sep="", end="")

    elif n == 2:
        print("f(n=", n, "): ", f_1, ", ", f_2, sep="", end="")

    else:
        print("f(n=", n, "): ", f_1, ", ", f_2, sep="", end="")
        operand_n_minus_1 = f_2
        operand_n_minus_2 = f_1
        current_position = 3

        while current_position <= n:
            fib = operand_n_minus_1 + operand_n_minus_2
            print(", ", fib, sep="", end="")
            operand_n_minus_1, operand_n_minus_2 = fib, operand_n_minus_1
            current_position += 1

    print()

print("Finished")


"""
Factorial:
Rules: f(n) = 1 when n = 0, f(n) = 1 when n = 1, f(n) = n * (n-1) ... * 1 when n > 1

Prompt the user for an integer

If the integer is less than 0 then:
    Print "The integer must be non-negative

Else:
    If n is 0 or n is 1 then:
        print "Factorial of n is 1"
    Else:
        factorial = 1
        position = 2

        while position is less than or equal to n:
            factorial = factorial * position
            increment position

        print "Factorial of n is factorial"

Terminate the program
"""

n = int(input("Please type a non-negative integer: "))

if n <= 0:
    print("Integer must be non-negative")

else:
    if (n == 0) or (n == 1):
        print("Factorial =", 1)

    else:
        factorial = 1
        current_position = 2

        while current_position <= n:
            factorial *= current_position
            current_position += 1

        print("Factorial =", factorial)

print("Finished")