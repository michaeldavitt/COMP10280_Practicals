# p4p1 - currency converter, using the EUR -> USD rate as at 21/09/2021

amount_in_euros = float(input("Please type the euro amount you wish to convert: €"))
eur_to_usd = 1.17
amount_in_usd = amount_in_euros * eur_to_usd
print("€", amount_in_euros, "= $", amount_in_usd)
