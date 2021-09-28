# p4-5p3 - tax calculator

# define initial variables
gross_income = float(input("Gross Income: € "))
print("You input: €", gross_income)
low_tax_rate = 0.23
high_tax_rate = 0.41
tax_band = 0.6

if gross_income >= 0:
    # calculate the gross income amount in each tax bracket (60/40 split)
    low_rate_income = gross_income * tax_band
    high_rate_income = gross_income * (1 - tax_band)

    # calculate taxes due at low and high rate
    tax_low_rate = low_rate_income * low_tax_rate
    tax_high_rate = high_rate_income * high_tax_rate

    # calculate total tax and net income
    total_tax_due = tax_low_rate + tax_high_rate
    net_income = gross_income - total_tax_due

    # output results
    print("Gross Income: €", gross_income)
    print("Taxes Due at Low Rate: €", tax_low_rate)
    print("Taxes Due at High Rate: €", tax_high_rate)
    print("Total Taxes Due: €", total_tax_due)
    print("Net Income: €", net_income)

else:
    print("Amount of income must be >= 0. Please try again.")

print("Finished")
