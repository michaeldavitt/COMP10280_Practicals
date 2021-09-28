# p6p3 - Program that comments on a user's name

"""
Pseudocode:

Get a name from the user

If name is my name:
    print "That's a cool name"

Else if name is "Mickey Mouse" or "Spongebob Squarepants":
    print "I don't think that's you're name"

Else:
    You have a nice name

"""

user_name = input("Please enter a name: ")

if user_name == "Michael Davitt":
    print("That's a cool name!")

elif user_name == "Mickey Mouse" or user_name == "Spongebob Squarepants":
    print("I don't think that is your name.")

else:
    print("You have a nice name.")

print("Finished")
