# p5p5 - Program that checks whether an entered string is the name of a town

user_place_name = input("Please enter the name of a town or city: ")

if user_place_name == "Dublin":
    print("You entered", user_place_name + ". " + user_place_name, "is in Leinster")

elif user_place_name == "Belfast":
    print("You entered", user_place_name + ". " + user_place_name, "is in Ulster")

elif user_place_name == "Cork":
    print("You entered", user_place_name + ". " + user_place_name, "is in Munster")

elif user_place_name == "Limerick":
    print("You entered", user_place_name + ". " + user_place_name, "is in Munster")

elif user_place_name == "Derry":
    print("You entered", user_place_name + ". " + user_place_name, "is in Ulster")

elif user_place_name == "Galway":
    print("You entered", user_place_name + ". " + user_place_name, "is in Connacht")

elif user_place_name == "Lisburn":
    print("You entered", user_place_name + ". " + user_place_name, "is in Ulster")

elif user_place_name == "Kilkenny":
    print("You entered", user_place_name + ". " + user_place_name, "is in Leinster")

elif user_place_name == "Waterford":
    print("You entered", user_place_name + ". " + user_place_name, "is in Munster")

elif user_place_name == "Sligo":
    print("You entered", user_place_name + ". " + user_place_name, "is in Connacht")

else:
    print("Sorry, I didn't recognise that name.")

print("Finished")
