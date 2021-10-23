"""
Pseudo Code:
define function xyzChecker(s):
    for each i in the range 0 to the length of the string s - 3 do:
        if s[i:i+3] is equal to xyz and (if i is equal to 0 or s[i-1] is not equal to ".") then:
    else:
        return False

Prompt the user for a string
Print the result of xyzChecker(user_string)
Terminate the program
"""

def xyzChecker(s):
    """Function that checks for the appearance of xyz in a string s

    Iterates through the string and checks to see if any of the slices = xyz
    Also checks that the slice is not proceeded by a full stop
    Returns True if the above conditions are satisfied, and False otherwise.
    """
    for i in range(len(s) - 2):
        if s[i:i+3] == "xyz" and (i==0 or s[i-1] != "."):
            return True

    else:
        return False

user_string = input("Please enter a string: ")
print(xyzChecker(user_string))
print("Finished!")