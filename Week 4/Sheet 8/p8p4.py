"""
Pseudocode:
prompt the user for a number
initialise all counters

while user number is non-negative:
    read the number

    if number is 0 then:
        print "number is 0"
        increment "number is 0" counter

    else if number is greater than 0 and less than or equal to 20 then:
        print "number is greater than 0 and less than or equal to 20"
        incremenet "number is greater than 0 and less than or equal to 20" counter

    do 4 more else if statements for the next four ranges, performing similar operations each time

    else:
        print "number is greater than 100"
        increment "greater than 100" counter

    prompt the user for a number

print out the number of numbers in each range
terminate the program
"""

user_num = int(input("Please enter a number (enter a negative number to exit): "))
zero = 0
zero_to_twenty = 0
twenty_to_forty = 0
forty_to_sixty = 0
sixty_to_eighty = 0
eighty_to_hundred = 0
plus_hundred = 0

while user_num >= 0:
    print("You have entered:", user_num)

    if user_num == 0:
        print(user_num, "is equal to 0")
        zero += 1

    elif 0 < user_num <= 20:
        print(user_num, "is greater than 0 and less than or equal to 20")
        zero_to_twenty += 1

    elif 20 < user_num <= 40:
        print(user_num, "is greater than 20 and less than or equal to 40")
        twenty_to_forty += 1

    elif 40 < user_num <= 60:
        print(user_num, "is greater than 40 and less than or equal to 60")
        forty_to_sixty += 1

    elif 60 < user_num <= 80:
        print(user_num, "is greater than 60 and less than or equal to 80")
        sixty_to_eighty += 1

    elif 80 < user_num <= 100:
        print(user_num, "is greater than 80 and less than or equal to 100")
        eighty_to_hundred += 1

    else:
        print(user_num, "is greater than 100")
        plus_hundred += 1

    user_num = int(input("Please enter a number (enter a negative number to exit): "))

print("Negative number entered!")
print("Showing Analysis:")
print()
print("Numbers equal to 0:", zero)
print("Numbers greater than 0 and less than or equal to 20:", zero_to_twenty)
print("Numbers greater than 20 and less than or equal to 40:", twenty_to_forty)
print("Numbers greater than 40 and less than or equal to 60:", forty_to_sixty)
print("Numbers greater than 60 and less than or equal to 80:", sixty_to_eighty)
print("Numbers greater than 80 and less than or equal to 100:", eighty_to_hundred)
print("Numbers greater than 100:", plus_hundred)

print("Finished")