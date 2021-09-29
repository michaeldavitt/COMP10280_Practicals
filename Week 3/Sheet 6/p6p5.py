# p6p5 - Password checker program

"""
Pseudocode

Create password
Get password from user

if user password is equal to stored password:
    print "You have successfully logged in"

else:
    print "Sorry, the password is wrong"
    
    Create a counter variable to track the number of password guesses
    Initialise counter variable = 0

    Create a variable for passing/failing the test
    Initialise the passing/failing variable with True

    While the counter is less than 3:
        Get password from user
        Increment counter
        If the user's password is not equal to the stored password:
            Set the passing/failing variable to False
        

    if the passing/failing variable is true:
        print "You have successfully logged in"
    
    else:
        print "You have been denied access"
"""

stored_pass = "password"
user_pass = input("Please type a password: ")

if user_pass == stored_pass:
    print("You have successfully logged in")

else:
    print("Sorry, the password is wrong")
    guesses = 0
    
    pass_fail = True

    while guesses < 3:
        user_pass = input("Please type a password: ")
        guesses += 1

        if user_pass != stored_pass:
            pass_fail = False

    if pass_fail:
        print("You have successfully logged in")

    else:
        print("You have been denied access")
