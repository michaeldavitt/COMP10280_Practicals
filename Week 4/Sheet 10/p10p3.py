"""
Pseudocode:

prompt the user for a string

while the string is not an empty string:
    read the string

    initialise a vowel counter = 0

    for each letter in the string:
        if the letter is a vowel:
            increment the vowel counter

    print the vowel counter

    prompt the user for a string

terminate the program
"""

user_str = input("Please enter a string: ")

while user_str != "":
    print("You entered", user_str)

    vowel_count = 0

    for letter in user_str:
        if letter == "a" or letter =="e" or letter == "i" or letter == "o" or letter == "u":
            vowel_count += 1
        
    print("Number of vowels in", user_str, ":", vowel_count)

    user_str = input("Please enter a string: ")

print("Finished")