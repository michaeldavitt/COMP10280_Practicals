"""
Pseudocode:
Introduce the program

Prompt user for an integer
Read the user integer

If user_integer is negative:
    print an error message

Else:
    Initialise all divisible counters (4, 5, 7 and 13) = 0
    Initialise a counter variable = 1

    While the counter is less than or equal to user_integer:
        If counter is divisible by 4:
            increment divisible by 4 counter
        
        If counter is divisible by 5:
            increment divisible by 5 counter
        
        If counter is divisible by 7:
            increment divisible by 7 counter

        If counter is divisible by 13:
            increment divisible by 13 counter
        
        increment counter variable

    print all divisible statements (number of numbers up to and including int divisible by 4 = ...)

Terminate the program
"""

print("Program to calculate the number of integers evenly divisible by 4, 5, 7 and 13")

user_num = int(input("Enter a non-negative integer: "))
print("You entered:", user_num)

if user_num < 0:
    print("Number entered should be >= 0")

else:
    div_by_4, div_by_5, div_by_7, div_by_13 = 0, 0, 0, 0

    counter = 1

    while counter <= user_num:
        if counter % 4 == 0:
            div_by_4 += 1

        if counter % 5 == 0:
            div_by_5 += 1

        if counter % 7 == 0:
            div_by_7 += 1

        if counter % 13 == 0:
            div_by_13 += 1

        counter += 1


    print("Number of numbers up to and including", user_num, "evenly divisible by 4:", div_by_4)
    print("Number of numbers up to and including", user_num, "evenly divisible by 5:", div_by_5)
    print("Number of numbers up to and including", user_num, "evenly divisible by 7:", div_by_7)
    print("Number of numbers up to and including", user_num, "evenly divisible by 13:", div_by_13)

print("Finished!")