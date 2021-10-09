"""
Pseudocode:
Introduce the program

Prompt user for a day

while day is positive:
    Read the day
    
    if day is between 1 and 31 inclusive:
        print day is day August 2021
    
    else if day is between 32 and 61 inclusive:
        print day is (day - 31) September 2021

    etc...
    
    else if day is between 335 and 365 inclusive:
        print day is (day - 334) July 2022

    else:
        print day is not in academic year

    prompt user for a day

Terminate the program
"""

print("Program to calculate the day, month and year in the 2021-2022 academic year of a given day.")
print()

day = int(input("Enter the day for which you want to find the date (an integer): "))

while day > 0:
    print("You entered:", day)

    if 1 <= day <= 31:
        print("Day number", day, "is", day, "August 2021")

    elif 32 <= day <= 61:
        print("Day number", day, "is", (day - 31), "September 2021")

    elif 62 <= day <= 92:
        print("Day number", day, "is", (day - 61), "October 2021")

    elif 93 <= day <= 122:
        print("Day number", day, "is", (day - 92), "November 2021")

    elif 123 <= day <= 153:
        print("Day number", day, "is", (day - 122), "December 2021")

    elif 154 <= day <= 184:
        print("Day number", day, "is", (day - 153), "January 2022")

    elif 185 <= day <= 212:
        print("Day number", day, "is", (day - 184), "February 2022")

    elif 213 <= day <= 243:
        print("Day number", day, "is", (day - 212), "March 2022")

    elif 244 <= day <= 273:
        print("Day number", day, "is", (day - 243), "April 2022")

    elif 274 <= day <= 304:
        print("Day number", day, "is", (day - 273), "May 2022")

    elif 305 <= day <= 334:
        print("Day number", day, "is", (day - 304), "June 2022")

    elif 335 <= day <= 365:
        print("Day number", day, "is", (day - 334), "July 2022")

    else:
        print("Day number", day, "is not in the 2021-2022 academic year!")

    day = int(input("Enter the day for which you want to find the date (an integer): "))

print("Finished!")