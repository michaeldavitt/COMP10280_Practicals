# Taken verbatum from the notes (Lecture 15 page 9)

# Program to print out the largest of two numbers entered by the user
# Uses two functions: max and print_max

"""
Pseudo Code:
Define a print max function which takes no formal parameters:
    Define a max function which takes two formal parameters a and b:
        if a is greater than b then:
            return a

        else:
            return b

    Prompt the user for two numbers
    print "The largest of the two numbers is" followed by the output of the max function call with actual arguments = two user numbers

    Add an empty return to signify that the function does not return anything

Call the print max function with no actual arguments.
Terminate the program
"""

def print_max():
    """Function that prints out the largest of two numbers
    Uses the function max to find the largest"""

    def max(a, b):
        """Function that returns the largest of its two arguments"""
        if a > b:
            return a
        else:
            return b

    # Prompt the user for two numbers
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    print("The largest of", number1, "and", number2, "is", max(number1, number2))
    
    return

print_max()
print("Finished")