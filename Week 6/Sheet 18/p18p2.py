"""
Pseudo Code:
def function codeChecker(s):
    initialise a counter for the number of times the word code appears and set this = 0
    for each element i in the range 0 to length of s - 4:
        if s[i:i+4] is equal to "code" then:
            increment the code counter

    return the code counter

Prompt the user for a string
Print the output of codeChecker(string)
"""

def codeChecker(s):
    """Function that counts how many times the word code appears in a string

    Accepts a formal parameter s which is presumed to be a string
    Iterates through the string, each time creating a slice of the string with four elements
    If this slice is equal to the word code, the number of instances of the word code increases by 1
    Returns the number of instances of the word code
    """
    code_counter = 0
    for i in range(len(s) - 3):
        if s[i:i+4] == "code":
            code_counter += 1

    return code_counter

user_string = input("Please enter a string: ")
print("The word \"code\" appears", codeChecker(user_string), "times in the string:", user_string)

print("Finished!")
