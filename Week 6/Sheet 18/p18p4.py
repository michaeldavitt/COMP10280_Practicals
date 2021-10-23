"""
Pseudo Code:
def endChecker(s1, s2):
    Check which string is the longest
    Assign the longest string to the variable long_string and the other to the variable short_string
    Convert both variables above to lowercase
    If the short string is equal to the long_string[len(long_string) - len(short_string):] then:
        return true
    Else:
        return false

Prompt the user for two strings
Print the result of endChecker(string 1, string 2)
Terminate the program
"""

def endChecker(s1, s2):
    """Function that checks if a shorter string is at the end of a longer string
    
    Assumes that both inputs are strings
    Ignores case differences
    Returns True if the shorter string appears at the end of the longer one and False otherwise
    """
    if len(s1) > len(s2):
        long, short = s1, s2
    else:
        long, short = s2, s1

    long, short = long.lower(), short.lower()

    if short == long[len(long) - len(short):]:
        return True

    else:
        return False

first_string = input("Please enter a string: ")
second_string = input("Please enter a string: ")
print(endChecker(first_string, second_string))
print("Finished!")