# p5p4 - Program checks if a number is in one of many specified ranges

user_num = int(input("Please type an integer: "))

if user_num == 0:
    print(user_num, "is 0")

elif 0 < user_num <= 20:
    print(user_num, "is greater than 0 and less than or equal to 20")

elif 20 < user_num <= 40:
    print(user_num, "is greater than 20 and less than or equal to 40")

elif 40 < user_num <= 60:
    print(user_num, "is greater than 40 and less than or equal to 60")

elif 60 < user_num <= 80:
    print(user_num, "is greater than 60 and less than or equal to 80")

elif 80 < user_num <= 100:
    print(user_num, "is greater than 80 and less than or equal to 100")

elif user_num > 100:
    print(user_num, "is greater than 100")

else:
    print(user_num, "is less than 0")

print("Finished")
