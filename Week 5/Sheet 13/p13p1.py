# Taken verbatum from the notes (Lecture 15 page 4)

"""
Pseudo Code:
Define the function max taking formal parameters a and b:
    if a is greater than b:
        return a

    else:
        return b

Prompt the user for two floating-point numbers
Call the max function and assign the output to the variable "biggest". Actual parameters = the two user numbers
print "The largest of the two numbers is: biggest"
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

biggest = max(number1, number2)
print("The largest of", number1, "and", number2, "is:", biggest)
print("Finished!")