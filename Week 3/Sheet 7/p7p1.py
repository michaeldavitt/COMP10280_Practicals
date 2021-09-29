# p7p1 - Leap year checker

"""
Pseudocode

Prompt the user for a year
Read the year
if year ≥ 0 then
    if (year mod 4 = 0 and year mod 100 != 0) or year mod 400 = 0 then
        Print(“Year is a leap year”)
    else
        Print(“Year is not a leap year”)
else
    Tell the user that the year must be ≥ 0
Program finishes
"""

year = int(input("Please enter a year"))
print("Year entered:", year)

if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "is a leap year.")

    else:
        print(year, "is not a leap year")

else:
    print("Year must be greater than 0")

print("Finished")
