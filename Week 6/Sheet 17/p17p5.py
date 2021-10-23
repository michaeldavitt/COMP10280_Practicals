# Copied verbatum from the lecture notes (Lecture 17 page 18-20) and sheet 17 Q5

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

    def recursive function isPal(s):
        if the length of the string s is less than or equal to 1 then:
            return True

        else:
            check if the first and last element in s are equal
            if these elements are equal, call the function isPal with s less the first and last string
            return True if the above conditions are met

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
        Returns False otherwise.
        Recursive function.
        Has print statements to trace its operation."""
        print("isPal function called with argument", s)
        if len(s) <= 1:
            # A palindrome of length 0 or 1 is a palindrome
            print("About to return True from isPal from the base case")
            return True
        else:
            # Compare the first and the last letters and check the remainder of the string
            result = s[0] == s[-1] and isPal(s[1:-1])
            print ("About to return result", result, "from isPal with argument", s)
        return result

    
    return isPal(toChars(s))


str = input("Enter a string (empty string to exit): ")
while str != "":
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")

print("Finished!")