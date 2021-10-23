"""
Pseudo Code:
def function digit_converter(number, base):
    create an empty list for the new digit we are creating
    create a letter list with the letters A - F
    while number is not equal to 0 do:
        store the result of number modulus base to a variable remainder
        if remainder is greater than 9:
            set remainder to the element of letters at position [remainder - 10]
        
        insert the remainder into position 0 in the new digit list
        set the number equal to the number divided by the base

    join the elements in the list using the .join method
    return the joined list

Prompt the user for a number in base 10
Prompt the user for a base
Print(digit_converter(number, base))
Terminate the program
"""

def digit_converter(number, base):
    """ Function to convert a given number in base 10 to a base specified by the user 
    
    Assumes that the base is less than or equal to 16
    Assumes that the number is positive
    While the number is not equal to 0, collect the remainder of number % base and add to a list
    Uses letters from A to F for hexadecimal representation when the above result is greater than 9
    Keep dividing the number by the base until the result is 0
    """
    new_digit = []
    letters = "ABCDEF"
    while number != 0:
        remainder = number % base
        if remainder > 9:
            remainder = letters[remainder - 10]
        
        new_digit.insert(0, str(remainder))
        number //= base
    
    joined_digit = "".join(new_digit)
    return joined_digit

user_num = int(input("Please enter a number in base 10: "))
user_base = int(input("Please enter a base: "))
print(user_num, "in base", user_base, ":", digit_converter(user_num, user_base))

print("Finished!")