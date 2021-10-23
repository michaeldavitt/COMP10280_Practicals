"""
Pesudo Code:
def function to_decimal(string, base):
    create a list of letters from A to F
    set power = length of the string
    initialise a variable for the digit = 0
    for i in the number:
        if i is a letter:
            set i equal to the index of i in the letters list + 10

        convert i to an integer
        multiply i by the power variable
        add the result to the digit variable
        decrease the power variable by 1

    return the digit variable
    
        
Prompt the user for a string of digits
Prompt the user for a base
Print the result of to_decimal(string, base)
"""

def to_decimal(string, base):
    """Function that converts a string in a given base to a decimal number
    
    Assumes the base is less than or equal to 16
    """
    letters = "abcdefABCDEF"
    power = len(string) - 1
    decimal_digit = 0

    for num in string:
        if num in letters:
            num = letters.index(num.lower()) + 10

        num = int(num)
        decimal_digit += num * (base ** power)
        power -= 1

    return decimal_digit

user_str = input("Please enter a string representing a number: ")
user_base = int(input("Please enter a base: "))
print(user_str, "in base 10:", to_decimal(user_str, user_base))

print("Finished!")