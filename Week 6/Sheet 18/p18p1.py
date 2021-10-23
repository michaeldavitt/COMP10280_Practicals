# Copied verbatum from the lecture notes (Lecture 17 page 18-20)

"""
Pseudo Code:
def function isPalindrome(s):
    def function toChars(s):
        convert all letters in s to lowercase with the .lower method
        initialise an empty string to store letters called letterstring

        for each letter in s do:
            if the letter is a letter then:
                add letter to letterstring

        return letterstring

    def function isPal(s):
        initialise a boolean variable = True
        for i in the range 0 to length of s - 1 do:
            if s[i] is not equal to s[length os s - i]:
                set the boolean variable to False

        return the boolean variable

    return the result of isPal(toChars(s))

Prompt the user for a string
while the string is not equal to the empty string do:
    Check if the string is a palindrome with isPalindrome(string)
    
    If the string is a palindrome then:
        Print that it is a palindrome
    
    else:
        Print that it is not a palindrome

    Prompt the user for another string

Terminate the program
"""



# Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered
def isPalindrome(s):
    """Checks whether the string s is a palindrome
    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""
    
    def toChars(s):
        """Converts a string to lowercase and removes non-letters
        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letters."""
        # First of all, convert uppercase letters to lowercase
        s = s.lower()
        # Start with an empty string
        letterstring = ''
        # Go through s...
        for c in s:
            # ... and add the character to the string if it is a letter
            if c in "abcdefghijklmnopqrstuvwxyz":
                letterstring += c
        return letterstring

    def isPal(s):
        """Checks whether the string s is a palindrome
        
        Assumes that s is a str with only lowercase letters and no non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise."""
        pass_fail = True
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                pass_fail = False

        return pass_fail
    
    return isPal(toChars(s))


str = input("Enter a string (empty string to exit): ")
while str != "":
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")

print("Finished!")