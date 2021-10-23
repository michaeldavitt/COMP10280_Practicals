"""
Pseudo Code:
function perfectChecker(num):
    initialise divisors
    for i from 1 to (num-1) do:
        if num1 mod i == 0 then:
            add i to divisors
    
    initialise a counter = 0
    for j in divisors do:
        add j to the counter

    if counter is equal to num then:
        return True
    
    else:
        return False


Prompt the user for a number x
Read x

If x is positive then:
    for each i in the range 1 to x do:
        if perfectChecker(i) then:
            print i

Terminate the program
"""

def perfectChecker(num):
    """Function that checks if a given number is a perfect number
    
    First, the function gets a list of proper factors
    Then, the proper factors are summed and the result of the summation is compared with the formal paramter
    If the sum of the proper factors is equal to the formal parameter, the function returns true, else it returns false
    """
    divisors = ()
    for i in range(1, num):
        if num % i == 0:
            divisors += (i,)
            
    counter = 0
    for j in divisors:
        counter += j

    if counter == num:
        return True

    else:
        return False

user_num = int(input("Please enter a positive integer (enter a non-positive integer to exit): "))
print("You have entered", user_num)

if user_num >= 1:
    print("Perfect Numbers:")
    
    for i in range(1, user_num + 1):
        if perfectChecker(i):
            print(i)

print("Finished")