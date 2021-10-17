# Taken verbatum from the notes (Lecture 15 page 5)

"""
Pseudo Code:
Define the function max taking formal parameters a and b:
    if a is greater than b:
        return a

    else:
        return b

Prompt the user for two floating-point numbers
Print "The largest of the two numbers is" followed by the result of the max function call with the two user numbers as the actual arguments
Terminate the program
"""

def max(a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:
        return b


# Prompt the user for two numbers
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
print("The largest of", number1, "and", number2, "is:", max(number1, number2))
print("Finished!")