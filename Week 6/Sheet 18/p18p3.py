"""
Pseudo Code:
def function codeChecker(s):
    initialise a counter for the number of times the word code appears and set this = 0
    for each element i in the range 0 to length of s - 4:
        if s[i:i+2] is equal to "co" and s[i+3] is equal to "e" and lowercase s[i+2] is in the alphabet then:
            increment the code counter

    return the code counter

Prompt the user for a string
Print the output of codeChecker(string)
"""

def codeChecker(s):
    """Function that counts how many times the word code appears in a string, where the letter d can vary

    Accepts a formal parameter s which is presumed to be a string
    Iterates through the string, and isolates a few sections of the string
    Checks to see if the slice is the word code, where the d can vary, and if it is, increments the code counter
    Returns the number of instances of the word code
    """
    code_counter = 0
    for i in range(len(s) - 3):
        if (s[i:i+2] == "co") and (s[i+2].lower() in "abcdefghijklmnopqrstuvwxyz") and (s[i+3] == "e"):
            code_counter += 1

    return code_counter

user_string = input("Please enter a string: ")
print("The word \"code\", where the d can be any letter, appears", codeChecker(user_string), "times in the string:", user_string)

print("Finished!")