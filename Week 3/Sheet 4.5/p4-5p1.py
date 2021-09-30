# p4-5p1 - Euro to Dollars Exchange Rate Program (exchange rate: €1 = $1.17 as at 28/09/2021)

exchange_rate = 1.17

user_currency = float(input("Please type the amount of € you wish to convert to $: € "))
print("You have input: €", user_currency)

if user_currency >= 0:
    new_currency = user_currency * exchange_rate
    print("€", user_currency, " = $", new_currency)

else:
    print("Amount must be >= 0. Please try again.")

print("Finished")