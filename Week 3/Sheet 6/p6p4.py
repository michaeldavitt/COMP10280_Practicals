# p6p4 - Password checking program

"""
Pseudocode:

Create a password variable
Initialised a user password

Create a counter variable to track the number of password guesses
Initialise counter variable = 0

While the user's password does not equal the stored password and the counter is less than 3:
    Get password from user
    Increment counter
    If the user's password is equal to the stored password:
        print "You have successfully logged in"
    
    else:
        print "Incorrect password"
        Get the user to enter a different password
    

if user password is not equal to stored password:
    print "You have been denied access"
"""

stored_pass = "password"
user_pass = ""

guesses = 0

while (user_pass != stored_pass) and guesses < 3:
    user_pass = input("Please type in a password: ")
    guesses += 1
    if user_pass == stored_pass:
        print("You have successfully logged in")

    else:
        print("Incorrect password")

if user_pass != stored_pass:
    print("You have been denied access")

print("Finished")
