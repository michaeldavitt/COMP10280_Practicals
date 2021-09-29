# p7p2 - Leap Year Program (Wikipedia algorithm)

"""
Pseudocode:
Prompt the user for a year
Read the year

if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""

year = int(input("Please enter a year"))
print("Year entered:", year)

if year % 4 != 0:
    print(year, "is a common year")

elif year % 100 != 0:
    print(year, "is a leap year")

elif year % 400 != 0:
    print(year, "is a common year")

else:
    print(year, "is a leap year")
